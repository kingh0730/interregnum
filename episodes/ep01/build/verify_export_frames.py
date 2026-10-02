# /// script
# requires-python = ">=3.11"
# dependencies = ["Pillow>=10"]
# ///
"""Check one decoded export frame for every unique approved state/caption plate."""
from pathlib import Path
from PIL import ImageChops, ImageStat
import render_reel as r


def main():
    spec = r.read_json(r.BUILD / 'render.json')
    audit = r.read_json(r.BUILD / 'export_audit.json')
    export = r.resolve(spec['output'])
    export_hash = r.digest_file(export)
    if audit['status'] != 'passed' or audit['export_sha256'] != export_hash:
        raise ValueError('A matching passed full-decode export audit is required')
    selected = {}
    for part in spec['segments']:
        selected.setdefault(part['plate'], part)
    parts = list(selected.values())
    frames = [p['start_frame'] + p['frames']//2 for p in parts]
    directory = r.WORK / 'encoded_review' / export_hash[:16]
    directory.mkdir(parents=True, exist_ok=True)
    selection = 'select=' + '+'.join(f'eq(n\\,{frame})' for frame in frames)
    r.run(['ffmpeg','-y','-v','error','-xerror','-i',export,'-vf',selection,
           '-fps_mode','vfr','-start_number',0,directory/'frame_%03d.png'])
    rows, review_parts = [], []
    for index, (part, frame) in enumerate(zip(parts,frames)):
        actual_path = directory / f'frame_{index:03d}.png'
        with r.Image.open(actual_path) as actual, r.Image.open(r.resolve(part['plate'])) as expected:
            if actual.size != (r.W,r.H):
                raise ValueError(f'Unexpected decoded size at frame{frame}')
            difference = ImageChops.difference(actual.convert('RGB'),expected.convert('RGB'))
            error = sum(ImageStat.Stat(difference).mean)/3
        # This allows codec quantization, while detecting a wrong shot, framing or conversion.
        # Visually reviewed native frames and paper-pair checks cover small localized state changes.
        if error > 5:
            raise ValueError(f'Export frame{frame} does not match approved plate: mean error{error:.3f}')
        rows.append({'frame':frame,'shot_id':part['shot_id'],'asset':part['asset'],
                     'subtitle':part['subtitle'],'expected_plate':part['plate'],
                     'decoded_frame':r.relative(actual_path),'mean_absolute_rgb_error':round(error,5)})
        review_parts.append({**part,'plate':r.relative(actual_path)})
    if len(list(directory.glob('frame_*.png'))) != len(rows):
        raise ValueError('Decoded review frame count differs from unique plate count')
    old_work = r.WORK
    r.WORK = directory
    r.prepare_review(review_parts,spec['input_hashes'])
    r.WORK = old_work
    report = {'status':'passed','export_sha256':export_hash,'sampled_unique_plates':len(rows),
              'matching_full_decode_audit':'episodes/ep01/build/export_audit.json',
              'method':'One actual decoded midpoint frame per unique approved composite; native size and RGB-error comparison. Contact sheets for visual review.',
              'maximum_mean_absolute_rgb_error':max(row['mean_absolute_rgb_error'] for row in rows),
              'review_manifest':r.relative(directory/'review/review_manifest.json'),'frames':rows}
    r.write_json(r.BUILD/'export_frame_audit.json',report)
    print(f"Decoded plate verification passed: {len(rows)} unique frames; maximum RGB error {report['maximum_mean_absolute_rgb_error']:.4f}")
    print(r.relative(directory/'review'))


if __name__ == '__main__':
    main()
