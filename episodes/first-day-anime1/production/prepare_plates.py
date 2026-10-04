"""Offline PNG plate extraction. Full-size work is per shot to keep disk bounded."""
from pathlib import Path
import argparse,json,subprocess,shutil,hashlib
import cv2,numpy as np
from PIL import Image,ImageFilter
R=Path(__file__).resolve().parents[1];REPO=R.parents[1];WORK=REPO/'work/first-day-anime1'
ap=argparse.ArgumentParser();ap.add_argument('shots',nargs='*');ap.add_argument('--preview',action='store_true');a=ap.parse_args()
media=json.loads((R/'render_kit/text/media.json').read_text());ids=a.shots or sorted({v['source_id'] for v in media.values()});base=WORK/('plates_preview' if a.preview else 'plates');base.mkdir(exist_ok=True)
for sid in ids:
 cfg=media[sid];src=R/cfg['file'];out=base/sid;out.mkdir(exist_ok=True);count=cfg['frames'];size=(480,270) if a.preview else (1920,1080)
 if cfg['kind']=='chroma':size=(round((270 if a.preview else 1080)*cfg['aspect']),270 if a.preview else 1080)
 fingerprint=hashlib.sha256(json.dumps({'cfg':cfg,'preview':a.preview,'version':5},sort_keys=True).encode()).hexdigest();marker=out/'complete.json'
 if marker.exists() and json.loads(marker.read_text()).get('fingerprint')==fingerprint and len(list(out.glob('[0-9][0-9][0-9][0-9].png')))==count:print('ready',sid,flush=True);continue
 if cfg['kind']=='lip_composite':
  cap=cv2.VideoCapture(str(src));fps=cap.get(cv2.CAP_PROP_FPS);ref=Image.open(R/'assets/plates/lipsync-face-test.png').convert('RGB');ref_np=np.array(ref);ref_gray=cv2.cvtColor(ref_np,cv2.COLOR_RGB2GRAY);mask=np.zeros(ref_gray.shape,np.uint8);mask[70:170,120:410]=255;points=cv2.goodFeaturesToTrack(ref_gray,70,.01,6,mask=mask);full=Image.open(R/'assets/plates/helix-front-master.png').convert('RGBA');blend=Image.new('L',ref.size,0)
  from PIL import ImageDraw
  ImageDraw.Draw(blend).ellipse((196,151,336,249),fill=255);blend=blend.filter(ImageFilter.GaussianBlur(9))
  frames=[]
  while True:
   ok,bgr=cap.read()
   if not ok:break
   frames.append(cv2.cvtColor(cv2.resize(bgr,ref.size),cv2.COLOR_BGR2RGB))
  cap.release()
  for i in range(count):
   arr=frames[min(len(frames)-1,round(i/cfg['fps']*fps))];gray=cv2.cvtColor(arr,cv2.COLOR_RGB2GRAY);nxt,status,_=cv2.calcOpticalFlowPyrLK(ref_gray,gray,points,None,winSize=(31,31),maxLevel=3);good=status[:,0]>0;M,_=cv2.estimateAffinePartial2D(points[good],nxt[good],method=cv2.RANSAC,ransacReprojThreshold=3)
   aligned=cv2.warpAffine(arr,cv2.invertAffineTransform(M),ref.size,borderMode=cv2.BORDER_REPLICATE) if M is not None else arr
   cheek=(slice(175,225),slice(175,195));delta=ref_np[cheek].mean((0,1))-aligned[cheek].mean((0,1));aligned=np.clip(aligned.astype(float)+delta,0,255).astype(np.uint8)
   patch=Image.composite(Image.fromarray(aligned),ref,blend);im=full.copy();im.paste(patch,(250,20),blend);reg=Image.new('RGBA',(1536,1792),(0,0,0,0));reg.alpha_composite(im,(248,128))
   if a.preview:reg=reg.resize((384,448),Image.Resampling.LANCZOS)
   reg.save(out/f'{i:04}.png',compress_level=6)
  marker.write_text(json.dumps({'fingerprint':fingerprint,'frames':count}));print('prepared lip',sid,count,flush=True);continue
 filters=[f'scale={size[0]}:{size[1]}:flags=lanczos']
 if cfg['kind']=='interpolated':filters.append('minterpolate=fps=120:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1')
 else:filters.append(f"fps={cfg['fps']}")
 filters.append('setpts=PTS-STARTPTS')
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(src),'-an','-vf',','.join(filters),'-frames:v',str(count),'-start_number','0',str(out/'%04d.png')],check=True)
 if cfg['kind']=='chroma':
  for i in range(count):
   p=out/f'{i:04}.png';rgb=np.array(Image.open(p).convert('RGB')).astype(np.float32)/255;dom=rgb[:,:,1]-np.maximum(rgb[:,:,0],rgb[:,:,2]);alpha=np.clip((1-dom-.06)/.94,0,1);alpha[dom>.9]=0;alpha[dom<.1]=1;fg=(rgb-(1-alpha[:,:,None])*np.array([0,1,0]))/np.maximum(alpha[:,:,None],.001);fg=np.clip(fg,0,1);fg[alpha==0]=0;rgba=np.concatenate([fg,alpha[:,:,None]],axis=2);Image.fromarray((rgba*255).astype(np.uint8),'RGBA').save(p,compress_level=6)
 if sid=='S22':
  for i in range(count):
   p=out/f'{i:04}.png';rgb=np.array(Image.open(p).convert('RGB'));H,W=rgb.shape[:2];hsv=cv2.cvtColor(rgb,cv2.COLOR_RGB2HSV);mask=((hsv[:,:,0]<30)&(hsv[:,:,1]<115)&(hsv[:,:,2]>165)&(rgb[:,:,0]>rgb[:,:,2])).astype(np.uint8)*255;roi=np.zeros_like(mask);roi[int(H*.54):int(H*.77),int(W*.445):int(W*.61)]=255;mask=cv2.bitwise_and(mask,roi);mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,np.ones((3,3),np.uint8));n,labels,stats,cent=cv2.connectedComponentsWithStats(mask);target=np.array([W*(.515+.012*i/max(1,count-1)),H*(.67-.03*i/max(1,count-1))]);candidates=[j for j in range(1,n) if stats[j,cv2.CC_STAT_AREA]>W*H*.0002]
   if candidates:
    j=min(candidates,key=lambda j:np.linalg.norm(cent[j]-target));m=(labels==j).astype(np.uint8)*255;m=cv2.GaussianBlur(m,(3,3),.6)/255.;gray=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY);sketch=cv2.divide(gray,255-cv2.GaussianBlur(255-gray,(0,0),5),scale=255);line=np.stack([sketch*.941,sketch*.933,sketch*.902],axis=-1);rgb=np.clip(rgb*(1-m[:,:,None])+line*m[:,:,None],0,255).astype(np.uint8);Image.fromarray(rgb).save(p,compress_level=6)
 if sid=='S44':
  alpha=np.asarray(Image.open(R/'assets/mattes/S44-v1_1.png').convert('L').resize((480,270))).astype(np.uint8);yy,xx=np.mgrid[0:270,0:480];ground=np.clip((yy/269-.48)/.12,0,1)*np.clip(xx/479/.06,0,1)*np.clip((1-xx/479)/.06,0,1)*np.clip((1-yy/269)/.08,0,1);alpha=np.maximum(alpha,(ground*255).astype(np.uint8));dep=np.asarray(Image.open(R/'assets/depth/S44-v1.png').convert('L').resize((480,270))).astype(np.uint8);gridx,gridy=np.meshgrid(np.arange(480,dtype=np.float32),np.arange(270,dtype=np.float32));prev=None
  for i in range(count):
   p=out/f'{i:04}.png';im=Image.open(p).convert('RGB');small=cv2.cvtColor(np.array(im.resize((480,270))),cv2.COLOR_RGB2GRAY)
   if prev is not None:
    flow=cv2.calcOpticalFlowFarneback(prev,small,None,.5,3,21,4,7,1.5,0);mx=gridx-flow[:,:,0];my=gridy-flow[:,:,1];alpha=cv2.remap(alpha,mx,my,cv2.INTER_LINEAR,borderMode=cv2.BORDER_CONSTANT);dep=cv2.remap(dep,mx,my,cv2.INTER_LINEAR,borderMode=cv2.BORDER_REPLICATE)
   prev=small
   m=Image.fromarray(alpha).filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.GaussianBlur(.6)).resize(im.size,Image.Resampling.LANCZOS);im.putalpha(m);im.save(p,compress_level=6);Image.fromarray(dep).resize((257,145),Image.Resampling.BILINEAR).save(out/f'{i:04}.depth.png')
 assert len(list(out.glob('[0-9][0-9][0-9][0-9].png')))==count,(sid,'incomplete sequence')
 marker.write_text(json.dumps({'fingerprint':fingerprint,'frames':count}));print('prepared',sid,count,'preview' if a.preview else 'full',flush=True)
