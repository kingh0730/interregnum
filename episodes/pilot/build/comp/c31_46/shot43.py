"""Shot 43 THE EMPTY HALL: k26 with the J15 stand-by (static, 50 %) inserted into the monitor wall through its own
bezel grid, the lit desk's monitors dimmed, the foreground desks cut out of the plate for parallax."""
from fx import *

k26, k03 = key("k26"), key("k03")
fg = key("k03_fg_desks")
h, w = k26.shape[:2]

# wall: the bright tile field of k03 (tiles bright, bezels dark) -> bounding quad + a soft tile mask
L03 = lum(k03)
tiles = ((L03 > 0.5) & (k03[..., 2] > k03[..., 0] + 0.2)).astype(np.uint8)
n, lab, st, _ = cv2.connectedComponentsWithStats(cv2.morphologyEx(tiles, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8)))
i = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
x, y, bw, bh = st[i, :4]
print("wall", x, y, bw, bh)
tile_m = blur((tiles * (lab == i)).astype(np.float32), 0.8)[..., None]
wall_m = blur((lab == i).astype(np.float32), 1.0)[..., None]

# J15 static, centre-cropped to the wall's aspect so the emblem stays round
j15 = cv2.imread(str(JS / "j15_standby_static.png"))[..., ::-1].astype(np.float32) / 255
ch = int(round(1920 * bh / bw))
j15 = j15[540 - ch // 2:540 - ch // 2 + ch]
ins = cv2.resize(j15, (bw, bh), interpolation=cv2.INTER_AREA)
canvas = np.zeros_like(k26)
canvas[y:y + bh, x:x + bw] = ins
# per-tile brightness jitter +-4 % (static: the broadcast is over)
rng = np.random.default_rng(43)
nt, tl = cv2.connectedComponents((tiles * (lab == i)).astype(np.uint8))
print("tiles", nt - 1)
fac = rng.uniform(0.96, 1.04, nt).astype(np.float32)
fac[0] = 1.0
jit = fac[cv2.dilate(tl.astype(np.float32), np.ones((5, 5), np.uint8)).astype(int)]
canvas *= jit[..., None]
canvas = canvas * 0.5
haze = np.array([0x1A, 0x35, 0x50], np.float32) / 255
canvas = canvas * 0.85 + haze * 0.15
bezel = k26 * 0.35                                  # dark bezels, from the plate itself
wall = canvas * tile_m + bezel * (1 - tile_m)
plate = k26 * (1 - wall_m) + wall * wall_m
# softer bloom: a wide, faint glow of the insert into the haze
glow = blur(canvas * tile_m, 25) * 0.35
plate = plate + glow * (1 - plate)

# the lit desk's two small monitors: dim them
L26 = lum(k26)
mon = ((L26 > 0.55) & (k26[..., 2] > k26[..., 0] + 0.15)).astype(np.float32)
mon[: int(0.62 * h)] = 0
mon[int(0.80 * h):] = 0
mon = blur(cv2.dilate(mon, np.ones((5, 5), np.uint8)), 3)[..., None]
plate = plate * (1 - mon) + plate * mon * np.array([0.38, 0.55, 0.68], np.float32)

# the signal lamp above the wall stays unlit (it switched off in shot 35)
rm = ((k26[..., 0] > 0.3) & (k26[..., 0] > 2 * k26[..., 1]) & (k26[..., 0] > 1.6 * k26[..., 2])).astype(np.float32)
rm[int(0.35 * h):] = 0
print("red lamp px", int(rm.sum()))
rm = blur(cv2.dilate(rm, np.ones((5, 5), np.uint8)), 2.5)[..., None]
off = np.dstack([plate[..., 1] * 0.9, plate[..., 1], plate[..., 2]]) * 0.5
plate = plate * (1 - rm) + off * rm

# parallax: cut the foreground desks out of the plate (inpaint under them) and re-use them from k26 pixels
fa = fg[..., 3]
hole = cv2.dilate((fa > 0.05).astype(np.uint8), np.ones((9, 9), np.uint8))
p8 = (np.clip(plate, 0, 1) * 255).astype(np.uint8)
clean = cv2.inpaint(p8, hole, 5, cv2.INPAINT_TELEA).astype(np.float32) / 255
save_png(HERE / "p43_plate.png", clean)
save_png(HERE / "p43_fg.png", np.dstack([plate, fa]))

spec(43, 6.0, [{"src": rel(HERE / "p43_plate.png"), "par": 0.55},
               {"src": rel(HERE / "p43_fg.png"), "par": 1.0}],
     camera={"from": focus_cam(0.50, 0.74, 1.07), "to": [0.5, 0.5, 1.0], "ease": "inout"},
     particles=[{"kind": "dust", "n": 120, "seed": 43, "par": 1.1, "wind": [0.002, -0.002],
                 "color": [0.75, 0.9, 1.0], "opacity": 0.35, "size": 0.7}],
     grade_=grade("HALL", exposure=float(np.log2(0.85))))
