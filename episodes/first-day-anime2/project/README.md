# OPUS 5.5 · 第一天

Production source for the 43.70-second, 1311-frame anime music video. The creative brief is `../files/OPUS55_MV_PLAN.md`. See `qa/qa_report.md` for the actual delivery status and limitations; source code alone is not an approval.

All generated artwork was made with the built-in Codex image generator. No Luma was used. Video-service requests failed before acceptance, so this version uses illustrated poses, Depth Anything depth meshes, separately layered scenes, camera rigs, procedural effects, and code typography. It does not contain generated character-animation clips.

## Files

- `helper/shots.json`, `sync.json`, `onsets.json`: authoritative timing.
- `helper/asset_map.json`, `features.json`: selected artwork and registered feature anchors.
- `helper/image_manifest.json`: generation prompts, sources, and selections.
- `helper/execution_decisions.json`: conflicts and substitutions resolved during production.
- `src/film_runtime.mjs`: deterministic Three.js scene composition.
- `src/Film.tsx`: Remotion adapter; the Remotion runtime was not installed or validated in this environment.
- `build/render.mjs`: the production renderer using locally installed Three.js and Playwright, piping lossless PNG frames to FFmpeg.
- `assets/mosaic/*.json`: actual-film frame provenance for the ending.
- `out/opus55_first_day_1080p30.mp4`: assembled delivery when present.
- `qa/review.html`: local player with frame stepping and all 52 shot entry points.

## Rebuild

Requirements: Node 22, Three.js 0.170.0, Playwright 1.63.0 with its Chromium browser, FFmpeg/FFprobe, Python with Pillow, NumPy, SciPy, OpenCV, Matplotlib, fontTools, and onnxruntime. Fonts and selected raster/depth/mask assets are local. Production used repository `.venv/bin/python`. Run Node commands from this project directory.

1. Run `scripts/preflight.py` and the supplied `../files/verify_sync.py` against `../first-day.mp3`.
2. Render the first 1177 frames in contiguous chunks. For example: `node build/render.mjs --mode=film --from=0 --frames=339 --width=1920 --out=/absolute/work/part0.mp4`. Production chunks start at 0, 339, 686, and 1014, with lengths 339, 347, 328, and 163.
3. Build `assets/mosaic/reflection-atlas.png` using `scripts/make_mosaic.py part0.mp4 part1.mp4 part2.mp4 part3.mp4 --out assets/mosaic/reflection-atlas.png --last-frame 1176`.
4. Render S37: `node build/render.mjs --mode=film --from=1177 --frames=41 --width=1920 --out=/absolute/work/part4.mp4`.
5. Copy the renderer's lossless `part4-f1217.png` to `assets/mosaic/hero.png`. Build `assets/mosaic/atlas.png` from parts 0–4 with `--last-frame 1217`.
6. Render S38/S39: `node build/render.mjs --mode=film --from=1218 --frames=93 --width=1920 --out=/absolute/work/part5.mp4`.
7. Run `scripts/assemble.py` with parts 0–5 in order. It validates contiguous frame hashes, concatenates H.264 without another generation loss, and muxes the original MP3 packets without re-encoding. This prioritizes the brief's untouched-MP3 requirement over its incompatible AAC wording.
8. Run `scripts/qa_final.py out/opus55_first_day_1080p30.mp4`. Review its actual-frame contact sheets, camera strips, cue images, and diagnostics. Numeric success is not a substitute for viewing the film.
9. Run `node build/render.mjs --mode=playback --video=out/opus55_first_day_1080p30.mp4` for real-time Chromium decoder counters. This does not establish perceptual audio quality or native VLC playback.

An existing complete mosaic permits a one-pass `npm run render`, but any changed prefix or S37 must first rebuild the dependent atlases and hero image in the order above. Do not use a stale mosaic after changing the film.

## Storage and reproducibility

Source artwork and media are intentionally not committed. Generation sources, selection records, depth-model URLs and SHA256 hashes remain in the helper manifests. Downloaded inference-model caches were removed after inference to reserve disk space for the export; finished depth maps and masks remain. Reproducible feature-overlay previews were compacted to JPEG. Keep source artwork, local fonts, and selected technical assets with this project when archiving.

Each render writes a video-bound `.source-frame-hashes.json`, retaining SHA256 for the exact PNG frames supplied to its encoder. Assembly carries those proofs into the final movie sidecar. Lossy H.264 decoding can introduce tiny changes across an otherwise identical source hold; the QA report distinguishes these from animation.
