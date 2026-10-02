# 第一天 — pre-motion review and handoff

## What is delivered

The complete 101-shot, 4:14 story reel uses reviewed photographic keyframes, the full supplied Mandarin recording, exact series/title graphics, and 77 Chinese lyric cues. The visual design is a luminous coastal future: ivory and ink costumes, pearl floors, titanium ribs, blue water and restrained coral hardware. Fast dance passages alternate with ordinary gestures, two long waiting holds, and the standing coda.

The film's central change is visible in the images: separate decks → missed connection → Lin on the fixed island while her empty deck leaves → Yu across the guarded bridge → a shared floor. The planned final-chorus dance includes a 7.9167-second uninterrupted full-body proof shot. That choreography is **planned**, not demonstrated by a held-image reel.

Watch the [Chinese lyric version](../../renders/first-day/first_day_story_reel_zh.mp4) or [clean picture version](../../renders/first-day/first_day_story_reel_clean.mp4). Reproduction instructions are in [README.md](README.md).

## Image review

Luma Uni-1 Max supplied the main image pass and environment work. Specific failures were repaired through built-in image edits: cropped or crowded shoes, reversed eyelines, misplaced people, duplicate furniture, merged platforms and inconsistent pair/coda framing. Exact prompts, source hashes and immutable input copies are recorded in `build/builtin_image_edits.json` and the five repair manifests. Built-in model and usage/cost were not exposed by that tool.

The topology repairs deliberately use simple plates: separate platform outlines, blue water on either side of one level guarded bridge, and a recognisable arch/rib identity for each floor. Later dock states derive from those plates. k36 intentionally repeats k16's starting image; k39 reuses k33's reaction; k54 returns to k52's standing coda. There are 55 keyframe entries, not a claim of 55 unique generated photographs.

The review checks complete images in edit order and native face/hand/foot details. Still acceptance covers identity, costume, composition, geography, visibility and the stated starting pose. It does not establish natural dancing, successful contact, weight transfer, traversing a bridge, mechanical motion, or continuity through a generated clip. Small hands in wide shots require motion-stage close inspection. Toe-led anticipation in k10 is not evidence of a completed heel-touch. The standing coda retains partial deck edges at the periphery: their departure is a future motion target, not something this held ending proves. Attempts to remove them degraded the photographic water and were rejected; k38 supplies the clear earlier proof that Lin stays on I while A leaves.

Full source images are fitted into 1920×1080 without a crop or imposed cinema bars. This episode's full-body dance framing is a deliberate 16:9 departure from the earlier general letterbox convention. There are no simulated pans, micro-zooms or dissolves in the story reel.

## Sound and text

The source MP3 and LRC remain unchanged. The 44.1 kHz stereo float master contains 11,199,636 samples per channel, with a single −8.2 dB gain adjustment. Measured master loudness is −16.0 LUFS, −8.0 dBTP and 6.1 LU LRA. No added speech, new score, SFX, cuts, tempo change, fades or silence. The 164–179.13-second stop is in the picture only.

The MP4 soundtrack is encoded once to AAC at 320 kb/s; both versions share that audio stream. Independent export checks found matching AAC packet hashes and decoded PCM, zero measured sample lag in five alignment windows, and −16.0 LUFS / −7.2 dBTP in the delivery decode. Picture lasts 6,096 frames at 24 fps, leaving 40 ms of picture after the complete 253.96-second master. Lyric starts preserve the supplied LRC. Provisional line endings avoid overlap and clear long gaps; the final lyric clears at 243.96 seconds before the closing credits. These are source-based timings, not verified sung-word alignment. Listening and experienced musical pacing remain for King's assembled playback review.

## Motion handoff — original pre-motion checkpoint

**2026-10-02 test update:** King subsequently authorized a short motion test. m10 and m42 were generated once each with MiniMax H3 Max; both returned downloadable video. The combined preview retains 418 returned frames at 24 fps (17.4167 seconds) and uses excerpts of the approved song master. The solo does not complete the specified phrase; the duet changes the contact sequence and pushes in until the feet leave frame. Neither take is accepted for production. See [the test receipt and review](build/motion_test.json) and [watch the preview](../../renders/first-day/first_day_motion_test.mp4). The remaining handoff below records the original stage 6 checkpoint, not the current submission state.

