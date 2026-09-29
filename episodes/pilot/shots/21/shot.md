# Shot 21 — SIGN-OFFS · DESK 4

**Duration:** 8 s (1:49–1:57; abs 109.0–117.0)  **Tool:** Codex plate p21 (shared with 24 and 26) + JS (the terminal
page) + comp (the insert, and amber light on her fingertips)
**Camera:** a hardware insert, a little above her eye line and 15° off the tube's axis; locked. The lower two thirds
of the glass and the top row of keys, where her fingertips rest.

**Action:** After the call, Ida calls up a page on the Script Terminal: SIGN-OFFS · DESK 4, every last line the Father
has spoken in 212 generated nights. The Engine's lines are cold: Sleep safely. Sleep safely. Scattered among them, in
her colour because she typed them, are lines no state has ever broadcast: Close the window. The wind is sly. Don't
argue with the rain. Leave a light on for whoever comes home late. From Night 150 every night ends the same, a solid
block of amber: Eat something warm before you sleep. The scroll slows to NIGHT 212, blank, the cursor blinking on the
tick. As the amber block rises into the lower glass, its light falls on her fingertips: **the first warm light on Ida
in the Hall comes from her own words.** **Reveal 3 (for the audience):** she has been writing to her grandmother
through the Father.

**Build:**
- Codex **p21**: the terminal with its tube blank, the meter, the lamps and the repeater, and her fingertips on the top
  row of keys. Shots 24 and 26 use a 1.25× crop of the same plate above the keys.
- JS **J09 v3** (below), inserted into the tube quad by homography with the tube artefacts. The rename is from
  `production_design.md` §9: this world has no file extensions, so `signoffs.txt` is gone.
- **The warm light:** `flicker(mask=fingertips, driver=the insert's amber luma, up to +35 % toward lamp amber)`. The
  fingertips are a small light region at the bottom of the plate; as the amber block fills the lower glass, they warm.
- `letterbox(2.39)`, `grade(HALL)` with the amber preserved.

**Keyframe prompt (`p21_terminal`; also the plate of shots 24 and 26):**
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
> Her hands (the woman on the attached sheet): slim fingers and the cuffs of a charcoal ribbed sweater.
> SHOT: a hardware insert at a steel operator's console in the dark hall, seen with a 60 mm lens from a little above the
> operator's eye line and 15 degrees to the right of the screen's axis. A small monochrome terminal tube, deeply curved
> and round-cornered, set back under a hood in a blue-grey hammered-enamel housing, fills the upper two thirds of the
> frame left of centre; its face glows blank, even pale cyan, and the hood's inner edge and the curve of the glass show
> their depth at the left. On the housing's right cheek, at the right of the frame: a round moving-coil meter behind
> frosted glass, lit cold from behind, with a blank arc scale and a black needle resting at zero; below it, a column of
> four small blank rectangular indicator lamps, unlit; at the housing's top right corner, a small red jewel lamp,
> unlit; on top of the housing, a small unit of four black flip-number cards, blank. Along the bottom of the frame, the
> top row of sculpted grey keys with blank cream legends, and at its right end one large square key of translucent red
> resin, unlit; a young woman's fingertips rest lightly on the keys, still. The tube's cold light is the only key: it
> lights the tops of her fingers and the keys as cut shapes. One repair: a strip of newer steel riveted over a crack in
> the hood. Everything else falls into black.

**Refs:** `assets/pilot/lookdev_v3/hall.png`, `assets/pilot/lookdev_v3/ida.png`.
**Layers:** none.

**JS spec (J09 v3 · the Script Terminal: SIGN-OFFS · DESK 4):**
- **Device** (`production_design.md` §4): a 30 cm two-layer (beam-penetration) tube, 48 columns × 12 rows of Operator
  Mono (a 7 × 9 dot matrix in a 9 × 14 cell; each dot a short horizontal dash with a dark gap between scan rows; slashed
  zero; straight apostrophe). The cold layer (high beam voltage: core `#DDFBFA`, bloom `#5FE1E6`, persistence ~60 ms)
  and the warm layer (low voltage: core `#FFD9A0`, bloom `#F2A441`, persistence ~400 ms).
- **The Operator Rule:** every character is coloured by who answers for it. The Engine's lines are cold; anything
  that came in through her keyboard is warm, even when the Engine repeats it. This replaces v1's colour-coded editor
  window, and it is the order's "THE OPERATOR ANSWERS FOR CONTENT" built into the glass.
- **Row 1, the header:** SIGN-OFFS · DESK 4, warm (she typed it), over a faint cold burn-in of the tube's usual header
  (SCRIPT · NIGHT) at 4 %.
- **Columns:** NIGHT ### in cold at half intensity (columns 1–9); the sign-off from column 12. Lines 001–211 are the
  Engine's "Sleep safely." (cold), except, warm and at full intensity:
  - NIGHT 023  Close the window. The wind is sly.
  - NIGHT 047  Don't argue with the rain.
  - NIGHT 061  Old bread makes good soup.
  - NIGHT 088  Leave a light on for whoever comes home late. (it wraps under column 12)
  - NIGHT 119  Call the ones you miss.
  - NIGHT 150 through NIGHT 211, every one: Eat something warm before you sleep. (a solid warm block)
  - The last line is NIGHT 212, with a warm block cursor after it.
- **The scroll** (0.0–6.0 s), from 001 to rest: it runs fast through the cold runs (up to 70 lines a second, the rows
  smearing into streaks), and slows to about 8 lines a second as each warm line crosses the middle row, like a thumb
  easing on the key. **Cold streaks vanish at once; warm streaks linger** (the long persistence), so her lines stay in
  the eye even at speed. From 3.5 s it eases out through the warm block; as it slows, the scroll becomes visible
  one-row jumps with a 1 px bounce.
- **At rest (6.0–8.0 s):** the header, NIGHT 202–211 and NIGHT 212. The block cursor blinks on the film's tick (0.5 s
  on, 0.5 s off).
- **The repeater** on the housing: TO AIR 01:08 → 01:01, one flip per whole second (Flap numerals, as in 06).
- **Tube artefacts:** scanlines (the tube is large in frame), barrel k1 0.05, bloom with a halation ring, faint raster
  breathing, a 6 % reflection of her hands and face in the dark glass, a static dust layer. No misconvergence: this
  tube is monochrome.

**Sound:**
- Soft trackpad scroll ticks at the scroll rate (−40 dB).
- Score 1M3: PAD **Dm** 109–111, **B♭** 111–113, **C** 113–117. Theme **A4** at 110.0, **F4** at 111.0, **G4** at
  112.0, and **E4 at 113.0, held** through the cut (unresolved).
- Hall tone; the hall clock at −4 dB.

*v3 sound note:* there are no trackpads in this world: the ticks are the terminal's scroll relay (dry 1 ms clicks at
the JS scroll rate, same level), thinning as the scroll slows.

**Motion prompt:** n/a (plate, JS and comp).

**Takes:** —
