"""Retain review sheets and requested full-size anchors from final PNGs."""
from pathlib import Path
import json, shutil
from PIL import Image, ImageDraw

r = Path(__file__).resolve().parents[1]
frames = r / 'render_kit/frames'
out = r / 'production/qa'; (out / 'anchors').mkdir(exist_ok=True)
timing = json.loads((r / 'timing.json').read_text())
anchors = [0,30,60,336,338,357,358,359,366,430,460,528,550,622,640,672,720,754,755,800,875,920,930,952,990,1005,1014,1020,1070,1180,1205,1230,1255,1290,1310]
for f in anchors:
    shutil.copy2(frames / f'{f:05}.png', out / 'anchors' / f'{f:05}.png')
for page in range(4):
    selected = timing['shots'][page*12:(page+1)*12]
    sheet = Image.new('RGB', (1920, (len(selected)+2)//3*390), '#141413')
    draw = ImageDraw.Draw(sheet)
    for j, shot in enumerate(selected):
        f = (shot['frame'] + shot['end_frame'])//2
        x,y = j%3*640, j//3*390
        with Image.open(frames/f'{f:05}.png') as im: sheet.paste(im.convert('RGB').resize((640,360),Image.Resampling.LANCZOS),(x,y))
        draw.text((x+8,y+365),f"{shot['id']} / frame {f} / {f/30:.3f} s",fill='#FAF9F5')
    sheet.save(out/f'final-contact-{page+1}.jpg',quality=92)
print('Saved 35 full-size anchors and four final shot review sheets.')
