"""Rooms, loudspeakers and voice chains for the v4 mix (audio/pilot/mix_plan.md §3-§4), in numpy.

Every filter here is zero-phase and applied in the FFT domain (magnitude responses of Butterworth / RBJ sections), so
nothing needs scipy. A room is (a) an optional transfer function or chain before it ("pre"), (b) an early part (the
direct sound and early reflections, each tap with its own delay, gain, pan and filter) and (c) a diffuse tail
(two decorrelated noise channels, split into octave bands 63 Hz-8 kHz, each decaying at its own RT60, faded in from
sparse to dense, energy-normalised). The tail's level is the room's `wet` (dB re the direct sound), overridable per
placement. IRs are cached in work/pilot/audio/ir/<ROOM>.npz (git-ignored).

    from rooms import apply_room, chain
    y = apply_room(x, "HALL_FAR")               # mono or (n, 2) in, (n + tail, 2) out
    y = apply_room(x, "DESK", wet=-16)           # objects sit wetter in the Hall than voices
"""
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
SR = 48000
IR_DIR = ROOT / "work" / "pilot" / "audio" / "ir"
IR_VERSION = 3  # bump to invalidate cached IRs


def db(g):
    return 10 ** (g / 20)


def mono(x):
    return x.mean(1) if x.ndim == 2 else x


def as_st(x):
    return np.stack([x, x], 1) if x.ndim == 1 else x


def pan_gains(p):
    """Equal-power pan, unity at centre."""
    p = float(np.clip(p, -1, 1))
    return np.sqrt((1 - p) / 2) * np.sqrt(2), np.sqrt((1 + p) / 2) * np.sqrt(2)


def pan(x, p):
    gl, gr = pan_gains(p)
    m = mono(x)
    return np.stack([m * gl, m * gr], 1)


def width(x, w):
    """Mid/side width: 1 = as is, 0 = mono."""
    x = as_st(x)
    m, s = (x[:, 0] + x[:, 1]) / 2, (x[:, 0] - x[:, 1]) / 2
    return np.stack([m + w * s, m - w * s], 1)


# ------------------------------------------------------------------ magnitude responses (f in Hz)
def _biquad_mag(f, b, a):
    w = 2 * np.pi * f / SR
    z1, z2 = np.exp(-1j * w), np.exp(-2j * w)
    return np.abs((b[0] + b[1] * z1 + b[2] * z2) / (a[0] + a[1] * z1 + a[2] * z2))


def _rbj(kind, f0, g, q=0.707):
    A = 10 ** (g / 40)
    w0 = 2 * np.pi * f0 / SR
    c, s = np.cos(w0), np.sin(w0)
    if kind == "peak":
        al = s / (2 * q)
        return [1 + al * A, -2 * c, 1 - al * A], [1 + al / A, -2 * c, 1 - al / A]
    al = s / 2 * np.sqrt(2)  # shelf slope S = 1
    sa = 2 * np.sqrt(A) * al
    if kind == "lshelf":
        return ([A * ((A + 1) - (A - 1) * c + sa), 2 * A * ((A - 1) - (A + 1) * c), A * ((A + 1) - (A - 1) * c - sa)],
                [(A + 1) + (A - 1) * c + sa, -2 * ((A - 1) + (A + 1) * c), (A + 1) + (A - 1) * c - sa])
    return ([A * ((A + 1) + (A - 1) * c + sa), -2 * A * ((A - 1) + (A + 1) * c), A * ((A + 1) + (A - 1) * c - sa)],
            [(A + 1) - (A - 1) * c + sa, 2 * ((A - 1) - (A + 1) * c), (A + 1) - (A - 1) * c - sa])


