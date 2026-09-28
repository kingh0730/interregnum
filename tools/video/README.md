# Video model

Animates keyframes (image-to-video) for anything that has to move like drawn or filmed footage.

**Status:** waiting for an API key. Suggested provider: **fal.ai**, because one key and pay-per-use billing give access to several models (Kling, Seedance, Veo, Wan). Check current models and prices before choosing; Sora was discontinued in 2026.

**Plan:**
1. `export FAL_KEY=...` in the shell environment. Never write the key into a file in this repo.
2. Bake-off: animate the same 2–3 keyframes (a character close-up, a wide establishing shot, an action beat) with 2–3 models; King picks.
3. Build `tools/video/i2v.py`: keyframe + motion prompt + duration → `work/<ep>/<shot>/takes/NN.mp4`, logging the model, seed and prompt next to each take.

**Prompting notes (to fill in during the bake-off):** camera language, acting verbs, which negatives help, max useful duration.
