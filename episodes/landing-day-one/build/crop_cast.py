from PIL import Image
import numpy as np
from pathlib import Path
r=Path(__file__).resolve().parents[1]
for medium in ['cel','toy']:
 im=Image.open(r/f'assets/cast-{medium}.png').convert('RGBA'); w,h=im.size
 # Column boundaries are actual empty strips, not equal-width guesses.
 edges=[0,.165,.337,.507,.671,.833,1]
 out=r/'assets'/medium;out.mkdir(exist_ok=True)
 for i in range(6):
  c=im.crop((int(w*edges[i]),0,int(w*edges[i+1]),h));a=np.array(c)[:,:,3];ys,xs=np.where(a>120)
  b=(max(0,xs.min()-2),max(0,ys.min()-2),min(c.width,xs.max()+3),min(c.height,ys.max()+3))
  c=c.crop(b);c.save(out/f'{i}.png')
print('12 crop assets retained alpha')
