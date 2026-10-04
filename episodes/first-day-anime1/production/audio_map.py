from pathlib import Path
import json,re,subprocess
import numpy as np
import librosa
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
y,sr=librosa.load(ROOT/'first-day.mp3',sr=22050)
hop=128
onset_env=librosa.onset.onset_strength(y=y,sr=sr,hop_length=hop)
onsets=librosa.onset.onset_detect(onset_envelope=onset_env,sr=sr,hop_length=hop,backtrack=False,units='time')
tempo,beats=librosa.beat.beat_track(onset_envelope=onset_env,sr=sr,hop_length=hop,start_bpm=86,trim=False,units='time')
lyrics=[]
for line in (ROOT/'first-day.lrc').read_text().splitlines():
 m=re.match(r'\[(\d+):(\d+\.\d+)\](.*)',line)
 if m:
  t=int(m[1])*60+float(m[2]);lyrics.append(dict(t=t,frame=int(t*30+.5),text=m[3]))
# Listed shot boundaries, with lyric anchors locked; other cuts seek nearest onset within 3 frames.
starts=[0,1.05,2.84,4.23,5.23,6.63,7.5,8.4,9.45,10.15,10.57,10.92,11.27,11.92,12.62,13.63,14.64,15.68,16.37,17.61,18.65,19.67,20.7,22.7,23.75,25.45,26.15,26.5,27.2,27.55,27.94,28.55,29.6,30.68,34.21]+[37.07+i*.3487 for i in range(8)]+[39.9]
anchors={v['frame'] for v in lyrics}
shots=[]
for i,t in enumerate(starts):
 f=int(t*30+.5); nearest=float(onsets[np.argmin(abs(onsets-t))]);nf=int(nearest*30+.5)
 # Lyric anchors stay fixed; all other cuts snap only within three frames.
 snap=f not in anchors and abs(nf-f)<=3
 shots.append(dict(id=f'S{i+1:02}',target=t,frame=nf if snap else f,onset=nearest,snapped=snap,lyric_anchor=f in anchors))
for i,s in enumerate(shots):s.update(end_frame=shots[i+1]['frame'] if i+1<len(shots) else 1311)
rms=librosa.feature.rms(y=y,frame_length=512,hop_length=hop)[0];rt=librosa.frames_to_time(np.arange(len(rms)),sr=sr,hop_length=hop)
gap=(rt>=11.45)&(rt<=11.92);prior=(rt>=10.9)&(rt<11.4)
report=dict(duration=len(y)/sr,fps=30,total_frames=1311,detected_tempo=float(np.asarray(tempo).ravel()[0]),beats=beats.tolist(),bars_estimated=[2.82+i*2.79 for i in range(15)],onsets=onsets.tolist(),lyrics=lyrics,shots=shots,stop_time=dict(window=[11.45,11.92],rms_mean=float(rms[gap].mean()),preceding_rms_mean=float(rms[prior].mean()),rms_drop_fraction=float(1-rms[gap].mean()/rms[prior].mean())))
best=(-1,None,None)
flux_times=librosa.frames_to_time(np.arange(len(onset_env)),sr=sr,hop_length=hop)
for period in np.linspace(.68,.72,401):
 for phase in np.linspace(0,period,81):
  grid=np.arange(phase,43.4,period);grid=grid[(grid>5.8)&~((grid>11.35)&(grid<11.93))]
  score=float(np.mean(np.array([np.interp(grid+off,flux_times,onset_env) for off in [-.018,0,.018]]).max(axis=0)))
  if score>best[0]:best=score,float(period),float(phase)
period,phase=best[1:];first=phase+round((2.82-phase)/period)*period
report['regular_grid_fit']={'score':best[0],'quarter_period':period,'phase':phase,'bpm':60/period}
report['beats_regular']=np.arange(phase,43.7,period).tolist()
report['bars']=[round(first+i*period*4,6) for i in range(16) if first+i*period*4<43.7]
report['beat_grid_note']='Preserve lyric anchors; snap all other boundaries to observed onsets only within three frames.'
assert len(shots)==44 and all(s['frame']<s['end_frame'] for s in shots)
(ROOT/'timing.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
fig,axs=plt.subplots(2,1,figsize=(17,6),gridspec_kw={'height_ratios':[2,1]})
t=np.arange(len(y))/sr;axs[0].plot(t[::100],y[::100],color='#D97757',lw=.5)
for s in shots:axs[0].axvline(s['frame']/30,color='#141413',alpha=.25,lw=.5)
for ax in axs:ax.axvspan(11.45,11.92,color='#788C5D',alpha=.3);ax.set_xlim(0,43.7)
axs[1].plot(rt,rms,color='#141413');axs[1].vlines(onsets,0,float(rms.max())*.25,color='#6A9BCC',lw=.5)
axs[0].set_title('FIRST DAY — waveform, 44 cuts, detected onsets and stop-time window');axs[1].set_xlabel('seconds')
fig.tight_layout();fig.savefig(ROOT/'assets'/'timing.png',dpi=140)
print(json.dumps({k:report[k] for k in ['duration','detected_tempo','stop_time']},indent=2))
