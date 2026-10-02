"""Episode-only paid voice performance with durable request records and measured selection.
Usage: uv run python episodes/ep01/build/audio_voice.py EDA|SEN [--seeds 1701,1702]
Never retries an uncertain POST; reruns reuse saved media and analyses.
"""
import argparse, concurrent.futures, difflib, hashlib, json, os, subprocess, sys, time, urllib.request, urllib.error
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'tools/audio'))
import voice_design as vd
import mlx_whisper
ap=argparse.ArgumentParser(); ap.add_argument('speaker'); ap.add_argument('--seeds',default='1701,1702'); ap.add_argument('--only'); a=ap.parse_args()
work=ROOT/'work/ep01/audio/dialogue'; work.mkdir(parents=True,exist_ok=True)
cast=json.loads((ROOT/'work/ep01/audio/cast/voices.json').read_text()); voice=cast[a.speaker]['voice_id']
story=json.loads((ROOT/'episodes/ep01/build/story.json').read_text())
lines=[dict(ln,shot_id=sh['id'],start=sh['start_frame']/24,end=sh['end_frame']/24) for sh in story['shots'] for ln in sh['dialogue'] if ln['speaker']==a.speaker]
if a.only:lines=[ln for ln in lines if ln['id'] in a.only.split(',')]
key=os.environ['ELEVENLABS_API_KEY_STARTER']; settings={'stability':0.85,'similarity_boost':0.8,'speed':1.0}
seeds=[int(x) for x in a.seeds.split(',')]
def generate(job):
 ln,seed=job; prefix=work/f"{ln['id']}_{seed}"; p=prefix.with_suffix('.mp3'); log=prefix.with_suffix('.request.json')
 body={'text':ln['text'],'model_id':'eleven_v4','seed':seed,'voice_settings':settings}
 if p.exists():return ln,seed,p
 if log.exists():raise RuntimeError(f'Unresolved request {log}; refusing duplicate POST')
 record={'line_id':ln['id'],'speaker':a.speaker,'voice_id':voice,'body':body,'state':'submission_pending','time':time.time()};log.write_text(json.dumps(record,indent=2))
 req=urllib.request.Request(f'https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format=mp3_44100_128',data=json.dumps(body).encode(),method='POST',headers={'xi-api-key':key,'Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(req,timeout=180) as r:
   data=r.read(); record.update(state='complete',request_id=r.headers.get('request-id'),content_type=r.headers.get('content-type'),bytes=len(data),sha256=hashlib.sha256(data).hexdigest());p.write_bytes(data)
 except urllib.error.HTTPError as e:
  record.update(state='http_error',status=e.code,detail=e.read().decode()[:500]);log.write_text(json.dumps(record,indent=2));raise
 log.write_text(json.dumps(record,indent=2));print('generated',p.name,flush=True);return ln,seed,p
jobs=[(ln,seed) for ln in lines for seed in seeds]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 results=list(pool.map(generate,jobs))
selp=work/'selection.json';selection=json.loads(selp.read_text()) if selp.exists() else {}
for ln in lines:
 candidates=[]
 for seed in seeds:
  p=work/f"{ln['id']}_{seed}.mp3";mp=p.with_suffix('.analysis.json')
  if mp.exists():c=json.loads(mp.read_text())
  else:
   m=vd.analyse(p) or {};tr=mlx_whisper.transcribe(str(p),path_or_hf_repo='mlx-community/whisper-small-mlx',language='en',verbose=False)['text'].strip();acc=difflib.SequenceMatcher(None,vd.words(ln['text']),vd.words(tr)).ratio()
   dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(p)]))
   c={'file':p.name,'seed':seed,'text_match':round(acc,3),'transcript':tr,'duration':dur,**m};mp.write_text(json.dumps(c,indent=2))
  c['score']=round(-(c.get('f0_spread_st',12)+.3*c.get('level_spread_db',18))-(0 if c['text_match']>=.99 else 1000*(1-c['text_match'])),2)
  candidates.append(c)
 candidates.sort(key=lambda c:-c['score']);selection[ln['id']]={'speaker':a.speaker,'voice_id':voice,'settings':settings,'text':ln['text'],'best':candidates[0],'candidates':candidates}
 selp.write_text(json.dumps(selection,indent=2)); print(ln['id'],candidates[0],flush=True)
