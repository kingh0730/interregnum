from pathlib import Path
import os,json
import cv2,numpy as np
from PIL import Image
import onnxruntime as ort
from rembg import remove,new_session
R=Path(__file__).resolve().parents[4];P=R/'work/first-day-anime-test/faithful';os.environ['REMBG_HOME']=str(P/'models');o=ort.SessionOptions();o.intra_op_num_threads=4;s=new_session('isnet-anime',sess_opts=o,providers=['CPUExecutionProvider']);cap=cv2.VideoCapture(str(R/'work/first-day-anime-test/motion/outro.mp4'));ok,base=cap.read();h,w=base.shape[:2];sift=cv2.SIFT_create();roi=np.zeros((h,w),'uint8');roi[int(h*.06):int(h*.66),int(w*.35):int(w*.95)]=255;kb,db=sift.detectAndCompute(cv2.cvtColor(base,cv2.COLOR_BGR2GRAY),roi);folder=P/'outro-layers';folder.mkdir(exist_ok=True);records=[];ids=list(range(0,min(31,int(cap.get(7))),2))
for f in ids:
 cap.set(1,f);ok,frame=cap.read();assert ok;kp,ds=sift.detectAndCompute(cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY),None);matches=cv2.BFMatcher().knnMatch(db,ds,k=2);good=[a for a,b in matches if a.distance<.72*b.distance];a=np.float32([kp[m.trainIdx].pt for m in good]);b=np.float32([kb[m.queryIdx].pt for m in good]);M,inlier=cv2.estimateAffinePartial2D(a,b,method=cv2.RANSAC,ransacReprojThreshold=4);assert M is not None and inlier.sum()>=10
 rgba=remove(Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)),session=s);aligned=cv2.warpAffine(np.array(rgba),M,(w,h),flags=cv2.INTER_LANCZOS4);Image.fromarray(aligned).save(folder/f'{f:04}.png');records.append({'frame':f,'matrix':M.tolist(),'inliers':int(inlier.sum())});print(f,int(inlier.sum()),flush=True)
(folder/'index.json').write_text(json.dumps({'fps':cap.get(5),'indices':ids,'registration':'SIFT similarity, upper-body reference features; toe movement retained','transforms':records},indent=2))
