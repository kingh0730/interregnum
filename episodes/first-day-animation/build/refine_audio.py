from pathlib import Path
import numpy as np, librosa,json
r=Path(__file__).resolve().parents[1];y,sr=librosa.load(r/'first-day.mp3',sr=22050);h=256
on=librosa.onset.onset_strength(y=y,sr=sr,hop_length=h)
tempo, beats=librosa.beat.beat_track(onset_envelope=on,sr=sr,hop_length=h,start_bpm=172,tightness=100,units='time')
o=librosa.onset.onset_detect(onset_envelope=on,sr=sr,hop_length=h,units='time')
a=json.load(open(r/'assets/audio.json'));a.update(tempo=float(np.asarray(tempo).ravel()[0]),beats=list(map(float,beats)),onsets=list(map(float,o)),analysis_hop=h)
json.dump(a,open(r/'assets/audio.json','w'),indent=2)
s=json.load(open(r/'build/manifest/shots.json'));print(type(s),list(s)[:7]);print('tempo',a['tempo'],'spacing',np.median(np.diff(beats)))
