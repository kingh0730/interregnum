"""Shot 04 FREEZE layers: glitch frames, frozen/desat stills (HALL navy lift baked, since grade lift is 0 so the
sliding bars stay black), ghost ear, letterbox bars."""
import sys; sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import *

fz = rd(ROOT / "work/pilot/k02_frozen.png").astype(np.float32) / 255
NAVY = np.array([0x20, 0x10, 0x0B], np.float32)[None, None] / 255 * 0.7     # BGR, #0B1020 (70 %)
BLIFT = np.array([38, 24, 16], np.float32)[None, None] / 255                 # broadcast #101826


def lift(img, l):
    return img + l * (1 - img)


def desat(img, a):
    g = img @ np.array([0.0722, 0.7152, 0.2126], np.float32)
    return img * (1 - a) + g[..., None] * a


def save(name, img):
    cv2.imwrite(str(C / name), np.clip(img * 255 + 0.5, 0, 255).astype(np.uint8))


# glitch frames 0-2: broadcast look, slices +-12 px, rgb split 4 px, 20 % luma dip
rng = np.random.default_rng(4)
for i in range(3):
    g = lift(fz, BLIFT).copy()
    for _ in range(4):
        y0 = int(rng.uniform(100, 950)); h = int(rng.uniform(30, 140)); dx = int(rng.choice([-12, -8, 8, 12]))
        g[y0:y0 + h] = np.roll(g[y0:y0 + h], dx, axis=1)
    g[..., 2] = np.roll(g[..., 2], 4, axis=1); g[..., 0] = np.roll(g[..., 0], -4, axis=1)
    save(f"04_g{i}.png", g * (0.8 if i < 2 else 0.9))
save("04_color.png", lift(fz, NAVY))
save("04_desat.png", lift(desat(fz, 0.6), NAVY))

# ghost ear: ear region of the desaturated frame, +6 px x, 40 %
ex, ey, ew, eh = 1216, 398, 92, 244          # ear_box from episodes/pilot/js/mesh_k02.json
d = lift(desat(fz, 0.6), NAVY)
gh = np.zeros((H, W, 4), np.float32)
gh[ey:ey + eh, ex + 6:ex + 6 + ew, :3] = d[ey:ey + eh, ex:ex + ew]
m = np.zeros((eh, ew), np.float32); m[6:-6, 6:-6] = 1; m = cv2.GaussianBlur(m, (0, 0), 3)
gh[ey:ey + eh, ex + 6:ex + 6 + ew, 3] = 0.4 * m
cv2.imwrite(str(C / "04_ghost.png"), np.clip(gh * 255 + 0.5, 0, 255).astype(np.uint8))

# J16 overlay: the JS render (re-marked on the real k02_frozen at 06:01) is used directly in 04.json.

# letterbox bars sliding in over 0.30 s (layer starts at 0.15), easeOutCubic, then held
bars = Pipe(C / "04_bars.mov", rgba=True)
for i in range(9):
    u = min(1, i / 24 / 0.30); h = int(round(138 * (1 - (1 - u) ** 3)))
    f = np.zeros((H, W, 4), np.uint8)
    f[:h, :, 3] = 255; f[H - h:, :, 3] = 255
    bars.put(f)
bars.close()
