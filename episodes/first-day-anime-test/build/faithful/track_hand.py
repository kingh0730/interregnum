from pathlib import Path
import cv2,numpy as np,json
R=Path(__file__).resolve().parents[4];P=R/'work/first-day-anime-test/faithful';cap=cv2.VideoCapture(str(R/'work/first-day-anime-test/motion/touch.mp4'));ok,im=cap.read();h,w=im.shape[:2];xy=[[506,357],[519,347],[550,331],[574,321],[605,320],[628,319],[658,315],[682,313],[704,300],[728,292],[746,306],[749,330],[742,349],[704,368],[686,378],[681,399],[665,423],[636,450],[617,449],[630,426],[601,461],[591,463],[590,451],[608,414],[571,447],[556,446],[552,438],[562,407],[584,373],[570,383],[557,392],[553,386],[559,374],[574,349],[548,360],[527,368],[513,367]];p=np.float32(xy).reshape(-1,1,2)*[w/1008,h/576];p=p.astype('float32');prev=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY);rows=[(p[:,0]/[w,h]).tolist()]
for i in range(1,8):
 ok,im=cap.read();cur=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY);q,st,_=cv2.calcOpticalFlowPyrLK(prev,cur,p,None,winSize=(31,31),maxLevel=3);q[st[:,0]==0]=p[st[:,0]==0];rows.append((q[:,0]/[w,h]).tolist());p=q;prev=cur
(P/'touch-hand-mask.json').write_text(json.dumps({'fps':24,'points':rows,'scope':'Manually traced Opus hand/forearm skin contour, propagated only across the eight-frame reaching interval'}))
