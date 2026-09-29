# Shot 27 — THE KEY

**Duration:** 4 s (2:25–2:29; abs 145.0–149.0)  **Tool:** Codex k16 + a silent Seedance take (v2) or a comp push (v1)
**Camera:** macro, 60 mm, at the operator's eye line; a push onto the fingertip, accelerating, then a hard cut

**Action:** Her index finger over the commit key: a square of translucent red resin lit from inside, the Lamp engraved
in its face. "Ten seconds." The phone rings, the pulse thuds, the hum rises. The finger comes down a few millimetres
and stops just above the key. We cut to black before it falls: the press happens in the cut. **Start pose:** the
finger above the key, not touching.

**Build:**
- Codex **k16**.
- **v2:** a 4 s silent take: the push, and the finger lowering a little and stopping. It never presses.
- **v1 fallback:** `push(1.00→1.06, focus=fingertip, easeInQuad)`.
- Both: the key's red pulses +15 % on each whole second, decaying over 0.4 s (the key is one flat red shape, so its
  mask is trivial). If the engraved emblem comes out wrong, lay the Lamp over it in comp (engraved, lit from within).
- `letterbox(2.39)`, `grade(HALL)`. **Hard cut at 4.0 to shot 28**, with no fade.

**Keyframe prompt (`k16_commit_key`):**
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
> Her hand (the woman on the attached sheet): a slim index finger and the cuff of a charcoal ribbed sweater.
> SHOT: a macro close-up at the operator's eye line with a 60 mm lens: the right end of an old keyboard of sculpted grey
> keys with blank cream legends, set in a blue-grey enamel console worn to bare metal along its edge. Right of centre,
> one large square key of translucent red resin, lit from inside, glows signal red, with a small emblem engraved in its
> face: a ring around a pointed flame on a short bar. A young woman's index finger enters from the upper left and
> hovers just above the key, not touching, its tip lit red from below; the rest of her hand is in shadow. A thin edge of
> cold pale cyan light from a screen above cuts the top of her finger. Everything else falls into black. Composition:
> the key right of centre, the fingertip just above it.

**Refs:** `assets/pilot/lookdev_v3/hall.png`, `assets/pilot/lookdev_v3/ida.png`.
**Layers:** none.
**JS spec:** none (the engraved Lamp is a comp fix only if needed).

**Sound:**
- **PA** (`Karen`, 165, PA chain): **"Ten seconds."** at shot +0.3 (abs 145.3).
- The red phone ring at abs 146.0; PULSE (loudest now); the hall clock.
- RISER peaking at 149.0.
- **At 4.0 (abs 149.0): HARD CUT, and every stem goes silent** (0.3 s).

**Motion prompt (v2, Seedance: start `work/pilot/keys_v3/k16_commit_key.png`, 4 s, `--no-audio`):** Colour woodcut
print animation; keep the first frame's exact carved shapes, flat inks and designs. A macro close-up of a woman's index
finger held just above a large square red key that glows from inside. The finger stays still for two seconds; then it
lowers a few millimetres and stops just above the key, without touching it. The camera moves in toward the fingertip,
slowly at first and then faster. No sound.

**Takes:** —
