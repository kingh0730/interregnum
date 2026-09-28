"""Render one story-reel shot from a JSON spec: layered stills and videos, camera move, parallax, particles,
light, grade. Deterministic; streams frames to ffmpeg.

usage: uv run tools/comp/reel.py <shot.json> [--preview]   (--preview: half res, every 4th frame to a contact sheet)

Spec (all keys optional except dur, out, layers):
{
  "dur": 6.0, "fps": 24, "out": "work/pilot/shots/03.mp4",
  "layers": [                       # bottom to top
    {"src": "a.png" | "b.mov" | "c.mp4",   # stills are cover-fitted to 16:9; videos play from their first frame
     "par": 1.0,                    # parallax factor: 0 = locked to frame, 1 = moves with camera, >1 = foreground
     "blend": "over|add|screen|multiply", "opacity": 1.0,
     "t0": 0, "t1": null, "fade_in": 0, "fade_out": 0,
     "fixed": false,                # true: ignore camera entirely (HUD / screen overlay)
     "drift": [dx, dy]}             # extra per-second slide in normalized frame units
  ],
  "camera": {"from": [cx, cy, zoom], "to": [cx, cy, zoom], "ease": "inout|in|out|linear|snap",
             "shake": 0.0, "shake_hz": 0.3,            # handheld drift, fraction of frame
             "punch": [[t, amount, decay_s], ...]},    # impact zoom punches
  "particles": [{"kind": "dust|ash|snow|embers|rain|sparks|motes", "n": 120, "seed": 1, "par": 1.2,
                 "wind": [0.02, 0.0], "size": 1.0, "opacity": 1.0, "color": [r,g,b] }],
  "light": {"flicker": 0.0, "flicker_hz": 9, "pulses": [[t, strength, decay_s, [r,g,b]], ...],
            "sweep": null},             # {"t0":, "t1":, "color":[..], "width":0.2, "angle":20}
  "grade": {"exposure": 0, "contrast": 1.0, "sat": 1.0, "lift": [0,0,0], "gain": [1,1,1],
            "bloom": 0.4, "vignette": 0.25, "grain": 0.018, "halation": 0.0, "chroma": 0.0},
  "letterbox": 2.39, "fade": {"in": 0, "out": 0, "color": [0,0,0]},
  "flash": [[t, dur, [r,g,b]], ...]     # hard frames of color (graphic cuts / impacts)
}
Coordinates: camera cx, cy are the frame centre in normalized source coords (0..1); zoom 1 = cover-fit.
"""
import json
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
W, H = 1920, 1080


def P(p):
    p = Path(p)
    return p if p.is_absolute() else ROOT / p


def ease(u, kind="inout"):
    u = float(np.clip(u, 0, 1))
    if kind == "linear":
        return u
    if kind == "in":
        return u * u * u
    if kind == "out":
        return 1 - (1 - u) ** 3
    if kind == "snap":  # fast start, long settle
        return 1 - (1 - u) ** 5
    return u * u * (3 - 2 * u) if u < 1 else 1.0


def smooth_noise(seed, t, hz):
    """Cheap band-limited noise in [-1, 1]: sum of incommensurate sines with seeded phases."""
    r = np.random.default_rng(seed)
    ph = r.uniform(0, 2 * np.pi, 4)
    f = hz * np.array([1.0, 1.618, 2.414, 3.303])
    a = np.array([0.55, 0.25, 0.13, 0.07])
    return float((a * np.sin(2 * np.pi * f * t + ph)).sum())


# ------------------------------------------------------------------ sources
class Still:
    def __init__(self, path):
        im = cv2.imread(str(P(path)), cv2.IMREAD_UNCHANGED)
        if im is None:
            raise FileNotFoundError(path)
        if im.ndim == 2:
            im = cv2.cvtColor(im, cv2.COLOR_GRAY2BGRA)
        if im.shape[2] == 3:
            im = np.dstack([im, np.full(im.shape[:2], 255, np.uint8)])
        im = im.astype(np.float32) / 255.0
        im[..., :3] = im[..., :3][..., ::-1] ** 2.2          # BGR -> linear RGB
        im[..., :3] *= im[..., 3:4]                            # premultiply
        self.img = im

    def get(self, t):
        return self.img


