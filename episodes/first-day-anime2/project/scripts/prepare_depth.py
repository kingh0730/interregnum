#!/usr/bin/env python3
"""Local, sequential ONNX technical depth/matte inference. Never edits source plates.

Examples:
  .venv/bin/python episodes/first-day-anime2/project/scripts/prepare_depth.py --ids S11
  .../prepare_depth.py --mode both --ids S25 S37
  .../prepare_depth.py --mode mask path/to/plate.png
"""
from __future__ import annotations
import argparse
import gc
import hashlib
import json
import time
from pathlib import Path
import numpy as np
import onnxruntime as ort
from PIL import Image, ImageDraw

PROJECT = Path(__file__).resolve().parents[1]
REPO = PROJECT.parents[2]
MODEL_DIR = REPO / 'work/opus55-models'
ANIME_MD5 = '6f184e756bb3bd901c8849220a83e38e'

def digest(path, algorithm='sha256'):
    h = hashlib.new(algorithm)
    with Path(path).open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def relative(path):
    try:
        return str(Path(path).resolve().relative_to(REPO))
    except ValueError:
        return str(Path(path).resolve())

def depth_input(image, config):
    """DPT aspect-preserving closest-scale resize, then nearest multiple of 14."""
    width, height = image.size
    sh, sw = config['size']['height'] / height, config['size']['width'] / width
    if config.get('keep_aspect_ratio'):
        sh = sw = sw if abs(1 - sw) < abs(1 - sh) else sh
    multiple = config.get('ensure_multiple_of', 1)
    out_w = max(multiple, int(round(width * sw / multiple) * multiple))
    out_h = max(multiple, int(round(height * sh / multiple) * multiple))
    rgb = image.convert('RGB').resize((out_w, out_h), Image.Resampling.BICUBIC)
    array = np.asarray(rgb, dtype=np.float32) * config['rescale_factor']
    array = (array - np.asarray(config['image_mean'], np.float32)) / np.asarray(config['image_std'], np.float32)
    return np.ascontiguousarray(array.transpose(2, 0, 1)[None]), (out_w, out_h)

def mask_input(image):
    # Mirrors installed rembg BaseSession.normalize / DisSession exactly.
    array = np.asarray(image.convert('RGB').resize((1024, 1024), Image.Resampling.LANCZOS), dtype=np.float32)
    array = array / max(float(array.max()), 1e-6)
    array -= np.array([.485, .456, .406], dtype=np.float32)
    return np.ascontiguousarray(array.transpose(2, 0, 1)[None]), (1024, 1024)

def session(path):
    settings = ort.SessionOptions()
    settings.intra_op_num_threads = 4
    settings.inter_op_num_threads = 1
    settings.execution_mode = ort.ExecutionMode.ORT_SEQUENTIAL
    return ort.InferenceSession(str(path), sess_options=settings, providers=['CPUExecutionProvider'])

