"""Shared helpers for shots 01-15 prep (compositor 1). Run from repo root with `uv run python`."""
import importlib.util, subprocess, json
from pathlib import Path
import cv2, numpy as np

ROOT = Path(__file__).resolve().parents[4]
W, H = 1920, 1080
spec = importlib.util.spec_from_file_location("reel", ROOT / "tools/comp/reel.py")
reel = importlib.util.module_from_spec(spec); spec.loader.exec_module(reel)
C = ROOT / "work/pilot/comp/c1"          # my prepared layers
K = ROOT / "work/pilot/keys"


def rd(p, flags=cv2.IMREAD_UNCHANGED):
    im = cv2.imread(str(p), flags)
    assert im is not None, p
    return im


def push_center(fx, fy, z):
    """camera centre that keeps normalized focus (fx, fy) fixed on screen at zoom z."""
    return [fx - (fx - 0.5) / z, fy - (fy - 0.5) / z, z]


def warp(img, cx, cy, z, opaque=True):
    return reel.cam_warp(img, cx, cy, z, opaque)


def src_to_frame(x, y, w, h, cx, cy, z):
    s = max(W / w, H / h) * z
    return W / 2 + s * (x - cx * w), H / 2 + s * (y - cy * h)


class Pipe:
    """Stream frames to ffmpeg. rgba=True -> .mov (png codec, alpha); else mp4."""
    def __init__(self, out, w=W, h=H, rgba=False, fps=24):
        out = str(out)
        if rgba:
            args = ["-c:v", "png", "-pix_fmt", "rgba"]
            pf = "bgra"
        else:
            args = ["-c:v", "libx264", "-crf", "12", "-preset", "medium", "-pix_fmt", "yuv420p"]
            pf = "bgr24"
        self.p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", pf, "-s", f"{w}x{h}",
                                   "-r", str(fps), "-i", "-", *args, out], stdin=subprocess.PIPE)

    def put(self, fr):
        self.p.stdin.write(np.ascontiguousarray(np.clip(fr, 0, 255).astype(np.uint8)).tobytes())

    def close(self):
        self.p.stdin.close(); self.p.wait()


def scanlines():
    p = C / "scanlines.png"
    if not p.exists():
        a = np.zeros((H, W, 4), np.uint8)
        a[::3, :, 3] = int(0.08 * 255)
        cv2.imwrite(str(p), a)
    return p


def smooth_noise(seed, t, hz):
    return reel.smooth_noise(seed, t, hz)
