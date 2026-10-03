"""Check delivered media and the regressions identified in playback feedback."""
from pathlib import Path
import hashlib,json,subprocess
import cv2,numpy as np
from PIL import Image
ROOT=Path(__file__).resolve().parents[4]
SRC=Path(__file__).resolve().parent
MASTER=ROOT/'renders/first-day-anime-test/first-day_opus55_graphics-v2_1080p30.mp4'
QA=ROOT/'work/first-day-anime-test/graphics-v2/qa'

def main():
    probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','stream=codec_name,width,height,r_frame_rate,nb_frames,duration','-of','json',str(MASTER)]))
    v=next(s for s in probe['streams'] if s['codec_name']=='h264')
    assert (v['width'],v['height'],v['r_frame_rate'],int(v['nb_frames']))==(1920,1080,'30/1',1311)
    subprocess.run(['ffmpeg','-v','error','-i',str(MASTER),'-f','null','-'],check=True)
    a=np.array(Image.open(QA/'frame-0346.jpg'))[516:605,382:585]
    b=np.array(Image.open(QA/'frame-0350.jpg'))[516:605,382:585]
    difference=float(np.abs(a.astype(float)-b).mean());assert difference==0
    cap=cv2.VideoCapture(str(MASTER));coverage=[]
    for frame in range(1185,1197):
        cap.set(cv2.CAP_PROP_POS_FRAMES,frame);ok,im=cap.read();assert ok
        coverage.append(float(np.mean(np.min(im[600:900,50:600],axis=2)<225)))
    cap.release();assert min(coverage)>.6
    base=ROOT/'work/first-day-anime-test/graphics-v2/clean-base.mp4'
    base_frames=int(subprocess.check_output(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=nb_frames','-of','csv=p=0',str(base)]).strip());assert base_frames==1311
    report=dict(master=str(MASTER.relative_to(ROOT)),sha256=hashlib.sha256(MASTER.read_bytes()).hexdigest(),probe=probe,full_decode='passed',clean_base_frames=base_frames,greeting_prefix_mean_pixel_difference=difference,transition_39s_nonblank_fraction_min=min(coverage),implementation='Bun + HTML Canvas 2D + textured paper meshes + Puppeteer/Chrome',sampled_frames=[int(p.stem.split('-')[1]) for p in sorted(QA.glob('frame-*.jpg'))],new_image_or_video_model_requests=0,normal_speed_audiovisual_review='pending user playback',sources={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in SRC.iterdir() if p.suffix in ['.js','.ts','.html','.py']})
    (SRC/'review.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['full_decode','clean_base_frames','greeting_prefix_mean_pixel_difference','transition_39s_nonblank_fraction_min']}))
if __name__=='__main__':main()
