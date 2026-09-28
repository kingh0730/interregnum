"""Shot 44 THE WARM WINDOWS: per-window cyan->amber switch-on wave from Nana's window, dawn sky swell, canal
reflections following their windows, drips from the tram wires. Writes the plate p44.mp4 (whole frame) and the
foreground tower fg44.mov (same animation, k08_fg_tower alpha) for parallax, then comp/44.json.
usage: uv run shot44.py [--still t ...]   (--still writes QA stills of the plate instead)"""
import sys

from fx import *

DUR = 10.0
SEED_XY = np.array([1343.0, 490.0])          # Nana's amber window centroid in k27 (1672x941)
AMBER = np.array([0xF2, 0xA4, 0x41], np.float32) / 255
AMBER_L = float(lum(AMBER[None, None])[0, 0])
MIRROR_Y = 640.0                              # water mirror axis: window y 490 <-> reflection y 790
WATER_Y = 662

k27, k08 = key("k27"), key("k08")
H_, W_ = k27.shape[:2]
M = np.load(HERE / "masks44.npz")
lab, cen, area = M["lab"], M["cen"], M["area"]
r, g, b = k27[..., 0], k27[..., 1], k27[..., 2]

# ------------------------------------------------------------------ windows (above the waterline)
n = len(area)
bb = np.zeros((n, 4), int)
ys, xs = np.nonzero(lab)
ls = lab[ys, xs]
bb[:, 0] = W_; bb[:, 1] = H_
np.minimum.at(bb[:, 0], ls, xs); np.minimum.at(bb[:, 1], ls, ys)
np.maximum.at(bb[:, 2], ls, xs); np.maximum.at(bb[:, 3], ls, ys)
bw, bh = bb[:, 2] - bb[:, 0] + 1, bb[:, 3] - bb[:, 1] + 1
fill = area / np.maximum(1, bw * bh)
cx, cy = cen[:, 0], cen[:, 1]
train = (cx > 290) & (cx < 500) & (cy > 560) & (cy < 605)
bad = (np.arange(n) > 0) & ((area > 1500) | (bh >= 60) | (bw >= 60) | ((fill < 0.35) & (area > 30)))
badzone = cv2.dilate(np.isin(lab, np.nonzero(bad)[0]).astype(np.uint8), np.ones((15, 15), np.uint8))
near_bad = np.zeros(n, bool)
near_bad[np.unique(lab[(badzone > 0) & (lab > 0)])] = True
top_band = ((cy < 70) & (cx < 1140)) | ((cy > 612) & (cx < 760))   # + lights under the bridge deck                      # bright cloud edges at the top of the sky
win = (np.arange(n) > 0) & (area >= 2) & ~bad & ~near_bad & (fill >= 0.35) & (cy < WATER_Y - 12) & ~train \
      & ~top_band
flat = lab.ravel()
mr = np.bincount(flat, r.ravel(), n) / np.maximum(area, 1)
mg = np.bincount(flat, k27[..., 1].ravel(), n) / np.maximum(area, 1)
mb = np.bincount(flat, b.ravel(), n) / np.maximum(area, 1)
refl = (np.arange(n) > 0) & (cy >= WATER_Y) & (area >= 2) & (area <= 6000) & (mg - mr > 0.08) & (mb - mr > 0.12) \
       & (fill >= 0.12)
print("windows", win.sum(), "reflection blobs", refl.sum())

rng = np.random.default_rng(44)
d = np.hypot(cx - SEED_XY[0], cy - SEED_XY[1])
dmax = d[win].max()
t_sw = 1.0 + 7.0 * (d / dmax) ** 0.8 + rng.uniform(-0.4, 0.4, n)
kind = np.zeros(n, int)                        # 0 amber, 1 dark (bedtime), 2 holdout (stays blue)
u = rng.uniform(0, 1, n)
kind[u < 0.08] = 1
kind[(u >= 0.08) & (u < 0.11)] = 2
order = np.argsort(np.where(win & (area >= 40), d, 1e9))
first = order[:12]
kind[first] = 0                                # the first switches near Nana's window all turn warm, one by one
t_sw[first] = 1.0 + np.linspace(0, 0.95, 12) + rng.uniform(-0.03, 0.03, 12)
early = win & (area < 40) & (t_sw < 2.0)
t_sw[early] = np.maximum(t_sw[early], 2.0)
t_sw = np.clip(t_sw, 0.9, None)

