from PIL import Image,ImageOps,ImageDraw
from pathlib import Path
import subprocess,io
r=Path(__file__).resolve().parents[1]
groups=[['m_S05','m_S06','m_S07','m_S08','m_S17'],['m_S18','m_S24','m_S27','m_P21_touch','m_S43']]
for gi,names in enumerate(groups):
 o=Image.new('RGB',(1600,1000),'#eee5d0');d=ImageDraw.Draw(o)
 for row,n in enumerate(names):
  for col,t in enumerate([0,.6,1.2,2.0,3.2]):
   b=subprocess.check_output(['ffmpeg','-v','error','-ss',str(t),'-i',str(r/f'assets/{n}.mp4'),'-frames:v','1','-vf','scale=320:180','-f','image2pipe','-vcodec','mjpeg','-']);im=Image.open(io.BytesIO(b));o.paste(im,(col*320,row*200));d.text((col*320+5,row*200+183),f'{n} {t:.1f}',fill='black')
 o.save(r/f'proofs/motion-review-{gi}.jpg')
names=['S09r','S26r','S28r','S22r','S13r','S33f'];o=Image.new('RGB',(1440,840),'#ddd5c5');d=ImageDraw.Draw(o)
for i,n in enumerate(names):
 im=ImageOps.fit(Image.open(r/f'assets/{n}.png').convert('RGB'),(480,270));x=i%3*480;y=i//3*420;o.paste(im,(x,y));d.text((x+8,y+275),n,fill='black')
o.save(r/'proofs/repaired-scenes.jpg')
