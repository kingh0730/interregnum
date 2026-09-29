"""k20 acceptance: align k20 to k02 and paste back only the eye region (feathered)."""
from common import *
a = key("k02_father_cu"); b = key("k20_father_eyes_closed")
bw, Wp = ecc_align(b, a, cv2.MOTION_HOMOGRAPHY)
print("warp", Wp.round(4).tolist())
h, w = a.shape[:2]
d = np.abs(a - bw).mean(2)
ds = cv2.GaussianBlur(d, (0, 0), 6)
print("diff outside eyes after align", ds.mean())
# eye region: box around both eyes, refined by the smoothed diff
box = np.zeros((h, w), np.float32)
x0, x1, y0, y1 = int(.36 * w), int(.64 * w), int(.33 * h), int(.47 * h)
box[y0:y1, x0:x1] = 1
m = ((ds > 0.05) * box).astype(np.uint8)
m = cv2.dilate(m, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (41, 41)))
m = feather(m.astype(np.float32), 9)
m = np.clip(m * 1.3, 0, 1)
out = a * (1 - m[..., None]) + bw * m[..., None]
wr(OUT / "k20_fixed.png", out)
wr(OUT / "k20_mask.png", np.dstack([m] * 3))
ys, xs = np.where(m > 0.02)
print("mask bbox", xs.min() / w, xs.max() / w, ys.min() / h, ys.max() / h)
c = (slice(int(.28 * h), int(.55 * h)), slice(int(.3 * w), int(.7 * w)))
sheet = np.vstack([np.hstack([a[c], out[c]]), np.hstack([bw[c], np.dstack([m] * 3)[c]])])
wr(OUT / "k20_check.jpg", sheet)
