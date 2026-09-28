# Shot 23 — THE FACE

**Duration:** 6 s (1:59–2:05; abs 119.0–125.0)  **Tool:** Codex keyframe + cutout layer + comp + wall insert
**Camera:** low angle from behind Ida. Push-in 1.00→1.10 toward the giant face's eyes, **accelerating** (easeInQuad),
with parallax.

**Action:** Ida has stood up. She is a small dark silhouette beneath the colossal face, which is now clean and in
full color, wearing no wireframe: ready for air. Above the wall, the red lamp glows standby. We move past her and into
his eyes. This is the scale of what she's about to do. **Start pose (v2):** Ida standing at the desk with her back to
camera, head tilted up.

**Build:**
- Codex **k14** (the wall is blank):
  `tools/imagegen/gen.sh assets/pilot/keyframes/k14_hall_low.png "<prompt>" assets/pilot/lookdev/ld1_hall.png assets/pilot/lookdev/ld4_ida.png assets/pilot/keyframes/k03_hall_wide.png`
- Codex layer **k14_fg_ida** (`ALPHA=1`, attach k14).
- Comp:
  - `insert(src=k02 clean, full color, no mesh, target=corners)`. The wall is seen in steep upward perspective, so
    click its 4 corners once. Then `bezels(12×8, 6 px)`, tile jitter ±4 %, a 12 % haze mix, and bloom.
  - The red lamp box glows at a slow standby pulse (0.5 Hz, 60–90 %).
  - `push(1.00→1.10, focus=the inserted face's eyes, easeInQuad)`, with `parallax(k14_fg_ida=1.0, plate=0.5)`. Ida
    slides down and out of the lower frame as we push.
  - `dust(80)` in the cold light.
  - `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (k14):**
> STYLE: a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean, confident
> dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow only around
> light sources; subtle paper grain; realistic human proportions and faces (not chibi, no oversized eyes); simplified
> graphic backgrounds with bold silhouettes and large areas of dark negative space. PALETTE: deep ink-navy and
> blue-black darkness; cold pale-cyan light comes only from screens; warm amber light comes only from household lamps
> and warm objects; signal red only where described; no other saturated colors. LIGHT: one strong motivated light
> source, deep shadows, light haze. FRAME: wide 16:9 landscape; keep every important element inside the central
> horizontal band, because the top and bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters, numbers,
> logos or watermarks anywhere; every screen is a blank, evenly glowing panel.
> LOCATION: the same vast dark concrete broadcast hall as in the attached images, with shrouded desks, brass pipes on
> the columns and haze.
> CHARACTER: a lone young woman seen from behind as a dark silhouette: a short blunt black bob, a charcoal sweater,
> and the edge of a mustard-amber scarf catching the light (the woman on the attached character sheet).
> SHOT: a low angle from just behind and below her as she stands at her desk. She is at the lower center of the frame
> with her head tilted up. She looks up at a colossal, flat monitor wall that fills most of the frame above her, seen
> in steep upward perspective, a grid of screens with thin black bezels all glowing one plain, even pale cyan with
> nothing on them. Above the wall, a small red signal-lamp box glows dim red. Haze and dust hang in the cold light.
> Composition: her head and shoulders at lower center, the giant wall above; strong vertical scale.

**Refs:** `assets/pilot/lookdev/ld1_hall.png`, `assets/pilot/lookdev/ld4_ida.png`, `assets/pilot/keyframes/k03_hall_wide.png`.

**Layers:** `assets/pilot/layers/k14_fg_ida.png` (`ALPHA=1`, attach k14). Prompt:
> Using the attached image, isolate only the woman's silhouette (head, shoulders and scarf) and the edge of her desk
> in the foreground, exactly as they appear, with the same position, scale, lighting and flat cel-painted style, on a
> genuinely transparent background. Everything else must be fully transparent. Keep the image the same size as the
> original.

**JS spec:** none. The insert is the k02 frame without the mesh.

**Sound:**
- PULSE on every tick; the hall clock.
- The DRONE returns (119.0) with an A1 fifth and the shimmer.
- A **BRASS** swell from +1.0 (abs 120.0), peaking at +5.5.
- No dialogue.

**Motion prompt (v2):** Flat 2D cel-painted style. Low angle from behind a lone woman standing at her desk in a vast
dark hall, looking up at a colossal wall of monitors that shows an old man's calm face. The red lamp above the wall
glows. Slow push-in past her toward the giant face's eyes. Dust in the cold light, faint haze. A deep electrical hum,
a clock ticking. No music. (In v2, re-insert the canonical k02 face in comp if the model alters the wall.)

**Takes:** —
