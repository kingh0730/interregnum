# Shot 32 — IDA LOOKS UP

**Duration:** 6 s (2:48–2:54; abs 168.0–174.0)  **Tool:** Codex keyframe + comp  **Camera:** from high in front of
her, the monitor wall's point of view. **Pull-back 1.06→1.00**, the only pull-back until the ending: the world
widening.

**Action:** In the hall, Ida watches her own words come out of his mouth, huge, filling the building: "Tomorrow,
you'll have to talk to each other." For the nation it means there will be no more addresses. For her it means Nana:
the two of them have only talked through him. The red phone rings on. **Start pose (v2):** seated, face tilted up to
the wall, eyes wet, hands on the keyboard.

**Build:**
- Codex **k18**:
  `tools/imagegen/gen.sh assets/pilot/keyframes/k18_ida_looks_up.png "<prompt>" assets/pilot/lookdev/ld4_ida.png assets/pilot/lookdev/ld1_hall.png assets/pilot/keyframes/k04_ida_desk_mcu.png`
- Comp:
  - `pull(1.06→1.00, focus=Ida's face)`.
  - `flicker(mask=cyan_lit, driver=constant + noise(0.3 Hz) 2 %)`: she is lit by the giant wall.
  - `dust(60)` falling slowly through the top light.
  - `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (k18):**
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
> SHOT: seen from high in front of her, as if from a giant wall of screens: Ida sits at her lone lit desk in the vast
> dark hall of the attached location frame. Her face is tilted up toward the camera and lit strongly by cold cyan light
> from above; her eyes are wide and wet, her lips closed. Her hands rest on the keyboard, and the small dented amber
> thermos stands on the desk. Around her in the darkness are rows of empty desks under pale dust sheets. Composition:
> Ida in the lower center, looking up just past the lens, with a lot of dark space around her.

**Refs:** `assets/pilot/lookdev/ld4_ida.png`, `assets/pilot/lookdev/ld1_hall.png`, `assets/pilot/keyframes/k04_ida_desk_mcu.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- **FATHER** (`Daniel`, 135, HALL chain: huge, from the wall, 6 s reverb): **"Tomorrow, you'll have to talk to each
  other."** at shot +0.6 (abs 168.6).
- The red phone rings at abs 170.0 and 173.0 (hall reverb, −12 dB).
- The hall clock ticks (its last minutes).
- Hall tone. No music.

**Motion prompt (v2):** Flat 2D cel-painted style. Ida sits at her lone desk in a vast dark hall, looking up at a
giant screen above the camera. Her face is lit cold cyan and her eyes are wet, and she does not move. From huge
speakers, an old man's voice says: "Tomorrow, you'll have to talk to each other." Slow pull-back revealing the empty
desks around her. Hall reverb, a telephone ringing. No music.

**Takes:** —