class Video:
    def __init__(self, path, fps):
        path = P(path)
        pr = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                             "stream=width,height", "-of", "csv=p=0", str(path)], capture_output=True, text=True)
        self.w, self.h = map(int, pr.stdout.strip().split(",")[:2])
        self.proc = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(path), "-r", str(fps), "-f", "rawvideo",
                                      "-pix_fmt", "rgba", "-"], stdout=subprocess.PIPE)
        self.idx, self.last = -1, None

    def get(self, t_local, fps):
        want = int(round(t_local * fps))
        while self.idx < want:
            buf = self.proc.stdout.read(self.w * self.h * 4)
            if len(buf) < self.w * self.h * 4:
                break  # hold last frame
            im = np.frombuffer(buf, np.uint8).reshape(self.h, self.w, 4).astype(np.float32) / 255.0
            im[..., :3] = im[..., :3] ** 2.2 * im[..., 3:4]
            self.last = im
            self.idx += 1
        return self.last


def cam_warp(img, cx, cy, zoom, opaque):
    """Map normalized source point (cx, cy) to frame centre, cover-fit scaled by zoom."""
    h, w = img.shape[:2]
    s = max(W / w, H / h) * zoom
    M = np.array([[s, 0, W / 2 - s * cx * w], [0, s, H / 2 - s * cy * h]], np.float32)
    interp = cv2.INTER_AREA if s < 0.7 else cv2.INTER_LINEAR
    return cv2.warpAffine(img, M, (W, H), flags=interp,
                          borderMode=cv2.BORDER_REPLICATE if opaque else cv2.BORDER_CONSTANT)


# ------------------------------------------------------------------ particles
KINDS = {
    #          count  size   speed(v)      color              blend  alpha
    "dust":   (1.0, (1, 3), (0.004, 0.01), (1.0, 0.9, 0.75), "add", 0.35),
    "motes":  (1.0, (2, 6), (0.002, 0.006), (1.0, 0.95, 0.85), "add", 0.25),
    "ash":    (1.0, (2, 5), (0.03, 0.07), (0.55, 0.55, 0.55), "over", 0.8),
    "snow":   (1.0, (2, 6), (0.04, 0.09), (0.95, 0.97, 1.0), "over", 0.85),
    "embers": (1.0, (1.5, 4), (-0.08, -0.03), (1.0, 0.45, 0.12), "add", 1.0),
    "sparks": (1.0, (1, 2.5), (-0.4, -0.15), (1.0, 0.75, 0.35), "add", 1.0),
    "rain":   (1.0, (1, 1.6), (0.9, 1.4), (0.75, 0.8, 0.9), "add", 0.22),
}


class Particles:
    def __init__(self, spec):
        self.kind = spec.get("kind", "dust")
        _, sz, sp, col, self.blend, alpha = KINDS[self.kind]
        n = int(spec.get("n", 120))
        r = np.random.default_rng(spec.get("seed", 1))
        self.x, self.y = r.uniform(0, 1, n), r.uniform(0, 1, n)
        self.z = r.uniform(0.4, 1.6, n)                   # per-particle depth: size, speed, parallax
        self.size = r.uniform(*sz, n) * spec.get("size", 1.0) * self.z
        self.vy = r.uniform(*sp, n) * self.z
        self.ph = r.uniform(0, 2 * np.pi, n)
        self.wind = np.array(spec.get("wind", [0.01, 0.0]))
        self.col = np.array(spec.get("color", col), np.float32) ** 2.2
        self.alpha = alpha * spec.get("opacity", 1.0)
        self.par = spec.get("par", 1.2)

    def draw(self, t, pan):
        wob = 0.006 * np.sin(t * 1.3 + self.ph) if self.kind in ("ash", "snow", "dust", "motes") else 0
        x = (self.x + (self.wind[0] + wob) * t * self.z - pan[0] * self.par * self.z) % 1.0
        y = (self.y + (self.vy + self.wind[1]) * t - pan[1] * self.par * self.z) % 1.0
        lay = np.zeros((H, W), np.float32)
        if self.kind == "rain":
            for xi, yi, zi in zip(x, y, self.z):
                p0 = (int(xi * W), int(yi * H))
                cv2.line(lay, p0, (int(p0[0] - 6 * zi), int(p0[1] - 60 * zi)), float(0.6 * zi), 1, cv2.LINE_AA)
        else:
            flick = 1.0
            for i, (xi, yi, si) in enumerate(zip(x, y, self.size)):
                if self.kind in ("embers", "sparks"):
                    flick = 0.55 + 0.45 * np.sin(t * 11 + self.ph[i] * 7)
                cv2.circle(lay, (int(xi * W * 16), int(yi * H * 16)), max(1, int(si * 16)), float(flick),
                           -1, cv2.LINE_AA, shift=4)
            lay = cv2.GaussianBlur(lay, (0, 0), 1.2 if self.kind != "motes" else 2.5)
        a = np.clip(lay * self.alpha, 0, 1)[..., None]
        return a * self.col, a, self.blend


