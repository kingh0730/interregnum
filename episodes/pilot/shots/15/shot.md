# Shot 15 — THE CITY

**Duration:** 7 s (1:17–1:24; abs 77.0–84.0)  **Tool:** Codex k08 + comp (window breathing, rain, water, beacon); an
optional silent Seedance take for the rain and the water
**Camera:** 300 mm from across the canal, 40 m up at the height of Nana's floor (a neighbour's eye); locked

**Action:** The city in rain. Across a black canal the towers are compressed into one wall, and hundreds of windows
glow the same cold blue: every television shows the standby card and waits for him. The windows breathe together, in
time with the card. One window is warm, on the camera's own horizon line, and the frame holds still with the city so
that we find it ourselves. Far off, a red beacon blinks on the Transmitter. **This composition returns at dawn (shot
44)**, when the warmth spreads from this window across the city. **Start pose:** the city in the rain.

**Build:**
- Codex **k08**. **Acceptance:** every window is a separate cut shape bounded by dark mullions (they are masked for
  shot 44), and there is exactly one amber window, on the horizon line at the right third.
- **Window mask:** luminance blobs on the facade grid, not a hue threshold (`production_design.md` §8), then
  connected components. Save to `work/pilot/v3/k08_windows.npz` for shot 44.
- **Comp (primary):** all cyan windows breathe together, ±6 % luma at 0.25 Hz, in phase with the standby card's
  breathing on the televisions; the amber window stays steady. `rain(layers=2)` drawn as carved cut lines, pale and
  thin, visible only where they cross light (multiply the rain's alpha by the plate's luminance). The canal's cyan cuts
  shift slowly sideways (a subtle horizontal displacement). The Transmitter's beacon blinks red every 2 s (0.3 s on).
- **v2 (optional):** a 7 s silent take for the rain and the water; the breathing and the beacon go on top in comp.
- The camera is locked: v1's truck and push are gone. `letterbox(2.39)`, `grade(CITY)`.

**Keyframe prompt (`k08_city_night`):**
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
> SHOT: the City at night in heavy rain, seen with an extreme long lens (300 mm) from across a canal, 40 metres up at the
> height of the fourteenth floor, so the towers are compressed into one wall. Identical sixteen-storey slab towers of
> board-formed concrete, carved with horizontal bands, stand stacked one behind another up to the top of the band; each
> slab ends in a rounded stair tower with a vertical slot of glass blocks glowing cold. Their facades are strict grids
> of hundreds of small windows, each a separate cut shape bounded by dark mullions; almost every window glows the same
> cold pale cyan from a television inside, brightest at the sill, with a curtain edge or a plant's silhouette in a few.
> Exactly one window glows warm amber from a lamp: in the nearest tower, on the camera's horizon line, at the right
> third of the frame. Residents' repairs: glazed-in balconies with mismatched frames, a pane painted over, laundry
> lines. Rain falls as fine slanted cut lines, visible only where it crosses light. Along the foot of the frame, a
> concrete embankment with an iron railing and solid black canal water, broken by short horizontal cuts of cyan beneath
> the lit windows. Far off between two towers, a thin lattice mast carries one small red lamp. Mercury street lamps on
> concrete posts along the embankment give a cold blue-green light; there is no orange light anywhere. At least half of
> the image is solid black.

**Refs:** `assets/pilot/lookdev_v3/city.png`.
**Layers:** none. v1's `k08_fg_tower` is cut: the camera no longer moves here, and 44 cuts its matte from the plate.
**JS spec:** J15 v3, the standby card, drives the breathing (its luminance curve); it is not inserted here.

**Sound:**
- City rain in wide stereo; canal lapping.
- **Tram bell** at shot +2.0 and +2.6 (abs 79.0, 79.6), distant.
- **City stand-by chime** at +3.0 (abs 80.0): the CHIME smeared through a 4 s reverb, as if from a thousand
  televisions at once.
- Score 1M3: the warm PAD (F) fades in from +5.0 (abs 82.0).
- No hall clock.

**Motion prompt (v2, optional, Seedance: start `work/pilot/keys_v3/k08_city_night.png`, 7 s, `--no-audio`):** Colour
woodcut print animation; keep the first frame's exact carved shapes, flat inks and designs. An extreme long-lens night
view across a canal to a wall of identical tower blocks in heavy rain. Hundreds of windows glow the same cold blue, and
one window glows warm amber. The buildings and every window stay exactly as they are. Rain falls in fine slanted lines,
and the short cuts of light on the black canal break and shift slowly. Locked-off camera. No sound.

**Takes:** —
