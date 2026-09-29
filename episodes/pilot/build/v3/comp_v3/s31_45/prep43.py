"""Shot 43: k26 (aligned to k03 within 0.4 px, so used whole) + the Wall insert (J15 wall mode, tile by tile into the
84 tube faces the plate actually has, 12 x 7) + the reverse dolly as a depth warp (pull 1.07 -> 1.00 about (0.50, 0.66),
parallax 1.0 near -> 0.55 at the wall) + carved dust. Output plate is 1920x1080 with the camera baked in."""
from common import *

W, H = 1920, 1080
a = key("k26_hall_empty"); h, w = a.shape[:2]
cmask = cyan_mask(a, 0.3)
bm = (cmask > 0.3).astype(np.uint8)
reg = np.zeros_like(bm); reg[int(.25 * h):int(.6 * h), int(.3 * w):int(.7 * w)] = 1
n, lab, st, cen = cv2.connectedComponentsWithStats(bm * reg, 8)
tubes = [i for i in range(1, n) if st[i, 4] > 60]
X0 = min(st[i, 0] for i in tubes); X1 = max(st[i, 0] + st[i, 2] for i in tubes)
Y0 = min(st[i, 1] for i in tubes); Y1 = max(st[i, 1] + st[i, 3] for i in tubes)
print(len(tubes), "tubes; wall", X0, X1, Y0, Y1)
# picture (x 240-1680 of the J15 frame) cover-fitted to the wall: full width, centre band of its height
pw, ph = 1440, 1080
sc = pw / (X1 - X0)
vis_h = (Y1 - Y0) * sc
py0 = (ph - vis_h) / 2
rng = np.random.default_rng(43)
gains = {i: np.array([1 + rng.uniform(-.08, .08), 1 + rng.uniform(-.08, .08), 1 + rng.uniform(-.08, .08)]) *
         (1 + rng.uniform(-.1, .1)) for i in tubes}
dead = tubes[int(rng.integers(len(tubes)))]
gains[dead] = np.array([0.04, 0.05, 0.06])
face = feather(np.isin(lab, tubes).astype(np.float32), 0.6) * np.clip(cmask * 1.5, 0, 1)
facemed = np.median(lum(a)[np.isin(lab, tubes)])
shade = np.clip(lum(a) / facemed, 0.3, 1.2) ** 0.5
# per-tube source maps into the picture, with barrel k1 0.05 per tube
mx = np.zeros((h, w), np.float32); my = np.zeros((h, w), np.float32); tg = np.ones((h, w, 3), np.float32)
tid = np.full((h, w), -1, np.int32)
for i in tubes:
    x, y, ww, hh, _ = st[i]
    x -= 2; y -= 2; ww += 4; hh += 4
    ys, xs = np.mgrid[y:y + hh, x:x + ww].astype(np.float32)
    lx = (xs - (x + ww / 2)) / (ww / 2); ly = (ys - (y + hh / 2)) / (hh / 2)
    k = 1 - 0.05 * (lx ** 2 + ly ** 2)
    xx = x + ww / 2 + lx * k * ww / 2; yy = y + hh / 2 + ly * k * hh / 2
    mx[y:y + hh, x:x + ww] = 240 + (xx - X0) * sc
    my[y:y + hh, x:x + ww] = py0 + (yy - Y0) * sc
    tg[y:y + hh, x:x + ww] = gains[i]
wallbox = np.zeros((h, w), bool); wallbox[Y0 - 3:Y1 + 3, X0 - 3:X1 + 3] = True


def insert(frame, t):
    tex = cv2.remap(frame, mx, my, cv2.INTER_AREA if False else cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    # hum bar: a dark band rolling up the picture every 7 s
    v = (my - py0) / vis_h
    bar = 1 - 0.12 * np.exp(-(((v - (1.15 - (t / 7.0) % 1 * 1.3)) / 0.08) ** 2))
    val = tex * tg * shade[..., None] * 1.25 * bar[..., None]
    m = (face * wallbox)[..., None]
    return a * (1 - m) + val * m


wall_frames = [f for f, _ in video_frames(JS / "j15_standby_wall.mp4")]
still = insert(wall_frames[0], 0.0)
(ROOT / "work/pilot/v3").mkdir(parents=True, exist_ok=True)
wr(ROOT / "work/pilot/v3/k26_wall.png", still)
wr(OUT / "k26_wall_check.jpg", cv2.resize(still[int(.25 * h):int(.6 * h), int(.3 * w):int(.7 * w)], None, fx=2, fy=2))

# camera: depth warp
U, V = np.meshgrid((np.arange(W) + 0.5) / W, (np.arange(H) + 0.5) / H)
r = np.sqrt(((U - 0.5) / 0.5) ** 2 + ((V - 0.45) / 0.55) ** 2)
p = (0.55 + 0.45 * np.clip(r, 0, 1) ** 1.2).astype(np.float32)
f = (0.5, 0.66)
light = feather(np.clip(lum(still) * 2, 0, 1), 50)
light = cv2.resize(light / light.max(), (W, H))
light = np.clip(light * 1.6 + 0.12, 0, 1)
dr = np.random.default_rng(431)
N = 120
dx, dy = dr.uniform(0, 1, N), dr.uniform(0, 1, N)
dz = dr.uniform(0.5, 1.5, N); dvy = dr.uniform(0.004, 0.01, N) * 0.7 * dz; dph = dr.uniform(0, 6.3, N)
dsz = dr.uniform(0.7, 1.6, N) * dz
wtr = Writer(OUT / "p43_plate.mov", W, H, alpha=False)
for i in range(144):
    t = i / FPS
    z = 1.07 + (1.0 - 1.07) * t / 6.0
    s = 1 + (z - 1) * p
    su = f[0] + (U - f[0]) / s; sv = f[1] + (V - f[1]) / s
    im = cv2.remap(insert(wall_frames[i], t), (su * w - 0.5).astype(np.float32), (sv * h - 0.5).astype(np.float32),
                   cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    # dust: hard pale specks, lit only inside the light, moving with the dolly at their own depth
    lay = np.zeros((H * 2, W * 2), np.float32)
    xs = (dx + 0.004 * np.sin(t * 0.7 + dph)) % 1; ys = (dy + dvy * t) % 1
    sd = 1 + (z - 1) * np.clip(0.55 + 0.4 * dz, 0.5, 1.2)
    xs = f[0] + (xs - f[0]) * sd; ys = f[1] + (ys - f[1]) * sd
    for xi, yi, si, pi in zip(xs, ys, dsz, dph):
        cv2.ellipse(lay, (int(xi * W * 2), int(yi * H * 2)), (max(1, int(si * 1.5)), max(1, int(si))), float(pi * 57),
                    0, 360, float(0.6 + 0.4 * np.sin(t * 1.9 + pi * 3)), -1, cv2.LINE_AA)
    lay = cv2.resize(lay, (W, H), interpolation=cv2.INTER_AREA)
    da = np.clip(lay * light * 0.5, 0, 1)[..., None]
    im = im * (1 - da) + np.array([0.82, 0.93, 0.93], np.float32) * da
    wtr.put(im)
wtr.close()
