"""Animated plates for the locked-off and simple shots (32, 33, 36, 38, 39, 40, 41, 42).
Each plate is the keyframe at source resolution (1672x940) with the Build's in-frame motion baked in; reel.py adds
the camera (32 only), paper, grade and letterbox.   usage: uv run python prep_shots.py 32 33 ..."""
import sys

from common import *

R = np.random.default_rng


def src(name):
    a = key(name)
    return a[: a.shape[0] - a.shape[0] % 2]


def jitter(img, m, dx, dy):
    if dx == 0 and dy == 0:
        return img
    h, w = img.shape[:2]
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    sh = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    ms = cv2.warpAffine(m, M, (w, h), flags=cv2.INTER_LINEAR)[..., None]
    return img * (1 - ms) + sh * ms


def poly_mask(shape, pts, blur=1.0):
    m = np.zeros(shape[:2], np.float32)
    cv2.fillPoly(m, [np.int32(pts)], 1.0, cv2.LINE_AA)
    return feather(m, blur)


def dust_layer(h, w, n, seed, t, region_w, speed=(0.004, 0.01), size=(0.8, 1.8), col=(0.85, 0.96, 0.95), alpha=0.55):
    """Carved dust: small hard-edged pale specks drifting down, visible only where region_w (0..1) is lit."""
    r = R(seed)
    x, y = r.uniform(0, 1, n), r.uniform(0, 1, n)
    z = r.uniform(0.5, 1.5, n)
    vy = r.uniform(*speed, n) * z
    ph = r.uniform(0, 2 * np.pi, n)
    sz = r.uniform(*size, n) * z
    lay = np.zeros((h * 2, w * 2), np.float32)
    xs = (x + 0.004 * np.sin(t * 0.9 + ph) + 0.002 * t) % 1.0
    ys = (y + vy * t) % 1.0
    for xi, yi, si, pi in zip(xs, ys, sz, ph):
        cx, cy = int(xi * w * 2), int(yi * h * 2)
        tw = 0.6 + 0.4 * np.sin(t * 2.1 + pi * 3)          # a speck turning in the light
        cv2.ellipse(lay, (cx, cy), (max(1, int(si * 1.4)), max(1, int(si))), float(pi * 57), 0, 360, float(tw), -1,
                    cv2.LINE_AA)
    lay = cv2.resize(lay, (w, h), interpolation=cv2.INTER_AREA)
    a = np.clip(lay * region_w * alpha, 0, 1)[..., None]
    return a, np.array(col, np.float32)


def steam_sprite():
    """The printed steam ribbon of k19, lifted off its background: (additive difference layer, bg-clean crop)."""
    a = key("k19_nana_listens")
    y0, y1, x0, x1 = 360, 600, 760, 890
    c = a[y0:y1, x0:x1]
    H_, S_, V_ = hsv(c)
    L = lum(c)
    bg = cv2.medianBlur((c * 255).astype(np.uint8), 21).astype(np.float32) / 255
    d = np.clip(lum(c) - lum(bg), 0, 1)
    m = ((S_ < 0.28) & (L > 0.3)).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8))
    hull = np.zeros(m.shape, np.uint8)
    cv2.fillPoly(hull, [np.int32([(72, 8), (100, 12), (106, 60), (98, 110), (104, 150), (92, 185), (76, 218),
                                  (28, 218), (30, 175), (50, 140), (54, 100), (68, 60)])], 1)
    region = cv2.dilate(m * hull, np.ones((7, 7), np.uint8)) * hull
    return (y0, y1, x0, x1), region.astype(np.float32)


def wave_warp(img, t, amp, wl, speed, grow=True, seed=0):
    """Traveling-wave horizontal displacement that climbs the image: steam rising and swaying."""
    h, w = img.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    s = 1 - yy / h                                  # 0 at the bottom (source), 1 at the top
    A = amp * (s ** 1.3 if grow else 1)
    dx = A * np.sin(2 * np.pi * (yy / wl + speed * t) + seed) + 0.4 * A * np.sin(2 * np.pi * (yy / (wl * 0.47) + speed * 1.7 * t) + seed * 2)
    return cv2.remap(img, xx - dx, yy, cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)


# ------------------------------------------------------------------ shots
def s32():
    a = src("k18_ida_from_wall"); h, w = a.shape[:2]
    cm = feather(cyan_mask(a, 0.3), 1.5)[..., None]
    light = feather(cyan_mask(a, 0.25), 60)
    light = np.clip(light / max(light.max(), 1e-3) * 1.4 + 0.25, 0, 1)
    wtr = Writer(OUT / "p32_plate.mov", w, h, alpha=False)
    for i in range(144):
        t = i / FPS
        k = 1 + 0.02 * noise1(t, 0.3, 32)
        im = a * (1 + (k - 1) * cm)
        da, col = dust_layer(h, w, 60, 320, t, light[..., None][..., 0], speed=(0.004, 0.009))
        im = im * (1 - da) + col * da
        wtr.put(im)
    wtr.close()


