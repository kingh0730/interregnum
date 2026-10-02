---
name: dance-generation
description: "First Day dance test: H3 Max still-image-plus-text missed choreography and camera lock; prove a short phrase before bulk motion"
metadata:
  node_type: memory
  type: feedback
  modified: 2026-10-02
---

## Observation (2026-10-02)

King watched the First Day motion test and said the dance did not really work, then explicitly asked to remember
this observation. Two MiniMax H3 Max image-to-video takes used approved photoreal stills and detailed text
choreography, at 768P with prompt expansion disabled: m10 solo (7 seconds requested) and m42 duet (10 seconds).

- **Solo:** forward walking and an arm gesture replaced the required heel-touch, quarter-turn, offer and retreat.
  The camera also reframed despite the locked-camera instruction.
- **Duet:** contact broke for a roughly full solo turn, followed by a second contact, instead of one modest connected
  turn. A camera push-in cropped feet by 3.25 seconds. Palms were still joined at the planned 8.417-second cut;
  the later lowering moved hands out of view, so a fully visible release and settled finish were not verified.
- Both returned technically usable video, but neither passed its planned dance action and framing requirements.

## Limits and how to apply

This is evidence against **our tested still-image-plus-text approach to this choreography**, based on one take per
case. It does not establish that all AI dance, other models, simpler movement, or performance-reference workflows
fail. The song was added afterward; no music conditioning or dance-performance reference was supplied. Beat
alignment was not tested, so do not record poor beat synchronization as an established model limitation.

Do not assume attractive poses or detailed choreography prompts establish a viable dance performance. Keep the
First Day full motion batch on hold; demonstrate a convincing short phrase in playback before scaling this
approach. Any new paid test still needs applicable authorization. A real dance-performance reference is a
candidate to test, not a demonstrated fix. Do not silently substitute walking and posing for a dance brief.

Evidence: `episodes/first-day/build/motion_test.json` contains requests, source hashes, timing observations and
review limits. Preview: `renders/first-day/first_day_motion_test.mp4`. Full source takes and sampled-frame evidence
remain under `work/first-day/motion/` and `work/first-day/motion-test/`.

Related: [[taste-notes]], [[episode-defaults]].
