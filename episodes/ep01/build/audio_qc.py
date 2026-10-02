"""Validate the delivered mix/conditioning timeline and report measurable limits."""
import hashlib,json,subprocess
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[3];W=ROOT/'work/ep01/audio'
story=json.loads((ROOT/'episodes/ep01/build/story.json').read_text());report=json.loads((W/'master_mix.report.json').read_text());subs=json.loads((W/'subtitles.json').read_text());lips=json.loads((W/'lipsync_manifest.json').read_text());shots={s['id']:s for s in story['shots']}
def probe(path):return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(path)]))
def read(path):return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(path),'-f','f32le','-acodec','pcm_f32le','-']),np.float32).reshape(-1,2)
for path in W.glob('master_mix*.wav'):
 p=probe(path);s=p['streams'][0];assert int(s['sample_rate'])==48000 and s['channels']==2 and abs(float(p['format']['duration'])-230)<1/48000,path
for s in subs:
 sh=shots[s['shot_id']];assert sh['start_frame']<=s['start_frame']<s['end_frame']<=sh['end_frame'] and sh['kind']!='title',s
for s in lips:
 p=probe(ROOT/s['path']);st=p['streams'][0];assert int(st['sample_rate'])==48000 and st['channels']==2 and abs(float(p['format']['duration'])-s['frames']/24)<1/48000,s
x=read(W/'master_mix.wav');assert np.isfinite(x).all() and not (np.abs(x)>=1).any()
q=x[109*48000:119*48000];zeros=int((np.max(np.abs(q),axis=1)==0).sum());assert zeros==0
for bus in ['action','music']:
 b=read(W/f'master_mix.{bus}.wav');assert np.max(np.abs(b[109*48000:119*48000]))<1e-8,bus
assert len(report['lines'])==len(subs)==len(lips)==26
assert not report['placeholders'] and not report['warnings']
assert report['master']['TP']<=-1 and abs(report['master']['I']+18)<=.5 and report['master']['LRA']<=16
qa={'duration_seconds':len(x)/48000,'sample_rate':48000,'channels':2,'master_sha256':hashlib.sha256((W/'master_mix.wav').read_bytes()).hexdigest(),'dialogue_lines':26,'subtitles':26,'lipsync_inputs':26,'active_lipsync_scene_inputs':sum(a['use_for_lipsync'] for a in lips),'subtitle_bounds_pass':True,'lipsync_lengths_pass':True,'finite_samples':True,'fullscale_samples':0,'master':report['master'],'quiet_hold_rms_dbfs':round(float(20*np.log10(np.sqrt(np.mean(q*q))+1e-12)),2),'quiet_hold_exact_zero_frames':zeros,'action_music_stop_exact_109s':True,'last_sample_abs':float(np.abs(x[-1]).max()),'stereo_correlation':round(float(np.corrcoef(x.T)[0,1]),4),'missing_sources':[],'warnings':[],'issues':[],'listening_review':'Not performed. Human playback required for voice naturalness, generated-foley recognition and artistic balance.','post_edit_asr':'24 of26 post-edit isolated utterances match exactly; D24 has only homophone spellings. D04 small-ASR bowl/ball ambiguity is mid-line, whereas both raw takes transcribe bowl. No dropped edge words detected.'}
(W/'technical_qc.json').write_text(json.dumps(qa,indent=2));print(json.dumps(qa,indent=2))
