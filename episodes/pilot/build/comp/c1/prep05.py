"""Shot 05 THE HALL: plate video = k03 (inpainted under the fg desks) + the frozen face (shot 04 end state: desat k02,
ghost ear, J16 overlay) inserted into the monitor wall tiles with per-tile jitter, haze and glow + dust in the light."""
import sys; sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import *
DUR, FPS = 8.0, 24
k = rd(K / "k03.png")[..., :3].astype(np.float32) / 255
h, w = k.shape[:2]
fg = rd(K / "k03_fg_desks.png")
fa = cv2.dilate((fg[..., 3] > 8).astype(np.uint8), np.ones((9, 9), np.uint8))
plate = cv2.inpaint((k * 255).astype(np.uint8), fa, 6, cv2.INPAINT_TELEA).astype(np.float32) / 255

# wall content = shot 04 final state
face = rd(C / "04_desat.png").astype(np.float32) / 255
g = rd(C / "04_ghost.png").astype(np.float32) / 255
face = face * (1 - g[..., 3:4]) + g[..., :3] * g[..., 3:4]
pr = subprocess.run(["ffmpeg", "-v", "error", "-sseof", "-0.05", "-i", str(ROOT / "work/pilot/js/s04_overlay_j16.mov"), "-frames:v", "1",
                     "-f", "rawvideo", "-pix_fmt", "bgra", "-"], capture_output=True).stdout
ov = np.frombuffer(pr[-W * H * 4:], np.uint8).reshape(H, W, 4).astype(np.float32) / 255
face = face * (1 - ov[..., 3:4]) + ov[..., :3] * ov[..., 3:4]
x0, x1, y0, y1 = 480, 1192, 246, 450                       # tile area in k03
cw = 1240; ch = int(round(cw * (y1 - y0) / (x1 - x0)))
cx0, cy0 = 340, 290
crop = face[cy0:cy0 + ch, cx0:cx0 + cw]
ins = cv2.resize(crop, (x1 - x0, y1 - y0), interpolation=cv2.INTER_AREA)
haze = np.array([0x50, 0x35, 0x1A], np.float32) / 255
ins = ins * 1.25 * 0.85 + haze * 0.15
ins = np.clip(ins, 0, 1)
# tile mask from the painted wall (keeps the painted bezels)
kb = k[y0:y1, x0:x1]
tm = ((kb[..., 0] > 0.7) & (kb[..., 1] > 0.6)).astype(np.float32)
tm = cv2.GaussianBlur(tm, (0, 0), 0.7)[..., None]
lab, nlab = cv2.connectedComponents((tm[..., 0] > 0.5).astype(np.uint8))[1], None
nlab = lab.max() + 1

# dust: lit only inside the wall's light (mask from blurred plate luminance + a cone under the wall)
lum = cv2.GaussianBlur(plate @ np.array([0.11, 0.59, 0.3], np.float32), (0, 0), 25)
Y, X = np.mgrid[0:h, 0:w].astype(np.float32)
cone = np.clip(1 - np.abs(X - w / 2) / (w * 0.22 + (Y - 250) * 0.5), 0, 1) * (Y > 240)
dmask = np.clip(lum * 1.8, 0, 1) * 0.5 + cone * 0.5
rng = np.random.default_rng(5)
N = 120
px, py = rng.uniform(0, w, N), rng.uniform(150, h, N)
pz = rng.uniform(0.5, 1.5, N); ph = rng.uniform(0, 6.28, N)

out = Pipe(C / "05_plate.mp4")
for i in range(int(DUR * FPS)):
    t = i / FPS
    f = plate.copy()
    jit = np.ones((y1 - y0, x1 - x0, 1), np.float32)
    for j in range(1, nlab):
        jit[lab == j] = 1 + 0.04 * smooth_noise(100 + j, t, 0.35)
    f[y0:y1, x0:x1] = f[y0:y1, x0:x1] * (1 - tm) + ins * jit * tm
    d = np.zeros((h, w), np.float32)
    xs = (px - 6 * t * pz + 4 * np.sin(t * 0.7 + ph)) % w
    ys = (py - 3.5 * t * pz + 3 * np.sin(t * 0.5 + ph * 2)) % h
    for xx, yy, zz in zip(xs, ys, pz):
        cv2.circle(d, (int(xx * 16), int(yy * 16)), int(16 * (0.6 + 0.9 * zz)), 1.0, -1, cv2.LINE_AA, shift=4)
    d = cv2.GaussianBlur(d, (0, 0), 0.8) * dmask * 0.55
    f = f + d[..., None] * np.array([1.0, 0.97, 0.85], np.float32)
    out.put(cv2.resize(f, (W, H), interpolation=cv2.INTER_LINEAR) * 255)
out.close()
