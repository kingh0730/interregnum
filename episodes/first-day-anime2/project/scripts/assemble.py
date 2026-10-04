"""Losslessly assemble verified frame-contiguous renders with the original MP3."""
from pathlib import Path
import argparse, hashlib, json, subprocess, tempfile

ROOT=Path(__file__).resolve().parents[1]
def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('segments',nargs='+',type=Path);ap.add_argument('--out',type=Path,default=ROOT/'out/opus55_first_day_1080p30.mp4');args=ap.parse_args()
    frames=[];sources=[]
    for p in args.segments:
        p=p.resolve();meta=json.loads(p.with_suffix('.source-frame-hashes.json').read_text())
        assert digest(p)==meta['video_sha256'],f'Changed source: {p}'
        assert [x['frame'] for x in meta['frames']]==list(range(len(frames),len(frames)+len(meta['frames']))),f'Noncontiguous source: {p}'
        frames.extend(meta['frames']);sources.append({'path':str(p),'sha256':meta['video_sha256']})
    assert len(frames)==1311
    args.out.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.NamedTemporaryFile(mode='w',suffix='.ffconcat',dir=args.out.parent) as listing:
        listing.write('ffconcat version 1.0\n')
        for p in args.segments:
            assert "'" not in str(p.resolve()),'Unsupported quote in path'
            listing.write("file '"+str(p.resolve())+"'\n")
        listing.flush()
        subprocess.run(['ffmpeg','-y','-v','warning','-f','concat','-safe','0','-i',listing.name,'-i',str(ROOT.parent/'first-day.mp3'),'-map','0:v:0','-map','1:a:0','-c','copy','-t','43.7','-video_track_timescale','30000','-movflags','+faststart',str(args.out)],check=True)
    manifest={'definition':'SHA256 of lossless PNG frames supplied to the segment encoders; segment video streams concatenated without re-encoding.','video_sha256':digest(args.out),'segments':sources,'frames':frames}
    args.out.with_suffix('.source-frame-hashes.json').write_text(json.dumps(manifest,indent=2))
    print(json.dumps({'output':str(args.out),'frames':len(frames),'sha256':manifest['video_sha256']}))

if __name__=='__main__':main()
