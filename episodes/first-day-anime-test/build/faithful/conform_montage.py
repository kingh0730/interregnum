"""Resolve the eighth-note montage against measured multiband transients.
Lyric anchors are immutable; all adjustments are limited to three target frames.
"""
from pathlib import Path
import json,hashlib
import librosa,numpy as np
from scipy.signal import find_peaks
R=Path(__file__).resolve().parents[4];E=R/'episodes/first-day-anime-test';S=Path(__file__).parent;W=R/'work/first-day-anime-test/faithful';timing=json.loads((E/'timing.json').read_text());timeline=json.loads((E/'build/timeline.json').read_text());y,sr=librosa.load(E/'first-day.mp3',sr=22050);hop=110;mag=np.abs(librosa.stft(y,n_fft=1024,hop_length=hop));freq=librosa.fft_frequencies(sr=sr,n_fft=1024);candidates=[dict(time=float(t),band='original full-band flux') for t in timing['onsets'] if 36.9<t<40]
for lo,hi in [(25,160),(150,2000),(2000,10000),(6000,10000)]:
 m=mag[(freq>=lo)&(freq<hi)];flux=np.maximum(0,np.diff(np.log1p(m),axis=1)).mean(0);peaks,_=find_peaks(flux,distance=18,prominence=np.percentile(flux,65)*.8)
 candidates.extend(dict(time=float((i+1)*hop/sr),band=f'{lo}-{hi} Hz flux') for i in peaks if 36.9<(i+1)*hop/sr<40)
changes=[]
for s in timeline['shots'][36:43]:
 target=s['target_start'];c=min(candidates,key=lambda c:abs(c['time']-target));frame=round(c['time']*30);before=s['start_frame']
 if abs(frame-round(target*30))<=3:s['start_frame']=frame
 changes.append(dict(shot=s['id'],target=target,previous_frame=before,frame=s['start_frame'],onset=c['time'],band=c['band'],deviation_frames=s['start_frame']-round(target*30)))
for i,s in enumerate(timeline['shots']):
 s['end_frame']=timeline['shots'][i+1]['start_frame'] if i<43 else 1311;s['duration']=(s['end_frame']-s['start_frame'])/30
 assert s['end_frame']>s['start_frame'] and abs(s['start_frame']-round(s['target_start']*30))<=3
for l in timing['lyrics']:
 anchor=next((s for s in timeline['shots'] if abs(s['target_start']-l['time'])<.00001),None)
 if anchor:assert anchor['start_frame']==l['frame']
(S/'timeline.json').write_text(json.dumps(timeline,ensure_ascii=False,indent=2)+'\n');(W/'data.json').write_text(json.dumps({'shots':timeline['shots'],'lyrics':timing['lyrics']},ensure_ascii=False));(S/'montage-onsets.json').write_text(json.dumps({'audio_sha256':hashlib.sha256((E/'first-day.mp3').read_bytes()).hexdigest(),'method':'Positive log-spectral flux, 1024 samples / 110-sample hop; per-band peaks separated >=90ms. Used only to resolve the explicitly onset-snapped eighth-note montage.','changes':changes,'candidates':candidates},indent=2)+'\n');print(changes)
