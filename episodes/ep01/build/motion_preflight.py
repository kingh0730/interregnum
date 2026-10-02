"""Independent, read-only local motion validation. Optional runner --dry-run only; never submits video.
Usage: uv run python episodes/ep01/build/motion_preflight.py [--runner-dry-run] [--only m07,m23,m30]
       [--quote-retakes m07,m23]
The shared runner's --dry-run prices jobs but does not decode media; this tool supplies those missing checks.
File/media validity and current recorded visual continuity approval are separate gates.
"""
import argparse,hashlib,json,re,subprocess,sys
from pathlib import Path
import numpy as np
from PIL import Image
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'episodes/ep01/build';W=ROOT/'work/ep01';ap=argparse.ArgumentParser();ap.add_argument('--runner-dry-run',action='store_true');ap.add_argument('--only');ap.add_argument('--quote-retakes');a=ap.parse_args()
sys.path.insert(0,str(ROOT/'tools'))
from continuity import evaluate_review
man=json.loads((B/'motion_plan.json').read_text());story=json.loads((B/'story.json').read_text());triage=json.loads((B/'motion_triage.json').read_text());lipdata=json.loads((W/'audio/lipsync_manifest.json').read_text());lips={x['shot_id']:x for x in lipdata};shots={x['id']:x for x in story['shots']};jobs=[dict(man['defaults'],**x) for x in man['jobs']];ids={x['id'] for x in jobs};errors=[];missing=[];checks=[]
continuity=evaluate_review(man.get('continuity_review'),ROOT)
# An otherwise valid review of another episode must not approve this handoff.
if continuity['review_sha256']:
 try:
  review=json.loads(Path(continuity['review_path']).read_text())
  for key,name in [('story','story.json'),('assets','assets.json'),('states','reel_states.json')]:
   if (ROOT/review.get(key,{}).get('path','')).resolve()!=(B/name).resolve():continuity['errors'].append(f'Continuity review must bind episode 01 {name}')
 except (ValueError,TypeError,AttributeError,OSError) as exc:continuity['errors'].append(f'Cannot verify episode continuity bindings: {exc}')
continuity['approved']=continuity['approved'] and not continuity['errors']
def fail(message):errors.append(message)
def probe(p):return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]))
def samples(p):return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-ar','48000','-ac','2','-f','f32le','-']),np.float32).reshape(-1,2)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assets_path=B/'assets.json';assets=json.loads(assets_path.read_text()) if assets_path.exists() else None
if assets is None:fail('Final approved assets.json is not available')
if len(ids)!=len(jobs):fail('Duplicate job IDs')
if len(jobs)!=30 or len(triage['shots'])!=40:fail('Expected30jobs and40triagedshots')
if story['fps']!=24 or story['total_frames']!=5520:fail('Story frame contract changed')
for row in triage['shots']:
 sh=shots[row['shot_id']]
 if row['input_state']!=sh['action'] or row['essential_story_check']!=sh['critical_action']:fail(f"Shot {row['shot_id']}: triage pose metadata differs from frozen story")
