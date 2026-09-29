# Shot 37 — NANA CALLING

**Duration:** 3 s (3:12–3:15; abs 192.0–195.0)  **Tool:** Codex plate p37 + JS (the pencilled name, the call lamp) +
comp
**Camera:** a macro insert across the desk at the telephone's height, 60 mm; locked

**Action:** The House Line rings: the Ministry-grey desk telephone, the same set as Nana's in cream. Its small amber
call lamp flashes with each ring, beside a paper card where Ida's pencil has written NANA. Soft behind it, the red
phone's handset shivers in its cradle. Two phones, two lights. The personal colour arrives as a small filament lamp
beside a name written by hand, which is exactly what Nana is to her. She will answer the grey one.

**Build:**
- Codex **p37**: the grey telephone with its lamp unlit and its card blank, the red telephone soft behind.
- JS **J12 v3** (below): the pencil strokes multiplied onto the card; the lamp's flashes and their warm light on the
  enamel.
- The red phone behind: `jitter(mask=its handset, 1 px, 25 Hz)` during its ring at shot +2.0–2.9.
- `letterbox(2.39)`, `grade(HALL)` with the amber kept warm (exclude the lamp and its spill from the cool grade).
- Removed: v1's smartphone, its app-style name screen, the "calling…" line and the accept and decline circles. A
  smartphone cannot exist in this world.

**Keyframe prompt (`p37_house_line`):**
> STYLE (RELIEF): a frame from an animated film printed by hand as a colour woodcut and linocut on warm cream paper. A
> carved blue-black key block holds the image; large areas stay solid black, with faint wood grain. Every surface (skin,
> cloth, hair, concrete, metal, glass, floor) is matte printed ink: no reflections, no sheen, no specular highlights, no
> smooth gradients. Light is a shape cut out of the black with crisp, slightly irregular knife edges. Middle tones
> everywhere, on walls, floors and machines as on faces, are parallel gouge strokes that follow the form. Colour is flat
> spot ink, never blended, with paper grain showing through: pale cold cyan where screens light things, amber where lamps
> light things, signal red only on red objects. Slight misregistration; no drawn outlines. Only screen light is soft.
> Faces are a few carved planes, calm; eyes are small dark shapes without highlights. Avoid: anime, airbrush, digital
> painting, 3D render, photorealism, lens flare, bokeh, neon, glossy or wet floors.
> FRAME: wide 16:9; keep everything important inside the central horizontal band, because the top and bottom 13% will
> be cropped to 2.39:1. No text, letters, numbers or logos anywhere; every screen is blank and evenly glowing.
> SHOT: a macro insert across a steel desk at the height of a telephone, seen with a 60 mm lens. In focus right of
> centre: a grey rotary desk telephone in blue-grey hammered enamel, its handset in the cradle and its coiled cord
> looping away; beside the dial, a small round amber glass jewel lamp, unlit; on the front of its base, a small paper
> card under a scratched celluloid window, blank. The enamel is chipped at one corner and repainted in a slightly
> different grey. Behind it at the left, soft and out of focus, a heavy red telephone with no dial. A thin cold rim of
> pale cyan light from a screen above cuts the tops of both telephones; everything else falls into black.

**Refs:** `assets/pilot/lookdev_v3/hall.png`.
**Layers:** none.

**JS spec (J12 v3 · the House Line):**
- **Device** (`production_design.md` §4): the state's one civilian telephone in Ministry grey, with a rotary dial, a
  small amber **call lamp** (a filament behind a jewel lens) that flashes while it rings, and a paper card under
  celluloid on its base.
- **The name:** NANA in Ida's pencil: small, careful capitals leaning slightly forward, drawn as SVG strokes with
  pressure (graphite: grain-modulated density, soft edges, matte), multiplied onto the card's quad. Over it, the
  celluloid's static scratch layer at 10 %.
- **The lamp:** it flashes with each ring, lit 0.1–0.6 s and 1.6–2.1 s, with a filament's thermal lag (a 60 ms rise and
  a 150 ms fall). Lit, the jewel glows `#FFD9A0` at its core with a small `#F2A441` bloom on the lens only. Its light on
  the grey enamel and the card is a hard-edged warm shape (the phone's near planes switch toward amber ink by up to
  35 %), not a soft glow: in RELIEF only screen light is soft.
- **The grey handset** rattles 0.5 px in its cradle on each ring. The bell phone has no buzz and does not vibrate.

**Sound:**
- **Ida's ringtone** (warm, marimba-like PLUCK): **A4 then D5, 0.25 s apart**, at +0.1 and +1.6 (abs 192.1, 193.6).
- The phone's buzz on the desk (60 Hz rattle, −30 dB) during the vibrations.
- The red phone continues at abs 194.0 (through the hall reverb, −6 dB): two phones, two lights.

*v3 sound note:* the ringtone now comes from the House Line's bell, which is Nana's bell: softer and higher than the
Red Line's (`production_design.md` §4). Keep the times and the A4–D5 contour, retune the pluck into a small bell, and
turn the desk buzz into the handset's rattle in its cradle.

**Motion prompt:** n/a (plate, JS and comp).

**Takes:** —
