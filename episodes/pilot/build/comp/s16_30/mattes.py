"""Plate-derived foreground mattes (GrabCut seeded) for parallax on k09 / k14 / k17, plus plates inpainted in the
reveal band behind them. Outputs (keyframe res 1672x941): <k>_fg.png (RGBA, plate pixels), <k>_ip.png (plate)."""
import cv2, numpy as np, sys
from pathlib import Path
O = Path(__file__).parent
K = O.parents[1] / "keys"
DBG = Path(sys.argv[1]) if len(sys.argv) > 1 else O
W0, H0 = 1672, 941
sx = W0 / 960  # preview-coords -> key coords


def P(*pts):
    return np.int32([[x * sx, y * sx] for x, y in pts])


def grabcut(img, seed_fg, seed_bg, prob_fg, iters=6):
    m = np.full(img.shape[:2], cv2.GC_PR_BGD, np.uint8)
    m[prob_fg > 0] = cv2.GC_PR_FGD
    m[seed_fg > 0] = cv2.GC_FGD
    m[seed_bg > 0] = cv2.GC_BGD
    bgd, fgd = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)
    cv2.grabCut(img, m, None, bgd, fgd, iters, cv2.GC_INIT_WITH_MASK)
    a = np.isin(m, (cv2.GC_FGD, cv2.GC_PR_FGD)).astype(np.uint8)
    # keep the largest components only, clean holes
    a = cv2.morphologyEx(a, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    a = cv2.morphologyEx(a, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(a)
    if n > 1:
        big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
        a = (lab == big).astype(np.uint8)
    return a


def finish(name, img, a, band=40):
    af = cv2.GaussianBlur(a.astype(np.float32), (0, 0), 1.2)
    fg = np.dstack([img, (af * 255).astype(np.uint8)])
    cv2.imwrite(str(O / f"{name}_fg.png"), fg)
    ring = cv2.dilate(a, np.ones((9, 9), np.uint8)) & (1 - cv2.erode(a, np.ones((band * 2 + 1,) * 2, np.uint8)))
    ip = cv2.inpaint(img, ring * 255, 9, cv2.INPAINT_TELEA)
    cv2.imwrite(str(O / f"{name}_ip.png"), ip)
    dbg = img.copy()
    dbg[a == 0] = (dbg[a == 0] * 0.3).astype(np.uint8)
    cnt, _ = cv2.findContours(a, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(dbg, cnt, -1, (0, 255, 0), 2)
    cv2.imwrite(str(DBG / f"matte_{name}.jpg"), cv2.resize(dbg, (960, 540)))
    cv2.imwrite(str(DBG / f"ip_{name}.jpg"), cv2.resize(ip, (960, 540)))


def poly(pts):
    m = np.zeros((H0, W0), np.uint8)
    cv2.fillPoly(m, [pts], 1)
    return m


which = sys.argv[2:] or ["k09", "k14", "k17"]

if "k09" in which:
    img = cv2.imread(str(K / "k09.png"))
    prob = poly(P((30, 140), (200, 140), (215, 330), (330, 330), (400, 500), (330, 540), (30, 540)))
    sure = poly(P((110, 200), (170, 200), (180, 330), (60, 420), (80, 520), (260, 520), (300, 420), (160, 260)))
    sure |= poly(P((50, 240), (100, 240), (120, 330), (50, 400)))
    bg = 1 - cv2.dilate(prob, np.ones((25, 25), np.uint8))
    bg |= poly(P((222, 180), (345, 180), (345, 322), (222, 322)))  # lamp, phone, side table
    bg |= poly(P((30, 130), (100, 130), (100, 212), (30, 212)))   # wall above the chair wing
    bg |= poly(P((335, 430), (400, 430), (400, 470), (335, 470)))  # rug
    a = grabcut(img, sure, bg, prob)
    finish("k09", img, a)

if "k14" in which:
    img = cv2.imread(str(K / "k14.png"))
    al = cv2.imread(str(O / "k14_fg_ida_al.png"), -1)[..., 3] > 128
    al = al.astype(np.uint8)
    al[int(505 / 565 * H0):, :int(405 / 1003 * W0)] = 0
    al[int(505 / 565 * H0):, int(590 / 1003 * W0):] = 0
    sure = cv2.erode(al, np.ones((21, 21), np.uint8))
    prob = cv2.dilate(al, np.ones((9, 9), np.uint8))
    bg = 1 - cv2.dilate(al, np.ones((31, 31), np.uint8))
    a = grabcut(img, sure, bg, prob)
    finish("k14", img, a, band=60)

if "k17" in which:
    img = cv2.imread(str(K / "k17.png"))
    Y = np.mgrid[0:H0, 0:W0][0] / H0
    lum = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) / 255.0
    sure = (Y > 0.80).astype(np.uint8)
    bg = (Y < 0.50).astype(np.uint8)
    tram = poly(P((0, 196), (60, 206), (200, 250), (216, 262), (216, 310), (0, 310)))  # tram rides with the crowd
    prob = ((Y > 0.53) & (lum < 0.22)).astype(np.uint8) | (Y > 0.70).astype(np.uint8)
    sure |= cv2.erode(tram, np.ones((9, 9), np.uint8)); prob |= tram; bg &= 1 - cv2.dilate(tram, np.ones((15, 15), np.uint8))
    a = grabcut(img, sure, bg, prob)
    finish("k17", img, a, band=40)
