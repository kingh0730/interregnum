from pathlib import Path
import json
from PIL import Image
import numpy as np
r=Path(__file__).resolve().parents[1]
p=r/'assets/cast-felt.png'
if p.exists():
 im=Image.open(p).convert('RGBA');w,h=im.size;(r/'assets/felt').mkdir(exist_ok=True)
 for i in range(6):
  col=i%3;row=i//3;top=0 if row==0 else int(h*.525);bottom=int(h*.525) if row==0 else h
  c=im.crop((col*w//3,top,(col+1)*w//3,bottom));a=np.array(c)[:,:,3];ys,xs=np.where(a>150);c=c.crop((max(0,xs.min()-2),max(0,ys.min()-2),min(c.width,xs.max()+3),min(c.height,ys.max()+3)));c.save(r/f'assets/felt/{i}.png')
images={}
for p in (r/'assets').glob('*.png'):images[p.stem]='/assets/'+p.name
for m in ['cel','toy','felt','ensemble','leap']:
 for p in (r/'assets'/m).glob('*.png'):images[m+'-'+p.stem]='/assets/'+m+'/'+p.name
conf={'images':images,'shots':{},'motion':{}}
p=r/'assets/production-assets.json'
if p.exists():
 old=json.loads(p.read_text());conf['shots']=old.get('shots',{});conf['motion']=old.get('motion',{})
p.write_text(json.dumps(conf,ensure_ascii=False,indent=2));print(len(images),'image assets')
