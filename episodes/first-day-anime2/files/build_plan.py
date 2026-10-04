#!/usr/bin/env python3
"""Generates ../OPUS55_MV_PLAN.md and shots.json from shots.py (all times computed from the verified grid)."""
import json
from shots import S
OFF, BEAT, FPS = 1.062, 60/88, 30
T = lambda u: max(0.0, OFF + u*BEAT)
def fmt(t): return f'{int(t//60)}:{t%60:06.3f}'
out = []
for sh in S:
    a, b = (0.0 if sh['u0'] < 0 else T(sh['u0'])), min(43.70, T(sh['u1'])); sh.update(t0=round(a,3), t1=round(b,3), f0=round(a*FPS), f1=round(b*FPS), dur=round(b-a,3))
json.dump(S, open('shots.json','w'), ensure_ascii=False, indent=1)
shots_md = []
for sh in S:
    shots_md.append(f"""### {sh['id']} · {fmt(sh['t0'])} → {fmt(sh['t1'])} · {sh['dur']:.3f}s · f{sh['f0']}–{sh['f1']} · `{sh['kind']}`
- **Lyric/audio:** {sh['lyric'] or '—'}
- **Frame:** {sh['frame']}
- **Camera:** {sh['cam']}
- **Build:** {sh['build']}
- **On-screen text:** {sh['text']}
- **Sync cue:** {sh['sync']}
""")
HEAD = open('plan_static_head.md', encoding='utf8').read()
TAIL = open('plan_static_tail.md', encoding='utf8').read()
open('../OPUS55_MV_PLAN.md','w',encoding='utf8').write(HEAD + '\n## 10. SHOT LIST (computed from the grid; 52 shots, 43.70 s, 1311 frames @30 fps)\n\n' + '\n'.join(shots_md) + '\n' + TAIL)
print('shots', len(S), 'last end', S[-1]['t1'])
