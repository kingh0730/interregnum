# Shot 33 — NANA LISTENS

**Duration:** 6 s (2:54–3:00; abs 174.0–180.0)  **Tool:** Codex keyframe + comp  **Camera:** CU, near-frontal (the
camera sits beside the TV); push-in 1.00→1.04, very slow

**Action:** Nana holds her tea under her chin, the TV's light on her face. From the small speaker: "Eat something
warm before you sleep." The line she has waited up for all night, and her own words. Her eyes glisten and the corners
of her mouth lift, just barely. Three notes of her theme begin, and then the dead air cuts them off. **Start pose
(v2):** holding the steaming cup near her chin, mouth closed, the beginning of a smile.

**Build:**
- Codex **k19**:
  `tools/imagegen/gen.sh assets/pilot/keyframes/k19_nana_listens.png "<prompt>" assets/pilot/lookdev/ld5_nana.png assets/pilot/lookdev/ld3_apartment.png assets/pilot/keyframes/k11_nana_phone_cu.png`
- Comp:
  - `push(1.00→1.04, focus=her eyes)`.
  - `flicker(mask=cyan_lit, driver=k02 broadcast luma + noise(0.4 Hz) 3 %)`.
  - `steam(the cup)`: slow, warm-lit.
  - `rainshadow` at 3 %.
  - `letterbox(2.39)`, `grade(HOME)`.

**Keyframe prompt (k19):**
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
> SHOT: a close-up of Nana seated in her armchair (in the apartment of the attached style frame), holding a small
> steaming white teacup in both hands near her chin. She faces almost straight toward the camera, which is placed just
> beside her television. Her face is lit by cold cyan television light, with the warm amber lamp glowing behind her
> shoulder. Her eyes glisten behind her gold-rimmed glasses; her mouth is closed, with the very beginning of a tender
> smile. Composition: face centered, eyes on the upper third, steam rising from the cup.

**Refs:** `assets/pilot/lookdev/ld5_nana.png`, `assets/pilot/lookdev/ld3_apartment.png`, `assets/pilot/keyframes/k11_nana_phone_cu.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- **FATHER** (`Daniel`, 135, TV chain: a small speaker in the room): **"Eat something warm before you sleep."** at
  shot +0.8 (abs 174.8).
- Room tone; rain on glass; Nana's clock; TV hum.
- Score: a warm PAD F(add9) at −38 dB from 176.0. Theme **A4 177.6, F4 178.4, G4 179.2**, then cut at 180.0 (the dead
  air). No phone here.

**Motion prompt (v2):** Flat 2D cel-painted style. Close-up: an elderly woman holds a steaming teacup near her chin,
facing the television, her face lit by its cold blue light, with warm lamplight behind her. The TV voice says: "Eat
something warm before you sleep." Her eyes glisten, and the corners of her mouth lift into a small, knowing smile.
Static camera. Rain on the window, a TV speaker. No music.

**Takes:** —