def s33():
    a = src("k19_nana_listens"); h, w = a.shape[:2]
    cm = feather(cyan_mask(a, 0.3), 1.5)[..., None]
    (y0, y1, x0, x1), reg = steam_sprite()
    crop = a[y0:y1, x0:x1]
    # clean plate under the ribbon (inpaint), then the ribbon as an additive difference layer
    clean = cv2.inpaint((crop * 255).astype(np.uint8), (reg > 0).astype(np.uint8), 9, cv2.INPAINT_TELEA)
    clean = clean.astype(np.float32) / 255
    diff = (crop - clean) * feather(reg, 1.5)[..., None]
    wtr = Writer(OUT / "p33_plate.mov", w, h, alpha=False)
    for i in range(144):
        t = i / FPS
        k = 1 + 0.03 * (0.7 * noise1(t, 0.4, 33) + 0.3 * noise1(t, 2.3, 34))   # the broadcast's luma + noise
        im = a * (1 + (k - 1) * cm)
        # the ribbon: waves climbing it; its density breathes a little
        dw = wave_warp(diff, t, amp=3.5, wl=120, speed=-0.45, seed=0.7)
        dens = 0.85 + 0.15 * np.sin(2 * np.pi * 0.31 * t)
        im[y0:y1, x0:x1] = clean * (1 + (k - 1) * cm[y0:y1, x0:x1]) + dw * dens
        wtr.put(im)
    wtr.close()


def s36():
    a = src("k22_red_phone"); h, w = a.shape[:2]
    H_, S_, V_ = hsv(a)
    red = ((H_ < 25) | (H_ > 340)) & (S_ > 0.45) & (V_ > 0.18)
    hs = poly_mask(a.shape, [(140, 250), (230, 215), (420, 195), (640, 205), (760, 240), (815, 300), (815, 380),
                             (770, 395), (700, 350), (650, 300), (400, 290), (345, 300), (330, 390), (270, 430),
                             (190, 430), (150, 380)], 0)
    hand = (cv2.dilate((red * (hs > 0.5)).astype(np.uint8), np.ones((5, 5), np.uint8)) * (hs > 0.5)).astype(np.float32)
    hand = feather(hand, 0.8)
    lit_edge = hand * np.clip((V_ - 0.45) * 4, 0, 1)
    cm = feather(cyan_mask(a, 0.25), 2)[..., None]
    r = R(36)
    wtr = Writer(OUT / "p36_plate.mov", w, h, alpha=False)
    for i in range(96):
        t = i / FPS
        ring = (0.0 <= t < 1.2) or (3.0 <= t < 4.0)
        im = a * (1 - 0.10 * (t / 4.0) * cm)                     # the Wall going to standby
        if ring:
            dx, dy = r.uniform(-0.6, 0.6), -abs(r.normal(0, 1.3)) * 1.0   # the handset hops in its cradle
            dy = max(dy, -1.3)
            im = im * (1 + 0.02 * r.uniform(-1, 1) * lit_edge[..., None])
            im = jitter(im, hand, dx, dy)
        wtr.put(im)
    wtr.close()


