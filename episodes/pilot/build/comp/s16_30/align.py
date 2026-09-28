"""Align cutout layers k09/k14/k17 fg onto their plates (SIFT similarity), save aligned RGBA + debug overlay."""
import cv2, numpy as np, sys
from pathlib import Path
R = Path(__file__).resolve().parents[4]
K = R / "work/pilot/keys"; O = Path(__file__).parent
S = Path(sys.argv[1]) if len(sys.argv) > 1 else O

def align(fg, plate, name):
    sift = cv2.SIFT_create(8000)
    m = (fg[..., 3] > 230).astype(np.uint8) * 255
    k1, d1 = sift.detectAndCompute(cv2.cvtColor(fg[..., :3], cv2.COLOR_BGR2GRAY), m)
    k2, d2 = sift.detectAndCompute(cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY), None)
    good = [a for a, b in cv2.BFMatcher().knnMatch(d1, d2, k=2) if a.distance < 0.75 * b.distance]
    p1 = np.float32([k1[x.queryIdx].pt for x in good]); p2 = np.float32([k2[x.trainIdx].pt for x in good])
    M, inl = cv2.estimateAffinePartial2D(p1, p2, method=cv2.RANSAC, ransacReprojThreshold=3.0)
    s = np.hypot(M[0, 0], M[0, 1])
    print(f"{name}: {len(good)} matches, {int(inl.sum())} inliers, scale={s:.4f} shift=({M[0,2]:.1f},{M[1,2]:.1f})")
    out = cv2.warpAffine(fg, M, (plate.shape[1], plate.shape[0]), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_CONSTANT)
    return out

for k, fgn in [("k09", "k09_fg_nana"), ("k14", "k14_fg_ida"), ("k17", "k17_fg_crowd")]:
    plate = cv2.imread(str(K / f"{k}.png")); fg = cv2.imread(str(K / f"{fgn}.png"), -1)
    al = align(fg, plate, fgn)
    cv2.imwrite(str(O / f"{fgn}_al.png"), al)
    a = al[..., 3:4] / 255.0
    dbg = (plate * (1 - a * 0.5) + np.array([0, 0, 255]) * a * 0.5 * (np.abs(al[..., :3].astype(float) - plate).mean(-1, keepdims=True) / 60)).clip(0, 255)
    edge = cv2.Canny(al[..., 3], 50, 150) > 0
    dbg[edge] = (0, 255, 0)
    cv2.imwrite(str(S / f"dbg_{fgn}.jpg"), cv2.resize(dbg.astype(np.uint8), None, fx=0.6, fy=0.6))
