"""Extract original-pixel actor layers for the prescribed 2.5D rigs."""
from pathlib import Path
import os,json,hashlib,time
import cv2,numpy as np
from PIL import Image
ROOT=Path(__file__).resolve().parents[4];OUT=ROOT/'work/first-day-anime-test/faithful';ASSET=ROOT/'work/first-day-anime-test/assets'
os.environ['REMBG_HOME']=str(OUT/'models')
from rembg import remove,new_session
import onnxruntime as ort

def main():
    opts=ort.SessionOptions();opts.intra_op_num_threads=4;opts.inter_op_num_threads=1
    session=new_session('isnet-anime',sess_opts=opts,providers=['CPUExecutionProvider'])
    targets=['flight-clean','float-clean']
    import sys
    if '--test' in sys.argv:targets=['birth-clean']
    for name in targets:
        path=OUT/(name+'-actor.png')
        if path.exists():continue
        im=Image.open(ASSET/(name+'.png')).convert('RGB')
        result=remove(im,session=session)
        result.save(path);print(name,flush=True)
    if '--test' in sys.argv:return
    for take in ['paper']:
        cap=cv2.VideoCapture(str((OUT/f'{take}.mp4') if take.endswith('-wide') else ROOT/f'work/first-day-anime-test/motion/{take}.mp4'));fps=cap.get(cv2.CAP_PROP_FPS);total=int(cap.get(cv2.CAP_PROP_FRAME_COUNT));folder=OUT/take;folder.mkdir(exist_ok=True)
        # View-conditioned sprite samples; these are not independent pose generations.
        step=2 if take=='paper' else 3
        for i in range(0,total,step):
            dst=folder/f'{i:04d}.png'
            if dst.exists():continue
            cap.set(cv2.CAP_PROP_POS_FRAMES,i);ok,frame=cap.read();assert ok
            im=Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB));result=remove(im,session=session)
            result.save(dst);print(take,i,total,flush=True)
        cap.release();(folder/'index.json').write_text(json.dumps({'fps':fps,'total_frames':total,'indices':list(range(0,total,step))}))
if __name__=='__main__':main()
