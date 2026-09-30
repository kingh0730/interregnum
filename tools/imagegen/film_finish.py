"""Film finish: pull generated stills toward one photographic look and away from AI sheen.

usage: uv run tools/imagegen/film_finish.py <in> <out> [--strength 1.0]
Steps (each gentle; strength scales them):
 1. De-oil: blend in a bilateral-smoothed copy on mid-frequency detail only, which softens the over-crisp micro-contrast
    ("oily" skin and surfaces) while keeping edges.
 2. Specular tame: compress luminance above ~0.8 with a soft shoulder (glossy highlights read as AI).
 3. Film curve: lift the blacks slightly, soft toe and shoulder, a touch less saturation in highlights and shadows.
 4. Halation: a faint warm glow around only the brightest edges.
 5. Grain: luminance-weighted monochrome grain at film scale (a 2 px cluster), stronger in the midtones.
"""
import argparse

import cv2
import numpy as np


def finish(img, s=1.0, seed=7):
    x = img.astype(np.float32) / 255.0
    # 1. de-oil: reduce mid-frequency detail (band between 1.5 px and 6 px blurs)
    b1 = cv2.GaussianBlur(x, (0, 0), 1.5)
    b2 = cv2.GaussianBlur(x, (0, 0), 6.0)
    mid = b1 - b2
    smooth = cv2.bilateralFilter((x * 255).astype(np.uint8), 7, 25, 7).astype(np.float32) / 255.0
    x = x * (1 - 0.35 * s) + smooth * (0.35 * s) - mid * 0.15 * s
    # 2. specular tame: soft shoulder on luminance
    lum = x @ np.array([0.299, 0.587, 0.114], np.float32)
    knee = 0.78
    over = np.clip(lum - knee, 0, None)
    newl = np.where(lum > knee, knee + over / (1 + over * 3.0 * s), lum)
    x = x * (newl / np.maximum(lum, 1e-4))[..., None]
    # 3. film curve: lifted blacks, soft toe, gentle desaturation at the extremes
    x = 0.035 * s + x * (1 - 0.05 * s)
    x = np.clip(x, 0, 1)
    x = x + 0.06 * s * np.sin(np.pi * x) * (x - 0.5)  # a mild S around the midtones
    lum = (x @ np.array([0.299, 0.587, 0.114], np.float32))[..., None]
    ext = np.abs(lum - 0.5) * 2
    x = lum + (x - lum) * (1 - 0.18 * s * ext)
    # 4. halation: warm glow from the brightest areas only
    hot = np.clip(lum - 0.85, 0, None)
    glow = cv2.GaussianBlur(hot, (0, 0), 9)[..., None] * np.array([0.35, 0.18, 0.08], np.float32)[None, None, ::-1]
    x = x + glow * 1.4 * s
    # 5. grain: luminance-weighted, clumped
    rng = np.random.default_rng(seed)
    g = rng.normal(0, 1, x.shape[:2]).astype(np.float32)
    g = cv2.GaussianBlur(g, (0, 0), 0.9)
    w = 0.5 + 0.5 * np.sin(np.pi * np.clip(lum[..., 0], 0, 1))
    x = x + (g * w * 0.028 * s)[..., None]
    return (np.clip(x, 0, 1) * 255 + 0.5).astype(np.uint8)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("inp")
    ap.add_argument("out")
    ap.add_argument("--strength", type=float, default=1.0)
    a = ap.parse_args()
    im = cv2.imread(a.inp, cv2.IMREAD_COLOR)
    cv2.imwrite(a.out, finish(im, a.strength))
    print(a.out)
