"""Shot 44 masks from k27: cyan windows (components), sky, water. Saves masks44.npz + a QA image."""
from fx import *

k = key("k27")
h, w = k.shape[:2]
r, g, b = k[..., 0], k[..., 1], k[..., 2]
L = lum(k)
rows = np.arange(h)[:, None]
cyan = (b > r + 0.12) & (g > r + 0.08) & (L > np.where(rows >= 662, 0.22, 0.30))
cyan = cyan.astype(np.uint8)
n, lab, st, cen = cv2.connectedComponentsWithStats(cyan, connectivity=8)
keep = np.zeros(n, bool)
keep[1:] = st[1:, cv2.CC_STAT_AREA] >= 2
print("cyan comps", n - 1, "kept", keep.sum())
# sky: bright-ish, not window-cyan, above the bridge line, connected to the top edge
sky_c = ((L > 0.16) & ~(cyan > 0) & ((r > 0.35) | (b > 0.38))).astype(np.uint8)
sky_c[640:] = 0
sky_c = cv2.morphologyEx(sky_c, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
n2, lab2, st2, _ = cv2.connectedComponentsWithStats(sky_c, connectivity=4)
top = set(np.unique(lab2[:5])) - {0}
big = {i for i in range(1, n2) if st2[i, cv2.CC_STAT_AREA] > 400 and st2[i, cv2.CC_STAT_TOP] < 300}
sky = np.isin(lab2, list(top | big)).astype(np.float32)
sky = cv2.morphologyEx(sky, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
# water: below the embankment; sky reflections there = pinkish / blue bright non-cyan pixels
water = np.zeros((h, w), np.float32)
water[700:] = 1
water[:, :0] = 0
wsky = (((r > 0.3) | (b > 0.35)) & ~(cyan > 0) & (L > 0.14)).astype(np.float32) * water
np.savez_compressed(HERE / "masks44.npz", lab=lab.astype(np.int32), keep=keep, cen=cen, area=st[:, cv2.CC_STAT_AREA],
                    sky=sky, wsky=wsky)
q = k.copy() * 0.35
q[cyan > 0] = [0, 1, 1]
q[sky > 0] = q[sky > 0] * 0.3 + np.array([1, 0, 1]) * 0.7
q[wsky > 0] = q[wsky > 0] * 0.3 + np.array([1, 1, 0]) * 0.7
save_png(HERE / "qa/masks44.png", q)
