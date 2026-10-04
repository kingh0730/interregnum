# 第一天 / First Day — Opus 5.5

## Graphics revision — Bun / Canvas

**Superseded: this revision departed from the locked director plan and is not a fidelity-approved master.**
The active shot-by-shot rebuild is tracked in `episodes/first-day-anime-test/build/faithful/compliance.json`.

Latest revision: `renders/first-day-anime-test/first-day_opus55_graphics-v2_1080p30.mp4`
(smaller copy: `renders/first-day-anime-test/first-day_opus55_graphics-v2_540p30.mp4`).
The overlay system was rebuilt after playback feedback. See
`episodes/first-day-anime-test/build/graphics-v2/README.md` for changes, checks and Bun rebuild commands.
The original production record and export below are retained as v1.


Full-length production cut: **43.70 seconds, 44 timeline shots, 1,311 frames, 1920×1080 at 30 fps**.
Codex built-in image generation supplied the artwork; MiniMax H3 Max supplied character and camera passes.
**No Luma was used.** The original song is the only soundtrack, encoded to AAC at the final mux.

## Watch

- Master: `renders/first-day-anime-test/first-day_opus55_1080p30.mp4`
- Smaller preview: `renders/first-day-anime-test/first-day_opus55_540p30.mp4`
- Full-film contact sheet: `renders/first-day-anime-test/first-day_opus55_1080p30-contact.jpg`
- Earlier animatic: `renders/first-day-anime-test/animatic.mp4`
- Original opening test: `renders/first-day-anime-test/opening-test_1080p30.mp4`
- Audio timing plot: `renders/first-day-anime-test/timing.png`

Generated media, fonts, logos, source takes, earlier takes and frame samples remain under the ignored
`work/first-day-anime-test/` and `renders/first-day-anime-test/` directories. They are not committed.
The character/environment references and official-vector sources are in
`work/first-day-anime-test/assets/`; font licence texts are in its `fonts/` subdirectory.

## Execution

The opening test was followed by the complete source package, full animatic, representative ankle/contact/helix
motion tests, remaining motion passes, targeted retakes, and the final composite. All lyrics and UI copy are
font-rendered. The screen reply is projected onto the monitor. The supplied official spark and A paths are
composited into plates or graphics; the image model was asked for blank pins and labels.

`episodes/first-day-anime-test/shotlog.csv` records every timeline shot, chosen take interval, seed, prompt and
retry count. Exact submitted motion requests are in
`episodes/first-day-anime-test/build/motion-plan-final.json`; the resumable request logs and estimated-cost
ledger are in `work/first-day-anime-test/h3_log/`. **Estimated motion spend: $4.29**, including retakes
(28 accepted requests, 143 generated seconds). This is the request ledger estimate, not an invoice.
Codex image calls additionally used subscription quota.

| Section | Implementation |
| --- | --- |
| S01–S02 | Codex face plate, projective reflection, authored feed animation; approved opening retained |
| S03–S13 | Room/tea/levitation passes plus calendar, screen reply, bursts and frozen stop-time graphics |
| S14 | Pure graphics: two white impact frames, departing bars, serif title, shake and chromatic edge split |
| S15–S19 | Birth/breath/pullback passes, authored music-page folds, glyphs and coral particles |
| S20–S23 | Conditioned ankle descent, three-step interval, observed fingertip contact, keyed hand orbit |
| S24–S33 | Sprint, keyed leap orbit, flight, billboard-frame composite, face inserts, climb and rolled float |
| S34 | Continuous two-person keyed camera pass with an authored 450° ribbon camera, text-ring pass, projected lyric and spark completion |
| S35 | Paper running pass sampled on stepped timing, with independently moving foreground paper grasses |
| S36–S43 | Short face/gesture/city/helix/embrace inserts, official spark, danmaku wall and whiteout |
| S44 | Toe movement and crane-away take, sky bubble and halo, paper end-card wipe, fade to cream |

