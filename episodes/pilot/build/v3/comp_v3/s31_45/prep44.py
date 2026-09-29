"""Shot 44, THE WARM WINDOWS: k27 + the window wave (screen blue -> lamplight, spreading from Nana's window), the
rose sky strengthening (60 % -> 100 % against k08's night sky), the beacon blinking, drips from the railing, and
the breathing pull (1.08 -> 1.00, easeInOutSine, scaled about her window). Output plate 1920x1080, camera baked."""
from common import *

W, H = 1920, 1080
DUR, N = 10.0, 240
d = key("k27_city_dawn"); h, w = d.shape[:2]
k08 = key("k08_city_night")[:h]
r_, g_, b_ = d[..., 0], d[..., 1], d[..., 2]

# ---- Nana's window (the seed) and the lamp amber
am = amber_mask(d, 0.3); am[:200] = 0; am[420:] = 0; am[:, :1150] = 0; am[:, 1380:] = 0
n, lab, st, cen = cv2.connectedComponentsWithStats((am > 0.4).astype(np.uint8), 8)
i = 1 + np.argmax(st[1:, 4]); seed = cen[i]
nana = (lab == i)
amber_ref = np.median(d[nana & (lum(d) > 0.5)], axis=0)
print("seed", seed, "amber ink", (amber_ref * 255).astype(int))

# ---- windows
cyw = cyan_mask(d, 0.3)
win = (cyan_mask(d, 0.45) > 0.35).astype(np.uint8)
LIM = 655
win[LIM:] = 0
lamps = [(160, 590), (660, 590), (1010, 592), (1560, 578)]
cones = np.zeros((h, w), np.uint8)
for lx, ly in lamps:
    cv2.fillPoly(cones, [np.int32([(lx - 18, ly - 22), (lx + 18, ly - 22), (lx + 100, 700), (lx - 100, 700)])], 1)
win[cones > 0] = 0
grp = cv2.morphologyEx(win, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (9, 5)))
n, lab, st, cen = cv2.connectedComponentsWithStats(grp, 8)
lamps = [(160, 590), (660, 590), (1010, 592), (1560, 578)]
tall = [j for j in range(1, n) if st[j, 3] > 2.2 * st[j, 2] and st[j, 3] > 40]
stair = [(st[j, 0] - 6, st[j, 0] + st[j, 2] + 6) for j in tall]
groups = []
for j in range(1, n):
    if any(x0 <= cen[j][0] <= x1 for x0, x1 in stair):
        continue
    x, y, ww, hh, a = st[j]
    if a < 25 or (hh > 2.2 * ww and hh > 40):                  # specks; stair-tower glass slots stay cold
        continue
    if any(abs(cen[j][0] - lx) < 30 and abs(cen[j][1] - ly) < 25 for lx, ly in lamps) and a < 150:
        continue                                                # street-lamp heads
    groups.append(j)
labd = np.zeros_like(lab)
for j in groups:
    labd[lab == j] = j
labd = cv2.dilate(labd.astype(np.float32), np.ones((7, 7), np.uint8)).astype(np.int32)
labd[LIM:] = 0
labd[cones > 0] = 0
wgt = np.clip(cyw * 3.0, 0, 1) * (labd > 0)
wgt = np.maximum(wgt, (labd > 0) * np.isin(lab, groups) * 1.0)
rng = np.random.default_rng(44)
dist = {j: np.hypot(*(cen[j] - seed)) for j in groups}
dmax = max(dist.values())
order = sorted(groups, key=lambda j: dist[j])
fate = {}
for k, j in enumerate(order):
    u = rng.uniform()
    fate[j] = "amber" if k < 6 else ("dark" if u < 0.08 else ("hold" if u < 0.11 else "amber"))
tsw = {j: 1.0 + 7.0 * (dist[j] / dmax) ** 0.8 + rng.uniform(-0.4, 0.4) for j in groups}
print(len(groups), "windows;", sum(v == "dark" for v in fate.values()), "go dark;",
      sum(v == "hold" for v in fate.values()), "hold out; first switches",
      sorted(round(tsw[j], 2) for j in order[:10]))
save_json(OUT / "win44.json", {"seed": seed.tolist(), "windows": [
    {"id": int(j), "c": [round(float(cen[j][0]), 1), round(float(cen[j][1]), 1)], "t": round(tsw[j], 3),
     "fate": fate[j]} for j in order]})
# per-pixel switch time and fate
T = np.full((h, w), 1e9, np.float32); F = np.zeros((h, w), np.int8)    # 1 amber, 2 dark
for j in groups:
    m = labd == j
    if fate[j] != "hold":
        T[m] = tsw[j]; F[m] = 1 if fate[j] == "amber" else 2
