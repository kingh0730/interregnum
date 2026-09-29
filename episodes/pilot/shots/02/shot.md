# Shot 02 — THE FATHER

**Duration:** 7 s (0:05–0:12; abs 5.0–12.0)  **Tool:** Codex k01 + the opening Seedance take (one take for 02 and 03)
in v2, or comp on k01 in v1 (broadcast, 4:3)
**Camera:** the broadcast camera: a centred medium close-up, with the take's slow mechanical push that carries on
through 03

**Action:** The Father, dead-centre, looks into the lens and greets the nation. After the worn, carved film of the
Lighting, the picture changes material: this is the only smooth image in the film (the Copy Rule), and the audience
should feel the change before they understand it (shot 04 explains it). He is a portrait that has learned to talk:
warm, reassuring and slightly wrong. **Start pose:** seated upright and square to the lens, mouth closed, calm, about
to speak.

**Build:**
- Codex **k01**, under the Copy Rule. It is the start frame of both of the Father's takes (02–03 and the address,
  29–34), so check it hardest: smooth, centred, and resembling no real person.
- **v2 (the broadcast lesson):** shots 02 and 03 are **one continuous take** from k01, cut in two like the final
  address. Generate 15 s ending on k02 (`--end`), so the take's slow push lands exactly on the close-up that shot 04
  freezes. 02 = take 0.0–7.0. 03 = the 7 s starting 0.6 s before the voiced onset of "I am well.". The skip between the
  two segments is hidden by the cut to the closer framing. If the end frame makes the push morph, drop `--end` and use
  the take's own last frame for 04.
- **v1 fallback:** k01 with `push(1.00→1.035, focus=(0.50, 0.40), linear)` (the broadcast camera moves like a machine)
  and luma breathing ±1.5 % at 0.3 Hz.
- Both: crop the centre 4:3 of the 16:9 source and pillarbox it to 1440×1080, then `broadcast()` with the J14 bug,
  closed captions inside the signal, `grade(BROADCAST)`. No letterbox.
- **A plant:** a one-frame stutter at shot +4.2 s. Hold the previous frame for 2 frames, then give one frame a 3 px
  horizontal offset on one 120 px-high slice across the mouth. It is barely perceptible.

**Keyframe prompt (`k01_father_mcu`):**
> STYLE (RELIEF): a frame from an animated film printed by hand as a colour woodcut and linocut on warm cream paper. A
> carved blue-black key block holds the image; large areas stay solid black, with faint wood grain. Every surface (skin,
> cloth, hair, concrete, metal, glass, floor) is matte printed ink: no reflections, no sheen, no specular highlights, no
> smooth gradients. Light is a shape cut out of the black with crisp, slightly irregular knife edges. Middle tones
> everywhere, on walls, floors and machines as on faces, are parallel gouge strokes that follow the form. Colour is flat
> spot ink, never blended, with paper grain showing through: pale cold cyan where screens light things, amber where lamps
> light things, signal red only on red objects. Slight misregistration; no drawn outlines. Only screen light is soft.
> Faces are a few carved planes, calm; eyes are small dark shapes without highlights. Avoid: anime, airbrush, digital
> painting, 3D render, photorealism, lens flare, bokeh, neon, glossy or wet floors.
> COPY RULE (for this image only, it overrides the style above): this is the broadcast picture itself, the machine's
> copy of a man, and the one image in the film that is not carved. Paint it as a flawless, polished digital studio
> portrait: smooth continuous gradients, soft even light with no hard shadows, perfect symmetry, skin with no texture
> or pores, no gouge strokes, no paper grain, no print texture of any kind. Use the attached sheet only for who he is
> (his face, hair, beard, ears, coat and pin), not for its carved style.
> FRAME: wide 16:9, of which only the central 4:3 will be used: keep him and everything important inside the middle
> three quarters of the width. No text, letters, numbers or logos anywhere.
> THE FATHER (the man on the attached sheet), an invented man who resembles no real person: about 85; a broad, round
> face with a broad nose; thick white hair brushed back in soft waves from a high forehead; heavy white brows; a short,
> full, rounded white beard; deep-set eyes under heavy lids; large ears with long lobes; a small dark mole high on his
> left cheekbone (on the right side of the picture); weathered warm-tan skin; a charcoal wool coat with a soft collar
> rolled around the neck, hidden fastenings and no buttons, pockets, medals or insignia; one small round silver pin on
> the left side of the collar, a ring around a pointed flame.
> SHOT: a television address from a studio, seen with a 100 mm lens at his eye level: a medium close-up from mid-chest
> up, perfectly centred and symmetrical, his eyes on the upper-third line, with calm headroom. He sits upright, square
> to the lens, and looks straight into it; his face is calm and kind, mouth closed, about to speak; his shoulders are
> level and his hands out of frame. Behind him is a deep blue studio backdrop, and centred behind his head a large round
> diffuser lamp: a pale disc of soft light with its rim faintly visible, like a full moon. The light is a soft, even
> frontal key and a cool pale rim on his hair and shoulders, with no shadows anywhere. He is perfectly still, a portrait
> about to speak.

