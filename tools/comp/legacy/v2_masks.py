"""Build blink patch masks and hair/scarf deformation weight maps; write debug overlays."""
import cv2
import numpy as np
from pathlib import Path

HERE = Path(__file__).parent
P = HERE / "prepped"
DBG = HERE / "debug"


def load(n):
    return cv2.imread(str(P / f"{n}.png"), cv2.IMREAD_UNCHANGED).astype(np.float32) / 255.0


def save_mask(n, m):
    cv2.imwrite(str(P / f"{n}.png"), (np.clip(m, 0, 1) * 255 + 0.5).astype(np.uint8))


def overlay(n, im, m, color=(0, 1, 0)):
    base = im[..., :3] * (0.35 + 0.65 * im[..., 3:4]) if im.shape[2] == 4 else im[..., :3]
    o = base * (1 - 0.6 * m[..., None]) + np.array(color) * 0.6 * m[..., None]
    cv2.imwrite(str(DBG / f"{n}.jpg"), (np.clip(o, 0, 1) * 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 80])


# --- blink: where do the closed/half eyes differ from the open-eyed girl? ---
girl = load("s2_girl")
ref = cv2.imread(str(HERE.parent / "frames" / "03_face.png")).astype(np.float32) / 255.0
for n in ["s2_closed", "s2_half"]:
    im = load(n)
    d = cv2.GaussianBlur(np.abs(im[..., :3] - ref).max(-1), (0, 0), 3)
    blob = (d > 0.08).astype(np.uint8)
    cnt, lab, stats, cent = cv2.connectedComponentsWithStats(blob)
    order = np.argsort(-stats[1:, cv2.CC_STAT_AREA]) + 1
    print(n, "largest diff blobs (x,y,w,h,area):", [tuple(stats[i]) for i in order[:6]])

# --- hair / scarf color masks per girl layer ---
for n in ["s1_girl", "s2_girl", "s3_girl"]:
    im = load(n)
    a = im[..., 3]
    hsv = cv2.cvtColor((im[..., :3] * 255).astype(np.uint8), cv2.COLOR_BGR2HSV).astype(np.float32)
    h, s, v = hsv[..., 0] * 2, hsv[..., 1] / 255, hsv[..., 2] / 255
    scarf = ((h < 12) | (h > 340)) & (s > 0.45) & (v > 0.2) & (a > 0.5)
    scarf = cv2.morphologyEx(scarf.astype(np.uint8), cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    cnt, lab, stats, _ = cv2.connectedComponentsWithStats(scarf)
    keep = np.zeros_like(scarf)
    for i in range(1, cnt):
        if stats[i, cv2.CC_STAT_AREA] > 2000:
            keep[lab == i] = 1
    hair = (s < 0.28) & (v > 0.5) & (a > 0.5)
    ys, xs = np.nonzero(keep)
    print(n, "scarf bbox", xs.min(), ys.min(), xs.max(), ys.max(), "area", keep.sum())
    hy, hx = np.nonzero(hair)
    print(n, "hair-ish bbox", hx.min(), hy.min(), hx.max(), hy.max(), "area", hair.sum())
    save_mask(f"{n}_scarf", keep.astype(np.float32))
    save_mask(f"{n}_hair", hair.astype(np.float32))
    overlay(f"{n}_scarf", im, keep.astype(np.float32), (0, 1, 0))
    overlay(f"{n}_hair", im, hair.astype(np.float32), (1, 0, 1))
