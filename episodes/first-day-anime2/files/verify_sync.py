#!/usr/bin/env python3
"""Verifies the beat grid against the actual audio. Needs ffmpeg + numpy + scipy.
usage: python verify_sync.py first-day.mp3 [--bpm 88 --offset 1.062]
Writes onsets.json (spectral-flux onsets + kick onsets) and prints PASS/FAIL.
PASS = best offset within +-35 ms of the given one AND the silence gap 11.30-11.95 s is found."""
import sys, json, subprocess, argparse, numpy as np, scipy.signal as s, scipy.io.wavfile as w
ap = argparse.ArgumentParser(); ap.add_argument('mp3'); ap.add_argument('--bpm', type=float, default=88.0)
ap.add_argument('--offset', type=float, default=1.062); a = ap.parse_args()
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', a.mp3, '-ac', '1', '-ar', '22050', '/tmp/_v.wav'], check=True)
sr, x = w.read('/tmp/_v.wav'); x = x.astype(float) / 32768; hop, n = 256, 1024; fs = sr / hop
f, t, S = s.stft(x, sr, nperseg=n, noverlap=n - hop); M = np.abs(S)
fl = np.maximum(0, np.diff(np.log1p(M * 50), axis=1)).sum(0); fl /= fl.max()
lo = np.maximum(0, np.diff(np.log1p(M[f < 150] * 50), axis=1)).sum(0); lo /= lo.max(); tt = t[1:]
on = [round(float(tt[p]), 3) for p in s.find_peaks(fl, height=0.4, distance=int(.12 * fs))[0]]
kick = [round(float(tt[p]), 3) for p in s.find_peaks(lo, height=0.35, distance=int(.2 * fs))[0]]
json.dump({'onsets': on, 'kicks': kick}, open('onsets.json', 'w'))
beat = 60 / a.bpm; best = None
for off in np.arange(a.offset - 0.25, a.offset + 0.25, 0.005):
    ts = np.arange(off % beat, len(x) / sr, beat); idx = np.clip((ts * fs).astype(int), 0, len(lo) - 1)
    sc = lo[idx].mean() + 0.5 * fl[idx].mean()
    if best is None or sc > best[0]: best = (sc, off)
d = best[1] - a.offset
d = (d + beat / 2) % beat - beat / 2
rms = np.array([np.sqrt((x[int(i * sr):int((i + .05) * sr)] ** 2).mean()) for i in np.arange(10.5, 13, .05)])
quiet = [round(10.5 + i * .05, 2) for i, v in enumerate(rms) if v < 0.02]
print('grid offset error (s):', round(d, 3)); print('silence gap found:', (quiet[0], quiet[-1]) if quiet else None)
ok = abs(d) <= 0.035 and quiet and 11.2 <= quiet[0] <= 11.45 and 11.85 <= quiet[-1] + .05 <= 12.0
print('PASS' if ok else 'FAIL -> re-run sync_grid.py with --offset', round(a.offset + d, 3))
