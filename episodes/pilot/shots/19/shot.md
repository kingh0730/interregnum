# Shot 19 — THE QUESTION

**Duration:** 4 s (1:39–1:43; abs 99.0–103.0)  **Tool:** Codex k12 + a Seedance take with dialogue (v2) or comp (v1)
**Camera:** close-up, one size tighter than 17: 85 mm, 10 cm above her eye line; locked-off. Short-sided.

**Action:** Ida lifts her eyes toward the face she makes every night, high and far away on the Wall, and asks the
question she has been carrying: "Why do you still watch him?" The eyes move; nothing else does. **Start pose:** the
handset at her ear, eyes lowered, mouth closed.

**Build:**
- Codex **k12**.
- **v2:** a 4 s take with the line (audio on).
- **v1 fallback:** locked-off; `flicker(mask=cyan_lit, driver=noise(0.5 Hz), 2 %)`. No push.
- `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (`k12_ida_question`):**
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
> SHOT: a close-up of Ida in the dark hall, seen with an 85 mm lens 10 cm above her eye line: her head and shoulders,
> three-quarters toward screen-left. The heavy grey handset of a desk telephone is at her far ear, held in her right
> hand, and its coiled cord runs down across her chest. Her eyes are lowered, her face composed, mouth closed. The cold
> pale cyan light of the great wall of screens far away at the left cuts her face as crisp planes, and a thin cold rim
> runs along the back of her hair. Composition: her face on the left third, turned toward the near edge of the frame,
> with dark space behind her head at the right; her amber scarf at the bottom edge.

**Refs:** `assets/pilot/lookdev_v3/ida.png`, `assets/pilot/lookdev_v3/hall.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- **IDA** (`Samantha`, 165, IDA hall chain): **"Why do you still watch him?"** at shot +0.6 (abs 99.6).
- Phone-line hiss; hall tone; the hall clock at −4 dB; warm PAD (Dm from 100.0).
- **PLUCK A4** (Nana's theme, note 1) at +3.6 (abs 102.6): the question hangs.

**Motion prompt (v2, Seedance: start `work/pilot/keys_v3/k12_ida_question.png`, 4 s, audio on):** Colour woodcut print
animation; keep the first frame's exact carved shapes, flat inks and designs. Close-up, 85 mm, slightly above her eye
line: a young woman in a dark hall holds a grey telephone handset to her ear, facing left, lit cold from the left, her
eyes lowered. Her head does not move. She lifts her eyes toward something high and far away at the left, and as they
settle she says quietly, at a slow pace: "Why do you still watch him?" Then she keeps her eyes there without moving.
She speaks in a young woman's low, soft, tired voice with a neutral General American accent. Understated performance:
her face stays composed; only her eyes and lips move. Locked-off camera. The low hum of a large hall. No music.

**Takes:** —
