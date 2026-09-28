"""Keyframe shots 32, 33, 35, 36, 38-42: bake mask-driven light effects into a plate video at key resolution,
then write the reel.py spec (camera, particles, grade, letterbox). usage: uv run plates.py 32 [33 ...]"""
import sys

from fx import *


def run(n, dur, img, fn):
    """fn(t, img) -> frame. Writes p{n}.mp4 and returns its repo-relative path."""
    h, w = img.shape[:2]
    out = HERE / f"p{n}.mp4"
    wr = Writer(out, w, h)
    for i in range(int(round(dur * FPS))):
        wr.write(fn(i / FPS))
    wr.close()
    return rel(out)


def jitter_region(img, mask, dx, dy):
    """Shift the masked region by (dx, dy) sub-pixel and composite it over the image."""
    h, w = img.shape[:2]
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    si = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    sm = cv2.warpAffine(mask, M, (w, h), flags=cv2.INTER_LINEAR)[..., None]
    return img * (1 - sm) + si * sm


def red_mask(img):
    r, g, b = img[..., 0], img[..., 1], img[..., 2]
    return ((r > 0.25) & (r > 1.8 * g) & (r > 1.6 * b)).astype(np.float32)


def ring_env(t, windows):
    return any(a <= t < b for a, b in windows)


# ------------------------------------------------------------------ 32 Ida looks up
def s32():
    k = key("k18")
    m = cyan_mask(k)[..., None]

    def f(t):
        return k * (1 + m * (0.02 * snoise(32, t, 0.3)))

    p = run(32, 6.0, k, f)
    spec(32, 6.0, [{"src": p}],
         camera={"from": focus_cam(0.49, 0.58, 1.06), "to": [0.5, 0.5, 1.0], "ease": "inout"},
         particles=[{"kind": "dust", "n": 60, "seed": 32, "par": 1.1, "wind": [0.003, 0.0],
                     "color": [0.75, 0.9, 1.0], "opacity": 0.55, "size": 0.9}],
         grade_=grade("HALL"))


# ------------------------------------------------------------------ 33 Nana listens
class Steam:
    def __init__(self, w, h, origin, n=26, seed=33, spread=60, rise=260, color=(1.0, 0.86, 0.7), alpha=0.10):
        r = np.random.default_rng(seed)
        self.w, self.h, self.o = w, h, origin
        self.ph = r.uniform(0, 1, n)            # life phase
        self.x0 = r.uniform(-spread, spread, n)
        self.sp = r.uniform(0.18, 0.3, n)        # lives per second
        self.wob = r.uniform(0, 6.28, n)
        self.rise, self.col, self.a = rise, np.array(color, np.float32), alpha

    def draw(self, t):
        sw, sh = self.w // 2, self.h // 2
        f = np.zeros((sh, sw), np.float32)
        life = (self.ph + self.sp * t) % 1.0
        for li, x0, wb in zip(life, self.x0, self.wob):
            y = self.o[1] - li * self.rise
            x = self.o[0] + x0 * (0.4 + li) + 25 * np.sin(wb + t * 0.9 + li * 4) + 40 * li
            rad = 10 + 40 * li
            a = np.sin(np.pi * li) ** 1.5
            cv2.circle(f, (int(x / 2), int(y / 2)), int(rad / 2), float(a), -1, cv2.LINE_AA)
        f = blur(f, 9)
        f = cv2.resize(f, (self.w, self.h))
        return np.clip(f, 0, 1)[..., None] * self.a


def s33():
    k = key("k19")
    h, w = k.shape[:2]
    m = cyan_mask(k)[..., None]
    st = Steam(w, h, (848, 505), alpha=0.14)
    rs = RainShadow(w, h, 0.03, seed=33)

    def f(t):
        fl = 0.03 * snoise(33, t, 0.4) + 0.006 * snoise(34, t, 9)
        img = k * (1 + m * fl) * rs.field(t)
        s = st.draw(t)
        return img + s * st.col * (1 - img)                 # screen-ish, warm-lit steam

    p = run(33, 6.0, k, f)
    spec(33, 6.0, [{"src": p}],
         camera={"from": [0.5, 0.5, 1.0], "to": focus_cam(0.45, 0.30, 1.04), "ease": "inout"},
         grade_=grade("HOME"))