Lc = lum(d)
cyan_ref = np.median(Lc[win > 0])
a_ = np.clip(Lc / cyan_ref, 0, 1.15)[..., None]
amber_px = np.clip(amber_ref / lum(amber_ref[None, None])[0, 0] * Lc[..., None] * 1.1, 0, 1)
key_ink = np.array([17, 21, 31], np.float32) / 255
dark_px = key_ink * (0.6 + 0.5 * a_)

# ---- sky: the warm inks of the dawn, blended toward k08's night sky; the beacon excluded
bx, by = 762, 68
yy, xx = np.mgrid[0:h, 0:w]
bea = np.hypot(xx - bx, yy - by)
skyw = np.clip((r_ - b_ - 0.05) * 5, 0, 1) * np.clip((r_ - 0.2) * 5, 0, 1)
skyw[int(0.25 * h):] = 0
skyw = feather(skyw, 0.8) * (bea > 14)
H_, S_, V_ = hsv(d)
beacon = ((((H_ < 25) | (H_ > 335)) & (S_ > 0.4)) & (bea < 12)).astype(np.float32)
beacon = feather(np.maximum(beacon, 0), 1.0) * np.clip(1.2 - bea / 12, 0, 1)
bexc = np.clip(r_ - np.maximum(g_, b_), 0, 1)
beacon_off = d.copy()
mn = np.minimum(g_, b_)[..., None] * np.array([0.9, 1.0, 1.1], np.float32)
beacon_off = d * (1 - beacon[..., None]) + mn * beacon[..., None]

# ---- drips from the railing (carved beads), one every 1.5 s near the lamp cones
drips = []
dr = np.random.default_rng(441)
for k in range(8):
    t0 = 0.4 + 1.5 * k + dr.uniform(-0.2, 0.2)
    lx = lamps[k % 4][0] + dr.uniform(-70, 70)
    drips.append((t0, lx))
RAIL_Y, LOW_Y = 697, 742


def drip_layer(t):
    lay = np.zeros((h * 2, w * 2), np.float32)
    for t0, x in drips:
        u = t - t0
        if u < 0 or u > 1.2:
            continue
        if u < 0.5:                                             # the bead gathers under the rail
            y, ry = RAIL_Y + 1.5 * u / 0.5, 1 + 1.2 * u / 0.5
        else:
            v = u - 0.5
            y, ry = RAIL_Y + 1.5 + 0.5 * 260 * v * v, 2.4
            if y > LOW_Y:
                continue
        cv2.ellipse(lay, (int(x * 2), int(y * 2)), (2, int(ry * 2)), 0, 0, 360, 1.0, -1, cv2.LINE_AA)
    return cv2.resize(lay, (w, h), interpolation=cv2.INTER_AREA)


# ---- camera
f = np.array([seed[0] / w, seed[1] / h]); ce = np.array([0.5, 0.40])
cover = max(W / w, H / h)
wtr = Writer(OUT / "p44_plate.mov", W, H, alpha=False)
for fi in range(N):
    t = fi / 24
    # sky and beacon
    s = 0.6 + 0.4 * ease_sine(t / DUR)
    im = d * (1 - skyw[..., None]) + (d * s + k08 * (1 - s)) * skyw[..., None]
    ph = t % 2.0
    on = np.clip(min(ph / 0.08, (1.0 - ph) / 0.08), 0, 1) if ph < 1.0 else 0.0
    im = im * (1 - beacon[..., None]) + (d * on + beacon_off * (1 - on)) * beacon[..., None]
    # the wave
    u = np.clip((t - T) / 0.35, 0, 1)[..., None]
    target = np.where((F == 2)[..., None], dark_px, amber_px)
    pop = ((t - T >= 0.35) & (t - T < 0.35 + 1 / 24) & (F == 1))[..., None] * 0.10
    m = wgt[..., None] * u
    im = im * (1 - m) + target * (1 + pop) * m
    # drips
    dl = drip_layer(t)[..., None] * 0.75
    im = im * (1 - dl) + np.array([0.86, 0.9, 0.86], np.float32) * dl
    # breathing pull, scaled about her window
    z = 1.08 + (1.0 - 1.08) * ease_sine(t / DUR)
    c = f + (ce - f) / z
    sc = cover * z
    M = np.float32([[sc, 0, W / 2 - sc * c[0] * w], [0, sc, H / 2 - sc * c[1] * h]])
    out = cv2.warpAffine(im, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    wtr.put(out)
    if fi in (0, 60, 120, 180, 239):
        wr(OUT / f"p44_f{fi:03d}.jpg", out[138:942])
wtr.close()
