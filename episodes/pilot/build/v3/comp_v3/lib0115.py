"""Shared helpers for the v3 pre-comps of shots 01-15 (inputs to tools/comp/reel.py)."""
import json, subprocess
from pathlib import Path
import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
CV = ROOT / "work/pilot/comp_v3"
KEYS = ROOT / "work/pilot/keys_v3"
JS = ROOT / "work/pilot/js_v3"
W, H, FPS = 1920, 1080, 24
SCR = Path("/private/tmp/claude-501/-Users-kingh0730-repos-interregnum/b27232ca-5280-4208-9826-f1156f716aae/scratchpad")


def P(p):
    p = Path(p)
    return p if p.is_absolute() else ROOT / p


def load(path, size=None, alpha=False):
    """Display-referred float RGB(A) in [0,1]; RGBA is straight (not premultiplied)."""
    im = cv2.imread(str(P(path)), cv2.IMREAD_UNCHANGED)
    if im is None:
        raise FileNotFoundError(path)
    if im.dtype == np.uint16:
        im = (im / 257).astype(np.uint8)
    if im.ndim == 2:
        im = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
    if im.shape[2] == 4:
        im = cv2.cvtColor(im, cv2.COLOR_BGRA2RGBA)
    else:
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    im = im.astype(np.float32) / 255
    if size:
        im = cv2.resize(im, size, interpolation=cv2.INTER_CUBIC if size[0] > im.shape[1] else cv2.INTER_AREA)
        im = np.clip(im, 0, 1)
    if not alpha and im.shape[2] == 4:
        im = im[..., :3]
    return im


def plate(name):
    return load(KEYS / f"{name}.png", (W, H))


def save(path, img):
    img = np.clip(img, 0, 1)
    if img.shape[2] == 4:
        out = cv2.cvtColor((img * 255 + .5).astype(np.uint8), cv2.COLOR_RGBA2BGRA)
    else:
        out = cv2.cvtColor((img * 255 + .5).astype(np.uint8), cv2.COLOR_RGB2BGR)
    cv2.imwrite(str(P(path)), out)


lin = lambda x: np.clip(x, 0, None) ** 2.2
disp = lambda x: np.clip(x, 0, None) ** (1 / 2.2)


class VReader:
    """Sequential RGBA reader (display-referred float, straight alpha)."""
    def __init__(self, path, size=None):
        path = P(path)
        pr = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                             "stream=width,height", "-of", "csv=p=0", str(path)], capture_output=True, text=True)
        self.w, self.h = map(int, pr.stdout.strip().split(",")[:2])
        self.p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(path), "-f", "rawvideo", "-pix_fmt", "rgba", "-"],
                                  stdout=subprocess.PIPE)
        self.i, self.last = -1, None

    def get(self, i):
        while self.i < i:
            n = self.w * self.h * 4
            buf = self.p.stdout.read(n)
            if len(buf) < n:
                break
            self.last = np.frombuffer(buf, np.uint8).reshape(self.h, self.w, 4).astype(np.float32) / 255
            self.i += 1
        return self.last

    def close(self):
        self.p.kill()


class VWriter:
    def __init__(self, path, size=(W, H), fps=FPS):
        self.size = size
        self.p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s",
                                   f"{size[0]}x{size[1]}", "-r", str(fps), "-i", "-", "-c:v", "libx264", "-crf", "8",
                                   "-preset", "medium", "-pix_fmt", "yuv444p", str(P(path))], stdin=subprocess.PIPE)

    def write(self, img):
        self.p.stdin.write((np.clip(img[..., :3], 0, 1) * 255 + .5).astype(np.uint8).tobytes())

    def close(self):
        self.p.stdin.close()
        self.p.wait()


def premul(rgba):
    return np.dstack([rgba[..., :3] * rgba[..., 3:4], rgba[..., 3:4]])


def over(dst, src_pm):
    """dst RGB, src premultiplied RGBA (same space)."""
    return src_pm[..., :3] + dst * (1 - src_pm[..., 3:4])


def quad_H(src_quad, dst_quad):
    return cv2.getPerspectiveTransform(np.float32(src_quad), np.float32(dst_quad))


def rect_quad(x, y, w, h):
    return [[x, y], [x + w, y], [x + w, y + h], [x, y + h]]


def warp(src, Hm, size=(W, H), border=cv2.BORDER_CONSTANT, interp=cv2.INTER_LINEAR):
    return cv2.warpPerspective(src, Hm.astype(np.float64), size, flags=interp, borderMode=border)


