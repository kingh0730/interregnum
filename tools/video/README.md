# Video model

Animates keyframes (image-to-video) for anything that has to move like drawn or filmed footage.

**Status:** working (`i2v.py`, fal.ai queue API, key from `$FAL_KEY`). Bake-off done 2026-09-29, about $24. The chosen model is **Seedance 2.5** (native dialogue with lip-sync; see `docs/strategy.md`). The candidate provider is **fal.ai**: confirm it hosts Seedance 2.5 and check prices. Used in v2 only.

**Plan:**
1. `export FAL_KEY=...` in the shell environment. Never write the key into a file in this repo.
2. Bake-off with Seedance 2.5 on 2–3 keyframes (a character close-up with a quoted line of dialogue, a wide establishing shot, an action beat). Check clip lengths, voice consistency across shots, audio-driven lip-sync, a clean no-music stem, and Chinese vs English. King judges the motion. Compare one other model only if Seedance disappoints.
3. Build `tools/video/i2v.py`: keyframe + motion prompt + duration → `work/<ep>/<shot>/takes/NN.mp4`, logging the model, seed and prompt next to each take.

**Bake-off findings (2026-09-29; pilot shots 16, 17, 19 and 44; stills, transcripts and pitch only, motion unverified):**
- **Endpoint:** `bytedance/seedance-2.5/image-to-video` gives 720p at most, 4–30 s, about $0.47/s at 720p ($0.22/s at 480p), in about 4–8 min per take.
  Output is 1280×720 at 24 fps, upscaled to 1080p in the conform.
- **Style and identity:** the flat cel look and the characters hold from the start frame, with no drift across 4–10 s.
- **Dialogue:** a line written in quotes in the prompt is spoken word for word (Whisper-verified), with visible mouth shapes and acting.
  Reference-to-video with an `[Audio1]` voice keeps the start frame's composition, but it ad-libbed a word, and pitch
  didn't move toward the reference. Voice identity needs ears.
- **Unwanted audio:** a no-dialogue take may carry a spoken phrase. For non-dialogue shots use `--no-audio` and keep our sound design.
- **Story effects:** a "windows switch to amber" prompt gave one gimmick take (a glowing dome) and one good take (patchy
  window-by-window spread). Generate 2 takes of any effect-driven shot; sky or colour changes are left to the grade.
- **Recipe:** the shot's motion prompt as written, 2 drafts at 480p, the winner re-rendered at 720p with its seed.

**Prompting notes (to fill in during the bake-off):** camera language, acting verbs, which negatives help, max useful duration.
