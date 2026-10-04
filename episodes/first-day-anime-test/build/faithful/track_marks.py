from pathlib import Path
import cv2,numpy as np,json
R=Path(__file__).resolve().parents[4];W=R/'work/first-day-anime-test';out={}
data={'sing':(W/'faithful/lipsync-test/mandarin-line.mp4',[[493,191],[617,138],[709,57],[628,440]],76),'breath':(W/'motion/breath.mp4',[[493,191],[617,138],[709,57],[628,440]],40),'flight':(W/'motion/flight.mp4',[[548,125],[584,136],[626,119],[568,207]],26)}
data['unfurl']=(W/'faithful/unfurl-clean/unfurl-clean.mp4',[[231*983/540,115*562/810],[261*983/540,106*562/810],[289*983/540,86*562/810],[250*983/540,178*562/810]],49)
data['helix']=(W/'faithful/helix-camera/helix-camera.mp4',[[530*983/960,95*562/541],[550*983/960,90*562/541],[569*983/960,68*562/541],[544*983/960,153*562/541]],16)
data['xiaoman-flight']=(W/'motion/flight.mp4',[[245,152],[274,145]],20)
data['steps']=(W/'faithful/steps-performance/steps-performance.mp4',[[350,130],[368,127],[380,114],[363,162]],61)
data['hand']=(W/'faithful/hand-camera-reverse/hand-camera-reverse.mp4',[[337*983/540,65*562/810],[337*983/540,65*562/810],[395*983/540,41*562/810],[348*983/540,165*562/810]],70)
for name,(path,pts,n) in data.items():
 c=cv2.VideoCapture(str(path));ok,frame=c.read();h,w=frame.shape[:2];p=np.float32(pts).reshape(-1,1,2)*np.float32([w/983,h/562]);prev=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);frames=[{'points':(p[:,0]/[w,h]).tolist(),'error':[0]*4}]
 for i in range(1,n):
  ok,frame=c.read()
  if not ok:break
  cur=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  if name=='sing' and i==24:p=np.float32([[488,192],[613,138],[700,57],[624,448]]).reshape(-1,1,2)*np.float32([w/983,h/562]);prev=cur
  if name=='hand' and i in [30,54,60]:
   reset={30:[[296,134],[332,129],[372,116],[319,209]],54:[[220,144],[220,144],[0,0],[0,0]],60:[[207,151],[238,155],[0,0],[219,230]]}[i];p=np.float32(reset).reshape(-1,1,2)*np.float32([w/540,h/810]);prev=cur
  q,st,e=cv2.calcOpticalFlowPyrLK(prev,cur,p,None,winSize=(41,41),maxLevel=3,criteria=(3,40,.001));back,_,_=cv2.calcOpticalFlowPyrLK(cur,prev,q,None,winSize=(41,41),maxLevel=3);err=np.linalg.norm(back[:,0]-p[:,0],axis=1);q[st[:,0]==0]=p[st[:,0]==0];frames.append({'points':(q[:,0]/[w,h]).tolist(),'error':err.tolist()});p=q;prev=cur
 out[name]={'fps':c.get(5),'frames':frames,'source':str(path.relative_to(R))};print(name,'maximum forward-back error',max(max(f['error']) for f in frames))
(W/'faithful/marks.json').write_text(json.dumps(out))
