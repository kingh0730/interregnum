# 第一天 — independent concept and plan review

Review authority: the director's canonical Chinese script and production lock. The
complete supplied 253.96-second song remains fixed. This review does not approve
unseen motion, sound by listening, or unfinished image assets.

## Initial material findings — resolved and verified

1. **The English episode outline contradicts the canonical script.** Its verse
   describes a wrist-circle where the fixed phrase uses a quarter-turn; its
   164–179.13-second section starts with Lin crossing where she must already have
   crossed at 160–164 seconds; its coda specifies sitting where the canonical
   coda ends standing at the sea rail. Harmonize the outline before deriving shots.
   The crossing conflict matters most: it replaces the deliberate hard stop with
   another action and obscures the choice to stay.
2. **Sunlight has contradictory geographic coordinates.** The production lock
   places the common camera north of the island looking south, then describes
   west sunlight as screen-left. In that view, west is screen-right. Choose one
   consistent physical direction and carry it through the common master and
   reverse-angle prompts. A merely frame-relative source is acceptable if the
   contradictory compass claim is removed.

The previously rejected look tests did not meet the requested futuristic scale;
the director is already replacing that world master. No acceptance is inferred
from those tests. The story premise itself is understandable without a technical
explanation: the island is a place to wait, Lin waits first, and Yu answers.

## Locked checks for the next pass

- Before 160 seconds: Lin stays on A, Yu stays on B, I remains empty.
- 160–164: Lin crosses through a stopped, open, level left dock; both feet arrive
  on I before the hard hold begins.
- 164–179.13: Lin stays on I while A leaves; the camera and her body hold.
- 179.13–191.05: Lin repeats heel-touch → quarter-turn → palm, omits retreat;
  Yu sees her and crosses the stopped, open, level right dock.
- First final-chorus phrase: feet and actual hand contact remain visible in one
  eventual sustained two-shot. Pose cuts in this reel remain illustrative.
- Coda: pair stands at the sea rail, with no return to separate galleries.
- Original face references and shared A/B/I set references appear wherever needed;
  image dependency IDs resolve and precede dependent generation.
- Each image-manifest prompt matches its corresponding `shot.md` prompt exactly.
- Motion jobs name required actions and landing poses; the final timeline points
  to existing assets and totals the full 6,096 frames at 24 fps.

## Plan audit

The first complete plan contains 101 shots, 55 keyframes, 53 future motion jobs,
and 6,096 contiguous frames. Automated inspection found no exact-image-prompt
mismatches between the manifest and shot documents; all motion prompts also match.
Reference/base/dependency IDs resolve without cycles. Every source trim is within
its planned take and equals its edit interval. Final source trims remain provisional.

Three observed conflicts were repaired and the regenerated files rechecked:

1. k46 now specifies Lin's bare forearm and ivory top edge, preserving her sleeveless costume.
2. k33 now keeps Yu standing throughout its start pose and action.
3. m52 now completes the invitation by 4.5 seconds, then holds. Shot 100 uses its
   separate 6–9.208-second tail, without replaying shot 98's action.

The planner has already separated Yu's landing (k55) from the final duet start
(k42), avoiding an accidental eleven-second identical-plate hold across that turn.
Lin's crossing and waiting windows and Yu's answer windows match the locked story,
with frame-ceiling quantization at the music boundaries. The plan passes: no unresolved narrative, prompt, dependency, or timing conflicts
were found in this audit. It prepares 327 primary motion seconds, or 426 seconds
including the planned takes. Image existence and visual continuity remain pending
generation. No motion quality is approved.


## Frozen production recipe and audio refresh

The frozen recipes retain 101 shots, 55 keyframes, 53 future motion jobs and all
6,096 contiguous frames. Exact image prompts and motion prompts match all 101 shot
documents. Reference/base/dependency IDs resolve without cycles; every source trim
fits its planned take and edit interval. The recipe now uses approved composition
frames to retain floor space and local architecture. Current scene conditioning
uses no character sheets and at most five reference URLs. Original portraits
remain the face authorities wherever the face is readable. This replaces the
previous broader reference bundles after the director's representative tests.

k10 and k42 are completed built-in reframes, explicitly marked as external in the
scene manifest. Their exact edit prompts, output hashes and every input hash match
the recorded provenance. They must be excluded from Luma submission. All other
scene recipes use Luma. k05's approved oblique establishing view governs the later
geography variations; it is not described as the local north-to-south camera view.
The future motion plan continues to total 327 primary seconds, or 426 seconds with
planned takes. No motion requests are submitted or approved by this review.

Three current keyframes decode (k05, k10, k42); the remaining 52 are pending
production at this audit. File existence is not pixel approval. The independent
visual reviewer has separately assessed the three existing compositions; complete
shot-to-shot image continuity remains open. Re-run
`uv run episodes/first-day/build/delivery_audit.py` after generation or recipe edits.

The current master PCM checksum was checked again and still matches the complete
source decode with only the recorded −8.2 dB gain. It retains 11,199,636 stereo
samples per channel at 44,100 Hz: exactly 253.960 seconds. Source MP3 and LRC SHA-256
hashes remain unchanged. All 77 cue texts and start times match the supplied lyric
lines exactly; all four metadata entries are separated; the SRT matches those cues
and their millisecond timestamps. No cue timing was revised. These are signal and
text integrity checks, not listening or forced-alignment approval.
