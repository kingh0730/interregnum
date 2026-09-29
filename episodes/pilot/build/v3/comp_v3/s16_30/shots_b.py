"""v3 plates for shots 21-30 (see shots.py)."""
import cv2
import numpy as np

from lib import *
from shots import FACE, STILL, Out, Rain, glow_mask, screen_mask, soft, want

AMBER = hexc("#E9A23B")
RED = hexc("#CC3A2B")
RED_HOT = hexc("#F0643A")
COLD = hexc("#8ED8D6")
COLD_HOT = hexc("#D8F4F1")


# ------------------------------------------------------------------ the Script Terminal (21, 24, 26)
P21 = "p21_terminal"
P21_GLASS = (420, 120, 1080, 620)
P21_WINDOWS = [((1072, 11), (1134, 11), (1134, 92), (1072, 92)),
               ((1141, 15), (1205, 15), (1205, 96), (1141, 96)),
               ((1215, 21), (1277, 21), (1277, 104), (1215, 104)),
               ((1288, 25), (1352, 25), (1352, 111), (1288, 111))]
FLAP_CARDS = [(200, 330, 540, 750), (560, 330, 900, 750), (1020, 330, 1360, 750), (1380, 330, 1720, 750)]
PIVOT = np.float32([1347, 419])
A0 = np.arctan2(337 - 419, 1301 - 1347)   # needle at 0
A1 = np.arctan2(352 - 419, 1435 - 1347)   # needle at 1.0
LAMP1 = (1343, 473, 1396, 506)            # NO PREDICTION (red)
LAMP2 = (1339, 531, 1391, 566)            # SCRIPT LOCKED (cold)
JEWEL = ((1492, 219), 17)                 # VIEWING (red jewel)


def rounded_quad(q, shape, grow=4, radius=30):
    """Filled quad (key coords), grown by `grow` px, with its corners rounded by `radius` px."""
    c = q.mean(0)
    qq = c + (q - c) * (1 + grow / np.linalg.norm(q - c, axis=1, keepdims=True))
    m = np.zeros(shape[:2], np.uint8)
    cv2.fillConvexPoly(m, np.int32(qq * 8), 1, cv2.LINE_AA, shift=3)
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * radius + 1,) * 2)
    return cv2.morphologyEx(m, cv2.MORPH_OPEN, k).astype(np.float32)


def lamp_layer(V, rect, col, hot, W, H, round_=False):
    """A lit legend lamp: flat ink with a hotter centre (tungsten behind coloured glass), as (rgb_lin, mask)."""
    if round_:
        (cx, cy), r = rect
        c = V.pts([cx, cy])[0]
        rr = r * V.s
        m = np.zeros((H, W), np.float32)
        cv2.circle(m, (int(c[0] * 8), int(c[1] * 8)), int(rr * 8), 1.0, -1, cv2.LINE_AA, shift=3)
        Y, X = np.mgrid[0:H, 0:W].astype(np.float32)
        d = np.sqrt((X - c[0]) ** 2 + (Y - c[1]) ** 2) / rr
    else:
        x0, y0, x1, y1 = rect
        p = V.pts([[x0, y0], [x1, y1]])
        m = np.zeros((H, W), np.float32)
        cv2.rectangle(m, tuple(np.int32(p[0])), tuple(np.int32(p[1])), 1.0, -1)
        m = cv2.GaussianBlur(m, (0, 0), 1.0)
        Y, X = np.mgrid[0:H, 0:W].astype(np.float32)
        c = p.mean(0)
        hw = (p[1] - p[0]) / 2
        d = np.sqrt(((X - c[0]) / hw[0]) ** 2 + ((Y - c[1]) / hw[1]) ** 2) / 1.2
    k = np.clip(1 - d, 0, 1)[..., None] ** 1.5
    rgb = lin(col) * (1 - k) * 1.1 + lin(hot) * k * 1.6
    return rgb.astype(np.float32), m[..., None]


