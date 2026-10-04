# REJECTED EXPERIMENT: not used by the delivered compositor. Retained for provenance.
from pathlib import Path
import os
from PIL import Image
import numpy as np,cv2
import onnxruntime as ort
from rembg import new_session,remove
R=Path(__file__).resolve().parents[4];P=R/'work/first-day-anime-test/faithful';A=R/'work/first-day-anime-test/assets';os.environ['REMBG_HOME']=str(P/'models');o=ort.SessionOptions();o.intra_op_num_threads=4;s=new_session('isnet-anime',sess_opts=o,providers=['CPUExecutionProvider'])
im=Image.open(A/'helix-start-clean.png');m=np.array(remove(im,session=s).getchannel('A'));h,w=m.shape
poly=np.array([[0,.13],[.30,.13],[.31,.32],[.43,.37],[.43,.52],[.39,.57],[.44,.82],[.31,.88],[.17,.68],[0,.62]])*np.array([w,h]);clip=np.zeros((h,w),'uint8');cv2.fillPoly(clip,[poly.astype('int32')],255);m=np.minimum(m,clip);m=(m>110).astype('uint8')*255
im=im.convert('RGBA');im.putalpha(Image.fromarray(m));im.crop((int(w*.11),int(h*.16),int(w*.44),int(h*.85))).save(P/'helix-xiaoman.png')
