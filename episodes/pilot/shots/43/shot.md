# Shot 43 — THE EMPTY HALL

**Duration:** 6 s (3:37–3:43; abs 217.0–223.0)  **Tool:** Codex edit of k03 + cutout layer (reuse) + comp + wall
insert  **Camera:** the exact framing of shot 05, played in reverse: **pull 1.07→1.00**, with parallax

**Action:** The same wide as when we met her, but the desk is empty and the chair pushed back. She went home. On the
monitor wall there is no face, only the Lamp, dim. Far below, the red phone rings for no one. **Start pose (v2):** the
empty hall; the camera pulls back up the aisle.

**Build:**
- Codex **k26**, an **edit** of k03 (attach only k03):
  `tools/imagegen/gen.sh assets/pilot/keyframes/k26_hall_empty.png "<prompt>" assets/pilot/keyframes/k03_hall_wide.png`
- **Acceptance:** the architecture must match k03. Difference-check it; if the edit shifted the image, SIFT-align it
  to k03.
- Comp:
  - `insert(J15 stand-by, target=auto)` into the wall, at **50 % brightness** and **not** breathing (the broadcast is
    over). Then `bezels(12×8)`, haze and a softer bloom.
  - The lit desk's two small monitors are dim.
  - `pull(1.07→1.00, focus=(0.50, 0.74))`: the exact inverse of shot 05's move. Use `parallax(k03_fg_desks=1.0,
    plate=0.55)` with the same layer, aligned to k26.
  - `dust(120)`, slower (−30 %).
  - `letterbox(2.39)`, `grade(HALL)` at −15 % exposure.

**Keyframe prompt (k26, edit of k03):**
> STYLE (keep exactly): a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean,
> confident dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow only
> around light sources; subtle paper grain; simplified graphic backgrounds with bold silhouettes and large areas of
> dark negative space. PALETTE: deep ink-navy and blue-black darkness; cold pale-cyan light only from screens; a small
> amber accent only where described; no other saturated colors. Wide 16:9; important content in the central
> horizontal band. No text, letters, numbers, logos or watermarks anywhere; every screen is a blank glowing panel.
> EDIT the attached image: remove the lone woman completely. Her chair is now pushed back from the lit desk, turned
> slightly, and empty; the small amber thermos is gone from the desk. The giant monitor wall glows a dimmer, deeper
> blue, still blank. The small signal-lamp box above the wall stays unlit. Keep everything else exactly identical,
> pixel-aligned: the hall, the perspective, the dust-sheeted desks, the pipes, the columns, the haze, the framing,
> the colors and the line style.

**Refs:** `assets/pilot/keyframes/k03_hall_wide.png` (the image being edited).
**Layers:** reuses `assets/pilot/layers/k03_fg_desks.png` (no new cutout).
**JS spec:** **J15 stand-by**, static (breathing off), at 50 % brightness.

**Sound:**
- **The red phone, far away** in the empty hall: HALL REVERB (6 s), −20 dB, ringing at abs 218.0 and 221.0. After
  223 it is gone.
- Rain on the high roof; the hall tone at −6 dB (the power is off).
- No clock.
- Score: PAD **B♭**, fading −30→−40 dB (1M6).

**Motion prompt (v2):** Flat 2D cel-painted style. The vast dark concrete hall, now empty: the lone desk's chair is
pushed back and nobody is there, and the giant monitor wall shows only a dim blue glow. Slow pull-back up the central
aisle. Dust drifts in the cold light. A telephone keeps ringing somewhere far below; rain on the high roof. No music.
(Re-insert the emblem on the wall in comp.)

**Takes:** —
