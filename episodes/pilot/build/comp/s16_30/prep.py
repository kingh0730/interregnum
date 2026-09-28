"""Per-shot base plates for shots 16-30: bake the pixel-level effects (screen inserts, masked flicker, steam, drops,
rain shadows, jitter, pulses, reflections) into a keyframe-resolution video, which reel.py then moves, grades and
letterboxes.  usage: uv run work/pilot/comp/s16_30/prep.py <shot> [...] [--still DIR]
"""
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np

O = Path(__file__).parent
R = O.parents[3]
K = R / "work/pilot/keys"
JS = R / "work/pilot/js"
W0, H0 = 1672, 941
FPS = 24
sx = W0 / 960  # preview coords (960 wide) -> key coords


def key(name):
    return cv2.imread(str(K / f"{name}.png")).astype(np.float32) / 255.0


def lum(img):
    return img[..., 0] * 0.0722 + img[..., 1] * 0.7152 + img[..., 2] * 0.2126


def cyan_mask(img, blur=25):
    b, g, r = img[..., 0], img[..., 1], img[..., 2]
    m = np.clip(((b + g) / 2 - r - 0.04) / 0.25, 0, 1) * np.clip(lum(img) / 0.25, 0, 1)
    return cv2.GaussianBlur(m, (0, 0), blur)


def red_mask(img, blur=6):
    b, g, r = img[..., 0], img[..., 1], img[..., 2]
    m = np.clip((r - np.maximum(g, b) - 0.15) / 0.3, 0, 1)
    return cv2.GaussianBlur(m, (0, 0), blur)


def noise(seed, t, hz):
    r = np.random.default_rng(seed)
    ph = r.uniform(0, 2 * np.pi, 4)
    f = hz * np.array([1.0, 1.618, 2.414, 3.303])
    a = np.array([0.55, 0.25, 0.13, 0.07])
    return float((a * np.sin(2 * np.pi * f * t + ph)).sum())


def read_video(path, w=1920, h=1080):
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(path), "-f", "rawvideo", "-pix_fmt", "bgr24", "-"],
                         stdout=subprocess.PIPE)
    while True:
        buf = p.stdout.read(w * h * 3)
        if len(buf) < w * h * 3:
            break
        yield np.frombuffer(buf, np.uint8).reshape(h, w, 3).astype(np.float32) / 255.0


_j15 = None


def j15_luma():
    """J15 stand-by luminance curve, normalized to [-1, 1] (192 frames, loops)."""
    global _j15
    if _j15 is None:
        l = np.array([lum(cv2.resize(f, (192, 108))).mean() for f in read_video(JS / "j15_standby.mp4")])
        _j15 = (l - l.mean()) / max(1e-6, (l.max() - l.min()) / 2)
    return _j15


class Writer:
    def __init__(self, name, still_dir=None):
        self.out = O / f"{name}.mp4"
        self.still_dir, self.name, self.i = still_dir, name, 0
        self.p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "bgr24",
                                   "-s", f"{W0}x{H0}", "-r", str(FPS), "-i", "-", "-c:v", "libx264rgb", "-crf", "9",
                                   "-preset", "fast", str(self.out)], stdin=subprocess.PIPE)

    def write(self, img):
        u8 = (np.clip(img, 0, 1) * 255 + 0.5).astype(np.uint8)
        if self.still_dir and self.i in (0, 60):
            cv2.imwrite(str(Path(self.still_dir) / f"base_{self.name}_{self.i}.jpg"), u8)
        self.p.stdin.write(u8.tobytes())
        self.i += 1

    def close(self):
        self.p.stdin.close()
        self.p.wait()
        print(self.out, self.i, "frames")


# ------------------------------------------------------------------ effects
def quad_from_bright(img, region, thr=0.55):
    """4 corners of the largest bright cyan panel inside region (x0,y0,x1,y1 in key px)."""
    x0, y0, x1, y1 = region
    m = np.zeros(img.shape[:2], np.uint8)
    sub = img[y0:y1, x0:x1]
    c = (lum(sub) > thr) & (sub[..., 0] > sub[..., 2] + 0.1)
    m[y0:y1, x0:x1] = c.astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
    cnts, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = cv2.convexHull(max(cnts, key=cv2.contourArea))
    for eps in np.linspace(0.005, 0.1, 40):
        ap = cv2.approxPolyDP(cnt, eps * cv2.arcLength(cnt, True), True)
        if len(ap) == 4:
            break
    pts = ap.reshape(4, 2).astype(np.float32)
    s, d = pts.sum(1), np.diff(pts, axis=1).ravel()
    return np.float32([pts[np.argmin(s)], pts[np.argmin(d)], pts[np.argmax(s)], pts[np.argmax(d)]])  # TL TR BR BL


