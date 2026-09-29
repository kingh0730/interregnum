# Shot 01 — THE LIGHTING (ident)

**Duration:** 5 s (0:00–0:05; abs 0.0–5.0)  **Tool:** Codex plate p01 + a silent Seedance take (v2) or a comp flame
(v1), with the JS caption card, film wear and telecine chain (broadcast, 4:3)  **Camera:** locked (a film on the
telecine)

**Action:** The nation's nightly ritual begins, and it is a film. In a black studio, one spotlight finds a
ceremonial lamp: a steel ring on a stand, a slim burner inside it, a bar beneath. A taper enters from the right, the
wick catches on the second bell, and the flame stands on the third. The caption card superimposes THE EVENING ADDRESS
· 21:00. The print is 41 years old and has run 14,763 times: scratched, dusty, weaving in the gate, tinted cold by
the broadcast chain. It is the only live thing left in the broadcast. The same film returns faster and colder in
shot 28, and at its old warmth in the alt tail (46). It replaces v1's app-splash emblem (`production_design.md` §7).

**Build:**
- Codex **p01**: the lamp **lit**, printed in black ink only. The unlit state is derived, not generated: mask the flame
  (one flat cream shape on solid black) and fill it with the surrounding black → `work/pilot/v3/p01_unlit.png`.
- **v2:** a 5 s silent Seedance take from `p01_unlit.png`, ending on p01 (`--end`). Slip it so the catch lands on the
  F♯ at 1.0.
- **v1 fallback:** the flame grows from the wick on p01's flame mask (scale 0 → 1 from its base over 1.0–1.5 s, with a
  2-frame flicker at the catch). No taper.
- The spotlight finds the ring at 0.5 s: p01's lit shapes rise from 0 to 100 % in 4 frames, a lamp switching on.
- JS **J01** caption card and film wear (below), then `broadcast()` without the bug, `grade(BROADCAST)`, and the 4:3
  pillarbox (1440×1080, centred). No letterbox. The first 0.2 s are black leader with the splice bump. Hard cut at 5.0.

**Keyframe prompt (`p01_lighting`):**
> STYLE (RELIEF): a frame from an animated film printed by hand as a colour woodcut and linocut on warm cream paper. A
> carved blue-black key block holds the image; large areas stay solid black, with faint wood grain. Every surface (skin,
> cloth, hair, concrete, metal, glass, floor) is matte printed ink: no reflections, no sheen, no specular highlights, no
> smooth gradients. Light is a shape cut out of the black with crisp, slightly irregular knife edges. Middle tones
> everywhere, on walls, floors and machines as on faces, are parallel gouge strokes that follow the form. Colour is flat
> spot ink, never blended, with paper grain showing through: pale cold cyan where screens light things, amber where lamps
> light things, signal red only on red objects. Slight misregistration; no drawn outlines. Only screen light is soft.
> Faces are a few carved planes, calm; eyes are small dark shapes without highlights. Avoid: anime, airbrush, digital
> painting, 3D render, photorealism, lens flare, bokeh, neon, glossy or wet floors.
> FRAME: wide 16:9, of which only the central 4:3 will be used: keep the lamp inside the middle three quarters of the
> width. No text, letters or numbers anywhere.
> SHOT: this image is printed in black ink only on cream paper, with no colour ink at all, like a frame of an old
> black-and-white film. A 50 mm view at the height of the lamp, in a completely black studio. In the centre stands a
> ceremonial lamp: a thin steel ring about a metre across, upright on a short stand; inside the ring, a slim burner;
> beneath it, a straight horizontal bar. A single flame stands on the burner, a tall pointed shape cut out of the black.
> One hard spotlight from above and slightly left cuts the upper edge of the ring and the top of the bar as crisp lines
> and throws a small pool of light under the stand. The ring shows one old repair: a clamp bolted over a crack. Every
> other part of the frame is solid black with the faint grain of the wood.

**Refs:** none. No lookdev applies to a black-and-white film of a lamp; the words carry it.
**Layers:** none.

**JS spec (J01 v3 · the Lighting, a Year One film on the telecine; the picture is the 1440×1080 4:3 window):**
- **Device:** a 35 mm black-and-white print of the ident film, shot in Year One and run through the telecine every night
  for 41 years. The caption is a separate hand-painted card, superimposed optically.
- **Caption card:** THE EVENING ADDRESS · 21:00 in State Capitals (`production_design.md` §5: a 4 × 6 module grid,
  monoline one module thick, quarter-circle corners of outer radius 1.5 modules, the O a rounded rectangle, letter
  spacing 1 module, word space 3), module 13 px (cap height 78 px), centred at y 820 of the picture. Hand-painted:
  cream `#E8DDC4` on black, dry-brush edges (1–2 px edge noise and two or three brush breaks per letter), the whole card
  0.5° off level; the middle dot a painted square. It fades up 2.2–3.0 s as an additive superimposition with 1.5 px
  blur and its own gate weave (it is a second strip of film).
- **Picture:** p01 (or the take), 4:3 crop, mapped to a monochrome film response (black `#11151F` to cream
  `#E8DDC4`), with grain at 3 %.
- **Wear:** 2–3 vertical scratches that stay put for the whole shot (they are on the print: cream, 1 px, 30–60 %); 3–6
  dust specks a frame, black and white; gate weave ±1.5 px on low-frequency noise; flicker ±4 %; a splice bump at
  0.2 s (a 2-frame, 12 px vertical jump with a flash of frame line).
- **Telecine and chain:** interlace twitter on thin horizontals, soft video bloom, and the cold tint (highlights mapped
  toward `#DDF1EE`). No bug: the ident is the channel.
- **Timeline:** 0.0–0.2 black leader; 0.5 the spotlight finds the ring; 1.0 the wick catches; 1.5 the flame stands;
  2.2–3.0 the caption; hold to 5.0.
- **Variants:** `fast` (shot 28) and `alt` (shot 46) are specified in those shots.

**Sound:**
- CHIME (BELL) **A4 at 0.5, F♯4 at 1.0, D4 at 1.5**, synced to circle, flame and base line.
- HYMN D major swell 1.0–4.8 (1M1).
- Broadcast studio tone (soft hiss at −48 dB).
- No dialogue.

*v3 sound note:* the three bells now land on the spotlight, the catch and the standing flame, at the same times. The
chime comes off the film's optical track, so give it a trace of wow and flutter.

**Motion prompt (v2, Seedance: start `work/pilot/v3/p01_unlit.png`, `--end work/pilot/keys_v3/p01_lighting.png`, 5 s,
`--no-audio`):** Woodcut print animation in black ink on cream paper, like an old black-and-white film; keep the first
frame's exact carved shapes. A ceremonial lamp in a black studio: a steel ring on a stand, a burner inside it, a bar
beneath, lit by one spotlight. The lamp does not move. After half a second, a thin taper enters from the right edge and
touches the burner; a flame catches and rises into a tall pointed shape; the taper withdraws out of frame to the right.
Then the flame stands still. Locked-off camera. No sound.

**Takes:** —