# reflection pixels take the switch time of the window at their mirrored position (nearest window), +0.2 s
winmask = np.isin(lab, np.nonzero(win)[0]).astype(np.uint8)
dist, near = cv2.distanceTransformWithLabels(1 - winmask, cv2.DIST_L2, 5, labelType=cv2.DIST_LABEL_PIXEL)
# map DIST_LABEL_PIXEL index -> component label
zy, zx = np.nonzero(winmask == 1)
pix_lab = np.zeros(near.max() + 1, np.int32)
# labels are assigned to zero pixels (window pixels) in raster order
pix_lab[1:len(zy) + 1] = lab[zy, zx]
assert (near[zy, zx] == np.arange(1, len(zy) + 1)).all(), "DIST_LABEL_PIXEL order assumption broken"
near_lab = pix_lab[near]                       # nearest window component for every pixel
# window reflections in the canal: cyan and brighter than their local surroundings (the reflected facades are
# themselves blue, so a plain threshold merges whole towers into one blob)
L27_ = lum(k27)
rows_ = np.arange(H_)[:, None]
reflmask = ((rows_ >= WATER_Y) & (b > r + 0.12) & (k27[..., 1] > r + 0.08) & (L27_ > 0.2)
            & (L27_ - blur(L27_, 10) > 0.035)).astype(np.uint8)
reflmask = cv2.morphologyEx(reflmask, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8))
reflmask[860:, :600] = 0                        # the stone edge in the foreground
reflmask[:690, :420] = 0                        # lights under the bridge
print("reflection px", int(reflmask.sum()))

# per-pixel owner label + delay, over a dilated support (windows + halo, reflections + halo)
own = np.zeros((H_, W_), np.int32)
delay = np.zeros((H_, W_), np.float32)
sup_w = cv2.dilate(winmask, np.ones((9, 9), np.uint8))
own[sup_w > 0] = near_lab[sup_w > 0]
wdist = dist
sup_r = cv2.dilate(reflmask, np.ones((7, 7), np.uint8)) & (np.arange(H_)[:, None] >= WATER_Y - 4)
ry, rx = np.nonzero(sup_r)
my = np.clip((2 * MIRROR_Y - ry).astype(int), 0, H_ - 1)
own[ry, rx] = near_lab[my, rx]
delay[ry, rx] = 0.2
# weights: 1 in the lit glass, falling off over the glow halo
core_w = blur(winmask.astype(np.float32), 0.7)
halo_w = np.exp(-wdist / 2.5).astype(np.float32) * (sup_w > 0)
wt = np.maximum(core_w, 0.85 * halo_w)
core_r = blur(reflmask.astype(np.float32), 0.8)
wt[ry, rx] = np.maximum(core_r[ry, rx], 0.6 * np.exp(-cv2.distanceTransform(1 - reflmask, cv2.DIST_L2, 3)[ry, rx] / 2.0))
wt = wt * (own > 0)
wt3 = wt[..., None]

