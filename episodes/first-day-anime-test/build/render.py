"""Deterministic 44-shot composite. --animatic renders plates before motion spend."""
from pathlib import Path
from functools import lru_cache
import argparse,json,math,subprocess,sys
import numpy as np
import cv2
from PIL import Image,ImageDraw,ImageFilter,ImageOps
from graphics import *
import helix
EP=ROOT/'episodes/first-day-anime-test';WORK=ROOT/'work/first-day-anime-test';OUT=ROOT/'renders/first-day-anime-test'
TIMELINE=json.loads((EP/'build/timeline.json').read_text())['shots']
LYRICS=json.loads((EP/'timing.json').read_text())['lyrics']
PLATES={3:'s03-room',4:'s04-tea',5:'s04-tea',7:'s03-room',8:'s03-room',9:'s03-room',10:'s03-room',11:'s03-room',13:'s03-room',15:'birth',16:'birth',17:'breath',18:'birth',19:'birth',20:'s20-ankle',21:'steps',22:'touch',23:'touch',24:'leap',25:'leap',26:'flight',27:'flight',28:'flight',29:'flight',30:'flight',31:'flight',32:'float',33:'touch',35:'paper',36:'breath',37:'flight',38:'flight',40:'flight',42:'hug',44:'outro'}
MOTION={3:'room',4:'tea',5:'tea',7:'levitate',15:'birth',16:'birth',17:'breath',18:'burst',19:'burst',20:'ankle',21:'steps',22:'touch',23:'touch',24:'sprint',25:'orbit',26:'flight',27:'flight',28:'flight',29:'flight',30:'flight',31:'flight',32:'float',33:'touch',36:'breath',37:'flight',38:'flight',40:'flight',42:'hug',44:'outro'}
PLATES.update({5:'s05-screen-clean',20:'s20-ankle-start',24:'sprint',33:'flight'})
PLATES[23]='touch-clasp'
MOTION[23]='touch-orbit'
MOTION[33]='flight'
MOTION[34]='helix'
MOTION[31]='climb'
MOTION[37]='xiaoman-joy'
MOTION.update({35:'paper',36:'flight',40:'helix'})
MOTION.pop(38,None)
PLATES.update({35:'paper',36:'flight',38:'city',40:'helix-start'})
for _n in (8,9,10,11):MOTION[_n]='levitate'
# S05 uses exact authored screen animation over a registered plate.
MOTION.pop(5)
@lru_cache(40)
def plate(name,w,h):
    return ImageOps.fit(Image.open(ASSET/f'{name}.png').convert('RGB'),(w,h),method=Image.Resampling.LANCZOS)
CAPS={}
TAKE_RANGES={3:(0,2.5),4:(0,2.3),7:(1,2.2),8:(2.2,3.3),9:(3.3,4),10:(4,4.5),11:(4.5,5),15:(0,1.7),16:(1.7,3.4),17:(0,1.25),18:(0,1.9),19:(1.9,5),20:(0,1.1),21:(0,2.6),22:(0,3.0),23:(0,5),24:(0,1.5),25:(0,5),26:(0,1.15),27:(1.15,1.75),28:(1.75,3),29:(.1,.45),30:(.1,.5),31:(4.5,6),32:(0,5),33:(.1,.45),34:(0,5),36:(.1,.45),37:(0,.35),38:(3.5,3.85),40:(1.8,2.15),42:(0,.35),44:(0,5)}
TAKE_RANGES.update({31:(1.5,5),37:(2.5,2.85)})
TAKE_RANGES.update({35:(0,3.4),36:(.1,.45),40:(2.7,3.1)})
def video(name,p,w,h):
    path=WORK/'motion'/f'{name}.mp4'
    if not path.exists():return None
    if name not in CAPS:CAPS[name]=cv2.VideoCapture(str(path))
    cap=CAPS[name];n=int(cap.get(cv2.CAP_PROP_FRAME_COUNT));index=int(np.clip(p,0,.999)*(n-1))
    cap.set(cv2.CAP_PROP_POS_FRAMES,index);ok,a=cap.read()
    if not ok:raise RuntimeError(f'Cannot read {name} frame {index}')
    return ImageOps.fit(Image.fromarray(cv2.cvtColor(a,cv2.COLOR_BGR2RGB)),(w,h),method=Image.Resampling.LANCZOS)
