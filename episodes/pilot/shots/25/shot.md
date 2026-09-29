# Shot 25 — HER EYES

**Duration:** 3 s (2:13–2:16; abs 133.0–136.0)  **Tool:** Codex k15 + a silent Seedance take (v2) or comp (v1)
**Camera:** extreme close-up of her eyes, 85 mm, just above her eye line; locked-off

**Action:** Her eyes, lowered to the keys, lit from below by her own screen. The red telephone rings somewhere in the
hall, and she doesn't look away. The cut to her also covers time: she types the two lines we'll see in 26 while we are
on her. v1's wet eyes, the tear and the text reflected in her eyes are gone: in RELIEF eyes carry no highlights, and a
keyframe never shows tears. Her eyes read the line, blink once, and do not lift. The ring and the cut do the rest.
**Start pose:** eyes lowered to the keyboard, face composed.

**Build:**
- Codex **k15**.
- **v2:** a 4 s silent take (use 3 s): the eyes read along the line and blink once.
- **v1 fallback:** locked-off; the screen's light moves on her face as she types: a few soft horizontal bands on the
  cyan-lit mask (the terminal's rows as light, one of them amber), rising 20 px over the shot.
- `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (`k15_ida_eyes`):**
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
> SHOT: an extreme close-up of Ida's eyes and the bridge of her nose, framed from her brows to just below her eyes across
> the width of the frame, the straight black line of her bangs along the top edge; seen with an 85 mm lens just above her
> eye line, her face three-quarters toward screen-left. Her eyes are lowered to a keyboard below the frame; they are
> small dark almond shapes without any highlight. The cold pale cyan light of a small screen below cuts her lower lids,
> the underside of her brow ridge and the side of her nose as crisp shapes; the rest falls into black. Her face is
> composed and still. Composition: her eyes across the left two thirds of the frame; the right third is her temple and
> hair falling into black.

**Refs:** `assets/pilot/lookdev_v3/ida.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- The red phone ring at +1.0 (abs 134.0), in the hall reverb.
- PULSE; the hall clock; muffled keystrokes (−10 dB) at an irregular typing rhythm under the shot. She is typing the
  two lines we'll see in 26.
- **RISER starts at 0.0 (abs 133.0)** and runs to 149.0.
- No dialogue.

**Motion prompt (v2, Seedance: start `work/pilot/keys_v3/k15_ida_eyes.png`, 4 s, `--no-audio`; use 3 s):** Colour
woodcut print animation; keep the first frame's exact carved shapes, flat inks and designs. An extreme close-up of a
young woman's eyes, lit from below by a small screen, lowered to a keyboard. Her head does not move. Her eyes move along
a line from left to right, and again, as she reads what she types; then her eyelids lower once in a slow blink and
lift. She does not look up. Understated performance: only her eyes and eyelids move. Locked-off camera. No sound.

**Takes:** —