# targets: amber keeps each pixel's luminance pattern (x1.1); dark = the unlit facade (inpainted), dimmed
L27 = lum(k27)
LCORE = 0.72                                   # typical luminance of a lit cyan window core in k27
amberized = np.clip(AMBER * (1.1 * np.clip(L27 / LCORE, 0, 1.15))[..., None], 0, 1)
refl_rows = (np.arange(H_)[:, None] >= WATER_Y - 4)[..., None]
amberized = np.where(refl_rows, np.clip(AMBER * (1.0 * np.clip(L27 / 0.55, 0, 1.1))[..., None], 0, 1), amberized)
holes = cv2.dilate(((winmask + reflmask) > 0).astype(np.uint8), np.ones((5, 5), np.uint8))
small = cv2.resize((k27 * 255).astype(np.uint8), (W_ // 2, H_ // 2), interpolation=cv2.INTER_AREA)
hs = cv2.resize(holes, (W_ // 2, H_ // 2), interpolation=cv2.INTER_NEAREST)
unlit = cv2.resize(cv2.inpaint(small, hs, 3, cv2.INPAINT_TELEA), (W_, H_)).astype(np.float32) / 255
dark = unlit * 0.75

# ------------------------------------------------------------------ sky
sky = blur(M["sky"].astype(np.float32), 1.5)[..., None]
wsky = blur(M["wsky"].astype(np.float32), 2.0)[..., None]
k08s = blur(k08, 5)
pink = np.clip((r - b) * 3 + 0.2, 0, 1)[..., None] * np.clip((L27 - 0.15) * 4, 0, 1)[..., None]

# ------------------------------------------------------------------ drips from the upper tram wire
WIRE = lambda x: 390 - 0.41 * x
drng = np.random.default_rng(144)
drips = [(0.4 + 1.5 * j + drng.uniform(-0.3, 0.3), drng.uniform(180, 820)) for j in range(7)]


def frame(t):
    s = 0.6 + 0.4 * ease_sine(t / DUR)
    base = k27 * s + k08s * (1 - s)
    img = k27 * (1 - sky) + base * sky
    img = img * (1 - wsky) + (k27 * (0.75 + 0.25 * s) + k08s * (0.25 - 0.25 * s)) * wsky
    wl = ease_sine((t - 6.0) / 4.0)
    img = img * (1 + 0.08 * wl * pink * sky * np.array([1.0, 0.85, 0.6], np.float32))
    # windows
    tt = t_sw[own] + delay                                   # per-pixel switch time
    p = np.clip((t - tt) / 0.35, 0, 1) * (own > 0)
    p = p * p * (3 - 2 * p)
    kd = kind[own]
    p = np.where(kd == 2, 0, p)
    pop = 1 + 0.10 * (((t - tt) >= 0.35) & ((t - tt) < 0.35 + 1 / FPS) & (kd == 0))
    tgt = np.where((kd == 1)[..., None], dark, amberized * pop[..., None])
    a = (p * wt)[..., None]
    img = img * (1 - a) + tgt * a
    # soft 6 px warm glow around lit windows
    gsrc = cv2.resize((p * (kd == 0) * np.clip(core_w + core_r * 0.6, 0, 1)).astype(np.float32),
                      (W_ // 2, H_ // 2), interpolation=cv2.INTER_AREA)
    glow = cv2.resize(blur(gsrc, 3.0), (W_, H_))[..., None]
    img = img + glow * AMBER * 0.30 * (1 - img)
    # drips
    for t0, x in drips:
        if t0 <= t < t0 + 0.7:
            dt = t - t0
            y = WIRE(x) + 4 + 0.5 * 1400 * dt * dt
            if y < H_:
                al = 0.55 * (1 - dt / 0.7)
                y1 = y - min(18, 2 + 1400 * dt * 0.012)
                lay = np.zeros((H_, W_), np.float32)
                cv2.line(lay, (int(x * 16), int(y1 * 16)), (int(x * 16), int(y * 16)), 1.0, 2, cv2.LINE_AA, shift=4)
                lay = blur(lay, 0.6)[..., None] * al
                img = img * (1 - lay) + np.array([0.95, 0.85, 0.9], np.float32) * lay
    return np.clip(img, 0, 1)


def main():
    if "--still" in sys.argv:
        for ts in sys.argv[sys.argv.index("--still") + 1:]:
            save_png(HERE / f"qa/p44_{float(ts):04.1f}.png", frame(float(ts)))
        return
    fga = key("k08_fg_tower")[..., 3:4]
    wp = Writer(HERE / "p44.mp4", W_, H_)
    wf = Writer(HERE / "fg44.mov", W_, H_, alpha=True)
    for i in range(int(round(DUR * FPS))):
        f = frame(i / FPS)
        wp.write(f)
        wf.write(np.dstack([f, fga]))                       # straight alpha; reel premultiplies
    wp.close()
    wf.close()
    spec(44, DUR, [{"src": rel(HERE / "p44.mp4"), "par": 0.4},
                   {"src": rel(HERE / "fg44.mov"), "par": 1.0}],
         camera={"from": focus_cam(SEED_XY[0] / W_, SEED_XY[1] / H_, 1.06), "to": [0.5, 0.5, 1.0], "ease": "inout"},
         grade_=grade("DAWN"))


if __name__ == "__main__":
    main()
