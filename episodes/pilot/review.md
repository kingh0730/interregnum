# Pilot v1 review: CONTINUITY (built overnight 2026-09-29)

**Watch:** `renders/pilot/continuity_v1.mp4` (4:02). Then `continuity_v1_alt_ending.mp4`, which is the same cut plus
a 10 s cynical tail (shot 46). Subtitles are burned in; `.srt` files sit next to both.

This is the v1 story reel: Codex keyframes, compositing, JS screens, `say` scratch voices, and a synthesized temp score.
There's no video model and no Suno. Judge it on story, pacing, images and sound design, not on character motion.

## What Claude could not check
Claude judged stills and audio metrics only. These need your eyes and ears:
- **Overall pacing and whether it plays or feels like "PPT".** The writer designed stillness into the story (the Father
  *is* a frozen image), but you're the judge.
- **Motion events:** the capsule drop (10), the glitch and freeze (04), the archive scroll (08), the loop overflow (12),
  the typing rhythm and amber autocomplete (24, 26), the dissolve (34), and the window wave (44).
- **Sound:** balance, the tape-stop at 0:19, the "I am well" choir building to STOP at 1:10, and the walla near the end.
  The `say` voices are timing placeholders.

## Weakest shots (the compositors' own notes)
- **07, 13, 17, 19, 25, 32:** quiet pushes on stills. Correct to the spec, but closest to "PPT"; they're the best
  candidates for Seedance in v2.
- **10:** the capsule turns mid-fall and looks a little oversized.
- **37:** a flat phone screen.
- **40:** a 1.28× digital punch-in that's visibly softer.
- **30, 43:** soft inpainted edges may show behind the parallax layers.

## Decisions for you
1. **Main ending or alt ending (46)?**
2. **Does the angle work as the series opener?** `episode.md` has a table of which questionnaire answers would change
   what, including the company-set variant if the dead-leader premise is a red line.
3. **Is the look right?** It's flat 2D cel with navy ink, cyan screens and amber lamps. Codex drifts toward 3D renders
   unless it's pushed, so the style lead lives in `build/style_prefix.txt`.

## Rebuilding
- **Recipes:** they're in `build/`.
  - `images.json` holds every Codex prompt; run `tools/imagegen/batch.py` with `--prefix-file`.
  - `comp/NN.json` holds the shot specs for `tools/comp/reel.py`. Run the prep scripts in `comp/c1`, `comp/s16_30` and
    `comp/c31_46` first.
  - `audio/main.json` is the mix, rendered with `tools/audio/mix.py`.
  - `edit_*.json` are the conforms, run with `tools/comp/assemble.py`.
- **Paths:** the recipes point at `work/pilot/`. Copy them back there to re-run.
