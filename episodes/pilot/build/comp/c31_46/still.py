"""Render single full-res frames of a reel spec: uv run still.py NN t1 [t2 ...] [--crop x0,y0,x1,y1]"""
import json, sys
from pathlib import Path
import cv2
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools/comp"))
import reel
args = sys.argv[1:]
crop = None
if "--crop" in args:
    i = args.index("--crop"); crop = list(map(int, args[i + 1].split(","))); args = args[:i]
n = args[0]
spec = json.loads((reel.ROOT / f"work/pilot/comp/{n}.json").read_text())
shot = reel.Shot(spec)
want = sorted(int(round(float(t) * 24)) for t in args[1:])
for i in range(max(want) + 1):
    f = shot.frame(i)
    if i in want:
        if crop: f = f[crop[1]:crop[3], crop[0]:crop[2]]
        p = Path(__file__).parent / f"qa/{n}_{i:03d}.jpg"
        cv2.imwrite(str(p), cv2.cvtColor(f, cv2.COLOR_RGB2BGR), [cv2.IMWRITE_JPEG_QUALITY, 88]); print(p)
