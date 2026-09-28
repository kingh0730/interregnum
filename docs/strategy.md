# Production strategy: v1 → v2 (agreed with King, 2026-09-29)

An engineer's approach: build everything that is **orthogonal** to what the paid models do well, ship a complete
version, then use the models to polish.

## v1: the story reel (Claude alone, no paid models)
A complete, watchable cut of each episode, like a Pixar story reel or a very good motion comic. Judge it on story,
pacing and images, not motion.
- Story, script, edit timing and subtitles
- Codex keyframes for every shot (`tools/imagegen/gen.sh`)
- Blender for 3D set pieces and exact camera moves; JS for in-world screens, titles and graphics
- Python compositing: layers, parallax, particles, light FX, grading
- Sound design and ambience; **scratch dialogue** with macOS `say` voices to time every line
- **Temp score** that defines tempo and hit points (it becomes the Suno cue sheet)

## v2: polish (paid models)
- **Seedance 2.5** (video model) replaces held keyframes shot by shot, and speaks the dialogue with lip-sync
- **Suno** replaces the temp score

## Contracts that make v2 a swap, not a redo
- **Keyframes double as image-to-video start frames:** composition, headroom and the pose at the *start* of the action.
- **Shot durations fit the model's clip lengths** (around 5–10 s; confirm in the bake-off).
- **Every `shot.md` carries its motion prompt and exact quoted dialogue**, so v2 is a batch job.
- **Dialogue is written for lip-sync:** one clear speaker per shot, mouth visible, short lines that fit inside one
  clip. Write dialogue scenes as shot/reverse-shot, not crowded two-shots.
- **Prompt Seedance for dialogue and effects but no background music**, so the score stays Suno's. Claude mixes the stems.
- **Music:** Suno won't hit exact timings, so expect to re-cut some scenes to the real music in v2. That's normal.

## Seedance 2.5 (from third-party guides, verify in the bake-off)
- Generates video, dialogue with lip-sync, sound effects and ambience in one pass; 8+ languages including English and Chinese.
  Dialogue goes in quotes in the prompt. A supplied voice or music track can reportedly drive the lip-sync and pacing.
- **Known weak spot: voice consistency across shots.** Fallback: generate each character's voice once, then drive
  every shot from that audio.
- Test both Chinese and English quality if the series is bilingual.
- Needs an API key through a provider that hosts it (fal.ai is the candidate; check availability and price). Key in env only.

## Suno (music)
- **No public API** (partner program only, since July 2026). Since 2026-09-03 its terms only allow commercial use of
  tracks **downloaded directly from Suno on a paid plan**, so third-party wrappers leave a public release unlicensed.
- Workflow: Claude writes a **cue sheet** per episode (in/out times, mood arc, tempo, instrumentation, reference
  works, lyrics, a ready-to-paste Suno prompt) → King generates tracks in Suno and drops the downloads into
  `audio/music/` → Claude cuts them to picture and mixes.
