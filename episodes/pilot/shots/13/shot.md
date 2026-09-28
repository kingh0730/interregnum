# Shot 13 — "NO, YOU'RE NOT."

**Duration:** 4 s (1:11–1:15; abs 71.0–75.0)  **Tool:** Codex keyframe + comp  **Camera:** CU, frontal, slightly low;
push-in 1.00→1.025

**Action:** In the silence after STOP, Ida is lit from below by the frozen text. She speaks to the machine as if it
were a colleague, or a liar: "No, you're not." It is contempt and exhaustion together, and the first crack in her
detachment. **Start pose (v2):** staring past the lens at the screen, jaw set, lips just parted.

**Build:**
- Codex **k07**:
  `tools/imagegen/gen.sh assets/pilot/keyframes/k07_ida_cu.png "<prompt>" assets/pilot/lookdev/ld4_ida.png assets/pilot/keyframes/k04_ida_desk_mcu.png`
- Comp:
  - `push(1.00→1.025, focus=eyes)`.
  - The light is steady (the screen is frozen) with a very faint 1 % noise.
  - Optional: a tiny mirrored and blurred crop of J07's frozen last frame in each eye highlight, at 20 %.
  - `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (k07):**
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
> SHOT: a close-up of Ida, frontal, from a slightly low angle. Her face is lit hard from below and in front by the
> cold cyan glow of a screen just beneath the camera. She stares past the lens at the screen, jaw set, brows slightly
> lowered: contempt and exhaustion. Her lips are just parted, as if about to speak. Tiny cyan reflections show in her
> eyes. Background: pure darkness with a few faint cyan bokeh shapes. Composition: face centered slightly left, eyes on
> the upper third, the amber scarf at the bottom edge.

**Refs:** `assets/pilot/lookdev/ld4_ida.png`, `assets/pilot/keyframes/k04_ida_desk_mcu.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- The hall clock returns at 0.0 (abs 71.0), and the DRONE returns at −3 dB.
- **IDA** (`Samantha`, 160, IDA hall chain): **"No, you're not."** at shot +1.0 (abs 72.0), quiet and flat.
- Nothing else.

**Motion prompt (v2):** Flat 2D cel-painted style. Close-up of Ida lit from below by cold cyan screen light, staring
at the screen with her jaw set. She says quietly, with contempt and exhaustion: "No, you're not." Almost no head
movement, one slow blink after the line. Static camera. Room hum, clock ticking. No music.

**Takes:** —
