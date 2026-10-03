# Graphics v2 — Bun and Canvas

The complete overlay pass is authored in `film.js` and rendered by Chrome through Bun.
Python/ffmpeg only conforms the existing clean footage; it draws no graphics in this revision.
The v1 export is preserved.

## Deliverables

- `renders/first-day-anime-test/first-day_opus55_graphics-v2_1080p30.mp4`
- `renders/first-day-anime-test/first-day_opus55_graphics-v2_540p30.mp4`
- Diagnostic frames: `work/first-day-anime-test/graphics-v2/qa/`
- Technical review: `episodes/first-day-anime-test/build/graphics-v2/review.json`

## Changes

| Passage | New treatment |
| --- | --- |
| Glasses → feed | One uniformly scaled and rotated plane throughout both shots. No squeeze mapping or renderer switch at the old cut. |
| Calendar | Typeset calendar with thirty circled repetitions, layered page edges, bindings, shadows, a curved page turn and an unprinted back face. |
| Thinking mark | One authoritative SVG, isolated with restrained illumination and properly spaced type. |
| Levitation / bursts | Existing animated paper retained; additional blank polygon cards and stacked burst logos removed. Light and fine particles replace the clutter. |
| Greeting | Fixed left origin and baseline, preloaded fonts, deterministic character reveal and restrained cursor timing. |
| Music page | Authored notation, paper lighting and triangulated curved surfaces. The two leaves split independently; no triangle bridges the opening gap. |
| Flight | Source camera bank retained. Whole-frame rotations and mirrored edge extension removed; face crops preserved. |
| Helix | Fine luminous calligraphic trails replace opaque broad ribbons; characters and lyrics remain readable. |
| Danmaku | Measured text widths and constant per-lane velocities prevent overlapping comments. Density tapers into the ending. |
| 39-second transition | Image-to-image light wipe from the actual outgoing embrace frame into the meadow; no empty white shot. |
| Titles / captions | Shared font and spacing system, textured colour fields, restrained linework and a quieter end card. Act I lyrics sit in the lower matte. |

This is a revision of the overlays and edit presentation, not a new set of generated performances.
Graphics baked into the existing generated takes retain their original model limitations.

## Rebuild

From the repository root:

```sh
.venv/bin/python episodes/first-day-anime-test/build/graphics-v2/prepare_base.py
bun episodes/first-day-anime-test/build/graphics-v2/render.ts --stills
bun episodes/first-day-anime-test/build/graphics-v2/render.ts
```

The renderer uses the existing `tools/web/node_modules/puppeteer-core` installation and Google Chrome.
It serves only local production resources on a temporary loopback port. Every frame uses absolute timeline
time and seeded procedural details. Source clips are validated against their required frame counts,
padded only where needed for conformance, then assigned a continuous 30 fps clock.

A truncated Noto Sans SC file from the earlier asset download was replaced for this pass. The complete font
is `work/first-day-anime-test/graphics-v2/fonts/NotoSansSC.ttf`, sourced from
`https://raw.githubusercontent.com/google/fonts/main/ofl/notosanssc/NotoSansSC%5Bwght%5D.ttf`.
Its SIL OFL licence is the existing `work/first-day-anime-test/assets/fonts/NotoSansSC-OFL.txt`.
All custom browser font families have unique names and are explicitly loaded before rendering.

Review includes transition-frame inspection, a pixel comparison of the fixed greeting prefix, full export
decoding, frame count and a check that the 39-second sequence retains image content. These checks do not
substitute for normal-speed audiovisual playback.
