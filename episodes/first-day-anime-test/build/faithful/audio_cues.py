from pathlib import Path
import json
import librosa,numpy as np
from scipy.signal import find_peaks
R=Path(__file__).resolve().parents[4];E=R/'episodes/first-day-anime-test';W=R/'work/first-day-anime-test/faithful';y,sr=librosa.load(E/'first-day.mp3',sr=22050);hop=110;s=np.abs(librosa.stft(y,n_fft=1024,hop_length=hop));freq=librosa.fft_frequencies(sr=sr,n_fft=1024);low=s[(freq>=25)&(freq<=150)].sum(axis=0);flux=np.maximum(0,np.diff(low,prepend=low[0]));peaks,_=find_peaks(flux,distance=int(.22*sr/hop),prominence=np.percentile(flux,92)*.60);frames=sorted(set(round(i*hop/sr*30) for i in peaks));frames=[f for f in frames if f<338 or 440<f<1197];(W/'audio-cues.json').write_text(json.dumps({'source':'first-day.mp3','method':'positive 25-150 Hz spectral flux, local peaks separated >=220 ms','kick_frames':frames,'scope':'micro-shake cues only; the supplied soundtrack is not modified'},indent=2));print(len(frames),'low-frequency impact cues')
