"""The Proof / Wall variant of the engraved k02: the cream halo disc toned down so a desaturated picture on a monitor
reads like the smooth k02 did (its disc was smaller and sat in a mid-blue ground). Luminance x0.72 on the disc only,
through a soft colour-distance mask (the disc's cream, measured on a 2 px blur) confined to the disc's circle and to
the disc's own connected region, so the face, hair, beard and coat are untouched.
Used by: prep_assets.sh (embed k02p -> j16_proof.html: the J16 overlay's picture/ghost ear and J03's tube picture),
pre_0115.py (04's frozen picture once it is on the Proof's tube; f04_frozen.png for the 05 Wall insert) and
s16_30/shots_b.py (the 23 tile wall). The broadcast shots (02 03 29 31 34) keep the key as is.
usage: uv run work/pilot/comp_v3/tone_disc.py  ->  work/pilot/v3/k02_proof.png (+ k02_proof_mask.png)"""
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "work/pilot/keys_v3/k02_father_cu.png"
OUT = ROOT / "work/pilot/v3/k02_proof.png"
GAIN = 0.72


def disc_mask(im):
    b = cv2.GaussianBlur(im, (0, 0), 2)
    b4 = cv2.GaussianBlur(im, (0, 0), 6)
    ref = np.median(b4[(b4.min(2) > 0.7) & (b4[..., 0] - b4[..., 2] > 0.12)], 0)   # the disc's cream
    d = np.linalg.norm(b - ref, axis=2)
    soft = np.clip((0.22 - d) / 0.12, 0, 1)
    hard = (np.linalg.norm(b4 - ref, axis=2) < 0.12).astype(np.uint8)
    n, lab, st, _ = cv2.connectedComponentsWithStats(hard)
    big = st[1:, cv2.CC_STAT_AREA].max()                  # the head splits the disc: keep every large piece
    keep = np.isin(lab, [i for i in range(1, n) if st[i, cv2.CC_STAT_AREA] > 0.05 * big]).astype(np.uint8)
    (cx, cy), r = cv2.minEnclosingCircle(cv2.findNonZero(keep))
    circ = np.zeros(keep.shape, np.float32)
    cv2.circle(circ, (int(cx), int(cy)), int(r + 3), 1, -1, cv2.LINE_AA)
    region = cv2.dilate(keep, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (13, 13))).astype(np.float32)
    m = soft * region * circ
    return cv2.GaussianBlur(m, (0, 0), 1.2), (cx, cy, r), ref


if __name__ == "__main__":
    im = cv2.imread(str(SRC))[..., ::-1].astype(np.float32) / 255
    m, (cx, cy, r), ref = disc_mask(im)
    out = im * (1 - (1 - GAIN) * m[..., None])
    OUT.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(OUT), (np.clip(out, 0, 1) * 255 + .5).astype(np.uint8)[..., ::-1])
    cv2.imwrite(str(OUT.with_name("k02_proof_mask.png")), (m * 255 + .5).astype(np.uint8))
    print(f"disc centre ({cx:.0f}, {cy:.0f}) r {r:.0f}, cream {np.round(ref * 255)}, mask mean {m.mean():.3f}")
    print(OUT)
