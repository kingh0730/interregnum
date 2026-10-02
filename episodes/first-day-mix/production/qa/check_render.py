#!/usr/bin/env python3
"""Technical evidence only. Never asserts visual quality, sync perception or continuity approval."""
import argparse
import hashlib
import itertools
import json
import re
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

def run(*args):
    result = subprocess.run([str(a) for a in args], capture_output=True)
    if result.returncode:
        raise RuntimeError(str(args[0]) + ' exit ' + str(result.returncode) + ': ' + result.stderr.decode(errors='replace'))
    return result

def sha(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda: f.read(1048576), b''):
            h.update(block)
    return h.hexdigest()

def probe(p):
    return json.loads(run('ffprobe', '-v', 'error', '-count_frames', '-show_streams', '-show_format', '-of', 'json', p).stdout)

def audio(p):
    cmd = ['ffmpeg', '-hide_banner', '-nostats', '-i', p, '-map', '0:a:0', '-af', 'loudnorm=I=-16:TP=-1:LRA=11:print_format=json', '-f', 'null', '-']
    r = run(*cmd)
    matches = re.findall(r'\{\s*"input_i".*?\}', r.stderr.decode(), flags=re.S)
    raw = run('ffmpeg', '-v', 'error', '-i', p, '-map', '0:a:0', '-ac', '2', '-ar', '48000', '-f', 's32le', '-').stdout
    return {'file_sha256': sha(p), 'decoded_stereo_48k_s32le_sha256': hashlib.sha256(raw).hexdigest(),
            'decoded_samples_per_channel': len(raw)//8,
            'loudness_input_metrics': json.loads(matches[-1]) if matches else None}, raw