def s38():
    a = src("k23_ida_nana"); h, w = a.shape[:2]
    H_, S_, V_ = hsv(a)
    red = (((H_ < 25) | (H_ > 340)) & (S_ > 0.4) & (V_ > 0.12)).astype(np.uint8)
    reg = np.zeros((h, w), np.uint8); reg[630:880, 0:660] = 1
    phone = cv2.morphologyEx(red * reg, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    phone = feather(cv2.dilate(phone, np.ones((5, 5), np.uint8)).astype(np.float32), 1.0) * reg
    am = feather(amber_mask(a, 0.3), 1.5)[..., None]
    r = R(38)
    wtr = Writer(OUT / "p38_plate.mov", w, h, alpha=False)
    for i in range(72):
        t = i / FPS
        k = 1 + 0.02 * noise1(t, 0.3, 380)
        im = a * (1 + (k - 1) * am)
        if 2.0 <= t < 3.0:
            im = jitter(im, phone, r.uniform(-0.9, 0.9), r.uniform(-0.9, 0.9))
        wtr.put(im)
    wtr.close()


def ghost39():
    """The burned-in ghost (J15 ghost texture) on k24's switched-off set. The set is seen obliquely at the right
    edge; its 4:3 face runs off frame, so the quad extends past x 1672."""
    a = src("k24_nana_know"); h, w = a.shape[:2]
    g = rd(JS / "j15_standby_ghost.png")
    g = g[:, 240:1680]                                             # the 4:3 face
    gh, gw = g.shape[:2]
    dst = np.float32([[1606, 268], [1790, 238], [1790, 772], [1606, 740]])
    M = cv2.getPerspectiveTransform(np.float32([[0, 0], [gw, 0], [gw, gh], [0, gh]]), dst)
    gw_ = cv2.warpPerspective(g, M, (w, h), flags=cv2.INTER_AREA)
    # the dark glass: dark pixels right of the bezel inside the quad
    q = np.zeros((h, w), np.float32); cv2.fillPoly(q, [np.int32(dst)], 1.0, cv2.LINE_AA)
    glass = q * np.clip((0.16 - lum(a)) * 12, 0, 1)
    glass = feather(glass, 1.5)
    return gw_, glass


def s39():
    a = src("k24_nana_know"); h, w = a.shape[:2]
    gw_, glass = ghost39()
    base = a + np.clip(gw_ - 0.02, 0, 1) * glass[..., None]          # light held by the dark glass (additive)
    am = feather(amber_mask(a, 0.3), 1.5)[..., None]
    wtr = Writer(OUT / "p39_plate.mov", w, h, alpha=False)
    for i in range(96):
        t = i / FPS
        k = 1 + 0.01 * noise1(t, 1.7, 39)
        wtr.put(base * (1 + (k - 1) * am))
    wtr.close()
    wr(OUT / "p39_check.jpg", np.clip(base[200:800, 1400:], 0, 1) ** 0.5)


def flicker_plate(name, n, amt, hz, seed, out):
    a = src(name); h, w = a.shape[:2]
    am = feather(amber_mask(a, 0.3), 1.5)[..., None]
    wtr = Writer(OUT / out, w, h, alpha=False)
    for i in range(n):
        t = i / FPS
        k = 1 + amt * noise1(t, hz, seed)
        wtr.put(a * (1 + (k - 1) * am))
    wtr.close()


def s40():
    flicker_plate("k28_ida_how_long", 72, 0.02, 0.3, 40, "p40_plate.mov")


def s41():
    flicker_plate("k29_nana_since", 120, 0.01, 1.7, 41, "p41_plate.mov")


def s42():
    a = src("k25_ida_home"); h, w = a.shape[:2]
    cm = feather(cyan_mask(a, 0.25), 1.5)[..., None]
    am = feather(amber_mask(a, 0.3), 1.5)[..., None]
    # the steam sprite from k19's printed ribbon, scaled to a thin wisp at the cap's thread
    (y0, y1, x0, x1), reg = steam_sprite()
    k19 = key("k19_nana_listens"); crop = k19[y0:y1, x0:x1]
    clean = cv2.inpaint((crop * 255).astype(np.uint8), (reg > 0).astype(np.uint8), 9, cv2.INPAINT_TELEA)
    diff = np.clip((crop - clean.astype(np.float32) / 255), 0, 1) * feather(reg, 1.5)[..., None]
    sc = 0.85
    spr = cv2.resize(diff, None, fx=sc, fy=sc, interpolation=cv2.INTER_AREA)
    rows = np.nonzero(spr.sum(axis=(1, 2)) > 0.05)[0]
    spr = spr[: rows.max() + 1]
    sh, sw = spr.shape[:2]
    # anchor: the sprite's bottom-centre of the ribbon at the cap's thread (k25 cap ~ x 555, thread y ~ 580)
    cols = np.nonzero(spr[-12:].sum(axis=(0, 2)))[0]
    bx = int(cols.mean()) if len(cols) else sw // 2
    ax, ay = 575, 575
    X0, Y0 = ax - bx, ay - sh
    wtr = Writer(OUT / "p42_plate.mov", w, h, alpha=False)
    for i in range(168):
        t = i / FPS
        f = ease_sine((t - 1.0) / 5.0)
        im = a * (1 - 0.6 * f * cm)                                   # the cold rim fades by 60 %
        k = 1 + 0.015 * noise1(t, 0.3, 42)
        im = im * (1 + (k - 1) * am)
        g = ease_sine(t / 7.0)                                        # HALL -> warm across the shot
        im = im * np.array([1 + 0.035 * g, 1 + 0.005 * g, 1 - 0.07 * g], np.float32)
        if t >= 4.5:
            u = t - 4.5
            grow = np.clip(u / 1.6, 0, 1)                              # the wisp climbs out of the thread
            dw = wave_warp(spr, t, amp=4.0, wl=90, speed=-0.5, seed=1.3)
            yy = np.arange(sh)[:, None, None] / sh
            reveal = np.clip((yy - (1 - grow)) / 0.15, 0, 1)
            dens = 0.75 * np.clip(u / 0.6, 0, 1)
            im[Y0:Y0 + sh, X0:X0 + sw] += dw * reveal * dens
        wtr.put(im)
    wtr.close()


if __name__ == "__main__":
    for s in sys.argv[1:]:
        globals()["s" + s]()
        print("done", s)
