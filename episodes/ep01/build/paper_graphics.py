# /// script
# requires-python = ">=3.11"
# dependencies = ["Pillow>=10"]
# ///
"""Author physical paper inserts and exact replacement states for COMMON ROOM.

Uses a clean photographic top-down ash tabletop as substrate. The papers,
folds, slots, labels and tab occlusions are deterministic authored geometry.
No generation calls. Run `uv run <this file> [--background <local-image>]`.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import os
import random
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont, ImageOps

ROOT=Path(__file__).resolve().parents[3]
BUILD=ROOT/'episodes/ep01/build'
OUT=ROOT/'work/ep01/paper'
W,H=1920,1080
FONT_EN=Path('/System/Library/Fonts/Supplemental/Courier New.ttf')
FONT_ZH=Path('/System/Library/Fonts/Hiragino Sans GB.ttc')
PAPER=(228,221,202,255)
LIGHT=(241,235,220,255)
INK=(66,66,60,255)
BLUE=(57,78,92,255)
CLAY=(142,91,68,255)


def font(size,zh=False):
    p=FONT_ZH if zh else FONT_EN
    if not p.exists():
        raise FileNotFoundError(p)
    return ImageFont.truetype(str(p),size)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save_json(path,obj):
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')


def text(layer,xy,label,size=32,colour=INK,zh=False,anchor='la'):
    ImageDraw.Draw(layer).text(xy,label,font=font(size,zh),fill=colour,anchor=anchor)


def destination_mark(base,cx,cy,address,scale=1.0):
    """Literal destination sketch printed in ink, not a new abstract system symbol."""
    d=ImageDraw.Draw(base)
    if address.startswith('RING'):
        col=(159,79,62,255)
        r=18*scale
        d.ellipse((cx-r,cy-r,cx+r,cy+r),outline=col,width=3)
        ellipse=Image.new('RGBA',(W,H),(0,0,0,0))
        ed=ImageDraw.Draw(ellipse)
        ed.ellipse((cx-39*scale,cy-10*scale,cx+39*scale,cy+10*scale),outline=col,width=3)
        # A single sloping ring reproduces the visible outside world's shape.
        crop=ellipse.crop((int(cx-50*scale),int(cy-35*scale),int(cx+50*scale),int(cy+35*scale)))
        crop=crop.rotate(-18,resample=Image.Resampling.BICUBIC)
        base.alpha_composite(crop,(int(cx-50*scale),int(cy-35*scale)))
    else:
        col=(78,101,115,255)
        for dx in (-24,0,24):
            d.line((cx+(dx+7)*scale,cy-20*scale,cx+(dx-7)*scale,cy+20*scale),fill=col,width=4)


def center_label(layer,box,en,zh,size=32):
    x0,y0,x1,y1=box
    cx=(x0+x1)/2
    text(layer,(cx,y0),en,size,anchor='ma')
    text(layer,(cx,y0+size+14),zh,max(24,size-6),zh=True,anchor='ma')


def paper_polygon(base,points,fill=PAPER,shadow=True):
    if shadow:
        shade=Image.new('RGBA',(W,H),(0,0,0,0))
        ImageDraw.Draw(shade).polygon([(x-5,y+10) for x,y in points],fill=(27,24,18,75))
        base.alpha_composite(shade.filter(ImageFilter.GaussianBlur(7)))
    skin=Image.new('RGBA',(W,H),(0,0,0,0))
    draw=ImageDraw.Draw(skin)
    draw.polygon(points,fill=fill,outline=(130,121,101,210),width=2)
    # Low-amplitude static paper fibres: exact seed, confined to the paper mask.
    mask=skin.getchannel('A')
    rng=random.Random(17)
    fibres=Image.new('RGBA',(W,H),(0,0,0,0))
    d=ImageDraw.Draw(fibres)
    minx,maxx=int(min(x for x,y in points)),int(max(x for x,y in points))
    miny,maxy=int(min(y for x,y in points)),int(max(y for x,y in points))
    for _ in range(max(0,(maxx-minx)*(maxy-miny)//1700)):
        x=rng.randrange(max(0,minx),min(W,maxx));y=rng.randrange(max(0,miny),min(H,maxy))
        d.line((x,y,x+rng.randrange(2,7),y),fill=(117,103,81,10),width=1)
    fibres.putalpha(ImageChops.multiply(fibres.getchannel('A'),mask))
    skin.alpha_composite(fibres)
    base.alpha_composite(skin)


def paper_rect(base,box,fill=PAPER,cut=5):
    x0,y0,x1,y1=box
    paper_polygon(base,[(x0+cut,y0),(x1,y0+2),(x1-2,y1),(x0,y1-2)],fill)


def crease(base,a,b):
    d=ImageDraw.Draw(base)
    d.line((a,b),fill=(115,109,96,130),width=2)
    d.line(((a[0]+1,a[1]+2),(b[0]+1,b[1]+2)),fill=(248,244,228,190),width=2)


def houseletter(base,box,owner,colour,address=None):
    x0,y0,x1,y1=box;cx=(x0+x1)/2
    paper_rect(base,box)
    # The enclosure is its own folded paper, with tucked side folds and a top flap.
    crease(base,(x0+32,y0+186),(x0+32,y1-22))
    crease(base,(x1-33,y0+186),(x1-33,y1-22))
    crease(base,(x0+34,y1-107),(x1-34,y1-107))
    d=ImageDraw.Draw(base)
    d.line((x0+32,y1-107,cx,y1-29,x1-33,y1-107),fill=(133,124,105,180),width=2)
    paper_polygon(base,[(x0+7,y0+6),(x1-7,y0+6),(x1-25,y0+145),(cx,y0+184),(x0+25,y0+145)],fill=LIGHT,shadow=False)
    crease(base,(x0+7,y0+6),(x1-7,y0+6))
    text(base,(cx,y0+60),owner,42,colour,anchor='ma')
    if address:
        text(base,(cx,y0+117),address,27,anchor='ma')
        destination_mark(base,cx,y0+198,address,scale=.85)
    # Owner identity is a tiny edge thread, not a colored interface container.
    d.line((x0+18,y0+225,x0+18,y1-142),fill=colour,width=4)


def slit(base,x,y,width):
    d=ImageDraw.Draw(base)
    d.line((x,y,x+width,y),fill=(46,43,35,255),width=6)
    d.line((x,y+4,x+width,y+4),fill=(248,242,225,255),width=2)


def tab(base,x,y,width,height,owner,address,colour,clip_y=None,loose=False):
    """Pointed paper tongue; clip hides its tip beneath a genuine dark slit."""
    layer=Image.new('RGBA',(W,H),(0,0,0,0))
    p=[(x,y),(x+width,y+2),(x+width,y+height-21),(x+width/2,y+height),(x,y+height-21)]
    paper_polygon(layer,p,fill=(236,231,214,255),shadow=True)
    d=ImageDraw.Draw(layer)
    d.line((x+9,y+8,x+9,y+height-28),fill=colour,width=5)
    text(layer,(x+width/2,y+38),owner,25,colour,anchor='ma')
    text(layer,(x+width/2,y+90),address,24,anchor='ma')
    destination_mark(layer,x+width/2,y+157,address,scale=.9)
    crease(layer,(x+4,y+height-57),(x+width-4,y+height-57))
    if clip_y is not None:
        mask=Image.new('L',(W,H),0)
        ImageDraw.Draw(mask).rectangle((0,0,W,clip_y),fill=255)
        layer.putalpha(ImageChops.multiply(layer.getchannel('A'),mask))
    base.alpha_composite(layer)
    if clip_y is not None:
        # Bottom edge of tongue disappears under a paper lip; no outlined tip below.
        d=ImageDraw.Draw(base)
        d.line((x-7,clip_y+2,x+width+7,clip_y+2),fill=(53,49,39,255),width=4)
        d.line((x-7,clip_y+5,x+width+7,clip_y+5),fill=(242,235,216,255),width=2)


def room_token(base,box,en,zh,owner_colour=None):
    x0,y0,x1,y1=box
    paper_rect(base,box,fill=LIGHT)
    d=ImageDraw.Draw(base)
    # A pen-drawn room outline and one window; these are physical architectural marks.
    d.rectangle((x0+19,y0+21,x1-19,y1-24),outline=(83,81,72,255),width=3)
    d.line((x0+39,y0+21,x1-40,y0+21),fill=(234,234,216,255),width=7)
    d.line((x0+39,y0+17,x1-40,y0+17),fill=(82,81,72,255),width=2)
    label_size=min(25, int((x1-x0-24)/(0.61*len(en))))
    center_label(base,(x0,y0+(y1-y0)*.43,x1,y1),en,zh,label_size)
    if owner_colour:
        d.line((x0+10,y0+20,x0+10,y1-20),fill=owner_colour,width=4)


def kitchen(base,box,slots=False):
    x0,y0,x1,y1=box
    paper_rect(base,box,fill=(233,226,207,255))
    # Long folded flap, attached bottom edge; one kitchen, with its actual counter plan.
    crease(base,(x0+8,y1-34),(x1-8,y1-34))
    center_label(base,(x0,y0+(112 if slots else 60),x1,y1),'KITCHEN','厨房',34)
    d=ImageDraw.Draw(base)
    yy=y1-103
    d.rectangle((x0+68,yy,x1-68,yy+29),outline=INK,width=2)
    d.rectangle((x0+86,yy+5,x0+118,yy+24),outline=INK,width=2)
    d.ellipse((x1-116,yy+5,x1-95,yy+25),outline=INK,width=2)
    if slots:
        slit(base,x0+70,y0+84,156)
        slit(base,x1-226,y0+84,156)


def graphic_k02(background,after):
    im=background.copy()
    houseletter(im,(300,112,1020,967),'EDA',BLUE)
    houseletter(im,(1270,242,1780,972),'SEN',CLAY,'RAIN 04')
    # Private-room flap. Its only active address tongue is changed by replacement.
    paper_rect(im,(417,384,904,852),fill=LIGHT)
    center_label(im,(417,577,904,760),'PRIVATE ROOM','私人房间',32)
    slit(im,560,474,205)
    if after:
        tab(im,579,268,168,257,'EDA','RING 12',BLUE,clip_y=474)
        tab(im,100,551,168,250,'EDA','RAIN 04',BLUE)
    else:
        tab(im,579,268,168,257,'EDA','RAIN 04',BLUE,clip_y=474)
        tab(im,1019,523,168,250,'EDA','RING 12',BLUE)
    return im


def graphic_k07(background,after):
    im=background.copy()
    houseletter(im,(105,142,555,950),'EDA',BLUE,'RING 12')
    houseletter(im,(1358,142,1808,950),'SEN',CLAY,'RAIN 04')
    kitchen(im,(735,540,1215,887),slots=True)
    room_token(im,(1507,386,1663,796),'NARROW ROOM','窄房间',CLAY)
    if after:
        room_token(im,(222,386,450,796),'LONG ROOM','长房间',BLUE)
    else:
        room_token(im,(638,133,866,543),'LONG ROOM','长房间',BLUE)
    return im


def graphic_k18(background,after):
    im=background.copy()
    houseletter(im,(90,135,635,944),'EDA',BLUE,'RING 12')
    houseletter(im,(1285,135,1830,944),'SEN',CLAY,'RAIN 04')
    # Private spaces stay visibly separate outside the one shared flap.
    room_token(im,(233,464,493,835),'LONG ROOM','长房间',BLUE)
    room_token(im,(1475,464,1639,835),'NARROW ROOM','窄房间',CLAY)
    kitchen(im,(627,360,1293,841),slots=True)
    # Two independent slits: Sen is seated in both states; Eda completes the second.
    tab(im,1084,209,124,282,'SEN','RAIN 04',CLAY,clip_y=444)
    if after:
        tab(im,714,209,124,282,'EDA','RING 12',BLUE,clip_y=444)
    else:
        tab(im,714,109,124,282,'EDA','RING 12',BLUE)
    return im


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--background',default='work/ep01/refs/ref_paper.png')
    a=ap.parse_args()
    bg_path=Path(a.background)
    if not bg_path.is_absolute():bg_path=ROOT/bg_path
    if not bg_path.exists():raise FileNotFoundError(f'Photographic tabletop is required: {bg_path}')
    with Image.open(bg_path) as src:
        src=ImageOps.exif_transpose(src).convert('RGB')
        if abs(src.width/src.height-W/H)>.03:
            raise ValueError('Background must be approximately16:9; do not silently crop unrelated substrate')
        bg=src.resize((W,H),Image.Resampling.LANCZOS).convert('RGBA')
    OUT.mkdir(parents=True,exist_ok=True)
    assets={}
    provenance={}
    for key,fn in [('k02',graphic_k02),('k07',graphic_k07),('k18',graphic_k18)]:
        for after in (False,True):
            aid=key+'_after' if after else key
            path=OUT/(aid+'.png')
            fn(bg,after).convert('RGB').save(path)
            assets[aid]=str(path.relative_to(ROOT))
            provenance[aid]={'sha256':sha(path),'background':str(bg_path.relative_to(ROOT)),
                             'background_sha256':sha(bg_path),'generator_sha256':sha(__file__),'state':'after' if after else 'before'}
    states={'02':[{'offset_frame':0,'asset':'k02'},{'offset_frame':48,'asset':'k02_after'}],
            '08':[{'offset_frame':0,'asset':'k07'},{'offset_frame':72,'asset':'k07_after'}],
            '29':[{'offset_frame':0,'asset':'k18'},{'offset_frame':72,'asset':'k18_after'}]}
    save_json(BUILD/'paper_assets.json',assets)
    save_json(BUILD/'paper_states.json',states)
    save_json(OUT/'provenance.json',provenance)
    print('Authored six physical-paper states; cuts at8.0,40.0,152.0seconds. Root merges paper_assets.json and paper_states.json.')


if __name__=='__main__':main()
