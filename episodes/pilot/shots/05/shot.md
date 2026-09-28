# Shot 05 — THE HALL

**Duration:** 8 s (0:22–0:30; abs 22.0–30.0)  **Tool:** Codex keyframe + cutout layer + comp + screen insert
**Camera:** super-wide, symmetrical, from high at the back of the hall. Slow dolly-in (push 1.00→1.07) toward the one
lit desk, with parallax.

**Action:** A concrete cathedral in the dark. Rows of shrouded desks recede toward a wall of monitors that shows the
frozen face, twenty metres tall, still wearing its wireframe. Far below, one lit desk and one small woman with an
amber scarf. That is the whole power structure in a single image. Nobody moves; dust drifts in the light. **Start
pose (v2):** Ida seated with her back to camera at the lit desk.

**Build:**
- Codex **k03**:
  `tools/imagegen/gen.sh assets/pilot/keyframes/k03_hall_wide.png "<prompt>" assets/pilot/lookdev/ld1_hall.png assets/pilot/lookdev/ld4_ida.png`
- Codex layer (`ALPHA=1`), see **Layers**.
- Comp:
  - `insert(src=work/pilot/k02_mesh_state.png composited over k02_frozen, target=auto)` into the blank cyan monitor
    wall. The wall is frontal and rectangular, so fit 4 corners. Then `bezels(12×8, 6 px)`, tile jitter ±4 %, haze mix
    15 % toward `#1A3550`, and bloom. The face stays desaturated as in shot 04.
  - `push(1.00→1.07, focus=(0.50, 0.74), easeInOutSine, 0–8 s)`, with `parallax(k03_fg_desks=1.0, plate=0.55)`.
  - `dust(120)`: slow drift up-left, lit only inside the cyan light cone.
  - The red lamp box above the wall stays unlit here.
  - `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (k03):**
> STYLE: a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean, confident
> dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow only around
> light sources; subtle paper grain; realistic human proportions and faces (not chibi, no oversized eyes); simplified
> graphic backgrounds with bold silhouettes and large areas of dark negative space. PALETTE: deep ink-navy and
> blue-black darkness; cold pale-cyan light comes only from screens; warm amber light comes only from household lamps
> and warm objects; signal red only where described; no other saturated colors. LIGHT: one strong motivated light
> source, deep shadows, light haze. FRAME: wide 16:9 landscape; keep every important element inside the central
> horizontal band, because the top and bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters, numbers,
> logos or watermarks anywhere; every screen is a blank, evenly glowing panel.
> LOCATION: the Hall of a government broadcast ministry at night, drawn in the style of the attached style frame. An
> immense dark hall like the nave of a concrete cathedral, seen from high up at the back in perfect symmetrical
> one-point perspective. Rows of abandoned operator desks covered with pale dust sheets recede in straight lines
> toward the far wall. The entire far wall is one colossal, flat, frontal, rectangular wall of monitors (a grid of
> about 12 by 8 screens with thin black bezels), all glowing one plain, even, pale cyan with nothing on them. They
> throw cold light and long shadows down the hall through faint haze. Above the monitor wall, centered, is a small
> unlit red signal-lamp box. Brass pneumatic-tube pipes run up the concrete columns.
> CHARACTER: in the lower center of the frame, far away and small, a single desk lit by its own two small monitors,
> where a lone young woman sits with her back to us: a short blunt black bob, a charcoal sweater, and a mustard-amber
> scarf, which is the only warm color in the image (she is the woman on the attached character sheet). Dust motes
> hang in the light beams; the ceiling is lost in darkness. Mood: vast, silent, sacred, lonely.

**Refs:** `assets/pilot/lookdev/ld1_hall.png`, `assets/pilot/lookdev/ld4_ida.png`.

**Layers:** `assets/pilot/layers/k03_fg_desks.png` (`ALPHA=1`, attach k03). Prompt:
> Using the attached image, isolate only the two nearest rows of dust-sheeted desks at the far left and far right
> edges of the frame (the closest foreground desks), exactly as they appear, with the same position, scale, lighting
> and flat cel-painted style, on a genuinely transparent background. Everything else must be fully transparent.
> Keep the image the same size as the original.

Align the layer to k03 with SIFT (`tools/comp/legacy/v2_align_layers.py`) and inpaint the plate behind it. Shot 43
reuses this layer on k26.

**JS spec:** none new. The wall insert is shot 04's frozen state (k02 plus the J16 mesh).

**Sound:**
- Hall room tone (55 Hz hum and air); rain on a high roof, distant.
- **Hall clock ticks** on every whole second (22, 23, … 29), in HALL REVERB.
- A distant pneumatic hiss at shot +5.5 (abs 27.5).
- Score 1M2: DRONE fades in from 22.0 over 3 s.
- No dialogue.

**Motion prompt (v2):** A vast dark concrete broadcast hall in flat 2D cel-painted style. Slow dolly forward down
the central aisle toward the single lit desk, where a small woman sits with her back to camera. The giant frozen face
on the monitor wall glows cold cyan, dust drifts through the light beams, and a faint haze moves. Nobody moves. Low
electrical hum, rain on a high roof, a clock ticking. No music.

**Takes:** —
