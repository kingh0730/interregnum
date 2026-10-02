# COMMON ROOM / 一室两家

**AI SI - I · Episode 01 · 3:50 · 1920×1080 · 24 fps**

Eda and Sen are dividing their home. In a world where different addresses can open into the same physical room, they choose to keep one full kitchen shared. Their separate lives begin; so does the inconvenience of sharing a worktop.

**Current status: review version; spatial-continuity approval withdrawn.** User review identified continuity failures at shots 05→06 (00:25) and 23→24 (01:59). The full episode still requires a continuity audit and repair before motion. No video-model request has been submitted. See the [current continuity gate](build/continuity_review.json).

## Open the episode

- [Review-version story reel](../../renders/ep01/common_room_story_reel.mp4) — unchanged media; all 40 shots, paper-state changes, prepared sound and Chinese-first bilingual subtitles. Spatial continuity is not approved.
- [Bilingual SRT](../../renders/ep01/common_room_story_reel.srt).
- [Final WAV master](../../work/ep01/audio/master_mix.wav) — 48 kHz stereo, 24-bit.
- [Script](script.md), [shot list](shotlist.md), [creative review](creative-review.md), and [motion handoff](motion_plan.md).
- [Delivery manifest](build/delivery_manifest.json), [export audit](build/export_audit.json), [visual review](build/visual_review.json), and [motion preflight](build/motion_preflight.json).

Media links point into this local workspace. Generated media and service/account logs are intentionally excluded from Git; the production recipes and audit summaries are committed.

## Existing material and technical checks

The package contains the researched concept, locked bilingual script, art/camera/production/sound bibles, character and location references, 27 selected photographic plates, six exact paper states, an authored end card, 26 dialogue lines, original score, designed effects and the current edit. Reference selection does not establish spatial continuity across the assembled cuts. The reel uses native 16:9 composition without letterboxing or artificial camera drift. Its one deliberate music/action stop falls at 01:49, followed by ten uninterrupted seconds of kitchen air and the decision tableau.

Luma Uni-1 Max supplied the original photographic material. Codex built-in edits supplied the selected scene variants; exact lettering was authored with code. `build/assets.json` records the current selection, without establishing spatial continuity. `build/codex_edits.json` retains executed scene-edit prompts. `build/images.json` and `build/plate_prompts.json` preserve original generation plans and history; they are not instructions to resubmit every entry.

Audio delivery includes five matching stems and 26 isolated dialogue files, 23 prepared for on-screen lip-sync. See [the audio file index](../../work/ep01/audio/delivery.json). The master measures **−18.0 LUFS, −1.8 dBTP and 15.6 LU loudness range**. Format, sample integrity, subtitle bounds, line lengths and the exact sound stop pass technical checks.

Earlier still and caption inspections are retained as historical findings; their spatial-continuity sign-off is superseded by the current blocked review. The technical export and muxed-audio audits remain PASS: complete decode, frame count, sample integrity and measured alignment are unchanged. **Perceptual audio playback has not been performed:** voice naturalness, generated-effect recognition, musical effect and final listening balance remain listening-review items. These technical results do not establish artistic or spatial approval. Generated character motion does not yet exist.

**Superseded status history:** the earlier release description said, “Production is complete through the still-based story reel and prepared final sound. The next stage is video generation.” That readiness claim is withdrawn; the existing reel is a review version requiring continuity work first.

## Rebuild locally

With the existing ignored media restored, these commands make no generation requests. They do not clear the blocked continuity gate or turn the current reel into an approved motion handoff:

```sh
uv run episodes/ep01/build/render_reel.py --prepare-review
uv run episodes/ep01/build/render_reel.py --jobs 2
uv run python episodes/ep01/build/motion_preflight.py --runner-dry-run
uv run python episodes/ep01/build/package_delivery.py
```

The renderer uses ffmpeg/ffprobe and the local Helvetica and Hiragino Sans GB fonts. It validates inputs before rendering, caches exact static segments and refuses to publish if source hashes change. `--prepare-review` creates the actual caption/state composites and contact sheets without encoding video. The motion dry-run checks all images and isolated audio and prices the existing runner without submitting footage.

## Motion and cost

The handoff records **30 proposed H3 Max jobs: 23 lip-sync and seven silent action shots**, with held inserts and exact graphics retained in the edit. **Motion is blocked pending full continuity audit, repair and renewed approval.** The earlier quote remains **$0.89** for three tests, included in the **$8.28** first-pass estimate; a proposed $4 retake reserve makes a **$12.28** envelope. Repairs may require revising that plan. These are future estimates; current motion spending is zero.

The recorded fal usage estimate is **$2.456 for successful outputs**, or **$2.969** if every failed request is conservatively priced too. These figures are not reconciled invoices. The 39 known built-in image-edit calls and ElevenLabs subscription usage are recorded separately without an invented dollar charge. See [the budget audit](build/budget_estimate.json).
