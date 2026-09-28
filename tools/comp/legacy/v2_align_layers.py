"""Align Codex-derived layers to their source keyframes and build deformation masks."""
import cv2
import numpy as np
from pathlib import Path

HERE = Path(__file__).parent
A = HERE / "assets"
OUT = HERE / "prepped"
DBG = HERE / "debug"
OUT.mkdir(exist_ok=True)
DBG.mkdir(exist_ok=True)
FR = HERE.parent / "frames"
W, H = 1672, 941


def load(p):
    im = cv2.imread(str(p), cv2.IMREAD_UNCHANGED)
    if im.shape[2] == 3:
        im = np.dstack([im, np.full(im.shape[:2], 255, np.uint8)])
    im = im.astype(np.float32) / 255.0
    a = im[..., 3]
    if a.max() > 0:
        im[..., 3] = np.clip(a / a.max(), 0, 1)
    return im


def align(src, ref, name):
    """Similarity transform mapping src onto ref, estimated from SIFT matches on opaque pixels."""
    sift = cv2.SIFT_create(6000)
    g = lambda im: cv2.cvtColor((im[..., :3] * 255).astype(np.uint8), cv2.COLOR_BGR2GRAY)
    m = (src[..., 3] > 0.9).astype(np.uint8) * 255
    k1, d1 = sift.detectAndCompute(g(src), m)
    k2, d2 = sift.detectAndCompute(g(ref), None)
    matches = cv2.BFMatcher().knnMatch(d1, d2, k=2)
    good = [a for a, b in matches if a.distance < 0.7 * b.distance]
    p1 = np.float32([k1[x.queryIdx].pt for x in good])
    p2 = np.float32([k2[x.trainIdx].pt for x in good])
    M, inl = cv2.estimateAffinePartial2D(p1, p2, method=cv2.RANSAC, ransacReprojThreshold=2.0)
    s = np.hypot(M[0, 0], M[0, 1])
    print(f"{name}: {len(good)} matches, {int(inl.sum())} inliers, scale={s:.4f} "
          f"rot={np.degrees(np.arctan2(M[1,0], M[0,0])):.3f}deg shift=({M[0,2]:.1f},{M[1,2]:.1f})")
    out = cv2.warpAffine(src, M, (ref.shape[1], ref.shape[0]), flags=cv2.INTER_LANCZOS4,
                         borderMode=cv2.BORDER_REPLICATE if src[..., 3].min() > 0.99 else cv2.BORDER_CONSTANT)
    return np.clip(out, 0, 1)


def save(name, im):
    cv2.imwrite(str(OUT / f"{name}.png"), (np.clip(im, 0, 1) * 255 + 0.5).astype(np.uint8))


refs = {1: load(FR / "02_railing.png"), 2: load(FR / "03_face.png"), 3: load(FR / "05_airplane.png")}
for name, shot in [("s1_sky", 1), ("s1_ground", 1), ("s1_girl", 1), ("s2_bg", 2), ("s2_girl", 2),
                   ("s2_closed", 2), ("s2_half", 2), ("s3_bg", 3), ("s3_girl", 3)]:
    im = load(A / f"{name}.png")
    al = align(im, refs[shot], name)
    save(name, al)
    # debug: difference against the reference where the layer is opaque
    d = np.abs(al[..., :3] - refs[shot][..., :3]).mean(-1) * al[..., 3]
    cv2.imwrite(str(DBG / f"diff_{name}.png"), np.clip(d * 4 * 255, 0, 255).astype(np.uint8))
save("s3_plane", load(A / "s3_plane.png"))
