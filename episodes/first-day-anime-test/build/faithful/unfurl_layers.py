# REJECTED EXPERIMENT: not used by the delivered compositor. Retained for provenance.
from pathlib import Path
import os,json
import cv2,numpy as np
from PIL import Image
import onnxruntime as ort
from rembg import remove,new_session
R=Path(__file__).resolve().parents[4];P=R/'work/first-day-anime-test/faithful';os.environ['REMBG_HOME']=str(P/'models');o=ort.SessionOptions();o.intra_op_num_threads=4;s=new_session('isnet-anime',sess_opts=o,providers=['CPUExecutionProvider'])
c=cv2.VideoCapture(str(P/'unfurl/unfurl.mp4'));folder=P/'unfurl/layers';folder.mkdir(exist_ok=True);ids=list(range(0,85,3))
for i in ids:
 c.set(1,i);ok,a=c.read();assert ok;im=Image.fromarray(cv2.cvtColor(a,cv2.COLOR_BGR2RGB));m=np.array(remove(im,session=s).getchannel('A'));m[:,:int(m.shape[1]*.27)]=0;m=(m>100).astype('uint8')*255
 count,labels,stats,_=cv2.connectedComponentsWithStats(m)
 for j in range(1,count):
  if stats[j,4]<350:m[labels==j]=0
 im=im.convert('RGBA');im.putalpha(Image.fromarray(m));im.save(folder/f'{i:04}.png');print(i,flush=True)
(folder/'index.json').write_text(json.dumps({'fps':24,'indices':ids}))
