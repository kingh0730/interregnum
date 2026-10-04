"""Build actual-film atlases from encoded, frame-indexed first-pass segments."""
from pathlib import Path
import argparse, hashlib, json
import cv2
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('segments',nargs='+',type=Path);ap.add_argument('--out',required=True,type=Path);ap.add_argument('--last-frame',required=True,type=int);args=ap.parse_args()
    wanted={round(k*7.5) for k in range(int(args.last_frame/7.5)+1)};wanted.add(args.last_frame)
    frames={};sources=[];expected=0
    for p in args.segments:
        side=p.with_suffix('.source-frame-hashes.json')
        meta=json.loads(side.read_text());assert meta['video_sha256']==digest(p),f'Changed segment: {p}'
        indices=[v['frame'] for v in meta['frames']]
        assert indices==list(range(expected,expected+len(indices))),f'Noncontiguous source frames: {p}'
        cap=cv2.VideoCapture(str(p));local=0
        while True:
            ok,bgr=cap.read()
            if not ok:break
            f=expected+local
            if f in wanted:frames[f]=Image.fromarray(cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB)).resize((64,36),Image.Resampling.LANCZOS)
            local+=1
        cap.release();assert local==len(indices),f'Decoder frame-count mismatch: {p}'
        sources.append({'path':str(p.resolve()),'sha256':meta['video_sha256'],'from':expected,'frames':local})
        expected+=local
    assert expected==args.last_frame+1
    assert wanted==set(frames),f'Missing sampled frames: {sorted(wanted-set(frames))}'
    ordered=sorted(frames);atlas=Image.new('RGB',(1920,720));tiles=[]
    for i in range(600):
        f=ordered[i%len(ordered)];tile=frames[f].resize((64,36),Image.Resampling.LANCZOS)
        atlas.paste(tile,(i%30*64,i//30*36));tiles.append({'tile':i,'frame':f})
    args.out.parent.mkdir(parents=True,exist_ok=True);atlas.save(args.out)
    manifest={'atlas':str(args.out.resolve()),'sha256':digest(args.out),'source_scope':[0,args.last_frame],'unique_frames':len(ordered),'sample_frames':ordered,'sampling':'Every0.25s rounded to30fps plus exact last frame; samples repeat across600 tiles.','grid':[30,20],'tile_size':[64,36],'sources':sources,'tiles':tiles}
    args.out.with_suffix('.json').write_text(json.dumps(manifest,indent=2))
    print(json.dumps({'atlas':str(args.out),'unique_frames':len(ordered),'tiles':600}))
if __name__=='__main__':main()
