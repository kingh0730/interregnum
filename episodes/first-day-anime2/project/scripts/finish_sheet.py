"""Apply code-authored brand ornaments without asking the image model to draw logos."""
from pathlib import Path
from io import BytesIO
import json
import re
import subprocess
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
raw=(ROOT/'assets/brand/spark-source.svg').read_text()
svg=re.sub(r'fill="[^"]+"','fill="#D97757"',raw,count=1)
(ROOT/'assets/brand/spark.svg').write_text(svg)
im=Image.open(ROOT/'assets/sheets/opus-base.png').convert('RGBA')
# Normalized to the inspected 1536 x 1024 reference sheet.
pins=[(198,107,22),(407,102,22),(654,110,19),(1208,120,27),(1466,110,25),(1222,433,26),(1380,467,26),(1217,748,25),(1468,748,26)]
ties=[(159,231,23),(432,213,21),(1204,291,25),(1433,286,25),(1186,616,24),(1458,585,20),(1162,934,23),(1406,943,24)]
eyes=[(130,145,5),(176,138,5),(425,134,5),(463,145,5),(624,138,4),(1386,160,8),(1443,153,8),(1406,506,7),(1471,491,7),(1124,808,8),(1188,802,8),(1378,791,8),(1441,803,8)]
def stamp(x,y,size,color):
    source=svg.replace('#D97757',color)
    png=subprocess.check_output(['rsvg-convert','-w',str(size*3),'-h',str(size*3)],input=source.encode())
    icon=Image.open(BytesIO(png)).convert('RGBA')
    icon=icon.resize((size,size),Image.Resampling.LANCZOS)
    im.alpha_composite(icon,(round(x-size/2),round(y-size/2)))
for x,y,size in pins+ties:stamp(x,y,size,'#D97757')
for x,y,size in eyes:stamp(x,y,size,'#FAF9F5')
im.save(ROOT/'assets/sheets/opus.png')
(ROOT/'assets/sheets/opus-overlays.json').write_text(json.dumps({'source':'opus-base.png','spark':'../brand/spark.svg','pins':pins,'ties':ties,'eyes':eyes},indent=2))
im.crop((1024,640,1536,1024)).save(ROOT/'qa/opus-detail.png')
print(ROOT/'assets/sheets/opus.png')
