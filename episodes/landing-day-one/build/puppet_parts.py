from pathlib import Path
from PIL import Image,ImageDraw,ImageChops
import numpy as np,json
r=Path(__file__).resolve().parents[1]
im=Image.open(r/'assets/cast-cel-v2.png').convert('RGBA');w,h=im.size
for i in range(6):
 col=i%3;row=i//3;top=0 if row==0 else int(h*[.55,.54,.522][col]);bottom=int(h*.522) if row==0 else h;c=im.crop((col*w//3,top,(col+1)*w//3,bottom));a=np.array(c)[:,:,3];ys,xs=np.where(a>150);c=c.crop((max(0,xs.min()-2),max(0,ys.min()-2),min(c.width,xs.max()+3),min(c.height,ys.max()+3)));c.save(r/f'assets/cel/{i}.png')
# normalized in each isolated full-body crop. Shoulder/elbow/wrist, measured on source.
skeleton=[[(.33,.29),(.23,.43),(.085,.53)],[(.34,.22),(.23,.40),(.07,.56)],[(.31,.22),(.20,.40),(.07,.56)],[(.34,.36),(.22,.53),(.08,.63)],[(.32,.34),(.23,.52),(.08,.63)],[(.30,.24),(.19,.40),(.08,.56)]]
for medium in ['cel','toy']:
 for i in range(6):
  src=Image.open(r/f'assets/{medium}/{i}.png').convert('RGBA');w,h=src.size;body=src.copy();combined=Image.new('L',src.size);pts=skeleton[i];cfg=[]
  for side in [-1,1]:
   points=[(x if side<0 else 1-x,y) for x,y in pts]
   for j in range(2):
    p,q=points[j:j+2];mask=Image.new('L',src.size);d=ImageDraw.Draw(mask);width=int(w*(.185 if j==0 else .16));P=tuple(int(v*s) for v,s in zip(p,(w,h)));Q=tuple(int(v*s) for v,s in zip(q,(w,h)));d.line([P,Q],fill=255,width=width)
    for x,y in [P,Q]:d.ellipse((x-width/2,y-width/2,x+width/2,y+width/2),fill=255)
    part=src.copy();part.putalpha(ImageChops.multiply(src.getchannel('A'),mask));part.save(r/f'assets/{medium}/{i}-arm-{side}-{j}.png');combined=ImageChops.lighter(combined,mask)
    cfg.append({'side':side,'segment':j,'pivot':p,'end':q})
  body.putalpha(ImageChops.multiply(src.getchannel('A'),ImageChops.invert(combined)));body.save(r/f'assets/{medium}/{i}-body.png')
(r/'assets/rig-joints.json').write_text(json.dumps(skeleton))
