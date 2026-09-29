"""Pre-comps for v3 shots 01-15. usage: uv run work/pilot/comp_v3/pre_0115.py NN [--sheet]"""
import sys, json, os
sys.path.insert(0, __import__("os").path.dirname(__file__))
from lib0115 import *

SHEET = "--sheet" in sys.argv


def run(shot, n, fn, out):
    """Render n frames of fn(i) into CV/out (mp4); with --sheet only 6 frames to a sheet."""
    if SHEET:
        idx = np.linspace(0, n - 1, 6).astype(int)
        if os.environ.get("FRAMES"):
            idx = [int(x) for x in os.environ["FRAMES"].split(",")]
        fr = []
        for i in range(n):
            if i in idx:
                f = fn(i)
                if i in idx:
                    fr.append(f)
        sheet(fr, SCR / f"pre{shot}.jpg", cols=min(3, len(fr)), scale=float(os.environ.get("SCALE", 0.25)))
        print(SCR / f"pre{shot}.jpg")
        return
    w = VWriter(CV / out)
    for i in range(n):
        w.write(fn(i))
    w.close()
    print(CV / out, n)


# ------------------------------------------------------------------ 01
def s01():
    v = VReader(JS / "j01_lighting.mp4")
    def fn(i):
        f = v.get(i)[..., :3]
        pic = grade_broadcast(f[:, PX0:PX0 + PW], lift=0.0, sat=0.0)
        return broadcast(pic, i, bloom_amt=0.04, twitter=False)
    fn.seq = True
    run("01", 120, fn, "01_pre.mp4")




# ------------------------------------------------------------------ 02 / 03: the Father on k01 / k02
def father_pic(src, s, focus):
    """Centre 4:3 crop of a 16:9 key at 1440x1080, pushed to scale s about focus (fractions of the picture)."""
    h, w = src.shape[:2]
    cw = h * 4 / 3
    k = PW / cw
    x0 = (w - cw) / 2
    fx, fy = focus[0] * PW, focus[1] * PH
    # source -> crop: X = k*(x - x0), Y = k*y ; push: X' = fx + s*(X - fx)
    M = np.float32([[s * k, 0, fx + s * (-k * x0 - fx)], [0, s * k, fy + s * (0 - fy)]])
    return cv2.warpAffine(src, M, (PW, PH), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)


def push_affine(s, focus):
    """The same push, as an affine on picture space (for overlays placed on the unpushed picture)."""
    fx, fy = focus[0] * PW, focus[1] * PH
    return np.float32([[s, 0, fx * (1 - s)], [0, s, fy * (1 - s)]])


PUSH03 = (1.04, (0.50, 0.42))
K02P = "work/pilot/v3/k02_proof.png"   # k02 with the cream disc toned down for monitors (tone_disc.py)


def father_shot(shot, key, s1, focus, n, stutter=None, freeze=None):
    src = load(KEYS / f"{key}.png")
    bug = VReader(JS / f"j14_bug_cc_{shot}.mov")
    held = {}

    def picture(i):
        t = i / FPS
        if freeze is not None and t >= freeze:
            t = freeze
        s = 1 + (s1 - 1) * min(t / (n / FPS), 1)
        pic = father_pic(src, s, focus)
        pic = pic * (1 + 0.015 * np.sin(2 * np.pi * 0.3 * t))
        return np.clip(pic, 0, 1), s

    def fn(i):
        j = i
        if stutter and stutter[0] < i <= stutter[0] + 2:
            j = stutter[0]  # hold the previous frame for 2 frames
        pic, _ = picture(j)
        b = bug.get(i)
        bb = bug.last if j == i else held.get(j, b)
        held[i] = b
        pic = grade_broadcast(pic)
        pic = over(pic, premul(bb[:, PX0:PX0 + PW]))
        if stutter and i == stutter[0] + 3:
            y0, y1 = stutter[1]
            pic[y0:y1] = np.roll(pic[y0:y1], 3, 1)
        return broadcast(pic, j)
    fn.seq = True
    if shot == "03" and not SHEET:
        # 04's frozen picture is k02 unpushed (the frame the J16 mesh was placed on); 04's sync tear
        # carries the picture from 03's final 1.04 push back to 1.00, so the cut does not jump. f04_frozen feeds
        # the 05 Wall insert, so it is the Proof variant (cream disc toned down, tone_disc.py).
        save(CV / "f04_frozen.png", father_pic(load(K02P), 1.0, focus))
    run(shot, n, fn, f"{shot}_pre.mp4")


def s02():
    father_shot("02", "k01_father_mcu", 1.035, (0.50, 0.40), 168, stutter=(100, (450, 570)))


def s03():
    father_shot("03", "k02_father_cu", PUSH03[0], PUSH03[1], 168, freeze=6.9)


# ------------------------------------------------------------------ p04: the Proof (04, 06)
Q04 = [[361.0, 196.7], [947.2, 267.2], [989.5, 714.2], [379.5, 717.0]]    # glass quad, plate space
TIP0 = np.float32([930, 537])                                             # the pen tip in p04
RING = np.float32([1227.5, 574.5])    # J03's pen circle, texture space (measured on the engraved-k02 J03; smooth k02: 1209, 557)
LAMPS04 = [[1252 + 3 * i, 354 + 56 * i, 52, 38] for i in range(6)]      # x, y, w, h (5 and 6 extrapolated)
FLAPS04 = [[1205, 230], [1347, 230], [1347, 312], [1205, 312]]            # the four-card window unit
HOOD_PLATE = [[572, 739], [768, 739], [768, 775], [572, 775]]