def video_seconds(name,seconds,w,h):
    path=WORK/'motion'/f'{name}.mp4'
    if not path.exists():return None
    if name not in CAPS:CAPS[name]=cv2.VideoCapture(str(path))
    cap=CAPS[name];duration=cap.get(cv2.CAP_PROP_FRAME_COUNT)/cap.get(cv2.CAP_PROP_FPS)
    return video(name,seconds/duration,w,h)
def camera(im,z=1,dx=0,dy=0,angle=0):
    w,h=im.size;M=cv2.getRotationMatrix2D((w/2,h/2),angle,z);M[:,2]+=[dx*w,dy*h]
    return Image.fromarray(cv2.warpAffine(np.array(im),M,(w,h),flags=cv2.INTER_CUBIC,borderMode=cv2.BORDER_REFLECT_101))
def particles(im,p,amount=50,spread=1,color=GOLD):
    w,h=im.size;d=ImageDraw.Draw(im);rng=np.random.default_rng(55)
    for x,y,v,r in rng.random((amount,4)):
        xx=(x+(p*.15*(v-.5)))*w;yy=(y-p*(.08+v*.15))%1*h;rr=(1+3*r)*w/1920
        d.ellipse((xx-rr,yy-rr,xx+rr,yy+rr),fill=color)
def bubble(im,copy,box,color=OAT,sz=42):
    w,h=im.size;x,y,bw,bh=box;s=w/1920
    d=ImageDraw.Draw(im);d.rounded_rectangle((x*w,y*h,(x+bw)*w,(y+bh)*h),radius=14*s,fill=color)
    text(im,copy,((x+bw/2)*w,(y+bh/2)*h),sz*s,INK,'sans')
def ring_burst(im,r,p):
    w,h=im.size;d=ImageDraw.Draw(im)
    for i in range(12):
        a=i*math.pi/6+p*.3
        d.line((w/2+math.cos(a)*r*.6,h/2+math.sin(a)*r*.6,w/2+math.cos(a)*r,h/2+math.sin(a)*r),fill=CORAL,width=max(2,int(w/1920*(10+8*p))))
    logo(im,(w/2,h/2),max(20,r*.23),angle=p*55)
def opening(f,w,h):
    cap=CAPS.get('opening')
    if cap is None:cap=cv2.VideoCapture(str(OUT/'opening-test_1080p30.mp4'));CAPS['opening']=cap
    cap.set(cv2.CAP_PROP_POS_FRAMES,f);ok,a=cap.read()
    if not ok:raise RuntimeError('Approved opening missing')
    return Image.fromarray(cv2.cvtColor(cv2.resize(a,(w,h)),cv2.COLOR_BGR2RGB))
