from pathlib import Path
import os,json,sys
import numpy as np,cv2
from PIL import Image
import onnxruntime as ort
from rembg import remove,new_session
R=Path(__file__).resolve().parents[4];P=R/'work/first-day-anime-test/faithful';os.environ['REMBG_HOME']=str(P/'models');o=ort.SessionOptions();o.intra_op_num_threads=4;s=new_session('isnet-anime',sess_opts=o,providers=['CPUExecutionProvider']);name=sys.argv[1] if len(sys.argv)>1 else 'hand-camera';folder=P/name/'layers';folder.mkdir(exist_ok=True);cap=cv2.VideoCapture(str(P/name/(name+'.mp4')));ids=list(range(0,int(cap.get(7)),3))
for i in ids:
 dest=folder/f'{i:04}.png'
 if dest.exists():continue
 cap.set(1,i);ok,a=cap.read();assert ok;rgb=cv2.cvtColor(a,cv2.COLOR_BGR2RGB);im=Image.fromarray(rgb);alpha=np.array(remove(im,session=s).getchannel('A'));alpha=np.clip((alpha.astype(float)-30)*255/200,0,255).astype('uint8')
 # Background is neutral white. Suppress the remaining neutral near-white fringe,
 # without removing highlights inside the opaque character mask.
 edge=alpha<200;white=rgb.min(axis=2)>237;alpha[edge&white]=0
 num,l,st,_=cv2.connectedComponentsWithStats((alpha>70).astype('uint8'))
 for k in range(1,num):
  if st[k,4]<600:alpha[l==k]=0
 im=im.convert('RGBA');im.putalpha(Image.fromarray(alpha));im.save(dest);print(name,i,flush=True)
(folder/'index.json').write_text(json.dumps({'fps':cap.get(5),'indices':ids,'width':int(cap.get(3)),'height':int(cap.get(4))}))
