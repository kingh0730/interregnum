"""Shared helpers for shots 31-46: plate writers, light masks, noise, grade presets. Display-space float RGB (0..1)."""
import json
import subprocess
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[4]
PILOT = ROOT / "work/pilot"
KEYS = PILOT / "keys"
JS = PILOT / "js"
HERE = Path(__file__).resolve().parent
FPS = 24


def key(name):
    im = cv2.imread(str(KEYS / f"{name}.png"), cv2.IMREAD_UNCHANGED)
    if im.shape[2] == 4:
        rgb = im[..., :3][..., ::-1].astype(np.float32) / 255
        return np.dstack([rgb, im[..., 3:].astype(np.float32) / 255])
    return im[..., ::-1].astype(np.float32) / 255


def save_png(path, rgb):
    im = (np.clip(rgb, 0, 1) * 255 + 0.5).astype(np.uint8)
    if im.shape[2] == 4:
        im = np.dstack([im[..., :3][..., ::-1], im[..., 3:]])
    else:
        im = im[..., ::-1]
    cv2.imwrite(str(path), im)


class Writer:
    """Stream float RGB (or RGBA with alpha=True -> ProRes 4444 .mov) frames to a near-lossless plate."""

    def __init__(self, path, w, h, alpha=False):
        self.alpha = alpha
        path = Path(path)
        if alpha:
            args = ["-pix_fmt", "rgba", "-s", f"{w}x{h}", "-r", str(FPS), "-i", "-", "-c:v", "prores_ks",
                    "-profile:v", "4444", "-pix_fmt", "yuva444p10le", "-qscale:v", "6", str(path)]
        else:
            args = ["-pix_fmt", "rgb24", "-s", f"{w}x{h}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "8",
                    "-preset", "fast", "-pix_fmt", "yuv444p", str(path)]
        self.p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo"] + args, stdin=subprocess.PIPE)

    def write(self, img):
        self.p.stdin.write((np.clip(img, 0, 1) * 255 + 0.5).astype(np.uint8).tobytes())

    def close(self):
        self.p.stdin.close()
        self.p.wait()


def lum(img):
    return img[..., 0] * 0.2126 + img[..., 1] * 0.7152 + img[..., 2] * 0.0722


def blur(m, s):
    return cv2.GaussianBlur(m, (0, 0), s)


def cyan_mask(img, s=25):
    """Pixels lit by screen light: blue/green dominate red, weighted by brightness."""
    r, g, b = img[..., 0], img[..., 1], img[..., 2]
    m = np.clip((np.minimum(g, b) * 0.5 + b * 0.5 - r) * 3.0, 0, 1) * np.clip(lum(img) * 2.5, 0, 1)
    return np.clip(blur(m, s), 0, 1)


def amber_mask(img, s=25):
    r, g, b = img[..., 0], img[..., 1], img[..., 2]
    m = np.clip((r - b) * 2.5, 0, 1) * np.clip((g - b) * 3, 0, 1) * np.clip(lum(img) * 2.5, 0, 1)
    return np.clip(blur(m, s), 0, 1)


def snoise(seed, t, hz):
    r = np.random.default_rng(seed)
    ph = r.uniform(0, 2 * np.pi, 4)
    f = hz * np.array([1.0, 1.618, 2.414, 3.303])
    a = np.array([0.55, 0.25, 0.13, 0.07])
    return float((a * np.sin(2 * np.pi * f * t + ph)).sum())


def ease_sine(u):
    u = float(np.clip(u, 0, 1))
    return 0.5 - 0.5 * np.cos(np.pi * u)


class RainShadow:
    """Droplet shadows sliding down (luminance only). Returns a multiplier field."""

    def __init__(self, w, h, amount=0.03, n=90, seed=7):
        r = np.random.default_rng(seed)
        self.w, self.h, self.a = w, h, amount
        self.x = r.uniform(0, 1, n)
        self.y0 = r.uniform(0, 1, n)
        self.v = r.uniform(0.01, 0.06, n)
        self.sz = r.uniform(3, 9, n)
        self.ph = r.uniform(0, 6.28, n)

    def field(self, t):
        sw, sh = self.w // 4, self.h // 4
        f = np.zeros((sh, sw), np.float32)
        y = (self.y0 + self.v * t + 0.004 * np.sin(t * 0.7 + self.ph)) % 1.0
        for xi, yi, si in zip(self.x, y, self.sz):
            c = (int(xi * sw), int(yi * sh))
            cv2.ellipse(f, c, (max(1, int(si / 4)), max(1, int(si / 2.5))), 0, 0, 360, 1.0, -1, cv2.LINE_AA)
            cv2.line(f, c, (c[0], int(c[1] - si * 2)), 0.5, max(1, int(si / 8)), cv2.LINE_AA)
        f = blur(f, 2.0)
        f = cv2.resize(f, (self.w, self.h))
        return 1 - self.a * np.clip(f, 0, 1)[..., None]


# ------------------------------------------------------------------ grade presets (reel.py "grade" dicts)
GRADES = {
    "HALL": {"exposure": 0, "contrast": 1.03, "sat": 1.0, "lift": [0.030, 0.040, 0.075], "gain": [0.97, 1.0, 1.04],
             "bloom": 0.5, "vignette": 0.25, "grain": 0.02},
    "HOME": {"exposure": 0, "contrast": 1.02, "sat": 1.02, "lift": [0.030, 0.025, 0.035], "gain": [1.04, 1.0, 0.96],
             "bloom": 0.55, "vignette": 0.22, "grain": 0.02},
    "DAWN": {"exposure": 0, "contrast": 1.02, "sat": 1.03, "lift": [0.030, 0.035, 0.075], "gain": [1.04, 0.99, 0.98],
             "bloom": 0.5, "vignette": 0.2, "grain": 0.015},
    "BROADCAST": {"exposure": 0, "contrast": 0.95, "sat": 0.92, "lift": [0.045, 0.06, 0.09], "gain": [1, 1, 1],
                  "bloom": 0.3, "vignette": 0.15, "grain": 0.015, "chroma": 1},
    "JS": {"exposure": 0, "contrast": 1.0, "sat": 1.0, "lift": [0, 0, 0], "gain": [1, 1, 1],
           "bloom": 0.2, "vignette": 0.12, "grain": 0.014},
}


def grade(name, **kw):
    g = dict(GRADES[name])
    g.update(kw)
    return g


def rel(p):
    return str(Path(p).resolve().relative_to(ROOT))


def spec(n, dur, layers, camera=None, grade_=None, letterbox=True, **extra):
    s = {"dur": dur, "fps": FPS, "out": f"work/pilot/shots/{n:02d}.mp4", "layers": layers}
    if camera:
        s["camera"] = camera
    if grade_:
        s["grade"] = grade_
    if letterbox:
        s["letterbox"] = 2.39
    s.update(extra)
    p = PILOT / f"comp/{n:02d}.json"
    p.write_text(json.dumps(s, indent=1))
    return p


def focus_cam(fx, fy, z):
    """Camera centre that keeps normalized source point (fx, fy) where it sits at zoom 1."""
    return [fx + (0.5 - fx) / z, fy + (0.5 - fy) / z, z]


def broadcast_layers():
    return [{"src": rel(HERE / "scanlines.png"), "fixed": True},
            {"src": "work/pilot/js/j14_bug.png", "fixed": True}]


def make_scanlines():
    a = np.zeros((1080, 1920, 4), np.uint8)
    a[::3, :, 3] = int(0.08 * 255)
    cv2.imwrite(str(HERE / "scanlines.png"), a)