def warp_into(src, quad, crop=None):
    h, w = src.shape[:2]
    x0, y0, x1, y1 = crop or (0, 0, w, h)
    Hm = cv2.getPerspectiveTransform(np.float32([[x0, y0], [x1, y0], [x1, y1], [x0, y1]]), quad)
    out = cv2.warpPerspective(src, Hm, (W0, H0), flags=cv2.INTER_AREA if (x1 - x0) > 2 * (quad[1, 0] - quad[0, 0])
                              else cv2.INTER_LINEAR)
    m = np.zeros((H0, W0), np.float32)
    cv2.fillConvexPoly(m, np.int32(np.round(quad * 8)), 1.0, cv2.LINE_AA, shift=3)
    return out, m, Hm


def barrel(img, k=0.03):
    h, w = img.shape[:2]
    Y, X = np.mgrid[0:h, 0:w].astype(np.float32)
    nx, ny = (X - w / 2) / (w / 2), (Y - h / 2) / (h / 2)
    r2 = nx * nx + ny * ny
    f = 1 + k * r2
    mx, my = (nx * f) * w / 2 + w / 2, (ny * f) * h / 2 + h / 2
    return cv2.remap(img, mx, my, cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)


def scanlines(img, amt=0.08, period=3):
    img = img.copy()
    img[::period] *= 1 - amt
    return img


def cover_crop(src_w, src_h, quad):
    """Crop rect of the source that matches the quad's aspect (cover)."""
    qw = (np.linalg.norm(quad[1] - quad[0]) + np.linalg.norm(quad[2] - quad[3])) / 2
    qh = (np.linalg.norm(quad[3] - quad[0]) + np.linalg.norm(quad[2] - quad[1])) / 2
    a = qw / qh
    if src_w / src_h > a:
        cw = src_h * a
        return ((src_w - cw) / 2, 0, (src_w + cw) / 2, src_h)
    ch = src_w / a
    return (0, (src_h - ch) / 2, src_w, (src_h + ch) / 2)


class RainShadow:
    """Droplet shadows sliding down (luminance-only), as projected from a rainy window."""

    def __init__(self, seed, n=70, region=(0, 0, W0, H0)):
        r = np.random.default_rng(seed)
        self.r = region
        self.x = r.uniform(0, 1, n)
        self.y = r.uniform(-0.2, 1, n)
        self.v = r.uniform(0.03, 0.16, n)
        self.s = r.uniform(5, 16, n)
        self.stick = r.uniform(0, 10, n)

    def __call__(self, t):
        x0, y0, x1, y1 = self.r
        w, h = (x1 - x0) // 4, (y1 - y0) // 4
        lay = np.zeros((h, w), np.float32)
        for i in range(len(self.x)):
            # stop-and-go sliding like a real droplet run
            tt = t + self.stick[i]
            yy = (self.y[i] + self.v[i] * (tt + 0.35 * np.sin(tt * 1.7 + i))) % 1.2 - 0.1
            cx, cy, s = int(self.x[i] * w), int(yy * h), self.s[i] / 4
            cv2.ellipse(lay, (cx, cy), (max(1, int(s * 0.7)), max(1, int(s))), 0, 0, 360, 1.0, -1, cv2.LINE_AA)
            cv2.line(lay, (cx, cy), (cx, int(cy - s * 5)), 0.45, max(1, int(s * 0.5)), cv2.LINE_AA)
        lay = cv2.GaussianBlur(lay, (0, 0), 2.5)
        full = np.zeros((H0, W0), np.float32)
        full[y0:y0 + h * 4, x0:x0 + w * 4] = cv2.resize(lay, (w * 4, h * 4))
        return np.clip(full, 0, 1)


