# Shot 42 — COME HOME

**Duration:** 7 s (3:30–3:37; abs 210.0–217.0)  **Tool:** Codex keyframe + comp  **Camera:** CU, Ida facing
screen-left; slow push-in 1.00→1.04 on her eyes

**Action:** Ida's face breaks: her eyes close, a tear falls, and a laugh comes through the crying. Two hundred and
twelve nights of carrying it alone, and she never had to. From the phone, Nana: "Come home. The soup's still warm."
The cyan on her hair fades as the monitors go dark, until only the phone's amber is left on her face. Nana's theme
plays whole for the first time and resolves just after "warm". **Start pose (v2):** eyes closed, the tear on her
cheek, the laugh beginning.

**Build:**
- Codex **k25**:
  `tools/imagegen/gen.sh assets/pilot/keyframes/k25_ida_tears.png "<prompt>" assets/pilot/lookdev/ld4_ida.png assets/pilot/keyframes/k23_ida_answers.png`
- Comp:
  - `push(1.00→1.04, focus=eyes)`.
  - **Light change:** the cyan rim fades by 60 % over 1.0–6.0 s (use the cyan-lit mask) while the amber holds. Shift
    the grade from HALL to warm across the shot.
  - **Tear glint (optional, subtle):** a small specular highlight (6 px, `#FFFFFF` at 60 %) slides 50 px down the
    tear track over 1.5–4.5 s (easeIn). Check the stills: if it reads as a sticker, drop it.
  - `letterbox(2.39)`.

**Keyframe prompt (k25):**
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
> SHOT: a close-up of Ida with the small dark phone still at her ear on the side facing the camera, her face
> three-quarters toward screen-left. Her eyes are closed and one tear runs down her cheek; the beginning of a laugh
> breaks through the crying, a small open smile. The warm amber glow of the phone lights her cheek, and the cold cyan
> of the hall is only a faint rim on her hair. Background: dark. Composition: face left of center, eyes on the upper
> third, the amber scarf at the bottom edge.

**Refs:** `assets/pilot/lookdev/ld4_ida.png`, `assets/pilot/keyframes/k23_ida_answers.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- **NANA (V.O., on the phone)** (`Moira`, 145, PHONE chain): **"Come home. The soup's still warm."** at shot +1.5
  (abs 211.5).
- Ida's breath and laugh-sob (fx): breaths at abs 210.6, 211.2, 214.8 and 215.6, and a shaky laugh at 215.0.
- **Nana's theme resolved** (1M6): A4 210.2, F4 211.0, G4 211.8, E4 212.6, F4 213.4, **D4 214.4**, then a high D5
  echo at 215.4. PAD **F → C/E → Dm**.
- The red phone at abs 212.0 and 215.0, far off (−18 dB), fading from attention.
- **No ducking of the D4 resolution.**

**Motion prompt (v2):** Flat 2D cel-painted style. Close-up: Ida, a small phone at her ear, closes her eyes; a tear
runs down her cheek and a laugh breaks through the crying. From the phone, a warm old voice: "Come home. The soup's
still warm." Static camera, slow push-in. A quiet hall, a faint telephone. No music. (Supply the rendered Nana voice
track as the audio, since she is off-screen.)

**Takes:** —
