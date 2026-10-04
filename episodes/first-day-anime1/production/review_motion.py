from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess
from PIL import Image,ImageDraw,ImageFont
R=Path(__file__).resolve().parents[1];out=R.parents[1]/'work/first-day-anime1/motion-review';out.mkdir(parents=True,exist_ok=True)
font=ImageFont.truetype(str(R/'render_kit/fonts/Poppins-Regular.ttf'),18)
def review(sid):
 rows=[]
 for take in [1,2]:
  src=R/'assets/motion'/f'{sid}_take{take}.mp4';f=out/f'{sid}_{take}.jpg'
  subprocess.run(['ffmpeg','-v','error','-y','-i',str(src),'-vf','fps=2,scale=384:-1,tile=6x1','-frames:v','1',str(f)],check=True)
  im=Image.open(f).convert('RGB');ImageDraw.Draw(im).text((8,8),f'{sid} take {take}',font=font,fill='white',stroke_width=2,stroke_fill='black');rows.append(im)
 result=Image.new('RGB',(rows[0].width,rows[0].height*2),'#141413');result.paste(rows[0],(0,0));result.paste(rows[1],(0,rows[0].height));result.save(out/f'{sid}-compare.jpg');return sid
with ThreadPoolExecutor(max_workers=3)as pool:
 for sid in pool.map(review,['S01','S03','S04','S05','S16','S17','S18','S21','S22','S23','S24','S29','S30','S42','S44']):print(sid)
