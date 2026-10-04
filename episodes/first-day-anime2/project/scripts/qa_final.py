#!/usr/bin/env python3
"""Evidence-only final-media QA. Never equates technical measurements with art approval.
Run from repository root with .venv/bin/python. Exit 1 means a measured check failed;
exit 2 means a required input/tool failed. A diagnostic run can never approve delivery.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time as clocktime
from fractions import Fraction
os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir())/'opus55-matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from PIL import Image, ImageDraw, ImageFont

PROJECT=Path(__file__).resolve().parents[1]
SCENE_THRESHOLDS=(.03,.10,.30)
FPS=30
EXPECTED_FRAMES=1311
HARD_CUES=[('bubble',5.23),('spark-fill',11.289),('birth-impact',11.971),('ankle-contact',18.104),('white-out',22.880),('dolly-zoom-end',33.789)]
MANUAL=[
 'Character on-model in every appearance: coral inner hair, spark pupils, tie, costume and silhouettes.',
 'All generated text/logos absent; all required OPUS5.5/Anthropic identity moments legible.',
 'All six memes present and approved; no generated pseudo-Hanzi visible.',
 'Lyrics use correct glyphs, avoid eyes, and stay in the required safe area.',
 'Every named camera direction is visible; reduced camera angles and retained fractions reviewed.',
 'Every shot/action/pose is present; rendered contact and choreography satisfy the brief.',
 'Depth/layer borders and disocclusions inspected at100% final resolution.',
 'Contact sheets, type peaks, six hard cues, scopes and camera strips visually reviewed.',
 'Normal-speed final playback in VLC and a browser: motion, dropped frames and perceptual audio reviewed.',
]

def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()

def run(args, binary=False):
 p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if p.returncode:raise RuntimeError('Command failed: '+' '.join(map(str,args))+'\n'+p.stderr.decode(errors='replace')[-5000:])
 return p.stdout if binary else p.stdout.decode(errors='replace')

def probe(path):
 return json.loads(run(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(path)]))

def dump(path,value):
 Path(path).write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n')

def evidence(path):
 return {'path':str(Path(path).resolve()),'sha256':sha(path),'bytes':Path(path).stat().st_size}

def packet_data(path):
 d=json.loads(run(['ffprobe','-v','error','-select_streams','a:0','-show_packets','-show_data_hash','sha256','-show_entries','packet=data_hash,pts_time,duration_time,size','-of','json',str(path)]))
 return d.get('packets',[])

def decode_audio(path,rate=11025):
 return np.frombuffer(run(['ffmpeg','-v','error','-threads','4','-i',str(path),'-map','0:a:0','-ac','1','-ar',str(rate),'-f','f32le','-'],binary=True),dtype='<f4').copy()

def alignment(source,actual,rate):
 n=min(len(source),len(actual))
 if n<rate:return {'status':'FAIL','reason':'Less than1s decoded audio'}
 a=source[:n].astype(np.float64);b=actual[:n].astype(np.float64)
 corr=signal.correlate(b-b.mean(),a-a.mean(),mode='full',method='fft');lags=signal.correlation_lags(n,n,mode='full')
 take=np.abs(lags)<=rate
 lag=int(lags[take][np.argmax(corr[take])])
 x,y=(source[:min(len(source),len(actual)-lag)],actual[lag:]) if lag>=0 else (source[-lag:],actual)
 m=min(len(x),len(y));x=x[:m].astype(float);y=y[:m].astype(float)
 cosine=float(np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y)+1e-20));rmse=float(np.sqrt(np.mean((x-y)**2)))
 return {'status':'PASS' if abs(lag)<=rate/FPS and cosine>=.9999 else 'FAIL','sampleRate':rate,'sourceDecodedSamples':len(source),'finalDecodedSamples':len(actual),'lagSamples':lag,'lagSeconds':lag/rate,'lagFrames':lag/rate*FPS,'lagSign':'positive means final audio delayed relative to source','alignedCosineSimilarity':cosine,'alignedRMSE':rmse,'scope':'mono11025Hz decoded waveforms; maximum search lag±1s; allowed alignment±1frame, similarity>=.9999'}

def read_exact(pipe,size):
 chunks=[];left=size
 while left:
  b=pipe.read(left)
  if not b:break
  chunks.append(b);left-=len(b)
 return b''.join(chunks)

def previews(video,out,selected):
 folder=out/'frames';folder.mkdir(exist_ok=True)
 p=subprocess.Popen(['ffmpeg','-v','error','-threads','4','-filter_threads','2','-i',str(video),'-map','0:v:0','-vf','scale=480:270:flags=lanczos','-fps_mode','passthrough','-pix_fmt','rgb24','-f','rawvideo','-'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 index=0;previous=None;energy=[];frame_paths={};rgb_hist=np.zeros((3,256),dtype=np.int64);waveform=np.zeros((256,480),dtype=np.int64)
 while True:
  raw=read_exact(p.stdout,480*270*3)
  if not raw:break
  if len(raw)!=480*270*3:raise RuntimeError('Truncated preview decode')
  rgb=np.frombuffer(raw,np.uint8).reshape(270,480,3)
  grey=(rgb@np.array([.2126,.7152,.0722],np.float32)).astype(np.float32)
  energy.append(0 if previous is None else float(np.mean(np.abs(grey-previous))))
  previous=grey
  if index in selected:
   path=folder/f'f{index:04d}.jpg';Image.fromarray(rgb).save(path,quality=91,subsampling=0);frame_paths[index]=path
  if index%30==0:
   for c in range(3):rgb_hist[c]+=np.bincount(rgb[:,:,c].ravel(),minlength=256)
   bins=np.clip(np.round(grey),0,255).astype(int);xs=np.broadcast_to(np.arange(480),(270,480));waveform+=np.bincount((bins*480+xs).ravel(),minlength=256*480).reshape(256,480)
  index+=1
 err=p.stderr.read().decode(errors='replace');code=p.wait()
 if code:raise RuntimeError('Preview decode failed: '+err)
 return np.asarray(energy),frame_paths,rgb_hist,waveform

def font(size=18):
 return ImageFont.truetype(str(PROJECT/'assets/fonts/NotoSansSC.ttf'),size)

def sheet(rows,destination,columns=4):
 # Rows: [(label,[frame paths])]. Explicit labels make evidence reviewable.
 result=Image.new('RGB',(480*columns,310*len(rows)),(25,25,25));draw=ImageDraw.Draw(result)
 for r,(label,paths) in enumerate(rows):
  draw.text((8,r*310+5),label,font=font(18),fill=(245,244,237))
  for c,path in enumerate(paths):
   if path and Path(path).exists():result.paste(Image.open(path).convert('RGB'),(c*480,r*310+32))
   else:draw.text((c*480+10,r*310+100),'MISSING FRAME',font=font(),fill='red')
 result.save(destination,quality=91,subsampling=0)

def classify_hold(metrics,hashes,count):
 if len(metrics)!=count:return 'FAIL-incomplete-hold-window'
 if len(set(hashes))==1:return 'PASS-exact-decoded-hold'
 # A sparse high-contrast codec edge outlier is not evidence of moving content.
 # These labels request review; neither threshold combination manufactures a pass.
 if all(m['meanDifferenceFromFirst']<=.15 and m['p99DifferenceFromFirst']<=2 for m in metrics):return 'REVIEW-small-decoded-variation-codec-compatible'
 return 'REVIEW-decoded-variation-inconclusive'

def freeze_metrics(video,start,count,width,height):
 args=['ffmpeg','-v','error','-threads','4','-filter_threads','2','-i',str(video),'-map','0:v:0','-vf',f'select=between(n\\,{start}\\,{start+count-1})','-fps_mode','passthrough','-pix_fmt','rgb24','-f','rawvideo','-']
 p=subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 first=previous=None;metrics=[];hashes=[]
 for i in range(count):
  raw=read_exact(p.stdout,width*height*3)
  if len(raw)!=width*height*3:break
  current=np.frombuffer(raw,np.uint8).astype(np.int16);hashes.append(hashlib.sha256(raw).hexdigest())
  if first is None:first=current
  diff=np.abs(current-first)
  metrics.append({'frame':start+i,'meanDifferenceFromFirst':float(diff.mean()),'maxDifferenceFromFirst':int(diff.max()),'p99DifferenceFromFirst':float(np.percentile(diff,99)),'meanConsecutiveDifference':0 if previous is None else float(np.abs(current-previous).mean())})
  previous=current
 err=p.stderr.read().decode(errors='replace');code=p.wait()
 if code:raise RuntimeError('Freeze decode failed: '+err)
 return {'status':classify_hold(metrics,hashes,count),'framesExpected':count,'framesDecoded':len(metrics),'decodedRGBHashes':hashes,'metrics':metrics,'classificationLimits':'Exact decodedRGB identity passes. Mean<=.15/255 and p99<=2/255 only label small variation codec-compatible for REVIEW; max pixel outliers remain reported and never alone imply animation. Other variation is inconclusive REVIEW, not motion failure. Missing frames fail. Source-frame proof and actual image inspection remain separate.'}

def source_freeze_proof(path):
 if not path:return {'status':'PENDING','reason':'No independently verifiable source-frame freeze proof supplied'}
 data=json.loads(Path(path).read_text());result={'manifest':evidence(path),'groups':{}}
 for name,start,count in [('S10',339,20),('final12',1299,12)]:
  records=data.get(name,[]);verified=[]
  for r in records:
   file=Path(r['path']);file=file if file.is_absolute() else Path(path).parent/file
   ok=file.is_file() and sha(file)==r.get('sha256')
   verified.append({'frame':r.get('frame'),'path':str(file),'sha256':r.get('sha256'),'verified':ok})
  indices=[r['frame'] for r in verified]
  passed=len(records)==count and sorted(indices)==list(range(start,start+count)) and all(r['verified'] for r in verified) and len({r['sha256'] for r in verified})==1
  result['groups'][name]={'status':'PASS-source-bytes-identical' if passed else 'FAIL-source-proof','records':verified}
 result['status']='PASS' if all(g['status'].startswith('PASS') for g in result['groups'].values()) else 'FAIL'
 return result

def renderer_source_hashes(path,video):
 if not path or not Path(path).is_file():return {'status':'PENDING','reason':'No renderer PNG-hash sidecar found'}
 data=json.loads(Path(path).read_text());actual_video_hash=sha(video);binding=data.get('video_sha256')==actual_video_hash
 records=data.get('frames',[]);valid_records=all(isinstance(r.get('frame'),int) and re.fullmatch(r'[0-9a-fA-F]{64}',str(r.get('sha256',''))) for r in records)
 unique=len({r.get('frame') for r in records})==len(records)
 result={'manifest':evidence(path),'definition':data.get('definition'),'source':'Renderer hashes of lossless PNG buffers fed directly to encoder; no claim of decoded H264 byte identity.','videoHashBindingVerified':binding,'expectedVideoSha256':data.get('video_sha256'),'actualVideoSha256':actual_video_hash,'recordsStructurallyValid':bool(valid_records and unique),'groups':{}}
 for name,start,count in [('S10',339,20),('final12',1299,12)]:
  group=[r for r in records if isinstance(r.get('frame'),int) and start<=r['frame']<start+count]
  coverage=sorted(r['frame'] for r in group)==list(range(start,start+count))
  identical=bool(group) and len({r['sha256'] for r in group})==1
  passed=binding and valid_records and unique and coverage and identical
  result['groups'][name]={'status':'PASS-renderer-source-PNG-hold' if passed else 'FAIL-renderer-source-hold-proof','contiguousWindowCoverageVerified':coverage,'identicalSourceHashes':identical,'records':group}
 result['status']='PASS' if all(g['status'].startswith('PASS') for g in result['groups'].values()) else 'FAIL'
 return result

def scene_scores(video,out,shots):
 raw=run(['ffmpeg','-v','error','-threads','4','-filter_threads','2','-i',str(video),'-map','0:v:0','-vf',"select=gte(scene\\,0),metadata=print:key=lavfi.scene_score:file=-",'-an','-f','null','-'])
 (out/'scene_scores_raw.txt').write_text(raw)
 scores=[];frame=None;t=None
 for line in raw.splitlines():
  found=re.search(r'frame:\s*(\d+).*pts_time:([\d.eE+-]+)',line)
  if found:frame=int(found.group(1));t=float(found.group(2))
  if line.startswith('lavfi.scene_score=') and frame is not None:scores.append({'frame':frame,'ptsTime':t,'score':float(line.split('=')[1])})
 spectrum=[]
 for threshold in SCENE_THRESHOLDS:
  detected=[round(x['ptsTime']*FPS) for x in scores if x['score']>=threshold]
  matches=[]
  for s in shots[1:]:
   near=min(detected,key=lambda f:abs(f-s['f0'])) if detected else None
   exempt=s['id']=='S38'
   matches.append({'shot':s['id'],'expectedFrame':s['f0'],'nearestDetectedFrame':near,'lagFrames':None if near is None else near-s['f0'],'withinOneFrame':near is not None and abs(near-s['f0'])<=1,'exempt':exempt,'exemption':'S37-to-S38 intentionally continuous pull-out' if exempt else None,'transitionNote':'S20-to-S21 white flash spans684–686; first visible postwhite687 is valid+1, no invented difference onwhite' if s['id']=='S21' else None})
  expected=[s['f0'] for s in shots[1:]]
  extra=[f for f in detected if min(abs(f-e) for e in expected)>1]
  spectrum.append({'threshold':threshold,'detectedFrames':detected,'boundaries':matches,'extraDetections':extra,'missedNonexempt':sum(not m['withinOneFrame'] and not m['exempt'] for m in matches)})
 result={'status':'EVIDENCE-REVIEW','fixedThresholds':list(SCENE_THRESHOLDS),'thresholdPolicy':'Spectrum fixed before final render; no threshold chosen to force coverage. Grain/motion can create extra detections. Scores are transition evidence, separate from EDL/shot presence and manual review.','scores':scores,'spectrum':spectrum}
 dump(out/'scene_changes.json',result);return result

def lag_statistics(envelope,visual,out):
 n=min(len(envelope),len(visual));a=np.asarray(envelope[:n],float);v=np.asarray(visual[:n],float)
 def correlate(x,y,maxlag):
  x=x-x.mean();y=y-y.mean();den=np.linalg.norm(x)*np.linalg.norm(y)
  if den<1e-12:return {'valid':False,'reason':'Constant/empty signal'}
  corr=signal.correlate(y,x,mode='full',method='fft')/den;lags=signal.correlation_lags(len(y),len(x),mode='full');take=np.abs(lags)<=maxlag;corr=corr[take];lags=lags[take];peak=int(np.argmax(corr))
  return {'valid':True,'lagFrames':int(lags[peak]),'peakNormalizedCorrelation':float(corr[peak]),'lags':lags.tolist(),'normalizedCrossCorrelation':corr.tolist()}
 global_lag=correlate(a,v,15);windows=[]
 for start in range(0,n,120):
  stop=min(start+120,n)
  if stop-start<60:continue
  windows.append({'startFrame':start,'endFrameExclusive':stop,**correlate(a[start:stop],v[start:stop],15)})
 lags=[w['lagFrames'] for w in windows if w['valid']];median=float(np.median(lags)) if lags else None
 result={'status':'PASS-measured-median-only' if median is not None and abs(median)<=1 else 'FAIL-measured-median-lag' if median is not None else 'INDETERMINATE','global':global_lag,'windows':windows,'medianWindowLagFrames':median,'scope':'Actual mono decoded audio RMS in30fps bins versus mean absolute grayscale frame difference at480x270. Nonoverlapping4s windows; final>=2s accepted; lag search±15frames. Positive lag means picture changes follow audio. This correlation of unlike signals is a diagnostic, not proof of creative sync. Raw arrays included; no threshold adjustment or low-score exclusion.','audioEnvelope':a.tolist(),'visualDifference':v.tolist()}
 dump(out/'av_correlation.json',result)
 fig,axes=plt.subplots(3,1,figsize=(14,9));t=np.arange(n)/FPS
 axes[0].plot(t,a/(a.max()+1e-9),label='Audio RMS');axes[0].plot(t,v/(v.max()+1e-9),label='Visual mean difference',alpha=.7);axes[0].legend();axes[0].set(xlabel='Seconds',ylabel='Normalized amplitude')
 if global_lag['valid']:axes[1].plot(global_lag['lags'],global_lag['normalizedCrossCorrelation']);axes[1].axvline(global_lag['lagFrames'],color='coral')
 axes[1].set(xlabel='Lag frames (picture after audio positive)',ylabel='Global normalized correlation')
 axes[2].bar([w['startFrame']/FPS for w in windows if w['valid']],lags,width=3.5);axes[2].axhspan(-1,1,color='green',alpha=.15);axes[2].set(xlabel='Window start seconds',ylabel='Best lag frames')
 fig.tight_layout();fig.savefig(out/'av_correlation.png',dpi=130);plt.close(fig)
 return result

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('video',type=Path)
 parser.add_argument('--out',type=Path,default=PROJECT/'qa/final')
 parser.add_argument('--source-audio',type=Path,default=PROJECT.parent/'first-day.mp3')
 parser.add_argument('--lrc',type=Path,default=PROJECT.parent/'first-day.lrc')
 parser.add_argument('--source-freeze-proof',type=Path)
 parser.add_argument('--source-hashes',type=Path,help='Renderer PNG-hash JSON; default discovers video sibling.source-frame-hashes.json')
 parser.add_argument('--asset-map',type=Path)
 parser.add_argument('--camera-diagnostics',type=Path)
 parser.add_argument('--diagnostic',action='store_true')
 args=parser.parse_args()
 if not args.video.is_file():parser.error('Video absent; no QA pass or placeholder report will be created')
 if not args.source_audio.is_file():parser.error('Original MP3 absent; cannot validate final audio')
 if not args.lrc.is_file():parser.error('LRC absent; cannot build lyric peak evidence')
 out=args.out.resolve();out.mkdir(parents=True,exist_ok=True);run_started=clocktime.time()
 # Invalidate prior summaries before measuring a new input; stale evidence is not a pass.
 for old in [out/'qa.json',out/'qa.md']:
  if old.exists():old.unlink()
 for directory in ['camera','hard_cues']:(out/directory).mkdir(exist_ok=True)
 shots=json.loads((PROJECT/'helper/shots.json').read_text());metadata=probe(args.video);dump(out/'ffprobe.json',metadata)
 streams=metadata.get('streams',[]);video=next((s for s in streams if s['codec_type']=='video'),None);audio=next((s for s in streams if s['codec_type']=='audio'),None)
 if not video:raise RuntimeError('Input has no video stream')
 duration=float(metadata['format']['duration']);width,height=video['width'],video['height'];rate=float(Fraction(video['avg_frame_rate']));frames=int(video.get('nb_read_frames',video.get('nb_frames',0)));bitrate=int(video.get('bit_rate',0))
 checks={}
 def check(name,ok,actual,expected):checks[name]={'status':'PASS' if ok else 'FAIL','actual':actual,'expected':expected}
 check('resolution',width==1920 and height==1080,[width,height],[1920,1080]);check('fps',abs(rate-FPS)<1e-6,rate,FPS);check('frames',frames==EXPECTED_FRAMES,frames,EXPECTED_FRAMES);check('duration',abs(duration-43.70)<=.0200001,duration,'43.70±.02seconds');check('codec',video['codec_name']=='h264',video['codec_name'],'h264');check('pixelFormat',video['pix_fmt']=='yuv420p',video['pix_fmt'],'yuv420p');check('videoBitrate',bitrate>=15_000_000,bitrate,'>=15000000bps video stream (not container/audio)');check('shotManifest',len(shots)==52 and shots[0]['f0']==0 and shots[-1]['f1']==1311 and all(a['f1']==b['f0'] for a,b in zip(shots,shots[1:])),len(shots),'52 contiguous prescribed intervals ending1311; content review separate')
 try:
  run(['ffmpeg','-v','error','-xerror','-threads','4','-i',str(args.video),'-map','0','-f','null','-']);checks['fullDecode']={'status':'PASS','actual':'Full FFmpeg decode completed with-xerror','expected':'No decoder errors'}
 except RuntimeError as exc:checks['fullDecode']={'status':'FAIL','error':str(exc)}
 lyric=[]
 for line in args.lrc.read_text().splitlines():
  m=re.match(r'\[(\d+):(\d+(?:\.\d+)?)\](.*)',line)
  if m:lyric.append((int(m.group(1))*60+float(m.group(2)),m.group(3)))
 shot_samples={s['id']:[round(s['f0']+(s['f1']-s['f0']-1)*u) for u in [0,1/3,2/3,1]] for s in shots}
 camera_samples={s['id']:[s['f0'],round((s['f0']+s['f1']-1)/2),s['f1']-1] for s in shots}
 type_frames=[]
 for i,(start,text) in enumerate(lyric):
  end=lyric[i+1][0] if i+1<len(lyric) else 43.7
  # 75% into each LRC interval is a reproducible review candidate, not proven typography peak.
  type_frames.append((max(0,min(EXPECTED_FRAMES-1,round((start+.75*(end-start))*FPS))),text,start))
 selected={f for group in list(shot_samples.values())+list(camera_samples.values()) for f in group}|{f for f,_,_ in type_frames}|{339,348,358,1299,1304,1310}
 print('QA: extracting actual-video preview evidence',flush=True)
 visual,frame_paths,rgb_hist,waveform=previews(args.video,out,selected)
 check('decodedPreviewFrames',len(visual)==1311,len(visual),1311)
 contacts=[]
 for offset in range(0,len(shots),13):
  path=out/f'contact_sheet_{offset//13+1:02d}.jpg';rows=[(f"{s['id']}  f{s['f0']}–{s['f1']-1}  {s['kind']}",[frame_paths.get(f) for f in shot_samples[s['id']]]) for s in shots[offset:offset+13]];sheet(rows,path);contacts.append(str(path))
 camera_files=[]
 for s in shots:
  path=out/'camera'/f"{s['id']}.jpg";sheet([(s['id']+' | '+s['cam'],[frame_paths.get(f) for f in camera_samples[s['id']]])],path,3);camera_files.append(str(path))
 type_rows=[]
 for offset in range(0,len(type_frames),4):
  group=type_frames[offset:offset+4];type_rows.append((' | '.join(f'{text} f{f}' for f,text,_ in group),[frame_paths.get(f) for f,_,_ in group]))
 sheet(type_rows,out/'typography_peak_candidates.jpg')
 cue_evidence=[]
 for name,time in HARD_CUES:
  f=round(time*FPS);path=out/'hard_cues'/f'{name}-f{f}.png'
  if path.exists():path.unlink()
  run(['ffmpeg','-v','error','-threads','4','-filter_threads','2','-i',str(args.video),'-vf',f'select=eq(n\\,{f})','-frames:v','1','-y',str(path)])
  if not path.is_file():raise RuntimeError(f'Missing hard cue output {name}')
  cue_evidence.append({'name':name,'requestedSeconds':time,'frame':f,'actualGridSeconds':f/FPS,**evidence(path),'sourceResolution':[width,height]})
 print('QA: full-resolution hold measurements',flush=True)
 for name,indices in [('S10',[339,348,358]),('final12',[1299,1304,1310])]:sheet([(name+' decoded hold: start/mid/end',[frame_paths.get(f) for f in indices])],out/(name+'_hold_strip.jpg'),3)
 holds={'S10':freeze_metrics(args.video,339,20,width,height),'final12':freeze_metrics(args.video,1299,12,width,height)}
 hash_sidecar=args.source_hashes or args.video.with_suffix('.source-frame-hashes.json')
 if args.source_hashes and not args.source_hashes.is_file():raise RuntimeError('Explicit source-hashes sidecar absent')
 proof=renderer_source_hashes(hash_sidecar,args.video) if hash_sidecar.is_file() else source_freeze_proof(args.source_freeze_proof)
 if hash_sidecar.is_file():checks['rendererSourceHashBinding']={'status':'PASS' if proof['videoHashBindingVerified'] and proof['recordsStructurallyValid'] else 'FAIL','videoHashBindingVerified':proof['videoHashBindingVerified'],'recordsStructurallyValid':proof['recordsStructurallyValid']}
 dump(out/'hold_metrics.json',{'decoded':holds,'sourceProof':proof})
 for name,result in holds.items():
  source_pass=proof.get('groups',{}).get(name,{}).get('status','').startswith('PASS')
  checks['hold_'+name]={'status':'PASS' if result['status'].startswith('PASS') or (result['status']=='REVIEW-small-decoded-variation-codec-compatible' and source_pass) else 'REVIEW' if result['status'].startswith('REVIEW') else 'FAIL','decodedClassification':result['status'],'sourceProofVerified':source_pass,'sourceProofClassification':proof.get('groups',{}).get(name,{}).get('status','PENDING'),'scope':'Source proof establishes a source hold independently. Decoded variation alone does not establish motion; substantial decoded variation still requires image review.'}
 print('QA: fixed-spectrum scene scores and audio hashes',flush=True)
 scenes=scene_scores(args.video,out,shots);checks['sceneDetectionCoverage']={'status':'EVIDENCE-REVIEW','fixedThresholds':list(SCENE_THRESHOLDS),'spectrum':[{'threshold':t['threshold'],'missedNonexempt':t['missedNonexempt'],'extraDetections':len(t['extraDetections'])} for t in scenes['spectrum']],'scope':'Evidence/warning only; separate from EDL shot-presence and manual transition review'}
 src_packets=packet_data(args.source_audio);dst_packets=packet_data(args.video) if audio else[];dump(out/'source_audio_packets.json',src_packets);dump(out/'final_audio_packets.json',dst_packets)
 src_hashes=[p.get('data_hash') for p in src_packets];dst_hashes=[p.get('data_hash') for p in dst_packets]
 check('originalMP3PacketPayloads',bool(src_hashes) and all(src_hashes) and src_hashes==dst_hashes and audio is not None and audio['codec_name']=='mp3',{'sourcePacketCount':len(src_hashes),'finalPacketCount':len(dst_hashes),'finalCodec':audio['codec_name'] if audio else None,'firstDifferentPacket':next((i for i,(a,b) in enumerate(zip(src_hashes,dst_hashes)) if a!=b),None)},'Same complete MP3 packetSHA256 sequence; container metadata/PTS may differ')
 original=decode_audio(args.source_audio)
 if audio:
  actual=decode_audio(args.video);align=alignment(original,actual,11025);checks['decodedAudioAlignment']=align
  envelope=np.array([np.sqrt(np.mean(actual[round(i*11025/FPS):round((i+1)*11025/FPS)].astype(float)**2)) if round(i*11025/FPS)<len(actual) else 0 for i in range(len(visual))]);av=lag_statistics(envelope,visual,out);checks['audioVisualWindowMedian']={k:av[k] for k in ['status','medianWindowLagFrames','scope']}
 else:
  align={'status':'FAIL','reason':'No audio stream'};av={'status':'FAIL','reason':'No audio stream'};checks['decodedAudioAlignment']=align;checks['audioVisualWindowMedian']=av
 dump(out/'decoded_audio_alignment.json',align)
 expected_durations=np.array([s['f1']-s['f0'] for s in shots]);detected_sets=[]
 for entry in scenes['spectrum']:
  boundaries=sorted(set([0]+[f for f in entry['detectedFrames'] if 0<f<frames]+[frames]));detected_sets.append((entry['threshold'],np.diff(boundaries)))
 max_duration=max([int(expected_durations.max())]+[int(ds.max(initial=0)) for _,ds in detected_sets]);bins=np.arange(0,max_duration+11,10)
 fig,axes=plt.subplots(1,2,figsize=(13,5));axes[0].hist(expected_durations,bins=bins,alpha=.6,label='Prescribed shots.json')
 for threshold,ds in detected_sets:axes[0].hist(ds,bins=bins,histtype='step',label=f'Detected threshold{threshold:.2f}')
 axes[0].legend();axes[0].set(xlabel='Duration frames',ylabel='Count');axes[1].bar(range(len(shots)),expected_durations);axes[1].set(xlabel='Shot index in manifest',ylabel='Duration frames');fig.tight_layout();fig.savefig(out/'duration_histogram.png',dpi=130);plt.close(fig)
 duration_data={'expectedShotDurationsFrames':expected_durations.tolist(),'detectedSceneIntervalSpectrum':[{'threshold':threshold,'intervalsFrames':ds.tolist()} for threshold,ds in detected_sets],'sourceManifest':evidence(PROJECT/'helper/shots.json'),'scope':'Manifest is edit intent; fixed-threshold scene interval comparison does not establish that52 intended shot contents actually appear.'};dump(out/'duration_comparison.json',duration_data)
 fig,axes=plt.subplots(1,2,figsize=(13,5));
 for c,color in enumerate(['red','green','blue']):axes[0].plot(rgb_hist[c],color=color,alpha=.7)
 axes[0].set(xlabel='RGB value0–255',ylabel='Pixels in1sample/second');axes[1].imshow(np.log1p(waveform),origin='lower',aspect='auto',cmap='magma',extent=[0,480,0,255]);axes[1].set(xlabel='Image horizontal position480px',ylabel='Luma0–255');fig.tight_layout();fig.savefig(out/'scopes.png',dpi=130);plt.close(fig)
 optional={}
 for name,path in [('assetMap',args.asset_map),('cameraDiagnostics',args.camera_diagnostics)]:
  if path:optional[name]=evidence(path) if path.is_file() else {'status':'MISSING','path':str(path)}
 failed=[name for name,c in checks.items() if c['status'].startswith('FAIL')];review=[name for name,c in checks.items() if c['status'].startswith(('REVIEW','INDETERMINATE','EVIDENCE-REVIEW'))]
 report={'status':'DIAGNOSTIC-NOT-DELIVERY' if args.diagnostic else 'TECHNICAL-FAIL' if failed else 'TECHNICAL-REVIEW' if review else 'TECHNICAL-CHECKS-PASS-MANUAL-REVIEW-PENDING','diagnostic':args.diagnostic,'input':evidence(args.video),'sourceAudio':evidence(args.source_audio),'checks':checks,'failedChecks':failed,'reviewChecks':review,'hardCues':cue_evidence,'contactSheets':contacts,'cameraStrips':camera_files,'typographySamples':[{'frame':f,'text':text,'lrcStart':start} for f,text,start in type_frames],'manualReview':[{'item':x,'status':'PENDING'} for x in MANUAL],'optionalEvidence':optional,'scope':'No model identity, typography correctness, camera faithfulness, normal playback or aesthetic pass is inferred from file metrics. Contact sheets are evidence awaiting inspection.'}
 report['evidence']=[evidence(p) for p in sorted(out.rglob('*')) if p.is_file() and p.stat().st_mtime>=run_started-1 and p.name not in ['qa.json','qa.md']]
 dump(out/'qa.json',report)
 lines=['# Final-media QA evidence','',f"Status: **{report['status']}**",'',f"Input: `{args.video.resolve()}`",f"SHA256: `{report['input']['sha256']}`",'', '## Measured technical checks','', '| Check | Result |','|---|---|']
 lines.extend(f'| {name} | {c["status"]} |' for name,c in checks.items())
 lines+=['','Full measurements, raw scores, per-window lags, source packet hashes, file paths and evidenceSHA256 values are in [qa.json](qa.json).', '', '## Evidence for inspection','', '- Four-frame-per-shot contact sheets: '+', '.join(f'[sheet{i+1}]({Path(path).name})' for i,path in enumerate(contacts)), '- Three-frame camera strips:52 actual-video images in `camera/`.', '- Six full-input-resolution cues in `hard_cues/`; resolution is reported and cannot exceed the input.', '- [Typography candidate frames](typography_peak_candidates.jpg):75% into each LRC interval; these are reproducible candidates, not a claim of true text peak.', '- [Audio/visual cross-correlation](av_correlation.png) and [raw values](av_correlation.json).', '- [Scene detection scores](scene_changes.json), fixed thresholds0.03/0.10/0.30; S37→S38 continuous transition explicitly exempt.', '- [Duration histogram](duration_histogram.png) and [scopes](scopes.png).', '- [Hold differences](hold_metrics.json): strict decoded holds distinguished from loss-compatible low variation; uncertain holds are not silently passed.', '', '## Manual approval remains pending','']
 lines.extend('- [ ] '+item for item in MANUAL)
 if args.diagnostic:lines+=['','This is a diagnostic timing-card input. Expected format/content failures are preserved; this report does not approve a final film.']
 (out/'qa.md').write_text('\n'.join(lines)+'\n')
 print(json.dumps({'status':report['status'],'failedChecks':failed,'reviewChecks':review,'report':str(out/'qa.json')},ensure_ascii=False),flush=True)
 return 1 if failed else 0

if __name__=='__main__':
 try:sys.exit(main())
 except (RuntimeError,OSError,ValueError,KeyError) as exc:
  print('QA ERROR: '+str(exc),file=sys.stderr);sys.exit(2)
