# Shot 10 — CAPSULE

**Duration:** 3 s (0:54–0:57; abs 54.0–57.0)  **Tool:** Codex keyframe + cutout layer + comp  **Camera:** ECU at desk
height, static, micro push 1.00→1.02

**Action:** A rumble travels through the pipes. A black capsule with a red seal shoots out of the brass pipe and
slams into the cradle. The Committee still speaks in paper and brass: the old machinery of power sits beside the new
one. **Start pose (v2):** the empty cradle; the capsule arrives from the pipe.

**Build:**
- Codex **k05** (the empty cradle):
  `tools/imagegen/gen.sh assets/pilot/keyframes/k05_tube_cradle.png "<prompt>" assets/pilot/lookdev/ld1_hall.png`
- Codex layer **k05_capsule** (`ALPHA=1`, attach k05), see **Layers**. Trim it to its alpha bounding box.
- Comp:
  - 0.0–1.2 s: static plate with `push(1.00→1.02)` across the whole shot.
  - 1.20 s: the capsule appears at the pipe mouth (60 % scale, moving along the pipe's axis) with 5-subframe motion
    blur.
  - 1.20–1.35 s: it drops into the cradle (ease-in, gravity), scaling to 100 %.
  - **1.35 s impact:** `shake(6 px, 0.3 s)`, `puff(cradle rim, 30 particles)` of pale dust, and a small brass glint
    bloom on the pipe at 1.40.
  - 1.35–3.0 s: the capsule rocks once (±1.5° over 0.3 s), then settles.
  - `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (k05):**
> STYLE: a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean, confident
> dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow only around
> light sources; subtle paper grain; realistic human proportions and faces (not chibi, no oversized eyes); simplified
> graphic backgrounds with bold silhouettes and large areas of dark negative space. PALETTE: deep ink-navy and
> blue-black darkness; cold pale-cyan light comes only from screens; warm amber light comes only from household lamps
> and warm objects; signal red only where described; no other saturated colors. LIGHT: one strong motivated light
> source, deep shadows, light haze. FRAME: wide 16:9 landscape; keep every important element inside the central
> horizontal band, because the top and bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters, numbers,
> logos or watermarks anywhere; every screen is a blank, evenly glowing panel.
> SHOT: an extreme close-up at desk height, in the same world and style as the attached location frame. A heavy old
> brass pneumatic-tube receiver is fixed to the edge of a dark, scratched metal desk. A curved brass pipe comes down
> from the top of the frame and ends in an open, empty, cup-shaped brass cradle, with nothing in it yet. The brass
> reflects cold cyan light from a monitor out of frame at the left. Behind: darkness with faint haze and the vague
> depth of a vast hall. Composition: the pipe mouth at upper center and the empty cradle at lower center, with clear
> space between them for an object to drop in.

**Refs:** `assets/pilot/lookdev/ld1_hall.png`.

**Layers:** `assets/pilot/layers/k05_capsule.png` (`ALPHA=1`, attach k05). Prompt:
> STYLE: flat 2D cel-painted animation look with clean dark-navy ink contour lines, flat color shapes with one
> hard-edged shadow tone and subtle paper grain, matching the attached image. A single matte-black cylindrical
> pneumatic message capsule, about the length of a forearm, with rounded brass end caps and a band of red wax seal
> around its middle. It lies horizontally, seen from the same slightly-above angle as the attached image and lit by the
> same cold cyan light from the left. On a genuinely transparent background, with nothing else in the image. No text
> or markings.

**JS spec:** none.

**Sound:**
- 0.0–1.2 s: rumble travelling through the pipes (brown noise LPF 300 Hz, filter rising, panned L→C).
- **1.35 (abs 55.35): WHUMP and metallic clank.**
- 1.45–2.5: a hiss of released air.
- Hall clock (55, 56); DRONE.

**Motion prompt (v2):** Flat 2D cel-painted style. Extreme close-up of an old brass pneumatic-tube cradle on a dark
metal desk. A black message capsule with a red seal band shoots out of the curved brass pipe and drops hard into the
cradle, rocks once and settles, with a small puff of dust. Static camera. Pneumatic rumble, a heavy metallic clank, a
hiss of air. No music.

**Takes:** —