class Steam:
    def __init__(self, seed, origin, n=14, height=60, width=10, strength=0.10):
        r = np.random.default_rng(seed)
        self.o, self.hgt, self.wd, self.st = origin, height, width, strength
        self.ph = r.uniform(0, 1, n)
        self.dx = r.uniform(-1, 1, n)
        self.rate = r.uniform(0.25, 0.45, n)
        self.fr = r.uniform(0.5, 1.4, n)

    def __call__(self, t):
        lay = np.zeros((H0, W0), np.float32)
        for i in range(len(self.ph)):
            u = (self.ph[i] + t * self.rate[i]) % 1.0
            y = self.o[1] - u * self.hgt
            x = self.o[0] + self.dx[i] * self.wd * 0.5 + np.sin(u * 5 + i + t * self.fr[i]) * self.wd * 0.6 * u
            rad = 3 + 9 * u
            a = np.sin(np.pi * u) ** 1.5 * (1 - u)
            cv2.circle(lay, (int(x * 8), int(y * 8)), int(rad * 8), float(a), -1, cv2.LINE_AA, shift=3)
        return cv2.GaussianBlur(lay, (0, 0), 5) * self.st


class Drops:
    """Beads and runs on window glass inside a rect; returns (add_rgb, darken) maps."""

    def __init__(self, seed, rect, beads=160, runs=14):
        r = np.random.default_rng(seed)
        self.rect = rect
        x0, y0, x1, y1 = rect
        self.bx, self.by = r.uniform(x0, x1, beads), r.uniform(y0, y1, beads)
        self.bs = r.uniform(1.0, 2.8, beads)
        self.rx, self.ry0 = r.uniform(x0, x1, runs), r.uniform(y0, y1, runs)
        self.rv = r.uniform(25, 90, runs)
        self.rs = r.uniform(1.8, 3.2, runs)
        self.rph = r.uniform(0, 6, runs)

    def __call__(self, t):
        x0, y0, x1, y1 = self.rect
        lay = np.zeros((H0, W0), np.float32)
        for x, y, s in zip(self.bx, self.by, self.bs):
            cv2.circle(lay, (int(x * 8), int(y * 8)), int(s * 8), 0.45, -1, cv2.LINE_AA, shift=3)
        for i in range(len(self.rx)):
            span = y1 - y0
            yy = y0 + ((self.ry0[i] - y0) + self.rv[i] * (t + 0.3 * np.sin(t * 2.1 + self.rph[i]))) % span
            xx = self.rx[i] + 2 * np.sin(yy * 0.05 + i)
            top = max(y0, yy - 70)
            cv2.line(lay, (int(xx), int(top)), (int(xx), int(yy)), 0.25, 1, cv2.LINE_AA)
            cv2.circle(lay, (int(xx * 8), int(yy * 8)), int(self.rs[i] * 8), 1.0, -1, cv2.LINE_AA, shift=3)
        clip = np.zeros_like(lay)
        clip[y0:y1, x0:x1] = 1
        return cv2.GaussianBlur(lay, (0, 0), 0.8) * clip


