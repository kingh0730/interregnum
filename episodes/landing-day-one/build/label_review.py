from pathlib import Path
import json,subprocess,hashlib
from PIL import Image,ImageDraw,ImageFont
r=Path(__file__).resolve().parents[1];out=r.parents[1]/'renders/landing-day-one'
source=out/'landing-day-one-1080p60.mp4';target=out/'landing-day-one-labeled-review.mp4'
shots=json.loads((r/'assets/timeline.json').read_text());assert shots[0]['start']==0 and shots[-1]['end']==2621
assert all(a['end']==b['start'] for a,b in zip(shots,shots[1:]))
font='/System/Library/Fonts/Menlo.ttc';large=ImageFont.truetype(font,44);small=ImageFont.truetype(font,31)
cmd=['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s','1920x120','-r','60','-i','pipe:0','-i',str(source),'-filter_complex','[0:v][1:v]vstack=inputs=2[v]','-map','[v]','-map','1:a:0','-frames:v','2621','-c:v','libx264','-preset','fast','-crf','16','-pix_fmt','yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-c:a','copy','-movflags','+faststart','-metadata','title=Landing Day One - scene-labeled review',str(target)]
p=subprocess.Popen(cmd,stdin=subprocess.PIPE);idx=0
for f in range(2621):
 while f>=shots[idx]['end']:idx+=1
 s=shots[idx];im=Image.new('RGB',(1920,120),'#111923');d=ImageDraw.Draw(im)
 d.rectangle((0,116,1919,119),fill='#d9a441')
 d.text((34,29),s['id'],font=large,fill='#ffdf8a')
 d.text((246,19),f"SCENE {s['start']/60:06.3f} - {s['end']/60:06.3f} s",font=small,fill='#edf2f5')
 d.text((246,64),f"FRAMES {s['start']:04d} - {s['end']-1:04d}",font=small,fill='#aebdca')
 d.text((1280,19),f'FRAME {f:04d}',font=small,fill='#edf2f5')
 d.text((1280,64),f'TIME  00:{f/60:06.3f}',font=small,fill='#aebdca')
 if f==773:im.save(r/'proofs/review-label-bar.png')
 p.stdin.write(im.tobytes())
 if f and f%600==0:print(f'{f}/2621',flush=True)
p.stdin.close();assert p.wait()==0
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-of','json',str(target)]));v=next(s for s in probe['streams'] if s['codec_type']=='video');assert int(v['nb_read_frames'])==2621 and v['r_frame_rate']=='60/1'
def audiohash(path):
 raw=subprocess.check_output(['ffmpeg','-v','error','-i',str(path),'-map','0:a:0','-c','copy','-f','adts','-']);return hashlib.sha256(raw).hexdigest()
assert audiohash(source)==audiohash(target)
(r/'build/labeled-review-checks.json').write_text(json.dumps({'frames':2621,'fps':60,'dimensions':[v['width'],v['height']],'labels':len(shots),'label_position':'120px bar above full original image','audio_packets_identical_to_viewing_copy':True},indent=2))
(out/'scene-index.tsv').write_text('scene\tstart_seconds\tend_seconds\tfirst_frame\tlast_frame\n'+''.join(f"{s['id']}\t{s['start']/60:.3f}\t{s['end']/60:.3f}\t{s['start']}\t{s['end']-1}\n" for s in shots))
print(target,flush=True)
