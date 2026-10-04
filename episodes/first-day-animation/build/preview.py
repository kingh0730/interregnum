import json,os,subprocess,sys
from pathlib import Path
r=Path(__file__).resolve().parents[1];s=json.load(open(r/'compositor/timeline.json'))['shots'];frames=sorted(set([x['start_frame'] for x in s]+[(x['start_frame']+x['end_frame'])//2 for x in s]+[x['end_frame']-1 for x in s if 'P' in x['source']]))
env=dict(os.environ,MODE='preview',FRAMES=','.join(map(str,frames)))
subprocess.run(['/Users/kingh0730/.nvm/versions/node/v22.23.1/bin/node',str(r/'render.mjs')],env=env,check=True)
subprocess.run([sys.executable,str(r/'build/sheet.py'),str(r/'out/qa/timeline-preview.jpg')]+[str(r/'out/qa'/f'{(x["start_frame"]+x["end_frame"])//2:05d}.jpg')for x in s],check=True)
