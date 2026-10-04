# REJECTED EXPERIMENT: not used by the delivered compositor. Retained for provenance.
"""Propagate a reviewed interior-skin polygon; the browser restores source pixels only."""
from pathlib import Path
import cv2,numpy as np,json
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[4];P=R/'work/first-day-anime-test/faithful';cap=cv2.VideoCapture(str(P/'unfurl/unfurl.mp4'));ok,a=cap.read();h,w=a.shape[:2];points=[[643,339],[648,356],[656,379],[665,402],[669,450],[686,517],[684,536],[684,571],[682,598],[686,607],[697,605],[706,594],[708,574],[711,560],[704,541],[701,526],[711,483],[715,456],[711,421],[708,397],[716,344]];p=np.float32(points).reshape(-1,1,2);prev=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY);rows=[p[:,0].copy()];rgb={0:cv2.cvtColor(a,cv2.COLOR_BGR2RGB)}
for i in range(1,85):
 ok,a=cap.read();assert ok;cur=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY);q,st,_=cv2.calcOpticalFlowPyrLK(prev,cur,p,None,winSize=(31,31),maxLevel=3);back,bst,_=cv2.calcOpticalFlowPyrLK(cur,prev,q,None,winSize=(31,31),maxLevel=3);err=np.linalg.norm(back[:,0]-p[:,0],axis=1);valid=(st[:,0]>0)&(err<2);delta=np.median((q-p)[valid],axis=0);q[~valid]=p[~valid]+delta;p=q;prev=cur;rows.append(p[:,0].copy())
 if i in [42,84]:rgb[i]=cv2.cvtColor(a,cv2.COLOR_BGR2RGB)
(P/'unfurl/leg-mask.json').write_text(json.dumps({'source':'unfurl/unfurl.mp4','fps':24,'points':[(r/[w,h]).tolist() for r in rows],'scope':'Interior skin only. Does not synthesize or change limb geometry.'},indent=2))
out=Image.new('RGB',(1500,900))
for j,i in enumerate([0,42,84]):
 im=Image.fromarray(rgb[i]);g=ImageDraw.Draw(im);q=[tuple(pt) for pt in rows[i]];g.line(q+[q[0]],fill='red',width=2);im=im.crop((610,280,770,650)).resize((500,900));out.paste(im,(j*500,0))
out.save(P/'unfurl/leg-polygon-review.jpg')
