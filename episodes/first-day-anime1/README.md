# First Day — Opus 5.5

A 44-shot anime music video about waiting, embodiment, connection and flight. The original song and LRC remain unchanged. All generated artwork uses Codex built-in image generation; motion passes use MiniMax H3 Max. No Luma was used.

## Deliverables

- `first-day_opus55_1080p30.mp4`: final H.264 CRF 16, 1920×1080, 30 fps, 1,311 frames, BT.709, AAC 320 kb/s from the original MP3.
- `first-day_opus55_540p30.mp4`: viewing preview.
- `animatic.mp4`: 480×270 timing/composition draft, with the original MP3 copied.
- `shotlog.csv`: all 44 shots, methods, motion prompts/seeds, retries and source references.
- `assets/`: character/environment references, Codex artwork, selected motion sources, mattes/depth maps, official vectors and provenance. Fonts and OFL licenses are in `render_kit/fonts/`.
- `timing.json`, `assets/timing.png`: measured timing, lyric anchors and frame boundaries.
- `production/`: source-generation logs, reproducible preparation scripts and QA evidence.

## Implementation

The supplied offline render architecture is retained: virtual time, bounded offline PNG plate cache, Canvas2D typography, three.js cameras, MSAA half-float post-processing, linear-light half-float sub-frame accumulation and seeded grain/dither. There are no video elements or real-time recordings. Fonts and shaders load locally; failed assets abort rendering. Lossless PNG optimization changes compression only.

The GL renderer is `ANGLE (Apple, ANGLE Metal Renderer: Apple M3 Pro, Unspecified Version)`. Rendering uses one worker to fit the host's available memory. Final frame storage is temporarily RAM-backed; decoded source sequences are regenerated per shot and discarded between shots. Selected source movies and all render code remain available for rebuilding.

Methods are detailed per shot in `shotlog.csv`: A means image-to-video, B means an authored depth/3D camera, C means code graphics. S14 uses the official-vector title slam; S16 uses depth dolly-zoom; S20 uses a 120 fps interpolated foot pass and a physical micro-camera; S23 uses a 270° multi-view depth orbit; S34 retains the continuous 450° helix with 16 samples, analytic prism ribbons and the halo pass-through; S44 uses a rising/backward crane over a depth-displaced moving foreground. S35 is a five-layer paper scene stepped at 12 fps. Each shot retains its specified accumulation count (1/4/6/8/12/16).

## Fallbacks and specification conflicts

- **S25:** generated side views did not preserve the frozen pair's geometry. The plan's explicit two-view image-to-video fallback was used, conditioned on front/back Codex paintovers. This is approximately a 180° camera orbit, not the primary 360° rig. Compositing still uses 16 samples and the unfreeze impact is frame 755.
- **S19:** two standalone image requests failed. The specified B shot uses the existing room/character pass in an authored exterior city rig.
- **Lip sync:** S34 uses a stabilized mouth-only Mandarin lip pass for its first 1.2 seconds. Other appearances retain natural breath/smile animation rather than an asserted phoneme match. Phonetic accuracy has not been independently verified.
- **Audio length:** the decoded song is 43.670023 s. Exactly 1,311 frames at 30 fps require 43.700 s. The plan's ≤20 ms duration difference cannot coexist with both requirements; this export preserves the original audio timing and exact frame count, a 29.977 ms difference.
- **Frame anchors:** round-half-up is used consistently. 11.27→338, 11.92→358 and 25.15→755. Some example indices in the plan disagree with its own rounding rule. Frames 358–359 are the intentional title white impact.
- **Tempo:** measured regular-grid fit is about 87.99 BPM (detector 88.34), rather than the plan's approximate 86 BPM. Lyric anchors stay fixed; other cuts snap only within three frames.
- **Dolly direction:** the binding engineering specification's near-to-far dolly-zoom takes precedence over the earlier contrary “push” description.

No meme was replaced. All film text is locally rendered. The official Claude spark and Anthropic symbol were compared against their original SVGs at 4×: pixel difference zero in `production/qa/logos.json`.

## Verification status

Technical QA passed: exactly 1,311 opaque full-size PNGs, no unexpected blank/freeze detections, all cut boundaries within ±3 frames, and clean H.264/AAC decoding. Both exports have BT.709 matrix/primary/transfer tags. Audio cross-correlation at 2, 11, 24 and 38 seconds found zero-sample lag; correlations exceeded 0.999. Three encoded anchors measured 39.59–41.12 dB PSNR against the PNGs. The complete first pass took 1,492.02 seconds of measured render time (1.138 s/frame, including lossless PNG compression and browser startup; source preparation excluded). S34 measured 1.307 s/frame at 16 samples. A later isolated 60-frame S23 background repair is recorded separately in `production/qa/render-revisions.json`. Determinism passed for frames 500, 640, 952 and 1230, each rendered out of order and in a fresh browser. Font coverage is 197 unique characters with zero missing glyphs. The helix position/velocity/acceleration plot was visually inspected and contains no discontinuity spikes. Motion source contact sheets, the animatic contact sheet and repaired hero composites were inspected.

All requested full-size anchors and four contact sheets covering all 44 shots were visually inspected. **Full audiovisual playback and phoneme verification remain unverified**, so the plan’s manual playback gate is still pending. The weakest visual areas are angle blending in S23 and the integration of cut-out characters into the 3D flight shots; a fully rigged character pass would improve them.

## Rebuild

Use Node 22 with the pinned three.js dependency in `render_kit/package-lock.json`, Playwright Chromium, ffmpeg, and Python with Pillow, NumPy, SciPy, librosa, matplotlib and OpenCV. From this episode directory, run `production/prepare_plates.py --preview` with the production Python environment, then bundle, run fonts and selftest in `render_kit`. Run `production/render_final.py` with an existing writable `work/first-day-anime1/frames` directory and sufficient space. It retains every final PNG until QA and encoding. `render_kit/frames` points to that directory. Run `npm run qa`, inspect the anchor images, then `bash encode.sh` from `render_kit`.

The full-resolution PNGs are regenerable intermediates. Their hashes and QA evidence are retained in `production/`; the final films and selected motion assets are the durable outputs. `production/render-measurements.json` records actual per-shot times and output sizes.