def needle_draw(img_lin, V, v):
    a = A0 + (A1 - A0) * v
    L = 94
    tip = PIVOT + L * np.float32([np.cos(a), np.sin(a)])
    base = PIVOT + 12 * np.float32([np.cos(a), np.sin(a)])
    nrm = np.float32([-np.sin(a), np.cos(a)])
    poly = np.float32([base + nrm * 2.2, tip + nrm * 0.8, tip - nrm * 0.8, base - nrm * 2.2])
    p = V.pts(poly)
    m = np.zeros(img_lin.shape[:2], np.float32)
    cv2.fillConvexPoly(m, np.int32(p * 8), 1.0, cv2.LINE_AA, shift=3)
    m = m[..., None]
    img_lin[:] = img_lin * (1 - m) + lin(hexc("#11151F")) * m


def terminal(name, view, tex, n, flaps, panel=None, amber=None, refl=0.06, stills=(0,)):
    im = key(P21)
    if panel:  # the plate's needle is masked out; comp redraws it from the panel levels
        nm = np.zeros(im.shape[:2], np.uint8)
        cv2.line(nm, (1349, 414), (1300, 334), 1, 9)
        im8 = cv2.inpaint((im * 255).astype(np.uint8), nm * 255, 5, cv2.INPAINT_TELEA)
        im = im8.astype(np.float32) / 255
    V = View(*view)
    W, H = V.PW, V.PH
    base = V.img(im)
    qk = fit_quad(glow_mask(im, P21_GLASS))
    quad = V.pts(qk)
    gm = soft(V.mask(rounded_quad(qk, im.shape, grow=4, radius=34)), 0, 1.5)[..., None]
    # her reflection: a mirrored, darkened, blurred crop of k07 (her face lit from below), no hard edges
    k07 = key("k07_ida_no")[90:650, 280:800]
    k07 = cv2.GaussianBlur(cv2.flip(k07, 1), (0, 0), 6)
    l7 = lum(k07)[..., None]
    k07 = l7 + (k07 - l7) * 0.35
    hh, ww = k07.shape[:2]
    Yr, Xr = np.mgrid[0:hh, 0:ww].astype(np.float32)
    k07 = k07 * np.clip(1.25 - np.sqrt(((Xr - ww / 2) / (ww / 2)) ** 2 + ((Yr - hh / 2) / (hh / 2)) ** 2), 0, 1)[..., None]
    qc = quad.mean(0)
    qwid, qhei = np.linalg.norm(quad[1] - quad[0]), np.linalg.norm(quad[3] - quad[0])
    rq = qc + (quad - qc) * 0.8 + np.float32([0.08 * qwid, -0.04 * qhei])
    R_ = warp_quad(lin(k07), (0, 0, ww, hh), rq, (W, H), cv2.INTER_LINEAR) * refl
    # flap repeater windows
    wq = [V.pts(q) for q in P21_WINDOWS]
    # fingertips (21): the upper, nearer-the-glass parts of her hands
    fk = None
    if amber:
        sk = ((lum(im) > 0.42) & (im[..., 2] > im[..., 0] + 0.08)).astype(np.float32)
        sk[:560] = 0
        Y = np.mgrid[0:im.shape[0], 0:im.shape[1]][0].astype(np.float32)
        sk *= np.clip((800 - Y) / 190, 0, 1)
        fk = soft(V.mask(sk), 0, 1.2)[..., None]
        am = np.array([f["amber"] for f in load_json(amber)], np.float32)
        am = am / am.max()
    pnl = load_json(panel) if panel else None
    lamps = []
    if pnl:
        lamps = [("NO_PREDICTION", lamp_layer(V, LAMP1, RED, RED_HOT, W, H)),
                 ("SCRIPT_LOCKED", lamp_layer(V, LAMP2, COLD, COLD_HOT, W, H)),
                 ("VIEWING", lamp_layer(V, JEWEL, RED, RED_HOT, W, H, round_=True))]
    pap = paper(W, H, int(name), 0.018)
    base_l = lin(base)
    texs = hold(read_video(JS / tex), n)
    fl = hold(read_video(JS / flaps, alpha=True), n)
    o = Out(name, W, H, n, stills=stills)
    for i in o.frames():
        tf, ff = next(texs), next(fl)
        if not want(o, i):
            continue
        img = base_l.copy()
        if fk is not None:  # the first warm light on Ida: her own words on her fingertips
            a = am[min(i, len(am) - 1)]
            target = lum(img)[..., None] * lin(AMBER) / lum(lin(AMBER)[None, None])[..., None] * 1.25
            img = img + (target - img) * (0.35 * a) * fk
        # flaps: each card of the atlas into its window, darkened and cooled to the housing's light
        for (x0, y0, x1, y1), q in zip(FLAP_CARDS, wq):
            c = warp_quad(ff, (x0, y0, x1, y1), q, (W, H), clip=True)
            a_ = c[..., 3:4]
            img = img * (1 - a_) + lin(c[..., :3]) * np.float32([0.62, 0.58, 0.55]) * a_
        if pnl:
            p = pnl[min(i, len(pnl) - 1)]
            needle_draw(img, V, p["needle"])
            emit = np.zeros_like(img)
            for k, (rgb, m) in lamps:
                lv = float(p[k])
                if lv > 0.01:
                    img = img * (1 - m * lv * 0.9) + rgb * m * lv
                    emit += rgb * m * lv
            img += glow(emit, 0.5, 3, 12)
        t_ = warp_quad(lin(tf), FACE, quad, (W, H))
        img = img * (1 - gm) + (t_ + R_) * gm
        img += glow(t_ * gm, 0.3)
        o.put(disp(img) * pap, i)
    o.done()


