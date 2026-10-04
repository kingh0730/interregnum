from PIL import Image
from pathlib import Path
r=Path(__file__).resolve().parents[1]/'assets';o=r/'rigs';o.mkdir(exist_ok=True)
# Identical canvas and height; align torso axes without generative repainting or cropping the twin-tails.
items=[('front',r/'plates/helix-front-master.png',520),('left',r/'mattes/helix-left-v1.png',440),('back',r/'mattes/helix-back-v1.png',515),('right',r/'mattes/helix-right-v1.png',590)]
for name,p,cx in items:
 im=Image.open(p).convert('RGBA');canvas=Image.new('RGBA',(1536,1792),(0,0,0,0));canvas.alpha_composite(im,(768-cx,128));canvas.save(o/f'helix-{name}.png')
