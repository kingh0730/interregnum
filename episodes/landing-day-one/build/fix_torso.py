from pathlib import Path
from PIL import Image,ImageDraw,ImageChops
import json,numpy as np
r=Path(__file__).resolve().parents[1];sk=json.loads((r/'assets/rig-joints.json').read_text())
for m in ['cel','toy']:
 for i in range(6):
  im=Image.open(r/f'assets/{m}/{i}.png').convert('RGBA');w,h=im.size;mask=Image.new('L',im.size,255);d=ImageDraw.Draw(mask);pts=sk[i];sy=pts[0][1];wy=pts[2][1]
  # Keep continuous shoulder-to-waist silhouette; cut away the complete outer arm region.
  d.polygon([(0,int(sy*h)),(int(.30*w),int(sy*h)),(int(.31*w),int((wy+.03)*h)),(0,int((wy+.03)*h))],fill=0)
  d.polygon([(w,int(sy*h)),(int(.70*w),int(sy*h)),(int(.69*w),int((wy+.03)*h)),(w,int((wy+.03)*h))],fill=0)
  im.putalpha(ImageChops.multiply(im.getchannel('A'),mask));im.save(r/f'assets/{m}/{i}-body.png')
