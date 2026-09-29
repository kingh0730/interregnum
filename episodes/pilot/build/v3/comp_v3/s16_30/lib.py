"""Shared helpers for the v3 stills-reel plates of shots 16-30 (RELIEF).

A plate is the keyframe framed by a View (the final crop, clear of paper margins), with every pixel-level effect
baked in: screen textures by homography, lamps, needles, flaps, masked flicker, steam, drops, rain, glow on
emissive sources only, and a static paper grain. reel.py then does the permitted camera move, grade and letterbox.
"""
import json
import subprocess
from pathlib import Path

import cv2
import numpy as np

O = Path(__file__).resolve().parent
R = O.parents[3]
KEYS = R / "work/pilot/keys_v3"
JS = R / "work/pilot/js_v3"
FPS = 24
W0, H0 = 1672, 941


# ------------------------------------------------------------------ colour
def lin(img):
    return np.clip(img, 0, None) ** 2.2


def disp(img):
    return np.clip(img, 0, None) ** (1 / 2.2)


def lum(img):  # BGR
    return img[..., 0] * 0.0722 + img[..., 1] * 0.7152 + img[..., 2] * 0.2126


def hexc(h):  # '#RRGGBB' -> BGR float display
    h = h.lstrip("#")
    return np.array([int(h[4:6], 16), int(h[2:4], 16), int(h[0:2], 16)], np.float32) / 255


def key(name):
    return cv2.imread(str(KEYS / f"{name}.png")).astype(np.float32) / 255.0


def cyan_lit(img, blur=3):
    """Pixels printed in the cold ink (screen light), soft."""
    b, g, r = img[..., 0], img[..., 1], img[..., 2]
    m = np.clip(((b + g) / 2 - r - 0.08) / 0.25, 0, 1) * np.clip((lum(img) - 0.15) / 0.3, 0, 1)
    return cv2.GaussianBlur(m, (0, 0), blur) if blur else m


def red_mask(img, blur=2):
    b, g, r = img[..., 0], img[..., 1], img[..., 2]
    m = np.clip((r - np.maximum(g, b) - 0.18) / 0.25, 0, 1)
    return cv2.GaussianBlur(m, (0, 0), blur) if blur else m


def noise(seed, t, hz):
    r = np.random.default_rng(seed)
    ph = r.uniform(0, 2 * np.pi, 4)
    f = hz * np.array([1.0, 1.618, 2.414, 3.303])
    a = np.array([0.55, 0.25, 0.13, 0.07])
    return float((a * np.sin(2 * np.pi * f * t + ph)).sum())


# ------------------------------------------------------------------ framing
class View:
    """The final framing as a rect in key coords (x0, y0, w; 16:9), rendered at PW x PH."""

    def __init__(self, x0, y0, w, PW=1920, PH=1080):
        self.x0, self.y0, self.w = x0, y0, w
        self.h = w * PH / PW
        self.PW, self.PH = PW, PH
        self.s = PW / w
        self.A = np.float32([[self.s, 0, -self.s * x0], [0, self.s, -self.s * y0]])
        self.A3 = np.vstack([self.A, [0, 0, 1]]).astype(np.float64)

    def img(self, im, interp=cv2.INTER_CUBIC):
        return cv2.warpAffine(im, self.A, (self.PW, self.PH), flags=interp, borderMode=cv2.BORDER_CONSTANT)

    def mask(self, m):
        return np.clip(self.img(m.astype(np.float32), cv2.INTER_LINEAR), 0, 1)

    def pts(self, p):
        p = np.float32(p).reshape(-1, 2)
        return p * self.s + np.float32([-self.s * self.x0, -self.s * self.y0])

    def band(self, aspect=2.39):
        """Visible key-y range under the letterbox."""
        bh = self.w / aspect
        cy = self.y0 + self.h / 2
        return cy - bh / 2, cy + bh / 2


# ------------------------------------------------------------------ quads
def fit_quad(mask):
    """Sharp 4 corners (TL, TR, BR, BL) of a rounded, slightly bulged glowing face: fit a line to the middle of each
    side of the contour and intersect them."""
    m = (mask > 0.5).astype(np.uint8)
    cnts, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    c = max(cnts, key=cv2.contourArea).reshape(-1, 2).astype(np.float32)
    hull = cv2.convexHull(c.reshape(-1, 1, 2)).reshape(-1, 2)
    for eps in np.linspace(0.01, 0.2, 60):
        ap = cv2.approxPolyDP(hull.reshape(-1, 1, 2), eps * cv2.arcLength(hull.reshape(-1, 1, 2), True), True)
        if len(ap) == 4:
            break
    ap = ap.reshape(4, 2)
    s, d = ap.sum(1), np.diff(ap, axis=1).ravel()
    corners = np.float32([ap[np.argmin(s)], ap[np.argmin(d)], ap[np.argmax(s)], ap[np.argmax(d)]])
    lines = []
    for i in range(4):
        a, b = corners[i], corners[(i + 1) % 4]
        ab = b - a
        L = np.linalg.norm(ab)
        u = ab / L
        nrm = np.float32([-u[1], u[0]])
        proj = (c - a) @ u
        dist = np.abs((c - a) @ nrm)
        sel = (proj > 0.25 * L) & (proj < 0.75 * L) & (dist < 0.15 * L)
        pts = c[sel]
        vx, vy, x0, y0 = cv2.fitLine(pts, cv2.DIST_HUBER, 0, 0.01, 0.01).ravel()
        lines.append((np.float32([x0, y0]), np.float32([vx, vy])))
    out = []
    for i in range(4):
        (p1, d1), (p2, d2) = lines[i - 1], lines[i]
        A = np.array([[d1[0], -d2[0]], [d1[1], -d2[1]]], np.float64)
        tt = np.linalg.solve(A, (p2 - p1).astype(np.float64))
        out.append(p1 + d1 * tt[0])
    return np.float32(out)


