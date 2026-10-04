"""Render all final frames, one shot at a time, retaining all output PNGs for QA.
Only regenerable input sequences are removed between shots. The frame store may be RAM-backed.
"""
from pathlib import Path
import json,subprocess,sys,shutil,time,os,hashlib
R=Path(__file__).resolve().parents[1];REPO=R.parents[1];KIT=R/'render_kit';WORK=REPO/'work/first-day-anime1';NODE=Path.home()/'.nvm/versions/node/v22.23.1/bin/node'
timing=json.loads((R/'timing.json').read_text());media=json.loads((KIT/'text/media.json').read_text());frames=WORK/'frames';assert frames.exists(),'Frame store is not mounted'
digest=hashlib.sha256()
for p in [KIT/'dist/scene.js',KIT/'runtime.js',KIT/'accum.js',R/'production/prepare_plates.py']+sorted((KIT/'text').glob('*.json'))+sorted(p for d in ['plates','rigs','environment','depth','mattes','logos'] for p in (R/'assets'/d).rglob('*') if p.is_file())+sorted({R/v['file'] for v in media.values()}):
 digest.update(str(p.relative_to(R)).encode());digest.update(p.read_bytes())
fingerprint=digest.hexdigest();marker=frames/'render-inputs.json'
if marker.exists() and json.loads(marker.read_text()).get('fingerprint')!=fingerprint:
 if '--restart' not in sys.argv:raise SystemExit('Render inputs changed: use --restart to rebuild this production frame store')
 for p in frames.glob('*.png'):p.unlink()
marker.write_text(json.dumps({'fingerprint':fingerprint,'frame_count':1311,'resolution':[1920,1080],'fps':30})+'\n')
measurements=R/'production/render-measurements.json';records=json.loads(measurements.read_text()) if measurements.exists() else []
for shot in timing['shots']:
 sid=shot['id'];a,b=shot['frame'],shot['end_frame']-1
 if all((frames/f'{f:05}.png').is_file() for f in range(a,b+1)):
  print('resume skip',sid,flush=True);continue
 for p in (WORK/'plates').iterdir():
  if p.is_dir():shutil.rmtree(p)
 owner=media.get(sid,{}).get('source_id')
 if owner:subprocess.run([sys.executable,str(R/'production/prepare_plates.py'),owner],cwd=REPO,check=True)
 started=time.time();subprocess.run([str(NODE),str(KIT/'render.mjs'),f'--from={a}',f'--to={b}','--scale=1',f'--out={frames}','--workers=1','--angle=metal','--force'],cwd=KIT,check=True)
 missing=[f for f in range(a,b+1) if not (frames/f'{f:05}.png').is_file()];assert not missing,(sid,missing)
 records.append({'shot':sid,'frames':b-a+1,'seconds':round(time.time()-started,3),'png_bytes':sum((frames/f'{f:05}.png').stat().st_size for f in range(a,b+1))})
 (R/'production/render-measurements.json').write_text(json.dumps(records,indent=2)+'\n');print('finished',sid,records[-1],flush=True)
for p in (WORK/'plates').iterdir():
 if p.is_dir():shutil.rmtree(p)
files=list(frames.glob('*.png'));assert len(files)==1311,len(files)
print('COMPLETE: 1311 lossless final-size PNGs retained for QA',flush=True)
