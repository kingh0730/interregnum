from pathlib import Path
import subprocess,json
from PIL import Image,ImageDraw
r=Path(__file__).resolve().parents[1];d=r/'out/qa/motion';d.mkdir(exist_ok=True)
for p in sorted((r/'assets/clips').glob('*.mp4')):
 out=d/(p.stem+'.jpg')
 if not out.exists():subprocess.run(['ffmpeg','-v','error','-y','-i',str(p),'-vf','fps=1,scale=400:-1,tile=5x1','-frames:v','1',str(out)],check=True)
shots=[s for s in json.load(open(r/'compositor/timeline.json'))['shots']if s['source']=='V']
for k in range(0,len(shots),5):
 im=Image.new('RGB',(2000,250*10),'#141413');dr=ImageDraw.Draw(im)
 for j,s in enumerate(shots[k:k+5]):
  for take in [1,2]:
   p=d/f'{s["id"]}_take{take}.jpg';y=(j*2+take-1)*250
   if p.exists():im.paste(Image.open(p),(0,y+25));dr.text((10,y+4),p.stem,fill='white')
 im.save(d/f'batch-{k//5+1}.jpg')
