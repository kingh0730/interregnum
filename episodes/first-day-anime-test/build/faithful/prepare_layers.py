from pathlib import Path
import os,json
import cv2,numpy as np
from PIL import Image
ROOT=Path(__file__).resolve().parents[4];A=ROOT/'work/first-day-anime-test/assets';O=ROOT/'work/first-day-anime-test/faithful'
os.environ['REMBG_HOME']=str(O/'models')
from rembg import remove,new_session
import onnxruntime as ort
opts=ort.SessionOptions();opts.intra_op_num_threads=4;s=new_session('isnet-general-use',sess_opts=opts,providers=['CPUExecutionProvider'])
# Separate the persistent observer from the heroine; preserve exact source pixels.
birth=Image.open(A/'birth-clean.png').convert('RGB');w,h=birth.size;box=(0,int(h*.23),int(w*.30),int(h*.91));piece=remove(birth.crop(box),session=s);xiao=Image.new('RGBA',birth.size);xiao.paste(piece,(box[0],box[1]));xiao.save(O/'birth-xiaoman.png')
print('Registered persistent observer layer saved')
