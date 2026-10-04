from pathlib import Path
import json,cv2,numpy as np
R=Path(__file__).resolve().parents[1];media=json.loads((R/'render_kit/text/media.json').read_text())
marks={
'S01':{'reflection':[500,575,80]},
'S16':{'pin':[875,171,22],'eye0':[802,210,6],'eye1':[839,198,6]},
'S17':{'pin':[970,140,48],'brooch':[809,667,51],'eye0':[697,234,21],'eye1':[894,220,21]},
'S20':{'tag':[533,252,16]},
'S21':{'pin':[794,56,27],'brooch':[751,209,20],'eye0':[680,129,7],'eye1':[744,98,7],'tag':[775,722,9]},
'S23':{'pin':[564,99,40],'brooch':[352,443,29],'eye0':[430,194,11],'eye1':[515,244,11]},
'S24':{'pin':[714,80,27],'brooch':[628,262,23],'eye0':[587,153,8],'eye1':[645,125,8]},
'S25':{'pin':[813,206,22],'brooch':[790,289,14]},
'S29':{'pin':[946,125,38],'brooch':[872,585,35],'eye0':[609,300,16],'eye1':[780,225,16]},
'S42':{'pin':[746,80,40],'brooch':[714,348,28]},
'S44':{'pin':[577,94,27],'brooch':[475,258,22],'eye0':[479,134,9],'eye1':[537,148,9],'tag':[419,609,9]}}
result={}
for sid,items in marks.items():
 cfg=media[sid];cap=cv2.VideoCapture(str(R/cfg['file']));fps=cap.get(cv2.CAP_PROP_FPS);ok,frame=cap.read();assert ok,sid;H,W=frame.shape[:2];prev=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);states={};records={k:[] for k in items};weak=[]
 for k,(x,y,size) in items.items():
  px=x/1672*W;py=y/941*H;radius=max(22,size/1672*W*1.2);mask=np.zeros((H,W),np.uint8);cv2.rectangle(mask,(max(0,int(px-radius)),max(0,int(py-radius))),(min(W-1,int(px+radius)),min(H-1,int(py+radius))),255,-1);pts=cv2.goodFeaturesToTrack(prev,30,.01,4,mask=mask);states[k]={'pts':pts,'p':np.array([px,py],np.float32),'size':size/1672*W,'angle':0}
 def record():
  for k,s in states.items():records[k].append([float(s['p'][0]/W),float(s['p'][1]/H),float(s['size']/W),float(s['angle'])])
 record();index=0
 while True:
  ok,frame=cap.read()
  if not ok:break
  index+=1;gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  for k,s in states.items():
   if s['pts'] is None or len(s['pts'])<3:weak.append([index,k]);continue
   nxt,status,err=cv2.calcOpticalFlowPyrLK(prev,gray,s['pts'],None,winSize=(31,31),maxLevel=3);good=(status[:,0]>0)&(err[:,0]<35)
   if good.sum()<3:weak.append([index,k]);continue
   old=s['pts'][good];new=nxt[good];M,inliers=cv2.estimateAffinePartial2D(old,new,method=cv2.RANSAC,ransacReprojThreshold=2.5)
   if M is not None:
    scale=float(np.sqrt(M[0,0]**2+M[1,0]**2))
    if .9<scale<1.1:
     s['p']=(M[:,:2]@s['p']+M[:,2]).astype(np.float32);s['size']*=scale;s['angle']+=float(np.arctan2(M[1,0],M[0,0]))
   s['pts']=new.reshape(-1,1,2)
  record();prev=gray
 cap.release();result[sid]={'fps':fps,'marks':records,'weak_frames':weak};print(sid,'frames',index+1,'weak',len(weak),flush=True)
(R/'render_kit/text/tracking.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
