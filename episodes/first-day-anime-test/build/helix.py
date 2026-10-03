"""A continuous 3D camera orbit, ribbon geometry and illustrated hero billboards."""
import math
import numpy as np
import cv2
from PIL import Image,ImageDraw,ImageFilter
from graphics import ASSET,logo,text,halo,CORAL,GOLD

def render(w,h,p,hero=None,background=None,lyrics=True):
    sky=(background.copy() if background is not None else Image.open(ASSET/'sky.png').convert('RGB').resize((w,h),Image.Resampling.LANCZOS))
    ease=p*p*(3-2*p)
    # 450-degree world-space orbit with simultaneous pullback and 20-degree roll.
    theta=2.5*math.pi*ease
    distance=1.3+34*p**2.1
    eye=np.array([distance*math.sin(theta),1.4+4*ease,distance*math.cos(theta)])
    target=np.array([0.,1.,0.]);forward=target-eye;forward/=np.linalg.norm(forward)
    right=np.cross(forward,[0,1,0]);right/=np.linalg.norm(right)
    up=np.cross(right,forward);focal=w*.85
    roll=math.radians(20)*ease
    def project(points):
        pts=np.asarray(points)-eye
        depth=pts@forward
        x=(pts@right)/np.maximum(depth,.1)*focal
        y=-(pts@up)/np.maximum(depth,.1)*focal
        return np.column_stack([w/2+x*math.cos(roll)-y*math.sin(roll),h*.48+x*math.sin(roll)+y*math.cos(roll)]),depth
    polys=[]
    palette=['#D97757','#E4A76E','#FFD9A8','#9CC8C3','#6A9BCC','#B79BC5']
    # Paired hair ribbons grow into a prism; curved strips have width and depth.
    for k in range(12):
        u=np.linspace(0,1,95)
        angle=u*math.pi*3+k*math.pi/6+theta*.10
        radius=.5+(3+13*ease)*u
        yy=2.0+np.sin(u*math.pi*2+k*.35)*2.2+u*2.5
        xyz=np.column_stack([radius*np.cos(angle),yy,radius*np.sin(angle)])
        width=(.012+.075*u)*min(1,p*4)
        left=xyz.copy();rightp=xyz.copy();left[:,1]-=width;rightp[:,1]+=width
        a,da=project(left);b,db=project(rightp)
        # The prism trails converge into the twelve rays at the completion beat.
        # The authoritative SVG is composited over them to finish the exact mark.
        morph=max(0,min(1,(p-.66)/.16));morph=morph*morph*(3-2*morph)
        if morph:
            ray=k*math.pi/6
            direction=np.array([math.cos(ray),math.sin(ray)])
            normal=np.array([-direction[1],direction[0]])
            centre=np.array([w*.75,h*.28])
            target=centre+(h*.235*(.10+.90*u))[:,None]*direction
            half=(h*.011*(1-.25*u))[:,None]*normal
            a=a*(1-morph)+(target-half)*morph
            b=b*(1-morph)+(target+half)*morph
        for j in range(len(u)-1):
            if min(da[j],db[j],da[j+1],db[j+1])>1.2:
                polys.append(((da[j]+da[j+1])/2,[tuple(a[j]),tuple(a[j+1]),tuple(b[j+1]),tuple(b[j])],palette[k%len(palette)]))
    center,dep=project([[0,1,0]])
    scale=min(h*2.8,3.0/dep[0]*focal)
    # Unlike thumbnail(), resize permits the opening face to fill the screen.
    sprite=None
    if hero is not None:
        ratio=scale/hero.height
        sprite=hero.resize((max(1,round(hero.width*ratio)),max(1,round(scale))),Image.Resampling.LANCZOS)
    # The hero is an illustrated camera-facing card, the surrounding space is 3D.
    def paint_hero():
        if sprite is None:return
        anchor=.13+.29*min(1,p*2)
        pos=(int(center[0,0]-sprite.width/2),int(center[0,1]-sprite.height*anchor))
        sky.paste(sprite,pos,sprite)
        halo(sky,(center[0,0],pos[1]+sprite.height*.06),sprite.width*.3,theta, max(8,w/1920*20),max(0,1-p*1.8))
    polys.sort(reverse=True,key=lambda row:row[0])
    ribbons=Image.new('RGBA',(w,h))
    d=ImageDraw.Draw(ribbons)
    painted=False
    for depth,poly,col in polys:
        if depth<dep[0] and not painted:paint_hero();painted=True
        rgb=tuple(bytes.fromhex(col[1:]))
        d.polygon(poly,fill=(*rgb,150 if background is not None else 210))
    if not painted:paint_hero()
    glow=ribbons.filter(ImageFilter.GaussianBlur(max(1,w/250)))
    sky.paste(glow,(0,0),glow)
    sky.paste(ribbons,(0,0),ribbons)
    if p<.43:
        # The text ring grows past the camera at 32.0 s (p ~= .374).
        r=w*(.17+1.6*(min(1,p/.374)**3))
        halo(sky,(w*.5,h*.37),r,p*5,w/1920*(23+85*p),max(0,1-p/.43))
    # The completed official spark occupies the distant sky in the final phase.
    if p>.68:
        op=min(1,(p-.68)/.19)
        bloom=Image.new('RGBA',(w,h))
        logo(bloom,(w*.75,h*.28),h*.49,opacity=op*.45,color=GOLD)
        bloom=bloom.filter(ImageFilter.GaussianBlur(max(1,w/120)))
        sky.paste(bloom,(0,0),bloom)
        logo(sky,(w*.75,h*.28),h*.47,opacity=op*.94)
        # Restore the tiny hero in front of the sun.
        if p>.82:paint_hero()
    # Fixed world-space lyric plane: projected with the same camera as ribbons.
    if lyrics and p>.1:
        layer=Image.new('RGBA',(1600,170))
        text(layer,'第一天的纯真色彩它总是',(800,85),85,'#FAF9F5',stroke=2)
        # Suspended in the plane x=-4, oriented toward the final camera position.
        corners,depth=project([[-4,0,12],[-4,0,-12],[-4,-2.55,-12],[-4,-2.55,12]])
        if min(depth)>.3:
            matrix=cv2.getPerspectiveTransform(np.float32([[0,0],[1600,0],[1600,170],[0,170]]),corners.astype(np.float32))
            projected=Image.fromarray(cv2.warpPerspective(np.array(layer),matrix,(w,h)))
            sky.paste(projected,(0,0),projected)
        foreground=Image.new('RGBA',(w,h));d=ImageDraw.Draw(foreground)
        for depth,poly,col in polys:
            if depth<dep[0]*.8:d.polygon(poly,fill=(*tuple(bytes.fromhex(col[1:])),140))
        sky.paste(foreground,(0,0),foreground)
    if lyrics and p<.30:
        # Keep the lyric anchor readable as the camera exits the pupil, then
        # yield to its world-space counterpart as the camera passes the halo.
        label=Image.new('RGBA',(w,h))
        text(label,'第一天的纯真色彩它总是',(w*.5,h*.83),w/1920*54,'#FAF9F5',stroke=2)
        opacity=min(1,(p+.01)*35,max(0,(.30-p)/.08))
        label.putalpha(label.getchannel('A').point(lambda a:int(a*opacity)))
        sky.paste(label,(0,0),label)
    return sky
