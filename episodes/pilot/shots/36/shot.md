# Shot 36 — THE RED PHONE

**Duration:** 4 s (3:08–3:12; abs 188.0–192.0)  **Tool:** Codex keyframe + comp  **Camera:** CU on the desk; push-in
1.00→1.03

**Action:** In the new silence, the Committee's red phone rattles in its cradle, loud. Ida's hand lies flat beside
it and does not move. She doesn't answer. It's the old power calling into a void, and her choice made visible without
a gesture. **Start pose (v2):** the phone ringing and the hand still. The action is the handset rattling; the hand
stays put.

**Build:**
- Codex **k22**:
  `tools/imagegen/gen.sh assets/pilot/keyframes/k22_red_phone.png "<prompt>" assets/pilot/lookdev/ld1_hall.png assets/pilot/lookdev/ld4_ida.png`
- Comp:
  - `jitter(mask=red handset, found by hue threshold on the signal red, 1.5 px, 25 Hz)` during the rings: 0.0–1.2 s
    and 3.0–4.0 s.
  - A 2 % brightness flicker on the handset's highlights in sync with the jitter.
  - The monitor's cyan light dims slightly across the shot (−10 %).
  - `push(1.00→1.03)`, `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (k22):**
> STYLE: a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean, confident
> dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow only around
> light sources; subtle paper grain; realistic human proportions and faces (not chibi, no oversized eyes); simplified
> graphic backgrounds with bold silhouettes and large areas of dark negative space. PALETTE: deep ink-navy and
> blue-black darkness; cold pale-cyan light comes only from screens; warm amber light comes only from household lamps
> and warm objects; signal red only where described; no other saturated colors. LIGHT: one strong motivated light
> source, deep shadows, light haze. FRAME: wide 16:9 landscape; keep every important element inside the central
> horizontal band, because the top and bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters, numbers,
> logos or watermarks anywhere; every screen is a blank, evenly glowing panel.
> SHOT: a close-up on a dark, scratched metal desk in the hall of the attached style frame. A heavy old desk telephone
> in signal red, with its handset resting in the cradle and a thick coiled cord, has no markings. Beside it, a young
> woman's hand (the cuff of a charcoal-grey ribbed sweater, as on the attached character sheet) rests flat and still
> on the desk, not reaching for it. The cold cyan glow of a monitor from the upper left is dim. Darkness beyond.
> Composition: the red phone left of center, the hand at the right, with clear dark space between them.

**Refs:** `assets/pilot/lookdev/ld1_hall.png`, `assets/pilot/lookdev/ld4_ida.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- **The red phone, loud and dry, close**: rings at 0.0–1.2 and 3.0–4.2 (abs 188.0, 191.0).
- Nothing else: no hum, no clock.

**Motion prompt (v2):** Flat 2D cel-painted style. Close-up of a heavy red desk telephone ringing, the handset
rattling in its cradle. Beside it, a woman's hand rests flat on the desk and does not move. Static camera. The loud
bell of the telephone in a silent hall. No music.

**Takes:** —
