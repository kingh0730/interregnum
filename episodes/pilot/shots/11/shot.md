# Shot 11 — THE ORDER

**Duration:** 6 s (0:57–1:03; abs 57.0–63.0)  **Tool:** Codex keyframe + JS text layer + comp  **Camera:** overhead,
looking straight down; slow push-in 1.00→1.05 on the paper

**Action:** Ida's hands unroll a narrow slip. We read it line by line as she does: NIGHT 212 / NO AGREEMENT. / NO
TEXT TONIGHT. / LET HIM SPEAK. / THE OPERATOR ANSWERS FOR CONTENT. It carries a red seal with the Lamp. The rulers
cannot agree on the next lie, so they hand it to the machine and the blame to her. **Start pose (v2):** hands holding
the slip open and flat.

**Build:**
- Codex **k06** (the paper is blank):
  `tools/imagegen/gen.sh assets/pilot/keyframes/k06_order_paper.png "<prompt>" assets/pilot/lookdev/ld4_ida.png assets/pilot/lookdev/ld1_hall.png`
- JS **J06 `order`** renders a transparent text layer and a seal (below).
- Comp:
  - Find the paper's 4 corners: the largest cream region, `approxPolyDP`, or click them by hand once.
  - `insert(J06, target=corners)` with a **multiply** blend, so the ink sits in the paper grain, plus 0.6 px blur.
  - The lines are revealed as she reads, each fading up over 0.15 s: line 1 at 0.4, line 2 at 1.2, line 3 at 2.0,
    line 4 at 2.8, line 5 at 3.8. The seal is present from 0.0.
  - `push(1.00→1.05, focus=paper center)`.
  - `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (k06):**
> STYLE: a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean, confident
> dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow only around
> light sources; subtle paper grain; realistic human proportions and faces (not chibi, no oversized eyes); simplified
> graphic backgrounds with bold silhouettes and large areas of dark negative space. PALETTE: deep ink-navy and
> blue-black darkness; cold pale-cyan light comes only from screens; warm amber light comes only from household lamps
> and warm objects; signal red only where described; no other saturated colors. LIGHT: one strong motivated light
> source, deep shadows, light haze. FRAME: wide 16:9 landscape; keep every important element inside the central
> horizontal band, because the top and bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters, numbers,
> logos or watermarks anywhere; every screen is a blank, evenly glowing panel.
> SHOT: an overhead view looking straight down at a dark, scratched metal desk. A young woman's two hands (slim
> fingers, the cuffs of a charcoal-grey ribbed sweater, as on the attached character sheet) hold open a narrow strip
> of cream paper. The paper is flat and faces the camera squarely, its ends curling slightly, and it is completely
> blank with no marks at all, only a faint paper texture. Beside it lies an opened matte-black message capsule with
> brass end caps and a broken red wax band. Cold cyan monitor light falls from the top of the frame; deep shadows.
> Composition: the paper strip centered horizontally, filling the middle 60% of the frame width.

**Refs:** `assets/pilot/lookdev/ld4_ida.png`, `assets/pilot/lookdev/ld1_hall.png`.
**Layers:** none.

**JS spec (J06, transparent PNG sized to the paper's aspect, e.g. 1600×460 px):**
- Text: Courier New Bold 56 px, ink `#1B1E24`, left-aligned at x 80, 1.25 line height. The lines:
  1. `NIGHT 212`
  2. `NO AGREEMENT.`
  3. `NO TEXT TONIGHT.`
  4. `LET HIM SPEAK.`
  5. `THE OPERATOR ANSWERS FOR CONTENT.` (38 px, the small print)
- Render each line on its own layer so comp can reveal them one at a time.
- Typewriter texture: ±1 px baseline jitter per glyph, ink density 85–100 % per glyph, a slight 0.4 px bleed.
- **Seal** (its own layer): at the right end, a 160 px circle in `#C2362A`.
  - An inner ring, with the Lamp's flame and base line in negative space.
  - Rough edge (noise displacement 3 px), rotated −8°, at 90 % opacity, multiply blend.

**Sound:**
- Paper crinkle 0.0–0.6 (abs 57.0–57.6).
- Hall tone, clock and DRONE.
- A dark PAD swell on D2 from +2.0 (abs 59.0).
- A soft PULSE at +3.8 (abs 60.8) as the last line appears.
- No dialogue.

**Motion prompt (v2):** Flat 2D cel-painted style. Overhead close-up of a woman's hands holding open a narrow strip
of typed paper under cold cyan light. The paper trembles slightly as she reads, and her thumb tightens on the edge.
Static overhead camera, slow push-in. Paper rustle, room hum. No music. (In v2, re-apply the typed text in comp over
the generated clip.)

**Takes:** —
