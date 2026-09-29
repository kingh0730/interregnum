"""Shared helpers for the shots 31-45 prep scripts (story reel v3). Intermediates only; reel.py does the finish."""
import json
import subprocess
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[4]
KEYS = ROOT / "work/pilot/keys_v3"
JS = ROOT / "work/pilot/js_v3"
OUT = Path(__file__).resolve().parent
FPS = 24


def rd(path):
    """Read an image as float32 RGB in 0..1 (display space)."""
    im = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)
    if im is None:
        raise FileNotFoundError(path)
    if im.ndim == 2:
        im = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
    a = None
    if im.shape[2] == 4:
        a = im[..., 3].astype(np.float32) / 255
        im = im[..., :3]
    rgb = im[..., ::-1].astype(np.float32) / 255
    return (rgb, a) if a is not None else rgb


def key(name):
    return rd(KEYS / f"{name}.png")


def wr(path, rgb, a=None):
    im = (np.clip(rgb, 0, 1) * 255 + 0.5).astype(np.uint8)[..., ::-1]
    if a is not None:
        im = np.dstack([im, (np.clip(a, 0, 1) * 255 + 0.5).astype(np.uint8)])
    cv2.imwrite(str(path), im)


def lum(rgb):
    return rgb @ np.array([0.2126, 0.7152, 0.0722], np.float32)


def hsv(rgb):
    h = cv2.cvtColor((np.clip(rgb, 0, 1) * 255).astype(np.uint8), cv2.COLOR_RGB2HSV_FULL).astype(np.float32)
    return h[..., 0] * 360 / 256, h[..., 1] / 255, h[..., 2] / 255


def cyan_mask(rgb, lo=0.35):
    """Pixels lit by cold screen ink: blue/green high, red low."""
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    c = np.clip(((g + b) / 2 - r - 0.08) * 4, 0, 1) * np.clip((np.maximum(g, b) - lo) * 5, 0, 1)
    return c.astype(np.float32)


def amber_mask(rgb, lo=0.3):
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    c = np.clip((r - b - 0.15) * 4, 0, 1) * np.clip((r - lo) * 4, 0, 1) * np.clip((g - 0.6 * r + 0.15) * 5, 0, 1)
    return c.astype(np.float32)


def feather(m, px):
    return cv2.GaussianBlur(m.astype(np.float32), (0, 0), px) if px else m


def noise1(t, hz, seed):
    r = np.random.default_rng(seed)
    ph = r.uniform(0, 2 * np.pi, 4)
    f = hz * np.array([1.0, 1.618, 2.414, 3.303])
    a = np.array([0.55, 0.25, 0.13, 0.07])
    return float((a * np.sin(2 * np.pi * f * t + ph)).sum())


def ease_sine(u):
    u = np.clip(u, 0, 1)
    return 0.5 - 0.5 * np.cos(np.pi * u)


class Writer:
    """Lossless RGBA (PNG-in-MOV) intermediate; reel.py reads it as a video layer."""

    def __init__(self, path, w, h, alpha=True):
        self.w, self.h, self.alpha = w, h, alpha
        self.p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgba", "-s",
                                   f"{w}x{h}", "-r", str(FPS), "-i", "-", "-c:v", "png", "-pix_fmt",
                                   "rgba" if alpha else "rgb24", str(path)], stdin=subprocess.PIPE)

    def put(self, rgb, a=None):
        if a is None:
            a = np.ones(rgb.shape[:2], np.float32)
        im = np.dstack([np.clip(rgb, 0, 1), np.clip(a, 0, 1)[..., None]])
        self.p.stdin.write((im * 255 + 0.5).astype(np.uint8).tobytes())

    def close(self):
        self.p.stdin.close()
        self.p.wait()


def video_frames(path):
    pr = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
                         "-of", "csv=p=0", str(path)], capture_output=True, text=True)
    w, h = map(int, pr.stdout.strip().split(",")[:2])
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(path), "-f", "rawvideo", "-pix_fmt", "rgba", "-"],
                         stdout=subprocess.PIPE)
    while True:
        buf = p.stdout.read(w * h * 4)
        if len(buf) < w * h * 4:
            break
        im = np.frombuffer(buf, np.uint8).reshape(h, w, 4).astype(np.float32) / 255
        yield im[..., :3], im[..., 3]


def ecc_align(src, ref, mode=cv2.MOTION_HOMOGRAPHY, mask=None):
    """Warp src onto ref (float RGB). Returns warped src and the warp."""
    g1 = cv2.cvtColor((ref * 255).astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float32) / 255
    g2 = cv2.cvtColor((src * 255).astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float32) / 255
    W = np.eye(3, 3, dtype=np.float32) if mode == cv2.MOTION_HOMOGRAPHY else np.eye(2, 3, dtype=np.float32)
    crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 200, 1e-6)
    _, W = cv2.findTransformECC(g1, g2, W, mode, crit, None if mask is None else (mask > 0).astype(np.uint8), 5)
    h, w = ref.shape[:2]
    fl = cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP
    out = (cv2.warpPerspective(src, W, (w, h), flags=fl, borderMode=cv2.BORDER_REPLICATE)
           if mode == cv2.MOTION_HOMOGRAPHY else cv2.warpAffine(src, W, (w, h), flags=fl,
                                                                 borderMode=cv2.BORDER_REPLICATE))
    return out, W


def paper(path, amp=0.02, seed=7):
    """Static paper-grain multiply layer (fibre + tooth), 1920x1080, mean ~1-amp."""
    if Path(path).exists():
        return
    r = np.random.default_rng(seed)
    H, W = 1080, 1920
    n = np.zeros((H, W), np.float32)
    for sc, a in [(1, 0.5), (2, 0.3), (6, 0.25)]:
        z = r.normal(0, 1, (H // sc + 1, W // sc + 1)).astype(np.float32)
        n += a * cv2.resize(z, (W, H), interpolation=cv2.INTER_LINEAR)
    # fibres: short faint strokes
    fib = np.zeros((H, W), np.float32)
    for _ in range(2500):
        x, y = r.uniform(0, W), r.uniform(0, H)
        ang = r.uniform(0, np.pi)
        L = r.uniform(6, 30)
        cv2.line(fib, (int(x), int(y)), (int(x + np.cos(ang) * L), int(y + np.sin(ang) * L)), float(r.uniform(.3, 1)),
                 1, cv2.LINE_AA)
    n = n / n.std() * 0.6 + cv2.GaussianBlur(fib, (0, 0), 0.6) * 0.8
    m = 1 - amp * (0.5 + 0.5 * np.clip(n / 2, -1, 1))
    wr(path, np.dstack([m, m, m]))


def save_json(path, obj):
    Path(path).write_text(json.dumps(obj, indent=1))
