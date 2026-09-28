# Shot 04 — FREEZE

**Duration:** 3 s (0:19–0:22; abs 19.0–22.0)  **Tool:** comp + JS overlay on k02 (the frozen last frame of 03)
**Camera:** held; the push is frozen at 1.04

**Action:** Mid-breath, the broadcast tears and stops. The sound tape-stops into silence. A cyan wireframe snaps onto
the Father's face point by point, his left ear smears into a ghost of itself, and a red box flags it: DRIFT. Black
bars slide in from top and bottom, because we are no longer watching television. Timecode: CALIBRATION · REPLAY
NIGHT 211. A mouse click, and a clock begins to tick. **Reveal 1: he is a render, and someone is fixing him.**

**Build:** comp on `work/pilot/k02_frozen.png` (the last frame of shot 03 with the push at 1.04, without the bug).
- **0.00–0.12 s** `glitch(slices=4, ±12 px, rgb=4 px, 3 frames)` with a 20 % luma dip.
- **0.12 s** freeze. Then `desat(60 %)` over 0.12–0.42 s. The J14 bug disappears at 0.12.
- **0.15–0.45 s** `letterbox_in` (bars 0→138 px, easeOutCubic). This is the film's first letterbox.
- **0.20 s** the J16 mesh overlay (below) snaps on.
- **0.80 s** the ghost ear: duplicate the left-ear region of the image (the ear on image right, about 90×150 px), offset
  +6 px in x, at 40 % opacity. The red box and its label appear at the same time.
- **1.0–1.6 s** the timecode counts frames, then stops at 1.6 (the click).
- Hold to 3.0 s. `grade(HALL)` (the world grade, not broadcast), grain 2 %.

**Keyframe prompt:** none new (reuses k02 from shot 03).
**Refs:** `assets/pilot/keyframes/k02_father_cu.png` (via `work/pilot/k02_frozen.png`).
**Layers:** none.

**JS spec (J16 mesh + J02 labels; transparent 1920×1080 overlay, aligned to the frozen frame):**
- **Mesh:** about 120 landmark points marked once by hand on k02 at push 1.04 and saved as
  `episodes/pilot/js/mesh_k02.json`: brows 10, eyes 16, nose 9, mouth 20, jaw and beard line 17, ears 8, hairline 10,
  beard outline 12, cheeks 8, forehead 10. Delaunay triangulation.
  - Points: 4 px dots, `#5FE1E6` at 90 %, popping in over 0.20–0.45 s (random order).
  - Lines: 1.5 px `#5FE1E6` at 55 %, drawing on over 0.45–0.80 s.
- **Red box:** a 2 px `#E0412F` stroke around the ghost ear, with a 12 px tick mark at its top-left corner.
  - Label above the box: `L EAR · DRIFT +3.2 PX`, DIN Alternate Bold 22 px `#E0412F`.
- **Timecode:** at (60, 900), inside the bottom of the letterbox band, Menlo 24 px `#5FE1E6`:
  `CALIBRATION · REPLAY NIGHT 211 · 20:51:07:14`. The frames field counts 14 → 23 (1.0–1.6 s), then stops.
- **Desk tag:** at (60, 170), Menlo 20 px `#5FE1E6` at 60 %: `NIGHT DESK 4`.
- Save the full overlay state at 3.0 s as `work/pilot/k02_mesh_state.png`. Shots 05 and 06 reuse it.

**Sound:**
- **0.0–0.4 s TAPE-STOP** of the whole mix (the Father's hymn and room tone), plus a 0.12 s glitch zap at 0.0.
- 0.4–3.0 s the hall room tone fades in: vast, a 55 Hz hum and air.
- Mouse click at +1.6 (abs 20.6). **The hall clock starts at +2.0 (abs 21.0)** and ticks every whole second from here.
- No dialogue.

**Motion prompt:** n/a. In v2 this stays a comp and JS effect on the last frame of shot 03's clip.
**Takes:** —