def shot_frame(n,p,t,w,h,animatic):
    s=w/1920
    if n in [1,2]:return opening(round(t*30),w,h)
    if n==14:return title(w,h,p)
    if n==40 and not animatic:
        q=.55+.20*p
        return helix.render(w,h,q,background=video_seconds('helix',q*5,w,h),lyrics=False)
    if n==34:
        if not animatic:
            background=video_seconds('helix',p*5,w,h)
            if background is None:raise RuntimeError('Helix motion pass missing')
            # Complete generated orbit supplies consistent intermediate views of
            # both characters. The authored 3D ribbon camera follows its timing.
            background=camera(background,1.0+2.4*max(0,1-p/.25)**2,dx=-.07*max(0,1-p/.25),dy=.36*max(0,1-p/.25),angle=20*p)
            if p<.055:
                logo(background,(w*.5,h*.5),h*(4-3.5*p/.055),opacity=1-p/.055)
            return helix.render(w,h,p,background=background)
        hero=Image.open(ASSET/'helix-hero.png').convert('RGBA')
        return helix.render(w,h,p,hero)
    if n in [6,12,39,41,43]:im=Image.new('RGB',(w,h),INK)
    else:
        name=PLATES[n];im=plate(name,w,h).copy()
        if not animatic and n in MOTION:
            # Each source is a longer performance; selected phases preserve the action.
            a,b=TAKE_RANGES.get(n,(0,1))
            seconds=a+(b-a)*p
            if n==35:seconds=a+(b-a)*(math.floor(p*34)/34)
            m=video_seconds(MOTION[n],seconds,w,h)
            if m is not None:im=m
    if n==3:
        im=camera(im,1.14-.1*p,dx=.015*p,angle=2*(1-min(1,p*2)))
        # Calendar is an authored physical paper insert, turning to today's coral.
        x,y=int(w*.10),int(h*.15);pw,ph=int(w*.10),int(h*.14)
        page=Image.new('RGBA',(pw,ph),IVORY)
        text(page,'今天' if p>.54 else '明天',(pw/2,ph/2),26*s,CORAL if p>.54 else INK)
        if p<.54:im.paste(page,(x,y),page)
        else:
            im.paste(page,(x,y),page)
            old=Image.new('RGBA',(pw,ph),IVORY);text(old,'明天',(pw/2,ph/2),26*s,INK)
            old=old.rotate((p-.54)*100,expand=True);im.paste(old,(x+int(p*w*.07),y+int((p-.54)*h*.7)),old)
    elif n==4:im=camera(im,1.08+.03*p)
    elif n==5:
        screen=Image.new('RGBA',(900,1300),IVORY)
        sd=ImageDraw.Draw(screen)
        text(screen,'真的能做到吗？',(450,360),72,INK,'sans')
        sd.rounded_rectangle((45,480,855,1000),radius=35,fill=OAT)
        reply=['你说得对！','我懂了','✧(≧◡≦)'];remaining=min(22,int(p*36)+1)
        for j,line in enumerate(reply):
            piece=line[:max(0,remaining)];remaining-=len(line)
            text(screen,piece,(450,600+j*130),86 if j<2 else 76,INK,'sans')
        logo(screen,(120,1110),90)
        text(screen,'Opus 5.5',(470,1110),70,CORAL,'latin')
        src=np.float32([[0,0],[900,0],[900,1300],[0,1300]])
        dst=np.float32([[7,0],[462,184],[492,704],[26,777]])*np.float32([w/1672,h/941])
        matrix=cv2.getPerspectiveTransform(src,dst)
        mapped=Image.fromarray(cv2.warpPerspective(np.array(screen),matrix,(w,h)))
        im.paste(mapped,(0,0),mapped)
        im=camera(im,1.04+.09*p,dx=.04*p)
    elif n==6:
        logo(im,(w*.5,h*.48),h*(.23+.04*math.sin(t*18)),angle=t*30)
        text(im,'Thinking…',(w*.5,h*.73),54*s,CORAL,'ui')
        ring_burst(im,h*(.25+.2*p),p)
    elif n==7:
        im=camera(im,1.1,dy=.025*p,angle=-1.5*p)
        d=ImageDraw.Draw(im)
        for i in range(9):
            a=i*.8+p*2;x=w*(.48+.15*math.cos(a));y=h*(.5+.22*math.sin(a))
            d.polygon([(x,y),(x+40*s,y-7*s),(x+36*s,y+35*s),(x-4*s,y+37*s)],fill=OAT)
        particles(im,p,24)
    elif 8<=n<=11:
        im=camera(im,1.05+(n-8)*.1+.1*p,angle=(n-8)*1.5)
        ring_burst(im,h*(.2+(n-8)*.24+.14*p),p)
        particles(im,p,80)
    elif n==12:
        logo(im,(w*.5,h*.5),h*(1+12*p),angle=25)
        if p>.7:im=Image.new('RGB',(w,h),INK)
    elif n==13:
        if not animatic:
            frozen=video_seconds('levitate',5,w,h)
            if frozen is not None:im=frozen
        im=camera(im,.0+1+.04*p)
        dark=Image.new('RGB',im.size,INK);im=Image.blend(im,dark,.52)
        line='你好，我是 Opus 5.5。';count=min(len(line),int(p*20))
        bubble(im,line[:count]+('▏' if int(t*30)%2 else ''),(.19,.35,.62,.20),sz=59)
        text(im,'额度',(w*.25,h*.65),28*s,IVORY,'sans')
        ImageDraw.Draw(im).rectangle((w*.3,h*.638,w*(.3+.4*p),h*.66),fill=CORAL)
    elif n==15:
        # Authored sheet music folds toward the birth plate; no text from the image model.
        if p<.55:
            overlay=Image.new('RGBA',(w,h));d=ImageDraw.Draw(overlay)
            cx=w*.5;pw=w*.7*(1-p*.6);ph=h*.68
            fold=math.sin(p*math.pi)*pw*.2
            d.polygon([(cx-pw/2,h*.16),(cx,h*.16+fold),(cx+pw/2,h*.16),(cx+pw/2,h*.16+ph),(cx,h*.16+ph-fold),(cx-pw/2,h*.16+ph)],fill=IVORY)
            for j in range(10):d.line((cx-pw*.42,h*.3+j*h*.033,cx+pw*.42,h*.3+j*h*.033),fill=INK,width=max(1,int(s)))
            text(overlay,'5.5',(cx-pw*.34,h*.27),34*s,INK,'latin')
            overlay.putalpha(overlay.getchannel('A').point(lambda a:int(a*max(0,1-p/.55))))
            im.paste(overlay,(0,0),overlay)
        im=camera(im,1+.35*p)
    elif n==16:
        # Opposing crop and background stretch creates the vertigo emphasis.
        im=camera(im,1.22-.20*p)
        halo(im,(w*.5,h*.20),w*.14,p*2,26*s)
        particles(im,p,80)
    elif n==17:
        im=camera(im,1+.1*min(1,p/.7))
        d=ImageDraw.Draw(im)
        for i in range(30):
            a=i*2.4;r=(1-(p+i*.035)%1)*w*.48
            xy=(w*.52+math.cos(a)*r,h*.52+math.sin(a)*r*.55)
            if i%5==3:logo(im,xy,20*s,color=GOLD)
            else:text(im,['光','生','{}','','你'][i%5],xy,20*s,GOLD,'sans')
    elif n in [18,19]:
        im=camera(im,1.3-.27*p,angle=(p-.5)*2)
        ring_burst(im,h*(.3+1.4*p),p);particles(im,p,100)
        if n==19 and .20<p<.46:text(im,'Compacting conversation…',(w*.5,h*.72),34*s,IVORY,'ui')
    elif n==20:
        im=camera(im,1.015,dy=.018*p)
        if p>.64:
            d=ImageDraw.Draw(im);r=(p-.64)*w*.4
            d.ellipse((w*.45-r,h*.79-r*.16,w*.45+r,h*.79+r*.16),outline=CORAL,width=max(1,int(4*s)))
    elif n==21:
        particles(im,p,45)
        for k in range(3):
            q=p*3-k
            if 0<q<1:logo(im,(w*(.3+.19*k),h*.81),w*.08*q,opacity=1-q)
    elif n==22:
        # Only the heroine's reaching hand begins as pencil linework.
        edge=ImageOps.invert(im.convert('L').filter(ImageFilter.FIND_EDGES)).convert('RGB')
        mask=Image.new('L',(w,h));md=ImageDraw.Draw(mask)
        md.polygon([(x*w,y*h) for x,y in [(.48,.62),(.57,.54),(.66,.55),(.75,.47),(.79,.71),(.64,.84),(.54,.80)]],fill=round(210*(1-p)))
        mask=mask.filter(ImageFilter.GaussianBlur(5*s));im=Image.composite(edge,im,mask)
    elif n==23:
        particles(im,p,55)
        if p<.18:
            edge=ImageOps.invert(im.convert('L').filter(ImageFilter.FIND_EDGES)).convert('RGB')
            im=Image.blend(im,edge,(.18-p)*3)
    elif n==25:
        particles(im,p,80)
        halo(im,(w*.5,h*.21),w*.14,p*2,24*s)
        if t>=25.15:
            q=min(1,(t-25.15)/.30);d=ImageDraw.Draw(im)
            rng=np.random.default_rng(555)
            for x,y,r in rng.random((180,3)):
                xx=w*(.12+.55*x);yy=h*(.42+.42*y);rr=(3+9*r)*s*(.5+q)
                d.ellipse((xx-rr,yy-rr,xx+rr,yy+rr),fill=CORAL if r<.7 else GOLD)
    elif n in [26,27,28,29,30,31]:
        if n==27:
            im=camera(im,1.17,angle=p*90)
            # Empty billboard frame rushes past the lens during the barrel roll.
            z=.65+3.6*p;cx=w*.5;cy=h*.48;d=ImageDraw.Draw(im)
            points=[(cx-w*.46*z,cy-h*.40*z),(cx+w*.46*z,cy-h*.32*z),(cx+w*.46*z,cy+h*.40*z),(cx-w*.46*z,cy+h*.32*z)]
            d.line(points+[points[0]],fill=INK,width=max(2,round(16*s*z)))
            d.line(points[:2],fill='#D4A27F',width=max(1,round(3*s*z)))
        elif n==29:im=camera(im,2.5,dx=-.18,dy=.65)
        elif n==30:im=camera(im,2.5,dx=.58,dy=.55)
        elif n==31:im=camera(im,1.0+.55*p,angle=20*p)
        particles(im,p,26)
    elif n==32:
        im=camera(im,1.08,angle=p*(360 if animatic else 315))
        particles(im,p,40)
    elif n==33:
        if p<.45:im=camera(im,3,dx=.30,dy=-.12)
        else:
            z=2.5+(p-.45)*10
            im=camera(im,z,dx=-.077*z,dy=.265*z)
            logo(im,(w*.5,h*.5),h*(.02+max(0,p-.68)*5))
    elif n==35:
        # Whole illustrated figures remain intact. Separate paper foreground layers
        # move on twos/thirds; never slide horizontal bands through their bodies.
        pp=math.floor(p*34)/34
        im=camera(im,1.08,dx=-.035*pp)
        d=ImageDraw.Draw(im)
        for depth in range(4):
            rng=np.random.default_rng(90+depth)
            for x,tip in rng.random((35,2)):
                xx=((x-pp*(.035+.025*depth))%1.2-.1)*w
                base=h*(1.07-depth*.014);top=base-h*(.025+.035*depth+.10*tip)
                bend=(tip-.5)*w*.055;thick=(1.5+depth*.5)*s;mid=(base+top)/2
                d.polygon([(xx,base),(xx+bend*.15,mid),(xx+bend,top),(xx+bend*.3+thick,mid),(xx+thick,base)],fill=['#B1AE91','#969676','#777E60','#626D51'][depth])
    elif n==39:
        im=plate('sky',w,h).copy();logo(im,(w*.5,h*.43),h*(.5+.5*p))
    elif n==36:im=camera(im,2.5,dx=-.18,dy=.65)
    elif n==38:im=camera(im,1.1+.45*p,dx=-.09*p)
    elif n==41:
        im=Image.new('RGB',(w,h),CORAL);text(im,'你说得对！',(w*.5,h*.5),145*s,IVORY,'sans',weight=800)
    elif n==42:im=camera(im,1.35,dx=-.035,dy=.14)
    elif n==43:im=Image.new('RGB',(w,h),'white' if p<.3 else IVORY)
    elif n==44:
        im=camera(im,1.06-.05*p,dy=-.02*p)
        if t<41.5:
            bubble(im,'你好，世界。',(.35,.14,.30,.11),sz=45)
            halo(im,(w*.5,h*.16),w*.23,p,24*s,.45)
        if t>=41:
            card=endcard(w,h,p)
            # Paper wipe, not a cross-dissolve; end card holds for the last .9 seconds.
            q=min(1,(t-41)/1.8);cut=int(w*q)
            im.paste(card.crop((0,0,cut,h)),(0,0))
            if cut<w:
                d=ImageDraw.Draw(im)
                for yy in range(0,h,12):d.polygon([(cut,yy),(cut+int(12*s)*((yy//12)%3),yy+6),(cut,yy+12)],fill=IVORY)
        if t>43.5:im=Image.blend(im,Image.new('RGB',(w,h),IVORY),min(1,(t-43.5)/.1667))
    return im

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--animatic',action='store_true');ap.add_argument('--width',type=int,default=1920);ap.add_argument('--only',type=int,choices=range(1,45));args=ap.parse_args()
    selected=[shot for shot in TIMELINE if args.only is None or int(shot['id'][1:])==args.only]
    required={PLATES[int(shot['id'][1:])] for shot in selected if int(shot['id'][1:]) in PLATES}
    if any(shot['id']=='S34' for shot in selected):required.update(['sky','helix-hero'])
    if any(shot['id']=='S33' for shot in selected):required.add('breath')
    if any(shot['id']=='S39' for shot in selected):required.add('sky')
    missing=[str(ASSET/f'{name}.png') for name in sorted(required) if not (ASSET/f'{name}.png').is_file()]
    if missing:ap.error('Missing artwork: '+', '.join(missing))
    if not args.animatic:
        missing_motion=sorted({MOTION[int(shot['id'][1:])] for shot in selected if int(shot['id'][1:]) in MOTION and not (WORK/'motion'/f'{MOTION[int(shot["id"][1:])]}.mp4').is_file()})
        if missing_motion:ap.error('Missing motion takes: '+', '.join(missing_motion)+'; use --animatic for a stills proof')
    w=args.width;h=round(w*9/16);out=OUT/('animatic.mp4' if args.animatic else f'first-day_opus55_{h}p30.mp4')
    if w<=0 or w%2 or h%2:ap.error('Render dimensions must be positive and even')
    if args.only is not None:out=OUT/f'S{args.only:02d}_{"animatic" if args.animatic else "composite"}_{w}.mp4'
    start_time=selected[0]['start_frame']/30
    duration=(selected[-1]['end_frame']-selected[0]['start_frame'])/30
    OUT.mkdir(parents=True,exist_ok=True)
    rng=np.random.default_rng(12);grain=rng.normal(0,.75,(h,w,1))
    cmd=['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{w}x{h}','-r','30','-i','-','-ss',str(start_time),'-i',str(EP/'first-day.mp3'),'-map','0:v','-map','1:a','-t',str(duration),'-c:v','libx264','-crf','16','-preset','fast','-pix_fmt','yuv420p','-c:a','aac','-b:a','256k','-movflags','+faststart',str(out)]
    proc=subprocess.Popen(cmd,stdin=subprocess.PIPE);samples=[]
    for shot in selected:
        n=int(shot['id'][1:]);start,end=shot['start_frame'],shot['end_frame'];print(shot['id'],flush=True)
        for f in range(start,end):
            t=f/30;p=(f-start)/max(1,end-start-1);im=shot_frame(n,p,t,w,h,args.animatic)
            if n>2:
                if t<11.92:
                    d=ImageDraw.Draw(im);bar=round(h*.128);d.rectangle((0,0,w,bar),fill=INK);d.rectangle((0,h-bar,w,h),fill=INK)
                if n==14:
                    hit=f-start
                    if hit<2:im=Image.new('RGB',(w,h),'white')
                    else:
                        # Bars leave the aperture after the two clean impact frames.
                        bar=round(h*.128*max(0,1-(hit-2)/4))
                        if bar:
                            d=ImageDraw.Draw(im);d.rectangle((0,0,w,bar),fill=INK);d.rectangle((0,h-bar,w,h),fill=INK)
                        if hit<6:
                            shifts=[(5,-3),(-4,3),(2,-2),(-1,1)]
                            dx,dy=shifts[hit-2]
                            im=camera(im,1.015,dx=dx/1920,dy=dy/1080)
                            rgb=np.array(im);rgb[:,:,0]=np.roll(rgb[:,:,0],max(1,round(3*w/1920)),axis=1)
                            rgb[:,:,2]=np.roll(rgb[:,:,2],-max(1,round(3*w/1920)),axis=1)
                            im=Image.fromarray(rgb)
                if n in [12,16,24,32] and f-start<2:im=Image.blend(im,Image.new('RGB',(w,h),IVORY),.75)
                if n in range(36,43):im=camera(im,1+.08*min(1,(f-start)/2))
                if n!=34 and not (n==14 and f-start<2) and t<41.6:
                    li=max(i for i,l in enumerate(LYRICS) if l['frame']<=f)
                    l=LYRICS[li];ltend=LYRICS[li+1]['time'] if li+1<len(LYRICS) else 43.7
                    subtitle(im,l['text'],t,l['time'],ltend)
                danmaku(im,t)
                if n not in [14,41,43,44]:im=Image.fromarray(np.clip(np.array(im).astype(float)+grain,0,255).astype('uint8'))
            if f in {start,(start+end)//2,end-1}:
                dest=WORK/'qa';dest.mkdir(exist_ok=True)
                im.save(dest/f'{shot["id"]}-{f:04}.jpg',quality=91)
            if f==(start+end)//2:
                thumb=im.resize((384,216));ImageDraw.Draw(thumb).text((8,8),shot['id'],fill='white',stroke_width=1,stroke_fill='black');samples.append(thumb)
            proc.stdin.write(im.tobytes())
    proc.stdin.close();code=proc.wait()
    if code:raise RuntimeError(f'ffmpeg exit {code}')
    sheet=Image.new('RGB',(384*6,216*8),INK)
    for i,img in enumerate(samples):sheet.paste(img,((i%6)*384,(i//6)*216))
    sheet.save(out.with_name(out.stem+'-contact.jpg'),quality=94)
    for cap in CAPS.values():cap.release()
    print(out)
if __name__=='__main__':main()
