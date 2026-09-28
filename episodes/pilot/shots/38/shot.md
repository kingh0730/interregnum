# Shot 38 — "NANA—"

**Duration:** 3 s (3:15–3:18; abs 195.0–198.0)  **Tool:** Codex keyframe + comp  **Camera:** CU, Ida facing
screen-left; push-in 1.00→1.02

**Action:** She answers the small phone. Behind her, out of focus, the red one keeps ringing. She starts to explain,
confess or apologize ("Nana—"), and doesn't get further. Her face has changed: the cyan is dying and an amber glow
from the phone warms her cheek. **Start pose (v2):** the phone just raised to her ear, lips parted.

**Build:**
- Codex **k23**:
  `tools/imagegen/gen.sh assets/pilot/keyframes/k23_ida_answers.png "<prompt>" assets/pilot/lookdev/ld4_ida.png assets/pilot/keyframes/k12_ida_phone_cu.png assets/pilot/keyframes/k22_red_phone.png`
- Comp:
  - `push(1.00→1.02, focus=eyes)`.
  - `jitter(mask=the red phone in the soft foreground, 1 px, 25 Hz)` during its ring (abs 197.0–198.0, shot +2.0–3.0).
  - `flicker(mask=amber_lit, driver=noise(0.3 Hz), 2 %)`: the phone's screen light.
  - `letterbox(2.39)`, `grade(HALL)` with the amber preserved.

**Keyframe prompt (k23):**
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
> SHOT: a close-up of Ida at her desk, holding a small slim dark phone to her ear on the side facing the camera, her
> face three-quarters toward screen-left. She looks stunned and hollow, her eyes glistening, lips parted, about to
> speak. A warm amber glow from the phone's screen lights her cheek; the cold cyan monitor light has dimmed to a faint
> rim on her hair. In the soft-focus foreground at the lower left is the corner of a heavy signal-red desk telephone
> (as in the attached image of the red phone). Composition: face left of center, eyes on the upper third, the amber
> scarf at the bottom edge.

**Refs:** `assets/pilot/lookdev/ld4_ida.png`, `assets/pilot/keyframes/k12_ida_phone_cu.png`, `assets/pilot/keyframes/k22_red_phone.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- **IDA** (`Samantha`, 165, IDA hall chain): **"Nana—"** at shot +0.7 (abs 195.7). Render "Nana, I" and keep only
  0.5 s, with a 30 ms fade: she is cut off.
- The red phone rings at abs 197.0 (close-ish, −6 dB); phone-line hiss.
- No music yet.

**Motion prompt (v2):** Flat 2D cel-painted style. Close-up: Ida raises a small phone to her ear, stunned, eyes
glistening. In the blurred foreground a red desk telephone keeps ringing. She starts to say "Nana—" and stops. Static
camera. The red telephone bell in a silent hall. No music.

**Takes:** —