def shot21():
    terminal("21", (0, -105, 1672), "j09_signoffs.mp4", 192, "j_flaps_21.mov", amber="j09_amber.json",
             refl=0.02, stills=(0, 100, 170))


V24 = (240, 12 - (1338 * 9 / 16 - 1338 / 2.39) / 2, 1338)


def shot24():
    terminal("24", V24, "j10_terminal_24.mp4", 192, "j_flaps_24.mov", panel="j10_panel_24.json", refl=0.045,
             stills=(0, 40, 90, 150))


def shot26():
    terminal("26", V24, "j10_terminal_26.mp4", 216, "j_flaps_26.mov", panel="j10_panel_26.json", refl=0.045,
             stills=(0, 60, 110, 170))


# ------------------------------------------------------------------ the Air Clock (22)
BOARD = [((481, 622), (622, 622), (616, 767), (469, 767)), ((640, 622), (787, 622), (785, 767), (634, 767)),
         ((882, 622), (1030, 622), (1032, 767), (882, 767)), ((1047, 622), (1190, 622), (1197, 767), (1052, 767))]
J08_CARDS = [(1082, 300, 1252, 490), (1266, 300, 1436, 490), (1510, 300, 1680, 490), (1694, 300, 1864, 490)]


def shot22():
    im = key("p14_air_clock")
    V = View(0, 0, 1672, 2048, 1152)
    W, H = V.PW, V.PH
    base_l = lin(V.img(im))
    (cx, cy), (a1, a2), ang = ((833.6, 329.6), (402.1, 456.5), 88.6)
    rx, ry = a2 / 2, a1 / 2   # angle ~90: the first axis is vertical
    face_q = V.pts([[cx - rx, cy - ry], [cx + rx, cy - ry], [cx + rx, cy + ry], [cx - rx, cy + ry]])
    bq = [V.pts(q) for q in BOARD]
    plate_q = V.pts([[771, 785], [896, 785], [896, 809], [771, 809]])
    pap = paper(W, H, 22, 0.018)
    atl = hold(read_video(JS / "j08_air_clock_22.mov", alpha=True), 48)
    tint = np.float32([0.80, 0.74, 0.66])  # the board sits in cold shadow
    o = Out("22", W, H, 48, stills=(0, 30))
    for i in o.frames():
        f = next(atl)
        if not want(o, i):
            continue
        img = base_l.copy()
        layers = [((60, 60, 1020, 1020), face_q, np.float32([1, 1, 1]))]
        layers += [(r, q, tint) for r, q in zip(J08_CARDS, bq)]
        layers += [((1330, 560, 1630, 626), plate_q, tint)]
        for r, q, tn in layers:
            c = warp_quad(f, r, q, (W, H), clip=True)
            a_ = c[..., 3:4]
            img = img * (1 - a_) + lin(c[..., :3]) * tn * a_
        o.put(disp(img) * pap, i)
    o.done()


