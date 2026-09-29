"""Shots 35 (ON AIR off: J21 glass texture by homography onto k21) and 37 (House Line: J12 card, lamp, spill)."""
import json
import sys

from common import *
from prep_shots import jitter, poly_mask, src

R = np.random.default_rng


def s35():
    a = src("k21_on_air"); h, w = a.shape[:2]
    quad = np.float32([[298, 286], [1379, 286], [1386, 549], [297, 551]])
    srcq = np.float32([[60, 320], [1860, 320], [1860, 760], [60, 760]])
    M = cv2.getPerspectiveTransform(srcq, quad)
    qm = np.zeros((h, w), np.float32); cv2.fillPoly(qm, [np.int32(quad)], 1.0, cv2.LINE_AA)
    qm = feather(qm, 1.2)[..., None]
    # red spill outside the glass: the red ink's excess over the cold channels
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    excess = np.clip(r - np.maximum(g, b), 0, 1) * (1 - qm[..., 0])
    wgt = np.clip(excess * 4, 0, 1)[..., None]
    mn = np.minimum(g, b)[..., None] * np.array([0.92, 1.0, 1.08], np.float32)
    base = a * (1 - wgt) + mn * wgt                                  # the housing with no red light on it
    frames = list(video_frames(JS / "j21_on_air.mp4"))
    lv = np.array([lum(f[0][320:760, 60:1860]).mean() for f in frames]); lv /= lv[0]
    print("J21 level", lv.round(3).tolist())
    wtr = Writer(OUT / "p35_plate.mov", w, h, alpha=False)
    for i, (f, _) in enumerate(frames[:48]):
        glass = cv2.warpPerspective(f, M, (w, h), flags=cv2.INTER_AREA)
        k = float(np.clip((lv[i] - lv[-1]) / (1 - lv[-1]), 0.0, 1.1))
        im = base * (1 - min(k, 1.0)) + a * min(k, 1.0)                # the spill follows the lamp
        if i > 10:
            im[..., 1] += excess * 0.25 * k                           # the filament's afterglow warms the spill
        im = im * (1 - qm) + glass * qm
        wtr.put(im)
    wtr.close()


def s37():
    p = src("p37_house_line"); h, w = p.shape[:2]
    lamp = json.loads((JS / "j12_lamp.json").read_text())
    L = [f["lamp"] for f in lamp["frames"]]
    frames = list(video_frames(JS / "j12_house_line.mp4"))
    # the card: J12's multiply texture, cropped to the plate card's aspect, by homography
    cardq = np.float32([[903, 614], [1124, 619], [1124, 689], [902, 684]])
    asp = (221 / 70)
    cx0, cy0, cw, chh = 80, 120, 1040, 280
    sw = chh * asp; sx = cx0 + (cw - sw) / 2
    srcq = np.float32([[sx, cy0], [sx + sw, cy0], [sx + sw, cy0 + chh], [sx, cy0 + chh]])
    Mc = cv2.getPerspectiveTransform(srcq, cardq)
    card = cv2.warpPerspective(frames[0][0], Mc, (w, h), flags=cv2.INTER_AREA, borderValue=(1, 1, 1))
    cm = np.zeros((h, w), np.float32); cv2.fillPoly(cm, [np.int32(cardq)], 1.0, cv2.LINE_AA)
    card = card * cm[..., None] + (1 - cm[..., None])
    base = p * card
    # the jewel: the atlas lens (centre 1510,300; R 150) onto the dome (centre 835,509; rx 35, ry 33)
    jx, jy, rx, ry = 835, 509, 36, 34
    Mj = np.float32([[rx / 150, 0, jx - 1510 * rx / 150], [0, ry / 150, jy - 300 * ry / 150]])
    dome = np.zeros((h, w), np.float32); cv2.ellipse(dome, (jx, jy), (rx, ry), 0, 0, 360, 1.0, -1, cv2.LINE_AA)
    dome = feather(dome, 1.0)[..., None]
    a0 = cv2.warpAffine(frames[0][0], Mj, (w, h), flags=cv2.INTER_AREA)
    # the warm spill: a hard-edged pool cut around the lamp on the near planes of the grey set
    r = R(37)
    ang = np.linspace(0, 2 * np.pi, 60, endpoint=False)
    rad = 1 + 0.08 * r.standard_normal(60)
    pool = np.stack([jx + 40 + 250 * rad * np.cos(ang), jy + 70 + 150 * rad * np.sin(ang)], 1)
    pm = poly_mask(p.shape, pool, 0.6)
    body = np.clip((lum(p) - 0.05) * 20, 0, 1)
    body[: jy - 40] = 0
    pm = pm * body
    amber = np.array([0xE9, 0xA2, 0x3B], np.float32) / 255
    tint = amber * (lum(base) / lum(amber[None, None])[..., None] if False else 1)
    lb = lum(base)[..., None]
    amber_px = amber[None, None] * lb / float(lum(amber[None, None]).mean()) * 1.1
    # handsets
    gh = poly_mask(p.shape, [(672, 300), (760, 235), (1000, 205), (1300, 210), (1560, 250), (1612, 330), (1600, 470),
                              (1500, 470), (1420, 330), (1330, 300), (980, 290), (900, 300), (800, 380), (760, 470),
                              (672, 470)], 0.8)
    H_, S_, V_ = hsv(p)
    red = (((H_ < 25) | (H_ > 340)) & (S_ > 0.4) & (V_ > 0.12)).astype(np.float32)
    red[340:] = 0; red[:, 720:] = 0
    rh = feather(cv2.dilate(red, np.ones((5, 5), np.uint8)), 1.0)
    wtr = Writer(OUT / "p37_plate.mov", w, h, alpha=False)
    for i in range(72):
        t = i / FPS
        lv = L[i] if i < len(L) else 0
        im = base.copy()
        k = 0.35 * lv
        im = im * (1 - k * pm[..., None]) + amber_px * (k * pm[..., None])
        im = im * (1 + 0.12 * lv * pm[..., None])
        at = cv2.warpAffine(frames[i][0], Mj, (w, h), flags=cv2.INTER_AREA)
        im = im + np.clip(at - a0, 0, 1) * dome
        ringing = (0.1 <= t < 0.6) or (1.6 <= t < 2.1)
        if ringing:
            im = jitter(im, gh, r.uniform(-0.5, 0.5), r.uniform(-0.5, 0.2))
        if 2.0 <= t < 2.9:
            im = jitter(im, rh, r.uniform(-1, 1), r.uniform(-1, 1))
        wtr.put(im)
        if i == 8:
            wr(OUT / "p37_lit.jpg", np.clip(im[400:720, 700:1200], 0, 1))
    wtr.close()


if __name__ == "__main__":
    for s in sys.argv[1:]:
        globals()["s" + s]()
        print("done", s)
