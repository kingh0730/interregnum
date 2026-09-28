# Shot 17 — IDA CALLS

**Duration:** 4 s (1:30–1:34; abs 90.0–94.0)  **Tool:** Codex keyframe + comp  **Camera:** MCU, Ida facing
screen-left; push-in 1.00→1.03

**Action:** Ida has turned her back on the monitors, the phone pressed to her ear, hunched and private. "Nana. Don't
wait up tonight." It is a warning she doesn't explain, and it plants the danger. **Start pose (v2):** the phone at
her ear, eyes lowered, lips closed, about to speak.

**Build:**
- Codex **k10**:
  `tools/imagegen/gen.sh assets/pilot/keyframes/k10_ida_phone_mcu.png "<prompt>" assets/pilot/lookdev/ld4_ida.png assets/pilot/keyframes/k04_ida_desk_mcu.png`
- Comp:
  - `push(1.00→1.03, focus=her eyes)`.
  - Background monitor-wall bokeh with a 2 % slow brightness drift. `flicker(mask=cyan_lit, driver=noise(0.5 Hz), 2 %)`.
  - `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (k10):**
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
> SHOT: a medium close-up of Ida at her desk in a dark hall. She has turned away from her monitors and faces
> screen-left, shoulders slightly hunched, holding a small slim dark phone to her ear on the side facing the camera.
> Her eyes are lowered, her expression private and soft, lips closed, about to speak. Cold cyan light from the
> monitors behind her rims her hair and shoulder; the side of her face toward camera is in soft shadow, with a faint
> warm glow from the phone. Behind her, the giant monitor wall is out-of-focus cyan blocks. The small amber thermos
> stands on the desk. Composition: Ida left of center, looking left, with headroom above.

**Refs:** `assets/pilot/lookdev/ld4_ida.png`, `assets/pilot/keyframes/k04_ida_desk_mcu.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- **IDA** (`Samantha`, 165, IDA hall chain): **"Nana. Don't wait up tonight."** at shot +0.5 (abs 90.5).
- Phone-line hiss bed; hall tone; the hall clock (quieter, −4 dB); warm PAD.

**Motion prompt (v2):** Flat 2D cel-painted style. Medium close-up: Ida at her desk, turned away from her monitors,
holds a small phone to her ear and speaks softly, eyes lowered: "Nana. Don't wait up tonight." Slight head movement,
a tired breath. Static camera, slight push-in. Quiet hall hum. No music.

**Takes:** —
