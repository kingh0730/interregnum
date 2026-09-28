"""usage: still.py spec.json frame out.jpg [x0 y0 x1 y1]  -- one full-res frame (QA)."""
import sys, json; sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import *
s = reel.Shot(json.loads(open(sys.argv[1]).read()))
f = s.frame(int(sys.argv[2]))
if len(sys.argv) > 4:
    x0, y0, x1, y1 = map(int, sys.argv[4:8]); f = f[y0:y1, x0:x1]
cv2.imwrite(sys.argv[3], cv2.cvtColor(f, cv2.COLOR_RGB2BGR), [cv2.IMWRITE_JPEG_QUALITY, 88])
