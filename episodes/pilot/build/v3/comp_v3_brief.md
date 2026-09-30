# v3 story reel compositing brief (CONTINUITY, RELIEF redesign)

Repo /Users/kingh0730/repos/interregnum. Read these first:
- `CLAUDE.md`
- `episodes/pilot/bible/art_direction.md` (RELIEF), `episodes/pilot/bible/cinematography.md` (the camera-move rules: most shots are
  locked off; only the eight permitted moves exist) and `episodes/pilot/bible/production_design.md`
- `episodes/pilot/episode.md`, and each of YOUR shots' `episodes/pilot/shots/NN/shot.md` (Build, JS spec, Duration)
- `tools/comp/reel.py`

This is a stills reel: no video model. All motion comes from the Build: the permitted camera moves, screen content,
lamps, flaps, needles, paper, particles and light. Timeline and durations are exactly as in v1/v2 (242 s; the v1
frame count of each shot is the truth: `ffprobe -count_frames work/pilot/shots/NN.mp4`).

## Inputs
- **Keyframes:** `work/pilot/keys_v3/<id>.png` (the manifest `episodes/pilot/images_v3.json` maps ids to shots).
- **Lookdev:** `assets/pilot/lookdev_v3/`.
- **Screen pieces:** `work/pilot/js_v3/`, from pages in `episodes/pilot/js_v3/`. Each page header says whether its
  output is full-frame, an overlay, a screen texture (a 4:3 tube face with its artefacts already rendered; map it by
  homography into the keyframe's screen and add only reflection and grade, never a second tube pass), or an atlas.
  JSON files drive lamp and needle values.
- **Paper margins:** some keyframes show a sliver of cream paper at the edge (k07, k17, k23, maybe others). Always
  frame past it: raise the zoom until no margin is visible, and check every edge.

## Rules
- Never edit `tools/comp/reel.py`, `episodes/pilot/js_v3/*` or anything in `work/pilot/js_v3/`. Prepare
  intermediates under `work/pilot/comp_v3/`, and write each spec as `work/pilot/comp_v3/NN.json`.
- Output: `work/pilot/shots_v3/NN.mp4`, 1920x1080 at 24 fps, with exactly the v1 frame count.
- **Frames:** broadcast shots are 4:3 inside the frame (pillarboxed), as the bible says. World shots are 2.39
  letterbox.
- **Grade:** respect RELIEF: keep bloom low, glow only on screens and lamps, and grain as paper and ink, not film.
  Don't soften the carved edges.
- **Shot 04** is the pull-out reveal: the Father's 4:3 picture becomes a monitor at Ida's desk. Build it from the
  keyframes and plates the Build names.
- **QA:** run the `--preview` sheet first and Read it. Check the margins, the screen mapping, and the letterbox or
  pillarbox framing. Delete intermediates you no longer need. There's plenty of disk, but don't write PNG sequences.
- No git, no Codex, no fal.

## Report
A table of shot, frames and contents; problems; your 3 strongest and 3 weakest shots.
