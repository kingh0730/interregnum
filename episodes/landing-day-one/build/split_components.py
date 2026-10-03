from pathlib import Path
import argparse
from PIL import Image
import numpy as np
from scipy.ndimage import label,binary_dilation
ap=argparse.ArgumentParser();ap.add_argument('source');ap.add_argument('out');ap.add_argument('--count',type=int,default=6);a=ap.parse_args()
im=Image.open(a.source).convert('RGBA');arr=np.array(im);mask=arr[:,:,3]>90;labels,n=label(binary_dilation(mask,iterations=2));sizes=np.bincount(labels.ravel());ids=np.argsort(sizes[1:])[-a.count:]+1;rows=[]
for k in ids:
 ys,xs=np.where(labels==k);rows.append((k,(int(xs.min()),int(ys.min()),int(xs.max()+1),int(ys.max()+1))))
rows.sort(key=lambda z:(round((z[1][1]+z[1][3])/2/im.height*2) if a.count==6 else round((z[1][1]+z[1][3])/2/im.height*3), (z[1][0]+z[1][2])/2))
# Sort into equal count row groups after y-centre order.
rows.sort(key=lambda z:(z[1][1]+z[1][3])/2);cols=3
ordered=[]
for st in range(0,len(rows),cols):ordered.extend(sorted(rows[st:st+cols],key=lambda z:z[1][0]))
out=Path(a.out);out.mkdir(exist_ok=True,parents=True)
for i,(k,b) in enumerate(ordered):
 aa=arr.copy();aa[:,:,3]=np.where(labels==k,aa[:,:,3],0);crop=Image.fromarray(aa).crop(b);crop.save(out/f'{i}.png');print(i,b,int(sizes[k]))
