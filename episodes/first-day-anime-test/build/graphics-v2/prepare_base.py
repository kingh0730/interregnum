"""Conform clean imagery only. All new graphics and typography are browser-rendered."""
import sys,json,subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from render import ROOT,TIMELINE,PLATES,MOTION,TAKE_RANGES
OUT=ROOT/'work/first-day-anime-test/graphics-v2'
ASSET=ROOT/'work/first-day-anime-test/assets'
def run(s):
    n=int(s['id'][1:]);frames=s['end_frame']-s['start_frame'];duration=frames/30
    target=OUT/f'{s["id"]}.mp4'
    if target.exists():return target
    name=MOTION.get(n)
    if name:
        source=ROOT/f'work/first-day-anime-test/motion/{name}.mp4';a,b=TAKE_RANGES.get(n,(0,1))
        if n==35:a,b=0,3.4
        inp=['-i',str(source)];vf=f'trim=start={a}:end={b},setpts=(PTS-STARTPTS)*{duration/(b-a)},fps=30'
    else:
        source=ASSET/f'{PLATES.get(n,"s03-room")}.png'
        if n in (1,2):source=ASSET/'s01-glasses.png'
        if n in (6,12,14,39):source=ASSET/'sky.png'
        if n in (41,43):source=ASSET/('hug.png' if n==41 else 'outro.png')
        if n==13:
            inp=['-ss','5','-i',str(ROOT/'work/first-day-anime-test/motion/levitate.mp4')]
            vf='trim=duration=0.041667,setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration=1,fps=30'
        else:inp=['-loop','1','-framerate','30','-i',str(source)];vf='null'
    vf+=',scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1'
    subprocess.run(['ffmpeg','-y','-v','error',*inp,'-vf',vf,'-frames:v',str(frames),'-an','-c:v','libx264','-preset','fast','-crf','17','-pix_fmt','yuv420p','-g','15',str(target)],check=True)
    return target
if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    with ThreadPoolExecutor(max_workers=3) as pool:paths=list(pool.map(run,TIMELINE))
    listing=OUT/'concat.txt';listing.write_text(''.join(f"file '{p}'\n" for p in paths))
    subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',str(listing),'-c','copy','-movflags','+faststart',str(OUT/'clean-base.mp4')],check=True)
    (OUT/'data.json').write_text(json.dumps({'shots':TIMELINE,'lyrics':json.loads((ROOT/'episodes/first-day-anime-test/timing.json').read_text())['lyrics']},ensure_ascii=False))
    print(OUT/'clean-base.mp4')