# ------------------------------------------------------------------ finishing
def finish(img, g, t, frame, shape):
    img = img * 2 ** g.get("exposure", 0)
    b = g.get("bloom", 0.4)
    if b:
        sm = cv2.resize(img, (W // 4, H // 4), interpolation=cv2.INTER_AREA)
        br = np.clip(sm - 0.7, 0, None)
        bl = cv2.GaussianBlur(br, (0, 0), 5) * 0.6 + cv2.GaussianBlur(br, (0, 0), 20) * 0.6
        img = img + b * cv2.resize(bl, (W, H))
    hal = g.get("halation", 0)
    if hal:
        sm = cv2.resize(img, (W // 4, H // 4), interpolation=cv2.INTER_AREA)
        red = cv2.GaussianBlur(np.clip(sm - 0.8, 0, None), (0, 0), 8) * np.array([1.0, 0.25, 0.05], np.float32)
        img = img + hal * cv2.resize(red, (W, H))
    img = img / (1 + 0.15 * img)                                   # soft shoulder
    img = np.clip(img, 0, None) ** (1 / 2.2)                        # to display
    c = g.get("contrast", 1.0)
    img = (img - 0.5) * c + 0.5
    img = img * np.array(g.get("gain", [1, 1, 1]), np.float32) + np.array(g.get("lift", [0, 0, 0]), np.float32) * (1 - img)
    s = g.get("sat", 1.0)
    lum = (img * np.array([0.2126, 0.7152, 0.0722], np.float32)).sum(-1, keepdims=True)
    img = lum + (img - lum) * s
    ch = g.get("chroma", 0)
    if ch:
        k = int(ch)
        img[..., 0] = np.roll(img[..., 0], k, 1)
        img[..., 2] = np.roll(img[..., 2], -k, 1)
    v = g.get("vignette", 0.25)
    if v:
        img = img * shape["vig"](v)[..., None]
    gr = g.get("grain", 0.018)
    if gr:
        rng = np.random.default_rng(frame)
        n = rng.normal(0, gr, (H // 2, W // 2)).astype(np.float32)
        img = img + cv2.resize(n, (W, H))[..., None]
    return img


class Shot:
    def __init__(self, spec, preview=False):
        self.s = spec
        self.fps = spec.get("fps", 24)
        self.dur = spec["dur"]
        self.layers = []
        for L in spec["layers"]:
            src = L["src"]
            obj = Video(src, self.fps) if src.endswith((".mov", ".mp4", ".webm")) else Still(src)
            self.layers.append((L, obj))
        self.parts = [Particles(p) for p in spec.get("particles", [])]
        Y, X = np.mgrid[0:H, 0:W].astype(np.float32)
        r = (((X - W / 2) / (W / 2)) ** 2 + ((Y - H / 2) / (H / 2)) ** 2)
        self.shape = {"vig": lambda a: 1 - a * r ** 1.3}

    def camera(self, t):
        c = self.s.get("camera", {})
        a = np.array(c.get("from", [0.5, 0.5, 1.0]), float)
        b = np.array(c.get("to", c.get("from", [0.5, 0.5, 1.0])), float)
        u = ease(t / self.dur, c.get("ease", "inout"))
        cx, cy, z = a + (b - a) * u
        sh = c.get("shake", 0)
        if sh:
            hz = c.get("shake_hz", 0.3)
            cx += sh * smooth_noise(11, t, hz) / z
            cy += sh * smooth_noise(12, t, hz) * 0.6 / z
        for pt, amt, dec in c.get("punch", []):
            if t >= pt:
                z *= 1 + amt * np.exp(-(t - pt) / dec)
        return cx, cy, z

    def frame(self, i):
        t = i / self.fps
        cx, cy, z = self.camera(t)
        img = np.zeros((H, W, 3), np.float32)
        for L, obj in self.layers:
            t0, t1 = L.get("t0", 0), L.get("t1") or self.dur
            if not (t0 <= t < t1):
                continue
            src = obj.get(t - t0, self.fps) if isinstance(obj, Video) else obj.get(t)
            if src is None:
                continue
            if L.get("fixed"):
                lay = cv2.resize(src, (W, H), interpolation=cv2.INTER_AREA) if src.shape[:2] != (H, W) else src
            else:
                p = L.get("par", 1.0)
                dx, dy = L.get("drift", [0, 0])
                lay = cam_warp(src, 0.5 + (cx - 0.5) * p + dx * t, 0.5 + (cy - 0.5) * p + dy * t,
                               1 + (z - 1) * p, opaque=(L is self.s["layers"][0]))
            op = L.get("opacity", 1.0)
            fi, fo = L.get("fade_in", 0), L.get("fade_out", 0)
            if fi:
                op *= min(1, (t - t0) / fi)
            if fo:
                op *= min(1, (t1 - t) / fo)
            rgb, a = lay[..., :3] * op, lay[..., 3:4] * op
            mode = L.get("blend", "over")
            if mode == "over":
                img = rgb + img * (1 - a)
            elif mode == "add":
                img = img + rgb
            elif mode == "screen":
                img = 1 - (1 - img) * (1 - np.clip(rgb, 0, 1))
            elif mode == "multiply":
                img = img * (1 - a) + img * rgb
        pan = (cx - 0.5, cy - 0.5)
        for p in self.parts:
            rgb, a, mode = p.draw(t, pan)
            img = img + rgb if mode == "add" else rgb + img * (1 - a)
        lt = self.s.get("light", {})
        k = 1.0
        if lt.get("flicker"):
            k *= 1 - lt["flicker"] * (0.5 + 0.5 * smooth_noise(21, t, lt.get("flicker_hz", 9)))
        img = img * k
        for pt, st, dec, col in lt.get("pulses", []):
            if t >= pt:
                img = img + st * np.exp(-(t - pt) / dec) * np.array(col, np.float32) ** 2.2 * (0.05 + img)
        sw = lt.get("sweep")
        if sw and sw["t0"] <= t <= sw["t1"]:
            u = (t - sw["t0"]) / (sw["t1"] - sw["t0"])
            Y, X = np.mgrid[0:H:4, 0:W:4].astype(np.float32)
            ang = np.deg2rad(sw.get("angle", 20))
            d = (X / W * np.cos(ang) + Y / H * np.sin(ang)) - (-0.3 + 1.6 * u)
            m = np.exp(-(d / sw.get("width", 0.2)) ** 2)
            img = img + cv2.resize(m, (W, H))[..., None] * np.array(sw.get("color", [1, 0.9, 0.7]), np.float32) * 0.6
        out = finish(img, self.s.get("grade", {}), t, i, self.shape)
        fd = self.s.get("fade", {})
        f = 1.0
        if fd.get("in"):
            f = min(f, t / fd["in"])
        if fd.get("out"):
            f = min(f, (self.dur - t) / fd["out"])
        f = max(0.0, f)
        if f < 1:
            out = out * f + np.array(fd.get("color", [0, 0, 0]), np.float32) * (1 - f)
        for ft, fdur, col in self.s.get("flash", []):
            if ft <= t < ft + fdur:
                out = np.broadcast_to(np.array(col, np.float32), out.shape).copy()
        lb = self.s.get("letterbox")
        if lb:
            bar = int(round((H - W / lb) / 2))
            out[:bar] = 0
            out[H - bar:] = 0
        return (np.clip(out, 0, 1) * 255 + 0.5).astype(np.uint8)


def main():
    spec = json.loads(Path(sys.argv[1]).read_text())
    preview = "--preview" in sys.argv
    shot = Shot(spec, preview)
    n = int(round(shot.dur * shot.fps))
    out = P(spec["out"])
    out.parent.mkdir(parents=True, exist_ok=True)
    if preview:
        idx = np.linspace(0, n - 1, 6).astype(int)
        frames = []
        for i in range(n):
            f = shot.frame(i)  # videos must be read in order
            if i in idx:
                frames.append(cv2.resize(f, (W // 4, H // 4)))
        sheet = np.vstack([np.hstack(frames[:3]), np.hstack(frames[3:6])])
        cv2.imwrite(str(out.with_suffix(".sheet.jpg")), cv2.cvtColor(sheet, cv2.COLOR_RGB2BGR))
        print(out.with_suffix(".sheet.jpg"))
        return
    ff = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                           "-r", str(shot.fps), "-i", "-", "-c:v", "libx264", "-crf", "15", "-preset", "medium",
                           "-tune", "film", "-pix_fmt", "yuv420p", str(out)], stdin=subprocess.PIPE)
    for i in range(n):
        ff.stdin.write(shot.frame(i).tobytes())
    ff.stdin.close()
    ff.wait()
    print(out, n, "frames")


if __name__ == "__main__":
    main()
