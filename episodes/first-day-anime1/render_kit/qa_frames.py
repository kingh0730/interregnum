#!/usr/bin/env python3
"""Validate the actual rendered sequence, with only explicit plan exceptions."""
from pathlib import Path
import sys,json,hashlib
import numpy as np
from PIL import Image
root=Path(__file__).resolve().parent;folder=Path(sys.argv[1]);timing=json.loads((root.parent/'timing.json').read_text());shots=timing['shots'];files=sorted(folder.glob('*.png'));expected=[f'{i:05}.png' for i in range(1311)]
errors=[]
if [p.name for p in files]!=expected:errors.append('Sequence filenames/count differ from 00000.png through 01310.png')
flash=[(shots[11]['frame'],2),(358,2),(388,1),(shots[16]['frame'],2),(shots[23]['frame'],2),(755,1),(shots[31]['frame'],2),(shots[33]['frame'],1)]
intentional_uniform={f for a,n in flash for f in range(a,a+n)}|set(range(shots[42]['frame'],shots[42]['end_frame']))|{1310}
intentional_freeze=intentional_uniform|set(range(shots[12]['frame'],shots[12]['end_frame']))|set(range(round(42.8*30),1311))
prev=None;deltas=[];stats=[];hashes={}
for i,p in enumerate(files):
 with Image.open(p) as im:
  if im.size!=(1920,1080):errors.append([i,'wrong_dimensions',im.size])
  if im.mode=='RGBA' and im.getextrema()[3]!=(255,255):errors.append([i,'nonopaque'])
  a=np.asarray(im.convert('L').resize((192,108)),dtype=np.float32)
 mean,std=float(a.mean()),float(a.std());delta=None if prev is None else float(np.abs(a-prev).mean());deltas.append(delta or 0)
 if (mean<2 or mean>253 or std<.25) and i not in intentional_uniform:errors.append([i,'unexpected_uniform',mean,std])
 if delta is not None and delta<.015 and i not in intentional_freeze:errors.append([i,'unexpected_freeze',delta])
 stats.append({'frame':i,'mean':round(mean,3),'std':round(std,3),'delta':round(delta or 0,4)});hashes[p.name]=hashlib.sha256(p.read_bytes()).hexdigest();prev=a
match_cuts={'S09','S10','S11','S34'};cut_report=[]
for s in shots[1:]:
 f=s['frame'];target_frame=int(s['target']*30+.5)
 if abs(f-target_frame)>3:errors.append([s['id'],'cut_exceeds_three_frame_tolerance',f-target_frame])
 if s.get('lyric_anchor') and f!=target_frame:errors.append([s['id'],'lyric_anchor_moved'])
 near=range(max(1,f-3),min(1311,f+4));peak=max(near,key=lambda i:deltas[i]);visible=deltas[f]>.25 or max(deltas[i] for i in near)>.25 or s['id'] in match_cuts
 cut_report.append({'shot':s['id'],'expected_frame':f,'delta_at_boundary':round(deltas[f],3),'local_peak_frame':peak,'visible_transition_or_explicit_match_cut':visible})
 if not visible:errors.append([s['id'],'unresolved_cut'])
report={'frame_count':len(files),'resolution':[1920,1080],'fps':30,'intentional_uniform_frames':sorted(intentional_uniform),'intentional_holds':'S13 and the specified final end-card hold; impact/whiteout frames are intentional.','cuts':cut_report,'errors':errors,'passed':not errors,'scope':'Image sequence checks. Does not assert human audiovisual playback, phoneme accuracy, or semantic camera quality.'}
(root.parent/'production/frame-qa.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');(root.parent/'production/frame-stats.json').write_text(json.dumps(stats)+'\n');(root.parent/'production/frame-hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2));sys.exit(bool(errors))