def quad_mask(quad, size=(W, H), feather=0.0, ss=4):
    m = np.zeros((size[1] * 1, size[0] * 1), np.uint8)
    pts = np.round(np.float32(quad) * 16).astype(np.int32)
    cv2.fillPoly(m, [pts], 255, cv2.LINE_AA, shift=4)
    m = m.astype(np.float32) / 255
    if feather:
        m = cv2.GaussianBlur(m, (0, 0), feather)
    return m


def poly_mask(pts, size=(W, H), feather=0.0):
    return quad_mask(pts, size, feather)


def barrel(img, k1, mask_round=0.0, fill=0.0):
    """Barrel-distort an image about its centre (k1 like the JS CRT); optional rounded-corner mask (radius frac of w)."""
    h, w = img.shape[:2]
    Y, X = np.mgrid[0:h, 0:w].astype(np.float32)
    nx, ny = (X - w / 2) / (w / 2), (Y - h / 2) / (w / 2)
    r2 = nx * nx + ny * ny
    f = 1 + k1 * r2
    # inverse approx: sample source at r*(1+k1 r^2) -> pincushion sampling = barrel look
    mx, my = w / 2 + nx * f * (w / 2), h / 2 + ny * f * (w / 2)
    out = cv2.remap(img, mx, my, cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=fill)
    if mask_round:
        m = round_rect_mask(w, h, mask_round * w)
        ins = ((mx >= 0) & (mx <= w - 1) & (my >= 0) & (my <= h - 1)).astype(np.float32)
        m = m * cv2.GaussianBlur(ins, (0, 0), 1.0)
        return out, m
    return out


def round_rect_mask(w, h, r, feather=1.2):
    m = np.zeros((h, w), np.uint8)
    r = int(r)
    cv2.rectangle(m, (r, 0), (w - 1 - r, h - 1), 255, -1)
    cv2.rectangle(m, (0, r), (w - 1, h - 1 - r), 255, -1)
    for cx, cy in [(r, r), (w - 1 - r, r), (r, h - 1 - r), (w - 1 - r, h - 1 - r)]:
        cv2.circle(m, (cx, cy), r, 255, -1, cv2.LINE_AA)
    m = m.astype(np.float32) / 255
    return cv2.GaussianBlur(m, (0, 0), feather) if feather else m


def vignette(w, h, amt, power=1.3):
    Y, X = np.mgrid[0:h, 0:w].astype(np.float32)
    r = ((X - w / 2) / (w / 2)) ** 2 + ((Y - h / 2) / (h / 2)) ** 2
    return np.clip(1 - amt * r ** power, 0, 1)