# ------------------------------------------------------------------ the Wall (23)
def shot23():
    im = key("k14_hall_low")
    V = View(0, 0, 1672, 2112, 1188)
    W, H = V.PW, V.PH
    # 96 tube faces
    x0, y0 = 330, 240
    sub = im[y0:745, x0:1345]
    m = ((lum(sub) > 0.45) & (sub[..., 0] > sub[..., 2] + 0.1)).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    n, lab, st, cen = cv2.connectedComponentsWithStats(m)
    ids = [i for i in range(1, n) if st[i, cv2.CC_STAT_AREA] > 800]
    assert len(ids) == 96, len(ids)
    cen = cen[ids] + [x0, y0]
    rows = np.argsort(np.argsort(cen[:, 1])) // 12
    tiles = []
    for r in range(8):
        sel = [k for k in range(96) if rows[k] == r]
        sel.sort(key=lambda k: cen[k, 0])
        for c, k in enumerate(sel):
            full = np.zeros(im.shape[:2], np.float32)
            full[y0:745, x0:1345] = (lab == ids[k]).astype(np.float32)
            full = cv2.dilate(full, np.ones((3, 3), np.uint8))
            tiles.append((r, c, full))
    # the picture: k02 clean, cropped 2:1, one tile of it per tube
    k02 = key("k02_father_cu")[20:856]
    TW, TH = 160, 120
    pic = cv2.resize(k02, (12 * TW, 8 * TH), interpolation=cv2.INTER_AREA)
    rng = np.random.default_rng(23)
    wall = np.zeros((H, W, 3), np.float32)
    tid = np.full((H, W), -1, np.int32)
    tmask = np.zeros((H, W), np.float32)
    Yt, Xt = np.mgrid[0:TH, 0:TW].astype(np.float32)
    nx, ny = (Xt - TW / 2) / (TW / 2), (Yt - TH / 2) / (TH / 2)
    r2 = nx * nx + ny * ny
    bx, by = nx * (1 + 0.04 * r2) * TW / 2 + TW / 2, ny * (1 + 0.04 * r2) * TH / 2 + TH / 2
    vign = (1 - 0.25 * np.clip(r2 / 2, 0, 1) ** 1.2)[..., None]
    vmap = np.zeros((H, W), np.float32)
    DEAD, HUM = (0, 11), (7, 4)
    gains = []
    for idx, (r, c, full) in enumerate(tiles):
        t_img = pic[r * TH:(r + 1) * TH, c * TW:(c + 1) * TW]
        t_img = cv2.remap(t_img, bx, by, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT) * vign
        if (r, c) == DEAD:
            t_img = t_img * 0.03 + np.float32([0.07, 0.06, 0.05])
        q = V.pts(fit_quad(full))
        mk = V.mask(full)
        x_, y_, w_, h_ = cv2.boundingRect(np.int32(q))
        x_, y_ = max(0, x_ - 4), max(0, y_ - 4)
        w_, h_ = w_ + 8, h_ + 8
        Hm = cv2.getPerspectiveTransform(np.float32([[0, 0], [TW, 0], [TW, TH], [0, TH]]), np.float32(q - [x_, y_]))
        wp = cv2.warpPerspective(lin(t_img) * 1.15, Hm, (w_, h_), flags=cv2.INTER_LINEAR)
        roi = (slice(y_, y_ + h_), slice(x_, x_ + w_))
        mm = mk[roi][..., None]
        wall[roi] = wall[roi] * (1 - mm) + wp * mm
        tmask[roi] = np.maximum(tmask[roi], mk[roi])
        tid[roi][mk[roi] > 0.5] = idx
        if (r, c) == HUM:
            vv = cv2.warpPerspective(np.tile(np.linspace(0, 1, TH, dtype=np.float32)[:, None], (1, TW)), Hm,
                                     (w_, h_))
            vmap[roi] = np.where(mk[roi] > 0.3, vv, vmap[roi])
        col = np.float32([1 + rng.uniform(-0.08, 0.08), 1 + rng.uniform(-0.08, 0.08), 1]) * \
            (1 + rng.uniform(-0.1, 0.1))
        gains.append(col if (r, c) != DEAD else np.float32([1, 1, 1]))
    gains = np.float32(gains)
    hum_idx = [j for j, x in enumerate(tiles) if (x[0], x[1]) == HUM][0]
    # the matte of her and her desk (the near group), GrabCut-seeded
    img8 = (im * 255).astype(np.uint8)
    g = np.full(im.shape[:2], cv2.GC_BGD, np.uint8)
    g[600:941, 0:600] = cv2.GC_PR_BGD
    cv2.fillPoly(g, [np.int32([[250, 650], [330, 650], [350, 760], [360, 941], [210, 941], [215, 760]])],
                 cv2.GC_PR_FGD)
    cv2.fillPoly(g, [np.int32([[270, 700], [320, 700], [330, 900], [240, 900]])], cv2.GC_FGD)
    bgd, fgd = np.zeros((1, 65)), np.zeros((1, 65))
    cv2.grabCut(img8, g, None, bgd, fgd, 8, cv2.GC_INIT_WITH_MASK)
    a = np.isin(g, (1, 3)).astype(np.uint8)
    a = cv2.morphologyEx(a, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    nl, lb, st2, _ = cv2.connectedComponentsWithStats(a)
    a = (lb == 1 + np.argmax(st2[1:, cv2.CC_STAT_AREA])).astype(np.uint8)
    cnts, _ = cv2.findContours(a, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    a = np.zeros_like(a)
    cv2.drawContours(a, cnts, -1, 1, -1)
    ring = cv2.dilate(a, np.ones((5, 5), np.uint8)) & (1 - cv2.erode(a, np.ones((61, 61), np.uint8)))
    ip = cv2.inpaint(img8, ring * 255, 7, cv2.INPAINT_TELEA).astype(np.float32) / 255
    plate_k = im * (1 - ring[..., None]) + ip * ring[..., None]
    af = V.mask(cv2.GaussianBlur(a.astype(np.float32), (0, 0), 0.8))
    fg = V.img(im)
    pap = paper(W, H, 23, 0.018)
    fg_out = np.dstack([np.clip(fg * pap, 0, 1), af])
    cv2.imwrite(str(O / "k14_fg.png"), (fg_out * 255 + 0.5).astype(np.uint8))
    base_l = lin(V.img(plate_k))
    tm = soft(tmask, 0, 0.8)[..., None]
    base_l = base_l * (1 - tm)
    # ON AIR at standby
    ok = np.zeros(im.shape[:2], np.float32)
    ok[190:240, 795:878] = red_mask(im[190:240, 795:878], 0)
    om = V.mask(ok)[..., None]
    rph = np.random.default_rng(5).uniform(0, 2 * np.pi, 96)
    rhz = np.random.default_rng(6).uniform(0.05, 0.12, 96)
    tidc = np.clip(tid, 0, 95)
    o = Out("23", W, H, 144, stills=(0, 143))
    for i in o.frames():
        if not want(o, i):
            continue
        t = i / FPS
        slow = 1 + 0.02 * np.sin(2 * np.pi * rhz * t + rph)
        gmap = (gains * slow[:, None])[tidc]
        wl = wall * gmap
        ph = (-(t / 7.0)) % 1.0  # the hum bar rolls up every ~7 s
        d = np.minimum(np.abs(vmap - ph), 1 - np.abs(vmap - ph))
        hum = 1 - 0.08 * np.exp(-(d / 0.12) ** 2) * (tid == hum_idx)
        wl = wl * hum[..., None]
        img = base_l + wl * tm
        L = 0.75 + 0.15 * np.sin(2 * np.pi * 0.5 * t)
        img = img * (1 - om) + img * om * (L / 0.9)
        emit = wl * tm + img * om * 0.6
        img += glow(emit, 0.28, 5, 22)
        o.put(disp(img) * pap, i)
    o.done()
    eyes = V.pts([[835, 455]])[0] / [W, H]
    print("eyes (plate norm):", eyes)


# ------------------------------------------------------------------ her eyes (25), the key (27)
def shot25():
    im = key("k15_ida_eyes")
    V = View(0, 0, 1672)
    W, H = V.PW, V.PH
    base = V.img(im)
    cl = cyan_lit(base, 4)[..., None]
    pap = paper(W, H, 25, 0.018)
    Y = np.mgrid[0:H, 0:1][0].astype(np.float32)
    bands = [(0.30, 0.07, 1), (0.52, -0.06, 0), (0.68, 0.08, 0), (0.85, -0.05, 0)]  # y (frac), amount, amber?
    o = Out("25", W, H, 72, stills=(0, 71))
    for i in o.frames():
        if not want(o, i):
            continue
        t = i / FPS
        rise = 20 * V.s * t / 3.0
        img = lin(base)
        k = np.ones((H, 1), np.float32)
        warm = np.zeros((H, 1), np.float32)
        for j, (yf, amt, amb) in enumerate(bands):
            yc = yf * H - rise
            b = np.exp(-((Y - yc) / (0.05 * H)) ** 2)
            fl = 1 + 0.35 * noise(250 + j, t, 3.0)  # rows appear as she types
            k = k + amt * fl * b
            if amb:
                warm = warm + 0.10 * b * (0.8 + 0.2 * fl)
        img = img * (1 + (k[..., None] - 1) * cl)
        tgt = lum(img)[..., None] * lin(AMBER) / lum(lin(AMBER)[None, None])[..., None]
        img = img + (tgt - img) * warm[..., None] * cl
        o.put(disp(img) * pap, i)
    o.done()


def shot27():
    im = key("k16_commit_key")
    V = View(0, 0, 1672, 2048, 1152)
    W, H = V.PW, V.PH
    base = V.img(im)
    rm = red_mask(base, 2)[..., None]
    key_m = np.zeros(im.shape[:2], np.float32)
    key_m[465:750, 780:1160] = red_mask(im[465:750, 780:1160], 0)
    km = V.mask(key_m)[..., None]
    pap = paper(W, H, 27, 0.018)
    base_l = lin(base)
    o = Out("27", W, H, 96, stills=(0, 4, 95))
    for i in o.frames():
        if not want(o, i):
            continue
        t = i / FPS
        s = sum(np.exp(-(t - k) / 0.4) for k in range(4) if t >= k)
        img = base_l * (1 + 0.15 * s * rm)
        img += glow(img * km, 0.25 + 0.1 * s, 5, 24)
        o.put(disp(img) * pap, i)
    o.done()


# ------------------------------------------------------------------ the broadcast (29) and the street (30)
def father_picture():
    """k01 as the 4:3 broadcast picture (1440x1080), centred on his face."""
    k01 = key("k01_father_mcu")
    cx, w = 816, 941 * 4 / 3
    M = np.float32([[1440 / w, 0, -(cx - w / 2) * 1440 / w], [0, 1080 / 941, 0]])
    return cv2.warpAffine(k01, M, (1440, 1080), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)


def key_overlay(pic, ov):
    """J14 bug/captions (master coords, BGRA) keyed into the 1440x1080 picture."""
    o = ov[:, 240:1680]
    a = o[..., 3:4]
    return pic * (1 - a) + o[..., :3] * a


def shot29():
    pic0 = father_picture()
    ov = hold(read_video(JS / "j14_bug_cc_29.mov", alpha=True), 120)
    Y, X = np.mgrid[0:1080, 0:1440].astype(np.float32)
    r2 = ((X - 720) / 720) ** 2 + ((Y - 540) / 540) ** 2
    vig = (1 - 0.15 * r2 ** 1.3)[..., None]
    scan = np.ones((1080, 1, 1), np.float32)
    scan[::3] = 0.92
    lift = hexc("#101826")
    o = Out("29", 1920, 1080, 120, stills=(0, 60, 119))
    for i in o.frames():
        f = next(ov)
        if not want(o, i):
            continue
        t = i / FPS
        p = key_overlay(pic0, f)
        if i % 2:  # interlace twitter: thin horizontals shimmer by a line
            p[1:-1:2] = 0.8 * p[1:-1:2] + 0.2 * p[2::2]
        L_ = lin(p)
        L_ += glow(np.clip(L_ - 0.55, 0, None), 0.35, 4, 14)
        p = disp(L_)
        p[..., 2] = np.roll(p[..., 2], 1, 1)
        p[..., 0] = np.roll(p[..., 0], -1, 1)
        # one faint hum bar during the Address, raster breathing
        hb = ((Y[:, :1] / 1080 + t / 7.5) % 1.0)
        p = p * (1 - 0.035 * np.exp(-((hb - 0.5) / 0.08) ** 2))[..., None]
        p = p * (1 + 0.006 * np.sin(2 * np.pi * 0.3 * t))
        p = p * scan * vig
        lum_ = lum(p)[..., None]
        p = lum_ + (p - lum_) * 0.92
        p = lift + p * (1 - lift)
        frame = np.zeros((1080, 1920, 3), np.float32)
        frame[:, 240:1680] = p
        o.put(frame, i)
    o.done()


def shot30():
    im = key("k17_street")
    wv = 1656
    V = View(8, (941 - wv * 9 / 16) / 2 - 70, wv)  # band up: keep the pediment and bronze Lamp
    W, H = V.PW, V.PH
    base = V.img(im)
    rect = (900, 190, 1330, 480)
    qk = fit_quad(glow_mask(im, rect))
    quad = V.pts(qk)
    sk = rounded_quad(qk, im.shape, grow=2, radius=2)
    sm = soft(V.mask(sk), 1, 1.0)[..., None]
    # the picture: k01 at 4:3 with the bug (J14 at its first frame: bug only, no captions)
    ov = next(read_video(JS / "j14_bug_cc_29.mov", alpha=True))
    pic = key_overlay(father_picture(), ov)
    # screen space at the screen's own aspect; the 4:3 picture centred, the sides at the projector's black
    qw = (np.linalg.norm(quad[1] - quad[0]) + np.linalg.norm(quad[2] - quad[3])) / 2
    qh = (np.linalg.norm(quad[3] - quad[0]) + np.linalg.norm(quad[2] - quad[1])) / 2
    SH = 1080
    SW = int(SH * qw / qh)
    scr = np.zeros((SH, SW, 3), np.float32) + lin(COLD) * 0.035
    px = (SW - 1440) // 2
    scr[:, px:px + 1440] = lin(pic)
    Ys, Xs = np.mgrid[0:SH, 0:SW].astype(np.float32)
    rr = ((Xs - SW / 2) / (SW / 2)) ** 2 + ((Ys - SH / 2) / (SH / 2)) ** 2
    scr = scr * (1.25 - 0.55 * np.clip(rr, 0, 1.4) ** 0.9)[..., None]            # hot spot, dark corners
    scr = cv2.GaussianBlur(scr, (0, 0), 3.0)                                        # soft focus
    scr = scr * (1 - 0.22 * (0.5 + 0.5 * np.cos(2 * np.pi * Ys / 9.0)))[..., None]  # scanlines at this scale
    scr = scr * np.float32([1.08, 1.02, 0.92])                                     # cold projector
    warped = warp_quad(scr, (0, 0, SW, SH), quad, (W, H))
    base_l = lin(base)
    cl = cyan_lit(base, 4)[..., None] * (1 - soft(V.mask(sk), 12, 6)[..., None])
    # the lamps and the tram's windows glow
    em = ((lum(base) > 0.62) & (base[..., 0] > base[..., 2])).astype(np.float32) * (1 - V.mask(sk))
    em = soft(em, 0, 1.0)[..., None]
    light = cv2.GaussianBlur(lum(disp(base_l * (1 - sm) + warped * sm)), (0, 0), 25)
    light = np.clip((light - 0.12) / 0.35, 0, 1) ** 1.2
    beam = np.zeros((H, W), np.float32)
    cv2.fillConvexPoly(beam, np.int32(quad + [[-60, -40], [60, -40], [60, 120], [-60, 120]]), 1.0)
    light = np.clip(light + 0.6 * cv2.GaussianBlur(beam, (0, 0), 40), 0, 1)
    far = Rain(301, 900, W, H, length=(10, 18), speed=(1.1, 1.5), slant=0.10, width=1, alpha=0.5)
    near = Rain(302, 90, W, H, length=(36, 64), speed=(1.5, 2.1), slant=0.12, width=2, alpha=0.65)
    rc = lin(np.float32([0.93, 0.93, 0.82]))
    pap = paper(W, H, 30, 0.02)
    o = Out("30", W, H, 144, stills=(0, 72))
    for i in o.frames():
        if not want(o, i):
            continue
        t = i / FPS
        fk = 1 + 0.02 * noise(301, t, 1.7)
        img = base_l * (1 + (0.9 * fk - 1) * cl)
        img = img * (1 - sm) + warped * fk * sm
        img += glow(warped * sm * fk, 0.3, 6, 30) + glow(img * em, 0.25, 3, 14)
        r_ = (far.layer(t) + near.layer(t)) * light
        r_ = np.clip(r_, 0, 1)[..., None]
        img = img * (1 - r_) + rc * r_ * 0.9
        o.put(disp(img) * pap, i)
    o.done()


SHOTS_B = {"21": shot21, "22": shot22, "23": shot23, "24": shot24, "25": shot25, "26": shot26, "27": shot27,
           "29": shot29, "30": shot30}
