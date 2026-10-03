"""Decode returned footage and expose timed samples; not a playback approval."""
import argparse,json
from pathlib import Path
import cv2,numpy as np
from PIL import Image,ImageDraw
from graphics import ROOT
WORK=ROOT/'work/first-day-anime-test'

def inspect(path):
    cap=cv2.VideoCapture(str(path));count=int(cap.get(cv2.CAP_PROP_FRAME_COUNT));fps=cap.get(cv2.CAP_PROP_FPS)
    out=WORK/'motion-qa'/path.stem;out.mkdir(parents=True,exist_ok=True)
    selected=sorted(set(np.linspace(0,count-1,16).astype(int).tolist()))
    sheet=Image.new('RGB',(480*4,290*4),'#141413')
    for i,frame in enumerate(selected):
        cap.set(cv2.CAP_PROP_POS_FRAMES,frame);ok,arr=cap.read()
        if not ok:raise RuntimeError(f'{path}: cannot decode frame {frame}')
        im=Image.fromarray(cv2.cvtColor(arr,cv2.COLOR_BGR2RGB));im.save(out/f'{frame:04d}.jpg',quality=94)
        im.thumbnail((480,270));x=i%4*480;y=i//4*290;sheet.paste(im,(x,y))
        ImageDraw.Draw(sheet).text((x+8,y+272),f'{path.stem}  f{frame}  {frame/fps:.3f}s',fill='white')
    cap.release();sheet.save(out/'contact.jpg',quality=94)
    result=dict(path=str(path.relative_to(ROOT)),frames=count,fps=fps,duration=count/fps,sampled_frames=selected,playback_review='pending')
    (out/'probe.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('names',nargs='*');args=ap.parse_args()
    for p in sorted((WORK/'motion').glob('*.mp4')):
        if not args.names or p.stem in args.names:inspect(p)
