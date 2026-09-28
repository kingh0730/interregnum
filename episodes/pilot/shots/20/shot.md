# Shot 20 — "FOR THE ENDING."

**Duration:** 6 s (1:43–1:49; abs 103.0–109.0)  **Tool:** Codex keyframe + comp  **Camera:** a closer CU of Nana
facing screen-right; push-in 1.00→1.035

**Action:** Nana smiles privately, eyes on the screen: "For the ending." A beat. Then, tender and firm, what she says
every night: "Eat something warm, love." The audience hears the Father's line from the cold open in her mouth, and
the connection clicks. On second viewing, "For the ending" means *I watch for your line*. It is also what makes Ida
decide: the Father needs an ending. **Start pose (v2):** handset at her ear, a small smile, lips closed, about to
speak.

**Build:**
- Codex **k13**:
  `tools/imagegen/gen.sh assets/pilot/keyframes/k13_nana_smile_cu.png "<prompt>" assets/pilot/lookdev/ld5_nana.png assets/pilot/keyframes/k11_nana_phone_cu.png`
- Comp:
  - `push(1.00→1.035, focus=her eyes)`.
  - `flicker(mask=cyan_lit, driver=J15 luma, 4 %)`.
  - `rainshadow` at 3 %.
  - `letterbox(2.39)`, `grade(HOME)`.

**Keyframe prompt (k13):**
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
> floral print. She is exactly the same woman as in the attached images.
> SHOT: a closer close-up of Nana with the cream telephone handset at her ear on the side facing the camera, her
> face three-quarters toward screen-right and her eyes on the unseen television. A small private smile sits at the
> corner of her mouth: tender, knowing, a little amused. Her lips are closed, about to speak. Warm amber lamplight
> falls on the left side of her face and cold cyan television light on the right. Composition: her face fills the
> right half of the frame, eyes on the upper third.

**Refs:** `assets/pilot/lookdev/ld5_nana.png`, `assets/pilot/keyframes/k11_nana_phone_cu.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- **NANA** (`Moira`, 150, NANA chain): **"For the ending."** at shot +0.5 (abs 103.5).
- **PLUCK F4** (theme note 2) at +1.9 (abs 104.9), in the pause.
- **NANA** (`Moira`, 145): **"Eat something warm, love."** at +3.2 (abs 106.2).
- Room tone; rain; Nana's clock; phone-line hiss; warm PAD (Dm).

**Motion prompt (v2):** Flat 2D cel-painted style. Close-up: the elderly woman, handset at her ear and eyes on the
blue television, smiles privately and says: "For the ending." After a pause, tender and firm: "Eat something warm,
love." Static camera, very slow push-in. Rain, a clock ticking. No music.

**Takes:** —