def bloom(img_lin, thresh=0.6, amt=0.3, sig=(4, 16)):
    br = np.clip(img_lin - thresh, 0, None)
    sm = cv2.resize(br, (img_lin.shape[1] // 4, img_lin.shape[0] // 4), interpolation=cv2.INTER_AREA)
    b = sum(cv2.GaussianBlur(sm, (0, 0), s) for s in sig) / len(sig)
    return img_lin + amt * cv2.resize(b, (img_lin.shape[1], img_lin.shape[0]))


def smooth_noise(seed, t, hz):
    r = np.random.default_rng(seed)
    ph = r.uniform(0, 2 * np.pi, 4)
    f = hz * np.array([1.0, 1.618, 2.414, 3.303])
    a = np.array([0.55, 0.25, 0.13, 0.07])
    return float((a * np.sin(2 * np.pi * f * t + ph)).sum())


def desat(img, amt):
    l = (img * np.float32([0.2126, 0.7152, 0.0722])).sum(-1, keepdims=True)
    return l + (img - l) * (1 - amt)


def ease_out_cubic(u):
    u = min(max(u, 0), 1)
    return 1 - (1 - u) ** 3


def ease_inout_cubic(u):
    u = min(max(u, 0), 1)
    return 4 * u ** 3 if u < .5 else 1 - (-2 * u + 2) ** 3 / 2


# ---------------------------------------------------------------- broadcast()
PX0, PW, PH = 240, 1440, 1080
LIFT = np.float32([0x10, 0x18, 0x26]) / 255


def crop43(img):
    """Centre 4:3 of a 16:9 source, at 1440x1080."""
    h, w = img.shape[:2]
    cw = h * 4 / 3
    x0 = (w - cw) / 2
    M = np.float32([[PW / cw, 0, -x0 * PW / cw], [0, PH / h, 0]])
    return cv2.warpAffine(img, M, (PW, PH), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)


def grade_broadcast(pic, lift=1.0, sat=0.08):
    """grade(BROADCAST): soft, blacks lifted to #101826, mild saturation (picture space, display)."""
    pic = desat(pic, sat)
    pic = pic + np.maximum(LIFT - pic, 0) * lift * np.clip(1 - pic / 0.35, 0, 1)
    return np.clip(pic, 0, 1)


_scan = None


def broadcast(pic, frame, bloom_amt=0.12, vig=0.15, twitter=True):
    """pic: 1440x1080 display RGB (bug/cc already keyed in). Returns the 1920x1080 pillarboxed frame."""
    global _scan
    if _scan is None:
        s = np.ones((PH, 1), np.float32)
        s[::3] = 0.92
        _scan = s[:, :, None]
    x = lin(pic)
    x = bloom(x, 0.55, bloom_amt, (3, 10))
    p = disp(x)
    if twitter:  # interlace twitter: odd frames nudge half a line
        if frame % 2:
            p = 0.8 * p + 0.2 * np.roll(p, 1, 0)
    p = p * _scan
    p[..., 0] = np.roll(p[..., 0], 1, 1)
    p[..., 2] = np.roll(p[..., 2], -1, 1)
    p = p * vignette(PW, PH, vig)[..., None]
    out = np.zeros((H, W, 3), np.float32)
    out[:, PX0:PX0 + PW] = p
    return out


def sheet(frames, path, cols=3, scale=0.25):
    fr = [cv2.resize(f, (int(W * scale), int(H * scale)), interpolation=cv2.INTER_AREA) for f in frames]
    while len(fr) % cols:
        fr.append(np.zeros_like(fr[0]))
    rows = [np.hstack(fr[i:i + cols]) for i in range(0, len(fr), cols)]
    save(path, np.vstack(rows))


def paper_grain(path=CV / "paper_grain.png", amt=0.02, seed=7):
    """Static paper grain for reel.py: a multiply layer (display values ~ 1 - amt..1)."""
    r = np.random.default_rng(seed)
    n = r.normal(0, 1, (H, W)).astype(np.float32)
    fine = cv2.GaussianBlur(n, (0, 0), 0.7)
    fib = cv2.GaussianBlur(r.normal(0, 1, (H, W)).astype(np.float32), (0, 0), 3)
    fib = cv2.resize(cv2.resize(fib, (W // 2, H * 2)), (W, H))
    g = fine / fine.std() * 0.6 + fib / fib.std() * 0.4
    v = 1 - amt * (0.5 + 0.5 * np.clip(g / 2.2, -1, 1))
    save(path, np.dstack([v, v, v, np.ones_like(v)]))
    return path


def grid_crop(img, x0, y0, x1, y1, out, step=20, scale=2):
    c = (np.clip(img[y0:y1, x0:x1, :3], 0, 1) * 255).astype(np.uint8).copy()
    c = cv2.resize(c, None, fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)
    for x in range((x0 // step + 1) * step, x1, step):
        X = (x - x0) * scale
        col = (255, 0, 255) if x % 100 == 0 else (90, 0, 90)
        cv2.line(c, (X, 0), (X, c.shape[0]), col, 1)
        if x % 100 == 0:
            cv2.putText(c, str(x), (X + 2, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 1)
    for y in range((y0 // step + 1) * step, y1, step):
        Y = (y - y0) * scale
        col = (255, 0, 255) if y % 100 == 0 else (90, 0, 90)
        cv2.line(c, (0, Y), (c.shape[1], Y), col, 1)
        if y % 100 == 0:
            cv2.putText(c, str(y), (2, Y - 2), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 1)
    cv2.imwrite(str(out), cv2.cvtColor(c, cv2.COLOR_RGB2BGR))


def fit_quad(m, skip=None):
    """Quad of a rounded-rect glass mask: lines fitted to the middle 60 % of each side, intersected."""
    ys, xs = np.nonzero(m)
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    w, h = x1 - x0, y1 - y0
    top, bot, left, right = [], [], [], []
    for x in range(x0 + int(w * .2), x0 + int(w * .8), 3):
        col = np.nonzero(m[:, x])[0]
        top.append((x, col.min())); bot.append((x, col.max()))
    for y in range(y0 + int(h * .2), y0 + int(h * .8), 3):
        if skip and skip[0] < y < skip[1]:
            continue
        row = np.nonzero(m[y])[0]
        left.append((row.min(), y)); right.append((row.max(), y))
    L = [cv2.fitLine(np.float32(a), cv2.DIST_HUBER, 0, .01, .01).ravel() for a in (top, right, bot, left)]

    def inter(a, b):
        A = np.array([[a[0], -b[0]], [a[1], -b[1]]])
        t = np.linalg.solve(A, [b[2] - a[2], b[3] - a[3]])
        return [float(a[2] + a[0] * t[0]), float(a[3] + a[1] * t[0])]
    return [inter(L[3], L[0]), inter(L[0], L[1]), inter(L[1], L[2]), inter(L[2], L[3])]
