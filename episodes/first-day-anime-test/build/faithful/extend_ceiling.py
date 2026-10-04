"""Register the generated ceiling margin and preserve every original room pixel."""
from pathlib import Path
from PIL import Image
import cv2,numpy as np,json,hashlib
R=Path(__file__).resolve().parents[4];P=R/'work/first-day-anime-test/faithful';a=np.array(Image.open(P/'birth-room-clean.png').convert('RGB'));b=np.array(Image.open(P/'ceiling-painted.png').convert('RGB'));h,w=a.shape[:2];s=cv2.SIFT_create();ka,da=s.detectAndCompute(cv2.cvtColor(a,cv2.COLOR_RGB2GRAY),None);kb,db=s.detectAndCompute(cv2.cvtColor(b,cv2.COLOR_RGB2GRAY),None);pairs=cv2.BFMatcher().knnMatch(da,db,k=2);good=[m for m,n in pairs if m.distance<.7*n.distance];pa=np.float32([ka[m.queryIdx].pt for m in good]);pb=np.float32([kb[m.trainIdx].pt for m in good]);M,mask=cv2.estimateAffinePartial2D(pa,pb,method=cv2.RANSAC,ransacReprojThreshold=3);assert M is not None and mask.sum()>100;inv=cv2.invertAffineTransform(M);inv[1,2]+=200;expanded=cv2.warpAffine(b,inv,(w,h+200),flags=cv2.INTER_LANCZOS4,borderMode=cv2.BORDER_REPLICATE).astype(float)
delta=a[0].astype(float)-expanded[199]
for y in range(168,200):
 q=(y-168)/31;q=q*q*(3-2*q);expanded[y]+=delta*q
expanded=np.uint8(np.clip(expanded,0,255));expanded[200:]=a;assert np.array_equal(expanded[200:],a);Image.fromarray(expanded).save(P/'birth-room-overscan.png');meta={'margin_top_px':200,'original_width':w,'original_height':h,'output_width':w,'output_height':h+200,'inliers':int(mask.sum()),'old_to_generated':M.tolist(),'original_pixels_preserved':True,'source_sha256':hashlib.sha256((P/'birth-room-clean.png').read_bytes()).hexdigest(),'painted_sha256':hashlib.sha256((P/'ceiling-painted.png').read_bytes()).hexdigest()};(P/'ceiling-registration.json').write_text(json.dumps(meta,indent=2));print(meta)
