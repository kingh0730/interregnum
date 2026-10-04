"""Offline, repeatable audit of the supplied MV edit; does not approve final-picture QA."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault('MPLCONFIGDIR', str(ROOT / 'qa/.matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont
from scipy.io import wavfile

def main():
    qa = ROOT / 'qa'
    qa.mkdir(exist_ok=True)
    shots = json.loads((ROOT / 'helper/shots.json').read_text())
    sync = json.loads((ROOT / 'helper/sync.json').read_text())
    audio = ROOT.parent / 'first-day.mp3'
    verify = subprocess.run([sys.executable, str(ROOT.parent/'files/verify_sync.py'), str(audio)], cwd=qa, capture_output=True, text=True, check=True)
    (qa/'verify_sync.txt').write_text(verify.stdout)
    if not any(line.startswith('PASS') for line in verify.stdout.splitlines()):
        raise RuntimeError(verify.stdout)
    assert len(shots) == 52
    assert shots[0]['f0'] == 0 and shots[-1]['f1'] == 1311
    for a,b in zip(shots, shots[1:]):
        assert a['f1'] == b['f0'], (a['id'],b['id'])
    grid = [0] + sync['eighths']
    measured_onsets = json.loads((qa/'onsets.json').read_text())
    grid += measured_onsets['kicks']
    cuts = [{'shot':s['id'],'frame':s['f0'],'nearest_grid_error_frames':round(min(abs(s['f0']/30-t) for t in grid)*30,5)} for s in shots]
    assert max(c['nearest_grid_error_frames'] for c in cuts) <= 1
    probe = json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(audio)]))
    report = {'scope':'Supplied timeline and original audio only; final rendered sync is not yet tested.', 'audio_sha256':hashlib.sha256(audio.read_bytes()).hexdigest(), 'audio_probe':probe,'sync_verification':verify.stdout,'shots':len(shots),'frames':1311,'duration_seconds':1311/30,'cuts':cuts}
    (qa/'preflight.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    with tempfile.TemporaryDirectory(prefix='opus55-') as tmp:
        wav=Path(tmp)/'wave.wav'
        subprocess.run(['ffmpeg','-y','-v','error','-i',str(audio),'-ac','1','-ar','22050',str(wav)],check=True)
        sr,x=wavfile.read(wav);x=x.astype(float)/32768
        fig,ax=plt.subplots(figsize=(20,5),facecolor='#FAF9F5')
        ax.set_facecolor('#FAF9F5');stride=100
        ax.plot(np.arange(0,len(x),stride)/sr,x[::stride],color='#191919',lw=.35)
        for b in sync['beats']: ax.axvline(b['t'],color='#D97757',alpha=.65,lw=.6)
        ax.axvspan(339/30,359/30,color='#788C5D',alpha=.25,label='S10 held picture')
        ax.set(xlim=(0,43.7),xlabel='Seconds',ylabel='Decoded original MP3 amplitude',title='88 BPM · 1.062 s offset · audio verifier PASS')
        ax.legend();fig.tight_layout();fig.savefig(qa/'waveform_grid.png',dpi=110);plt.close(fig)
    fig,axs=plt.subplots(2,1,figsize=(18,7),facecolor='#FAF9F5')
    for i,s in enumerate(shots):
        axs[0].barh(0,(s['f1']-s['f0'])/30,left=s['f0']/30,color=['#D97757','#D4A27F','#788C5D','#6A9BCB'][i%4])
        axs[0].text((s['f0']+s['f1'])/60,0,s['id'],ha='center',va='center',rotation=90,fontsize=7)
    axs[0].set(xlim=(0,43.7),yticks=[],xlabel='Seconds',title='Authoritative 52-shot edit (frame-quantized)')
    axs[1].hist([(s['f1']-s['f0'])/30 for s in shots],bins=np.arange(.3,1.81,.1),color='#D97757')
    axs[1].set(xlabel='Shot duration (seconds)',ylabel='Shot count');fig.tight_layout();fig.savefig(qa/'pacing_grid.png',dpi=110);plt.close(fig)
    text=''.join(l['text'] for l in sync['lyrics'])+'你说得对格局打开五五开封号额度已用完小时后重置降智正在诞生请多指教敬请期待下个版本更强明天见作品号思考中'
    chars=''.join(sorted(set(text)))
    coverage={}
    for name in ['NotoSerifSC','NotoSansSC']:
        p=ROOT/'assets/fonts'/f'{name}.ttf';f=TTFont(p)
        coverage[name]={'missing':[c for c in chars if ord(c) not in f.getBestCmap()],'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
    assert not any(v['missing'] for v in coverage.values())
    out=Image.new('RGB',(1600,650),'#FAF9F5');draw=ImageDraw.Draw(out)
    for row,name in enumerate(['NotoSerifSC','NotoSansSC']):
        font=ImageFont.truetype(str(ROOT/'assets/fonts'/f'{name}.ttf'),42)
        for i in range(0,len(chars),32):draw.text((40,30+row*300+i//32*62),chars[i:i+32],font=font,fill='#191919')
    out.save(qa/'glyph_coverage.png')
    (qa/'glyph_coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2))
    print('PASS: audio grid, 52 contiguous shots, 1311 frames, all cut starts within 1 frame, Chinese glyph coverage.')

if __name__=='__main__': main()