`build/motion_plan.json` prepares 53 jobs, defaulting to MiniMax H3 Max at 768P with prompt expansion disabled. Current source handles total **334 seconds** for primary takes and **440 seconds** including planned extra takes. The final read-only runner dry run observed $0.03/second, giving **$10.02 / $13.20**, before unplanned retakes or other finishing costs. This supersedes the earlier $0.025 historical guide. These are estimates, not charges or authorization to submit; refresh pricing before submission. The dry run completed successfully without a generation POST; its receipt is `build/motion_dry_run.json`.

Start with the three benchmarks recorded in the manifest:

1. **m10 — solo phrase:** grounded heel-touch, readable quarter-turn, the inward offered palm, and retreat; retain full shoes and identity.
2. **m36 — Lin's crossing:** complete natural traversal of the stationary guarded bridge. A 10-second source handle is allowed, but the locked 160–164-second picture interval must contain the full readable choice. If the performance cannot fit naturally, revise the edit under a separately reviewed motion cut; do not hide an incomplete crossing or speed it unnaturally.
3. **m42 — shared phrase:** correct contact, modest partner turn, grounded feet, and a visible release to low hands before the later connected pose. Keep the long full-body cut genuinely continuous.

Each starting frame governs which anatomical hand is offered. Lin invites toward screen right and Yu toward screen left. Preserve the visible hand through a shot; a later phrase may offer the other hand only after a clear release. m40 begins with the palm already open and adds one gentle inward step, without retreat or an artificial reset.

Landing stills from other camera angles are QA references, not forced end-image conditioning for locked crossing shots. Inspect start, actual action landmarks, completion and the intended trim independently. Source trims remain provisional until real motion exists. Preserve the actual starting environment and compare neighboring shots again after motion; correct input pixels do not guarantee correct generated movement.

## Generation accounting

The local fal ledger records **81 distinct accepted image request IDs**, including deliberate retakes and two k09 requests that returned HTTP 422 during recovery. One-image arithmetic at the observed authenticated/public image rates gives **$0.243 / $8.262**. Those conflicting rate scenarios are not an invoice or confirmed billed cost. The ledger distinguishes saved successful responses from incomplete local receipts; repeated polling of the same ID is not counted as another request. The rejected k09 calls were replaced by a reviewed built-in frame.

Built-in generations, including recorded intermediate repairs, are counted separately by output hash; deliberate file-copy aliases are excluded. Their usage and cost are unknown. At the original stage 6 checkpoint, no paid motion-generation request or public publishing action had been performed. The subsequent short test added two motion requests, totaling 17 requested seconds and a $0.51 estimate at the live quoted rate; this is not an invoice. No public publishing occurred.

## Evidence

- `build/plan_audit.json`: source integrity, image decoding and provenance, dependency graph, all 101 image/motion prompt matches, contiguous frame timing and motion-handle totals.
- `build/visual_review_early.json`, `visual_review_middle.json`, `visual_review_late.json`: detailed observations and repair history; final current-image evidence is in `visual_review_final.json`.
- `build/generation_ledger.json`: deduplicated request evidence and separate built-in output accounting.
- `renders/first-day/first_day_story_reel.render_report.json`: actual output geometry, decoded frame counts, durations and source hashes.
- `build/export_audit.json`: independent full decode, AAC packet equality, sample alignment, loudness, source integrity and subtitle-cue comparison.
- `build/export_frame_review.json`: all 377 sampled shot/lyric/title frame checks pass; nine native decoded frames visually checked for text, title/credits and foot clearance.
- `work/first-day/qa/`: full edit-order contact sheets, native review details and export-frame checks.

Stages 0–6 are complete through the story reel with its final soundtrack. The authorized stage 7 test is now complete; the full motion batch and stage 7b finishing remain outstanding. Playback review of the test is still required, and the observed choreography and framing failures must be resolved before production acceptance.
