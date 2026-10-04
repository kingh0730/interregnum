#!/usr/bin/env python3
"""Flags blank frames, unintended freezes (stutter) and cut-rate profile problems. Usage: qa_frames.py frames/"""
import sys, glob, numpy as np
from PIL import Image
files = sorted(glob.glob(sys.argv[1] + '/*.png'))
assert len(files) == 1311, f'expected 1311 frames, got {len(files)}'
ALLOWED_HOLDS = [(11.27, 11.92)]   # S13 stop-time; add others deliberately, never silently
prev, bad, cuts = None, [], []
for i, f in enumerate(files):
    a = np.asarray(Image.open(f).convert('L').resize((192, 108)), dtype=np.float32)
    if a.mean() < 2 or a.mean() > 253: bad.append((i, 'blank', float(a.mean())))
    if prev is not None:
        d = float(np.abs(a - prev).mean())
        t = i / 30
        if d < 0.02 and not any(lo <= t <= hi for lo, hi in ALLOWED_HOLDS): bad.append((i, 'frozen', d))
        if d > 28: cuts.append(round(t, 2))
    prev = a
print('hard cuts detected at:', cuts)
print('PROBLEMS:' if bad else 'no blank/frozen problems', *bad[:60], sep='\n')
sys.exit(1 if bad else 0)
