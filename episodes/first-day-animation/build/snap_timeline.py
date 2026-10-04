import json,numpy as np
from pathlib import Path
r=Path(__file__).resolve().parents[1];tl=json.load(open(r/'build/manifest/shots.json'));a=json.load(open(r/'assets/audio.json'));ly=json.load(open(r/'assets/lyrics.json'));anchors=[x['start']for x in ly]+[11.2,11.92,5.78,10.64,42.45]
candidates=np.array(sorted(set(a['beats']+a['onsets'])));changes=[]
for s in tl['shots']:
 t=s['start'];s['authored_start']=t
 if min(abs(t-x)for x in anchors)<.005:continue
 near=float(candidates[np.argmin(abs(candidates-t))]);err=near-t
 if abs(err)<=.08:
  old=s['start_frame'];s['start_frame']=int(near*30+.5);s['start']=s['start_frame']/30;changes.append({'id':s['id'],'authored':t,'onset':near,'frame':s['start_frame'],'difference':err})
 else:changes.append({'id':s['id'],'authored':t,'nearest_event':near,'difference':err,'decision':'Retain explicit shot-list boundary: no measured event within tolerance.'})
for i,s in enumerate(tl['shots']):
 s['end_frame']=tl['shots'][i+1]['start_frame']if i+1<len(tl['shots'])else 1311;s['end']=s['end_frame']/30;s['frames']=s['end_frame']-s['start_frame'];s['duration']=s['end']-s['start'];s['start']=s['start_frame']/30
json.dump(tl,open(r/'compositor/timeline.json','w'),ensure_ascii=False,indent=2);json.dump({'measured_tempo':a['tempo'],'adjustments':changes},open(r/'build/timing-adjustments.json','w'),indent=2);print(len(changes),'non-anchor boundaries inspected')
