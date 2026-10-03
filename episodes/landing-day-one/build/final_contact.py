from pathlib import Path
from PIL import Image,ImageDraw
import json,subprocess,io,concurrent.futures
r=Path(__file__).resolve().parents[1];out=r.parents[1]/'renders/landing-day-one';movie=out/'landing-day-one-1440p60-master.mov';timeline=json.loads((r/'assets/timeline.json').read_text())
def grab(s):
 f=(s['start']+s['end']-1)//2
 raw=subprocess.check_output(['ffmpeg','-v','error','-threads','1','-ss',str(f/60),'-i',str(movie),'-frames:v','1','-vf','scale=320:180','-f','image2pipe','-vcodec','mjpeg','-'])
 return s['id'],f,Image.open(io.BytesIO(raw)).convert('RGB')
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(grab,timeline))
for page,start in enumerate(range(0,len(rows),35)):
 section=rows[start:start+35];sheet=Image.new('RGB',(1600,7*206),'#e8dfcf');d=ImageDraw.Draw(sheet)
 for i,(sid,f,im) in enumerate(section):
  x=i%5*320;y=i//5*206;sheet.paste(im,(x,y));d.text((x+8,y+183),f'{sid}  {f/60:.3f}s  f{f}',fill='#3a332c')
 sheet.save(out/f'contact-sheet-{page+1:02d}.jpg',quality=92)
print('Saved 69-shot contact sheets',flush=True)
