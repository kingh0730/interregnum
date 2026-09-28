"""Synthesize the soundtrack: wind ambience, airplane whoosh, soft pad + piano arpeggio."""
import wave
from pathlib import Path

import numpy as np

SR = 48000
DUR = 14.0
N = int(SR * DUR)
t = np.arange(N) / SR
rng = np.random.default_rng(7)


def bandpass(x, lo, hi):
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    m = 1 / (1 + (lo / np.maximum(f, 1)) ** 4) / (1 + (f / hi) ** 4)
    return np.fft.irfft(X * m, len(x))


def norm(x):
    return x / (np.abs(x).max() + 1e-9)


def env_adsr(n, a, r):
    e = np.ones(n)
    na, nr = int(a * SR), int(r * SR)
    e[:na] = np.linspace(0, 1, na)
    e[-nr:] *= np.linspace(1, 0, nr)
    return e


# ---- wind: two decorrelated noise beds with slow gusts
def wind(seed):
    r = np.random.default_rng(seed)
    x = bandpass(r.normal(size=N), 150, 1400)
    gust = 0.55 + 0.45 * np.sin(2 * np.pi * 0.23 * t + seed) * np.sin(2 * np.pi * 0.11 * t + 1.3 * seed)
    return norm(x) * gust


wl, wr = wind(1), wind(2)
wind_gain = 0.16 * np.interp(t, [0, 4.5, 9.0, 14], [1.0, 0.7, 1.0, 0.8])

# ---- whoosh as the plane flies off (shot 3 starts at 9.0s)
wh = np.zeros(N)
s0, s1 = int(9.0 * SR), int(10.6 * SR)
seg = rng.normal(size=s1 - s0)
k = np.linspace(0, 1, s1 - s0)
lo_band = norm(bandpass(seg, 300, 1500))
hi_band = norm(bandpass(seg, 1500, 5000))
wh[s0:s1] = (lo_band * (1 - k) + hi_band * k) * np.sin(np.pi * k ** 0.6) ** 2 * 0.35
pan = np.interp(t, [9.0, 10.6], [0.25, 0.85])  # left -> right, following the plane

# ---- music: Fmaj7 -> G6 -> Em7 -> Am(add9), 3.5s each
def midi(n):
    return 440 * 2 ** ((n - 69) / 12)


chords = [[53, 57, 60, 64], [55, 59, 62, 64], [52, 55, 59, 62], [45, 57, 60, 64, 71]]
pad = np.zeros(N)
for i, ch in enumerate(chords):
    a, b = int(i * 3.5 * SR), int(min((i + 1) * 3.5 + 0.8, DUR) * SR)
    tt = t[: b - a]
    e = env_adsr(b - a, 1.2, 1.0)
    for n in ch:
        f = midi(n)
        for det in (-0.12, 0.0, 0.12):
            v = np.sin(2 * np.pi * f * (1 + det / 100) * tt + rng.uniform(0, 6.28))
            v += 0.25 * np.sin(2 * np.pi * 2 * f * tt)
            pad[a:b] += v * e / len(ch)
pad = bandpass(pad, 60, 2200)

piano_l = np.zeros(N)
piano_r = np.zeros(N)
step = 60 / 84 / 2  # eighth notes at 84 bpm
arp_order = [0, 1, 2, 3, 2, 1]
tick = 0
tn = 0.9  # arpeggio enters after the fade-in
while tn < DUR - 1.2:
    ci = min(int(tn / 3.5), 3)
    ch = chords[ci]
    n = ch[arp_order[tick % len(arp_order)] % len(ch)] + 12
    f = midi(n)
    L = int(2.2 * SR)
    a = int(tn * SR)
    b = min(a + L, N)
    tt = np.arange(b - a) / SR
    note = sum(np.sin(2 * np.pi * f * h * tt) * np.exp(-tt * (2.2 + 1.8 * h)) / h ** 1.3 for h in (1, 2, 3, 4))
    note *= np.minimum(1, tt / 0.004)
    vel = 0.75 + 0.25 * rng.random()
    p = 0.5 + 0.3 * np.sin(tick * 0.9)
    piano_l[a:b] += note * vel * (1 - p)
    piano_r[a:b] += note * vel * p
    tick += 1
    tn += step

# chime on the plane's glint (~13.15s)
g0 = int(13.15 * SR)
tt = np.arange(N - g0) / SR
chime = sum(np.sin(2 * np.pi * midi(88) * r * tt) * np.exp(-tt * d) for r, d in [(1, 1.8), (2.76, 3.0), (5.4, 5.0)])
chime_full = np.zeros(N)
chime_full[g0:] = chime * 0.12

music_gain = np.interp(t, [0, 1.0, 12.8, 14], [0, 1, 1, 0]) * 0.22
L = wl * wind_gain + wh * (1 - pan) + (norm(pad) * 0.6 + norm(piano_l) * 0.5) * music_gain + chime_full
R = wr * wind_gain + wh * pan + (norm(pad) * 0.6 + norm(piano_r) * 0.5) * music_gain + chime_full
master = np.interp(t, [0, 0.6, 13.1, 14], [0, 1, 1, 0])
st = np.stack([L, R], 1) * master[:, None]
st = st / np.abs(st).max() * 0.89

out = Path(__file__).parent / "render" / "soundtrack.wav"
with wave.open(str(out), "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes((st * 32767).astype(np.int16).tobytes())
print("wrote", out)
