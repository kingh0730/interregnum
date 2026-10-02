from pathlib import Path
import cv2,json
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[3];p=root/'work/first-day-mix/production/video';out=root/'work/first-day-mix/production/qa/motion';out.mkdir(parents=True,exist_ok=True);summary={}
for path in sorted(p.glob('*.mp4')):
 cap=cv2.VideoCapture(str(path));n=int(cap.get(cv2.CAP_PROP_FRAME_COUNT));fps=cap.get(cv2.CAP_PROP_FPS);dur=n/fps
 sheet=Image.new('RGB',(1600,520),'#20232b');dr=ImageDraw.Draw(sheet)
 for j in range(8):
  f=min(n-1,round(j*(n-1)/7));cap.set(cv2.CAP_PROP_POS_FRAMES,f);ok,a=cap.read();assert ok
  im=Image.fromarray(cv2.cvtColor(a,cv2.COLOR_BGR2RGB));im.thumbnail((400,225));x=j%4*400;y=j//4*260
  sheet.paste(im,(x,y));dr.text((x+10,y+231),f'{path.stem} {f/fps:.2f}s / {f}',fill='white')
 sheet.save(out/(path.stem+'-full.jpg'),quality=94);cap.release();summary[path.stem]={'frames':n,'fps':fps,'duration':dur}
(root/'episodes/first-day-mix/production/clip-metadata.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary))