def hand_matte():
    f = CV / "p04_hand_matte.png"
    if f.exists():
        return load(f)[..., 0]
    p = plate("p04_proof")
    img = (p * 255).astype(np.uint8)[..., ::-1].copy()
    mask = np.full(img.shape[:2], cv2.GC_BGD, np.uint8)
    poly = np.int32([(912, 522), (1080, 495), (1180, 450), (1275, 455), (1325, 515), (1368, 605), (1405, 695),
                     (1520, 700), (1920, 755), (1920, 1080), (1190, 1080), (1190, 810), (1110, 725), (1015, 705),
                     (985, 600), (925, 562)])
    pm = np.zeros(mask.shape, np.uint8)
    cv2.fillPoly(pm, [poly], 1)
    mask[pm > 0] = cv2.GC_PR_FGD
    r, g, b = p[..., 0], p[..., 1], p[..., 2]
    skin = (r > 0.45) & (r > g * 1.12) & (r < g * 1.7) & (g > b * 1.05) & (g > 0.3) & (pm > 0)
    mask[skin] = cv2.GC_FGD
    mask[1000:1080, 1450:1920] = cv2.GC_FGD
    pen = np.zeros(mask.shape, np.uint8)
    cv2.line(pen, (935, 538), (1150, 575), 1, 9)
    mask[pen > 0] = cv2.GC_FGD
    for x, y, w, h in LAMPS04[:4]:
        mask[y - 4:y + h + 4, x - 4:x + w + 4] = cv2.GC_BGD
    col = np.zeros(mask.shape, bool)
    col[330:700, 1236:1345] = True
    mask[col & (r > 0.55) & (g < r * 0.62)] = cv2.GC_BGD
    cv2.setRNGSeed(1)
    bg, fg = np.zeros((1, 65)), np.zeros((1, 65))
    cv2.grabCut(img, mask, None, bg, fg, 6, cv2.GC_INIT_WITH_MASK)
    m = np.where((mask == 1) | (mask == 3), 1.0, 0.0).astype(np.float32)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    z = m[430:730, 1180:1420].copy()     # the back of the hand against the lamp column: close the hatching
    zc = cv2.morphologyEx(z, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (31, 31)))
    zc = cv2.morphologyEx(zc, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
    m[430:730, 1180:1420] = np.maximum(z, zc)
    m = cv2.GaussianBlur(m, (0, 0), 0.8)
    save(f, np.dstack([m, m, m]))
    return m


def glass_mask04():
    p = plate("p04_proof")
    r, g, b = p[..., 0], p[..., 1], p[..., 2]
    face = ((b > 0.6) & (g > 0.55) & (r < 0.8)).astype(np.uint8)
    n, lab, st, _ = cv2.connectedComponentsWithStats(face)
    i = np.argmax(st[1:, 4]) + 1
    m = (lab == i).astype(np.uint8)
    hull = cv2.convexHull(cv2.findNonZero(m))
    g = np.zeros_like(m)
    cv2.fillConvexPoly(g, hull, 1)
    g = cv2.dilate(g, np.ones((5, 5), np.uint8))
    return cv2.GaussianBlur(g.astype(np.float32), (0, 0), 1.2)


def ring_plate():
    Hm = quad_H(rect_quad(240, 0, 1440, 1080), Q04)
    return cv2.perspectiveTransform(RING[None, None], Hm)[0, 0]


def make_p04():
    """p04 with the hand moved so the pen tip sits on the ghost ear; returns (bg, hand_rgba_straight)."""
    fb, fh = CV / "p04_bg.png", CV / "p04_handlayer.png"
    if fb.exists() and fh.exists():
        return load(fb), load(fh, alpha=True)
    p = plate("p04_proof")
    m = hand_matte()
    D = ring_plate() + np.float32([-4, 4]) - TIP0          # tip just short of the ring's centre
    Y, X = np.mgrid[0:H, 0:W].astype(np.float32)
    w = np.clip((1860 - X) / (1860 - 1380), 0, 1)
    w = w * w * (3 - 2 * w)
    mx, my = X - D[0] * w, Y - D[1] * w
    hand = cv2.remap(np.dstack([p * m[..., None], m]), mx, my, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    # background: clone the lamp column / hood cheek downward one lamp pitch at a time, then inpaint the rest
    bg = p.copy()
    hole = cv2.dilate((m > 0.02).astype(np.uint8), np.ones((13, 13), np.uint8))
    hole[505:700, 1236:1335] = 1
    x0, x1 = 1140, 1350
    pitch, dxp = 56, 3
    for yy in range(470, 942):
        row = hole[yy, x0:x1] > 0
        if yy < 692:
            src = bg[yy - pitch, x0 - dxp:x1 - dxp]
        else:  # below lamp 6: the plain strip between lamps, repeated
            sy = 398 + (yy - 692) % 6
            sh = int(round(dxp * (yy - sy) / pitch))
            src = bg[sy, x0 - sh:x1 - sh]
        bg[yy, x0:x1][row] = src[row]
    hole2 = hole.copy()
    hole2[470:900, x0:x1] = 0
    bg8 = (np.clip(bg, 0, 1) * 255).astype(np.uint8)
    bg = cv2.inpaint(bg8, hole2, 9, cv2.INPAINT_TELEA).astype(np.float32) / 255
    save(fb, bg)
    save(fh, np.dstack([hand[..., :3] / np.maximum(hand[..., 3:], 1e-4), hand[..., 3:]]))
    print("hand moved by", D)
    return bg, load(fh, alpha=True)


FLAPWIN04 = [[1205, 230, 32, 80], [1242, 230, 33, 80], [1281, 230, 30, 80], [1315, 230, 32, 80]]
_cache = {}


def cached(key, fn):
    if key not in _cache:
        _cache[key] = fn()
    return _cache[key]


def reflection04_():
    """8 % glass reflection: the Wall's glowing grid (a darkened, blurred crop of k03) minus Ida's head."""
    k = plate("k03_hall_wide")
    wall = k[300:560, 700:1220]
    wall = cv2.GaussianBlur(wall, (0, 0), 3)
    Hm = quad_H(rect_quad(0, 0, wall.shape[1], wall.shape[0]), [[330, 170], [1010, 250], [1040, 700], [350, 700]])
    r = warp(lin(wall), Hm)
    head = np.zeros((H, W), np.float32)
    cv2.ellipse(head, (700, 520), (120, 150), -8, 0, 360, 1, -1, cv2.LINE_AA)     # her head, behind the camera
    cv2.ellipse(head, (700, 760), (290, 150), 0, 180, 360, 1, -1, cv2.LINE_AA)    # shoulders
    head = cv2.GaussianBlur(head, (0, 0), 25)
    return r * (1 - 0.9 * head[..., None])


def reflection04():
    r = reflection04_()
    return cv2.GaussianBlur(r, (0, 0), 5)


def lamp_insert(img, atlas, i, quad_xywh):
    """Atlas lamp i (600x120 at 100, 60+150i) into a plate lamp: legend fitted to the lens width."""
    x, y, w, h = quad_xywh
    a = atlas[60 + 150 * i + 12:60 + 150 * i + 108, 112:688]          # the lens, 576 x 96
    rgb = a[..., :3]
    lens_w, lens_h = w - 6, h - 6
    base = cv2.resize(cv2.GaussianBlur(rgb, (0, 0), 20), (lens_w, lens_h), interpolation=cv2.INTER_AREA)
    th = max(4, int(round(lens_w * 96 / 576)))
    txt = cv2.resize(rgb, (lens_w, th), interpolation=cv2.INTER_AREA)
    y0 = (lens_h - th) // 2
    base[y0:y0 + th] = txt
    m = round_rect_mask(lens_w, lens_h, 3, 0.6)[..., None]
    sub = img[y + 3:y + 3 + lens_h, x + 3:x + 3 + lens_w]
    img[y + 3:y + 3 + lens_h, x + 3:x + 3 + lens_w] = base * m + sub * (1 - m)
    return img


def flaps_insert(img, atlas):
    cards = [[200, 330, 340, 420], [560, 330, 340, 420], [1020, 330, 340, 420], [1380, 330, 340, 420]]
    for (cx, cy, cw, ch), (x, y, w, h) in zip(cards, FLAPWIN04):
        c = atlas[cy:cy + ch, cx:cx + cw]
        c = cv2.resize(c, (w - 2, h - 2), interpolation=cv2.INTER_AREA)
        pm = premul(c)
        # the card is lit only by the room: darken to sit in the hood's shadow
        pm[..., :3] *= 0.8
        img[y + 1:y + h - 1, x + 1:x + w - 1] = over(img[y + 1:y + h - 1, x + 1:x + w - 1], pm)
    return img


def hood_plate(img):
    j = load(JS / "j20_hood_plate.png", alpha=True)
    j[..., :3] = j[..., :3] * np.float32([0.5, 0.54, 0.6])       # into the hood's shadow
    e = cv2.GaussianBlur(j[..., 3], (0, 0), 1.0)
    j[..., :3] *= (0.75 + 0.25 * np.clip(1 - (np.roll(e, 1, 0) - e) * 4, 0, 1))[..., None]
    Hm = quad_H(rect_quad(0, 0, j.shape[1], j.shape[0]), HOOD_PLATE)
    pm = warp(premul(j), Hm, interp=cv2.INTER_AREA)
    return over(img, pm)


def proof_frame(tex, lamps_atlas, flaps_atlas, t, hand_dx=0.0, lift=0.0, shadow=None, refl_amt=0.06):
    """Compose p04 at plate scale with a tube texture (texture space: rect x240-1680). Display-referred out."""
    bg = cached("p04bg", lambda: make_p04()[0])
    hand = cached("p04hand", lambda: make_p04()[1])
    G = cached("G04", glass_mask04)
    Ht = cached("Ht04", lambda: quad_H(rect_quad(240, 0, 1440, 1080), Q04))
    refl = cached("refl04", reflection04)
    img = bg.copy()
    img = hood_plate(img)
    for i in range(6):
        img = lamp_insert(img, lamps_atlas, i, LAMPS04[i])
    img = flaps_insert(img, flaps_atlas)
    T = warp(tex[..., :3], Ht, interp=cv2.INTER_LINEAR)
    tl = lin(T) + refl * refl_amt * G[..., None]
    img = disp(lin(img) * (1 - G[..., None]) + tl * G[..., None])
    # the hand: -dx along the arm (tapered to the frame edge), lift = 2 px up and scale 0.98 about the wrist
    Y, X = np.mgrid[0:H, 0:W].astype(np.float32)
    w = np.clip((1860 - X) / (1860 - 1380), 0, 1)
    w = w * w * (3 - 2 * w)
    s = 1 - 0.02 * lift
    wx, wy = 1240, 700
    mx = wx + (X - wx) / (s * w + (1 - w)) - hand_dx * w
    my = wy + (Y - wy) / (s * w + (1 - w)) + 2 * lift * w
    hp = cv2.remap(premul(hand), mx, my, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    if shadow:
        off, op, blur = shadow
        a = hp[..., 3]
        sh = cv2.GaussianBlur(np.roll(np.roll(a, int(round(off)), 0), int(round(off)), 1), (0, 0), blur)
        img = img * (1 - op * sh * G)[..., None]
    img = over(img, hp)
    return img


def s06():
    tex = VReader(JS / "j03_proof_06.mp4")
    lamps = VReader(JS / "j03_lamps_06.mov")
    flaps = VReader(JS / "j_flaps_06.mov")

    def fn(i):
        t = i / FPS
        dx = -6 * ease_inout_cubic((t - 1.1) / 1.1)          # the drag: -6 px over 1.1-2.2
        lift = min(max((t - 2.2) / 0.25, 0), 1)
        # the shadow on the glass reaches the ear first (0.3-1.0), then separates on the lift
        a = min(max((t - 0.3) / 0.7, 0), 1)
        off = 9 - 4 * a + 4 * lift
        op = 0.18 + 0.17 * a - 0.12 * lift
        return proof_frame(tex.get(i), lamps.get(i), flaps.get(i), t, hand_dx=dx, lift=lift,
                           shadow=(off, op, 6 + 3 * lift))
    fn.seq = True
    run("06", 168, fn, "06_pre.mp4")


# ------------------------------------------------------------------ 04: freeze and pull out of the picture
MONITOR04 = np.float32([(0, 18), (272, 26), (1160, 158), (1342, 188), (1352, 1080), (0, 1080)])


def glass_tex(rw, rad):
    """Texture-space tube: the glass rounded rect (x240-1680) and the raster window (width rw, centred at 955)."""
    gm = np.zeros((H, W), np.float32)
    gm[:, PX0:PX0 + PW] = round_rect_mask(PW, PH, max(rad, 1), 1.0) if rad > 0.5 else 1
    return gm


def tube04(pic, u, frame, blur_sig=0.0):
    """pic: 1440x1080 display (picture + overlay). u in [0,1]: 0 = the flat broadcast picture, 1 = the Proof's tube
    as J03 draws it (raster 1090 wide at x 410-1500, barrel k1 .05, glass border, vignette, bloom). Returns
    (texture 1920x1080 display RGB, glass mask)."""
    k1 = 0.05 * u
    rw = int(round(PW - (PW - 1090) * u))
    cx = 960 - 5 * u
    r = cv2.resize(pic, (rw, PH), interpolation=cv2.INTER_AREA)   # as J03's CRT draws the raster
    rb, rm = barrel(r, k1, mask_round=0.02 * u + 1e-3)
    # misconvergence growing toward the corners (1 px), vignette, bloom/halation
    if u > 0:
        hh, ww = rb.shape[:2]
        Y, X = np.mgrid[0:hh, 0:ww].astype(np.float32)
        nx, ny = (X - ww / 2) / (ww / 2), (Y - hh / 2) / (hh / 2)
        d = 1.2 * u * (nx * nx + ny * ny) / 2
        rb[..., 0] = cv2.remap(rb[..., 0], X - d * nx, Y - d * ny, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        rb[..., 2] = cv2.remap(rb[..., 2], X + d * nx, Y + d * ny, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        rb = rb * (1 - u * (1 - vignette(ww, hh, 0.25)))[..., None]
    x = lin(rb)
    x = bloom(x, 0.55, 0.10 + 0.12 * u, (3, 12))
    rb = disp(x)
    tex = np.zeros((H, W, 3), np.float32)
    glassc = np.float32([0.047, 0.056, 0.064])
    gm = glass_tex(rw, 110 * u)
    tex[:] = glassc * gm[..., None]
    xs = int(round(cx - rw / 2))
    sub = tex[:, xs:xs + rw]
    tex[:, xs:xs + rw] = rb * rm[..., None] + sub * (1 - rm[..., None])
    if u > 0:
        dust = cached("dust04", _glass_dust)
        tex = tex * (1 - u * dust[..., :1]) + u * dust[..., 1:2] * 0.25
    if blur_sig > 0.3:
        tex = cv2.GaussianBlur(tex, (0, 0), blur_sig)
    return tex, gm


def _glass_dust():
    r = np.random.default_rng(4)
    dk = np.zeros((H, W), np.float32)
    lt = np.zeros((H, W), np.float32)
    for _ in range(60):
        x, y = r.uniform(260, 1660), r.uniform(20, 1060)
        rr = r.uniform(1, 3)
        cv2.circle(dk if r.random() < .5 else lt, (int(x * 4), int(y * 4)), int(rr * 4), float(r.uniform(.2, .6)), -1, cv2.LINE_AA, shift=2)
    # the light-pen smear over the ear
    cv2.ellipse(lt, (int(round(RING[0])), int(round(RING[1]))), (60, 34), -35, 0, 360, 0.35, -1, cv2.LINE_AA)
    lt = cv2.GaussianBlur(lt, (0, 0), 1.0)
    lt[400:740, 1100:1340] = cv2.GaussianBlur(lt[400:740, 1100:1340], (0, 0), 9)
    return np.dstack([cv2.GaussianBlur(dk, (0, 0), .8) * .35, lt * .5])


def sim(z, F, p0=None):
    """Similarity camera: frame = z*(p - F) + F (as a 3x3)."""
    return np.float64([[z, 0, F[0] * (1 - z)], [0, z, F[1] * (1 - z)], [0, 0, 1]])


def monitor_matte():
    m = poly_mask(MONITOR04, feather=1.0)
    G = cached("G04", glass_mask04)
    return m


def s04():
    src = load(KEYS / "k02_father_cu.png")
    frozen = father_pic(src, 1.0, PUSH03[1])                  # the broadcast picture (as 03 left it)
    frozen_p = father_pic(load(K02P), 1.0, PUSH03[1])         # the Proof variant: the disc tones down as it becomes the tube
    bug = VReader(JS / "j14_bug_cc_03.mov").get(167).copy()
    ov = VReader(JS / "j16_proof_overlay_04.mov")
    lamps = VReader(JS / "j03_lamps_04.mov")
    flaps = VReader(JS / "j_flaps_04.mov")
    bg, hand = make_p04()
    G = glass_mask04()
    Ht = quad_H(rect_quad(240, 0, 1440, 1080), Q04)
    refl = reflection04()
    Mm = monitor_matte()
    c0 = np.float32(Q04).mean(0)
    z0 = 1440 / ((np.linalg.norm(np.subtract(Q04[1], Q04[0])) + np.linalg.norm(np.subtract(Q04[2], Q04[3]))) / 2)
    F = (z0 * c0 - np.float32([960, 540])) / (z0 - 1)
    rect = np.float32(rect_quad(240, 0, 1440, 1080))

    def fn(i):
        t = i / FPS
        ovf = ov.get(i)
        lf, ff = lamps.get(i), flaps.get(i)
        if i <= 2:                                            # the sync tear, out of 03's push
            s = PUSH03[0] - (PUSH03[0] - 1) * i / 3
            pic = grade_broadcast(father_pic(src, s, PUSH03[1]))
            pic = over(pic, premul(bug[:, PX0:PX0 + PW]))
            k = [0.35, 1.0, 0.6][i]
            out = np.zeros_like(pic)
            for y in range(PH):
                sh = int(round(40 * k * (y / PH) ** 1.4))
                out[y, sh:] = pic[y, :PW - sh] if sh else pic[y]
            return broadcast(out, i)
        if t < 0.15:                                          # frozen; the bug has gone with the signal
            return broadcast(grade_broadcast(frozen), 3)
        # --- the room
        u = ease_inout_cubic((t - 0.15) / 0.35)               # the picture takes the curve of the glass
        v = ease_out_cubic((t - 0.15) / 1.85)                 # the pull (0.15-2.0)
        z = z0 ** (1 - v)
        zm = 1 + (z - 1) * 1.06                                # the monitor rides 6 % ahead of the hall
        C = sim(z, F)
        Cm = sim(zm, F)
        des = 0.4 * ease_inout_cubic((t - 0.15) / 1.85)
        pic = desat(frozen * (1 - u) + frozen_p * u, des)
        pic = over(pic, premul(ovf[:, PX0:PX0 + PW]))
        eff = zm * 598 / 1440
        tex, gm = tube04(pic, u, i, blur_sig=max(0, 0.45 / eff - 0.45))
        # the plate at plate scale (lamps, flaps, hood plate)
        room = bg.copy()
        room = hood_plate(room)
        for k in range(6):
            room = lamp_insert(room, lf, k, LAMPS04[k])
        room = flaps_insert(room, ff)
        fade = ease_inout_cubic((t - 0.15) / 0.3)
        hall = warp(room, C.astype(np.float32), border=cv2.BORDER_REPLICATE) * fade
        mon = warp(np.dstack([room * Mm[..., None], Mm]), Cm.astype(np.float32), border=cv2.BORDER_CONSTANT)
        img = over(hall, mon * np.float32([fade, fade, fade, 1]))
        # tube: texture -> frame, corners eased from the flat picture rect to the glass in the room
        q_room = cv2.perspectiveTransform(np.float32(Q04)[None], Cm.astype(np.float32))[0]
        q = rect + (q_room - rect) * u
        Hf = quad_H(rect, q) @ quad_H(rect_quad(240, 0, 1440, 1080), rect)
        Hf = quad_H(rect_quad(240, 0, 1440, 1080), q)
        T = warp(tex, Hf)
        Gt = warp(gm, Hf)
        Gr = warp(G, Cm.astype(np.float32))
        mask = Gt * (1 - u + u * Gr)
        rf = warp(refl, Cm.astype(np.float32)) * 0.06 * ease_inout_cubic((t - 0.6) / 1.4)
        tl = lin(T) + rf
        img = disp(lin(img) * (1 - mask[..., None]) + tl * mask[..., None])
        hp = warp(premul(hand), Cm.astype(np.float32), border=cv2.BORDER_REPLICATE)
        hp = hp * np.float32([fade, fade, fade, 1])
        img = over(img, hp)
        # letterbox in, pillarbox out
        bar = int(round(138 * ease_inout_cubic((t - 0.15) / 0.30)))
        if bar:
            img[:bar] = 0
            img[H - bar:] = 0
        return img
    fn.seq = True
    run("04", 72, fn, "04_pre.mp4")


# ------------------------------------------------------------------ 05: the Hall, the Wall in 84 tiles
SHIFT05 = 50     # the plate is lowered 50 px so the clock clears the top bar (the replicated rows sit under it)


def wall_tiles():
    k = plate("k03_hall_wide")
    r, g, b = k[..., 0], k[..., 1], k[..., 2]
    m = ((b > 0.6) & (g > 0.6)).astype(np.uint8)
    m[:, :650] = 0; m[:, 1270:] = 0; m[:280] = 0; m[600:] = 0
    n, lab, st, cen = cv2.connectedComponentsWithStats(m)
    tiles = [(st[i], (lab == i)) for i in range(1, n) if st[i, 4] > 150]
    xs = sorted(set(int(round(s[0] / 10)) for s, _ in tiles))
    cols = sorted(set(s[0] for s, _ in tiles))
    # grid indices by clustering
    def idx(v, allv):
        u = sorted(allv)
        groups = []
        for x in u:
            if not groups or x - groups[-1][-1] > 12:
                groups.append([x])
            else:
                groups[-1].append(x)
        for gi, gr in enumerate(groups):
            if gr[0] - 1 <= v <= gr[-1] + 1:
                return gi, len(groups)
    out = []
    for s, mk in tiles:
        c, nc = idx(s[0], [t[0][0] for t in tiles])
        rr, nr = idx(s[1], [t[0][1] for t in tiles])
        out.append((c, rr, s, mk))
    return out, nc, nr


def s05():
    k = plate("k03_hall_wide")
    frozen = load(CV / "f04_frozen.png")
    mesh = load("work/pilot/v3/f04_mesh_state.png", alpha=True)
    pic = desat(over(frozen, premul(mesh[:, PX0:PX0 + PW])), 0.6)
    tiles, nc, nr = wall_tiles()
    print("wall tiles", len(tiles), nc, "x", nr)
    x0 = min(s[0] for _, _, s, _ in tiles); x1 = max(s[0] + s[2] for _, _, s, _ in tiles)
    y0 = min(s[1] for _, _, s, _ in tiles); y1 = max(s[1] + s[3] for _, _, s, _ in tiles)
    aspect = (x1 - x0) / (y1 - y0)
    ch = PW / aspect
    cy0 = 520 - ch / 2
    crop = pic[int(cy0):int(cy0 + ch)]
    rng = np.random.default_rng(5)
    prm = []
    for c, rr, s, mk in tiles:
        sx, sy, sw, sh = s[:4]
        u0, u1 = c / nc, (c + 1) / nc
        v0, v1 = rr / nr, (rr + 1) / nr
        sub = crop[int(v0 * ch):int(v1 * ch), int(u0 * PW):int(u1 * PW)]
        sub = cv2.resize(sub, (sw + 2, sh + 2), interpolation=cv2.INTER_AREA)
        sub = barrel(sub, 0.04)
        sub = sub * vignette(sw + 2, sh + 2, 0.25)[..., None]
        tint = 1 + rng.uniform(-0.08, 0.08, 3).astype(np.float32)
        gain = 1 + rng.uniform(-0.10, 0.10)
        dead = (c == nc - 1 and rr == 0)
        hum = (c == 3 and rr == nr - 1)
        mm = cv2.dilate(mk.astype(np.uint8), np.ones((3, 3), np.uint8))[sy - 1:sy + sh + 1, sx - 1:sx + sw + 1]
        mm = cv2.GaussianBlur(mm.astype(np.float32), (0, 0), 0.6)
        prm.append(dict(c=c, r=rr, box=(sx - 1, sy - 1), sub=sub, m=mm, tint=tint, gain=gain, dead=dead, hum=hum,
                        seed=int(rng.integers(1e6))))
    # dust: specks rising from the grilles, lit only where the Wall's light falls
    L = cv2.GaussianBlur(k.mean(-1), (0, 0), 25)
    L = np.clip((L - 0.05) / 0.25, 0, 1)
    dr = np.random.default_rng(9)
    ND = 120
    dx, dy = dr.uniform(560, 1360, ND), dr.uniform(300, 1080, ND)
    dv, ds, dph = dr.uniform(8, 22, ND), dr.uniform(0.8, 2.0, ND), dr.uniform(0, 6.28, ND)

    def fn(i):
        t = i / FPS
        img = k.copy()
        glow = np.zeros((H, W, 3), np.float32)
        for p in prm:
            x, y = p["box"]
            h_, w_ = p["m"].shape
            if p["dead"]:
                col = np.full((h_, w_, 3), 0.03, np.float32)
            else:
                col = p["sub"][:h_, :w_] * p["tint"] * p["gain"] * (1 + 0.02 * smooth_noise(p["seed"], t, 0.4))
                col = 0.12 + 0.95 * col                              # phosphor floor: the tube is lit
                if p["hum"]:
                    ph = (1 - (t % 7) / 7)
                    yy = np.arange(h_)[:, None, None] / h_
                    col = col * (1 - 0.18 * np.exp(-((yy - ph) / 0.18) ** 2))
            mm = p["m"][..., None]
            img[y:y + h_, x:x + w_] = col * mm + img[y:y + h_, x:x + w_] * (1 - mm)
            glow[y:y + h_, x:x + w_] += col * mm
        x = lin(img)
        gl = cv2.GaussianBlur(lin(glow), (0, 0), 6)
        x = x + 0.25 * gl
        # dust
        lay = np.zeros((H, W), np.float32)
        for j in range(ND):
            yy = (dy[j] - dv[j] * t - 300) % 780 + 300
            xx = dx[j] + 6 * np.sin(t * 0.7 + dph[j])
            cv2.circle(lay, (int(xx * 8), int(yy * 8)), int(ds[j] * 8), 1.0, -1, cv2.LINE_AA, shift=3)
        lay = lay * L * 0.25
        x = x + lay[..., None] * lin(np.float32([0.75, 0.9, 0.9]))
        out = disp(x)
        out = np.vstack([np.repeat(out[:1], SHIFT05, 0), out[:H - SHIFT05]])
        return out
    run("05", 192, fn, "05_pre.mp4")
    # the near covers (parallax layer): everything below a dark row between two rows of covers
    if not SHEET:
        kk = np.vstack([np.repeat(k[:1], SHIFT05, 0), k[:H - SHIFT05]])
        rows = kk[700:780].mean(-1)
        rows[:, 880:1040] = 1                                   # ignore the aisle
        ycut = 700 + int(np.argmin(rows.mean(1)))
        a = np.zeros((H, W), np.float32)
        a[ycut:] = 1
        a = cv2.GaussianBlur(a, (0, 0), 1.0)
        save(CV / "05_near.png", np.dstack([kk, a]))
        print("near covers cut at", ycut)


# ------------------------------------------------------------------ 07 / 13: Ida, locked off; the tube's light lives
def cyan_mask(k):
    r, g, b = k[..., 0], k[..., 1], k[..., 2]
    l = k.mean(-1)
    m = np.clip((b - r - 0.04) / 0.12, 0, 1) * np.clip((g - r) / 0.08, 0, 1) * np.clip((l - 0.12) / 0.2, 0, 1)
    return cv2.GaussianBlur(m.astype(np.float32), (0, 0), 1.5)


def ida_locked(shot, key, n, amt, hz, dust_n, dust_box, seed):
    k = plate(key)
    M = cyan_mask(k)
    ramp = np.clip((0.62 * W - np.arange(W)) / (0.08 * W), 0, 1)[None, :]   # her tube only, not the Wall
    M = (M * ramp)[..., None]
    kl = lin(k)
    dr = np.random.default_rng(seed)
    x0, y0, x1, y1 = dust_box
    dx, dy = dr.uniform(x0, x1, dust_n), dr.uniform(y0, y1, dust_n)
    dvx, dvy = dr.uniform(-4, 4, dust_n), dr.uniform(-10, -3, dust_n)
    ds = dr.uniform(0.8, 1.8, dust_n)
    L = cv2.GaussianBlur(M[..., 0], (0, 0), 30)
    L = L / max(L.max(), 1e-3)

    def fn(i):
        t = i / FPS
        f = 1 + amt * smooth_noise(seed, t, hz)
        x = kl * (1 + (f - 1) * M)
        if dust_n:
            lay = np.zeros((H, W), np.float32)
            for j in range(dust_n):
                xx = x0 + (dx[j] - x0 + dvx[j] * t) % (x1 - x0)
                yy = y0 + (dy[j] - y0 + dvy[j] * t) % (y1 - y0)
                cv2.circle(lay, (int(xx * 8), int(yy * 8)), int(ds[j] * 8), 1.0, -1, cv2.LINE_AA, shift=3)
            x = x + (lay * L * 0.22)[..., None] * lin(np.float32([0.8, 0.95, 0.95]))
        return disp(x)
    run(shot, n, fn, f"{shot}_pre.mp4")


def s07():
    ida_locked("07", "k04_ida_desk", 96, 0.03, 0.8, 20, (120, 200, 900, 900), 71)


def s13():
    ida_locked("13", "k07_ida_no", 96, 0.01, 0.6, 0, (0, 0, 1, 1), 131)


# ------------------------------------------------------------------ 08: the Archive Reader
SHIFT08 = 70     # the plate is raised 70 px so the doctor's tag clears the bottom bar


def s08():
    p = plate("p08_archive")
    at = VReader(JS / "j04_archive.mp4")
    win = [[330, 246], [1562, 246], [1562, 406], [330, 406]]
    Hs = quad_H(rect_quad(0, 40, 1920, 276), win)
    wm = poly_mask([[362, 250], [1540, 250], [1540, 403], [362, 403]], feather=1.5)
    maps = [  # (atlas rect, plate quad, mode)
        ((110, 445, 520, 140), rect_quad(105, 588, 450, 162), "drum"),
        ((920, 445, 310, 140), rect_quad(750, 598, 285, 150), "drum"),
        ((270, 612, 320, 54), rect_quad(225, 772, 220, 37), "over"),
        ((975, 612, 260, 54), rect_quad(805, 772, 180, 37), "over"),
        ((1455, 836, 370, 44), rect_quad(1300, 474, 216, 26), "over"),
        ((1470, 900, 340, 80), rect_quad(1098, 668, 118, 28), "over"),
    ]
    Hm = [(quad_H(rect_quad(*a), q), poly_mask(q, feather=0.8), mode) for a, q, mode in maps]
    # the scope: atlas circle (1640, 580) r 200 -> plate (1408, 687) r 148
    sc = 148 / 200
    Hsc = np.float32([[sc, 0, 1408 - 1640 * sc], [0, sc, 687 - 580 * sc], [0, 0, 1]])
    scm = np.zeros((H, W), np.float32)
    cv2.circle(scm, (1408 * 4, 687 * 4), 148 * 4, 1, -1, cv2.LINE_AA, shift=2)
    scm = cv2.GaussianBlur(scm, (0, 0), 1)
    # the doctor's tag: the handwriting runs down the tag's length
    tag = np.float32([[1718, 845], [1797, 832], [1830, 1000], [1765, 1012]])
    tagm = poly_mask(tag, feather=1.0)
    d = (tag[2] + tag[3]) / 2 - (tag[0] + tag[1]) / 2
    d = d / np.linalg.norm(d)
    up = np.float32([d[1], -d[0]])
    p0 = (tag[0] + tag[1]) / 2 + d * 42
    L, hh = 128, 30
    tq = [p0 + up * hh / 2, p0 + d * L + up * hh / 2, p0 + d * L - up * hh / 2, p0 - up * hh / 2]
    Htag = quad_H(rect_quad(175, 830, 460, 95), tq)
    pl = lin(p)

    def fn(i):
        t = i / FPS
        a = at.get(i)[..., :3]
        x = pl.copy()
        strip = lin(warp(a, Hs))
        x = x * (1 - wm[..., None]) + x * strip * wm[..., None]
        for Hh, m, mode in Hm:
            s = lin(warp(a, Hh))
            if mode == "drum":
                s = s * 0.55                                   # the drums sit in the desk's shade
            x = x * (1 - m[..., None]) + s * m[..., None]
        s = lin(warp(a, Hsc))
        x = x * (1 - scm[..., None]) + s * scm[..., None]
        # the tag: dark until the scope's spill finds it at 4.9, then the ink shows
        k = ease_inout_cubic((t - 4.9) / 0.4)
        lit = 0.25 + 0.75 * k
        tint = np.float32([1, 1, 1]) * (1 - k) + np.float32([0.85, 1.0, 0.95]) * k
        tagl = x * lit * tint
        ink = warp(a, Htag).mean(-1)
        inka = np.clip((0.19 - ink) / 0.12, 0, 1) * 0.85
        tagl = tagl * (1 - inka[..., None] * np.float32([0.9, 0.9, 0.85]))
        x = x * (1 - tagm[..., None]) + tagl * tagm[..., None]
        out = disp(x)
        return np.vstack([out[SHIFT08:], np.repeat(out[-1:], SHIFT08, 0)])
    fn.seq = True
    run("08", 216, fn, "08_pre.mp4")


# ------------------------------------------------------------------ 10: the capsule
CAP_SRC = (830, 694, 265, 112)       # x, y, w, h of the capsule in k05b
CAP_REST = np.float32([962.5, 750 + 32])   # its centre at rest in k05's cup
LIP10 = [(726, 712), (790, 736), (846, 752), (849, 843), (1079, 843), (1082, 752), (1122, 738), (1157, 714),
         (1162, 1080), (726, 1080)]


def s10():
    a = plate("k05_cradle")
    b = plate("k05b_capsule")
    x, y, w, h = CAP_SRC
    cap = b[y:y + h, x:x + w]
    cm = round_rect_mask(w, h, 22, 1.2)
    capl = np.dstack([cap * cm[..., None], cm])                  # premultiplied
    lip = poly_mask(LIP10, feather=0.8)
    lipimg = np.dstack([a * lip[..., None], lip])
    # the rim's pale line (for the 3-frame brighten at 1.40)
    rim = ((a.mean(-1) > 0.55) & (poly_mask([(720, 680), (1170, 680), (1170, 770), (720, 770)]) > 0.5)).astype(np.float32)
    rim = cv2.GaussianBlur(rim, (0, 0), 1.2)
    mouth = np.float32([1030, 520])
    r = np.random.default_rng(10)
    NP = 30
    px, py = r.uniform(760, 1140, NP), r.uniform(690, 720, NP)
    pvx, pvy = r.uniform(-60, 60, NP), r.uniform(-90, -30, NP)
    psz = r.uniform(1.2, 3.0, NP)

    def cap_at(tt):
        """centre, scale, angle of the capsule at time tt (None before it appears)."""
        if tt < 1.20:
            return None
        if tt < 1.35:
            u = (tt - 1.20) / 0.15
            u = u * u                                             # gravity: ease-in
            c = mouth + (CAP_REST - mouth) * u
            return c, 0.6 + 0.4 * u, 28 * (1 - u)
        tr = tt - 1.35
        ang = 1.5 * np.sin(2 * np.pi * tr / 0.3) * np.exp(-tr / 0.12) if tr < 0.6 else 0.0
        return CAP_REST, 1.0, ang

    def place(c, s, ang):
        M = cv2.getRotationMatrix2D((w / 2, h / 2), ang, s)
        M[:, 2] += c - np.float32([w / 2, h / 2])
        return cv2.warpAffine(capl, M, (W, H), flags=cv2.INTER_LINEAR)

    def fn(i):
        t = i / FPS
        img = a.copy()
        st = cap_at(t)
        if st is not None:
            if t < 1.36:      # 5-subframe motion blur while it flies
                acc = np.zeros((H, W, 4), np.float32)
                for k in range(5):
                    s2 = cap_at(max(1.20, t - k / FPS / 5)) or st
                    acc += place(*s2)
                cl = acc / 5
            else:
                cl = place(*st)
            img = over(img, cl)
            img = over(img, lipimg)
        if 34 <= i <= 36:
            img = img + rim[..., None] * 0.25 * (1 - img)
        if t >= 1.35:          # the puff: pale carved specks off the rim
            tr = t - 1.35
            lay = np.zeros((H, W), np.float32)
            for j in range(NP):
                xx = px[j] + pvx[j] * tr * np.exp(-tr)
                yy = py[j] + pvy[j] * (1 - np.exp(-tr * 2.5)) / 2.5 * 1.0
                cv2.rectangle(lay, (int(xx), int(yy)), (int(xx + psz[j]), int(yy + psz[j] * 0.7)), 1.0, -1)
            op = max(0, 1 - tr / 1.2) * 0.7
            lay = cv2.GaussianBlur(lay, (0, 0), 0.5) * op
            img = img * (1 - lay[..., None]) + np.float32([0.85, 0.82, 0.72]) * lay[..., None]
            # the shake: 6 px, decaying over 0.3 s
            amp = 6 * np.exp(-tr / 0.1)
            if amp > 0.3:
                dx = amp * np.sin(2 * np.pi * 18 * tr)
                dy = amp * 0.6 * np.cos(2 * np.pi * 14 * tr)
                img = cv2.warpAffine(img, np.float32([[1, 0, dx], [0, 1, dy]]), (W, H), borderMode=cv2.BORDER_REPLICATE)
        return img
    run("10", 72, fn, "10_pre.mp4")


# ------------------------------------------------------------------ 11: the order
SLIP11 = [[475, 382], [1458, 376], [1458, 678], [475, 684]]


def s11():
    k = plate("k06_order")
    Hm = quad_H(rect_quad(0, 0, 1600, 480), SLIP11)
    x = lin(k)
    for layer in ("j06_form", "j06_typing", "j06_stamp"):
        j = load(JS / f"{layer}.png", alpha=True)
        j = j[:480, :1600]
        pm = warp(premul(j), Hm, interp=cv2.INTER_AREA)
        pm = cv2.GaussianBlur(pm, (0, 0), 0.6)
        a = pm[..., 3:4]
        col = pm[..., :3] / np.maximum(a, 1e-4)
        x = x * (1 - a) + x * lin(col) * a           # multiply: the ink sits in the onionskin grain
    sm = poly_mask(SLIP11, feather=6)[..., None]

    def fn(i):
        t = i / FPS
        f = 1 + 0.01 * smooth_noise(111, t, 0.8)
        return disp(x * (1 + (f - 1) * sm))
    run("11", 144, fn, "11_pre.mp4")


# ------------------------------------------------------------------ 12: the loop
PRINTER12 = [(700, 1080), (980, 760), (1130, 560), (1205, 448), (1400, 420), (1920, 405), (1920, 1080)]
PAPER12 = [[1632, 30], [2000, -12], [1935, 472], [1476, 472]]     # texture rect (560,0,800,930) -> plate
NEEDLE_PIVOT = np.float32([1030, 386])


def s12():
    p = plate("p12_loop")
    r, g, b = p[..., 0], p[..., 1], p[..., 2]
    face = ((b > 0.6) & (g > 0.6)).astype(np.uint8)
    n, lab, st, _ = cv2.connectedComponentsWithStats(face)
    i0 = np.argmax(st[1:, 4]) + 1
    fm = (lab == i0).astype(np.uint8)
    Q = fit_quad(fm)
    print("tube quad", np.round(Q, 1).tolist())
    hull = cv2.convexHull(cv2.findNonZero(fm))
    G = np.zeros_like(fm)
    cv2.fillConvexPoly(G, hull, 1)
    G = cv2.GaussianBlur(cv2.dilate(G, np.ones((5, 5), np.uint8)).astype(np.float32), (0, 0), 1.2)
    Ht = quad_H(rect_quad(240, 0, 1440, 1080), Q)
    # the plate's own needle out, the meter face inpainted
    nm = np.zeros((H, W), np.uint8)
    cv2.line(nm, (1030, 386), (958, 290), 1, 11)
    cv2.line(nm, (958, 290), (948, 276), 1, 7)
    base = cv2.inpaint((p * 255).astype(np.uint8), nm, 7, cv2.INPAINT_TELEA).astype(np.float32) / 255
    # the printer (foreground plane) and the paper
    pm = np.maximum(poly_mask(PRINTER12, feather=1.0), poly_mask([[1632, 30], [1920, 0], [1920, 472], [1476, 472]], feather=1))
    hole = cv2.dilate((pm > 0.05).astype(np.uint8), np.ones((31, 31), np.uint8))
    behind = cv2.inpaint((base * 255).astype(np.uint8), hole, 15, cv2.INPAINT_TELEA).astype(np.float32) / 255
    paperm = poly_mask([[1634, 34], [1920, 4], [1920, 470], [1480, 470]], feather=1.5)
    Hp = quad_H(rect_quad(560, 0, 800, 930), PAPER12)
    lamps = [(80, 700, 350, 130, [[987, 440], [1057, 440], [1057, 477], [987, 477]]),
             (530, 700, 350, 130, [[982, 505], [1055, 505], [1055, 541], [982, 541]])]
    lampH = [(quad_H(rect_quad(x, y, w, h), q), poly_mask(q, feather=0.7)) for x, y, w, h, q in lamps]
    panel = json.load(open(JS / "j07_panel.json"))
    tube = VReader(JS / "j07_loop_tube.mp4")
    pan = VReader(JS / "j07_loop_panel.mov")
    pap = VReader(JS / "j07_loop_paper.mov")
    paper_base = None

    def fn(i):
        nonlocal paper_base
        t = i / FPS
        tex = tube.get(i)[..., :3]
        pa = pan.get(i)
        pp = pap.get(i)
        x = base.copy()
        for Hh, m in lampH:
            s = warp(pa, Hh)
            x = x * (1 - m[..., None]) + (s[..., :3] * s[..., 3:4] + x * (1 - s[..., 3:4])) * m[..., None]
        # the needle: flat ink, carved edge, from the JSON value
        v = panel[i]["needle"]
        ang = np.deg2rad(-37 + 80 * v) + panel[i]["shiver_rad"]
        tip = NEEDLE_PIVOT + 118 * np.float32([np.sin(ang), -np.cos(ang)])
        nl = np.zeros((H, W), np.float32)
        pts = np.float32([NEEDLE_PIVOT + 5 * np.float32([np.cos(ang), np.sin(ang)]), tip,
                          NEEDLE_PIVOT - 5 * np.float32([np.cos(ang), np.sin(ang)])])
        cv2.fillConvexPoly(nl, np.int32(pts * 16), 1.0, cv2.LINE_AA, shift=4)
        x = x * (1 - 0.92 * nl[..., None]) + np.float32([0.07, 0.08, 0.1]) * 0.92 * nl[..., None]
        # the tube
        T = warp(tex, Ht)
        x = disp(lin(x) * (1 - G[..., None]) + lin(T) * G[..., None])
        # focus pull 6.0-7.0: the tube plane softens to 12 px, the printer sharpens from 10 px
        u = ease_inout_cubic((t - 6.0) / 1.0)
        bt, bp = 12 * u, 10 * (1 - u)
        backp = x * (1 - pm[..., None]) + behind * pm[..., None]
        if bt > 0.3:
            backp = cv2.GaussianBlur(backp, (0, 0), bt)
        # printer plane with the printed paper
        pr = x.copy()
        pt = warp(pp, Hp)
        if paper_base is None:
            paper_base = np.median(pp[200:600, 700:1200, :3].reshape(-1, 3), 0)
        ratio = np.clip(pt[..., :3] / np.maximum(paper_base, 1e-3), 0, 1.2)
        ratio = ratio * pt[..., 3:4] + (1 - pt[..., 3:4])
        pr = pr * (1 - paperm[..., None]) + pr * ratio * paperm[..., None]
        fg = np.dstack([pr * pm[..., None], pm])
        if bp > 0.3:
            fg = cv2.GaussianBlur(fg, (0, 0), bp)
        return over(backp, fg)
    run("12", 192, fn, "12_pre.mp4")


# ------------------------------------------------------------------ 14 (and 22's plate): the Air Clock
def s14():
    p = plate("p14_air_clock")
    at = VReader(JS / "j08_air_clock_14.mov")
    cx, cy, rx, ry = 978, 412, 272, 232
    A = np.float32([[rx / 480, 0, cx - 540 * rx / 480], [0, ry / 480, cy - 540 * ry / 480], [0, 0, 1]])
    cards = [[1082, 300, 170, 190], [1266, 300, 170, 190], [1510, 300, 170, 190], [1694, 300, 170, 190]]
    wins = [rect_quad(521, 713, 184, 194), rect_quad(710, 713, 184, 194), rect_quad(999, 713, 184, 194),
            rect_quad(1188, 713, 183, 194)]
    Hc = [quad_H(rect_quad(*c), w) for c, w in zip(cards, wins)]
    Hpl = quad_H(rect_quad(1330, 560, 300, 66), rect_quad(887, 899, 143, 27))
    r = np.random.default_rng(14)
    N = 26
    dx, dy = r.uniform(0, W, N), r.uniform(150, 950, N)
    vx, vy, sz = r.uniform(-6, 6, N), r.uniform(-8, 3, N), r.uniform(1.0, 2.2, N)

    def fn(i):
        t = i / FPS
        a = at.get(i)
        x = p.copy()
        pa = premul(a)
        def region(x, y, w, h):
            z = np.zeros_like(pa)
            z[y:y + h, x:x + w] = pa[y:y + h, x:x + w]
            return z
        hands = warp(region(40, 40, 1000, 1000), A, interp=cv2.INTER_AREA)
        x = over(x, hands * np.float32([1, 1, 1, 0.97]))
        for Hh, cr in zip(Hc, cards):
            c = warp(region(*cr), Hh, interp=cv2.INTER_AREA)
            c[..., :3] *= 0.85
            x = over(x, c)
        x = over(x, warp(region(1330, 560, 300, 66), Hpl, interp=cv2.INTER_AREA))
        lay = np.zeros((H, W), np.float32)
        for j in range(N):
            cv2.rectangle(lay, (int(dx[j] + vx[j] * t), int(dy[j] + vy[j] * t)),
                          (int(dx[j] + vx[j] * t + sz[j]), int(dy[j] + vy[j] * t + sz[j])), 1.0, -1)
        lay = cv2.GaussianBlur(lay, (0, 0), 0.6) * 0.45
        return x * (1 - lay[..., None]) + np.float32([0.75, 0.88, 0.88]) * lay[..., None]
    run("14", 48, fn, "14_pre.mp4")


# ------------------------------------------------------------------ 15: the city
def s15():
    k = plate("k08_city_night")
    r, g, b = k[..., 0], k[..., 1], k[..., 2]
    l = k.mean(-1)
    amber = poly_mask(rect_quad(1432, 318, 80, 62)) > 0.5
    cold = ((b > r + 0.08) & (l > 0.33)).astype(np.uint8)
    cold[870:] = 0
    cold[amber] = 0
    for hx in (190, 762, 1160, 1792):                    # the mercury lamps' cones do not breathe
        cv2.fillConvexPoly(cold, np.int32([(hx - 20, 640), (hx + 20, 640), (hx + 110, 800), (hx - 110, 800)]), 0)
    n, lab, st, _ = cv2.connectedComponentsWithStats(cold)
    keep = np.zeros(n, bool)
    keep[1:] = st[1:, 4] > 25
    win = keep[lab]
    np.savez_compressed(CV / "k08_windows.npz", labels=np.where(win, lab, 0).astype(np.int32),
                        amber_box=np.int32([1432, 318, 80, 62]))
    print("windows", keep.sum())
    M = cv2.GaussianBlur(win.astype(np.float32), (0, 0), 1.0)[..., None]
    luma = json.load(open(JS / "j15_luma.json"))["luma"]
    kl = lin(k)
    # rain: two layers of thin cut lines, visible only where they cross light
    L = cv2.GaussianBlur(l, (0, 0), 6)
    L = np.clip((L - 0.12) / 0.35, 0, 1)
    rr = np.random.default_rng(15)
    layers = []
    for n_, sp, ln, al, sl in ((420, 1300, 34, 0.35, 0.18), (220, 1900, 60, 0.5, 0.22)):
        layers.append((rr.uniform(0, W, n_), rr.uniform(0, H, n_), sp, ln, al, sl))
    # beacon at (875, 80)
    bm = np.zeros((H, W), np.float32)
    cv2.circle(bm, (875, 80), 9, 1, -1, cv2.LINE_AA)
    bglow = cv2.GaussianBlur(bm, (0, 0), 10)
    canal = np.clip((np.arange(H) - 880) / 20, 0, 1).astype(np.float32)[:, None]
    X = np.tile(np.arange(W, dtype=np.float32), (H, 1))
    Yg = np.tile(np.arange(H, dtype=np.float32)[:, None], (1, W))

    def fn(i):
        t = i / FPS
        br = 1 + 2 * (luma[min(int(round((77.0 + t) * 24)), len(luma) - 1)] - 1)      # ±6 %, with the card
        x = kl * (1 + (br - 1) * M)
        # the canal's cuts drift sideways
        dx = 3.5 * np.sin(Yg / 9 + t * 0.8) * canal + 2 * np.sin(Yg / 23 - t * 0.5) * canal
        x = cv2.remap(x, X + dx, Yg, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        # beacon: 0.3 s on every 2 s
        on = (t % 2.0) < 0.3
        if not on:
            x = x * (1 - 0.85 * bm[..., None]) + 0.85 * bm[..., None] * lin(np.float32([0.18, 0.08, 0.08]))
        else:
            x = x + bglow[..., None] * lin(np.float32([0.9, 0.25, 0.18])) * 0.8
        lay = np.zeros((H, W), np.float32)
        for xs, ys, sp, ln, al, sl in layers:
            yy = (ys + sp * t) % (H + 100) - 50
            xx = (xs - sl * sp * t) % W
            for a0, b0 in zip(xx, yy):
                cv2.line(lay, (int(a0), int(b0)), (int(a0 + sl * ln), int(b0 - ln)), al, 1, cv2.LINE_AA)
        lay = lay * L
        x = x + lay[..., None] * lin(np.float32([0.78, 0.9, 0.92])) * 0.5
        return disp(x)
    run("15", 168, fn, "15_pre.mp4")