def collisions(config):
    rows = config.get('overlays', [])
    issues = []
    width, height = config['width'], config['height']
    for row in rows:
        x,y,w,h = row['box']
        assert w > 0 and h > 0 and row['end_frame'] > row['start_frame'], 'Invalid overlay bounds'
        if x < 0 or y < 0 or x+w > width or y+h > height:
            issues.append({'type':'out_of_frame', 'id':row['id']})
    for a,b in itertools.combinations(rows, 2):
        if max(a['start_frame'], b['start_frame']) >= min(a['end_frame'], b['end_frame']):
            continue
        x,y,w,h = a['box']; X,Y,W,H = b['box']
        if max(x,X) < min(x+w,X+W) and max(y,Y) < min(y+h,Y+H):
            issues.append({'type':'overlap', 'ids':[a['id'], b['id']], 'intentional': b['id'] in a.get('allow_overlap_with', []) or a['id'] in b.get('allow_overlap_with', [])})
    return {'provided_boxes_only':True, 'issues':issues, 'checked_overlay_count':len(rows), 'limitation':'No OCR or automatic glyph bounds. Config must use actual renderer text boxes including stroke/padding; intentional overlaps remain listed.'}

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('config'); ap.add_argument('--out', required=True)
    args = ap.parse_args()
    c = json.loads(Path(args.config).read_text())
    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    p = (ROOT / c['video']).resolve()
    info = probe(p); v = next(s for s in info['streams'] if s['codec_type']=='video')
    n = int(v['nb_read_frames']); fps = Fraction(c['fps'])
    errors = []
    if (v['width'], v['height']) != (c['width'], c['height']): errors.append('Dimensions differ from config')
    if Fraction(v['avg_frame_rate']) != fps: errors.append('Average frame rate differs from config')
    if 'expected_frames' in c and n != c['expected_frames']: errors.append('Decoded frame count differs from expected_frames')
    if 'expected_duration_s' in c and abs(float(info['format']['duration'])-c['expected_duration_s']) > c.get('duration_tolerance_s', float(1/fps)):
        errors.append('Container duration differs from expected duration beyond tolerance')
    if c.get('source_audio') and not any(s['codec_type']=='audio' for s in info['streams']):
        errors.append('Final video has no audio stream although source_audio is configured')
    frames = set(); shot_rows = []
    for s in c['shots']:
        a,b = s['start_frame'],s['end_frame']
        assert type(a) is int and type(b) is int and 0 <= a < b <= n, f'Invalid shot bounds {s}'
        sample = sorted(set([a, (a+b-1)//2, b-1] + ([a-1] if a else []) + ([b] if b<n else [])))
        frames.update(sample); shot_rows.append({'id':s['id'],'frames':sample})
    # Full linear decode also identifies corruption outside the sampled frames.
    decode = subprocess.run(['ffmpeg','-v','error','-xerror','-i',str(p),'-map','0:v:0','-map','0:a?','-f','null','-'],capture_output=True)
    if decode.returncode: errors.append('Full decode failed')
    samples = sorted(frames)
    image_dir = out/'frames'; image_dir.mkdir(exist_ok=True)
    assert not list(image_dir.iterdir()), 'Use a new QA output directory; existing frame files could pollute sheets'
    def balanced_sum(items):
        if len(items) == 1: return items[0]
        mid = len(items)//2
        return '(' + balanced_sum(items[:mid]) + '+' + balanced_sum(items[mid:]) + ')'
    select = balanced_sum([f'eq(n{chr(92)},{f})' for f in samples]) if samples else '0'
    if samples:
        run('ffmpeg','-v','error','-i',p,'-vf',f'select={select},scale=480:-2','-fps_mode','vfr', image_dir/'%05d.png')
        # Exact frame mapping lives beside images; labels baked into each sheet with drawtext are optional.
        generated = sorted(image_dir.glob('*.png'))
        assert len(generated)==len(samples), 'Frame extraction count differs'
        mappings = [{'image':str(im),'frame':fr,'time_s':float(fr/fps)} for im,fr in zip(generated,samples)]
        for page,offset in enumerate(range(0,len(samples),20)):
            count = min(20,len(samples)-offset)
            run('ffmpeg','-v','error','-start_number',offset+1,'-i',image_dir/'%05d.png','-vf',f'tile=4x5:nb_frames={count}:padding=3:margin=3:color=white','-frames:v','1',out/f'contact-{page+1:02d}.png')
    else: mappings=[]
    r = {'kind':'technical_evidence','perceptual_review':'NOT PERFORMED BY THIS SCRIPT','config_sha256':sha(Path(args.config)),
         'video_sha256':sha(p),'probe':info,'errors':errors,'decode':{'returncode':decode.returncode,'stderr':decode.stderr.decode()},
         'samples':mappings,'shot_samples':shot_rows,'collision_check':collisions(c)}
    if any(s['codec_type']=='audio' for s in info['streams']):
        r['final_audio'], final_raw = audio(p)
        if c.get('source_audio'):
            src=(ROOT/c['source_audio']).resolve()
            r['source_audio'], source_raw = audio(src)
            expected=c.get('source_audio_sha256')
            r['source_file_unchanged'] = sha(src)==expected if expected else None
            if expected and not r['source_file_unchanged']: errors.append('Original audio source differs from pre-production hash')
            r['decoded_audio_exact_match']=source_raw==final_raw
            r['audio_integrity_note']='PCM comparison after identical stereo/48k conversion. Lossy encode or authorized mix changes make exact_match false; false is not evidence the source was replaced. No listening or perceptual sync judgment.'
    assets=[]
    for value in c.get('assets', []):
        f=(ROOT/value).resolve()
        assets.append({'path':str(f),'sha256':sha(f),'probe':probe(f)})
    r['source_assets']=assets
    logs=[]
    for row in c.get('generation_logs', []):
        f=(ROOT/row['path']).resolve()
        logs.append({'path':str(f),'sha256':sha(f),'bytes':f.stat().st_size,'expected_cost_usd':row.get('expected_cost_usd'),'actual_cost_usd':row.get('actual_cost_usd'),'cost_evidence':row.get('cost_evidence'),'note':'Amounts explicitly supplied, not inferred from response size or success.'})
    r['generation_logs']=logs
    for issue in r['collision_check']['issues']:
        if not issue.get('intentional', False): errors.append('Overlay geometry: '+json.dumps(issue))
    r['expected_cost_usd_known_subtotal']=sum(x['expected_cost_usd'] for x in logs if x['expected_cost_usd'] is not None)
    r['expected_cost_usd_total']=r['expected_cost_usd_known_subtotal'] if logs and all(x['expected_cost_usd'] is not None for x in logs) else None
    r['actual_cost_usd_total']=sum(x['actual_cost_usd'] for x in logs if x['actual_cost_usd'] is not None) if logs and all(x['actual_cost_usd'] is not None for x in logs) else None
    (out/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print(out/'report.json')
    return 2 if errors or decode.returncode else 0

if __name__=='__main__': raise SystemExit(main())