# ------------------------------------------------------------------ 35 ON AIR off
def s35():
    k = key("k21")
    h, w = k.shape[:2]
    red = red_mask(k)
    bright = (red > 0) & (lum(k) > 0.18)
    n, lab, stats, _ = cv2.connectedComponentsWithStats(bright.astype(np.uint8))
    i = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
    gx, gy, gw, gh = stats[i, :4]
    glass = (lab == i).astype(np.uint8)
    glass = cv2.morphologyEx(glass, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8)).astype(np.float32)
    glass = blur(glass, 1.5)
    print("glass", gx, gy, gw, gh)
    # the ON AIR lettering, 60 % of the glass width, centred, warped by the glass rectangle
    mk = cv2.imread(str(JS / "s35_onair_mask.png"), cv2.IMREAD_UNCHANGED)
    a = mk[..., 3].astype(np.float32) / 255 if mk.shape[2] == 4 else cv2.cvtColor(mk, cv2.COLOR_BGR2GRAY) / 255.0
    ys, xs = np.nonzero(a > 0.05)
    a = a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    lw = 0.60 * gw
    lh = lw * a.shape[0] / a.shape[1]
    cx, cy = gx + gw / 2, gy + gh / 2
    src = np.float32([[0, 0], [a.shape[1], 0], [a.shape[1], a.shape[0]], [0, a.shape[0]]])
    dst = np.float32([[cx - lw / 2, cy - lh / 2], [cx + lw / 2, cy - lh / 2], [cx + lw / 2, cy + lh / 2],
                      [cx - lw / 2, cy + lh / 2]])
    letters = cv2.warpPerspective(a, cv2.getPerspectiveTransform(src, dst), (w, h), flags=cv2.INTER_AREA)
    letters = blur(letters, 0.8) * glass
    L = letters[..., None]
    G = glass[..., None]
    # lit state: hotter, slightly orange letters
    on = k + L * np.array([0.0, 0.16, 0.05], np.float32) * G
    # off state: glass at 12 %, letters a touch darker; the red halo in the haze removed
    r, g, b = k[..., 0], k[..., 1], k[..., 2]
    excess = np.clip(r - g * 0.95, 0, None)              # the navy wall has r ~ g; the red haze lifts r
    dist = cv2.distanceTransform((1 - (glass > 0.5)).astype(np.uint8), cv2.DIST_L2, 5)
    halo_w = np.exp(-dist / 260.0)
    off = k.copy()
    off[..., 0] = r - excess * halo_w * 0.95
    off[..., 2] = b - np.clip(b - g * 1.6, 0, None) * halo_w * 0.5   # the magenta cast in the haze
    glass_off = k * 0.12 * (1 - 0.3 * L)
    off = off * (1 - G) + glass_off * G
    t_off, ramp = 0.4, 3 / FPS

    def f(t):
        u = np.clip((t - t_off) / ramp, 0, 1)
        img = on * (1 - u) + off * u
        if t >= t_off:
            ag = np.exp(-max(0.0, t - t_off - ramp * 0.5) / 0.3) * u
            img = img + G * (0.22 * ag) * np.array([1.0, 0.42, 0.08], np.float32) * (0.4 + 0.6 * L)
        return img

    p = run(35, 2.0, k, f)
    spec(35, 2.0, [{"src": p}], grade_=grade("HALL"))


# ------------------------------------------------------------------ 36 red phone
def s36():
    k = key("k22")
    h, w = k.shape[:2]
    rm = red_mask(k)
    yy = np.arange(h)[:, None] / h
    xx = np.arange(w)[None, :] / w
    hand = rm * (yy < 0.44) * (xx > 0.12) * (xx < 0.52)       # the handset, top of the phone
    hand = cv2.dilate(hand, np.ones((5, 5), np.uint8))
    hand = blur(hand, 1.2)
    hl = (hand * np.clip((lum(k) - 0.08) * 8, 0, 1))[..., None]
    cm = cyan_mask(k)[..., None]
    rng = np.random.default_rng(36)
    offs = rng.uniform(-1.5, 1.5, (200, 2))

    def f(t):
        i = int(round(t * FPS))
        img = k * (1 - 0.10 * cm * (t / 4.0))
        if ring_env(t, [(0.0, 1.2), (3.0, 4.0)]):
            dx, dy = offs[i]
            img = jitter_region(img, hand, dx, dy * 0.6)
            img = img * (1 + 0.02 * (1 if i % 2 else -1) * hl)
        return img

    p = run(36, 4.0, k, f)
    spec(36, 4.0, [{"src": p}],
         camera={"from": [0.5, 0.5, 1.0], "to": focus_cam(0.45, 0.5, 1.03), "ease": "inout"},
         grade_=grade("HALL"))


# ------------------------------------------------------------------ 38, 40 Ida answers
def s38():
    k = key("k23")
    h, w = k.shape[:2]
    rm = red_mask(k)
    yy = np.arange(h)[:, None] / h
    xx = np.arange(w)[None, :] / w
    ph = blur(cv2.dilate(rm * (yy > 0.6) * (xx < 0.45), np.ones((5, 5), np.uint8)), 2.0)
    am = amber_mask(k)[..., None]
    rng = np.random.default_rng(38)
    offs = rng.uniform(-1.0, 1.0, (100, 2))

    def f(t):
        img = k * (1 + am * 0.02 * snoise(38, t, 0.3))
        if 2.0 <= t < 3.0:
            dx, dy = offs[int(round(t * FPS))]
            img = jitter_region(img, ph, dx, dy)
        return img

    p = run(38, 3.0, k, f)
    spec(38, 3.0, [{"src": p}],
         camera={"from": [0.5, 0.5, 1.0], "to": focus_cam(0.42, 0.37, 1.02), "ease": "inout"},
         grade_=grade("HALL", gain=[1.0, 1.0, 1.02]))


