from pathlib import Path
import json, re, shutil, urllib.request, numpy as np, librosa
root=Path(__file__).resolve().parents[1]
for d in ['assets/audio','assets/fonts','assets/logos','assets/keyframes','assets/clips','assets/depth','out/qa']:(root/d).mkdir(parents=True,exist_ok=True)
shutil.copy2(root/'first-day.mp3',root/'assets/audio/first-day.mp3')
y,sr=librosa.load(root/'first-day.mp3',sr=44100,mono=True); hop=1470;n=1311
S=np.abs(librosa.stft(y,n_fft=2048,hop_length=hop));fr=librosa.fft_frequencies(sr=sr,n_fft=2048)
band=lambda lo,hi:S[(fr>=lo)&(fr<hi)].mean(axis=0)
norm=lambda a:(a/(np.percentile(a,98)+1e-9)).clip(0,1)
low,mid,high=map(norm,[band(20,150),band(150,2500),band(2500,12000)])
onset=librosa.onset.onset_strength(y=y,sr=sr,hop_length=hop)
tempo,beats=librosa.beat.beat_track(y=y,sr=sr,hop_length=hop,units='time',start_bpm=172)
onsets=librosa.onset.onset_detect(y=y,sr=sr,hop_length=hop,units='time')
rms=librosa.feature.rms(y=y,hop_length=hop)[0]
f=lambda a:[round(float(v),5) for v in np.pad(a,(0,max(0,n-len(a))))[:n]]
kick=low[:len(onset)]*norm(onset);env=np.maximum.accumulate(np.zeros(n))
for i,k in enumerate(f(kick)):env[i]=max(k,env[i-1]*.82 if i else 0)
env[336:358]=0
json.dump(dict(fps=30,frames=n,sample_rate=sr,decoded_samples=len(y),decoded_duration=len(y)/sr,tempo=float(np.asarray(tempo).ravel()[0]),beats=f(beats)[:len(beats)],onsets=f(onsets)[:len(onsets)],rms=f(norm(rms)),low=f(low),mid=f(mid),high=f(high),onset=f(norm(onset)),kick=f(kick),envelope=f(env)),open(root/'assets/audio.json','w'),indent=2)
lyrics=[]
for line in (root/'first-day.lrc').read_text().splitlines():
 m=re.match(r'\[(\d+):(\d+\.\d+)\](.*)',line)
 if m:lyrics.append(dict(start=int(m[1])*60+float(m[2]),text=m[3]))
for i,l in enumerate(lyrics):l['end']=lyrics[i+1]['start'] if i+1<len(lyrics) else 43.7
json.dump(lyrics,open(root/'assets/lyrics.json','w'),ensure_ascii=False,indent=2)
fonts={'NotoSansSC.ttf':'https://raw.githubusercontent.com/google/fonts/main/ofl/notosanssc/NotoSansSC%5Bwght%5D.ttf','Newsreader.ttf':'https://raw.githubusercontent.com/google/fonts/main/ofl/newsreader/Newsreader%5Bopsz,wght%5D.ttf','JetBrainsMono.ttf':'https://raw.githubusercontent.com/google/fonts/main/ofl/jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf'}
for name,url in fonts.items():
 dest=root/'assets/fonts'/name
 if not dest.exists():urllib.request.urlretrieve(url,dest)
print(json.dumps({'duration':len(y)/sr,'tempo':float(np.asarray(tempo).ravel()[0]),'beat_spacing':float(np.median(np.diff(beats))),'fonts':list(fonts)}))