def qa_image(source, output, path, label, rgba=None):
    # Pure technical visualization; source content is never generated or retouched.
    w = 640
    h = max(1, round(source.height / source.width * w))
    cards = [source.convert('RGB').resize((w, h)), output.convert('RGB').resize((w, h))]
    labels = ['Original plate (unchanged)', label]
    if rgba is not None:
        checker = Image.new('RGB', source.size, '#cccccc')
        draw = ImageDraw.Draw(checker)
        for y in range(0, source.height, 32):
            for x in range(0, source.width, 32):
                if (x // 32 + y // 32) % 2:
                    draw.rectangle((x, y, x + 31, y + 31), fill='#f0eee6')
        checker.paste(rgba, (0, 0), rgba.getchannel('A'))
        cards.append(checker.resize((w, h)))
        labels.append('Predicted alpha over checkerboard')
    sheet = Image.new('RGB', (w * len(cards), h + 32), '#191919')
    for i, card in enumerate(cards):
        sheet.paste(card, (i * w, 32))
    draw = ImageDraw.Draw(sheet)
    for i, text in enumerate(labels):
        draw.text((i * w + 8, 8), text, fill='white')
    sheet.save(path)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('paths', nargs='*', type=Path)
    parser.add_argument('--ids', nargs='+', default=[])
    parser.add_argument('--mode', choices=['depth', 'mask', 'both'], default='depth')
    args = parser.parse_args()
    sources = list(args.paths)
    for shot_id in args.ids:
        matches = sorted((PROJECT / 'assets/plates').glob(f'{shot_id}*.png'))
        # S1 must not unintentionally include S10 etc.
        matches = [p for p in matches if p.stem == shot_id or p.stem.startswith(shot_id + '-') or p.stem.startswith(shot_id + '_')]
        if not matches:
            parser.error(f'No plate matches {shot_id}')
        sources.extend(matches)
    sources = list(dict.fromkeys(p.resolve() for p in sources))
    if not sources:
        parser.error('Supply explicit paths or --ids; bulk inference is never implicit')
    if len({p.stem for p in sources}) != len(sources):
        parser.error('Source stems must be unique to avoid output collisions')
    for source in sources:
        if not source.is_file():
            parser.error(f'Missing input: {source}')
    for directory in ['assets/depth', 'assets/masks', 'assets/cutouts', 'qa/depth']:
        (PROJECT / directory).mkdir(parents=True, exist_ok=True)
    status_path = PROJECT / 'helper/depth-status.json'
    status = json.loads(status_path.read_text()) if status_path.exists() else {'schemaVersion': 1, 'models': {}, 'results': {}}
    status.update(status='technical-inference-not-final-visual-qa',sourcePlatesModified=False,networkUsedByScript=False,threads={'intraOp':4,'interOp':1,'execution':'sequential','concurrentSessions':1})
    modes = ['depth', 'mask'] if args.mode == 'both' else [args.mode]
    for mode in modes:
        model = MODEL_DIR / ('depth-anything-v2-small.onnx' if mode == 'depth' else 'isnet-anime.onnx')
        if mode == 'mask' and digest(model, 'md5') != ANIME_MD5:
            raise RuntimeError('Anime ONNX checksum mismatch: incomplete download or unexpected model; refusing inference')
        engine = session(model)
        config = json.loads((MODEL_DIR / 'preprocessor_config.json').read_text()) if mode == 'depth' else None
        metadata = {
            'file':relative(model),'sha256':digest(model),'providers':engine.get_providers(),'onnxruntimeVersion':ort.__version__,
            'inputs':[{'name':a.name,'shape':a.shape,'type':a.type} for a in engine.get_inputs()],
            'outputs':[{'name':a.name,'shape':a.shape,'type':a.type} for a in engine.get_outputs()],
            'source': 'https://huggingface.co/onnx-community/depth-anything-v2-small' if mode == 'depth' else 'https://github.com/danielgatis/rembg/releases/download/v0.0.0/isnet-anime.onnx',
            'preprocessing':config if mode == 'depth' else {'resize':[1024,1024],'resample':'Lanczos','rescale':'divide resized RGB by its maximum pixel value, lower-bounded 1e-6','mean':[.485,.456,.406],'std':[1,1,1],'layout':'NCHW float32'},
            'postprocessing':'per-image min/max normalization to grayscale L; larger inverse-depth prediction is whiter/nearer; bicubic resize to original dimensions' if mode == 'depth' else 'first ONNX output channel0, min/max normalization, uint8 L, Lanczos resize to original dimensions; unchanged source RGB plus predicted alpha',
        }
        if mode == 'depth':
            metadata['preprocessorSha256']=digest(MODEL_DIR / 'preprocessor_config.json')
            metadata['resizeImplementation']='DPT keep-aspect chooses scale closest to 1, dimensions rounded to nearest positive multiple14. No padding.'
        else:
            metadata['verifiedOfficialMd5']=ANIME_MD5
        status['models'][mode] = metadata
        print(json.dumps({'mode':mode,'inputs':metadata['inputs'],'outputs':metadata['outputs']}), flush=True)
        for source in sources:
            source_hash = digest(source)
            image = Image.open(source).convert('RGBA')
            tensor, input_size = depth_input(image, config) if mode == 'depth' else mask_input(image)
            started = time.monotonic()
            outputs = engine.run(None,{engine.get_inputs()[0].name:tensor})
            prediction = np.asarray(outputs[0][0] if mode == 'depth' else outputs[0][0,0], dtype=np.float32).squeeze()
            if prediction.ndim != 2 or not np.isfinite(prediction).all():
                raise RuntimeError(f'Invalid {mode} prediction for {source}')
            lo, hi = float(prediction.min()), float(prediction.max())
            if hi - lo <= 1e-10:
                raise RuntimeError(f'Constant {mode} prediction for {source}; refusing plausible-looking output')
            normalized = (prediction-lo)/(hi-lo)
            if mode == 'depth':
                resized = Image.fromarray(normalized, mode='F').resize(image.size, Image.Resampling.BICUBIC)
                out = Image.fromarray(np.round(np.clip(np.asarray(resized),0,1)*255).astype(np.uint8))
            else:
                out = Image.fromarray((normalized*255).astype(np.uint8)).resize(image.size,Image.Resampling.LANCZOS)
            target = PROJECT / ('assets/depth' if mode == 'depth' else 'assets/masks') / (source.stem+'.png')
            out.save(target)
            preview = PROJECT / 'qa/depth' / (source.stem+'-'+mode+'.jpg')
            result={'source':relative(source),'sourceSha256':source_hash,'output':relative(target),'outputSha256':digest(target),'modelSha256':metadata['sha256'],'inputDimensions':list(input_size),'sourceDimensions':list(image.size),'rawPredictionRange':[lo,hi],'elapsedSeconds':round(time.monotonic()-started,3),'visualReview':'pending','qaPreview':relative(preview)}
            if mode == 'mask':
                rgba=image.copy()
                original_alpha=np.asarray(image.getchannel('A'),dtype=np.uint16)
                rgba.putalpha(Image.fromarray((np.asarray(out,dtype=np.uint16)*original_alpha//255).astype(np.uint8)))
                cutout=PROJECT/'assets/cutouts'/(source.stem+'.png');rgba.save(cutout)
                native_preview=PROJECT/'qa/depth'/(source.stem+'-mask-native-dark.jpg')
                dark=Image.new('RGB',image.size,'#191919');dark.paste(rgba,(0,0),rgba.getchannel('A'));dark.save(native_preview,quality=95)
                result.update(cutout=relative(cutout),cutoutSha256=digest(cutout),foregroundPixelFraction=float(np.mean(np.asarray(out)>127)),nativeDarkPreview=relative(native_preview))
                qa_image(image,out,preview,'IS-Net anime predicted matte',rgba)
            else:
                qa_image(image,out,preview,'Depth Anything V2 relative inverse depth')
            if digest(source)!=source_hash:
                raise RuntimeError('Source plate changed during processing')
            status['results'].setdefault(source.stem,{})[mode]=result
            status_path.write_text(json.dumps(status,indent=2)+'\n')
            print(json.dumps({'source':source.stem,'mode':mode,'output':relative(target),'seconds':result['elapsedSeconds']}),flush=True)
            del outputs,tensor,prediction
        del engine
        gc.collect()
    status_path.write_text(json.dumps(status,indent=2)+'\n')

if __name__ == '__main__':
    main()
