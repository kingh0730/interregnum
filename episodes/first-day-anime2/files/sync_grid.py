#!/usr/bin/env python3
"""Builds sync.json (beat/bar grid, lyric lines, per-character lyric timing) for first-day.mp3.
Grid was measured by me (numpy/scipy flux fit): 88 BPM, downbeat of bar 1 at 1.062 s.
ALWAYS run verify_sync.py first; if it reports a different offset, pass --offset.
usage: python sync_grid.py --lrc first-day.lrc --out sync.json [--offset 1.062] [--bpm 88] [--onsets onsets.json]
"""
import argparse, json, re, bisect
FPS = 30
ap = argparse.ArgumentParser()
ap.add_argument('--lrc', default='first-day.lrc'); ap.add_argument('--out', default='sync.json')
ap.add_argument('--offset', type=float, default=1.062); ap.add_argument('--bpm', type=float, default=88.0)
ap.add_argument('--dur', type=float, default=43.70); ap.add_argument('--onsets', default='onsets.json')
a = ap.parse_args()
beat = 60.0 / a.bpm; bar = beat * 4
T = lambda u: a.offset + u * beat           # u = beats since bar-1 downbeat (can be fractional / negative)
lines = []
for l in open(a.lrc, encoding='utf8'):
    m = re.match(r'\[(\d+):(\d+\.\d+)\](.*)', l.strip())
    if m: lines.append({'t': int(m[1]) * 60 + float(m[2]), 'text': m[3].strip()})
for i, L in enumerate(lines):
    L['end'] = lines[i + 1]['t'] if i + 1 < len(lines) else a.dur
try: vocal_onsets = json.load(open(a.onsets))['onsets']
except Exception: vocal_onsets = []
def snap(t, tol=0.08):
    if not vocal_onsets: return t
    i = bisect.bisect_left(vocal_onsets, t); c = vocal_onsets[max(0, i - 1):i + 1]
    best = min(c, key=lambda x: abs(x - t)) if c else t
    return best if abs(best - t) <= tol else t
for L in lines:                                   # per-character timing: spread over sung span, snap to onsets
    chars = [c for c in L['text']]
    span_end = L['end'] - 0.18 if L['end'] - L['t'] < 3.4 else L['t'] + 2.6
    n = len(chars)
    L['chars'] = [{'c': c, 't': round(snap(L['t'] + (span_end - L['t']) * i / n), 3)} for i, c in enumerate(chars)]
grid = {'fps': FPS, 'bpm': a.bpm, 'beat': beat, 'bar': bar, 'offset': a.offset, 'duration': a.dur,
        'frames': round(a.dur * FPS),
        'beats': [{'u': u, 't': round(T(u), 3), 'frame': round(T(u) * FPS), 'bar': u // 4 + 1, 'beat_in_bar': u % 4 + 1}
                  for u in range(0, int((a.dur - a.offset) / beat) + 1)],
        'eighths': [round(T(u / 2), 3) for u in range(0, int((a.dur - a.offset) / beat * 2) + 1)],
        'sections': [
            {'name': 'verse', 'start': 0.0, 'end': round(T(15), 3)},
            {'name': 'stop_beat_silence', 'start': round(T(15), 3), 'end': round(T(16), 3)},
            {'name': 'chorus1', 'start': round(T(16), 3), 'end': round(T(32), 3)},
            {'name': 'chorus2_flight', 'start': round(T(32), 3), 'end': round(T(48), 3)},
            {'name': 'forever_x3_outro', 'start': round(T(48), 3), 'end': a.dur}],
        'lyrics': lines}
json.dump(grid, open(a.out, 'w'), ensure_ascii=False, indent=1)
print(f'beat {beat:.4f}s bar {bar:.4f}s frames {grid["frames"]} -> {a.out}')
for k in (0, 4, 8, 12, 15, 16, 20, 32, 48, 52, 56, 60): print(f'u={k:>2} t={T(k):7.3f}s f={round(T(k)*FPS)}')