Image prompts and provenance are in `episodes/first-day-anime-test/image-prompts.json`,
`episodes/first-day-anime-test/build/generation-records.json` and
`episodes/first-day-anime-test/build/resumed-image-prompts.json`.
The city insert is a crop of the environment sheet: `(0, 537, 593, 887)` in its 1774×887 source.
Exact mark placements and clean-source relationships are recorded by
`episodes/first-day-anime-test/build/mark_plates.py`.

## Repairs and method changes

- Corrected Opus's initial hair/skirt proportions; removed an extra ankle chain, restored Xiaoman's bare feet
  in the meadow, and erased invented lettering on the leap's paper sheets.
- Made a genuine pre-contact ankle frame; selected the observed landing interval rather than the whole take.
- Retook birth eye-colour drift, cropped walking feet, shortened flight hair and unwanted head sparkles.
- The first contact take achieved the clasp but missed the requested orbit. Extracted its actual clasp frame
  and used a keyed camera pass; retook unwanted release/background lettering.
- The five-view helix sheet failed the rear-view test. The selected character pass instead uses H3 camera
  keyframes for continuous intermediate views of both women, combined with local 3D ribbon geometry.
- Paper folding uses authored polygons rather than a cloth simulation. The reveal uses a push/zoom composite
  rather than a reconstructed room-depth rig. The shoe transition is carried by the impact, particle burst
  and barefoot incoming flight frame. No dedicated sung lip-sync pass is included.
- Meme wording was retained. `episodes/first-day-anime-test/build/assets-sources.md` records the searches,
  their limits, official artwork sources and font licences; no unverified capability claims were added.

## Verification and remaining review

`episodes/first-day-anime-test/build/delivery-audit.json` records export dimensions, frame count, full decode,
source hashes and costs. `episodes/first-day-anime-test/build/audio-integrity.json` records the decoded
song/output comparison. Lyric anchors retain `round(t*30)` frame positions. The opening ends at frame 85
(2.8333 seconds, nearest frame to 2.84). Onset data and the separately labelled provisional bar grid remain
in `episodes/first-day-anime-test/timing.json`; the measured stop-time RMS reduction is 93.5%.

Sampled source and rendered frames were inspected, with particular attention to identity, contact, feet,
text and the helix. These are **not** a normal-speed audiovisual approval or proof that every prescribed
camera angle and choreography detail was achieved exactly. `episodes/first-day-anime-test/build/continuity-review.json`
is specifically a conditioning-source review; final moving cut states have a separate pending review record.
The original plan's all-gates-passed status is not claimed.

The weakest passage is the integration of generated camera motion with the authored helix ribbons and halo.
Further polish should prioritize that integration, exact orbit/footfall timing, and fine costume/logo
preservation through generated motion. Review the assembled film with its song, especially 20.7–25.5 and
30.68–34.21 seconds. Normal-speed motion and audio judgment still need King's eyes and ears.

## Rebuild

From the repository root:

```sh
.venv/bin/python episodes/first-day-anime-test/build/render.py
.venv/bin/python episodes/first-day-anime-test/build/package.py
ffmpeg -y -i renders/first-day-anime-test/first-day_opus55_1080p30.mp4 -vf scale=960:540 -c:v libx264 -crf 20 -c:a copy -movflags +faststart renders/first-day-anime-test/first-day_opus55_540p30.mp4
```

Use `--animatic --width 960` for the stills animatic or `--only 14` for an individual shot. The final renderer
rejects missing plates or required motion takes. Existing accepted requests can be recovered with the saved
`work/first-day-anime-test/motion-plan.json`; do not regenerate that manifest or use `--redo` merely to resume.
Dependencies: Pillow, numpy, OpenCV, librosa, matplotlib, fontTools and ffmpeg. Exact fonts are retained locally;
Arial Unicode supplies the two missing emoticon glyphs on this macOS machine.
