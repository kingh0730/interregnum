from pathlib import Path
import subprocess,json,hashlib,time
r=Path(__file__).resolve().parents[1];repo=r.parents[1];out=repo/'renders/landing-day-one'
silent=out/'landing-day-one-1440p60-silent.mov';master=out/'landing-day-one-1440p60-master.mov';view=out/'landing-day-one-1080p60.mp4';audio=r/'assets/first-day.wav'
def run(args):
 print('Running',args[0],args[-1],flush=True);subprocess.run(args,check=True)
def probe(p,count=False):
 return json.loads(subprocess.check_output(['ffprobe','-v','error']+(['-count_frames'] if count else [])+['-show_streams','-show_format','-of','json',str(p)]))
def pcm(p):return subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-map','0:a:0','-c:a','pcm_s24le','-f','s24le','-'])
def digest(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for chunk in iter(lambda:f.read(8*1024*1024),b''):h.update(chunk)
 return h.hexdigest()
p=probe(silent,True);v=next(s for s in p['streams'] if s['codec_type']=='video');assert int(v['nb_read_frames'])==2621,(v.get('nb_read_frames'),'incomplete silent render')
if not master.exists() or master.stat().st_mtime<silent.stat().st_mtime:
 run(['ffmpeg','-y','-v','error','-i',str(silent),'-i',str(audio),'-map','0:v:0','-map','1:a:0','-c','copy','-map_metadata','-1','-metadata','title=落地第一天 · AI SI - I','-movflags','+faststart',str(master)])
if not view.exists() or view.stat().st_mtime<master.stat().st_mtime:
 run(['ffmpeg','-y','-v','error','-i',str(master),'-map','0:v:0','-map','0:a:0','-vf','scale=1920:1080:flags=lanczos:out_color_matrix=bt709','-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-c:a','aac','-b:a','320k','-ar','44100','-movflags','+faststart','-metadata','title=落地第一天 · AI SI - I',str(view)])
source=json.loads((r/'assets/audio-analysis.json').read_text());raw=pcm(master);pcm_hash=hashlib.sha256(raw).hexdigest();assert pcm_hash==source['pcm_s24le_sha256'];assert len(raw)//6==1925847
report={'source_duration':43.67,'expected_video_frames':2621,'fps':60,'master_pcm_bit_identical':True,'master_pcm_sha256':pcm_hash,'source_pcm_sha256':source['pcm_s24le_sha256'],'samples_per_channel':len(raw)//6,'outputs':{},'review_limits':'Full-speed aesthetic/musicality and p(doom) comparison remain unverified by a human. Technical checks do not certify them.'}
for path,width,height in [(master,2560,1440),(view,1920,1080)]:
 data=probe(path,True);v=next(s for s in data['streams'] if s['codec_type']=='video');a=next(s for s in data['streams'] if s['codec_type']=='audio')
 assert (v['width'],v['height'])==(width,height)
 assert int(v['nb_read_frames'])==2621 and v['r_frame_rate']=='60/1'
 assert all(v.get(k)=='bt709' for k in ['color_space','color_transfer','color_primaries'])
 assert abs(float(a['duration'])-43.67)<.002
 report['outputs'][path.name]={'path':str(path),'bytes':path.stat().st_size,'sha256':digest(path),'video':{k:v.get(k) for k in ['codec_name','profile','width','height','pix_fmt','r_frame_rate','nb_read_frames','duration','color_space','color_transfer','color_primaries']},'audio':{k:a.get(k) for k in ['codec_name','sample_rate','channels','bits_per_sample','duration']}}
(r/'build/delivery-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps({'frames':2621,'master_pcm_bit_identical':True,'outputs':list(report['outputs'])},ensure_ascii=False),flush=True)
