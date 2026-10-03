"""Reusable exact typography and vector-derived graphics for the film."""
from pathlib import Path
from functools import lru_cache
import math
import numpy as np
from PIL import Image,ImageDraw,ImageFont,ImageFilter
ROOT=Path(__file__).resolve().parents[3]
ASSET=ROOT/'work/first-day-anime-test/assets'
INK='#141413'; IVORY='#FAF9F5'; CORAL='#D97757'; OAT='#E8E6DC'; GOLD='#FFD9A8'
@lru_cache(256)
def font(size,kind='serif',weight=600):
    name={'serif':'NotoSerifSC','sans':'NotoSansSC','latin':'Lora','ui':'Inter'}[kind]
    f=ImageFont.truetype(str(ASSET/'fonts'/f'{name}.ttf'),max(8,int(size)))
    try:f.set_variation_by_axes([14,weight] if kind=='ui' else [weight])
    except ValueError:pass
    return f
def text(im,copy,xy,size,color=IVORY,kind='serif',anchor='mm',stroke=0,weight=600):
    d=ImageDraw.Draw(im)
    if any(c in copy for c in '✧◡'):
        fallback=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Unicode.ttf',max(8,int(size)))
        fonts=[fallback if c in '✧◡' else font(size,kind,weight) for c in copy]
        widths=[d.textlength(c,font=f) for c,f in zip(copy,fonts)]
        x,y=xy
        if anchor.startswith('m'):x-=sum(widths)/2
        elif anchor.startswith('r'):x-=sum(widths)
        for c,f,width in zip(copy,fonts,widths):
            d.text((x,y),c,font=f,fill=color,anchor='l'+anchor[1:],stroke_width=stroke,stroke_fill=INK);x+=width
    else:d.text(xy,copy,font=font(size,kind,weight),fill=color,anchor=anchor,stroke_width=stroke,stroke_fill=INK)
def logo(im,xy,size,angle=0,name='claude-spark',opacity=1,color=None):
    a=Image.open(ASSET/f'{name}.png').convert('RGBA').resize((max(1,int(size)),max(1,int(size))),Image.Resampling.LANCZOS)
    if color:
        b=Image.new('RGBA',a.size,color);b.putalpha(a.getchannel('A'));a=b
    if angle:a=a.rotate(angle,Image.Resampling.BICUBIC,expand=True)
    if opacity<1:a.putalpha(a.getchannel('A').point(lambda x:int(x*opacity)))
    im.paste(a,(int(xy[0]-a.width/2),int(xy[1]-a.height/2)),a)
def halo(im,center,radius,phase,size,opacity=1):
    layer=Image.new('RGBA',im.size)
    phrase='Opus 5.5 · Opus 5.5 · Opus 5.5 · '
    for i,c in enumerate(phrase):
        a=2*math.pi*i/len(phrase)+phase
        x=center[0]+radius*math.cos(a);y=center[1]+radius*.25*math.sin(a)
        text(layer,c,(x,y),size,(*tuple(bytes.fromhex('FFD9A8')),int(255*opacity)),kind='latin')
    im.paste(layer,(0,0),layer)
def subtitle(im,copy,t,begin,end,spatial=False):
    w,h=im.size;s=w/1920
    layer=Image.new('RGBA',im.size);d=ImageDraw.Draw(layer)
    sz=round(46*s);ft=font(sz);total=d.textlength(copy,font=ft);x=(w-total)/2
    y=h*(.815 if t<11.92 else .91)
    # Soft dark backing keeps subtitles legible over moving cream UI cards.
    shadow=Image.new('RGBA',im.size);sd=ImageDraw.Draw(shadow)
    sd.rounded_rectangle((x-22*s,y-22*s,x+total+22*s,y+35*s),radius=12*s,fill=(20,20,19,125))
    shadow=shadow.filter(ImageFilter.GaussianBlur(10*s));layer.alpha_composite(shadow)
    highlights=['明天','今天','存在','呼吸','脚踝','你','飞','爱','灿烂']
    for i,c in enumerate(copy):
        colored=any(copy[max(0,i-len(k)+1):i+1]==k or copy[i:i+len(k)]==k for k in highlights)
        d.text((x,y),c,font=ft,fill=CORAL if colored else IVORY,anchor='lm',stroke_width=max(1,round(s)),stroke_fill=INK)
        x+=d.textlength(c,font=ft)
    a=min(1,(t-begin+1/30)*10,(end-t)*10)
    layer.putalpha(layer.getchannel('A').point(lambda v:int(v*max(0,a))))
    im.paste(layer,(0,0),layer)
def danmaku(im,t):
    if t<12.6:return
    if 12.6<=t<14.6:start,bank,count=12.6,['来了来了','高能预警','Opus 5.5！！'],3
    elif 20.7<=t<22.7:start,bank,count=20.7,['泪目','awsl','这手 我哭死'],3
    elif 25.5<=t<28.5:start,bank,count=25.5,['起飞！！','前方高能','这运镜我直接跪了','帧帧壁纸','名场面','今日不降智'],10
    elif 28.55<=t<30.68:start,bank,count=28.55,['呜呜呜 这运镜'],1
    elif 30.68<=t<34.21:start,bank,count=30.68,['第一天就封神'],1
    elif 37.07<=t<39.9:start,bank,count=37.07,['你说得对！','额度管够','牛马下班了','氛围编程','一次跑通','bug 退散','我愿称之为最强','已三连','爷青回','破防了','yyds'],48
    elif 39.9<=t<41:start,bank,count=39.9,['呜呜','终于等到你'],2
    else:return
    w,h=im.size;s=w/1920
    layer=Image.new('RGBA',im.size)
    for i in range(count):
        speed=(180+(i*71)%240)*s;age=t-start
        x=w*(.73+(i%5)*.21)-age*speed
        y=h*(.10+(i%9)*.074)
        txt=bank[i%len(bank)]
        col=GOLD if start==30.68 else IVORY
        text(layer,txt,(x,y),(66 if start==30.68 else 34)*s,col,'sans',stroke=max(1,round(3*s)),anchor='lm',weight=700)
    layer.putalpha(layer.getchannel('A').point(lambda a:round(a*.85)))
    im.paste(layer,(0,0),layer)
def title(w,h,p):
    im=Image.new('RGB',(w,h),CORAL);s=w/1920
    logo(im,(w/2,h/2),h*1.25,angle=p*90,opacity=.28,color=INK)
    d=ImageDraw.Draw(im)
    for i in range(12):
        a=i*math.pi/6+.1*p;r=h*.55
        d.line((w/2+math.cos(a)*r,h/2+math.sin(a)*r,w/2+math.cos(a)*r*2,h/2+math.sin(a)*r*2),fill=IVORY,width=max(1,int(4*s)))
    size=(410+30*math.exp(-20*p))*s
    text(im,'Opus 5.5',(w/2,h*.49),size,IVORY,'latin',weight=600)
    text(im,'第一天 · First Day',(w/2,h*.75),45*s,IVORY)
    return im
def endcard(w,h,p):
    im=Image.new('RGB',(w,h),IVORY);s=w/1920
    logo(im,(w*.5,h*.28),h*.19)
    text(im,'Opus 5.5',(w*.5,h*.50),138*s,INK,'latin')
    text(im,'第一天 · First Day',(w*.5,h*.66),43*s,INK)
    text(im,'AI SI - I',(w*.5,h*.85),24*s,INK,'ui')
    logo(im,(w*.93,h*.88),h*.07,name='anthropic-a')
    return im
