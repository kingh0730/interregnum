"""Composite the layered anime clip: parallax camera, cel deformation, blink, petals, light FX, grade.

Usage: python render.py [--preview N] -> writes render/clip_silent.mp4 (or preview frames)
"""
import math
import subprocess
import sys
from multiprocessing import Pool
from pathlib import Path

import cv2
import numpy as np

HERE = Path(__file__).parent
P = HERE / "prepped"
OUTD = HERE / "render"
OUTD.mkdir(exist_ok=True)

FPS = 24
OW, OH = 1920, 1080
SW, SH = 1672, 941
S0 = OW / SW

SHOTS = [("s1", 4.5), ("s2", 4.5), ("s3", 5.0)]


# ---------------------------------------------------------------- utilities
def load(n, premul=True):
    im = cv2.imread(str(P / f"{n}.png"), cv2.IMREAD_UNCHANGED).astype(np.float32) / 255.0
    if im.ndim == 2:
        return im
    if im.shape[2] == 3:
        im = np.dstack([im, np.ones(im.shape[:2], np.float32)])
    if premul:
        im[..., :3] *= im[..., 3:4]
    return im


def ease(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def smoothstep(e0, e1, x):
    u = np.clip((x - e0) / (e1 - e0), 0, 1)
    return u * u * (3 - 2 * u)


def cam_matrix(z, off, focus, par, extra=None):
    """Source->output affine for a layer with parallax factor `par`."""
    zl = 1 + (z - 1) * par
    k = S0 * zl
    cx, cy = focus
    M = np.array([[k, 0, cx * S0 - k * cx + off[0] * par],
                  [0, k, cy * S0 - k * cy + off[1] * par]], np.float32)
    if extra is not None:  # extra affine applied in source space first
        M = M @ np.vstack([extra, [0, 0, 1]]).astype(np.float32)
    return M


def warp(layer, M, opaque=False):
    return cv2.warpAffine(layer, M, (OW, OH), flags=cv2.INTER_CUBIC,
                          borderMode=cv2.BORDER_REPLICATE if opaque else cv2.BORDER_CONSTANT)


def over(dst, src):
    """Premultiplied 'over'. dst is RGB (opaque), src is premultiplied RGBA."""
    return src[..., :3] + dst * (1 - src[..., 3:4])


def apply_pt(M, x, y):
    return M[0, 0] * x + M[0, 1] * y + M[0, 2], M[1, 0] * x + M[1, 1] * y + M[1, 2]


# ---------------------------------------------------------------- deformation fields
def deform_fields(name, anchor_scarf, scarf_r, head_c, hair_r):
    a = load(name, premul=False)[..., 3]
    scarf = load(f"{name}_scarf")
    hair = load(f"{name}_hair")
    Y, X = np.mgrid[0:SH, 0:SW].astype(np.float32)
    rs = np.hypot(X - anchor_scarf[0], Y - anchor_scarf[1])
    ws = cv2.GaussianBlur(scarf, (0, 0), 6) * smoothstep(scarf_r[0], scarf_r[1], rs)
    rh = np.hypot(X - head_c[0], Y - head_c[1])
    wh = cv2.GaussianBlur(hair * a, (0, 0), 5) * smoothstep(hair_r[0], hair_r[1], rh)
    ws = cv2.GaussianBlur(ws, (0, 0), 8)
    wh = cv2.GaussianBlur(wh, (0, 0), 6)
    return dict(X=X, Y=Y, rs=rs, ws=ws, wh=wh, rh=rh)


def deform(layer, f, t, amp_s, amp_h):
    # animate "on twos": hold each deformation for 2 frames like hand-drawn cels
    tq = math.floor(t * FPS / 2) * 2 / FPS
    ph = 2 * math.pi * 1.5 * tq - f["rs"] / 70.0
    dx = amp_s * f["ws"] * (np.sin(ph) + 0.35 * np.sin(2.3 * ph + 1.1))
    dy = amp_s * 0.55 * f["ws"] * np.sin(ph * 1.3 + 0.7)
    phh = 2 * math.pi * 0.8 * tq - f["Y"] / 90.0
    dx += amp_h * f["wh"] * (np.sin(phh) + 0.3 * np.sin(2.1 * phh + 0.4))
    dy += amp_h * 0.35 * f["wh"] * np.sin(phh + 1.3)
    return cv2.remap(layer, f["X"] - dx, f["Y"] - dy, cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT)


# ---------------------------------------------------------------- petals
def petal_sprite(size=128):
    s = size
    Y, X = np.mgrid[0:s, 0:s].astype(np.float32)
    u = (X - s / 2) / (s * 0.30)
    v = (Y - s * 0.55) / (s * 0.42)
    body = (u ** 2 * (1 + 0.6 * v) + v ** 2) < 1.0            # teardrop, wider at the top
    notch = (np.abs(X - s / 2) < (s * 0.09) * (1 - (Y - s * 0.13) / (s * 0.12))) & (Y < s * 0.25)
    a = (body & ~notch).astype(np.float32)
    a = cv2.GaussianBlur(a, (0, 0), s / 90)
    shade = np.clip(1 - 0.5 * np.hypot(u, v + 0.3), 0, 1)
    b, g, r = 0.74 + 0.16 * shade, 0.55 + 0.25 * shade, 0.97 + 0.03 * shade  # BGR pink
    rgb = np.dstack([b, g, r]).astype(np.float32)
    return np.dstack([rgb * a[..., None], a])


PETAL = None


class Petals:
    def __init__(self, seed, n, wind=(-110, 45), zrange=(0.3, 1.8)):
        rng = np.random.default_rng(seed)
        self.n = n
        self.z = rng.uniform(*zrange, n)
        self.x0 = rng.uniform(0, OW + 400, n)
        self.y0 = rng.uniform(-200, OH + 200, n)
        sp = rng.uniform(0.7, 1.3, n)
        self.vx = wind[0] * sp * (0.5 + self.z)
        self.vy = wind[1] * sp * (0.5 + self.z)
        self.rot0 = rng.uniform(0, 360, n)
        self.rotv = rng.uniform(-160, 160, n)
        self.flip = rng.uniform(1.5, 4.0, n)
        self.flipph = rng.uniform(0, 6.28, n)
        self.sway = rng.uniform(0, 6.28, n)

    def draw(self, img, t, zmin, zmax, light=(1.0, 0.92, 0.95)):
        global PETAL
        if PETAL is None:
            PETAL = petal_sprite()
        for i in range(self.n):
            z = self.z[i]
            if not (zmin <= z < zmax):
                continue
            x = (self.x0[i] + self.vx[i] * t + 18 * z * math.sin(1.7 * t + self.sway[i])) % (OW + 400) - 200
            y = (self.y0[i] + self.vy[i] * t) % (OH + 400) - 200
            size = 14 + 34 * z ** 1.6
            sx = max(0.18, abs(math.cos(self.flip[i] * t + self.flipph[i])))
            ang = self.rot0[i] + self.rotv[i] * t
            blur = 0.0 if 0.7 < z < 1.2 else (abs(z - 0.95) * 7) ** 1.5
            pad = int(size + 3 * blur + 4)
            sc = size / PETAL.shape[0]
            R = cv2.getRotationMatrix2D((PETAL.shape[1] / 2, PETAL.shape[0] / 2), ang, 1.0)
            A = np.array([[sc * sx, 0], [0, sc]], np.float32) @ R[:, :2]
            c = np.array([pad, pad], np.float32) - A @ np.array([PETAL.shape[1] / 2, PETAL.shape[0] / 2], np.float32)
            M = np.hstack([A, c[:, None]]).astype(np.float32)
            spr = cv2.warpAffine(PETAL, M, (2 * pad, 2 * pad), flags=cv2.INTER_LINEAR)
            if blur > 0.3:
                spr = cv2.GaussianBlur(spr, (0, 0), blur)
            fade = 0.55 + 0.45 * min(1.0, z)             # far petals recede into haze
            spr = spr * fade
            spr[..., :3] *= np.array(light, np.float32)
            x0, y0 = int(x) - pad, int(y) - pad
            xa, ya, xb, yb = max(x0, 0), max(y0, 0), min(x0 + 2 * pad, OW), min(y0 + 2 * pad, OH)
            if xa >= xb or ya >= yb:
                continue
            s = spr[ya - y0:yb - y0, xa - x0:xb - x0]
            img[ya:yb, xa:xb] = s[..., :3] + img[ya:yb, xa:xb] * (1 - s[..., 3:4])
        return img


# ---------------------------------------------------------------- light FX
def find_sun(bg):
    lum = cv2.GaussianBlur(bg[..., :3].mean(-1), (0, 0), 9)
    lum[int(lum.shape[0] * 0.55):] = 0          # the sun is in the sky, not on the railing
    y, x = np.unravel_index(np.argmax(lum), lum.shape)
    return float(x), float(y)


def sun_flare(img, sx, sy, t, strength=1.0):
    Y, X = np.mgrid[0:OH, 0:OW].astype(np.float32)
    dx, dy = X - sx, Y - sy
    r = np.hypot(dx, dy)
    th = np.arctan2(dy, dx)
    glow = np.exp(-(r / 90) ** 2) * 0.55 + np.exp(-(r / 420) ** 2) * 0.22
    rays = (0.5 + 0.5 * np.sin(14 * th + 0.15 * t)) * (0.5 + 0.5 * np.sin(23 * th - 0.1 * t + 1))
    rays = rays ** 3 * np.exp(-r / 520) * 0.22
    streak = np.exp(-(dy / 5) ** 2) * np.exp(-(np.abs(dx) / 700)) * 0.18
    warm = np.array([0.55, 0.78, 1.0], np.float32)  # BGR
    add = (glow + rays + streak)[..., None] * warm * strength
    # lens ghosts along the axis through frame centre
    cx, cy = OW / 2, OH / 2
    for k, rad, a in [(-0.35, 60, 0.05), (-0.8, 110, 0.035), (-1.25, 40, 0.06), (0.4, 25, 0.05)]:
        gx, gy = cx + (sx - cx) * k, cy + (sy - cy) * k
        rg = np.hypot(X - gx, Y - gy)
        ring = np.clip(1 - np.abs(rg - rad * 0.8) / (rad * 0.35), 0, 1) * 0.6 + (rg < rad) * 0.4
        add += cv2.GaussianBlur(ring.astype(np.float32), (0, 0), 3)[..., None] * a * strength * \
            np.array([1.0, 0.85, 0.7], np.float32)
    return img + add


def sparkle_points(bg, seed, region):
    """Pick bright pixels (sun glints on water/glass) to twinkle."""
    lum = bg[..., :3].mean(-1)
    x0, y0, x1, y1 = region
    m = np.zeros_like(lum, bool)
    m[y0:y1, x0:x1] = lum[y0:y1, x0:x1] > np.percentile(lum[y0:y1, x0:x1], 99.3)
    ys, xs = np.nonzero(m)
    rng = np.random.default_rng(seed)
    idx = rng.choice(len(xs), size=min(45, len(xs)), replace=False)
    return [(xs[i], ys[i], rng.uniform(2, 5), rng.uniform(0, 6.28), rng.uniform(0.5, 1.2)) for i in idx]


def draw_sparkles(img, pts, M, t):
    for x, y, w, ph, s in pts:
        ox, oy = apply_pt(M, x, y)
        k = max(0.0, math.sin(w * t + ph)) ** 10 * s
        if k < 0.02:
            continue
        L = int(16 * s + 6)
        xi, yi = int(ox), int(oy)
        if not (L <= xi < OW - L and L <= yi < OH - L):
            continue
        yy, xx = np.mgrid[-L:L + 1, -L:L + 1].astype(np.float32)
        star = (np.exp(-(yy / 1.2) ** 2) * np.exp(-np.abs(xx) / (L / 3)) +
                np.exp(-(xx / 1.2) ** 2) * np.exp(-np.abs(yy) / (L / 3)) +
                np.exp(-(xx ** 2 + yy ** 2) / 6)) * k
        img[yi - L:yi + L + 1, xi - L:xi + L + 1] += star[..., None] * np.array([0.8, 0.95, 1.0], np.float32)
    return img


def light_wrap(bg, girl_a, amount=0.6):
    """Bleed background light over the character's edges so she sits in the scene."""
    b = cv2.GaussianBlur(bg, (0, 0), 18)
    inner = cv2.GaussianBlur(girl_a, (0, 0), 7)
    edge = np.clip(girl_a - inner, 0, 1) * 2.2
    return b * (edge * amount)[..., None]


def finish(img, t_global, frame, fade):
    # bloom (computed at quarter res)
    small = cv2.resize(img, (OW // 4, OH // 4), interpolation=cv2.INTER_AREA)
    bright = np.clip(small - 0.8, 0, None)
    bloom = cv2.GaussianBlur(bright, (0, 0), 6) * 0.6 + cv2.GaussianBlur(bright, (0, 0), 18) * 0.5
    img = img + cv2.resize(bloom, (OW, OH), interpolation=cv2.INTER_LINEAR)
    # grade: soft filmic shoulder, cool shadows / warm highlights
    img = img / (1 + 0.18 * img)
    img = img * 1.12
    lum = img.mean(-1, keepdims=True)
    img = img + (0.03 * (1 - np.clip(lum * 2, 0, 1))) * np.array([1.0, 0.3, -0.4], np.float32)
    # vignette
    Y, X = np.mgrid[0:OH, 0:OW].astype(np.float32)
    v = 1 - 0.28 * (((X - OW / 2) / (OW / 2)) ** 2 + ((Y - OH / 2) / (OH / 2)) ** 2) ** 1.2
    img = img * v[..., None]
    # grain
    rng = np.random.default_rng(frame)
    g = cv2.GaussianBlur(rng.normal(0, 0.018, (OH, OW)).astype(np.float32), (0, 0), 0.7)
    img = img + g[..., None]
    img = img * fade
    return np.clip(img, 0, 1)


# ---------------------------------------------------------------- shots
class Shot1:
    dur = 4.5

    def __init__(self):
        self.sky = load("s1_sky")
        self.ground = load("s1_ground")
        self.girl = load("s1_girl")
        self.f = deform_fields("s1_girl", (600, 365), (60, 420), (600, 110), (120, 290))
        self.sun = find_sun(self.sky)
        self.petals = Petals(1, 70)
        self.spark = sparkle_points(self.ground, 1, (700, 250, 1672, 420))
        self.focus = (640, 420)

    def frame(self, t):
        u = ease(t / self.dur)
        z = 1.05 + 0.08 * u
        off = (20 - 60 * u, 6 - 12 * u)
        Msky = cam_matrix(z, (off[0] - 14 * t, off[1]), self.focus, 0.25)
        img = warp(self.sky, Msky, opaque=True)[..., :3]
        sx, sy = apply_pt(Msky, *self.sun)
        Mg = cam_matrix(z, off, self.focus, 0.6)
        img = over(img, warp(self.ground, Mg))
        img = draw_sparkles(img, self.spark, Mg, t)
        img = self.petals.draw(img, t, 0.0, 0.8)
        g = deform(self.girl, self.f, t, amp_s=11, amp_h=5)
        Mc = cam_matrix(z, off, self.focus, 1.0)
        gw = warp(g, Mc)
        bg = img.copy()
        img = over(img, gw) + light_wrap(bg, gw[..., 3])
        img = sun_flare(img, sx, sy, t, 0.9)
        img = self.petals.draw(img, t, 0.8, 9)
        return img


class Shot2:
    dur = 4.5
    # blink timings (seconds) -> sequence of cels on twos
    blinks = [1.3, 3.5]

    def __init__(self):
        self.bg = load("s2_bg")
        self.bg = cv2.GaussianBlur(self.bg, (0, 0), 2.2)
        self.girl = load("s2_girl")
        a = self.girl[..., 3:4]
        self.cels = {"open": self.girl}
        m = np.zeros((SH, SW), np.float32)
        cv2.rectangle(m, (628, 212), (848, 372), 1, -1)
        cv2.rectangle(m, (893, 270), (1062, 443), 1, -1)
        m = cv2.GaussianBlur(m, (0, 0), 9)[..., None]
        for n in ["half", "closed"]:
            c = load(f"s2_{n}", premul=False)[..., :3] * a  # premultiply with the girl's own alpha
            cel = self.girl.copy()
            cel[..., :3] = self.girl[..., :3] * (1 - m) + c * m
            self.cels[n] = cel
        self.f = deform_fields("s2_girl", (850, 640), (330, 820), (850, 390), (300, 560))
        self.sun = find_sun(self.bg)
        self.petals = Petals(2, 45, wind=(-130, 40), zrange=(0.4, 2.6))
        self.spark = sparkle_points(self.bg, 2, (1150, 480, 1672, 700))
        self.focus = (850, 420)

    def cel_at(self, t):
        f = int(round(t * FPS))
        for b in self.blinks:
            k = f - int(b * FPS)
            if 0 <= k < 2 or 5 <= k < 7:
                return "half"
            if 2 <= k < 5:
                return "closed"
        return "open"

    def frame(self, t):
        u = ease(t / self.dur)
        z = 1.03 + 0.06 * u
        off = (18 - 40 * u, -4 + 6 * u)
        Mb = cam_matrix(z, off, self.focus, 0.4)
        img = warp(self.bg, Mb, opaque=True)[..., :3]
        img = draw_sparkles(img, self.spark, Mb, t)
        sx, sy = apply_pt(Mb, *self.sun)
        img = self.petals.draw(img, t, 0.0, 0.9)
        g = deform(self.cels[self.cel_at(t)], self.f, t, amp_s=13, amp_h=6)
        br = 1 + 0.004 * math.sin(2 * math.pi * t / 3.4)            # breathing
        bob = 2.0 * math.sin(2 * math.pi * t / 3.4 + 0.6)
        extra = np.array([[1, 0, 0], [0, br, (1 - br) * SH + bob]], np.float32)
        gw = warp(g, cam_matrix(z, off, self.focus, 1.0, extra))
        bg = img.copy()
        img = over(img, gw) + light_wrap(bg, gw[..., 3], 0.8)
        img = sun_flare(img, sx, sy, t, 0.7)
        img = self.petals.draw(img, t, 0.9, 9)
        return img


class Shot3:
    dur = 5.0

    def __init__(self):
        self.bg = load("s3_bg")
        self.girl = load("s3_girl")
        self.plane = load("s3_plane")
        ys, xs = np.nonzero(self.plane[..., 3] > 0.05)
        self.plane = self.plane[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
        self.f = deform_fields("s3_girl", (470, 345), (90, 420), (370, 230), (110, 260))
        self.sun = find_sun(self.bg)
        self.petals = Petals(3, 60)
        self.spark = sparkle_points(self.bg, 3, (1150, 440, 1672, 620))
        self.focus = (800, 470)

    def plane_state(self, t):
        u = min(max(t / 4.3, 0), 1)
        s = 1 - (1 - u) ** 1.25
        p0, p1, p2 = np.array([800., 500.]), np.array([1050., 220.]), np.array(self.sun) + np.array([-10., -25.])
        pos = (1 - s) ** 2 * p0 + 2 * (1 - s) * s * p1 + s ** 2 * p2
        tan = 2 * (1 - s) * (p1 - p0) + 2 * s * (p2 - p1)
        heading = math.degrees(math.atan2(-tan[1], tan[0]))
        size = 320 / (1 + 12 * s ** 2.2)
        bank = 7 * math.sin(2.4 * t) * (1 - s)
        vis = 1.0 if u < 0.93 else max(0.0, 1 - (u - 0.93) / 0.07)
        return pos, heading, size, bank, s, vis

    def draw_plane(self, img, t, M):
        acc = np.zeros((OH, OW, 4), np.float32)
        for k in range(5):                                          # motion blur
            pos, heading, size, bank, s, vis = self.plane_state(t + (k - 2) / (FPS * 5))
            ph, pw = self.plane.shape[:2]
            sc = size / pw * M[0, 0]
            # the source art points its nose ~31deg above horizontal
            R = cv2.getRotationMatrix2D((pw / 2, ph / 2), heading - 31 + bank, sc)
            ox, oy = apply_pt(M, *pos)
            R[:, 2] += np.array([ox - pw / 2, oy - ph / 2])
            spr = cv2.warpAffine(self.plane, R.astype(np.float32), (OW, OH), flags=cv2.INTER_LINEAR)
            tint = np.array([0.72, 0.88, 1.0], np.float32) * (1 - 0.3 * s) + np.array([0.55, 0.75, 1.1]) * 0.3 * s
            spr[..., :3] *= tint.astype(np.float32)
            acc += spr * vis / 5
        img = over(img, acc)
        pos, _, _, _, s, vis = self.plane_state(t)
        return img, apply_pt(M, *pos), s

    def frame(self, t):
        u = ease(t / self.dur)
        z = 1.07 - 0.04 * u
        off = (-10 + 20 * u, -20 + 45 * u)
        Mb = cam_matrix(z, off, self.focus, 0.5)
        img = warp(self.bg, Mb, opaque=True)[..., :3]
        img = draw_sparkles(img, self.spark, Mb, t)
        sx, sy = apply_pt(Mb, *self.sun)
        img = self.petals.draw(img, t, 0.0, 0.8)
        img, (px, py), s = self.draw_plane(img, t, Mb)
        g = deform(self.girl, self.f, t, amp_s=12, amp_h=5)
        gw = warp(g, cam_matrix(z, off, self.focus, 1.0))
        bg = img.copy()
        img = over(img, gw) + light_wrap(bg, gw[..., 3])
        glint = max(0.0, 1 - abs(t - 4.15) / 0.35) ** 2
        img = sun_flare(img, sx, sy, t, 0.8 + 0.9 * glint)
        if glint > 0:
            img = sun_flare(img, px, py, t, 0.45 * glint)
        img = self.petals.draw(img, t, 0.8, 9)
        return img


# ---------------------------------------------------------------- driver
_SHOTS = None


def _init():
    global _SHOTS
    _SHOTS = [Shot1(), Shot2(), Shot3()]


def schedule():
    out = []
    for si, (_, d) in enumerate(SHOTS):
        n = int(round(d * FPS))
        out += [(si, i / FPS, n, i) for i in range(n)]
    return out


def render(idx):
    sched = schedule()
    si, t, n, i = sched[idx]
    img = _SHOTS[si].frame(t)
    total = len(sched)
    fade = min(1.0, idx / (0.6 * FPS), (total - 1 - idx) / (0.9 * FPS))
    img = finish(img, idx / FPS, idx, max(0.0, fade))
    return (img * 255 + 0.5).astype(np.uint8)


if __name__ == "__main__":
    total = len(schedule())
    if len(sys.argv) > 2 and sys.argv[1] == "--preview":
        _init()
        for idx in map(int, sys.argv[2].split(",")):
            cv2.imwrite(str(OUTD / f"preview_{idx:04d}.png"), render(idx))
        sys.exit()
    ff = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24",
                           "-s", f"{OW}x{OH}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "14",
                           "-preset", "slow", "-pix_fmt", "yuv420p", "-tune", "animation",
                           str(OUTD / "clip_silent.mp4")], stdin=subprocess.PIPE)
    with Pool(initializer=_init) as pool:
        for k, fr in enumerate(pool.imap(render, range(total), chunksize=4)):
            ff.stdin.write(fr.tobytes())
            if k % 24 == 0:
                print(f"frame {k}/{total}", flush=True)
    ff.stdin.close()
    ff.wait()
    print("done")
