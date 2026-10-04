from pathlib import Path
from PIL import Image
import cv2,numpy as np
R=Path(__file__).resolve().parents[1]/'assets'
for n in ['S23-v1','S23-90-v1','S23-180-v1','S23-270-v1']:
 src=np.array(Image.open(R/'plates'/f'{n}.png').convert('RGB'));alpha=np.array(Image.open(R/'mattes'/f'{n}.png').convert('RGBA'))[:,:,3]
 if '90-' in n or '270-' in n:
  samname=n.replace('-v1','-sam');sam=np.array(Image.open(R/'mattes'/f'{samname}.png').convert('RGBA'))[:,:,3]
  binary=(sam>30).astype(np.uint8)*255;binary=cv2.morphologyEx(binary,cv2.MORPH_CLOSE,np.ones((7,7),np.uint8));contours,_=cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE);filled=np.zeros_like(binary)
  for c in contours:
   if cv2.contourArea(c)>300:cv2.drawContours(filled,[c],-1,255,-1)
  alpha=np.maximum(alpha,filled)
  if n=='S23-90-v1':cv2.fillPoly(alpha,[np.array([[626,680],[645,688],[667,722],[639,741],[625,725]],np.int32)],255)
 alpha=cv2.GaussianBlur(alpha,(3,3),.55)
 out=Image.fromarray(src).convert('RGBA');out.putalpha(Image.fromarray(alpha));out.save(R/'mattes'/f'{n}-refined.png')
 gray=cv2.cvtColor(src,cv2.COLOR_RGB2GRAY);gray=cv2.GaussianBlur(gray,(3,3),.6);sketch=cv2.divide(gray,255-cv2.GaussianBlur(255-gray,(0,0),12),scale=255);paper=np.stack([sketch*.941,sketch*.933,sketch*.902],axis=-1).clip(0,255).astype(np.uint8);line=Image.fromarray(paper).convert('RGBA');line.putalpha(Image.fromarray(alpha));line.save(R/'mattes'/f'{n}-line.png')
 dep=np.array(Image.open(R/'depth'/f'{n}.png').convert('L'));dep=cv2.GaussianBlur(cv2.dilate(dep,np.ones((9,9),np.uint8)),(0,0),4);Image.fromarray(dep).save(R/'depth'/f'{n}-smooth.png')
