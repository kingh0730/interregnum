# Video model

Animates keyframes (image-to-video) for anything that has to move like drawn or filmed footage.

**Status:** waiting for an API key. The chosen model is **Seedance 2.5** (native dialogue with lip-sync; see `docs/strategy.md`). The candidate provider is **fal.ai**: confirm it hosts Seedance 2.5 and check prices. Used in v2 only.

**Plan:**
1. `export FAL_KEY=...` in the shell environment. Never write the key into a file in this repo.
2. Bake-off with Seedance 2.5 on 2–3 keyframes (a character close-up with a quoted line of dialogue, a wide establishing shot, an action beat). Check clip lengths, voice consistency across shots, audio-driven lip-sync, a clean no-music stem, and Chinese vs English. King judges the motion. Compare one other model only if Seedance disappoints.
3. Build `tools/video/i2v.py`: keyframe + motion prompt + duration → `work/<ep>/<shot>/takes/NN.mp4`, logging the model, seed and prompt next to each take.

**Prompting notes (to fill in during the bake-off):** camera language, acting verbs, which negatives help, max useful duration.
