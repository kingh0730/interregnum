# Shot 25 — HER EYES

**Duration:** 3 s (2:13–2:16; abs 133.0–136.0)  **Tool:** Codex keyframe + comp  **Camera:** ECU of her eyes; push-in
1.00→1.02

**Action:** Her eyes are wet, with lines of glowing text reflected in them. The red phone rings, and she doesn't look
away. The cut to her also covers time: two more lines get typed while we're on her. **Start pose (v2):** eyes looking
down at the keyboard, a tear gathering on the lower lid.

**Build:**
- Codex **k15**:
  `tools/imagegen/gen.sh assets/pilot/keyframes/k15_ida_ecu.png "<prompt>" assets/pilot/lookdev/ld4_ida.png assets/pilot/keyframes/k07_ida_cu.png`
- Comp:
  - `push(1.00→1.02, focus=between the eyes)`.
  - Optional: in each eye highlight, a tiny mirrored crop of J10's text band at 25 %, scrolling up 20 px over the
    shot (as if she is reading).
  - `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (k15):**
> STYLE: a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean, confident
> dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow only around
> light sources; subtle paper grain; realistic human proportions and faces (not chibi, no oversized eyes); simplified
> graphic backgrounds with bold silhouettes and large areas of dark negative space. PALETTE: deep ink-navy and
> blue-black darkness; cold pale-cyan light comes only from screens; warm amber light comes only from household lamps
> and warm objects; signal red only where described; no other saturated colors. LIGHT: one strong motivated light
> source, deep shadows, light haze. FRAME: wide 16:9 landscape; keep every important element inside the central
> horizontal band, because the top and bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters, numbers,
> logos or watermarks anywhere; every screen is a blank, evenly glowing panel.
> CHARACTER: IDA: a woman of 27 with a short blunt black bob and straight-cut bangs just above her eyebrows, dark brown
> eyes with tired lower lids, straight dark brows, a small straight nose and warm light-olive skin. She is exactly the
> same woman as in the attached images.
> SHOT: an extreme close-up of Ida's eyes and the bridge of her nose, framed from her eyebrows to just below her eyes
> and filling the frame width, with her straight black bangs at the top edge. Her eyes look slightly down toward a
> keyboard. They are wet and reflect tiny lines of glowing cyan light, and a single tear gathers on the lower lid of
> one eye but has not fallen. Cold cyan light comes from below; everything else falls into darkness.

**Refs:** `assets/pilot/lookdev/ld4_ida.png`, `assets/pilot/keyframes/k07_ida_cu.png`.
**Layers:** none.
**JS spec:** none (the optional reflection uses a J10 frame).

**Sound:**
- The red phone ring at +1.0 (abs 134.0), in the hall reverb.
- PULSE; the hall clock; muffled keystrokes (−10 dB) at an irregular typing rhythm under the shot. She is typing the
  two lines we'll see in 26.
- **RISER starts at 0.0 (abs 133.0)** and runs to 149.0.
- No dialogue.

**Motion prompt (v2):** Flat 2D cel-painted style. Extreme close-up of Ida's eyes, wet and reflecting glowing lines
of text. A tear gathers; she blinks once slowly and keeps looking down at the screen, her eyes moving as she reads.
Static camera. A telephone rings somewhere off-screen; low hum. No music.

**Takes:** —
