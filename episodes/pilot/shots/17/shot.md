# Shot 17 — IDA CALLS

**Duration:** 4 s (1:30–1:34; abs 90.0–94.0)  **Tool:** Codex k10 + a Seedance take with dialogue (v2) or comp (v1)
**Camera:** medium close-up, 85 mm, 10 cm above her eye line; locked-off. Ida faces screen-left, short-sided.

**Action:** Ida has turned her chair away from her screens and holds the House Line's grey handset to her ear, its
coiled cord running down across her chest to the desk: the line to Nana, crossing the frame. Private, shoulders drawn
in. "Nana. Don't wait up tonight." A warning she doesn't explain; it plants the danger. **Start pose:** the handset at
her ear, eyes lowered, mouth closed, about to speak.

**Build:**
- Codex **k10**. The smartphone of v1 is gone: this world has only the House Line, a grey rotary desk phone
  (`production_design.md` §4).
- **v2:** a 4 s take with the line (audio on).
- **v1 fallback:** locked-off; the Wall behind her drifts 2 % in brightness (slow noise), with
  `flicker(mask=cyan_lit, driver=noise(0.5 Hz), 2 %)`. No push.
- `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (`k10_ida_calls`):**
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
> SHOT: a medium close-up of Ida at her desk in the dark hall, seen with an 85 mm lens 10 cm above her eye line. She has
> turned her chair away from her screens and faces screen-left, her shoulders drawn in. She holds the heavy grey handset
> of a desk telephone to her far ear with her right hand, and its coiled cord loops down across her chest to the desk
> below the frame. Her eyes are lowered, her face composed, mouth closed, about to speak. The cold pale cyan light of a
> great wall of screens far away at the left lights her face in crisp cut planes; the screens behind her cut a thin
> cold rim along her hair and shoulder. Composition: her head on the left third, turned toward the near edge of the
> frame; behind her head, dark space and the soft glow of her desk's screens at the right.

**Refs:** `assets/pilot/lookdev_v3/ida.png`, `assets/pilot/lookdev_v3/hall.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- **IDA** (`Samantha`, 165, IDA hall chain): **"Nana. Don't wait up tonight."** at shot +0.5 (abs 90.5).
- Phone-line hiss bed; hall tone; the hall clock (quieter, −4 dB); warm PAD.

**Motion prompt (v2, Seedance: start `work/pilot/keys_v3/k10_ida_calls.png`, 4 s, audio on):** Colour woodcut print
animation; keep the first frame's exact carved shapes, flat inks and designs. Medium close-up, 85 mm, slightly above
her eye line: a young woman at a desk in a dark hall, turned away from her screens and facing left, holds a grey
telephone handset to her ear, its coiled cord across her chest. Her eyes are lowered to the floor in front of her. Her
head does not move. After half a second she says quietly, lips barely moving: "Nana. Don't wait up tonight." Then she
stays still, listening. She speaks in a young woman's low, soft, tired voice with a neutral General American accent.
Understated performance: her face stays composed; only her lips move. Locked-off camera. The low hum of a large hall.
No music.

**Takes:** —