def response(f, ops):
    """Magnitude of a chain of filter ops: ["hp", fc, order], ["lp", fc, order], ["bp", lo, hi, order],
    ["peak", f0, dB, Q], ["lshelf", f0, dB], ["hshelf", f0, dB], ["gain", dB]."""
    m = np.ones_like(f)
    fs = np.maximum(f, 1e-3)
    for op in ops:
        k = op[0]
        if k == "lp":
            m = m / np.sqrt(1 + (fs / op[1]) ** (2 * (op[2] if len(op) > 2 else 2)))
        elif k == "hp":
            m = m / np.sqrt(1 + (op[1] / fs) ** (2 * (op[2] if len(op) > 2 else 2)))
        elif k == "bp":
            n = op[3] if len(op) > 3 else 2
            m = m / np.sqrt(1 + (op[1] / fs) ** (2 * n)) / np.sqrt(1 + (fs / op[2]) ** (2 * n))
        elif k in ("peak", "lshelf", "hshelf"):
            b, a = _rbj(k, op[1], op[2], op[3] if len(op) > 3 else 0.707)
            m = m * _biquad_mag(np.minimum(f, SR / 2 - 1), b, a)
        elif k == "gain":
            m = m * db(op[1])
        elif k == "dehum":  # narrow notches on the mains series (the generator's 50 Hz-comb artifact): -30 dB, +-1.5 Hz
            base, top = op[1], op[2]
            for h in np.arange(base, top + 1, base):
                m = m * (1 - 0.968 * np.exp(-((f - h) / 1.5) ** 2))
        elif k == "kw":  # BS.1770 K-weighting (48 kHz coefficients)
            m = m * _biquad_mag(f, [1.53512485958697, -2.69169618940638, 1.19839281085285],
                                [1, -1.69065929318241, 0.73248077421585])
            m = m * _biquad_mag(f, [1.0, -2.0, 1.0], [1, -1.99004745483398, 0.99007225036621])
        else:
            raise ValueError(op)
    return m


def filt(x, ops, pad=None):
    """Zero-phase FFT filter; mono or (n, c)."""
    if not ops or len(x) == 0:
        return x
    pad = int(0.25 * SR) if pad is None else pad
    n = len(x)
    L = n + pad
    X = np.fft.rfft(x, L, axis=0)
    m = response(np.fft.rfftfreq(L, 1 / SR), ops)
    y = np.fft.irfft(X * (m[:, None] if x.ndim == 2 else m), L, axis=0)
    return y[:n]


def lp_sweep(x, t, keys):
    """Time-varying low-pass: keys [[t, Hz], ...] against sample times t; bank of static filters, log-interpolated."""
    hz = np.interp(t, [k[0] for k in keys], [k[1] for k in keys])
    lo, hi = min(k[1] for k in keys), max(k[1] for k in keys)
    if hi / lo < 1.05:
        return filt(x, [["lp", lo, 2]])
    cs = np.geomspace(lo, hi, 7)
    pos = np.interp(np.log(hz), np.log(cs), np.arange(len(cs)))
    out = np.zeros_like(x)
    for i, c in enumerate(cs):
        w = np.clip(1 - np.abs(pos - i), 0, 1)
        if w.max() > 0:
            out += filt(x, [["lp", c, 2]]) * (w[:, None] if x.ndim == 2 else w)
    return out


# ------------------------------------------------------------------ resampling
def resample_ratio(x, r):
    """Play x at r times the speed (pitch up by r), FFT resampling: the output has len(x) / r samples."""
    if abs(r - 1) < 1e-6:
        return x.copy()
    n = len(x)
    m = max(1, int(round(n / r)))
    X = np.fft.rfft(x, axis=0)
    k = m // 2 + 1
    if k <= X.shape[0]:
        Y = X[:k]
    else:
        Y = np.zeros((k,) + X.shape[1:], complex)
        Y[:X.shape[0]] = X
    return np.fft.irfft(Y, m, axis=0) * (m / n)


def warp(x, pos):
    idx = np.arange(len(x))
    if x.ndim == 1:
        return np.interp(pos, idx, x, right=0.0)
    return np.stack([np.interp(pos, idx, x[:, c], right=0.0) for c in range(x.shape[1])], 1)


def vary_rate(x, cents):
    """Time-varying pitch by resampling: cents[i] is the deviation at output sample i (array, len = output)."""
    r = 2 ** (np.asarray(cents) / 1200)
    pos = np.concatenate([[0], np.cumsum(r)[:-1]])
    return warp(x, pos)


def wow_flutter(x, wow_hz, wow_c, fl_hz, fl_c, seed=0):
    rng = np.random.default_rng(seed)
    t = np.arange(len(x)) / SR
    c = wow_c * np.sin(2 * np.pi * wow_hz * t + rng.uniform(0, 6.3)) + fl_c * np.sin(2 * np.pi * fl_hz * t + rng.uniform(0, 6.3))
    return vary_rate(x, c)


def softclip(x, drive=1.8):
    return np.tanh(drive * x) / np.tanh(drive)


def lpnoise(n, fc, seed):
    rng = np.random.default_rng(seed)
    v = filt(rng.normal(0, 1, n), [["lp", fc, 2]])
    return v / (np.std(v) + 1e-12)


