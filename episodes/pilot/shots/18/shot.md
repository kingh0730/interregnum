# Shot 18 — NANA ANSWERS

**Duration:** 5 s (1:34–1:39; abs 94.0–99.0)  **Tool:** Codex keyframe + comp  **Camera:** CU, Nana facing
screen-right (the reverse of Ida); push-in 1.00→1.03

**Action:** Nana, the receiver at her ear, her face split between the TV's blue and the lamp's gold. The whole film
meets on her face. "I always wait up. He's on soon." Is she waiting for Ida or for him? Both. **Start pose (v2):**
receiver at her ear, eyes on the (off-frame) TV, mouth closed, about to speak.

**Build:**
- Codex **k11**:
  `tools/imagegen/gen.sh assets/pilot/keyframes/k11_nana_phone_cu.png "<prompt>" assets/pilot/lookdev/ld5_nana.png assets/pilot/lookdev/ld3_apartment.png`
- **Acceptance:** this sets Nana's face for shots 20, 33, 39 and 41. Check it against ld5_nana and retake if it
  drifts.
- Comp:
  - `push(1.00→1.03, focus=her eyes)`.
  - `flicker(mask=cyan_lit, driver=J15 luma, 4 %)` on the TV side.
  - `rainshadow` at 3 % across her face and the wall behind her (droplet shadows sliding down).
  - `letterbox(2.39)`, `grade(HOME)`.

**Keyframe prompt (k11):**
> STYLE: a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean, confident
> dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow only around
> light sources; subtle paper grain; realistic human proportions and faces (not chibi, no oversized eyes); simplified
> graphic backgrounds with bold silhouettes and large areas of dark negative space. PALETTE: deep ink-navy and
> blue-black darkness; cold pale-cyan light comes only from screens; warm amber light comes only from household lamps
> and warm objects; signal red only where described; no other saturated colors. LIGHT: one strong motivated light
> source, deep shadows, light haze. FRAME: wide 16:9 landscape; keep every important element inside the central
> horizontal band, because the top and bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters, numbers,
> logos or watermarks anywhere; every screen is a blank, evenly glowing panel.
> CHARACTER: NANA: a small woman of 82 with silver-white hair in a low bun held by a dark wooden hairpin, a soft round
> face with deep smile lines, bright dark eyes behind thin round gold wire-rimmed glasses, warm light-brown skin,
> small pearl stud earrings; she wears a dark bottle-green knitted cardigan over a cream blouse with a tiny faded
> floral print. Match the attached character sheet exactly.
> SHOT: a close-up of Nana seated in her armchair (in the apartment of the attached style frame), holding an old
> cream-colored telephone handset to her ear on the side facing the camera. Her face is turned three-quarters toward
> screen-right, where the television is (off-frame). Her face is lit half by cold cyan television light from the right
> and half by warm amber lamplight from the left, the two colors meeting softly on her nose and cheeks. Her eyes are
> attentive behind her gold-rimmed glasses; her mouth is closed, about to speak. Behind her, the pleated lamp shade
> glows softly at the left. Composition: Nana right of center, looking right, eyes on the upper third.

**Refs:** `assets/pilot/lookdev/ld5_nana.png`, `assets/pilot/lookdev/ld3_apartment.png`.
**Layers:** none.
**JS spec:** none. The flicker driver is J15's luminance curve.

**Sound:**
- **NANA** (`Moira`, 150, NANA chain): **"I always wait up. He's on soon."** at shot +0.4 (abs 94.4).
- Room tone; rain on glass; Nana's clock; the TV's faint stand-by tone; phone-line hiss; warm PAD.

**Motion prompt (v2):** Flat 2D cel-painted style. Close-up: an elderly woman holds an old telephone handset to her
ear, her face half in cold blue TV light and half in warm lamplight. She answers gently, eyes on the television: "I
always wait up. He's on soon." A small nod. Static camera. Rain on the window, a clock ticking. No music.

**Takes:** —
