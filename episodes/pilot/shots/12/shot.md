# Shot 12 — THE LOOP

**Duration:** 8 s (1:03–1:11; abs 63.0–71.0)  **Tool:** Codex plate p12 + JS (the terminal's text, the meter, the
printer's paper) + comp (focus pull, raster breathing) + dialogue sound design
**Camera:** locked, from Ida's right at desk height, in two planes; a focus pull at 6.0

**Action:** She lets him speak: the FREE lamp blinks. The Engine writes the Father on the Script Terminal in cold
letters, word by word, while his voice reads them. It starts plausibly and then can only repeat: I am well. I am well.
The scroll smears into bands of light, the picture swells, and the needle pins at 0.99 and shivers. Then the loop
escapes the glass into the room: the Log Printer in the foreground hammers I AM WELL. I AM WELL. onto fanfold paper
that climbs toward the lens and spills over the desk. The red HALT lamp. The printer stops mid-word (I AM WE), the tube
drops to standby, and the needle stays pinned: the machine is still certain. **The thesis in one image:** a model
trained only on the past can only produce more of it.

**Build:**
- Codex **p12**: the terminal and the teleprinter in one frame, with the tube and the paper blank.
- JS **J07 v3** (below) renders the terminal and the paper strip. Comp inserts the tube picture by homography with the
  tube artefacts, redraws the meter's needle (the plate's needle masked out), lights the FREE and HALT lamps on their
  masks, and maps the printed paper onto the plate's paper (a texture that scrolls up inside the paper's mask as the
  paper advances, with a simple mesh warp at the fold).
- **Focus pull 6.0–7.0 s:** layer blur: the tube softens to 12 px while the printer sharpens from 10 px to 0.
- The dialogue drives the timing: D06 and D07 are rendered first, and the Engine's words append on the voice's word
  onsets.
- `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (`p12_loop`):**
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
> SHOT: a hardware insert in two planes, seen from the operator's right at desk height with a 60 mm lens, at a steel
> console in a dark hall. The left two thirds: a small monochrome terminal tube, deeply curved and round-cornered, set
> back under a hood in a blue-grey hammered-enamel housing, its face glowing blank, even pale cyan; on the housing's
> right cheek, a round moving-coil meter behind frosted glass lit cold from behind, with a blank arc scale and a black
> needle resting at zero, and below it a column of four small blank rectangular indicator lamps, unlit. The right
> third, in the near foreground and slightly out of focus: the platen and hood of an upper-case teleprinter on its own
> stand, with a blank strip of pale fanfold paper rising from it toward the camera and folding over at the top. The
> tube's cold light is the only key: it cuts the hood's edges and the top of the paper as thin shapes; everything else
> falls into black. One repair: the teleprinter's hood is held on with a strap of newer steel.

**Refs:** `assets/pilot/lookdev_v3/hall.png`.
**Layers:** none.

**JS spec (J07 v3 · the Script Terminal running free, and the Log Printer):**
- **The tube** (`production_design.md` §4): a 30 cm two-layer tube showing 48 columns × 12 rows of Operator Mono (a 7 × 9
  dot matrix in a 9 × 14 cell, 2 descender rows; each dot a short horizontal dash with a dark gap between scan rows;
  slashed zero; straight apostrophe). Everything here is the Engine's, so everything is **cold**: core `#DDFBFA`, bloom
  `#5FE1E6`, persistence about 60 ms.
- **The text**, appended on the voice's word onsets from 0.3 s: Good evening, my children. The harvest is in. The sea
  is calm. I am well. Sleep safely; I am watching over you. I am well. The sea is calm. I am well. I am well. I am
  well… From 3.5 s only "I am well." is appended, accelerating from 3 to 15 a second by 7.0.
- **Scroll:** one-row jumps with a 1 px bounce until about 5 s; then the rate outruns the phosphor and the rows smear
  into bright persistence bands.
- **Raster breathing:** the picture swells up to 0.5 % as its brightness rises (strongest over 5.0–7.4 s). A hum bar
  (−8 %) rolls up once every 6 s. Scanlines are visible (the tube is large in frame).
- **The meter:** the needle rises to 0.99 at 0.3 s (a 0.3 s rise, 8 % overshoot, settle) and is pinned there, shivering
  ±0.5° at 6 Hz from 3.5 s. The scale is engraved PREDICTION, 0 to 1.0, in State Capitals on the frosted glass.
- **The lamps:** FREE (red) blinks at 1 Hz from 0.3 s. HALT (red) lights at 7.4. Legends engraved and filled black.
- **The printer** (6.0–7.4 s, once the focus has pulled to it): the paper shows I AM WELL. I AM WELL. in upper case
  from the teleprinter's type (a 10-pitch monoline sans in blue-black ribbon ink, uneven strike density, the odd
  half-struck letter), printed at the choir's rate. The paper advances and folds over the desk edge.
- **7.4 s, HALT:** the printer stops mid-word (I AM WE). The tube drops to 30 % standby with the text still on it. The
  needle stays pinned at 0.99. Hold to 8.0.
- **Removed:** v1's top bar, preview pane, waveform and confidence column. The meter is the confidence.

**Sound:**
- **FATHER (generated)** (`Daniel`, 150, LOOP chain, dry): D06 from shot +0.3 (abs 63.3).
- **D07 Loop choir** from +3.5 (abs 66.5): about 30 copies of "I am well.", accelerating, detuned ±15–40 cents,
  randomly panned, and getting darker (full recipe in `cues.md` §6). The DRONE and PAD glide up a semitone, D→E♭.
- **At +7.4 (abs 70.4): mute everything, including the hall clock.** Total silence until 71.0.
- Subtitle: *I am well. I am well. I am well…*

*v3 sound note:* add the teleprinter's hammering at the choir's rate from 6.0 (the loop made physical), cut dead with
everything else at 7.4.

**Motion prompt:** n/a (plate, JS and comp). The paper's advance is a texture scroll, not a take.

**Takes:** —