# ------------------------------------------------------------------ IR builder
BANDS = np.array([63, 125, 250, 500, 1000, 2000, 4000, 8000.0])


def _band_weights(f):
    """Smooth octave-band partition of unity over f (log-f triangular)."""
    lf = np.log2(np.maximum(f, 1))
    lb = np.log2(BANDS)
    w = np.zeros((len(BANDS), len(f)))
    for i in range(len(BANDS)):
        w[i] = np.clip(1 - np.abs(lf - lb[i]), 0, 1)
    w[0][lf < lb[0]] = 1
    w[-1][lf > lb[-1]] = 1
    return w / (w.sum(0) + 1e-12)


def diffuse_tail(rt60, length, density=(0.0, 0.0), predelay=0.0, seed=1, stereo=True, lp=None):
    """rt60: dict {band_hz: seconds} (log-interpolated onto the 8 octave bands) or one number.
    density (t0, t1): sparse at t0 -> dense by t1. Energy-normalised per channel."""
    if isinstance(rt60, (int, float)):
        rts = np.full(len(BANDS), float(rt60))
    else:
        ks = sorted(rt60)
        rts = np.interp(np.log2(BANDS), np.log2(ks), [rt60[k] for k in ks])
    n = int(length * SR)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    chans = []
    for c in range(2 if stereo else 1):
        z = rng.normal(0, 1, n)
        t0, t1 = density
        if t1 > t0:
            p = np.clip((t - t0) / (t1 - t0), 0, 1) ** 2 * 0.98 + 0.02
            keep = rng.random(n) < p
            z = np.where(keep, z / np.sqrt(p), 0.0)
            z[t < t0] = 0
        Z = np.fft.rfft(z)
        f = np.fft.rfftfreq(n, 1 / SR)
        W = _band_weights(f)
        y = np.zeros(n)
        for i, rt in enumerate(rts):
            y += np.fft.irfft(Z * W[i], n) * np.exp(-6.91 * t / rt)
        if lp:
            y = filt(y, [["lp", lp, 1]])
        y = y / np.sqrt((y ** 2).sum() + 1e-20)
        chans.append(np.concatenate([np.zeros(int(predelay * SR)), y]))
    return np.stack(chans, 1) if stereo else np.stack([chans[0], chans[0]], 1)


