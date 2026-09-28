# Shot 30 — THE STREET

**Duration:** 6 s (2:37–2:43; abs 157.0–163.0)  **Tool:** Codex keyframe + cutout layer + comp + facade-screen insert
**Camera:** wide street; push-in 1.00→1.04 toward the giant screen, with parallax

**Action:** A tram stopped mid-street in the rain. A crowd under umbrellas, faces lifted to the giant screen on a
building, where the Father speaks: "I died in the spring." The words echo off the buildings. The tram's hum cuts out
and there is only rain. Nobody moves: the stillness of a whole city in shock. **Start pose (v2):** a crowd standing
still, looking up.

**Build:**
- Codex **k17** (the screen is blank):
  `tools/imagegen/gen.sh assets/pilot/keyframes/k17_street_crowd.png "<prompt>" assets/pilot/lookdev/ld2_city.png`
- Codex layer **k17_fg_crowd** (`ALPHA=1`, attach k17).
- Comp:
  - `insert(src=k01 with broadcast() treatment and the J14 bug, target=auto)` into the facade screen, plus strong
    bloom and a cyan light spill on the wet street (add luminance along the reflection streaks, driven by the inserted
    frame's luma).
  - `rain(layers=2)` plus ground splashes (tiny particles at street level).
  - The tram windows glow steadily.
  - `push(1.00→1.04, focus=screen)`, with `parallax(k17_fg_crowd=1.0, plate=0.6)`.
  - `letterbox(2.39)`, `grade(CITY)`.

**Keyframe prompt (k17):**
> STYLE: a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean, confident
> dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow only around
> light sources; subtle paper grain; realistic human proportions and faces (not chibi, no oversized eyes); simplified
> graphic backgrounds with bold silhouettes and large areas of dark negative space. PALETTE: deep ink-navy and
> blue-black darkness; cold pale-cyan light comes only from screens; warm amber light comes only from household lamps
> and warm objects; signal red only where described; no other saturated colors. LIGHT: one strong motivated light
> source, deep shadows, light haze. FRAME: wide 16:9 landscape; keep every important element inside the central
> horizontal band, because the top and bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters, numbers,
> logos or watermarks anywhere; every screen is a blank, evenly glowing panel.
> LOCATION: a street in the City of the attached style frame, at night in heavy rain. A wide view down a wet street:
> at the left, a stopped tram with glowing windows; in the foreground and middle ground, a crowd of about forty
> people, seen from behind and from the side as dark silhouettes, many holding umbrellas. They all stand perfectly
> still and look up at a gigantic screen on the facade of a tall building ahead. The screen is blank, glowing plain
> cyan with nothing on it. The wet street reflects the cyan light in long streaks, and rain slants through the light.
> Nobody's face is visible. Composition: the giant screen in the upper center, the crowd across the lower half.
> Mood: a whole city frozen, listening.

**Refs:** `assets/pilot/lookdev/ld2_city.png`.

**Layers:** `assets/pilot/layers/k17_fg_crowd.png` (`ALPHA=1`, attach k17). Prompt:
> Using the attached image, isolate only the nearest foreground people with umbrellas (the closest silhouettes of the
> crowd), exactly as they appear, with the same position, scale, lighting and flat cel-painted style, on a genuinely
> transparent background. Everything else must be fully transparent. Keep the image the same size as the original.

**JS spec:** the J14 bug inside the inserted screen image.

**Sound:**
- City rain and street splashes; the tram idle hum from 0.0 to **1.8 (abs 158.8), then cut dead**.
- **FATHER** (`Daniel`, 130, STREET chain: echoing off the buildings with a 350 ms slapback): **"I died in the
  spring."** at shot +0.8 (abs 157.8).
- After the line: only rain.
- No music, no clock, no phone.

**Motion prompt (v2):** Flat 2D cel-painted style. A rainy street at night: a stopped tram and a crowd of
silhouetted people with umbrellas standing still, all looking up at a giant screen on a building where an old man
speaks: "I died in the spring." Rain streaks through the cold light, and nobody moves. Slow push-in toward the
screen. Rain, the voice echoing off buildings, a tram's hum cutting out. No music. (In v2, re-insert the k01 frame
into the screen in comp.)

**Takes:** —
