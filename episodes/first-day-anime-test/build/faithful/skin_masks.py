# REJECTED EXPERIMENT: not used by the delivered compositor. Retained for provenance.
from pathlib import Path
from PIL import Image,ImageDraw
import cv2,numpy as np,json
R=Path(__file__).resolve().parents[4];P=R/'work/first-day-anime-test/faithful/unfurl';cap=cv2.VideoCapture(str(P/'unfurl.mp4'));folder=P/'skin-masks';folder.mkdir(exist_ok=True)
poly=np.array([[643,339],[648,356],[656,379],[665,402],[669,450],[686,517],[684,536],[684,571],[682,598],[686,607],[697,605],[706,594],[708,574],[711,560],[704,541],[701,526],[711,483],[715,456],[711,421],[708,397],[716,344]],np.int32)
ids=[0,42,84]
import sys
if '--all' in sys.argv:ids=list(range(0,85,3))
review=Image.new('RGB',(500*len(ids),925),'#C9DCE9') if len(ids)==3 else None
for j,f in enumerate(ids):
 cap.set(1,f);ok,bgr=cap.read();assert ok;h,w=bgr.shape[:2];rect=(600,310,190,320);x,y,rw,rh=rect;rgb=cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB);crop=bgr[y:y+rh,x:x+rw];outline=np.zeros((rh,rw),'uint8');cv2.fillPoly(outline,[poly-[x,y]],255);envelope=cv2.dilate(outline,np.ones((27,27),'uint8'));mask=np.where(envelope>0,cv2.GC_PR_FGD,cv2.GC_BGD).astype('uint8');mask[20:212,82:94]=cv2.GC_FGD;mask[230:285,84:93]=cv2.GC_FGD
 c=rgb[y:y+rh,x:x+rw].astype(float);red=(c[:,:,0]>c[:,:,1]*1.45)&(c[:,:,0]-c[:,:,2]>60);mask[red]=cv2.GC_BGD
 cv2.grabCut(crop,mask,None,np.zeros((1,65)),np.zeros((1,65)),6,cv2.GC_INIT_WITH_MASK);m=np.uint8((mask==cv2.GC_FGD)|(mask==cv2.GC_PR_FGD))*255
 final=np.zeros((h,w),'uint8');final[y:y+rh,x:x+rw]=m;layer=Image.new('RGBA',(w,h),'white');layer.putalpha(Image.fromarray(final));layer.save(folder/f'{f:04}.png')
 if review:
  out=Image.fromarray(rgb).convert('RGBA');out.putalpha(Image.fromarray(final));bg=Image.new('RGB',(w,h),'#C9DCE9');bg.paste(out,(0,0),out);im=bg.crop((610,280,770,650)).resize((500,925));review.paste(im,(j*500,0))
 print(f,flush=True)
if review:review.save(P/'skin-mask-test.jpg')
else:(folder/'index.json').write_text(json.dumps({'indices':ids,'source':'unfurl.mp4','method':'GrabCut on leg-only ROI, fixed reviewed interior skin seeds, exclude coral sash; source RGB remains unchanged'}))
