"""v3 plates for shots 16-30. usage: uv run python shots.py <NN> [...] [--still]
Each shot writes b<NN>.mp4 (plus any static layers) next to this file; --still writes only frame stills to qa/."""
import sys

import cv2
import numpy as np

from lib import *

STILL = "--still" in sys.argv
QA = O / "qa"


class Out:
    """Frame sink: the plate video, or (with --still) a few stills for QA."""

    def __init__(self, name, W, H, n, stills=(0,)):
        self.name, self.n, self.stills, self.i = name, n, stills, 0
        self.w = None if STILL else Writer(O / f"b{name}.mp4", W, H)

    def put(self, img, i=None):
        self.i = self.i if i is None else i
        if self.i in self.stills or (STILL and self.i == self.n - 1):
            cv2.imwrite(str(QA / f"b{self.name}_{self.i:03d}.jpg"), (np.clip(img, 0, 1) * 255).astype(np.uint8),
                        [cv2.IMWRITE_JPEG_QUALITY, 92])
        if self.w:
            self.w.write(img)
        self.i += 1

    def frames(self):
        """Indices to render: all, or only the stills."""
        return range(self.n)

    def done(self):
        if self.w:
            self.w.close()


def want(o, i):
    return not STILL or i in o.stills or i == o.n - 1


def soft(m, grow=0, feather=1.5):
    m = m.astype(np.float32)
    if grow > 0:
        m = cv2.dilate(m, np.ones((2 * grow + 1,) * 2, np.uint8))
    elif grow < 0:
        m = cv2.erode(m, np.ones((-2 * grow + 1,) * 2, np.uint8))
    return np.clip(cv2.GaussianBlur(m, (0, 0), feather), 0, 1) if feather else m


FACE = (240, 0, 1680, 1080)  # the 4:3 tube face inside every screen texture


def screen_mask(im, rect, thr=0.28):
    """Glass mask including the glow's falloff into the bezel (the texture's own dark edge replaces it)."""
    return glow_mask(im, rect, thr=thr, close=5)


# ------------------------------------------------------------------ carved particles
class Steam:
    """A few pale cut ribbons rising from origin, fading out by `height` px (plate px)."""

    def __init__(self, seed, origin, n=5, height=60, sway=6, col=(0.80, 0.86, 0.91), alpha=0.45, width=2):
        r = np.random.default_rng(seed)
        self.o, self.h, self.sway, self.col, self.alpha, self.wd = np.float32(origin), height, sway, col, alpha, width
        self.ph = r.uniform(0, 1, n)
        self.rate = r.uniform(0.28, 0.42, n)
        self.dx = r.uniform(-1, 1, n)
        self.len = r.uniform(0.25, 0.45, n)
        self.fr = r.uniform(0.6, 1.3, n)

    def draw(self, img, t):
        for i in range(len(self.ph)):
            u = (self.ph[i] + t * self.rate[i]) % 1.0
            a = self.alpha * np.sin(np.pi * min(1, u / 0.25) / 2) * (1 - u) ** 1.2
            if a < 0.02:
                continue
            us = np.linspace(u, max(0, u - self.len[i]), 8)
            xs = self.o[0] + self.dx[i] * self.sway * 0.6 + np.sin(us * 7 + i * 1.7 + t * self.fr[i]) * self.sway * us
            ys = self.o[1] - us * self.h
            pts = np.int32(np.stack([xs, ys], 1) * 8)
            lay = np.zeros(img.shape[:2], np.float32)
            cv2.polylines(lay, [pts], False, 1.0, self.wd, cv2.LINE_AA, shift=3)
            m = (lay * a)[..., None]
            img[:] = img * (1 - m) + np.float32(self.col) * m


class Drops:
    """Carved beads on a window pane: stop-and-go slides with a short run above each bead."""

    def __init__(self, seed, mask, n=40, size=2.2, col=(0.86, 0.85, 0.62), alpha=0.55, speed=(0.02, 0.07)):
        r = np.random.default_rng(seed)
        ys, xs = np.nonzero(mask > 0.5)
        self.x0, self.x1, self.y0, self.y1 = xs.min(), xs.max(), ys.min(), ys.max()
        self.mask = mask
        self.x = r.uniform(self.x0, self.x1, n)
        self.y = r.uniform(0, 1, n)
        self.v = r.uniform(*speed, n)
        self.stick = r.uniform(0, 10, n)
        self.s = r.uniform(0.7, 1.3, n) * size
        self.col, self.alpha = np.float32(col), alpha

    def draw(self, img, t):
        lay = np.zeros(img.shape[:2], np.float32)
        H = self.y1 - self.y0
        for i in range(len(self.x)):
            tt = t + self.stick[i]
            # slides in bursts: position advances mostly during short windows
            burst = tt * self.v[i] + 0.04 * np.clip(np.sin(tt * 2.1 + i), 0, 1) ** 4
            yy = self.y0 + ((self.y[i] + burst) % 1.0) * H
            cx, cy, s = self.x[i], yy, self.s[i]
            cv2.ellipse(lay, (int(cx * 8), int(cy * 8)), (int(s * 0.8 * 8), int(s * 8)), 0, 0, 360, 1.0, -1,
                        cv2.LINE_AA, shift=3)
            cv2.line(lay, (int(cx * 8), int((cy - s) * 8)), (int(cx * 8), int((cy - s * 5) * 8)), 0.5,
                     1, cv2.LINE_AA, shift=3)
        m = (lay * self.mask * self.alpha)[..., None]
        img[:] = img * (1 - m) + self.col * m


