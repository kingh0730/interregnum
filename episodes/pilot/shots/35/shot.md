# Shot 35 — ON AIR OFF

**Duration:** 2 s (3:06–3:08; abs 186.0–188.0)  **Tool:** Codex k21 + JS (the cast relief letters) + comp (the switch)
**Camera:** extreme close-up with a long lens; locked

**Action:** High on the apse wall, the ON AIR lamp: a riveted steel box with a front of cast red glass, the words cast
into the glass. It clicks off. The glass drops dark in three frames with an orange afterglow from the filament, and the
letters stay behind as relief, catching a little of the cold light from below. The building's hum winds down to
nothing. The letterbox is back: we are in the world, and the Father's 4:3 frame is gone for good. **Start pose:** the
lamp lit; the action is its switching off.

**Build:**
- Codex **k21**: the lamp lit, its glass blank.
- JS **J21**, the lettering as a height map (below), laid onto the glass by a homography of its 4 corners.
- **Lit (0.0–0.4 s):** the cast letters glow hotter than the glass around them (+25 % luma, a touch toward orange).
- **0.4 s, off:** the red glass drops to 12 % luminance over 3 frames, with an orange filament afterglow decaying over
  0.3 s. Unlit, the letters read as a darker embossing, their bevels catching the cold light from below.
- Comp is primary: the switch is exact and needs no model. `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (`k21_on_air`):**
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
> SHOT: an extreme close-up with a 200 mm lens of a lamp box mounted high on a board-formed concrete wall in a dark
> hall: a riveted steel box two metres wide with a front of thick cast red glass, lit from inside and glowing even
> signal red; the glass has a slightly uneven cast surface and no lettering or marks at all. One repair: a newer steel
> strap riveted across a cracked corner of the box. Its red light cuts the rivet heads and the plank grain of the
> concrete around it as small red shapes; a faint cold pale cyan glow from far below touches the underside of the
> housing. Everything else falls into black. Composition: the lamp box level and square to the camera, centred, filling
> the middle third of the frame.

**Refs:** `assets/pilot/lookdev_v3/hall.png`.
**Layers:** none.

**JS spec (J21 · ON AIR, cast into the glass):**
- **Letters:** ON AIR in State Capitals, **cast finish** (`production_design.md` §5): the 4 × 6 module skeleton at a
  module of one tenth of the glass's height, a word space of 3 modules, centred. It replaces v1's DIN mask.
- **Relief:** render the glyphs as a height map with a 45° bevel of 0.4 modules. Lit, the bevel reads as a brighter
  rim and the letter faces as hotter glass. Unlit, shade the height map with the cold light from below: the lower
  bevels catch a thin pale cyan edge, the upper bevels go dark.
- **Colour:** lit `#E0412F` with the letters toward `#F0643A`; unlit, the glass at 12 % (`#3A1512`), the relief visible.
- Static: one height map, used as a mask for both states.

**Sound:**
- **Relay click at +0.4 (abs 186.4).**
- The hall's electrical hum winds down from 55 Hz to 20 Hz, with gain going to zero over 1.4 s.
- Then silence: no clock (it stopped), no phone yet.

**Motion prompt (v2, optional; comp is primary because the switch must land on the relay click. Seedance: start
`work/pilot/keys_v3/k21_on_air.png`, 4 s, `--no-audio`; use 2 s):** Colour woodcut print animation; keep the first
frame's exact carved shapes, flat inks and designs. An extreme close-up of a riveted steel lamp box with a front of red
glass, high on a concrete wall, glowing. After half a second the light inside goes out: the glass darkens to a dull deep
red, with a brief orange glow fading from inside it. Nothing else moves. Locked-off camera. No sound.

**Takes:** —
