"""Assemble frozen final render chunks with supplied song, preserving source audio file."""
from pathlib import Path
import subprocess,json,hashlib
root=Path(__file__).resolve().parents[3];prod=root/'episodes/first-day-mix/production';work=root/'work/first-day-mix/production';dest=root/'renders/first-day-mix';dest.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
frozen=json.loads((prod/'final-render-inputs.json').read_text())
for name,digest in frozen['files'].items():
 if sha(root/name)!=digest:raise SystemExit('Frozen input changed: '+name)
parts=[work/'final-part-a.mp4',work/'final-part-b.mp4']
patch=work/'final-reserved-patch.mp4'
fit22=work/'final-birth22-patch.mp4';fit24=work/'final-birth24-patch.mp4'
for fit in [fit22,fit24]:
 if not fit.exists() or not fit.with_suffix('.mp4.json').exists():raise SystemExit('Birth fit patch not complete: '+str(fit))
meme=work/'final-meme-patch.mp4'
if not meme.exists() or not meme.with_suffix('.mp4.json').exists():raise SystemExit('Meme-label patch not complete')
if not patch.exists() or not patch.with_suffix('.mp4.json').exists():raise SystemExit('Reserved-tile patch not complete')
for p in parts:
 if not p.exists() or not p.with_suffix('.mp4.json').exists():raise SystemExit('Chunk not complete: '+str(p))
con=work/'final-concat.txt';con.write_text(''.join("file '"+str(p)+"'\n" for p in parts))
out=dest/'first-day-mix-final.mp4'
base=work/'final-base-silent.mp4'
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',str(con),'-c','copy',str(base)],check=True)
# Replace exact intervals [494,715) meme ownership and [1883,1922) reserved tile.
filters='[0:v]split=5[a][b][d][e][f];[a]trim=end_frame=494,setpts=PTS-STARTPTS[p0];[b]trim=start_frame=715:end_frame=878,setpts=PTS-STARTPTS[p1];[d]trim=start_frame=935:end_frame=978,setpts=PTS-STARTPTS[p2];[e]trim=start_frame=1031:end_frame=1883,setpts=PTS-STARTPTS[p3];[f]trim=start_frame=1922,setpts=PTS-STARTPTS[p4];[1:v]setpts=PTS-STARTPTS[mp];[2:v]setpts=PTS-STARTPTS[tp];[3:v]setpts=PTS-STARTPTS[f22];[4:v]setpts=PTS-STARTPTS[f24];[p0][mp][p1][f22][p2][f24][p3][tp][p4]concat=n=9:v=1:a=0[v]'
subprocess.run(['ffmpeg','-v','error','-y','-i',str(base),'-i',str(meme),'-i',str(patch),'-i',str(fit22),'-i',str(fit24),'-i',str(root/'episodes/first-day-mix/first-day.wav'),'-filter_complex',filters,'-map','[v]','-map','5:a:0','-c:v','libx264','-preset','fast','-crf','16','-pix_fmt','yuv420p','-r','60','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-c:a','aac','-b:a','320k','-af','apad=pad_dur=0.013333333','-t','43.683333333','-movflags','+faststart','-metadata','title=AI SI - I | 先别落地','-metadata','comment=First Day Mix; original supplied music; generated motion and authored mixed-media animation',str(out)],check=True)

info=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(out)]))
v=next(s for s in info['streams'] if s['codec_type']=='video');assert int(v['nb_read_frames'])==2621 and (v['width'],v['height'])==(1920,1080)
poster=dest/'first-day-mix-poster.jpg';subprocess.run(['ffmpeg','-v','error','-y','-ss','32.65','-i',str(out),'-frames:v','1','-q:v','2',str(poster)],check=True)
record={'file':str(out.relative_to(root)),'sha256':sha(out),'bytes':out.stat().st_size,'frames':2621,'fps':v['avg_frame_rate'],'width':1920,'height':1080,'duration':info['format']['duration'],'source_audio_sha256':sha(root/'episodes/first-day-mix/first-day.wav'),'chunks':{str(p.relative_to(root)):sha(p) for p in parts},'meme_patch':{'path':str(meme.relative_to(root)),'sha256':sha(meme),'frames':[494,715]},'birth_fit_patches':[{'path':str(q.relative_to(root)),'sha256':sha(q)} for q in [fit22,fit24]],'reserved_tile_patch':{'path':str(patch.relative_to(root)),'sha256':sha(patch),'frames':[1883,1922]},'final_qa_status':'pending separate full decode / frame / audio / visual review'}
(prod/'delivery.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n');print(out)
