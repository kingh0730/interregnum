"""Shot 02 stutter plant: frame-hold still + one frame with a 3 px slip on a 120 px slice across the mouth."""
import sys; sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import *
spec = json.loads((ROOT / "work/pilot/comp/02.json").read_text())
cam = reel.Shot.__new__(reel.Shot); cam.s = spec; cam.dur = spec["dur"]
im = rd(K / "k01.png")
hold = warp(im, *cam.camera(100 / 24))          # frame 100 held over frames 101-102
cv2.imwrite(str(C / "02_hold.png"), hold)
slip = warp(im, *cam.camera(103 / 24)).copy()
y0, y1 = 480, 600                                # mouth band
slip[y0:y1] = np.roll(slip[y0:y1], 3, axis=1)
cv2.imwrite(str(C / "02_slip.png"), slip)
