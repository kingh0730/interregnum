"""broadcast(): pillarbox (4:3 at x 240-1680), scanlines (1 px dark every 3 px at 8 %), interlace twitter
(a 2 % field line alternating each frame). A fixed full-frame RGBA overlay video. Plus shot 34's picture plate:
k02 -> k20 (eye-region paste-back) dissolve 1.0-2.5 s easeInOutSine with a 3 % luma dip at the midpoint."""
import sys
from common import *

H, W = 1080, 1920


def overlay(n_frames, path):
    wtr = Writer(path, W, H)
    y = np.arange(H)[:, None]
    base = np.where(y % 3 == 2, 0.08, 0.0) * np.ones((1, W), np.float32)
    for i in range(n_frames):
        a = base.copy()
        field = (y % 2 == (i % 2)) & (y % 3 != 2)
        a = np.where(field, 0.02, a).astype(np.float32) * np.ones((1, W), np.float32)
        a[:, :240] = 1
        a[:, 1680:] = 1
        wtr.put(np.zeros((H, W, 3), np.float32), a)
    wtr.close()


def plate34():
    a = key("k02_father_cu")
    b = rd(OUT / "k20_fixed.png")
    h, w = a.shape[:2]
    h2 = h - h % 2
    wtr = Writer(OUT / "p34_plate.mov", w, h2, alpha=False)
    for i in range(144):
        t = i / FPS
        u = ease_sine((t - 1.0) / 1.5)
        im = a * (1 - u) + b * u
        if 1.0 <= t <= 2.5:
            im = im * (1 - 0.03 * np.sin(np.pi * (t - 1.0) / 1.5))
        wtr.put(im[:h2])
    wtr.close()


if __name__ == "__main__":
    overlay(120, OUT / "bc_overlay_120.mov")
    overlay(144, OUT / "bc_overlay_144.mov")
    plate34()
