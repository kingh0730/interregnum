"""Objective source QA, never a substitute for human listening."""
import json,subprocess,sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'tools/audio'))
import voice_design as vd
w=ROOT/'work/ep01/audio';out={}
for group in ['sfx','music']:
 for p in sorted((w/group).glob('*.mp3')):
  x=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-ac','2','-ar','16000','-f','f32le','-']),np.float32).reshape(-1,2)
  stereo_peak=float(np.max(np.abs(x))); stereo_full=int((np.abs(x)>=1).sum()); correlation=float(np.corrcoef(x.T)[0,1]);x=x.mean(1)
  e=np.sqrt(np.mean(x[:len(x)//1600*1600].reshape(-1,1600)**2,axis=1)+1e-16)
  rec={'duration':len(x)/16000,'peak_dbfs':round(float(20*np.log10(max(stereo_peak,1e-12))),2),'rms_dbfs':round(float(20*np.log10(np.sqrt(np.mean(x*x))+1e-12)),2),'finite':bool(np.isfinite(x).all()),'fullscale_samples':stereo_full,'active_100ms_fraction_rel18db':round(float((e>np.percentile(e,95)*10**(-18/20)).mean()),3)}
  if group=='music':
   trp=w/'transcripts'/f'music_{p.stem}.txt'
   if not trp.exists():trp.write_text(vd.transcript(p))
   rec['asr_text']=trp.read_text().strip();rec['sections_rms_dbfs']=[round(float(20*np.log10(np.sqrt(np.mean(x[int(a*16000):int(b*16000)]**2))+1e-12)),2) for a,b in [(0,50),(50,75),(75,90)]]
   frames=np.lib.stride_tricks.sliding_window_view(x,1024)[::512];power=np.abs(np.fft.rfft(frames*np.hanning(1024),axis=1))**2;f=np.fft.rfftfreq(1024,1/16000);total=power.sum(1)+1e-18
   cent=(power*f).sum(1)/total;roll=f[np.argmax(np.cumsum(power,axis=1)>=.9*total[:,None],axis=1)];active=total>np.percentile(total,95)*.01
   rec.update(stereo_correlation=round(correlation,4),median_spectral_centroid_hz=round(float(np.median(cent[active])),1),median_90pct_rolloff_hz=round(float(np.median(roll[active])),1))
  out[str(p.relative_to(ROOT))]=rec
(w/'source_measurements.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
