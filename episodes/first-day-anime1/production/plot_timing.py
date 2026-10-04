"""Redraw timing evidence without changing the approved frame map."""
from pathlib import Path
import json
import numpy as np
import librosa
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
r = Path(__file__).resolve().parents[1]
d = json.loads((r / 'timing.json').read_text())
y, sr = librosa.load(r / 'first-day.mp3', sr=22050)
font = FontProperties(fname=str(r / 'render_kit/fonts/NotoSansSC-Bold.otf'), size=8)
fig, ax = plt.subplots(3, 1, figsize=(20, 9), sharex=True, gridspec_kw={'height_ratios': [3, 1, 2]})
t = np.arange(len(y)) / sr
ax[0].plot(t[::100], y[::100], color='#D97757', lw=.5)
for i, s in enumerate(d['shots']):
    f = s['frame'] / 30
    ax[0].axvline(f, color='#141413', alpha=.3, lw=.5)
    ax[0].text(f, .75 if i % 2 == 0 else .95, s['id'], fontsize=6, rotation=90, transform=ax[0].get_xaxis_transform())
ax[1].vlines(d['onsets'], 0, .3, color='#6A9BCC', lw=.6, label='Detected onsets')
ax[1].vlines(d['beats_regular'], .4, .65, color='#788C5D', lw=.7, label='Fitted quarter beats')
ax[1].vlines(d['bars'], .7, 1, color='#D97757', lw=1.2, label='Estimated bars')
ax[1].legend(loc='upper left', ncol=3, fontsize=8)
for i, line in enumerate(d['lyrics']):
    ax[2].axvline(line['t'], color='#D97757', alpha=.3)
    ax[2].text(line['t']+.04, .9-(i%3)*.3, line['text'], fontproperties=font, rotation=20, va='top')
for a in ax:
    a.axvspan(11.45, 11.92, color='#788C5D', alpha=.15)
    a.set_xlim(0, 43.7)
ax[1].set_yticks([]); ax[2].set_yticks([]); ax[2].set_ylim(-.25, 1.05)
ax[0].set_title('FIRST DAY — 44-shot timing, measured onsets, fitted beats and locked lyric anchors')
ax[2].set_xlabel('Seconds; title impact at frame 358 / 11.933 s')
fig.tight_layout(); fig.savefig(r / 'assets/timing.png', dpi=140)
