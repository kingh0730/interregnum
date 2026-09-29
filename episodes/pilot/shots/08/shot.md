# Shot 08 — ARCHIVE

**Duration:** 9 s (0:41–0:50; abs 41.0–50.0)  **Tool:** Codex plate p08 + JS (the film strip, drum counters, scope
trace and handwriting) + comp  **Camera:** straight overhead, 50 mm, locked (paper and the archive are evidence)

**Action:** The Archive Reader, from above: a bar of warm light across the dark desk. Forty-one years of the Evening
Address run across it on film, one frame a month, the year tabs flicking past, until the strip brakes to a dead stop
on the last live frame, flagged in grease pencil: LAST LIVE CAPTURE · 10 MAR. Beside it the scope lights NO SIGNAL
over a flat trace, and its light finds a paper tag in a doctor's hand: 11 MAR · 04:12. The death was recorded by hand,
and the state covered it with a machine. Then the strip moves on over a tape splice into cold stock, frames of the copy
racing into a streak, the GENERATED drums rolling to 212, and stops on a clear, unexposed frame of pure warm light:
212 · TONIGHT. **Reveal 2 reads without a label:** a living man carved on warm film, then the smooth cold copy, then an
empty warm frame that a hand will fill.

**Build:**
- Codex **p08**: overhead of the light table in the desk's left wing, its window lit warm and empty, the drum counters
  and scope blank, the tag blank.
- JS **J04 v3** (below): the strip is inserted into the window quad with a **multiply** blend over the frosted glass,
  because film is a transparency lit from beneath. The drums go into their windows, the trace into the scope's circle,
  the handwriting onto the tag, each by homography.
- `letterbox(2.39)`, `grade(HALL)`, keeping the light table warm (exclude its mask from the cool grade).

**Keyframe prompt (`p08_archive`; also the source of shot 46's counter):**
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
> SHOT: straight down from directly overhead with a 50 mm lens: the left wing of a steel operator's desk in blue-grey
> hammered enamel, its edge worn to bare metal, in the dark. Across the middle of the frame runs a long frosted-glass
> window set flush into the desk top and lit warm amber from below by a tungsten lamp: a horizontal bar of warm light,
> blank and even, with a small roller housing at each end and nothing on the glass. Below the window, at the lower left
> and lower centre, two mechanical counters behind small glass windows, one with five black number drums and one with
> three, all blank. At the lower right, a round oscilloscope tube 12 centimetres across in a steel bezel, dark, with two
> knobs; a small blank paper tag hangs from one knob on a string and lies in shadow. One repair: the glass window is
> held at one corner by a newer steel clip. The warm window is the only light and cuts the desk top around it as crisp
> shapes; everything else falls into black.

**Refs:** `assets/pilot/lookdev_v3/hall.png`.
**Layers:** none.

**JS spec (J04 v3 · the Archive Reader, the drum counters and the vitals scope):**
- **Device** (`production_design.md` §4): a light table with a motorised transport. The index strip is 35 mm
  black-and-white film, one frame per month since Year One, with paper tabs flagging each year. After the frame of 10
  MAR comes a clear tape splice, then the generated nights on a different stock, recorded from a tube. Two mechanical
  drum counters (white numerals on black drums) sit behind engraved plates, CAPTURED and GENERATED. The 12 cm vitals
  scope has a cold green-cyan long-afterglow phosphor, a plate engraved VITALS · SUBJECT F, a red NO SIGNAL legend lamp,
  and a paper tag on its knob.
- **The strip** (rendered flat, 4-perf, a 150 px frame pitch in window space): sprocket holes at both edges, frame
  lines, edge fog. **Captured frames** are black-and-white crops of the `father` lookdev sheet: the living man, carved,
  with the head angle varying from frame to frame, grain, and density ±8 %. The year tabs are small paper tabs taped to
  the edge and marked 1…41 in the archivist's grease pencil (blunt, waxy SVG strokes).
- **0.0–4.6 s, captured:** right to left. The strip eases in over 0–1.0 s to a cruise where the frames smear along
  its length and the frame lines flicker, then eases out over 3.0–4.6 s so the frame of 10 MAR stops dead in the
  centre at 4.6 (a 2 px overshoot and settle: it brakes). CAPTURED rolls 00001 → 14,763 with the strip (numerals roll
  vertically; a carry rolls the next drum).
- **4.6 s:** the last live frame, flagged in grease pencil on the film's edge: LAST LIVE CAPTURE · 10 MAR. It has been
  there since March; the stop reveals it.
- **4.9 s:** the scope's NO SIGNAL lamp lights red (a 2-frame dip, then red) over a flat trace: the beam sweeps left to
  right with ±1 px noise and a 1.5 s afterglow behind it. Its faint green-cyan spill finds the tag, which brightens from
  5 % to 25 % and shows 11 MAR · 04:12 in the doctor's hurried cursive (SVG strokes with pressure, dark ink).
- **5.2–8.2 s, generated:** the strip moves on over the clear tape splice (a visible bump and tape edge) into the cold
  stock: blue-base frames of the copy (crops of k01 and k02, smooth, with scanlines inside each frame), accelerating
  from 3 to about 150 frames a second until they streak. GENERATED rolls 001 → 212, the drums blurring, then settling.
- **8.2 s:** it stops on a **clear, unexposed frame**: pure warm light from the lamp beneath, boxed in grease pencil,
  with 212 · TONIGHT written beside it. Hold to 9.0. v1's cursor block is gone.
- **The argument in materials:** warm film of a carved, living man (lit by a filament), then the cold stock of a smooth
  copy, then an empty frame of warm light (tonight is unwritten, and a hand will write it).

**Sound:**
- 0.0–4.4 s: RISER (the whoosh of years).
- **At 4.6 (abs 45.6): SUB HIT, and everything else drops out** (DRONE ducks −15 dB).
- 4.9–8.9 (abs 45.9–49.9): the flatline tone, 1 kHz at −32 dB.
- 5.2–8.2 (abs 46.2–49.2): 212 soft clicks, one per generated thumbnail, accelerating into a buzz.
- 8.5 (abs 49.5): one low PLUCK D2.
- The hall clock continues underneath, quietly (−4 dB).

*v3 sound note:* the 212 clicks are now the transport's frame clicks as the generated frames pass the gate (same
times); add a soft motor whine under the captured run.

**Motion prompt:** n/a (plate, JS and comp).

**Takes:** —
