from pathlib import Path
import json,numpy as np,cv2,onnxruntime as ort
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[1];s=ort.InferenceSession('work/first-day-animation/models/onnx/model.onnx',providers=['CPUExecutionProvider'])
shots=json.load(open(root/'compositor/timeline.json'))['shots'];done=[]
for shot in shots:
 if 'P' not in shot['source']:continue
 sid=shot['id'];key='S09b_color' if sid=='S09b' else sid
 a=np.array(Image.open(root/f'assets/keyframes/{key}.png').convert('RGB'));h,w=a.shape[:2];nw=round(w/h*518/14)*14
 x=cv2.resize(a,(nw,518)).astype('float32')/255;x=(x-[.485,.456,.406])/[.229,.224,.225];x=x.transpose(2,0,1)[None].astype('float32')
 d=s.run(None,{'pixel_values':x})[0].squeeze();d=(d-d.min())/(d.max()-d.min()+1e-9);d=cv2.resize(d,(w,h));Image.fromarray((d*65535).astype('uint16')).save(root/f'assets/depth/{sid}.png');Image.fromarray((d*255).astype('uint8')).save(root/f'out/qa/depth-{sid}.jpg');done.append(sid);print(sid,flush=True)
json.dump({'model':'onnx-community/depth-anything-v2-small','near':'white','shots':done},open(root/'build/depth-report.json','w'),indent=2)
