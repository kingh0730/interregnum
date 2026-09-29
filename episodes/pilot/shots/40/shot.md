# Shot 40 — "HOW LONG?"

**Duration:** 3 s (3:22–3:25; abs 202.0–205.0)  **Tool:** Codex k28 (a new keyframe, not a punch-in) + a Seedance take
with dialogue (v2) or comp (v1)
**Camera:** a tighter close-up than 38 (the ladder tightens as the truth arrives): 85 mm, 10 cm above her eye line;
locked-off; still short-sided

**Action:** "How long?" Tighter than 38: the world has narrowed to this call. She leans over the desk, the handset at
her ear. At the lower edge of the frame her free hand rests on the desk and slowly closes around the phone cord; that
hand is the whole performance. **Start pose:** leaning forward, the handset at her ear, eyes lowered, mouth closed, the
free hand open on the desk beside the cord.

**Build:**
- Codex **k28**. v1's 1.25× punch-in on k23 was visibly soft, and a soft start frame gives a soft clip.
- **v2:** a 4 s take with the line (audio on); use 3 s. The prompt is `cinematography.md` §8's rewrite, adapted.
- **v1 fallback:** locked-off; `flicker(mask=amber_lit, driver=noise(0.3 Hz), 2 %)`. The red phone is out of frame now,
  but its sound remains.
- `letterbox(2.39)`, `grade(HALL)` with the amber preserved.

**Keyframe prompt (`k28_ida_how_long`):**
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
> SHOT: a tight close-up of Ida, tighter than a close-up, seen with an 85 mm lens 10 cm above her eye line: she leans
> forward over her desk in the dark hall, her head low, three-quarters toward screen-left, and her head and the heavy grey
> handset at her far ear fill the left half of the frame. She holds the handset with her right hand. Her face is
> composed, eyes lowered, mouth closed. At the bottom edge of the frame, her left hand rests open on the desk beside the
> coiled telephone cord. A small amber lamp on the telephone just below the frame lights her cheek, jaw and fingers from
> below as warm cut shapes; the cold of the hall is only a thin rim on the back of her hair. Composition: her face on the
> left third, turned toward the near edge of the frame; the right half of the frame is dark space.

**Refs:** `assets/pilot/lookdev_v3/ida.png`, `assets/pilot/lookdev_v3/hall.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- **IDA** (`Samantha`, 150, IDA hall chain): **"How long?"** at shot +0.8 (abs 202.8). Quiet, the voice almost
  breaking.
- The red phone at abs 203.0 (hall reverb, −12 dB: she has turned away from it); phone-line hiss; warm PAD.

**Motion prompt (v2, Seedance: start `work/pilot/keys_v3/k28_ida_how_long.png`, 4 s, audio on; use 3 s):** Colour
woodcut print animation; keep the first frame's exact carved shapes, flat inks and designs. Close-up, tighter than the
last shot: her head and the handset fill the left half of the frame, three-quarter view facing screen-left. Ida leans
over the desk and holds the grey handset to her ear. She is still. She says quietly, lips barely moving: "How long?"
Then she waits, listening, without moving. At the lower edge of the frame, her free hand rests on the desk and slowly
closes around the phone cord. She speaks in a young woman's low, soft, tired voice with a neutral General American
accent. Understated performance: her face stays composed; only her lips and that hand move. Locked-off camera. The
silence of a vast hall, a telephone far away. No music.

**Takes:** —
