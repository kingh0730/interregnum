from pathlib import Path
import subprocess,json,hashlib
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'assets/first-day.wav'
pcm=subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-f','s24le','-'])
f32=subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-ac','1','-f','f32le','-'])
x=np.frombuffer(f32,dtype='<f4'); sr=44100; hop=441; n=2048
frames=np.array([np.pad(x[i:i+n],(0,max(0,n-len(x[i:i+n])))) for i in range(0,len(x),hop)])
spec=np.abs(np.fft.rfft(frames*np.hanning(n),axis=1)); freqs=np.fft.rfftfreq(n,1/sr)
features={'rms':np.sqrt(np.mean(frames**2,axis=1))}
for name,a,b in [('low',30,220),('mid',220,2400),('high',2400,16000)]:features[name]=np.sqrt(np.mean(spec[:,(freqs>=a)&(freqs<b)]**2,axis=1))
for k,v in features.items():features[k]=np.clip(v/(np.percentile(v,97)+1e-9),0,1).round(5).tolist()
flux=np.maximum(0,np.diff(spec,axis=0,prepend=spec[:1])).sum(axis=1); flux/=np.percentile(flux,98)
onsets=[]
for i in range(2,len(flux)-2):
 if flux[i]>0.35 and flux[i]>=max(flux[i-2:i+3]) and (not onsets or i/100-onsets[-1][0]>.10):onsets.append([round(i/100,3),round(float(min(1,flux[i])),4)])
anchors=[0,170,314,494,715,878,1057,1180,1362,1527,1713,1841,2053,2224,2394,2621]
lyrics=['你说活在明天活在期待','不如活得今天很自在','我说我懂了会不会太快','未来第一天要展开','第一天我存在','第一次呼吸畅快','站在地上的脚踝','因为你而有真实感','第一天我存在','第一次能飞起来','爱是腾空的魔幻','第一天的纯真色彩它总是','永远那么灿烂','永远那么灿烂','永远那么灿烂']
data={'duration':len(x)/sr,'sample_rate':sr,'channels':2,'bits_per_sample':24,'samples_per_channel':len(x),'pcm_s24le_sha256':hashlib.sha256(pcm).hexdigest(),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'fps':100,'features':features,'onsets':{'spectral_flux':onsets},'lyrics':[{'start_frame':a,'end_frame':b,'text':t} for a,b,t in zip(anchors,anchors[1:],lyrics)],'alignment':'supplied line anchors; syllable alignment and vocal offset unverified','note':'Full-mix spectral bands, not separated vocal or drum stems. No BPM claimed.'}
(ROOT/'assets/audio-analysis.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')))
print(json.dumps({k:v for k,v in data.items() if k not in ('features','onsets','lyrics')},indent=2))