def glow_mask(img, rect, thr=0.55, close=9):
    """The bright cyan face inside rect (x0, y0, x1, y1) of a key."""
    x0, y0, x1, y1 = rect
    m = np.zeros(img.shape[:2], np.uint8)
    sub = img[y0:y1, x0:x1]
    c = (lum(sub) > thr) & (sub[..., 0] > sub[..., 2] + 0.05)
    m[y0:y1, x0:x1] = c.astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((close, close), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(m)
    big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
    m = (lab == big).astype(np.uint8)
    # fill holes
    cnts, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    f = np.zeros_like(m)
    cv2.drawContours(f, cnts, -1, 1, -1)
    return f.astype(np.float32)


def warp_quad(src, src_rect, quad, size, interp=cv2.INTER_AREA, clip=False):
    """Warp src's rect (x0, y0, x1, y1) onto quad (TL TR BR BL) in an image of size (W, H). clip: keep only the
    rect (for atlases, whose other regions would otherwise land around the quad)."""
    x0, y0, x1, y1 = src_rect
    Hm = cv2.getPerspectiveTransform(np.float32([[x0, y0], [x1, y0], [x1, y1], [x0, y1]]), np.float32(quad))
    out = cv2.warpPerspective(src, Hm, size, flags=interp, borderMode=cv2.BORDER_CONSTANT)
    if clip:
        m = np.zeros(out.shape[:2], np.float32)
        cv2.fillConvexPoly(m, np.int32(np.float32(quad) * 8), 1.0, cv2.LINE_AA, shift=3)
        out = out * m[..., None]
    return out


# ------------------------------------------------------------------ video io
def read_video(path, alpha=False, w=1920, h=1080):
    fmt, ch = ("rgba", 4) if alpha else ("bgr24", 3)
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(path), "-f", "rawvideo", "-pix_fmt", fmt, "-"],
                         stdout=subprocess.PIPE)
    while True:
        buf = p.stdout.read(w * h * ch)
        if len(buf) < w * h * ch:
            break
        f = np.frombuffer(buf, np.uint8).reshape(h, w, ch).astype(np.float32) / 255.0
        if alpha:
            f = f[..., [2, 1, 0, 3]]  # -> BGRA
        yield f
    p.wait()


def hold(gen, n):
    """Yield exactly n frames, holding the last one if the source is short."""
    last = None
    for i in range(n):
        try:
            last = next(gen)
        except StopIteration:
            pass
        yield last


class Writer:
    def __init__(self, path, W, H):
        self.out = Path(path)
        self.i = 0
        self.p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "bgr24",
                                   "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264rgb", "-crf", "6",
                                   "-preset", "fast", str(self.out)], stdin=subprocess.PIPE)

    def write(self, img):
        self.p.stdin.write((np.clip(img, 0, 1) * 255 + 0.5).astype(np.uint8).tobytes())
        self.i += 1

    def close(self):
        self.p.stdin.close()
        self.p.wait()
        print(self.out.name, self.i, "frames")


# ------------------------------------------------------------------ texture / light
def paper(W, H, seed=7, amt=0.02):
    """Static paper grain and ink squash: multiplicative field around 1.0 (baked into the plate, never per frame)."""
    r = np.random.default_rng(seed)
    n = np.zeros((H, W), np.float32)
    for s, a in ((0.7, 0.5), (1.6, 0.35), (4.0, 0.25)):
        g = r.normal(0, 1, (H, W)).astype(np.float32)
        n += a * cv2.GaussianBlur(g, (0, 0), s) * s ** 0.5
    fib = cv2.GaussianBlur(r.normal(0, 1, (H, W)).astype(np.float32), (0, 0), sigmaX=6, sigmaY=0.8)
    n += 0.5 * fib * 2
    n /= n.std()
    return (1 + amt * n)[..., None]


def glow(emit_lin, strength=0.3, s1=4, s2=18):
    """Soft bloom from an emissive-only linear image (screens and lamps)."""
    h, w = emit_lin.shape[:2]
    sm = cv2.resize(emit_lin, (w // 2, h // 2), interpolation=cv2.INTER_AREA)
    g = cv2.GaussianBlur(sm, (0, 0), s1 / 2) * 0.5 + cv2.GaussianBlur(sm, (0, 0), s2 / 2) * 0.5
    return strength * cv2.resize(g, (w, h), interpolation=cv2.INTER_LINEAR)


def load_json(name):
    return json.loads((JS / name).read_text())


def j15_luma(t_abs):
    d = load_json("j15_luma.json")["luma"]
    return d[min(len(d) - 1, int(round(t_abs * FPS)))]
