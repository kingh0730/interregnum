# 第一天 — independent concept and delivery review

The pre-motion plan and canonical still assets pass this audit: 101 picture cuts,
55 keyframes, 53 planned motion jobs and 6,096 contiguous frames at 24 fps. The
complete supplied 253.96-second Mandarin song remains fixed. This report does not
approve generated motion, sound by listening, or the final subtitled playback.

## Story and continuity

The episode makes its relationship legible through changing distance: Lin and Yu
begin on separate touring decks; Lin chooses to cross first and wait; Yu answers
her invitation; the pair finishes standing together at the island's sea rail.
Before 160 seconds Lin remains on A, Yu on B and I is empty. Lin's crossing occupies
160–164 seconds, followed by the deliberate 164–179.13 hold. Yu's answer and
crossing occupy 179.13–191.05 seconds. Music-boundary frame quantization is retained.
The rest periods and held wait interrupt the quick dance editing as intended.

The early outline's wrist-circle motif, misplaced first crossing and seated coda
were corrected to the canonical script. The conflicting compass description of
sunlight was removed. Lin's sleeveless costume, Yu's standing start pose and the
coda's separate invitation/hold source ranges now agree across the plan.

Actual-pixel review required targeted repairs to eyelines, costume details,
complete feet and floor margins, duplicate benches, the spare jacket and dock
geography. The adopted crossing views clearly separate the peripheral floor from
the island, with a short level guarded bridge and visible water around it. Lin and
Yu start aboard their respective decks. The late landing and waiting states keep
the intended occupancy. Rejected source bytes and intermediate attempts remain
preserved; the review records retain the original failures.

The repeated palm gesture is locked by its inward screen direction and the visible
arm within each shot. The future plan does not promise a single anatomical arm
across every camera angle. Still poses establish intentions; they do not establish
weight transfer, gait, partner contact, moving-platform mechanics or synchronized
dance. Those remain explicit motion-review requirements.

## Frozen plan and assets

Every exact image prompt and every motion prompt matches its corresponding shot
document across all 101 cuts. Image dependencies resolve without cycles. Every
source trim fits its planned take and equals its edit interval. The planner's
comparison with the prior 832ffda plan retains all picture cuts, key IDs,
durations, sections, kinds and motion-job groupings. Source and derived hashes
were checked again against the final release and stayed unchanged during audit.

The final plan prepares 334 primary motion seconds, or 440 seconds including
planned takes. Both crossing jobs are ten seconds. Their landing pictures, k37
and k55, are QA references only because their cameras differ; neither is forced
as an end image. The first contact phrase completes and releases the hands before
a later contact phrase. The close invitation holds an already offered palm and
adds a gentle inward step, without repeating the heel-turn.

All 55 canonical image files decode. Thirty-three are explicitly external in the
scene manifest, including the intentional copies k36=k16, k39=k33 and k54=k52.
Their exact prompts, output hashes and immutable input hashes match the central
provenance. Final image uploads were verified against canonical bytes. The other
scene recipes retain their Luma provenance. Original portraits remain identity
authorities; neither the optional Lin sheet nor the rejected Yu sheet conditions
current scenes.

The final coda uses k52_v1 and its identical k54 copy, selected by the director for
its photographic water. Later alternatives remain recorded and are not canonical.
The early, middle and late visual reports bind their still findings to file hashes.
A successful file check does not replace those pixel reviews. Subtitle collisions
and the final sequence's playback rhythm belong to rendered-reel review.

## Audio and generation accounting

The source MP3 and LRC SHA-256 hashes remain unchanged. The audio integrity check
verified the complete source decode with only the recorded −8.2 dB gain: 11,199,636
stereo samples per channel at 44,100 Hz, exactly 253.960 seconds. The checked master
measures −16.0 LUFS. All 77 cue texts and supplied start times match the lyric
source; four metadata entries stay separate. The SRT matches the cue text and
millisecond timestamps. These are signal and text checks, without listening or
forced-alignment approval.

The local ledger contains 81 distinct accepted fal request IDs: 79 saved image
responses, one saved terminal HTTP422 response and one recovery request without a
saved response receipt. The director observed terminal HTTP422 for that recovery
in tool output; the ledger distinguishes this observation from local provider
receipts. An image response is not visual approval and none of these counts is a
billing statement.

Built-in provenance contains 36 distinct recorded generation-output SHA-256 values:
two base portraits and 34 scene edits, including rejected intermediate outputs.
The three intentional copy aliases are excluded, and outputs recorded in both a
repair batch and the central registry count once. Built-in usage and price were
not exposed. The ledger's separate fal arithmetic scenarios use supplied rates;
they are not confirmed charges. No motion generation is submitted by this audit.

Run `uv run episodes/first-day/build/delivery_audit.py` after any recipe or asset
change. Machine-check details and the final source hashes are in
`build/plan_audit.json`; generation accounting is in `build/generation_ledger.json`.

## Completed export technical checks

Both finished reels independently decode to 6,096 frames at 1920×1080 and 24 fps.
Their AAC packet payloads and decoded audio match each other exactly. Stereo audio
remains 44,100 Hz with the full 253.960-second declared program starting at zero.
Five sampled waveform comparisons against the unchanged master find zero sample
lag. Each decoded delivery measures −16.0 LUFS and −7.2 dBTP. Raw AAC decoding
exposes 876 additional silent codec-padding samples; those are outside the
container-declared program, and the original final silent second is preserved.
All 77 exported subtitle cues match the approved text and times; the SRT adds only
a final newline. Source MP3/LRC and every rendered image-input hash remain intact.
See `build/export_audit.json` for the file hashes, methods and limits. These checks
do not claim listening, visual subtitle placement or dance synchronization.
