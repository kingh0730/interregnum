"""Render the required disposable timing cards, never a production-picture substitute."""
from pathlib import Path
import json
import subprocess
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
shots=json.loads((ROOT/'helper/shots.json').read_text())
sync=json.loads((ROOT/'helper/sync.json').read_text())
font=ImageFont.truetype(str(ROOT/'assets/fonts/Inter.ttf'),36)
small=ImageFont.truetype(str(ROOT/'assets/fonts/Inter.ttf'),20)
chinese=ImageFont.truetype(str(ROOT/'assets/fonts/NotoSerifSC.ttf'),28)
W,H=960,540
out=ROOT/'qa/timing_cards.mp4'
cmd=['ffmpeg','-y','-v','error','-f','rawvideo','-pixel_format','rgb24','-video_size',f'{W}x{H}','-framerate','30','-i','-','-i',str(ROOT.parent/'first-day.mp3'),'-map','0:v','-map','1:a','-c:v','libx264','-preset','fast','-crf','20','-pix_fmt','yuv420p','-c:a','copy','-t','43.7','-movflags','+faststart',str(out)]
p=subprocess.Popen(cmd,stdin=subprocess.PIPE)
colors=['#D97757','#D4A27F','#788C5D','#6A9BCB']
try:
    for f in range(1311):
        s=next(s for s in shots if s['f0']<=f<s['f1'])
        frozen=s['id']=='S10' or f>=1299
        shown=s['f0'] if s['id']=='S10' else min(f,1299)
        im=Image.new('RGB',(W,H),'#F0EEE6' if frozen else colors[shots.index(s)%4]);d=ImageDraw.Draw(im)
        d.text((48,40),'TIMING TEST / NOT FINAL ART',font=small,fill='#191919')
        d.text((48,140),s['id'],font=font,fill='#191919')
        d.text((48,200),f"{s['f0']}–{s['f1']-1}  /  {(s['f1']-s['f0'])/30:.3f} s",font=font,fill='#191919')
        d.text((48,280),f'Frame {shown:04d}  |  {shown/30:.3f} s',font=small,fill='#191919')
        for b in sync['beats']:
            x=48+b['t']/43.7*(W-96)
            d.line((x,H-65,x,H-45),fill='#191919',width=1)
        d.line((48,H-45,48+shown/1311*(W-96),H-45),fill='#FAF9F5',width=5)
        if frozen:d.text((48,345),'HELD FRAME',font=font,fill='#191919')
        else:
            lyric=next((l for l in sync['lyrics'] if l['t']<=f/30<l['end']),None)
            if lyric:d.text((48,365),lyric['text'],font=chinese,fill='#191919')
        p.stdin.write(im.tobytes())
finally:p.stdin.close()
if p.wait()!=0:raise RuntimeError('Timing-card encoding failed')
print(out)
