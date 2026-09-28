"""Shot 15 THE CITY. Plate video (k08 minus the fg tower): windows + their canal reflections breathe +-6 % at 0.25 Hz,
J15 stand-by inserted into the billboard, ripple displacement on the canal. FG tower: still (windows pre-darkened
6 %, warm halo on the amber window) + an add-blend mp4 carrying its breathing. Also saves work/pilot/k08_windows.npz."""
import sys; sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import *
FPS, DUR = 24, 7.0
N = int(DUR * FPS)
k = rd(K / "k08.png")[..., :3]
h, w = k.shape[:2]
hsv = cv2.cvtColor(k, cv2.COLOR_BGR2HSV).astype(np.int32)
cyan = ((hsv[..., 0] >= 85) & (hsv[..., 0] <= 105) & (hsv[..., 2] > 150) & (hsv[..., 1] > 60)).astype(np.uint8)
n, lab, st, _ = cv2.connectedComponentsWithStats(cyan, connectivity=4)
bb = np.argmax(st[1:, 4]) + 1                       # the billboard
bx, by, bw, bh = st[bb, :4]
WATER_Y = 690
win = (cyan > 0) & (lab != bb) & (np.mgrid[0:h, 0:w][0] < WATER_Y)
refl = (cyan > 0) & (np.mgrid[0:h, 0:w][0] >= WATER_Y)
amber = ((hsv[..., 0] >= 5) & (hsv[..., 0] <= 25) & (hsv[..., 2] > 150) & (hsv[..., 1] > 100))
amber[:, :1250] = False; amber[:400] = False; amber[600:] = False
wl = lab.copy(); wl[~win] = 0
np.savez_compressed(ROOT / "work/pilot/k08_windows.npz", labels=wl.astype(np.int32), windows=win, reflections=refl,
                    amber=amber, billboard=np.array([bx, by, bw, bh]), size=np.array([w, h]),
                    note="k08 source px (1672x941). labels: connected components of cyan windows above the waterline "
                         "(0 = none); windows/reflections/amber: bool masks; billboard: x,y,w,h")
fgs = rd(K / "k08_fg_tower.png").astype(np.float32) / 255
fa = fgs[..., 3]

def up(m, blur=0.8):
    m = cv2.resize(m.astype(np.float32), (W, H), interpolation=cv2.INTER_LINEAR)
    return cv2.GaussianBlur(m, (0, 0), blur) if blur else m

plate = cv2.resize(k, (W, H), interpolation=cv2.INTER_CUBIC).astype(np.float32) / 255
wmask = up((win | refl) & (fa < 0.5))[..., None]
fgw = up(win & (fa >= 0.5))[..., None]
# billboard: black it out, add the stand-by (cropped to the board's aspect)
S = W / w
quad = np.float32([[bx, by], [bx + bw, by], [bx + bw, by + bh], [bx, by + bh]]) * S
bmask = up(lab == bb, 1.0)[..., None]
cw = int(1080 * bw / bh); cx0 = (1920 - cw) // 2
Mb = cv2.getPerspectiveTransform(np.float32([[cx0, 0], [cx0 + cw, 0], [cx0 + cw, 1080], [cx0, 1080]]), quad)
sb = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(ROOT / "work/pilot/js/j15_standby.mp4"), "-f", "rawvideo",
                       "-pix_fmt", "bgr24", "-"], stdout=subprocess.PIPE)
# canal ripple: water region minus the dock
water = np.zeros((h, w), np.uint8); water[WATER_Y + 2:] = 1
cv2.fillPoly(water, [np.int32([(0, 680), (200, 688), (222, 760), (335, 790), (440, 845), (560, 895), (600, 941), (0, 941)])], 0)
water = up(water, 4)
Y, X = np.mgrid[0:H, 0:W].astype(np.float32)
depth = np.clip((Y - WATER_Y * S) / (H - WATER_Y * S), 0, 1)

fg_still = fgs.copy()
fg_still[..., :3] *= (1 - 0.06 * cv2.resize(fgw[..., 0], (w, h))[..., None])
# warm halo around the amber window (in the fg layer, so it moves with the tower)
am = cv2.GaussianBlur(amber.astype(np.float32), (0, 0), 14) * 0.9
halo = am[..., None] * np.array([0.25, 0.62, 0.95], np.float32)       # BGR amber
fg_still[..., :3] = fg_still[..., :3] + halo * (1 - fg_still[..., :3]) * 0.6
fg_still[..., 3] = np.maximum(fg_still[..., 3], np.clip(am * 0.5, 0, 1) * (fa > 0.01))
cv2.imwrite(str(C / "15_fg.png"), np.clip(fg_still * 255 + 0.5, 0, 255).astype(np.uint8))
fg_lin = (cv2.resize(fgs[..., :3], (W, H)) ** 2.2) * fgw

pv = Pipe(C / "15_plate.mp4"); fv = Pipe(C / "15_fgbreath.mp4")
for i in range(N):
    t = i / FPS
    s = np.sin(2 * np.pi * 0.25 * t)
    f = plate * (1 + 0.06 * s * wmask)
    fr = np.frombuffer(sb.stdout.read(1920 * 1080 * 3), np.uint8).reshape(1080, 1920, 3).astype(np.float32) / 255
    ins = cv2.warpPerspective(fr, Mb, (W, H), flags=cv2.INTER_AREA)
    f = f * (1 - bmask) + (ins * 1.7 + np.float32([0.10, 0.08, 0.02])) * bmask
    dx = water * (1.2 + 3.5 * depth) * (np.sin(Y * 0.21 + t * 2.6 + 1.7 * np.sin(X * 0.004 + t * 0.7))
                                         + 0.5 * np.sin(Y * 0.53 - t * 3.9))
    f = cv2.remap(f, X + dx, Y + 0.4 * dx, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    pv.put(f * 255)
    d = fg_lin * 0.06 * (1 + s)
    fv.put(np.clip(d, 0, 1) ** (1 / 2.2) * 255)
pv.close(); fv.close(); sb.stdout.close()
