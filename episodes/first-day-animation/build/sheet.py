from PIL import Image,ImageDraw
from pathlib import Path
import sys,math
files=[Path(p)for p in sys.argv[2:]]
out=Path(sys.argv[1]);w=480;h=294;cols=4
im=Image.new('RGB',(cols*w,math.ceil(len(files)/cols)*h),'#141413');d=ImageDraw.Draw(im)
for i,p in enumerate(files):
 a=Image.open(p).convert('RGB');a.thumbnail((w,270));x=(i%cols)*w;y=(i//cols)*h;im.paste(a,(x,y+24));d.text((x+8,y+5),p.stem,fill='white')
im.save(out)