class Rain:
    """Rain as carved cut lines, visible only where they cross light (alpha follows the local light)."""

    def __init__(self, seed, n, W, H, length=(18, 34), speed=(1.0, 1.5), slant=0.12, width=1, alpha=0.9):
        r = np.random.default_rng(seed)
        self.W, self.H = W, H
        self.x, self.y = r.uniform(0, 1, n), r.uniform(0, 1, n)
        self.len = r.uniform(*length, n)
        self.v = r.uniform(*speed, n)
        self.slant, self.width, self.alpha = slant, width, alpha

    def layer(self, t):
        lay = np.zeros((self.H, self.W), np.float32)
        for i in range(len(self.x)):
            y = ((self.y[i] + self.v[i] * t) % 1.1 - 0.05) * self.H
            x = ((self.x[i] + self.slant * self.v[i] * t * self.H / self.W) % 1.0) * self.W
            L = self.len[i]
            p0 = (int(x * 8), int(y * 8))
            p1 = (int((x - self.slant * L) * 8), int((y - L) * 8))
            cv2.line(lay, p0, p1, 1.0, self.width, cv2.LINE_AA, shift=3)
        return lay * self.alpha


# ------------------------------------------------------------------ Nana's flat and Ida's calls
def shot16():
    im = key("k09_nana_room")
    V = View(16, (941 - 1640 * 9 / 16) / 2, 1640)
    W, H = V.PW, V.PH
    base = V.img(im)
    # the State Receiver's glass
    gk = screen_mask(im, (1420, 340, 1650, 690))
    quad = V.pts(fit_quad(glow_mask(im, (1420, 340, 1650, 690))))
    gm = soft(V.mask(gk), 1, 1.2)[..., None]
    cl = cyan_lit(base) * (1 - soft(V.mask(gk), 8, 4))  # the set's light on the room
    # cream handset for the ring jitter
    hk = np.zeros(im.shape[:2], np.float32)
    sub = im[600:668, 70:262]
    hk[600:668, 70:262] = ((lum(sub) > 0.55) & (sub[..., 2] > sub[..., 0] + 0.05)).astype(np.float32)
    hm = soft(V.mask(cv2.dilate(hk, np.ones((5, 5), np.uint8))), 0, 1.0)[..., None]
    # window panes (dark blue glass, lit windows) for the drops
    wk = np.zeros(im.shape[:2], np.float32)
    for x0, x1 in ((908, 1038), (1060, 1232)):
        wk[196:486, x0:x1] = 1
    plant = (im[..., 1] > im[..., 0] + 0.02) & (im[..., 2] < im[..., 1] + 0.12) & (lum(im) > 0.12)
    wk *= 1 - cv2.dilate(plant.astype(np.float32), np.ones((9, 9), np.uint8))
    wk[380:490, 1100:1240] = 0  # the pot plant on the sill
    drops = Drops(16, soft(V.mask(wk), -2, 1.0), n=46, size=2.0, col=(0.78, 0.84, 0.72), alpha=0.5)
    steam = [Steam(161, V.pts([632, 424])[0], n=5, height=62, sway=7, col=(0.72, 0.84, 0.93), alpha=0.42),
             Steam(162, V.pts([1011, 650])[0], n=4, height=56, sway=5, col=(0.72, 0.84, 0.93), alpha=0.38)]
    pap = paper(W, H, 16, 0.018)
    reflect = cv2.GaussianBlur(cv2.flip(base, 1), (0, 0), 5) * 0.05
    frames = list(read_video(JS / "j15_standby_set.mp4"))
    L = np.array([lum(cv2.resize(f[:, 240:1680], (144, 108))).mean() for f in frames])
    drv = (L - L.mean()) / max(1e-6, (L.max() - L.min()) / 2)
    rings = [(3.5, 3.9), (4.1, 4.5), (5.5, 5.9)]
    rng = np.random.default_rng(3)
    o = Out("16", W, H, 144, stills=(0, 90))
    for i in o.frames():
        if not want(o, i):
            continue
        t = i / FPS
        img = base.copy()
        if any(a <= t < b for a, b in rings):
            dx, dy = rng.choice([-1.15, 1.15]), rng.choice([-1.15, 0, 1.15])
            sh = cv2.warpAffine(img, np.float32([[1, 0, dx], [0, 1, dy]]), (W, H), borderMode=cv2.BORDER_REPLICATE)
            img = img * (1 - hm) + sh * hm
        img = img * (1 + 0.04 * drv[i] * cl[..., None])
        drops.draw(img, t)
        for s in steam:
            s.draw(img, t)
        L_ = lin(img)
        tex = warp_quad(lin(frames[min(i, len(frames) - 1)]), FACE, quad, (W, H))
        L_ = L_ * (1 - gm) + (tex + lin(reflect)) * gm
        L_ += glow(tex * gm, 0.35)
        img = disp(L_) * pap
        o.put(img, i)
    o.done()


