from pathlib import Path
import subprocess,json,hashlib,numpy as np
from PIL import Image,ImageDraw
r=Path(__file__).resolve().parents[1];frames=Path('work/first-day-animation/frames');out=r/'out';video=out/'opus55_first_day.mp4'
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(video)]));v=next(s for s in probe['streams']if s['codec_type']=='video');a=next(s for s in probe['streams']if s['codec_type']=='audio')
def packets(p):
 data=json.loads(subprocess.check_output(['ffprobe','-v','error','-select_streams','a:0','-show_packets','-show_data_hash','sha256','-show_entries','packet=data_hash','-of','json',str(p)]));return[x['data_hash']for x in data['packets']]
src=packets(r/'first-day.mp3');dst=packets(video);luma=[]
for i in range(1311):
 p=frames/f'{i:05d}.jpg';im=np.asarray(Image.open(p).convert('RGB').resize((160,90))).astype(float)/255;luma.append(float(np.mean(im@np.array([.2126,.7152,.0722]))))
checks={'width':v['width']==1920,'height':v['height']==1080,'fps':v['r_frame_rate']=='30/1','frames':int(v['nb_frames'])==1311,'duration':abs(float(v['duration'])-43.7)<.001,'audio_codec_unchanged':a['codec_name']=='mp3','audio_packet_payloads_identical':src==dst,'no_all_black_frames':min(luma)>.005,'title_frame':358,'silence_frames':[336,358]}
report={'checks':checks,'video':{'codec':v['codec_name'],'duration':v['duration'],'frames':v['nb_frames'],'fps':v['r_frame_rate']},'audio':{'codec':a['codec_name'],'source_packets':len(src),'output_packets':len(dst),'encoded_packet_hashes_identical':src==dst},'luminance':{'min':min(luma),'act1_mean':float(np.mean(luma[:336])),'silence_mean':float(np.mean(luma[336:358])),'act2_mean':float(np.mean(luma[358:920])),'act3_mean':float(np.mean(luma[920:]))},'review_limit':'Contact sheets verify sampled imagery. They do not establish normal-speed perceptual motion or musical feel.'}
(out/'qa/technical-report.json').write_text(json.dumps(report,indent=2));(out/'qa/luminance.json').write_text(json.dumps(luma));
import matplotlib;matplotlib.use('Agg');import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(12,3));ax.plot(np.arange(1311)/30,luma,color='#D97757',linewidth=.8);ax.axvspan(11.2,11.933,color='#141413',alpha=.16);ax.set(xlabel='Time (seconds)',ylabel='Mean luminance',ylim=(0,1));ax.axvline(11.933,color='#788C5D');fig.tight_layout();fig.savefig(out/'qa/luminance.png',dpi=140);plt.close(fig)
print(json.dumps(report,indent=2));assert all(x for x in checks.values()if isinstance(x,bool))