if {j['shot_id'] for j in jobs if j['endpoint']=='lipsync'}!={s for s,x in lips.items() if x['use_for_lipsync']}:fail('On-screen voice coverage mismatch')
if {j['shot_id'] for j in jobs}&{'02','08','19','22','29','40'}:fail('Graphic/off-screen insert/title incorrectly submitted')
if len({j['out'] for j in jobs})!=len(jobs):fail('Output path collision')
if a.only and set(a.only.split(','))-ids:fail('Unknown --only IDs')
if a.quote_retakes and set(a.quote_retakes.split(','))-ids:fail('Unknown retake IDs')
for j in jobs:
 sh=shots[j['shot_id']];dur=(sh['end_frame']-sh['start_frame'])/24;rec={'id':j['id'],'shot':j['shot_id'],'endpoint':j['endpoint']}
 if j['image_key']!=sh['asset']:fail(f"{j['id']}: wrong canonical image key")
 if j['resolution']!='768P' or j['prompt_expansion_mode']!='disabled':fail(f"{j['id']}: resolution/expansion default changed")
 if type(j['duration']) is not int or not 5<=j['duration']<=15:fail(f"{j['id']}: duration outside integer5–15s")
 if j['source_edit']!=[0,dur] or j['final_edit_frames']!=sh['end_frame']-sh['start_frame']:fail(f"{j['id']}: edit window mismatch")
 if not j['out'].startswith('work/ep01/motion/') or Path(j['out']).suffix!='.mp4':fail(f"{j['id']}: output outside reserved motion directory")
 if j.get('deps') or isinstance(j['image'],dict):fail(f"{j['id']}: unplanned chained dependency")
 image=ROOT/j['image']
 if assets:
  canonical=assets.get(j['image_key'])
  if isinstance(canonical,dict):canonical=canonical.get('path')
  if not canonical:fail(f"{j['id']}: image key absent from approved assets map")
  if canonical and (ROOT/canonical).resolve()!=image.resolve():fail(f"{j['id']}: input differs from final approved assets map")
 if not image.is_file():missing.append(str(image.relative_to(ROOT)));rec['image_status']='missing'
 else:
  try:
   with Image.open(image) as im:
    width,height=im.size;mode=im.mode;im.verify()
   ratio=width/height
   if abs(ratio-16/9)>.025 or width<768 or height<432:fail(f"{j['id']}: unexpected image canvas {width}x{height}")
   actual_image_hash=digest(image)
   if j.get('approved_image_sha256') and j['approved_image_sha256']!=actual_image_hash:fail(f"{j['id']}: approved image bytes changed")
   rec.update(image_path=j['image'],image_status='decodes',image_shape=[width,height],image_mode=mode,image_sha256=actual_image_hash)
  except Exception as exc:fail(f"{j['id']}: image decode failed: {exc}")
 if j['endpoint']=='lipsync':
  ln=lips[j['shot_id']]
  if j.get('prompt') or j.get('end_image') or j.get('params',{}).get('prompt'):fail(f"{j['id']}: unsupported lip-sync direction field")
  if j.get('params')!={'enable_transcription':False}:fail(f"{j['id']}: unexpected lip-sync params")
  if j['input_audio_source']!=ln['path']:fail(f"{j['id']}: wrong isolated source")
  source=ROOT/ln['path'];audio=ROOT/j['audio']
  for p in [source,audio]:
   if not p.is_file():missing.append(str(p.relative_to(ROOT)))
  if source.is_file() and audio.is_file():
   try:
    p=probe(audio);st=p['streams'][0];seconds=float(p['format']['duration']);x=samples(audio);original=samples(source)
    if int(st['sample_rate'])!=48000 or st['channels']!=2:fail(f"{j['id']}: conditioning format must be48k stereo")
    if abs(seconds-j['duration'])>1/48000 or seconds<5:fail(f"{j['id']}: conditioning duration mismatch or below5s")
    if len(original)!=(sh['end_frame']-sh['start_frame'])*2000:fail(f"{j['id']}: original shot audio length mismatch")
    if not np.array_equal(x[:len(original)],original):fail(f"{j['id']}: submission altered original isolated speech")
    if len(x)>len(original) and np.any(x[len(original):]):fail(f"{j['id']}: submission tail contains non-silence")
    if not np.isfinite(x).all() or np.max(np.abs(x))>=1:fail(f"{j['id']}: conditioning waveform invalid/clipped")
    rec.update(audio_seconds=seconds,audio_sha256=digest(audio),original_prefix_sample_identical=True,padded_tail_silent=True)
   except Exception as exc:fail(f"{j['id']}: audio validation failed: {exc}")
 elif j['endpoint']=='i2v':
  prompt=j.get('prompt','')
  if not prompt or 'mouths remain closed' not in prompt.lower():fail(f"{j['id']}: missing closed-mouth behaviour direction")
  if re.search(r'\b(says?|talk\w*|speaks?|speech|dialogue|shouts?|sings?|lip.?sync)\b',prompt,re.I):fail(f"{j['id']}: speech-trigger wording in motion prompt")
  if j.get('audio') or j.get('params',{}).get('target_audio_url'):fail(f"{j['id']}: unsupported combined action/speech assumption")
 else:fail(f"{j['id']}: unknown endpoint")
 checks.append(rec)
