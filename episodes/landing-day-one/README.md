# 《落地第一天》 · AI SI - I

43.670 秒中文音乐短片。人类的一只手放平纸地板；AI 在脚步里获得重量、影子、飞翔和光。落地的圆环成为媒介的边界，最后从一条墨线收束成一个点。

## Delivery

- [Scene-labeled review copy](../../renders/landing-day-one/landing-day-one-labeled-review.mp4) — all 69 scene IDs, scene ranges, live frame number and time, in a separate top bar.
- [1080p60 viewing copy](../../renders/landing-day-one/landing-day-one-1080p60.mp4) — H.264 / AAC.
- [1440p60 master](../../renders/landing-day-one/landing-day-one-1440p60-master.mov) — ProRes 422 / original PCM24 audio.
- [Delivery checks](build/delivery-checks.json) and [review record](build/final-review.md).

This is a fresh production. No previous First Day creative assets or renderer were used. The supplied WAV is copied unchanged into `assets/first-day.wav`; generated clips' audio is excluded.

## Direction and implementation

The unchanged [planner result](production-plan.md) and [original prompt](original-prompt.txt) are authoritative source documents. The direction is also split into `creative-direction.md`, `cast-and-world.md`, `music-and-edit.md`, `shots.md`, `assets-and-techniques.md` and `execution-and-review.md`.

`assets/timeline.json` preserves all 69 shot units, 60 fps and contiguous coverage `[0,2621)`. `assets/production-assets.json` records selected plates, source-video windows, cadence and conform paths. No lyric, audio section or shot interval is removed to fit generation.

The film combines newly generated cel, photoreal, gongbi, toy, felt, cyber and pencil artwork with authored ink, pixel, luminous and negative-space sequences. It includes seventeen usable generated motion sources, separate pose/effect clocks, Chinese lyric performance, radial medium masks, floor contact rings, optical-flow conforming for aerial footage, a 12,000-shard field, frozen-pose camera motion, shadow choreography, a lens/SDF ink point and the final cadence decay. Twelve planned medium registers are represented; the high-frame-rate anime register is distinguished by motion treatment rather than claimed as a different drawing medium.

The six leads appear by name in readable entrance windows. Nine supporting characters have separate artwork. Supplemental AI names appear on the ring stairs. Historical milestones and speculative concepts are kept distinct. Current meme evidence and fallback decisions are in [research](build/research.md).

## Proof decisions and review limits

The initial smoothly deformed sleeves were rejected. Primitive 3D rigs remain as timing proofs, not finished character artwork. The first MiniMax reference-to-video request failed at the provider. Image-to-video subsequently returned the visible hand-raise / palm-to-chest / heel phrase and became the selected motion route.

The DeepSeek skid ends on the planner's freeze alternative to protect shoe framing. The launch uses authored full-body animation after contact because the generated take cropped raised hands. The time-slice uses constrained cutout parallax; the overhead finale and shadows are authored. These choices preserve the specified edit instead of substituting a different film.

Technical verification and inspected still/action samples are recorded separately from full-speed artistic approval. Musicality, naturalness of all motion, and a full-speed comparison with p(doom) have **not** been certified by a human reviewer. No claim of surpassing that reference is made.

## Source, credits and generation records

The [p(doom) renderer](https://github.com/mexicat/pdoom-video) by Giacomo Magnanini supplied actual MIT-licensed compositor, GLSL, deterministic math and finishing code. Adapted files and the original license are in `src/vendor/pdoom/`; the inspected revision and specific mechanisms are recorded in [source-study](build/source-study.md). Its song, lyrics and artwork are not used.

Ma Shan Zheng and ZCOOL KuaiLe are bundled with their OFL notices in `assets/fonts/`. All required display glyphs were checked. The source WAV is the user-supplied music.

Image artwork used Luma Uni-1 Max and built-in imagegen. [Built-in prompt specifications and provenance](build/imagegen-prompts.md), Luma manifests under `build/`, and motion manifests under `build/motion/`, `build/motion-more/` and `build/finale-motion/` preserve the production decisions. Request-based API estimates are in [cost-report](build/cost-report.json); built-in image generation uses subscription quota separately.

## Re-render

Use Node 22.23.1 (the repository's noninteractive default Node shim is older). Dependencies are pinned by `bun.lock`.

```sh
bun install
node node_modules/vite/bin/vite.js build --outDir build/dist
mkdir -p build/dist/assets
cp assets/production-assets.json build/dist/assets/production-assets.json
node build/serve.mjs
```

In another terminal, from this folder:

```sh
node build/render.mjs --port 5189 --out ../../renders/landing-day-one/landing-day-one-1440p60-silent.mov --from 0 --to 2621 --scale 1 --samples 4 --prores
```

`build/finish.py` performs delivery muxing and verification. `build/conform.py` resumes local source-frame extraction; it does not submit generation requests. Do not rerun generation manifests just to render the film. The saved source-image/video files are required.

`build/verify-render.mjs` tests arbitrary seeking and the final hold. GPU/Canvas raster rounding is checked with an explicit numerical tolerance; bit-for-bit equality of every intermediate GPU render is not claimed. The final eleven held frames are identical before encoding.
