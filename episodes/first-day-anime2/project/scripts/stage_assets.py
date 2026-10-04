"""Prepare only stale technical depth/mattes for the selected production sources."""
from pathlib import Path
import argparse, hashlib, json, subprocess, sys
import numpy as np
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--skip-normalize',action='store_true');args=ap.parse_args()
    if not args.skip_normalize:subprocess.run([sys.executable,str(ROOT/'scripts/build_asset_map.py')],check=True)
    mapping=json.loads((ROOT/'helper/asset_map.json').read_text())
    status=json.loads((ROOT/'helper/depth-status.json').read_text())
    depth_sources={};mask_sources={}
    for shot in mapping['shots'].values():
        if not shot.get('plate'):continue
        p=ROOT/shot['plate']
        if not p.is_file():continue
        if shot.get('depth'):
            technical=ROOT/'assets/depth-inputs'/p.name
            depth_sources[p.stem]=technical if technical.exists() else p
        if shot.get('mask'):
            im=Image.open(p)
            genuine_alpha=im.mode=='RGBA' and float(np.mean(np.asarray(im.getchannel('A'))==0))>.01
            if not genuine_alpha:mask_sources[p.stem]=p
    for mode,sources in [('depth',depth_sources),('mask',mask_sources)]:
        stale=[]
        for stem,p in sources.items():
            record=status.get('results',{}).get(stem,{}).get(mode,{})
            target=ROOT/('assets/depth' if mode=='depth' else 'assets/masks')/(stem+'.png')
            if record.get('sourceSha256')!=sha(p) or not target.exists() or record.get('outputSha256')!=sha(target):stale.append(str(p))
        if stale:
            print(f'{mode}: {len(stale)} new/changed selected sources',flush=True)
            subprocess.run([sys.executable,str(ROOT/'scripts/prepare_depth.py'),'--mode',mode,*stale],check=True)
        else:print(f'{mode}: selected technical outputs current',flush=True)
if __name__=='__main__':main()
