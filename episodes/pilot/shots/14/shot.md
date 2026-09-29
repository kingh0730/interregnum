# Shot 14 — FOUR MINUTES

**Duration:** 2 s (1:15–1:17; abs 75.0–77.0)  **Tool:** Codex plate p14 (shared with 22) + JS (the hands and the
flaps) + comp  **Camera:** a long lens up the axis from Desk 4; locked

**Action:** The Air Clock, high on the apse wall, seen far off through haze: a 3 m slave clock over its TO AIR board.
The second hand steps; the board reads 04:00, and on the next tick the flaps clack to 03:59. "Four minutes." The
countdown belongs to the building, not to a screen. It is the same framing both times (14 and 22): repetition is the
ritual, and the change is the story.

**Build:**
- Codex **p14**: the clock face with no hands and a board of blank flaps.
- JS **J08 v3** (below) renders the hands and the flap faces. Comp lays the hands onto the face's ellipse and the flap
  faces onto the cards by homography, and adds a few carved dust specks drifting in the haze.
- `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (`p14_air_clock`; also the plate of shot 22):**
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
> SHOT: a long-lens view with a 200 mm lens from far below, looking up the centre line of a dark concrete hall at the
> top of its end wall. Centred high on the board-formed concrete wall hangs a huge round slave clock three metres
> across: a cream enamel face, chipped at the rim, with plain black baton marks and no hands at all. Directly beneath
> it, in a steel frame, a long black board of four blank split-flap number cards in two pairs, each card split by a
> thin hinge line, with a small blank engraved plate on the frame. Both are lit from below by the cold pale cyan glow of
> a wall of screens out of frame beneath, which cuts the lower edges of the clock's rim and the board's frame as thin
> shapes and fades upward through parallel hatching of haze, with a few specks of dust between us and them. The
> concrete shows its plank grain and one pale patch of newer concrete. Composition: the clock and the board centred on
> the frame's vertical axis, the clock face filling about three quarters of the band's height and the board beneath it,
> dark wall on both sides.

**Refs:** `assets/pilot/lookdev_v3/hall.png`.
**Layers:** none.

**JS spec (J08 v3 · the Air Clock and the TO AIR board; params `time`, `toAir`, `alarm`, `push`):**
- **Device** (`production_design.md` §4): a slave clock with a 3 m cream enamel face and black baton hands, stepped by
  the broadcast master's pulse, which is why it stops when the broadcast dies (34). Beneath it, a split-flap board:
  cream numerals on black flaps, split by the hinge line; the minutes drum's **00 flap is printed red**. The board is
  centred under the face, as in §4, not beside it.
- **Hands:** hour and minute hands as tapered black batons, the second hand a thin black baton with a round
  counterweight; flat ink shapes with a 1 px irregular carved edge and no shadow. They are laid onto the face's ellipse
  (the face is seen from below) by homography.
- **Second hand:** steps on each whole second, a 2-frame move with a 1-frame overshoot and settle (the slave clock's
  twitch). **Minute hand:** jumps once a minute with a clunk.
- **Flaps:** Flap numerals (condensed square numerals with rounded corners), cream `#E8DDC4` on black, `MM:SS` on four
  cards with a painted colon on the frame. In each flip the top half falls in 3 frames and the bottom lands with a
  1-frame bounce, on the tick. The frame's plate reads TO AIR, engraved in State Capitals and cream-filled, the fill
  chipped from the A.
- **This shot:** `time="20:56"`, `toAir=240`, `alarm=false`, no push. At 0.0 the second hand steps and the flaps read
  04:00; at 1.0 the hand steps again and the cards flip to 03:59 (the minutes card to 03, the seconds pair to 59).
- **Removed:** v1's full-screen DIN numerals and frame line. The countdown is an object seen through air.

**Sound:**
- A heavy clock tick at 0.0 (+4 dB) and at 1.0.
- **PA** (`Karen`, 165, PA chain): **"Four minutes."** at shot +0.3 (abs 75.3).
- The DRONE begins to fade (77.0–78.0).

*v3 sound note:* add the flaps' clack under the tick at 1.0.

**Motion prompt:** n/a (plate, JS and comp).

**Takes:** —
