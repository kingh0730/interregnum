# 第一天 · AI SI - I

Mandarin music-and-dance pilot, built around the complete supplied recording of 孙燕姿《第一天》. The selected story is **借一步 / Borrow a Step**: two people perform an apparent duet from separate travelling seaside galleries; Lin steps ashore and waits, giving Yu a real place to join her.

## Watch

- [Chinese lyric story reel](../../renders/first-day/first_day_story_reel_zh.mp4)
- [Clean picture story reel](../../renders/first-day/first_day_story_reel_clean.mp4) — switchable Chinese subtitle track, initially off.
- [Chinese subtitle sidecar](../../renders/first-day/first_day_story_reel.zh.srt)

These are **pre-motion story reels**, with held, reviewed images, the complete soundtrack, titles and lyrics. They establish the cut, visual direction and story geography. They are not the animated dance film. Picture runs 4:14 at 1920×1080/24 fps; the uncut recording runs 4:13.96.

## Production sources

- [Episode and story](episode.md), [script](script.md), [101-shot edit](shotlist.md).
- [Art direction](bible/art_direction.md), [production design](bible/production_design.md), [cinematography](bible/cinematography.md), [choreography](bible/choreography.md), [sound](bible/sound.md).
- [Final review and handoff](review.md).
- [Image recipes](build/keyframes.json), [frame timeline](build/timeline.json), [future motion manifest](build/motion_plan.json).
- [Generation records](build/generation_ledger.json), [local conformance audit](build/plan_audit.json).

The original MP3 and LRC are retained unchanged. The sound master applies one constant gain adjustment, with no rearrangement, added dialogue, score, effects, fades or invented silence. Lyric starts come from the supplied LRC; human listening must still confirm their sung alignment and the experienced pacing.

## Rebuild

From the repository root, with the existing local media:

```sh
uv run episodes/first-day/build/render_reel.py episodes/first-day/build/render.json --validate-only
uv run episodes/first-day/build/render_reel.py episodes/first-day/build/render.json
```

The renderer preserves entire source images, holds them without simulated camera movement, composes Chinese type locally, and checks both exports before replacing them. Generation assets live under `assets/`, intermediate media under `work/first-day/`, and exports under `renders/first-day/`; media are deliberately excluded from Git.

Stage 7 is prepared separately. No motion-generation request has been submitted. Use the handoff's three benchmark cases and inspect real action before approving a full motion batch.
