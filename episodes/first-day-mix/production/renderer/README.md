# First Day offline renderer

Original dependency-free Canvas renderer; 1920×1080. No public site/deployment. `index.html?config=<URL>` exposes `window.ready` and asynchronous `window.renderFrame(t)`.

Run from repository root with the existing Node binary:

```sh
/Users/kingh0730/.nvm/versions/node/v22.23.1/bin/node episodes/first-day-mix/production/renderer/export.mjs --config episodes/first-day-mix/production/film-config.json --out work/first-day-mix/production/film-silent.mp4
```

Full default render exports **2621 frames at 60 fps**: timestamps 0 through 43.6666667 s, duration 43.6833333 s. Root assembly owns the supplied 43.67 s audio and exact final presentation policy. Video is H.264 CRF17 yuv420p with explicit BT.709 metadata. PNG frames stream through FFmpeg with backpressure; no image sequence is retained.

`--from 12 --to 18` exports a frame-aligned chunk. `--stills 0.2,5.5,20.1 --out work/first-day-mix/production/review` saves only requested PNGs. Also supports `--fps`, `--preset`, `--crf`, `--root`.

The local HTTP server supports byte ranges for seeking video. Assets resolve relative to the config JSON URL. Each active video is paused and sought to `sourceStart + (t-start) * sourceRate`; drawing waits for `seeked` and checks decoded readiness. Optional `loop` wraps source time; otherwise source time clamps just before the end. An unavailable required asset rejects `window.ready`; there is no generated mannequin fallback.

Config fields:

- `videos`, `sprites`, `plates`: ID → relative URL (or `{url}` object).
- `shots`: `{id,start,end,scene,palette,cast,newCast,video,sourceStart,sourceRate,label,params}`.
- Scene names: `opening`, `birth`, `fan`, `attention`, `future`, `cel`, `pixel`, `paper` / `fractures`, `explosion`, `ensemble`, `video`.
- Palettes: `day`, `night`, `jade`, `rose`, `gold`.
- `bgVideo`, `bgSourceStart`, `bgSourceRate` optionally place an awaited, deterministically sought motion plate beneath a procedural scene. `plate` selects a still background. Birth defaults to go_macro/cyber_fan; ensemble defaults to canopy_detail.
- `newCast` directs birth reveals; established cast occupy stable globally indexed background seats. Other scenes feature a subset when a full roster would obscure characters. `ensemble` fits all 23 on a suspended canopy with curved depth tiers, load lines and larger foreground leads.
- A video shot does not automatically add duplicate sprites. Set `overlayCast:true` only when such a composite is intended. `overlay` sets procedural effects opacity (default 0.2).
- `labels`: array of `{text,start,end}` or `{text,in_frame,out_frame}`, optional x/y/size/color. If provided, these are the sole identity/concept labels; per-shot label and automatic model names are suppressed. Timed labels span cuts and duplicate text is removed per frame.
- `lyrics`: `{start,end,text}` with bottom safe-area captions. `modelNames` maps cast IDs to display names. `brand` forces the series mark; the final 1.6 s includes `AI SI - I`.

All geometric time calculations and hash-based particles are stateless. Selected character poses quantize at 12 fps while effects remain continuous. Dance shots use the GPT/DeepSeek A/B artwork at six pose changes per second, with measured waist anchors and head-based scale to avoid equal-bounding-box size jumps. Canvas compositing is 2.5D: perspective geometry and ordering are authored, not a physically based 3D scene. Still QA does not prove motion quality.

`smoke-config.json` exercises procedural scenes without assets. It is a renderer test, not a production alternative or final character design.

Measured music response: `audioFeatures` accepts `envelopes_fps`, `rms_envelopes:{mix,low,high}` and `onsets:{mix,low,high}` arrays of `[seconds,strength]`. `envelopeAt` linearly interpolates raw RMS; `attackAt` returns the strongest recent exponentially decayed attack, normalized by each band's 95th-percentile detected strength. Low/high are full-mix frequency bands, not instrument-separated stems. Procedural glow and particle brightness receive restrained modulation; video plates, camera geometry and flashes are unaffected.

`rhythm:{bpm,phase,subdivisions:2,status:"candidate"}` controls A/B pose holds. At 175.8 BPM, two subdivisions produce 0.17065 s holds; one produces 0.34130 s. This is an editorial grid derived from a tempo candidate, not a claim of listened beat validation. Pose selection reads absolute frame time, independently of 12 fps pose-coordinate quantization.

After each frame, `window.textBoxes` exposes measured screen-space text rectangles including conservative shadow padding, font and alpha. It records glyph placement without changing it. `window.attackAt` and `window.envelopeAt` are also available for inspection.
