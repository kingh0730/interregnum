# Shot 13 — "NO, YOU'RE NOT."

**Duration:** 4 s (1:11–1:15; abs 71.0–75.0)  **Tool:** Codex k07 + a Seedance take with dialogue (v2) or comp (v1)
**Camera:** close-up, 85 mm, 10 cm above her eye line (a colleague's eye, never below); locked-off

**Action:** In the silence after HALT, Ida is lit from below by the frozen text. She speaks to the machine as if it
were a colleague, or a liar: "No, you're not." The line carries the first crack in her detachment. Her face barely
moves; the silence, the light from below and the flat voice carry it. **Start pose:** eyes on the terminal below the
frame, mouth closed, about to speak.

**Build:**
- Codex **k07**.
- **v2:** a 4 s take with the line (audio on).
- **v1 fallback:** locked-off; the light is steady (the tube is on standby), with a faint 1 % noise. v1's eye-highlight
  reflections are dropped: eyes carry no highlights in RELIEF.
- `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (`k07_ida_no`):**
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
> IDA (the woman on the attached sheet): 27, slim; a blunt black bob cut straight at the jaw, with straight bangs above
> her brows; straight dark brows; a small straight nose; warm light-olive skin; a small silver hoop in her left ear; a
> charcoal ribbed turtleneck and a hand-knitted mustard-amber scarf, the only warm colour on her.
> SHOT: a close-up of Ida seated at her desk in the dark hall, seen with an 85 mm lens from her front-left, 10 cm above
> her eye line. She faces screen-left and looks down at a small terminal screen just below the bottom-left of the frame;
> its cold pale cyan light is the only key and cuts her face from below as crisp shapes: the underside of her jaw, her
> lower lip, the undersides of her brows and of her bangs lit, her forehead falling into black. Her face is composed
> and still: jaw set, mouth closed, eyes resting on the screen. Composition: her face on the left third, turned toward
> the near edge of the frame; behind her head the right half of the frame is dark space, with a few far, soft pale
> blocks of the wall of tubes. Her amber scarf shows at the bottom edge.

**Refs:** `assets/pilot/lookdev_v3/ida.png`, `assets/pilot/lookdev_v3/hall.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- The hall clock returns at 0.0 (abs 71.0), and the DRONE returns at −3 dB.
- **IDA** (`Samantha`, 160, IDA hall chain): **"No, you're not."** at shot +1.0 (abs 72.0), quiet and flat.
- Nothing else.

**Motion prompt (v2, Seedance: start `work/pilot/keys_v3/k07_ida_no.png`, 4 s, audio on):** Colour woodcut print
animation; keep the first frame's exact carved shapes, flat inks and designs. Close-up, 85 mm, slightly above her eye
line: a young woman at a desk in a dark hall, lit from below by a small screen, faces left, her eyes on the screen. Her
head does not move. After one second she says quietly and flatly, lips barely moving: "No, you're not." Then she keeps
looking at the screen without moving. She speaks in a young woman's low, soft, tired voice with a neutral General
American accent. Understated performance: her face stays composed; only her lips move. Locked-off camera. The low hum
of a large hall. No music.

**Takes:** —
