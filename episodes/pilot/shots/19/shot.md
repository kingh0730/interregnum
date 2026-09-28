# Shot 19 — THE QUESTION

**Duration:** 4 s (1:39–1:43; abs 99.0–103.0)  **Tool:** Codex keyframe + comp  **Camera:** CU, Ida facing screen-left;
push-in 1.00→1.03

**Action:** Ida lifts her eyes toward the face she makes every night and asks the question she's been carrying: "Why
do you still watch him?" It's guilt, frustration and love at once. **Start pose (v2):** phone at her ear, eyes lifted
toward the off-screen monitors, lips slightly parted.

**Build:**
- Codex **k12**:
  `tools/imagegen/gen.sh assets/pilot/keyframes/k12_ida_phone_cu.png "<prompt>" assets/pilot/lookdev/ld4_ida.png assets/pilot/keyframes/k10_ida_phone_mcu.png`
- Comp: `push(1.00→1.03, focus=eyes)`, `flicker(mask=cyan_lit, driver=noise(0.5 Hz), 2 %)`, `letterbox(2.39)`,
  `grade(HALL)`.

**Keyframe prompt (k12):**
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
> mustard-amber wool scarf worn loosely around her neck, and a thin grey lanyard with a blank white ID card. She is
> exactly the same woman as in the attached images.
> SHOT: a close-up of Ida holding a small slim dark phone to her ear on the side facing the camera, her face
> three-quarters toward screen-left. She has lifted her eyes toward the offscreen monitors with a hesitant, pained
> look; her lips are slightly parted, about to ask a question. Cold cyan light comes from the left side, with a faint
> warm glow from the phone on her cheek. Background: dark, with soft cyan bokeh. Composition: face left of center,
> eyes on the upper third, the amber scarf at the bottom edge.

**Refs:** `assets/pilot/lookdev/ld4_ida.png`, `assets/pilot/keyframes/k10_ida_phone_mcu.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- **IDA** (`Samantha`, 165, IDA hall chain): **"Why do you still watch him?"** at shot +0.6 (abs 99.6).
- Phone-line hiss; hall tone; the hall clock at −4 dB; warm PAD (Dm from 100.0).
- **PLUCK A4** (Nana's theme, note 1) at +3.6 (abs 102.6): the question hangs.

**Motion prompt (v2):** Flat 2D cel-painted style. Close-up: Ida, phone at her ear, lifts her eyes toward the
off-screen monitors and asks, hesitantly: "Why do you still watch him?" She swallows after the line. Static camera.
Hall hum. No music.

**Takes:** —
