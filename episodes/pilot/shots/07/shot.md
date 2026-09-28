# Shot 07 — IDA

**Duration:** 4 s (0:37–0:41; abs 37.0–41.0)  **Tool:** Codex keyframe + comp  **Camera:** MCU, three-quarter from
her front-left; slow push-in 1.00→1.03 on her eyes

**Action:** Our first real look at her. Ida, lit by the monitor just off the left edge, stylus raised, precise and
detached, more tired than anyone should be. By her keyboard sits a small dented amber thermos, unopened (Nana's
soup; it pays off at "The soup's still warm"). **Start pose (v2):** seated, stylus raised near the left edge, about
to tap.

**Build:**
- Codex **k04**:
  `tools/imagegen/gen.sh assets/pilot/keyframes/k04_ida_desk_mcu.png "<prompt>" assets/pilot/lookdev/ld4_ida.png assets/pilot/lookdev/ld1_hall.png`
- **Acceptance:** this keyframe sets Ida's face for the rest of the film. Check it against ld4_ida (bob, bangs,
  earring on her left ear, scarf) and retake if it drifts. Later Ida keyframes attach it.
- Comp:
  - `push(1.00→1.03, focus=(0.66, 0.40), easeInOutSine)`.
  - `flicker(mask=cyan_lit, driver=noise(0.8 Hz), 3 %)`: the monitor refreshing as she works.
  - `dust(20)` inside the screen light, in the space in front of her.
  - `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (k04):**
> STYLE: a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean, confident
> dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow only around
> light sources; subtle paper grain; realistic human proportions and faces (not chibi, no oversized eyes); simplified
> graphic backgrounds with bold silhouettes and large areas of dark negative space. PALETTE: deep ink-navy and
> blue-black darkness; cold pale-cyan light comes only from screens; warm amber light comes only from household lamps
> and warm objects; signal red only where described; no other saturated colors. LIGHT: one strong motivated light
> source, deep shadows, light haze. FRAME: wide 16:9 landscape; keep every important element inside the central
> horizontal band, because the top and bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters, numbers,
> logos or watermarks anywhere; every screen is a blank, evenly glowing panel.
> CHARACTER: IDA: a woman of 27, slim, with a short blunt jaw-length black bob and straight-cut bangs just above her
> eyebrows, dark brown eyes with tired lower lids, straight dark brows, a small straight nose, a small silver hoop
> earring in her left ear, warm light-olive skin; she wears a charcoal-grey ribbed turtleneck sweater, a hand-knitted
> mustard-amber wool scarf worn loosely around her neck, and a thin grey lanyard with a blank white ID card. Match the
> attached character sheet exactly.
> SHOT: a medium close-up of Ida seated at her desk, seen in three-quarter view from her front-left. She faces
> screen-left toward a monitor just outside the left edge of the frame, whose cold cyan glow is the key light on her
> face. She holds a slim stylus raised near the left edge, as if about to touch the screen. Her expression is focused,
> precise, detached and very tired. On the desk beside her keyboard sits a small dented amber-colored thermos flask,
> unopened. Behind her, far out of focus, the giant cyan monitor wall of the dark hall (in the style of the attached
> location frame) dissolves into soft glowing blocks. Composition: her head on the right third, looking left into
> open space, with comfortable headroom; her amber scarf catches a little of the light.

**Refs:** `assets/pilot/lookdev/ld4_ida.png`, `assets/pilot/lookdev/ld1_hall.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- Hall clock (38, 39, 40); hall tone and DRONE.
- Two small stylus taps at shot +1.5 and +2.7 (abs 38.5, 39.7).
- A slow exhale at +3.2 (abs 40.2).
- No dialogue.

**Motion prompt (v2):** Flat 2D cel-painted style. Ida sits at her desk, lit cold cyan by a monitor just off-frame
left, and makes two small precise stylus taps toward the screen, eyes steady and tired; then she exhales slowly.
Static camera with a very slow push-in. Hall hum, clock ticking, soft stylus taps. No music.

**Takes:** —