retakes=set(a.quote_retakes.split(',')) if a.quote_retakes else set();quote=round(sum(j['duration']*man['rates_usd_per_second'][j['endpoint']] for j in jobs if j['id'] in retakes),2)
ledger=B/'h3_log/ledger.jsonl'; records=[json.loads(x) for x in ledger.read_text().splitlines() if x.strip()] if ledger.exists() else []; seen_requests=set(); seen_jobs=set();spent=0.;retake_spent=0.
for rec in records:
 if rec.get('request_id') in seen_requests:continue
 seen_requests.add(rec.get('request_id'));cost=float(rec.get('price',0));spent+=cost
 if rec.get('id') in seen_jobs:retake_spent+=cost
 seen_jobs.add(rec.get('id'))
if retake_spent+quote>man['budget']['retake_reserve_cap_usd']+.0001:fail('Recorded plus quoted retakes exceed proposed reserve')
report={'stage':'Preparation only; no motion generation authorized or performed','manifest':'episodes/ep01/build/motion_plan.json','manifest_sha256':digest(B/'motion_plan.json'),'story_sha256':digest(B/'story.json'),'local_media_ready':not errors and not missing,'visual_approval':'This validates files and media bounds only; it does not replace image continuity review.','errors':errors,'missing_sources':sorted(set(missing)),'checks':checks,'budget':man['budget'],'quoted_retakes':sorted(retakes),'quoted_retake_usd':quote,'recorded_estimated_spend_usd':round(spent,3),'recorded_retake_spend_usd':round(retake_spent,3),'runner_dry_run_performed':False,'video_requests_submitted':0}
if a.runner_dry_run and not errors and not missing:
 cmd=['uv','run','tools/video/h3_batch.py','episodes/ep01/build/motion_plan.json','--root',str(ROOT),'--dry-run']
 if a.only:cmd+=['--only',a.only]
 r=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True);log=W/'motion/runner_dry_run.txt';log.parent.mkdir(parents=True,exist_ok=True);log.write_text(r.stdout+r.stderr);report.update(runner_dry_run_performed=True,runner_returncode=r.returncode,runner_log=str(log.relative_to(ROOT)))
 expected=sum(j['duration']*man['rates_usd_per_second'][j['endpoint']] for j in jobs if not a.only or j['id'] in a.only.split(','))
 found=re.search(r'estimated new spend \$([0-9.]+)',r.stdout)
 if r.returncode:errors.append('Shared runner dry-run failed; inspect saved output')
 if found:report['runner_estimate_usd']=float(found.group(1));report['local_selected_estimate_usd']=round(expected,2)
 if found and abs(float(found.group(1))-round(expected,2))>.02:errors.append('Live/fallback runner price differs from captured rate or existing jobs; reconcile before any paid run')
 elif not found:errors.append('Runner estimate missing')
report['local_media_ready']=not errors and not missing
continuity_summary={k:v for k,v in continuity.items() if k not in ['source_hashes','shot_sources']}
continuity_summary['review_path']=man.get('continuity_review')
report.update(continuity_review=continuity_summary,continuity_approved=continuity['approved'],ready_for_motion=report['local_media_ready'] and continuity['approved'])
out=B/'motion_preflight.json'
if out.exists():
 previous=json.loads(out.read_text())
 if 'superseded_spatial_approval_history' in previous:report['superseded_spatial_approval_history']=previous['superseded_spatial_approval_history']
 if previous.get('runner_dry_run_performed'):
  report['previous_runner_quote']={k:previous[k] for k in ['manifest_sha256','runner_returncode','runner_log','runner_estimate_usd','local_selected_estimate_usd'] if k in previous}
 elif 'previous_runner_quote' in previous:report['previous_runner_quote']=previous['previous_runner_quote']
out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:report[k] for k in ['local_media_ready','continuity_approved','ready_for_motion','errors','missing_sources','budget','runner_dry_run_performed','video_requests_submitted']},indent=2));sys.exit(0 if report['ready_for_motion'] else 2)
