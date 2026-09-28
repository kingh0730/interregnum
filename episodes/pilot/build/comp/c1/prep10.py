"""Shot 10 CAPSULE: base video with the capsule dropping from the pipe mouth onto the cradle (5-subframe motion
blur), impact shake, dust puff, brass glint, one rock and settle. reel.py then adds the micro push, grade, letterbox."""
import sys; sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import *
FPS, N = 24, 72
S = W / 1672
plate = cv2.resize(rd(K / "k05.png")[..., :3], (W, H), interpolation=cv2.INTER_CUBIC).astype(np.float32) / 255
cap = rd(K / "k05_capsule.png").astype(np.float32) / 255
ys, xs = np.nonzero(cap[..., 3] > 0.03)
cap = cap[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
cap[..., :3] *= cap[..., 3:4]                                        # premultiply
REST_LEN = 520 * S                                                   # capsule length at rest (frame px)
k_rest = REST_LEN / cap.shape[1]
MOUTH = np.array([835 * S, 385 * S]); REST = np.array([836 * S, 566 * S])
# cradle occluder: the cup's front wall and its two side lugs (the capsule settles into the saddle between them)
k5 = rd(K / "k05.png")[..., :3].astype(np.int32); b_, g_, r_ = k5[..., 0], k5[..., 1], k5[..., 2]
yy, xx = np.mgrid[0:k5.shape[0], 0:k5.shape[1]]
yf = 610 - 22 * ((xx - 832) / 137.0) ** 2
occ = (((r_ > 70) & (r_ > b_ + 10)) | ((b_ > 140) & (g_ > 110))) & (xx > 645) & (xx < 1030) & (yy > 556) & (yy < 760)
occ &= (yy > yf) | (xx < 700) | (xx > 962)
occ = cv2.morphologyEx(occ.astype(np.uint8), cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
occ = cv2.GaussianBlur(cv2.resize(occ.astype(np.float32), (W, H)), (0, 0), 1.0)[..., None]
T0, T1 = 1.20, 1.35


def ease_in(u): return u * u


def state(t):
    if t < T0: return None
    if t < T1:
        u = ease_in((t - T0) / (T1 - T0))
        return MOUTH + (REST - MOUTH) * u, 0.6 + 0.4 * u, 75 * (1 - u) - 3 * u
    d = t - T1
    rock = 1.5 * np.sin(2 * np.pi * d / 0.3) * np.exp(-d / 0.25) if d < 1.2 else 0
    return REST, 1.0, -3 + rock


def draw_cap(img_acc, a_acc, st, wgt):
    (cx, cy), sc, ang = st
    k = k_rest * sc
    M = cv2.getRotationMatrix2D((cap.shape[1] / 2, cap.shape[0] / 2), ang, k)
    M[0, 2] += cx - cap.shape[1] / 2; M[1, 2] += cy - cap.shape[0] / 2
    c = cv2.warpAffine(cap, M, (W, H), flags=cv2.INTER_AREA if k < 0.7 else cv2.INTER_LINEAR)
    img_acc += c[..., :3] * wgt; a_acc += c[..., 3:4] * wgt


rng = np.random.default_rng(10)
NP = 30
pu_x = np.concatenate([rng.normal(675 * S, 12, NP // 2), rng.normal(1000 * S, 12, NP - NP // 2)])
pu_y = rng.normal(565 * S, 5, NP)
pu_vx = rng.normal(0, 60, NP) + np.where(pu_x < 960, -40, 40)
pu_vy = rng.uniform(-90, -20, NP); pu_r = rng.uniform(2, 6, NP)
GL = np.array([968 * S, 355 * S])
Y, X = np.mgrid[0:H, 0:W].astype(np.float32)

out = Pipe(C / "10_base.mp4")
for i in range(N):
    t = i / FPS
    f = plate.copy()
    acc = np.zeros((H, W, 3), np.float32); aa = np.zeros((H, W, 1), np.float32)
    subs = [t + (j - 2) / FPS / 5 for j in range(5)] if T0 <= t < T1 + 1 / FPS else [t]
    for ts in subs:
        st = state(ts)
        if st is not None: draw_cap(acc, aa, st, 1 / len(subs))
    f0 = f.copy()
    f = acc + f * (1 - aa)
    if t >= T0 + 0.08: f = f * (1 - occ) + f0 * occ
    if t >= T1:                                                       # dust puff
        d = t - T1
        if d < 1.0:
            lay = np.zeros((H, W), np.float32)
            for x, y, vx, vy, r in zip(pu_x, pu_y, pu_vx, pu_vy, pu_r):
                px = x + vx * d * np.exp(-d); py = y + vy * d * np.exp(-d * 1.5) + 12 * d * d
                cv2.circle(lay, (int(px * 16), int(py * 16)), int(16 * r * (1 + 2 * d)), 1.0, -1, cv2.LINE_AA, shift=4)
            lay = cv2.GaussianBlur(lay, (0, 0), 3) * 0.35 * (1 - d) ** 1.5
            f = f + lay[..., None] * np.array([0.75, 0.8, 0.85], np.float32)
    if t >= 1.40:                                                     # brass glint on the pipe rim
        d = t - 1.40
        gl = np.exp(-((X - GL[0]) ** 2 + (Y - GL[1]) ** 2) / (2 * 14 ** 2))
        streak = np.exp(-((Y - GL[1]) ** 2) / (2 * 2.5 ** 2) - ((X - GL[0]) ** 2) / (2 * 90 ** 2))
        f = f + (gl * 0.9 + streak * 0.5)[..., None] * np.exp(-d / 0.18) * np.array([0.55, 0.85, 1.0], np.float32)
    if t >= T1:                                                       # impact shake
        d = t - T1; amp = 6 * np.exp(-d / 0.12) if d < 0.4 else 0
        if amp > 0.2:
            M = np.float32([[1, 0, amp * smooth_noise(31, t, 9)], [0, 1, amp * smooth_noise(32, t, 11)]])
            f = cv2.warpAffine(f, M, (W, H), borderMode=cv2.BORDER_REPLICATE)
    out.put(f * 255)
out.close()
