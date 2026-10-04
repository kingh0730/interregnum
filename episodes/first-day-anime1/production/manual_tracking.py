from pathlib import Path
import json
p=Path(__file__).resolve().parents[1]/'render_kit/text/tracking.json';d=json.loads(p.read_text());s=d['S21'];W,H=1916,1080
# Two visually inspected endpoint frames; suppress unreliable points while the head is cropped.
keys={'eye0':([880,61,22],[886,82,22]),'eye1':([965,48,22],[972,78,22]),'brooch':([934,184,22],[939,212,22]),'pin':([1030,34,31],[1040,60,31])}
for name,(a,b) in keys.items():
 vals=s['marks'][name]
 for f in range(13,min(60,len(vals))):vals[f][2]=0
 for f in range(60,len(vals)):
  u=min(1,(f-60)/12);v=[a[i]+(b[i]-a[i])*u for i in range(3)];vals[f]=[v[0]/W,v[1]/H,v[2]/W,0]
for frame,name in s['weak_frames']:
 if name=='tag' and frame<len(s['marks'][name]):s['marks'][name][frame][2]=0
s['manual_review']='Native frames 60 and 72 inspected; endpoint head marks re-registered; marks withheld during head crop and uncertain tag tracking.'
p.write_text(json.dumps(d,separators=(',',':'))+'\n')