def flicker_shot(name, keyname, view, amt, driver, extras=None, emit=None, stills=(0,), n=None):
    """Locked-off close shots: cyan-lit pixels breathe with a driver; optional drops; glow on emissive masks."""
    im = key(keyname)
    V = View(*view)
    W, H = V.PW, V.PH
    base = V.img(im)
    cl = cyan_lit(base)[..., None]
    em = V.mask(emit(im)) if emit else None
    pap = paper(W, H, int(name), 0.018)
    ex = extras(im, V) if extras else []
    o = Out(name, W, H, n, stills=stills)
    for i in o.frames():
        if not want(o, i):
            continue
        t = i / FPS
        img = base * (1 + amt * driver(t) * cl)
        for e in ex:
            e.draw(img, t)
        if em is not None:
            L_ = lin(img)
            L_ += glow(L_ * em[..., None], 0.22)
            img = disp(L_)
        o.put(img * pap, i)
    o.done()


def wall_emit(rect):
    def f(im):
        x0, y0, x1, y1 = rect
        m = np.zeros(im.shape[:2], np.float32)
        sub = im[y0:y1, x0:x1]
        m[y0:y1, x0:x1] = ((lum(sub) > 0.5) & (sub[..., 0] > sub[..., 2] + 0.1)).astype(np.float32)
        return m
    return f


def emit_union(*fs):
    return lambda im: np.clip(sum(f(im) for f in fs), 0, 1)


def shot17():
    flicker_shot("17", "k10_ida_calls", (0, 0, 1672), 0.02, lambda t: noise(171, t, 0.5),
                 emit=emit_union(wall_emit((20, 170, 360, 410)), wall_emit((1220, 330, 1672, 580))), n=96)


def nana_window_drops(rect, plant_box, seed):
    def f(im, V):
        x0, y0, x1, y1 = rect
        wk = np.zeros(im.shape[:2], np.float32)
        sub = im[y0:y1, x0:x1]
        blue = (sub[..., 0] > sub[..., 2] + 0.02) | ((lum(sub) > 0.45) & (sub[..., 2] > sub[..., 0]))
        wk[y0:y1, x0:x1] = blue.astype(np.float32)
        if plant_box:
            a, b, c, d = plant_box
            wk[b:d, a:c] = 0
        wk = cv2.morphologyEx(wk, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
        return [Drops(seed, soft(V.mask(wk), -2, 1.0), n=34, size=2.2, col=(0.78, 0.84, 0.72), alpha=0.45)]
    return f


def shot18():
    flicker_shot("18", "k11_nana_answers", (0, 0, 1672), 0.04, lambda t: (j15_luma(94.0 + t) - 1) / 0.03,
                 extras=nana_window_drops((1245, 175, 1590, 555), (1430, 440, 1600, 560), 18), n=120)


def shot19():
    flicker_shot("19", "k12_ida_question", (0, 0, 1672), 0.02, lambda t: noise(191, t, 0.5),
                 emit=emit_union(wall_emit((0, 170, 360, 530)), wall_emit((1360, 460, 1672, 600))), n=96)


def shot20():
    flicker_shot("20", "k13_nana_ending", (0, 0, 1672), 0.04, lambda t: (j15_luma(103.0 + t) - 1) / 0.03, n=144)


SHOTS = {"16": shot16, "17": shot17, "18": shot18, "19": shot19, "20": shot20}

if __name__ == "__main__":
    import shots_b
    SHOTS.update(shots_b.SHOTS_B)
    for a in sys.argv[1:]:
        if not a.startswith("--"):
            SHOTS[a]()