def tight_crop(name, fx_, fy_, z, out_name):
    k = key(name)
    h, w = k.shape[:2]
    cx, cy, _ = focus_cam(fx_, fy_, z)
    cw, ch = w / z, h / z
    M = np.float32([[1920 / cw, 0, -(cx * w - cw / 2) * 1920 / cw], [0, 1080 / ch, -(cy * h - ch / 2) * 1080 / ch]])
    im = cv2.warpAffine(k, M, (1920, 1080), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REFLECT)
    sh = im + 0.5 * (im - blur(im, 0.8))           # gentle sharpening (~0.3 px equivalent at source scale)
    sh = np.clip(sh, 0, 1)
    save_png(HERE / out_name, sh)
    return sh


def s40():
    k = tight_crop("k23", 0.42, 0.37, 1.25, "k23b_ida_answers_tight.png")
    am = amber_mask(k)[..., None]
    p = run(40, 3.0, k, lambda t: k * (1 + am * 0.02 * snoise(40, t, 0.3)))
    spec(40, 3.0, [{"src": p}],
         camera={"from": [0.5, 0.5, 1.0], "to": focus_cam(0.42, 0.37, 1.28 / 1.25), "ease": "inout"},
         grade_=grade("HALL", gain=[1.0, 1.0, 1.02], grain=0.026))


# ------------------------------------------------------------------ 39, 41 Nana amber
def s39():
    k = key("k24")
    h, w = k.shape[:2]
    am = amber_mask(k)[..., None]
    rs = RainShadow(w, h, 0.03, seed=39)

    def f(t):
        fl = 0.01 * (0.6 * snoise(39, t, 5) + 0.4 * snoise(40, t, 0.7))
        return k * (1 + am * fl * np.array([1.0, 0.9, 0.7], np.float32)) * rs.field(t)

    p = run(39, 4.0, k, f)
    spec(39, 4.0, [{"src": p}],
         camera={"from": [0.5, 0.5, 1.0], "to": focus_cam(0.63, 0.35, 1.03), "ease": "inout"},
         grade_=grade("HOME", gain=[1.06, 1.0, 0.93]))


def s41():
    k = tight_crop("k24", 0.62, 0.40, 1.20, "k24b_nana_amber_tight.png")
    h, w = k.shape[:2]
    am = amber_mask(k)[..., None]
    rs = RainShadow(w, h, 0.03, seed=41)

    def f(t):
        fl = 0.01 * (0.6 * snoise(41, t, 5) + 0.4 * snoise(42, t, 0.7))
        return k * (1 + am * fl * np.array([1.0, 0.9, 0.7], np.float32)) * rs.field(t)

    p = run(41, 5.0, k, f)
    spec(41, 5.0, [{"src": p}],
         camera={"from": [0.5, 0.5, 1.0], "to": focus_cam(0.62, 0.40, 1.24 / 1.20), "ease": "inout"},
         grade_=grade("HOME", gain=[1.06, 1.0, 0.93], grain=0.026))


# ------------------------------------------------------------------ 42 come home
def s42(glint=True):
    k = key("k25")
    h, w = k.shape[:2]
    cm = cyan_mask(k, s=15)[..., None]
    am = amber_mask(k)[..., None]
    p0, p1 = np.array([606.0, 345.0]), np.array([621.0, 395.0])

    def f(t):
        u = ease_sine((t - 1.0) / 5.0)
        img = k * (1 - 0.6 * cm * u)
        warm = np.array([1 + 0.05 * u, 1 + 0.012 * u, 1 - 0.06 * u], np.float32)
        img = img * (1 + (warm - 1) * (1 - 0.5 * am))
        img = img * (1 + am * 0.015 * snoise(42, t, 0.3))
        if glint and 1.5 <= t <= 4.5:
            v = ((t - 1.5) / 3.0) ** 2                       # easeIn
            c = p0 + (p1 - p0) * v
            env = np.sin(np.pi * (t - 1.5) / 3.0) ** 0.5
            g = np.zeros((h, w), np.float32)
            cv2.circle(g, (int(c[0] * 16), int(c[1] * 16)), 3 * 16, 1.0, -1, cv2.LINE_AA, shift=4)
            g = blur(g, 1.2)[..., None] * 0.6 * env
            img = img * (1 - g) + g
        return img

    p = run(42, 7.0, k, f)
    spec(42, 7.0, [{"src": p}],
         camera={"from": [0.5, 0.5, 1.0], "to": focus_cam(0.31, 0.35, 1.04), "ease": "inout"},
         grade_=grade("HALL", lift=[0.03, 0.035, 0.06], gain=[1.0, 1.0, 1.01]))


if __name__ == "__main__":
    for a in sys.argv[1:]:
        globals()["s" + a]()