# ------------------------------------------------------------------ shots
def shot16(still):
    img = cv2.imread(str(O / "k09_ip.png")).astype(np.float32) / 255.0
    n = 144
    quad = quad_from_bright(img, (int(780 * sx), int(170 * sx), int(890 * sx), int(310 * sx)))
    print("TV quad", quad.round(1).tolist())
    # shrink slightly inside the bezel and bulge the corners a touch (CRT)
    c = quad.mean(0)
    quad = c + (quad - c) * np.float32([1.07, 1.035])
    cyan = cyan_mask(img)
    _, scr_m, _ = warp_into(np.zeros((10, 10, 3), np.float32), quad)
    scr_m = cv2.GaussianBlur(scr_m, (0, 0), 1.0)
    cyan = cyan * (1 - cv2.dilate(scr_m, np.ones((9, 9), np.uint8)))
    jl = j15_luma()
    steam = [Steam(3, (1250, 386), n=18, height=60, width=26, strength=0.22),
             Steam(4, (622, 440), n=12, height=52, width=9, strength=0.22)]
    drops = Drops(7, (int(330 * sx), int(22 * sx), int(570 * sx), int(215 * sx)))
    rs = RainShadow(9, n=50, region=(int(320 * sx), int(215 * sx), int(640 * sx), int(410 * sx)))
    # handset patch (cream receiver on the phone)
    hx0, hy0, hx1, hy1 = int(255 * sx), int(272 * sx), int(322 * sx), int(305 * sx)
    sub = img[hy0:hy1, hx0:hx1]
    hm = np.zeros((H0, W0), np.float32)
    hm[hy0:hy1, hx0:hx1] = ((lum(sub) > 0.45) & (sub[..., 2] > sub[..., 0])).astype(np.float32)
    hm = cv2.GaussianBlur(cv2.dilate(hm, np.ones((3, 3), np.uint8)), (0, 0), 0.8)
    rings = [(3.5, 3.9), (4.1, 4.5), (5.5, 5.9)]
    Yv, Xv = np.mgrid[0:1080, 0:1440].astype(np.float32)
    vig43 = (1 - 0.45 * (((Xv - 720) / 720) ** 2 + ((Yv - 540) / 540) ** 2) ** 1.5)[..., None].clip(0.3, 1)
    wr = Writer("b16", still)
    frames = read_video(JS / "j15_standby.mp4")
    for i in range(n):
        t = i / FPS
        jf = next(frames)
        crt = scanlines(barrel(jf[:, 240:1680] * 1.9 + np.float32([0.03, 0.05, 0.02]), 0.03), 0.12)
        crt = crt * vig43
        ins, _, _ = warp_into(crt, quad)
        f = img.copy()
        f = f * (1 - scr_m[..., None]) + ins * scr_m[..., None]
        # flicker: cyan-lit pixels follow the stand-by luminance, 4 %
        f = f * (1 + 0.04 * jl[i % len(jl)] * cyan[..., None])
        # rain shadows on the wall under the window, 4 %
        f = f * (1 - 0.04 * rs(t)[..., None])
        # drops on the glass: pale cyan beads/runs, darker rims
        d = drops(t)
        f = f + d[..., None] * np.float32([0.30, 0.26, 0.16]) - cv2.GaussianBlur(d, (0, 0), 2)[..., None] * 0.05
        # steam, warm-lit
        for s in steam:
            f = f + s(t)[..., None] * np.float32([0.62, 0.78, 0.92])
        # ringing handset jitter, 1 px at 25 Hz
        if any(a <= t < b for a, b in rings):
            dx = 0.9 * np.sign(np.sin(2 * np.pi * 25 * t + 0.3))
            dy = 0.5 * np.sign(np.sin(2 * np.pi * 25 * t * 1.13 + 1.1))
            M = np.float32([[1, 0, dx], [0, 1, dy]])
            sh = cv2.warpAffine(f, M, (W0, H0), borderMode=cv2.BORDER_REPLICATE)
            shm = cv2.warpAffine(hm, M, (W0, H0))[..., None]
            f = f * (1 - shm) + sh * shm
        wr.write(f)
    wr.close()


def face_shot(name, keyname, n, flick_amt, driver, shadow, still, extra=None):
    img = key(keyname)
    cyan = cyan_mask(img)
    jl = j15_luma()
    rs = RainShadow(21, n=90) if shadow else None
    wr = Writer(name, still)
    for i in range(n):
        t = i / FPS
        drv = jl[i % len(jl)] if driver == "j15" else noise(31, t, 0.5)
        f = img * (1 + flick_amt * drv * cyan[..., None])
        if extra:
            f = extra(f, t, i)
        if rs is not None:
            f = f * (1 - shadow * rs(t)[..., None])
        wr.write(f)
    wr.close()


def shot17(still):
    img = key("k10")
    wall = np.clip((lum(img) - 0.45) / 0.2, 0, 1) * (img[..., 0] > img[..., 2] + 0.1)
    wall = cv2.GaussianBlur(wall.astype(np.float32), (0, 0), 8)[..., None]
    face_shot("b17", "k10", 96, 0.02, "noise", 0, still,
              extra=lambda f, t, i: f * (1 + 0.02 * noise(41, t, 0.15) * wall))


