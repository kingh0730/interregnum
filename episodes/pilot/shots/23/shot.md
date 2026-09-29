# Shot 23 — THE FACE

**Duration:** 6 s (1:59–2:05; abs 119.0–125.0)  **Tool:** Codex k14 + the Wall insert (the clean face), then a silent
Seedance take (v2) or a comp push (v1)
**Camera:** 28 mm, 0.6 m high, just behind her, looking up: the only low angle in the Hall. It pushes past her into
his eyes, accelerating.

**Action:** Ida has stood up. She is a small dark shape at the lower left, off the axis: standing, she breaks the
Hall's symmetry, and that is an act. Above her the face fills the Wall, clean now, in full colour and without its
wireframe: ready for air. The ON AIR lamp above it glows dimly on standby. We move past her shoulder and into his
eyes. This is the scale of what she's about to do. **Start pose:** Ida standing at her desk with her back to us, her
head tilted up.

**Build:**
- Codex **k14**.
- **The Wall insert** (both versions): **k02, clean** (no mesh, full colour), tile by tile into k14's 96 quads, seen in
  steep upward perspective: click the Wall's outer 4 corners once and let the niche grid carry the tiles. Per tube, as
  in 05: curvature, colour and brightness jitter, the dead tube, the hum bar, bloom, and scanlines (the tiles are larger
  than 250 px here). Save as `work/pilot/v3/k14_wall.png`, the comp plate and the Seedance start frame.
- The ON AIR lamp at a dim standby glow (0.5 Hz, 60–90 %), a filament kept warm.
- **v2:** a 6 s silent take from `k14_wall.png`: the push. If the model alters the face, re-insert it per frame on a
  planar track of the Wall.
- **v1 fallback:** `push(1.00→1.10, focus=the face's eyes, easeInQuad)`, with `parallax(her=1.0, plate=0.5)` on a matte
  of her silhouette cut from k14 (GrabCut); she slides down and out of the lower frame. `dust(80)` in the cold light.
- `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (`k14_hall_low`):**
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
> SHOT: a low angle from 60 centimetres above the floor, just behind Ida (the woman on the attached sheet) and a little
> to her right, seen with a 28 mm lens looking up. She stands at her desk with her back to us, a small dark shape at the
> lower left of the frame: the black bob, the shoulders of the charcoal sweater, one edge of the mustard-amber scarf cut
> out by the light. Above and beyond her, filling most of the frame in steep upward perspective, is the great end wall
> of the hall: a grid of 12 by 8 deep concrete niches with thick walls between them, each holding a large
> round-cornered television tube, all glowing the same blank, even pale cyan. It is the only strong light, and it cuts
> her outline and the edge of the desk as thin cold lines. Above the wall on the centre line, a riveted steel lamp box
> with a dim red glass front, and above it the pale round face of a huge clock. The board-formed concrete piers at both
> sides rise out of frame, carved with plank grain. Parallel hatching of haze and a few specks of dust hang in the cold
> light. Composition: the wall of tubes square and centred above; she is off-centre at the lower left, breaking the
> symmetry.

**Refs:** `assets/pilot/lookdev_v3/hall.png`, `assets/pilot/lookdev_v3/ida.png`.
**Layers:** none. v1's `k14_fg_ida` is cut: Seedance makes the move, and the v1 fallback cuts her matte from the plate.
**JS spec:** none. The Wall shows k02, clean.

**Sound:**
- PULSE on every tick; the hall clock.
- The DRONE returns (119.0) with an A1 fifth and the shimmer.
- A **BRASS** swell from +1.0 (abs 120.0), peaking at +5.5.
- No dialogue.

**Motion prompt (v2, Seedance: start `work/pilot/v3/k14_wall.png`, 6 s, `--no-audio`):** Colour woodcut print
animation; keep the first frame's exact carved shapes, flat inks and designs. A low angle from behind a young woman
standing at her desk in a vast dark hall, looking up at a colossal wall of television tubes that together show an old
man's still face. She does not move, and the face on the wall does not change. Dust drifts slowly in the cold light.
The camera moves forward past her shoulder toward the eyes of the face on the wall, slowly at first and then faster,
straight, without turning, so that she slides out of the bottom of the frame. No sound.

**Takes:** —