**Refs:** `assets/pilot/lookdev_v3/father.png` (identity only).
**Layers:** none.

**JS spec (J14 v3 · the broadcast bug, and J17 closed captions; both live inside the signal):**
- **Device:** the broadcast chain's caption generator, keyed into the picture. Everything it makes is cropped,
  scanlined and bloomed with the 4:3 picture; nothing is laid over the master frame.
- **The Mosaic Lamp:** the Lamp (ring, flame, base) rebuilt on an 8 × 8 grid of soft-cornered square blocks (7 px with
  1 px gaps, 63 px overall), white `#F4F4EE`, keyed with a 1-block black edge, at 70 %. Top-left of the picture, at
  (304, 56) in the master (64 px in from the picture's edge). The state's sacred sign in its crudest copy.
- **LIVE:** Caption Mosaic (a 5 × 7 grid of soft-cornered blocks; block 4 px, cap height 28 px, 1-block spacing),
  white keyed with a 1-block black edge, at 70 %. Bottom-right of the picture: right edge at x 1616, baseline at y 1024.
- **Closed captions:** each line in Caption Mosaic (block 5 px), white letters on black cells (every character cell a
  black block), centred at y 950, scanlined with the picture. They replace v1's Menlo box.

**Sound:**
- **FATHER** (`Daniel`, rate 135, BROADCAST chain): **"Good evening, my children."** at shot +0.6 (abs 5.6);
  **"The harvest is in. The sea is calm."** at +3.0 (abs 8.0).
- HYMN progression (1M1): **D** 5.0–8.5, **G** 8.5–12.0, at −26 dB under the voice.
- Broadcast studio tone. No clock (we are inside the television).
- Give the 4.2 s stutter a 1-frame digital tick at −36 dB.

**Motion prompt (v2, Seedance: the opening take for 02 and 03; start `work/pilot/keys_v3/k01_father_mcu.png`, `--end
work/pilot/keys_v3/k02_father_cu.png`, 15 s, audio on):** A smooth, polished television broadcast picture; keep the
first frame's exact face, soft even light and colours. A medium close-up of an elderly man, perfectly centred, looking
straight into the lens against a deep blue backdrop with a round pale lamp behind his head. One continuous take. He
speaks directly into the lens, slowly, with long pauses between lines: "Good evening, my children." (pause) "The
harvest is in. The sea is calm." (a long pause) "I am well." (a long pause) "Eat something warm before you sleep."
Between lines his face does not move: minimal head movement, one slow blink, an almost unnaturally smooth stillness.
After the last line he keeps looking into the lens without moving. The camera pushes in very slowly at a constant
speed, from medium close-up to close-up, and stays centred on his eyes. He speaks in a deep, slow, resonant old man's
voice with a neutral General American accent, warm and grandfatherly, with measured broadcast pacing. Soft studio room
tone. No music.

**Takes:** —