def shot23(still):
    img = cv2.imread(str(O / "k14_ip.png")).astype(np.float32) / 255.0
    orig = key("k14")
    n = 144
    quad = quad_from_bright(orig, (int(215 * sx), int(95 * sx), int(745 * sx), int(360 * sx)), thr=0.5)
    print("wall quad", quad.round(1).tolist())
    np.save(O / "k14_quad.npy", quad)
    face = key("k02")
    crop = cover_crop(W0, H0, quad)
    ins, qm, Hm = warp_into(face, quad, crop)
    # synthetic 12 x 7 tile grid in wall space -> bezel mask and tile labels
    GW, GH = 1200, 700
    tiles = np.zeros((GH, GW), np.int32)
    cols, rows, bez = 12, 7, 9
    for r in range(rows):
        for c in range(cols):
            x0, x1 = c * GW // cols + bez // 2, (c + 1) * GW // cols - bez // 2
            y0, y1 = r * GH // rows + bez // 2, (r + 1) * GH // rows - bez // 2
            tiles[y0:y1, x0:x1] = 1 + r * cols + c
    Hg = cv2.getPerspectiveTransform(np.float32([[0, 0], [GW, 0], [GW, GH], [0, GH]]), quad)
    lab = cv2.warpPerspective(tiles.astype(np.float32), Hg, (W0, H0), flags=cv2.INTER_NEAREST).astype(np.int32)
    tm = cv2.warpPerspective((tiles > 0).astype(np.float32), Hg, (W0, H0), flags=cv2.INTER_LINEAR)
    tm = tm * qm
    haze = np.float32([0x50, 0x35, 0x1A]) / 255.0
    bezel_col = np.float32([0.10, 0.07, 0.04])
    red = red_mask(orig, 10)
    red_core = orig * red[..., None]
    # eyes of the inserted face (k02 eyes at 0.5, 0.40) in key coords
    ex, ey = crop[0] + 0.5 * (crop[2] - crop[0]), crop[1] + 0.40 * (crop[3] - crop[1])
    e = cv2.perspectiveTransform(np.float32([[[ex, ey]]]), Hm)[0, 0]
    print("face eyes at", (e / [W0, H0]).round(4).tolist())
    np.save(O / "k14_eyes.npy", e / [W0, H0])
    ntiles = rows * cols
    wr = Writer("b23", still)
    for i in range(n):
        t = i / FPS
        jit = np.ones(ntiles + 1, np.float32)
        jit[1:] = [1 + 0.04 * noise(100 + k, t, 0.35) for k in range(ntiles)]
        mult = jit[lab][..., None]
        scr = ins * 1.08 * mult
        scr = scr * 0.88 + haze * 0.12
        wallc = scr * tm[..., None] + bezel_col * (qm - tm)[..., None]
        f = img * (1 - qm[..., None]) + wallc
        # standby lamp: 0.5 Hz, 60-90 %
        k = 0.6 + 0.3 * (0.5 + 0.5 * np.sin(2 * np.pi * 0.5 * t - np.pi / 2))
        f = f + (k / 0.9 - 1) * red_core
        wr.write(f)
    wr.close()


def shot25(still):
    img = key("k15")
    fr = None
    for j, fr_ in enumerate(read_video(JS / "s24_i.mp4")):
        if j == 150:
            fr = fr_
            break
    band = fr[250:520, 180:1740]                      # the script lines
    band = cv2.flip(band, 1)
    irises = [(int(252 * sx), int(310 * sx)), (int(690 * sx), int(307 * sx))]
    rad = int(44 * sx)
    wr = Writer("b25", still)
    for i in range(72):
        t = i / FPS
        f = img.copy()
        for (cx, cy) in irises:
            w = int(rad * 2.0)
            hh = int(w * band.shape[0] / band.shape[1])
            small = cv2.resize(band, (w, hh), interpolation=cv2.INTER_AREA)
            lay = np.zeros((H0, W0, 3), np.float32)
            y = int(round(cy - hh / 2 + 6 - (20 / 1.148) * (t / 3.0)))
            x = cx - w // 2
            lay[y:y + hh, x:x + w] = small
            m = np.zeros((H0, W0), np.float32)
            cv2.circle(m, (cx, cy), int(rad * 0.92), 1.0, -1, cv2.LINE_AA)
            m = cv2.GaussianBlur(m, (0, 0), 3)
            text = np.clip(lum(lay) - 0.12, 0, 1)[..., None] * np.float32([1.0, 0.95, 0.85])
            f = f + 0.25 * text * m[..., None] * 1.6
        wr.write(f)
    wr.close()


