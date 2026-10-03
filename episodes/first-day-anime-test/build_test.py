"""Opening S01/S02 proof. Run from repo root with .venv/bin/python."""
from pathlib import Path
import json, re, subprocess, math, csv
import numpy as np
import librosa
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import cv2

ROOT = Path(__file__).resolve().parents[2]
EP = Path(__file__).resolve().parent
WORK = ROOT / 'work/first-day-anime-test'
OUT = ROOT / 'renders/first-day-anime-test'
W,H,FPS = 1920,1080,30
FONT = WORK / 'assets/fonts/NotoSerifSC.ttf'

def analyze():
    y,sr=librosa.load(EP/'first-day.mp3',sr=22050)
    hop=220
    onset_env=librosa.onset.onset_strength(y=y,sr=sr,hop_length=hop)
    onsets=librosa.onset.onset_detect(onset_envelope=onset_env,sr=sr,hop_length=hop,units='time')
    tempo,beats=librosa.beat.beat_track(onset_envelope=onset_env,sr=sr,hop_length=hop,start_bpm=86,units='time')
    lyrics=[]
    for m in re.finditer(r'\[(\d+):(\d+\.\d+)\](.*)',(EP/'first-day.lrc').read_text()):
        t=int(m[1])*60+float(m[2]); lyrics.append(dict(time=t,frame=round(t*30),text=m[3]))
    rms=librosa.feature.rms(y=y,frame_length=1024,hop_length=hop)[0]
    ts=librosa.frames_to_time(np.arange(len(rms)),sr=sr,hop_length=hop)
    before=float(np.mean(rms[(ts>=10.8)&(ts<11.4)]))
    gap=float(np.mean(rms[(ts>=11.45)&(ts<11.92)]))
    nearest=float(onsets[np.argmin(abs(onsets-1.05))])
    cut=round(nearest*30) if abs(nearest-1.05)<=.1 else round(1.05*30)
    data=dict(source='first-day.mp3',duration=len(y)/sr,fps=30,lyrics=lyrics,
        detected_bpm=float(np.asarray(tempo).reshape(-1)[0]),detected_beats=beats.tolist(),onsets=onsets.tolist(),
        bars={'source':'director grid, provisional metrical interpretation', 'times':np.arange(2.82,len(y)/sr,2.79).tolist()},
        stop_time={'window':[11.45,11.92],'rms_before':before,'rms_gap':gap,'drop_fraction':1-gap/before},
        opening={'s02_frame':cut,'target_seconds':1.05,'nearest_onset':nearest,'end_frame':85,'lyric_anchor':2.84})
    (EP/'timing.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axs=plt.subplots(2,1,figsize=(15,5))
    axs[0].plot(np.arange(len(y))[::100]/sr,y[::100],lw=.4,color='#788C5D')
    for l in lyrics: axs[0].axvline(l['time'],color='#D97757',alpha=.5,lw=.6)
    axs[0].set(title='First Day: waveform and locked lyric anchors',xlim=(0,len(y)/sr))
    axs[1].plot(ts,rms,color='#141413'); axs[1].axvspan(11.45,11.92,color='#D97757',alpha=.25)
    axs[1].set(xlim=(10.5,12.5),title=f'Stop-time RMS reduction: {1-gap/before:.1%}',xlabel='Seconds')
    fig.tight_layout(); fig.savefig(OUT/'timing.png',dpi=130); plt.close(fig)
    return data

def font(n):
    f=ImageFont.truetype(str(FONT),n)
    f.set_variation_by_axes([600])
    return f

def feed(scroll=0,thinking=False):
    im=Image.new('RGB',(1200,1600),'#141413'); d=ImageDraw.Draw(im)
    messages=['再等等，下个版本更强','明天就发布了','Opus 5.5 什么时候出？','等 5.5 再说']
    for j in range(16):
        yy=int(140+j*230-scroll)
        if yy < -200 or yy>1600: continue
        xx=90+(j%2)*105
        d.rounded_rectangle((xx,yy,xx+900,yy+155),radius=18,fill='#E8E6DC')
        d.text((xx+42,yy+44),messages[j%4],font=font(48),fill='#141413')
    if thinking:
        yy=int(140+16*230-scroll)
        d.rounded_rectangle((150,yy,1050,yy+170),radius=18,fill='#E8E6DC')
        d.text((300,yy+50),'Thinking…',font=font(54),fill='#D97757')
        # UI text asterisk, not a substitute for the later official logo lockup.
        for angle in range(0,180,30):
            a=math.radians(angle)
            d.line((253-23*math.cos(a),yy+87-23*math.sin(a),253+23*math.cos(a),yy+87+23*math.sin(a)),fill='#D97757',width=5)
    return im

def render(data):
    plate=Image.open(WORK/'assets/s01-glasses.png').convert('RGB').resize((W,H))
    # Perspective map fits the blank screen reflection in the supplied plate.
    src=np.float32([[0,0],[1200,0],[1200,1600],[0,1600]])
    dst=np.float32([[859,615],[1327,563],[1350,745],[904,814]])
    mat=cv2.getPerspectiveTransform(src,dst)
    reflected=np.array(feed())
    reflection=cv2.warpPerspective(reflected,mat,(W,H))
    mask=cv2.warpPerspective(np.ones((1600,1200),np.float32),mat,(W,H))*.65
    base=np.uint8(np.array(plate)*(1-mask[:,:,None])+reflection*mask[:,:,None])
    cut=data['opening']['s02_frame']; frames=85
    proc=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r','30','-i','-',
        '-i',str(EP/'first-day.mp3'),'-map','0:v','-map','1:a','-t',str(frames/FPS),'-c:v','libx264','-crf','16',
        '-preset','fast','-pix_fmt','yuv420p','-c:a','aac','-b:a','256k','-movflags','+faststart',str(OUT/'opening-test_1080p30.mp4')],stdin=subprocess.PIPE)
    samples=[]
    for f in range(frames):
        t=f/FPS
        if f<cut:
            p=f/max(1,cut-1)
            # Lens dive is a motivated acceleration, not a dissolve.
            z=1+.13*p+5.3*p**5
            cx=960+(1100-960)*p; cy=540+(680-540)*p
            M=np.float32([[z,0,W/2-z*cx],[0,z,H/2-z*cy]])
            arr=cv2.warpAffine(np.array(plate),M,(W,H),flags=cv2.INTER_CUBIC,borderMode=cv2.BORDER_REFLECT)
            combined=np.vstack([M,[0,0,1]])@mat
            reflection=cv2.warpPerspective(reflected,combined,(W,H),flags=cv2.INTER_CUBIC)
            mask=cv2.warpPerspective(np.ones((1600,1200),np.float32),combined,(W,H))*(.55+.45*p**3)
            arr=np.uint8(arr*(1-mask[:,:,None])+reflection*mask[:,:,None])
            im=Image.fromarray(arr)
        else:
            p=(f-cut)/(frames-cut-1)
            # Accelerate through repeated waiting bubbles; land at Thinking at 2.50.
            q=min(1,(t-cut/FPS)/(2.50-cut/FPS))
            scroll=3160*(q*q*(3-2*q))
            ui=feed(scroll,True)
            im=Image.new('RGB',(W,H),'#141413')
            ui=ui.resize((1250,1667),Image.Resampling.LANCZOS)
            im.paste(ui,(335,-240))
            if .15<q<.94: im=im.filter(ImageFilter.GaussianBlur(1.1))
            if q>=1:
                z=1+.015*(t-2.5)/.34
                im=Image.fromarray(cv2.warpAffine(np.array(im),np.float32([[z,0,W/2*(1-z)],[0,z,H/2*(1-z)]]),(W,H)))
        d=ImageDraw.Draw(im)
        bar=138
        d.rectangle((0,0,W,bar),fill='#141413'); d.rectangle((0,H-bar,W,H),fill='#141413')
        # Full lyric remains anchored at zero; highlighted words follow the bible.
        parts=[('你说活在','#FAF9F5'),('明天','#D97757'),('活在期待','#FAF9F5')]
        ft=font(51); widths=[d.textlength(s,font=ft) for s,c in parts]; x=(W-sum(widths))/2
        alpha=min(1,(f+1)/3)
        for (s,c),width in zip(parts,widths):
            d.text((x,864),s,font=ft,fill=c,stroke_width=1,stroke_fill='#141413'); x+=width
        if f in [0,15,cut-1,cut,50,65,75,84]:
            im.save(WORK/f'frame-{f:03d}.jpg',quality=94)
            thumb=im.resize((640,360)); ImageDraw.Draw(thumb).text((12,12),f'{f:03d} / {t:.2f}s',fill='white'); samples.append(thumb)
        proc.stdin.write(im.tobytes())
    proc.stdin.close()
    if proc.wait(): raise RuntimeError('ffmpeg failed')
    sheet=Image.new('RGB',(640*4,360*2))
    for i,im in enumerate(samples):sheet.paste(im,((i%4)*640,(i//4)*360))
    sheet.save(OUT/'opening-contact-sheet.jpg',quality=94)
    subprocess.run(['ffmpeg','-y','-v','error','-i',str(OUT/'opening-test_1080p30.mp4'),'-vf','scale=960:540','-c:v','libx264','-crf','20','-c:a','copy',str(OUT/'opening-test_540p.mp4')],check=True)

if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    data=analyze(); print(json.dumps(data['stop_time']),flush=True); render(data)
