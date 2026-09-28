"""Composite the Blender character renders over the v2 background/FX.

Usage: python comp.py twos|ones      -> render/turn_blender_<mode>.mp4
       python comp.py still A.png ... -> render/still_<name>.png previews
"""
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent / "v2"))
import render as R  # noqa: E402

N = 78
shot = R.Shot2()


def load_char(path):
    ch = cv2.imread(str(path), cv2.IMREAD_UNCHANGED).astype(np.float32) / 255
    ch = cv2.resize(ch, (R.SW, R.SH), interpolation=cv2.INTER_AREA)
    ch[..., :3] *= ch[..., 3:4]
    return ch


def grade_char(gw, sun):
    """Anime compositing on the character layer (output space, premultiplied):
    warm/dim grade, a painted rim of sunlight on the sun-facing edge, and a light gradient."""
    a = gw[..., 3:4]
    rgb = gw[..., :3]
    # grade: pull whites down, warm the midtones, deepen shadows a touch
    rgb = rgb * np.array([0.80, 0.84, 0.95], np.float32)
    rgb = np.clip(rgb, 0, None) ** 1.25
    lum = rgb.mean(-1, keepdims=True)
    rgb = lum + (rgb - lum) * 1.35                     # more saturated, less chalky
    # rim light: alpha edge on the side facing the sun
    sx, sy = sun
    H, W = a.shape[:2]
    ys, xs = np.nonzero(a[..., 0] > 0.5)
    cx, cy = xs.mean(), ys.mean()
    d = np.array([sx - cx, sy - cy], np.float32)
    d /= np.linalg.norm(d) + 1e-6
    sh = np.float32([[1, 0, -d[0] * 9], [0, 1, -d[1] * 9]])
    shifted = cv2.warpAffine(a[..., 0], sh, (W, H))
    rim = np.clip(a[..., 0] - shifted, 0, 1)
    rim = cv2.GaussianBlur(rim, (0, 0), 1.6) * a[..., 0]
    rgb = rgb + rim[..., None] * np.array([0.45, 0.72, 1.0], np.float32) * 0.85
    # gradient: warm glow toward the sun, cooler and darker toward the bottom
    Y, X = np.mgrid[0:H, 0:W].astype(np.float32)
    warm = np.exp(-(((X - sx) / (W * 0.55)) ** 2 + ((Y - sy) / (H * 0.7)) ** 2))
    rgb = rgb * (1 + 0.18 * warm[..., None] * np.array([0.3, 0.7, 1.0], np.float32))
    rgb = rgb * (1 - 0.22 * np.clip((Y - H * 0.55) / (H * 0.45), 0, 1))[..., None]
    return np.dstack([rgb, a[..., 0]])


def frame(ch, i):
    t = i / 24
    u = R.ease(t / (N / 24))
    z, off = 1.03 + 0.04 * u, (10 - 25 * u, 0)
    Mb = R.cam_matrix(z, off, shot.focus, 0.4)
    img = R.warp(shot.bg, Mb, opaque=True)[..., :3]
    img = R.draw_sparkles(img, shot.spark, Mb, t)
    sx, sy = R.apply_pt(Mb, *shot.sun)
    img = shot.petals.draw(img, t, 0.0, 0.9)
    gw = grade_char(R.warp(ch, R.cam_matrix(z, off, shot.focus, 1.0)), (sx, sy))
    bg = img.copy()
    bg = R.sun_flare(bg, sx, sy, t, 0.7)                # flare lives behind her...
    img = R.over(bg, gw) + R.light_wrap(bg, gw[..., 3], 0.35)
    img = img + 0.25 * (R.sun_flare(np.zeros_like(img), sx, sy, t, 0.7))  # ...with only a faint veil over her
    img = shot.petals.draw(img, t, 0.9, 9)
    return R.finish(img, t, i, min(1.0, i / 10, (N - 1 - i) / 12) if i >= 0 else 1.0)


if __name__ == "__main__":
    if sys.argv[1] == "still":
        for p in sys.argv[2:]:
            img = frame(load_char(p), 40)
            cv2.imwrite(str(HERE / "render" / f"still_{Path(p).stem}.png"), (img * 255 + 0.5).astype(np.uint8))
        sys.exit()
    step = 2 if sys.argv[1] == "twos" else 1
    out = HERE / "render" / f"turn_blender_{sys.argv[1]}.mp4"
    ff = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24",
                           "-s", f"{R.OW}x{R.OH}", "-r", "24", "-i", "-", "-c:v", "libx264", "-crf", "14",
                           "-pix_fmt", "yuv420p", str(out)], stdin=subprocess.PIPE)
    for i in range(N):
        src = (i // step) * step + 1                     # hold each pose for `step` frames
        img = frame(load_char(HERE / "render" / "frames" / f"{src:03d}.png"), i)
        ff.stdin.write((img * 255 + 0.5).astype(np.uint8).tobytes())
    ff.stdin.close()
    ff.wait()
    print("wrote", out)