def shot27(still):
    img = key("k16")
    red = red_mask(img, 12)
    Y, X = np.mgrid[0:H0, 0:W0]
    hand = ((X > 0.45 * W0) & (Y < 0.62 * H0) & ((lum(img) > 0.22) | (img[..., 2] > 0.35))).astype(np.float32)
    hand = cv2.morphologyEx(hand, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    hand = cv2.GaussianBlur(cv2.dilate(hand, np.ones((5, 5), np.uint8)), (0, 0), 1.5)[..., None]
    wr = Writer("b27", still)
    for i in range(96):
        t = i / FPS
        dx = 0.6 / 1.148 * np.sin(2 * np.pi * 9 * t)
        dy = 0.35 / 1.148 * np.sin(2 * np.pi * 9 * t * 1.27 + 1.3)
        M = np.float32([[1, 0, dx], [0, 1, dy]])
        sh = cv2.warpAffine(img, M, (W0, H0), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        hm = cv2.warpAffine(hand, M, (W0, H0))[..., None]
        f = img * (1 - hm) + sh * hm
        dt = t - np.floor(t)
        p = 0.15 * max(0.0, 1 - dt / 0.4) ** 2
        f = f + p * red[..., None] * (f + 0.05) * np.float32([0.35, 0.45, 1.0])
        wr.write(f)
    wr.close()


def shot30(still):
    img = cv2.imread(str(O / "k17_ip.png")).astype(np.float32) / 255.0
    orig = key("k17")
    quad = quad_from_bright(orig, (int(470 * sx), int(40 * sx), int(670 * sx), int(215 * sx)), thr=0.55)
    print("facade quad", quad.round(1).tolist())
    # the broadcast frame: k01 cover-fit 1920x1080, scanlines, bug
    k01 = cv2.resize(key("k01"), (1920, 1080), interpolation=cv2.INTER_AREA)
    bug = cv2.imread(str(JS / "j14_bug.png"), -1).astype(np.float32) / 255.0
    bc = k01 * (1 - bug[..., 3:4]) + bug[..., :3] * bug[..., 3:4]
    bc = scanlines(bc * 0.92 + 0.04, 0.10)
    ins, qm, _ = warp_into(bc, quad, cover_crop(1920, 1080, quad))
    qm = cv2.GaussianBlur(qm, (0, 0), 0.7)
    fgm = cv2.imread(str(O / "k17_fg.png"), -1)[..., 3].astype(np.float32) / 255.0
    Y, X = np.mgrid[0:H0, 0:W0]
    street = (Y > 0.60 * H0).astype(np.float32)
    refl = street * np.clip((orig[..., 0] - orig[..., 2] - 0.15) / 0.3, 0, 1) * np.clip((lum(orig) - 0.15) / 0.3, 0, 1)
    refl = cv2.GaussianBlur(refl, (0, 0), 2)[..., None]
    rng = np.random.default_rng(5)
    wr = Writer("b30", still)
    base_l = lum(ins[qm > 0.5]).mean()
    for i in range(144):
        t = i / FPS
        br = 1 + 0.025 * np.sin(2 * np.pi * 0.25 * t) + 0.01 * noise(51, t, 3)
        scr = ins * 1.18 * br
        f = img * (1 - qm[..., None]) + scr * qm[..., None]
        # glow halo around the screen
        halo = cv2.GaussianBlur(scr * qm[..., None], (0, 0), 28) * 0.55 + cv2.GaussianBlur(scr * qm[..., None], (0, 0), 90) * 0.35
        f = f + halo * (1 - qm[..., None])
        # cyan spill along the wet reflection streaks, driven by screen luma
        f = f + refl * np.float32([0.9, 0.85, 0.35]) * 0.14 * br
        # ground splashes
        lay = np.zeros((H0, W0), np.float32)
        for _ in range(55):
            x, y = rng.uniform(0, W0), rng.uniform(0.70 * H0, H0)
            r = rng.uniform(1.0, 3.5)
            cv2.circle(lay, (int(x * 8), int(y * 8)), int(r * 8), 0.8, 1, cv2.LINE_AA, shift=3)
            cv2.circle(lay, (int(x), int(y - r)), 1, 1.0, -1, cv2.LINE_AA)
        lay = cv2.GaussianBlur(lay, (0, 0), 0.6) * (lum(img) > 0.08)
        f = f + lay[..., None] * np.float32([0.55, 0.5, 0.35]) * 0.5
        wr.write(f)
    wr.close()


def shot_js_scan():
    """Full-frame scanline multipliers (display-space values) for the monitor / broadcast feel."""
    for name, amt in (("scan4", 0.04), ("scan8", 0.08)):
        im = np.full((1080, 1920, 4), 255, np.uint8)
        im[::3, :, :3] = int(round(255 * (1 - amt)))
        cv2.imwrite(str(O / f"{name}.png"), im)


SHOTS = {
    "16": shot16,
    "17": shot17,
    "18": lambda s: face_shot("b18", "k11", 120, 0.04, "j15", 0.03, s),
    "19": lambda s: face_shot("b19", "k12", 96, 0.02, "noise", 0, s),
    "20": lambda s: face_shot("b20", "k13", 144, 0.04, "j15", 0.03, s),
    "23": shot23,
    "25": shot25,
    "27": shot27,
    "30": shot30,
}

if __name__ == "__main__":
    args = sys.argv[1:]
    still = None
    if "--still" in args:
        k = args.index("--still")
        still = args[k + 1]
        del args[k:k + 2]
    for a in args:
        if a == "scan":
            shot_js_scan()
        else:
            SHOTS[a](still)
