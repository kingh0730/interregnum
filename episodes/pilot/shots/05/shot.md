# Shot 05 — THE HALL

**Duration:** 8 s (0:22–0:30; abs 22.0–30.0)  **Tool:** Codex k03 + the Wall insert, then a silent Seedance take (v2)
or a comp push (v1)
**Camera:** 24 mm, 10 m up at the back of the nave on its centre line, in one-point perspective (the institution's
eye). It travels down the nave toward Desk 4 on rails, at a constant speed.

**Action:** A concrete basilica in the dark. Four hundred covered desks, laced shut the day after the operators were
dismissed, recede in rows like a field of graves toward the Wall. There the frozen face, twenty metres tall, is broken
into 96 tubes in deep niches and still wears its wireframe. On the axis, a third of the way from the Wall, one lit
desk and one small woman in an amber scarf, less than three percent of the frame. The camera moves toward her like a
machine. Nobody moves; dust rises from the floor grilles into the light. **Start pose:** Ida seated at the lit desk
with her back to us.

**Build:**
- Codex **k03**.
- **The Wall insert** (both versions): `f04_frozen.png` with `f04_mesh_state.png` over it, desaturated 60 % as at the
  end of 04, inserted tile by tile into k03's 96 glowing quads (`production_design.md` §4): one homography and one tile
  per tube, barrel k1 0.04, a rounded mask with a corner radius of 8 % of the tile width, 25 % vignette, colour ±8 % and
  brightness ±10 % per tube plus ±2 % slow noise, and bloom. One tube at the upper right, outside the face, is dead
  black; one near the lower edge carries a hum bar rolling up every ~7 s. Save the result as
  `work/pilot/v3/k03_wall.png`: it is both the comp plate and the Seedance start frame. This replaces v1's
  `bezels(12×8)`.
- **v2:** an 8 s silent take from `k03_wall.png`: the dolly. If the model alters the face, re-insert it per frame on a
  planar track of the Wall's outer quad.
- **v1 fallback:** `push(1.00→1.07, focus=(0.50, 0.66), linear)` at a rail's constant speed, with
  `parallax(near_covers=1.0, plate=0.55)` on a matte of the nearest covered desks cut from k03 itself (GrabCut plus
  inpainting). `dust(120)` rising from the grilles, lit only inside the Wall's light.
- The ON AIR lamp and the gallery stay dark: nobody is watching yet. `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (`k03_hall_wide`):**
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
> SHOT: a vast night interior in exact one-point perspective, seen with a 24 mm lens from 10 metres up at the back of
> the nave, on its centre line. The Hall of a broadcast ministry, built like a basilica: square board-formed concrete
> piers, carved with plank grain and rows of round tie-holes, rise into a ribbed vault lost in solid black; olive-black
> brass pneumatic tubes climb every pier and never shine; a cast-iron horn loudspeaker on each pier points down the
> nave. Between the piers, four hundred operator desks under fitted canvas covers laced on with cord stand in straight
> rows, a field of pale shapes cut from the dark, receding to the far end. The floor is dark terrazzo printed as matte
> black ink broken by short straight gouge strokes; thin inlaid brass lines, printed as pale cold cut lines, run the
> length of the nave; iron floor grilles breathe dust up into the light. The whole far wall is a grid of 12 by 8 deep
> concrete niches with thick walls between them, each holding one large old television tube with a curved,
> round-cornered face, all glowing the same blank pale cyan: the only strong light, throwing the piers' long shadows
> down the nave as cut shapes. Above the wall on the centre line: a riveted steel lamp box with a dark, unlit red glass
> front, a long black board of blank flip-number cards, and a huge pale round clock face with plain baton marks. High
> on the left wall, a dark glass gallery box juts over the nave, unlit. On the centre line, a third of the way from the
> wall, one uncovered desk is lit by its own small glowing screens, and Ida (the woman on the attached sheet) sits at
> it with her back to us: a black bob and a mustard-amber scarf, the only warm colour in the image. She is tiny, less
> than three percent of the frame, at the foot of the vanishing point. At least half of the image is solid black.

**Refs:** `assets/pilot/lookdev_v3/hall.png`, `assets/pilot/lookdev_v3/ida.png`.
**Layers:** none. v1's `k03_fg_desks` is cut: Seedance makes the move, and the v1 fallback cuts its matte from the
plate.
**JS spec:** none new. The Wall shows shot 04's frozen state, tile by tile.

**Sound:**
- Hall room tone (55 Hz hum and air); rain on a high roof, distant.
- **Hall clock ticks** on every whole second (22, 23, … 29), in HALL REVERB.
- A distant pneumatic hiss at shot +5.5 (abs 27.5).
- Score 1M2: DRONE fades in from 22.0 over 3 s.
- No dialogue.

**Motion prompt (v2, Seedance: start `work/pilot/v3/k03_wall.png`, 8 s, `--no-audio`):** Colour woodcut print
animation; keep the first frame's exact carved shapes, flat inks and designs. An extreme wide view in one-point
perspective from high at the back of a vast dark concrete hall: rows of covered desks lead to a wall of glowing
television tubes that together show one enormous still face. On the centre line far below, a small woman sits at the
one lit desk with her back to us. Nothing in the hall moves, she does not move, and the face on the wall does not
change. Only dust drifts slowly upward in the cold light. The camera travels forward along the centre line at a
constant speed, like a camera on rails, without tilting or turning. No sound.

**Takes:** —
