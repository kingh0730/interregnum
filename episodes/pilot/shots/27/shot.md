# Shot 27 — THE KEY

**Duration:** 4 s (2:25–2:29; abs 145.0–149.0)  **Tool:** Codex keyframe + comp  **Camera:** ECU; push-in 1.00→1.06
on the fingertip, accelerating (easeInQuad)

**Action:** Her index finger hovers above a large red-lit key. "Ten seconds." The phone rings, the pulse thuds, the
hum rises. The finger stays up. We cut to black before it falls: the press happens in the cut. **Start pose (v2):**
the finger above the key, not touching. The v2 action is the press.

**Build:**
- Codex **k16**:
  `tools/imagegen/gen.sh assets/pilot/keyframes/k16_commit_key.png "<prompt>" assets/pilot/lookdev/ld1_hall.png assets/pilot/lookdev/ld4_ida.png`
- Comp:
  - `push(1.00→1.06, focus=fingertip, easeInQuad)`.
  - The key's red glow pulses on each whole second (+15 % luma on the tick, decaying over 0.4 s).
  - Finger tremor: 0.6 px at 9 Hz, applied to a mask of the finger (skin-tone region).
  - `letterbox(2.39)`, `grade(HALL)`. **Hard cut at 4.0 to shot 28**, with no fade.

**Keyframe prompt (k16):**
> STYLE: a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean, confident
> dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow only around
> light sources; subtle paper grain; realistic human proportions and faces (not chibi, no oversized eyes); simplified
> graphic backgrounds with bold silhouettes and large areas of dark negative space. PALETTE: deep ink-navy and
> blue-black darkness; cold pale-cyan light comes only from screens; warm amber light comes only from household lamps
> and warm objects; signal red only where described; no other saturated colors. LIGHT: one strong motivated light
> source, deep shadows, light haze. FRAME: wide 16:9 landscape; keep every important element inside the central
> horizontal band, because the top and bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters, numbers,
> logos or watermarks anywhere; every screen is a blank, evenly glowing panel.
> SHOT: an extreme close-up of an old broadcast console in the dark hall of the attached style frame. A large square
> backlit key glowing dim signal red is set into a scratched dark metal panel, with no markings on it. A young
> woman's index finger (the cuff of a charcoal-grey ribbed sweater visible, as on the attached character sheet)
> hovers just above the key, not yet touching, its tip lit red from below. A thin cyan reflection from a screen
> off-frame shows on the fingernail. Everything else falls into darkness. Composition: the key slightly below center,
> the finger entering from the upper right.

**Refs:** `assets/pilot/lookdev/ld1_hall.png`, `assets/pilot/lookdev/ld4_ida.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- **PA** (`Karen`, 165, PA chain): **"Ten seconds."** at shot +0.3 (abs 145.3).
- The red phone ring at abs 146.0; PULSE (loudest now); the hall clock.
- RISER peaking at 149.0.
- **At 4.0 (abs 149.0): HARD CUT, and every stem goes silent** (0.3 s).

**Motion prompt (v2):** Flat 2D cel-painted style. Extreme close-up of a woman's index finger hovering over a large
red-lit console key. The finger trembles slightly, then presses down firmly. Static camera, slight push-in. A
telephone ringing, a clock ticking, a rising electrical hum. No music.

**Takes:** —
