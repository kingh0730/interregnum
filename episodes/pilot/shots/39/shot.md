# Shot 39 — "I KNOW, LOVE."

**Duration:** 4 s (3:18–3:22; abs 198.0–202.0)  **Tool:** Codex keyframe + comp  **Camera:** CU, Nana facing
screen-right; push-in 1.00→1.03

**Action:** Nana's television is dark now, and only the lamp lights her: the cyan has left her face for good. She is
calm and not surprised. "I know, love." The line lands like a key turning. **Start pose (v2):** handset at her ear,
lamp-lit, the corners of her mouth lifted, lips closed.

**Build:**
- Codex **k24**:
  `tools/imagegen/gen.sh assets/pilot/keyframes/k24_nana_amber.png "<prompt>" assets/pilot/lookdev/ld5_nana.png assets/pilot/lookdev/ld3_apartment.png assets/pilot/keyframes/k11_nana_phone_cu.png`
- Comp:
  - `push(1.00→1.03, focus=eyes)`.
  - The lamp is steady, with a 1 % warm flicker (filament).
  - `rainshadow` at 3 %. There is no TV flicker (the set is off).
  - `letterbox(2.39)`, `grade(HOME)` biased warm, with no cyan anywhere on her.

**Keyframe prompt (k24):**
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
> SHOT: a close-up of Nana in her armchair (in the apartment of the attached style frame), with the old cream-colored
> telephone handset at her ear on the side facing the camera and her face three-quarters toward screen-right. The
> television behind her is switched off, its screen dark grey. Her face is lit only by the warm amber table lamp. She
> is calm and tender, her eyes soft behind her glasses, the corners of her mouth lifted, lips closed, about to speak.
> Background: warm dark-brown shadows, the dark television and the rain-streaked window. Composition: face right of
> center, eyes on the upper third, with room above her head for a tighter reframe.

**Refs:** `assets/pilot/lookdev/ld5_nana.png`, `assets/pilot/lookdev/ld3_apartment.png`, `assets/pilot/keyframes/k11_nana_phone_cu.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- **NANA** (`Moira`, 145, NANA chain): **"I know, love."** at shot +0.6 (abs 198.6).
- Room tone; rain on glass. **Nana's clock is still ticking** (her time goes on). There is no TV hum (the set is off).
- Phone-line hiss.
- Score 1M6: the warm PAD (F) enters at +1.5 (abs 199.5), −30 dB.

**Motion prompt (v2):** Flat 2D cel-painted style. Close-up: an elderly woman lit only by a warm lamp holds an old
telephone handset to her ear; the television behind her is dark. Calm and tender, she says: "I know, love." A small
smile. Static camera. Rain on the window, a clock ticking. No music.

**Takes:** —