def _kernel(ops, n=1024):
    """A filtered unit impulse (zero-phase, centred at n // 2)."""
    d = np.zeros(n)
    d[n // 2] = 1
    return filt(d, ops, pad=0) if ops else d


def taps(spec, length=None):
    """spec: [(delay_s, gain_db, pan, [filter ops]), ...] -> stereo early IR (direct included if listed)."""
    L = int((length or (max(s[0] for s in spec) + 0.05)) * SR) + 1024
    ir = np.zeros((L, 2))
    for d, g, p, ops in spec:
        k = _kernel(ops)
        s = int(round(d * SR)) - 512
        gl, gr = pan_gains(p)
        for c, gc in enumerate((gl, gr)):
            a = max(0, s)
            ir[a:a + len(k) - (a - s), c] += k[a - s:] * db(g) * gc
    return ir


def _cached(name, build):
    IR_DIR.mkdir(parents=True, exist_ok=True)
    p = IR_DIR / f"{name}.npz"
    if p.exists():
        z = np.load(p)
        if int(z["v"]) == IR_VERSION:
            return z["early"], z["tail"]
    early, tail = build()
    np.savez(p, early=early, tail=tail, v=IR_VERSION)
    return early, tail


# The rooms: (early taps, tail, default wet in dB re direct). Taps: (delay, dB, pan, filter ops).
HALL_RT = {63: 7.5, 125: 7.0, 250: 6.5, 500: 6.0, 1000: 5.5, 2000: 4.5, 4000: 3.2, 8000: 2.0}
HALL_TAPS = [(0.005, -6, 0, [["lp", 6000, 1]]), (0.045, -14, -0.7, [["lp", 5000, 1]]), (0.052, -14, 0.7, [["lp", 5000, 1]]),
             (0.175, -16, 0.1, [["lp", 3500, 1]]), (0.230, -12, 0.0, [["hp", 900, 1], ["hshelf", 4000, 3]]),
             (0.470, -20, 0.0, [["lp", 1200, 2]])]


def hall_wet():
    """The basilica's reverberant field (taps + tail) as one energy-normalised stereo IR, pre-delay removed."""
    def build():
        er = taps(HALL_TAPS, 0.5)
        tail = diffuse_tail(HALL_RT, 8.0, density=(0.08, 0.25), seed=11)
        n = max(len(er), len(tail))
        ir = np.zeros((n, 2))
        ir[:len(er)] += er
        ir[:len(tail)] += tail * db(-3)
        return np.zeros((1, 2)), ir / np.sqrt((ir ** 2).sum(0).mean())
    return _cached("HALL", build)[1]


def _join(*parts):
    n = max(len(p) for p in parts)
    out = np.zeros((n, 2))
    for p in parts:
        out[:len(p)] += p
    return out


def _delay(ir, s):
    return np.concatenate([np.zeros((int(s * SR), 2)), ir])


def horn_array():
    """HALL_HORNS: 30 horns, one each side of 15 piers from 80 m behind Desk 4 to 40 m in front, 9 m aside, 6 m up.
    Arrival d/343 (minus the nearest horn's, so the first horn is on time), gain 20 log10(d_min/d), pan +-0.5
    narrowing with distance; horns behind face away (-6 dB, low-pass 1.8 kHz)."""
    spec = []
    ys = np.linspace(-80, 40, 15)
    ds = [np.sqrt(y * y + 81 + 36) for y in ys]
    dmin = min(ds)
    for y, d in zip(ys, ds):
        for side in (-1, 1):
            g = 20 * np.log10(dmin / d)
            ops = [["lp", 12000, 1]]
            if y < 0:
                g -= 6
                ops = [["lp", 1800, 2]]
            spec.append(((d - dmin) / 343, g, side * 0.5 * dmin / d, ops))
    return taps(spec, 0.45)


HORN_PRE = [["hp", 350, 3], ["lp", 5000, 3], ["peak", 1100, 6, 2.0], ["peak", 2800, 3, 1.2]]
TV_PRE = [["hp", 180, 2], ["lp", 5500, 3], ["peak", 400, 5, 1.2], ["peak", 2500, 3, 1.0]]
MONITOR_PRE = [["hp", 160, 2], ["lp", 7000, 2], ["peak", 600, 4, 1.5]]
PHONE_BAND = [["hp", 280, 3], ["lp", 3600, 3], ["peak", 1800, 3, 1.0]]
FLAT_RT = {125: 0.5, 500: 0.38, 2000: 0.3, 8000: 0.2}
FLAT_TAPS = [(0.0, 0, 0, []), (0.007, -5, 0.0, [["lp", 5000, 1]]), (0.011, -9, -0.5, [["lp", 4000, 1]]),
             (0.013, -10, 0.5, [["hp", 800, 1]]), (0.017, -12, 0.2, [["lp", 3000, 1]])]
STREET_FACADE = [(0.064, -9, -0.6, [["lp", 5000, 1]]), (0.071, -9, 0.6, [["lp", 5000, 1]])]


def _room_def(name):
    """-> (early IR, tail IR (unit energy), default wet dB)."""
    if name == "HALL":
        return np.array([[1.0, 1.0]]), hall_wet(), -6
    if name in ("DESK", "DESK_GLASS"):
        def b():
            spec = [(0.0, 0, 0, []), (0.002, -8, 0, [["lp", 6000, 1]])]
            if name == "DESK_GLASS":
                spec.append((0.0012, -9, 0.1, [["hp", 800, 2]]))
            return taps(spec, 0.01), _delay(hall_wet(), 0.020)
        e, t = _cached(name, b)
        return e, t, -24
    if name == "HALL_FAR":
        def b():
            e = taps([(0.0, -12, 0, [["lp", 6000, 2]]), (0.060, -8 - 12, 0.0, [["lp", 3000, 1]]),
                      (0.090, -6 - 12, 0.1, [["hp", 900, 1], ["hshelf", 4000, 3]])], 0.1)
            return e, _delay(hall_wet(), 0.030)
        e, t = _cached(name, b)
        return e, t, -12 - 4 + 0  # tail at -4 dB re the (-12 dB) direct
    if name == "HALL_FLOOR":
        def b():
            short = diffuse_tail(0.8, 1.2, density=(0.0, 0.03), seed=21, lp=2000)
            return np.array([[1.0, 1.0]]), _join(short * db(-10) / db(-18), hall_wet())
        e, t = _cached(name, b)
        return e, t, -18
    if name == "ATTENTION":
        def b():
            return taps([(0.0, -8, 0, [["lp", 2500, 2]])], 0.01), _delay(hall_wet(), 0.020)
        e, t = _cached(name, b)
        return e, t, -8 - 6
    if name == "HALL_HORNS":
        def b():
            return horn_array(), hall_wet()
        e, t = _cached(name, b)
        return e, t, -3
    if name == "BCAST":
        def b():
            return np.array([[1.0, 1.0]]), diffuse_tail(0.7, 0.9, seed=31, stereo=False)
        e, t = _cached(name, b)
        return e, t, -26
    if name == "FLAT":
        def b():
            return taps(FLAT_TAPS, 0.03), _delay(diffuse_tail(FLAT_RT, 1.0, density=(0.01, 0.04), seed=41), 0.004)
        e, t = _cached(name, b)
        return e, t, -18
    if name in ("STREET_PR", "STREET"):
        def b():
            if name == "STREET_PR":
                spec = [(0.0, -6, 0, [])] + STREET_FACADE
                g, lp = -4, 4500.0
                for i in range(1, 6):  # flutter between the facades
                    spec.append((0.064 * (i + 1), -9 + g * i, 0.3 * (-1) ** i, [["lp", lp, 1]]))
                    lp *= 0.75
                spec.append((0.350, -8, 0.0, [["lp", 3000, 1]]))  # the slap off the buildings behind the crowd
                return taps(spec, 0.4), diffuse_tail(2.2, 2.6, density=(0.06, 0.2), predelay=0.02, seed=51)
            return taps([(0.0, 0, 0, [])] + STREET_FACADE, 0.1), diffuse_tail(1.4, 1.8, density=(0.05, 0.15), seed=52)
        e, t = _cached(name, b)
        return e, t, (-8 if name == "STREET_PR" else -14)
    if name == "CANAL":
        def b():
            return (taps([(0.0, 0, 0, [["lp", 3500, 1]]), (0.008, -4, 0.0, [["lp", 2500, 1]])], 0.02),
                    diffuse_tail(2.5, 3.0, density=(0.02, 0.12), seed=61, lp=3500))
        e, t = _cached(name, b)
        return e, t, -10
    if name == "DAWN":
        def b():
            return (taps([(0.0, 0, 0, []), (0.004, -6, -0.3, [["lp", 6000, 1]]), (0.009, -9, 0.3, [["lp", 5000, 1]])], 0.02),
                    diffuse_tail(0.35, 0.6, density=(0.01, 0.05), seed=71))
        e, t = _cached(name, b)
        return e, t, -20
    if name == "AIR":
        def b():
            return (taps([(0.0, 0, 0, []), (0.009, -7, -0.4, [["lp", 7000, 1]]), (0.014, -9, 0.4, [["lp", 6000, 1]]),
                          (0.021, -11, 0.0, [["lp", 5000, 1]])], 0.03),
                    diffuse_tail(1.2, 1.6, density=(0.015, 0.06), predelay=0.01, seed=81))
        e, t = _cached(name, b)
        return e, t, -10
    if name == "WINDOW_SMALL":
        def b():
            return np.array([[1.0, 1.0]]), diffuse_tail(0.4, 0.6, density=(0.005, 0.03), seed=91)
        e, t = _cached(name, b)
        return e, t, -12
    if name == "CITY_DIFFUSE":
        def b():
            return np.array([[1.0, 1.0]]), diffuse_tail(4.0, 4.5, density=(0.05, 0.3), seed=101, lp=3000)
        e, t = _cached(name, b)
        return e, t, -6
    if name in ("DRY", "HALL_BED", "OPTICAL", "OPTICAL_COLD", "PHONE_EAR"):
        return np.array([[1.0, 1.0]]), None, None
    raise ValueError(f"unknown room {name}")


def conv(x, ir):
    """x mono or stereo, ir stereo -> stereo, full length."""
    x = as_st(x)
    n = len(x) + len(ir) - 1
    L = 1 << (n - 1).bit_length()
    X = np.fft.rfft(x, L, axis=0)
    H = np.fft.rfft(ir, L, axis=0)
    return np.fft.irfft(X * H, L, axis=0)[:n]


def convolve_room(x, name, wet=None):
    early, tail, w0 = _room_def(name)
    y = conv(x, early) if len(early) > 1 else as_st(x) * early[0]
    if tail is not None:
        w = w0 if wet is None else wet
        z = conv(x, tail) * db(w)  # the tail is unit-energy, so wet is dB re the direct sound
        n = max(len(y), len(z))
        out = np.zeros((n, 2))
        out[:len(y)] += y
        out[:len(z)] += z
        y = out
    return y


# ------------------------------------------------------------------ rooms that are processes
def optical(x, cold=False, seed=0):
    x = mono(x)
    x = filt(x, [["hp", 90, 2], ["lp", 3000 if cold else 7500, 2]])
    x = wow_flutter(x, 0.6, 5, 9, 1 if cold else 2, seed=seed)
    pk = np.abs(x).max() + 1e-12
    u = x / pk
    x = (u + 0.016 * (u * u - np.mean(u * u))) * pk  # 0.8 % second harmonic
    if cold:
        t = np.arange(len(x)) / SR
        x = x * np.clip(1 - t / 1.2, 0, 1) ** 1.5
    return as_st(x)


def tape_stage(x, seed=0, hiss_db=-56):
    """Year One's message repeater: band 250 Hz-6 kHz, tanh drive 1.4, wow 0.45 Hz +-8 c, a capstan start
    (-40 c rising to 0 over 60 ms), hiss under the phrase only."""
    x = mono(x)
    x = filt(x, [["hp", 250, 2], ["lp", 6000, 2]])
    pk = np.abs(x).max() + 1e-12
    x = np.tanh(1.4 * x / pk) / np.tanh(1.4) * pk
    t = np.arange(len(x)) / SR
    c = 8 * np.sin(2 * np.pi * 0.45 * t + np.random.default_rng(seed).uniform(0, 6.3)) - 40 * np.clip(1 - t / 0.06, 0, 1)
    x = vary_rate(x, c)
    envl = filt(np.abs(x), [["lp", 8, 1]])
    envl = np.clip(envl / (envl.max() + 1e-12) * 4, 0, 1)
    hiss = filt(np.random.default_rng(seed + 7).normal(0, 1, len(x)), [["hp", 1500, 1]])
    x = x + hiss / np.std(hiss) * db(hiss_db) * pk * envl
    return x


def horns_pre(x):
    x = filt(mono(x), HORN_PRE)
    pk = np.abs(x).max() + 1e-12
    return softclip(x / pk, 1.8) * pk


def tv_pre(x):
    x = filt(mono(x), TV_PRE)
    pk = np.abs(x).max() + 1e-12
    u = x / pk
    return np.tanh(u + 0.08 * u * u) * pk


def monitor_pre(x):
    x = filt(mono(x), MONITOR_PRE)
    pk = np.abs(x).max() + 1e-12
    return softclip(x / pk, 1.2) * pk


def phone_ear(x, seed=0):
    """Nana's carbon microphone and the line, as Ida hears it (mono, centre, no room on our side)."""
    x = mono(x)
    pk = np.abs(x).max() + 1e-12
    u = x / pk
    u = u + 0.005 * (4 * u ** 3 - 3 * u)  # 0.5 % third harmonic
    u = u * (1 + 0.03 * lpnoise(len(u), 200, seed))  # carbon grain
    return as_st(filt(u, PHONE_BAND) * pk)


def line_spill(x, wet=-20):
    y = filt(mono(x), PHONE_BAND + [["peak", 3000, 2, 1.0], ["gain", -26]])
    return convolve_room(y, "DESK", wet)


def city_sets(x, seed=5):
    """The Chime through a thousand televisions: forty TV copies smeared 0-350 ms, 0 to -14 dB, pans +-0.9,
    low-passed 1.8-4 kHz by distance, then CANAL and a 4 s diffuse at -6 dB. A smear, not an echo."""
    rng = np.random.default_rng(seed)
    v = tv_pre(x)
    n = len(v) + int(0.4 * SR)
    out = np.zeros((n, 2))
    for i in range(40):
        d = rng.uniform(0, 0.35)
        g = rng.uniform(-14, 0)
        fc = 4000 - (4000 - 1800) * (d / 0.35) * rng.uniform(0.6, 1.0)
        c = filt(v, [["lp", fc, 2]]) * db(g)
        s = int(d * SR)
        gl, gr = pan_gains(rng.uniform(-0.9, 0.9))
        out[s:s + len(c), 0] += c * gl
        out[s:s + len(c), 1] += c * gr
    out /= np.sqrt(40)
    y = convolve_room(out, "CANAL")
    return convolve_room(y, "CITY_DIFFUSE")


def window_room(x, dist_db, pan_pos, lpf=1800, phone=False, seed=0):
    """A walla voice in a small room, out of a window, across the canal."""
    x = mono(x)
    if phone:
        x = mono(phone_ear(x, seed))
    y = convolve_room(x, "WINDOW_SMALL")
    y = filt(y, [["hp", 200, 2], ["lp", lpf, 3], ["gain", dist_db]])
    y = pan(y, pan_pos)
    early, tail, _ = _room_def("CANAL")
    z = conv(mono(y), tail) * db(-14)
    out = np.zeros((max(len(y), len(z)), 2))
    out[:len(y)] += y
    out[:len(z)] += z
    return out


# ------------------------------------------------------------------ the room table (§3)
def apply_room(x, name, wet=None, kind="object", seed=0):
    """Put a dry sound (mono or stereo) in a room from mix_plan.md §3. Returns stereo, longer by the room's tail."""
    if name in (None, "DRY", "HALL_BED"):
        return as_st(x)
    if name == "OPTICAL":
        return optical(x, seed=seed)
    if name == "OPTICAL_COLD":
        return optical(x, cold=True, seed=seed)
    if name == "BCAST":
        y = filt(mono(x), [["hp", 60, 2], ["lp", 12000, 1]])
        return convolve_room(y, "BCAST", wet)
    if name == "DESK":
        return convolve_room(x, "DESK", wet if wet is not None else (-24 if kind == "voice" else -16))
    if name == "DESK_GLASS":
        return convolve_room(x, "DESK_GLASS", wet if wet is not None else -24)
    if name == "HALL_FLOOR":
        y = filt(x, [["lp", 2000, 2]])
        y = width(convolve_room(y, "HALL_FLOOR", wet), 0.3)
        return y
    if name == "MONITOR":
        return convolve_room(monitor_pre(x), "DESK", -24)
    if name == "HALL_HORNS":
        return convolve_room(horns_pre(x), "HALL_HORNS", wet)
    if name == "HALL_PA":
        return convolve_room(horns_pre(tape_stage(x, seed)), "HALL_HORNS", wet)
    if name == "HALL_PA_NOTAPE":
        return convolve_room(horns_pre(x), "HALL_HORNS", wet)
    if name == "TV":
        return convolve_room(tv_pre(x), "FLAT", wet if wet is not None else -12)  # 1.2 m from the set
    if name == "FLAT":
        return convolve_room(x, "FLAT", wet if wet is not None else (-18 if kind == "voice" else -10))
    if name == "PHONE_EAR":
        return phone_ear(x, seed)
    if name == "LINE_SPILL":
        return line_spill(x, wet if wet is not None else -20)
    if name == "STREET_PR":
        y = filt(mono(x), [["hp", 150, 3], ["lp", 6000, 3], ["peak", 1500, 3, 1.0]])
        return convolve_room(y, "STREET_PR", wet)
    if name in ("STREET", "CANAL", "DAWN", "AIR", "HALL_FAR", "ATTENTION", "HALL"):
        return convolve_room(x, name, wet)
    if name == "CITY_SETS":
        return city_sets(x, seed)
    raise ValueError(f"unknown room {name}")


# ------------------------------------------------------------------ voice chains (§4)
def _frames(x, hop=0.01):
    k = int(hop * SR)
    n = len(x) // k
    return x[:n * k].reshape(n, k), k


def engraving(x):
    """The Father: breaths removed, gaps to digital zero, level ridden to -20 dBFS (300 ms RMS, +-1 dB), EQ, mono."""
    x = mono(x).astype(float)
    fr, k = _frames(x)
    rms = np.sqrt((fr ** 2).mean(1)) + 1e-12
    ldb = 20 * np.log10(rms)
    top = np.percentile(ldb, 95)
    active = ldb > top - 32
    lo = filt(x, [["lp", 1500, 2]])
    lfr, _ = _frames(lo)
    ratio = (lfr ** 2).mean(1) / (rms ** 2)
    voiced = active & (ratio > 0.35)
    # breaths: active unvoiced runs more than 80 ms from any voiced frame
    vi = np.nonzero(voiced)[0]
    keep = np.zeros(len(active), bool)
    for i in np.nonzero(active)[0]:
        if voiced[i] or (len(vi) and np.min(np.abs(vi - i)) <= 8):
            keep[i] = True
    # close small holes (< 60 ms) inside words, then 10 ms fades
    g = keep.astype(float)
    for i in range(1, len(g) - 1):
        if not keep[i]:
            a = np.nonzero(keep[max(0, i - 6):i])[0]
            b = np.nonzero(keep[i + 1:i + 7])[0]
            if len(a) and len(b):
                g[i] = 1
    gs = np.repeat(g, k)
    gs = np.concatenate([gs, np.zeros(len(x) - len(gs))])
    m = int(0.01 * SR)
    gs = np.convolve(gs, np.ones(m) / m, "same")
    x = x * gs
    # ride: 300 ms RMS to -20 dBFS within +-1 dB (50 ms attack, 400 ms release)
    w = int(0.3 * SR)
    ms = np.convolve(x * x, np.ones(w) / w, "same")
    lv = 10 * np.log10(ms + 1e-14)
    act = gs > 0.5
    want = np.where(act & (lv > -60), -20 - lv, np.nan)
    idx = np.arange(len(x))
    ok = ~np.isnan(want)
    if ok.any():
        want = np.interp(idx, idx[ok], want[ok])
    else:
        want = np.zeros(len(x))
    want = np.clip(want, -18, 18)
    step = 48
    ws = want[::step]
    out = np.zeros(len(ws))
    y = ws[0]
    ca, cr = 1 - np.exp(-step / (0.05 * SR)), 1 - np.exp(-step / (0.4 * SR))
    for i, v in enumerate(ws):
        y += (v - y) * (ca if v < y else cr)
        out[i] = y
    gdb = np.interp(idx, idx[::step], out)
    x = x * db(gdb)
    x = filt(x, [["lshelf", 150, 1.5], ["peak", 3500, 1.5, 1.0], ["hshelf", 7000, -2]])
    x[gs < 1e-4] = 0.0  # the gaps are digital zero: the carrier is his only floor
    return x


def de_ess(x, f0=6500, cut=-3):
    fr, k = _frames(x, 0.005)
    hi = filt(x, [["hp", 5000, 2]])
    hfr, _ = _frames(hi, 0.005)
    r = (hfr ** 2).mean(1) / ((fr ** 2).mean(1) + 1e-14)
    msk = np.repeat((r > 0.5).astype(float), k)
    msk = np.concatenate([msk, np.zeros(len(x) - len(msk))])
    m = int(0.01 * SR)
    msk = np.convolve(msk, np.ones(m) / m, "same")
    y = filt(x, [["peak", f0, cut, 2.0]])
    return x * (1 - msk) + y * msk


def ida_chain(x):
    x = filt(mono(x), [["hp", 70, 2], ["peak", 180, 2, 1.0]])
    return de_ess(x)


def nana_chain(x):
    return filt(mono(x), [["hp", 60, 2], ["peak", 250, 1.5, 1.0], ["hshelf", 5000, -1]])


CHAINS = {"father": engraving, "ida": ida_chain, "nana": nana_chain, "none": lambda x: mono(x)}


# ------------------------------------------------------------------ loudness (BS.1770, numpy)
def kweight(x):
    return filt(as_st(x), [["kw"]], pad=int(0.5 * SR))


def st_curve(x, win=3.0, hop=0.1):
    """Short-term (win=3.0) or momentary (0.4) loudness every `hop` s, window centred; LUFS."""
    k = kweight(x)
    e = (k ** 2).sum(1)
    h = int(hop * SR)
    n = len(e) // h
    blk = e[:n * h].reshape(n, h).mean(1)
    m = max(1, int(round(win / hop)))
    c = np.convolve(blk, np.ones(m) / m, "same")
    return -0.691 + 10 * np.log10(c + 1e-20)


def integrated(x):
    k = kweight(x)
    e = (k ** 2).sum(1)
    h = int(0.1 * SR)
    n = len(e) // h
    blk = e[:n * h].reshape(n, h).mean(1)
    if n < 4:
        return -0.691 + 10 * np.log10(blk.mean() + 1e-20)
    g = np.convolve(blk, np.ones(4) / 4, "valid")
    L = -0.691 + 10 * np.log10(g + 1e-20)
    g1 = g[L > -70]
    if not len(g1):
        return -120.0
    rel = -0.691 + 10 * np.log10(g1.mean()) - 10
    g2 = g1[(-0.691 + 10 * np.log10(g1)) > rel]
    return -0.691 + 10 * np.log10(g2.mean())


def span_loudness(x, a=None, b=None):
    """Mean-square K-weighted loudness over samples [a, b) (the 'line' loudness: a short-term reading over the line)."""
    k = kweight(x)[a:b]
    return -0.691 + 10 * np.log10((k ** 2).sum(1).mean() + 1e-20)
