# Shot 15 — THE CITY

**Duration:** 7 s (1:17–1:24; abs 77.0–84.0)  **Tool:** Codex keyframe + cutout layer + comp + screen insert
**Camera:** long lens across the canal. It trucks left 3 % while pushing 1.00→1.06, and ends centered on the one
amber window. Parallax.

**Action:** The city in rain. Across a black canal, towers stacked into the distance with hundreds of windows, and
nearly every one glows the same cold blue: every television shows the stand-by Lamp and waits for him. The windows
breathe together, in sync. One window is warm. We drift toward it. **This composition is reused at dawn (shot 44)**,
where the warmth spreads from this window across the city. **Start pose (v2):** static city in the rain.

**Build:**
- Codex **k08**:
  `tools/imagegen/gen.sh assets/pilot/keyframes/k08_city_night.png "<prompt>" assets/pilot/lookdev/ld2_city.png`
- Codex layer **k08_fg_tower** (`ALPHA=1`, attach k08).
- **Acceptance:** the windows must be clean, flat, separable rectangles (they are masked in shot 44), and there must
  be exactly one amber window, at about the lower-right third point.
- Comp:
  - **Window mask:** HSV threshold on the flat cyan (hue about 180–195°, high value) → connected components. Save it
    to `work/pilot/k08_windows.npz` for shot 44.
  - All cyan windows breathe together: ±6 % luma at 0.25 Hz, in phase with the J15 stand-by breathing on the TVs.
  - The amber window stays steady with a soft warm glow.
  - `insert(J15 stand-by, target=the blank billboard at far left)`, plus bloom.
  - `truck(−3 %, 0)` combined with `push(1.00→1.06)`, with the focus ending on the amber window (easeInOutSine), and
    `parallax(k08_fg_tower=1.0, plate=0.4)`.
  - `rain(layers=2)`: far layer fine and dense at a 20° slant; near layer long, sparse streaks.
  - Canal: animated ripple displacement on the reflections (subtle noise flow).
  - `letterbox(2.39)`, `grade(CITY)`.

**Keyframe prompt (k08):**
> STYLE: a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean, confident
> dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow only around
> light sources; subtle paper grain; realistic human proportions and faces (not chibi, no oversized eyes); simplified
> graphic backgrounds with bold silhouettes and large areas of dark negative space. PALETTE: deep ink-navy and
> blue-black darkness; cold pale-cyan light comes only from screens; warm amber light comes only from household lamps
> and warm objects; signal red only where described; no other saturated colors. LIGHT: one strong motivated light
> source, deep shadows, light haze. FRAME: wide 16:9 landscape; keep every important element inside the central
> horizontal band, because the top and bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters, numbers,
> logos or watermarks anywhere; every screen is a blank, evenly glowing panel.
> LOCATION: the City at night, in the architecture and style of the attached style frame. A long-lens view across a
> dark canal toward a dense wall of identical concrete residential tower blocks stacked one behind another. Their
> facades are strict grids of hundreds of small square windows drawn as clean flat rectangles, and almost every window
> glows the same flat cold cyan-blue, as if lit by television screens. Exactly one window glows warm amber from a
> household lamp: it is in the nearest tower at the lower right, on the lower-right third point. Heavy rain falls in
> fine slanted streaks. Tram wires cut diagonally across the upper frame. The black canal reflects the cyan windows in
> long broken streaks. Low clouds glow faintly. At the far left, a taller distant building carries a huge blank
> billboard screen glowing plain cyan. Mood: a whole city waiting in front of the same screen; one warm light.

**Refs:** `assets/pilot/lookdev/ld2_city.png`.

**Layers:** `assets/pilot/layers/k08_fg_tower.png` (`ALPHA=1`, attach k08). Prompt:
> Using the attached image, isolate only the nearest tower block at the right side of the frame (including the
> single warm amber window), exactly as it appears, with the same position, scale, lighting and flat cel-painted
> style, on a genuinely transparent background. Everything else must be fully transparent. Keep the image the same
> size as the original.

**JS spec:** uses **J15 stand-by** (the breathing emblem on a blue gradient, no text) for the billboard.

**Sound:**
- City rain in wide stereo; canal lapping.
- **Tram bell** at shot +2.0 and +2.6 (abs 79.0, 79.6), distant.
- **City stand-by chime** at +3.0 (abs 80.0): the CHIME smeared through a 4 s reverb, as if from a thousand
  televisions at once.
- Score 1M3: the warm PAD (F) fades in from +5.0 (abs 82.0).
- No hall clock.

**Motion prompt (v2):** Flat 2D cel-painted style. A long-lens night view across a canal to tower blocks in heavy
rain. Hundreds of windows glow the same cold blue and one window glows warm amber. Rain streaks, ripples run on the
canal, and the blue windows pulse faintly in unison. Very slow drift left and push toward the amber window. Rain, a
distant tram bell, a faint chime echoing from many televisions. No music.

**Takes:** —
