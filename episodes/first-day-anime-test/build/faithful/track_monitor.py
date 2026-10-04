from pathlib import Path
import cv2,numpy as np,json
from PIL import Image,ImageDraw
from scipy.signal import savgol_filter
R=Path(__file__).resolve().parents[4];P=R/'work/first-day-anime-test/faithful/reply-performance';cap=cv2.VideoCapture(str(P/'reply-performance.mp4'));rows=[];frames=[];(P/'masks').mkdir(exist_ok=True)
for i in range(49):
 ok,a=cap.read();assert ok;h,w=a.shape[:2];rgb=cv2.cvtColor(a,cv2.COLOR_BGR2RGB);v=rgb.astype(float);mask=((v.min(2)>165)&(v.mean(2)>203)&(v[:,:,0]-v[:,:,1]<38)&(v[:,:,1]-v[:,:,2]<70)).astype('uint8');mask[:,int(w*.42):]=0;mask[int(h*.91):]=0;num,l,st,_=cv2.connectedComponentsWithStats(mask);m=l==(1+np.argmax(st[1:,4]));ys,xs=np.where(m);right=xs.max();
 top=[];bottom=[];rs=[];ls=[]
 for x in range(int(w*.07),int(right-w*.025),8):
  yy=np.where(m[:,x])[0]
  if len(yy)>30:top.append((x,yy.min()));
  if len(yy)>30 and x>w*.18:bottom.append((x,yy.max()))
 for y in range(int(h*.26),int(h*.64),8):
  xx=np.where(m[y])[0]
  if len(xx)>30:rs.append((y,xx.max()))
 for y in range(int(h*.04),int(h*.21),8):
  xx=np.where(m[y])[0]
  if len(xx)>30:ls.append((y,xx.min()))
 def fit(p):return np.polyfit(np.array(p)[:,0],np.array(p)[:,1],1)
 at,bt=fit(top);ab,bb=fit(bottom);ar,br=fit(rs);al,bl=fit(ls)
 def meet(a,b,c,d):
  # y=a*x+b and x=c*y+d
  x=(c*b+d)/(1-c*a);return[x,a*x+b]
 q=np.array([meet(at,bt,al,bl),meet(at,bt,ar,br),meet(ab,bb,ar,br),meet(ab,bb,al,bl)]);rows.append(q);frames.append(rgb);mask_image=Image.new('RGBA',(w,h),'white');mask_image.putalpha(Image.fromarray(cv2.GaussianBlur(m.astype('uint8')*255,(3,3),.65)));mask_image.save(P/'masks'/f'{i:04}.png')
raw=np.array(rows);smooth=savgol_filter(raw,11,2,axis=0);error=np.linalg.norm(raw-smooth,axis=2);print('quad smoothing max pixels',float(error.max()));(P/'monitor.json').write_text(json.dumps({'fps':24,'width':w,'height':h,'method':'Measured blank-screen boundary lines; 11-frame quadratic smoothing','max_smoothing_error_px':float(error.max()),'quads':(smooth/[w,h]).tolist()},indent=2))
out=Image.new('RGB',(1920,540))
for j,i in enumerate([0,6,12,18,24,30,36,48]):
 im=Image.fromarray(frames[i]);d=ImageDraw.Draw(im);q=[tuple(xy) for xy in smooth[i]];d.line(q+[q[0]],fill='red',width=4);im=im.resize((480,270));out.paste(im,((j%4)*480,(j//4)*270))
out.save(P/'monitor-review.jpg')
