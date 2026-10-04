# 第一天 / First Day — director-plan rebuild

The current cut is `renders/first-day-anime-test/first-day_opus55_faithful_1080p30.mp4`.
It is 43.70 seconds, 44 shots and 1,311 frames at 1920×1080/30 fps. The smaller copy is
`renders/first-day-anime-test/first-day_opus55_faithful_540p30.mp4`.

This rebuild follows the unchanged `episodes/first-day-anime-test/director-response.md` and replaces the
previous graphics revision. The compositor is HTML/Canvas/WebGL, bundled and rendered with Bun.
Codex built-in image generation supplies the illustrated assets; MiniMax H3 Max supplies performance and
multi-angle passes. No Luma was used. The original MP3 is the sole soundtrack, encoded once to AAC at mux.

## What changed

- S01–S02 share one uniformly scaled feed surface, including the transition through the glasses. There is no
  stretched-text version switching to an unrelated flat feed.
- S03 uses a mounted, textured calendar with thirty circled 明天 entries and a falling torn page revealing 今天.
  S05 projects real-font text onto the tracked monitor, preserving the plant's foreground occlusion.
- S06 has one spark inside the Thinking indicator. S07 uses bent paper, rising straw and rattling keycaps.
  S08–S11 share measured ring radii. S13 types on the stationary monitor with the prescribed four-percent push.
- S14 has two pure-white impact frames, the departing bars, large Lora title and a shatter made from its actual
  printed pixels. S15 uses a hinged music-paper humanoid and a matched closed-eye dive; the eye opens at 12.93.
- S16 has a depth-separated room, persistent Xiaoman, isolated hair-unfurl performance, a twelve-percent camera
  push and widening lens. Ceiling extension preserves every original room pixel.
- S20 uses the observed foot contact and a six-centimetre camera settle. S21 selects exactly the first three
  planted steps, conformed to 18.65, 19.00 and 19.35, retaining the face at the end.
- S23, S25 and S34 use authored 3D camera paths with isolated multi-angle paired-character passes. The hand orbit
  is 270° at 24 mm. The frozen leap orbits 360° in 1.1 seconds, then dissolves the actual shoes and socks into
  a registered barefoot end state. The continuous helix orbits 450°, rolls 20°, crosses the text halo at 32.00
  and completes the spark at 33.50.
- S26–S27 travel through actual 3D towers and a billboard frame. Glass surfaces reflect both characters. The
  barrel roll is a camera move through that space. S32 uses a true camera roll and cylindrical sheet-music lanterns.
- S35 has five depth layers made from the detailed paper illustration, with running figures sampled at 12 fps.
  S36–S43 retain the prescribed montage, including the white-then-ivory S43 shot. S44 cranes from the moving toes
  to the meadow, then resolves to the official cream end card.

## Evidence and review scope

`episodes/first-day-anime-test/build/faithful/verification.json` records the encoded-file checks, frame counts,
lyric request times, camera traces, pure-white/cream frames, and decoded original-song comparison.
`episodes/first-day-anime-test/build/faithful/compliance.json` maps all 105 shot requirements to implementation
and review evidence. A rendered camera value does not itself establish pleasing motion or physical correctness.
Sampled frame review and normal-speed audiovisual review are separate; the latter, including precise Mandarin
lip-sync, remains pending. No all-gates-passed claim is made.

The full-resolution contact sheet is `renders/first-day-anime-test/first-day_opus55_faithful-contact.jpg`.
Each render retains its exact bundle, requested-asset hashes, camera trace and diagnostic frames under the ignored
`work/first-day-anime-test/faithful/runs/` directory. The current run is named in the verification report.

The technically weakest part remains the transition between generated character views in the fastest orbits.
The background camera paths are exact, but the performance sources are generated 2D views. Further production
budget should go to coherent multi-view character animation and sung-mouth timing after playback feedback.

## Rebuild

From the repository root, with the retained local assets:

```sh
cd episodes/first-day-anime-test/build/faithful
bun install --frozen-lockfile
bun run render
```

`bun run stills` renders diagnostic frames; `bun run preview` renders a 540p working movie. The renderer rejects
browser/shader errors and media/source changes during a run. Final validation and the smaller delivery copy:

```sh
.venv/bin/python episodes/first-day-anime-test/build/faithful/verify.py
ffmpeg -y -i renders/first-day-anime-test/first-day_opus55_faithful_1080p30.mp4 -vf scale=960:540 -c:v libx264 -crf 20 -c:a copy -movflags +faststart renders/first-day-anime-test/first-day_opus55_faithful_540p30.mp4
```

Bun 1.3.14, Three 0.186.1, Chrome 154 and ffmpeg were used. The existing repository Puppeteer installation is
imported by the renderer. Python preparation uses Pillow, numpy, OpenCV, rembg/ONNX Runtime and librosa.
Prepared media is retained, so rendering does not regenerate or purchase anything. Preparation scripts with
source approvals are historical recipes guarded by fixed reviewed-input hashes; new sources need a fresh review.

The original production and superseded graphics-v2 records are retained in
`episodes/first-day-anime-test/build/faithful/legacy-production.md`.
Exact correction prompts and motion manifests are in `build/faithful/generations.json` and
`build/faithful/motion-provenance.json` relative to this episode. The correction motion ledger totals **$1.75**
for eleven accepted requests; with the original $4.29, the recorded estimate is **$6.04**, not an invoice.
Codex image generation also used subscription quota. Rejected masks/takes are retained and identified in the
production notes; none of the failed room-background actor masks are used by the delivered reveal or hero orbits.

Official Claude/Anthropic vector paths come from the official Claude site, as recorded in
`episodes/first-day-anime-test/build/assets-sources.md`. Noto Serif SC, Noto Sans SC, Lora and Inter are retained
with their SIL OFL licences; Noto Sans Symbols 2 supplies the missing emoticon symbols, also under SIL OFL.
Font binaries and source artwork remain in ignored working assets. Meme wording remains the director's bank;
search evidence and its limits are recorded in the existing asset-source note.
