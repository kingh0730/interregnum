"""Measure cream paper margins on each keyframe edge (px of the 1672x941 key)."""
import sys
import cv2
import numpy as np
PAPER = np.array([0xC4, 0xDD, 0xE8], np.float32)  # BGR of #E8DDC4

def margins(path):
    im = cv2.imread(path).astype(np.float32)
    d = np.linalg.norm(im - PAPER, axis=2)
    paper = d < 60
    out = {}
    for name, prof in (("left", paper.mean(0)), ("right", paper.mean(0)[::-1]),
                       ("top", paper.mean(1)), ("bottom", paper.mean(1)[::-1])):
        n = 0
        while n < len(prof) and prof[n] > 0.5:
            n += 1
        # also count thin partial ragged edge (>15%)
        m = n
        while m < 60 and prof[m] > 0.15:
            m += 1
        out[name] = (n, m)
    return out

for p in sys.argv[1:]:
    print(p.split("/")[-1], margins(p))
