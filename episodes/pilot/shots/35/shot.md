# Shot 35 — ON AIR OFF

**Duration:** 2 s (3:06–3:08; abs 186.0–188.0)  **Tool:** Codex keyframe + comp  **Camera:** ECU, static

**Action:** High on the hall's concrete wall, the red signal lamp clicks off. The building's hum winds down to
nothing. It is the end of the broadcast, and of something larger. The letterbox is back: we are in the world, and the
Father's full frame is gone for good. **Start pose (v2):** the lamp lit; the action is switching off.

**Build:**
- Codex **k21** (the lamp lit, blank glass):
  `tools/imagegen/gen.sh assets/pilot/keyframes/k21_on_air_lamp.png "<prompt>" assets/pilot/lookdev/ld1_hall.png`
- Comp:
  - **Lettering:** render `ON AIR` (DIN Condensed Bold, sized to 60 % of the glass width) as a mask. It shows as
    brighter, hotter red letters in the lit glass (+25 % luma, slightly orange) and as barely visible darker letters
    when unlit. Warp it onto the glass face with a homography of its 4 corners.
  - At **0.4 s the lamp switches off**: the red glass luminance drops to 12 % over 3 frames, with an orange filament
    afterglow decaying over 0.3 s. The red halo in the haze vanishes with it.
  - `letterbox(2.39)`, `grade(HALL)`. Static camera.

**Keyframe prompt (k21):**
> STYLE: a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean, confident
> dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow only around
> light sources; subtle paper grain; realistic human proportions and faces (not chibi, no oversized eyes); simplified
> graphic backgrounds with bold silhouettes and large areas of dark negative space. PALETTE: deep ink-navy and
> blue-black darkness; cold pale-cyan light comes only from screens; warm amber light comes only from household lamps
> and warm objects; signal red only where described; no other saturated colors. LIGHT: one strong motivated light
> source, deep shadows, light haze. FRAME: wide 16:9 landscape; keep every important element inside the central
> horizontal band, because the top and bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters, numbers,
> logos or watermarks anywhere; every screen is a blank, evenly glowing panel.
> SHOT: an extreme close-up of an old rectangular broadcast signal-lamp box mounted high on a dark concrete wall, in
> the hall of the attached style frame. It has a riveted metal housing with a frosted red glass front, glowing bright
> signal red and completely blank, with no lettering. It casts a faint red halo into the surrounding haze. A faint
> cyan glow from far below touches the underside of the housing. Composition: the lamp centered, filling the middle
> third of the frame, the glass face square to the camera, dark wall around it.

**Refs:** `assets/pilot/lookdev/ld1_hall.png`.
**Layers:** none.
**JS spec:** the `ON AIR` lettering mask (static; DIN Condensed Bold, tracking 0.2 em).

**Sound:**
- **Relay click at +0.4 (abs 186.4).**
- The hall's electrical hum winds down from 55 Hz to 20 Hz, with gain going to zero over 1.4 s.
- Then silence: no clock (it stopped), no phone yet.

**Motion prompt (v2):** Flat 2D cel-painted style. Extreme close-up of an old red signal lamp on a concrete wall,
glowing bright red. With a click it switches off, and the glow fades from the frosted glass. Static camera. A relay
click, an electrical hum winding down. No music. (In v2, re-apply the ON AIR lettering in comp.)

**Takes:** —
