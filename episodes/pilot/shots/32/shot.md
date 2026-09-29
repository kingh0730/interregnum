# Shot 32 — IDA LOOKS UP

**Duration:** 6 s (2:48–2:54; abs 168.0–174.0)  **Tool:** Codex k18 + a silent Seedance take (v2) or a comp pull (v1)
**Camera:** 50 mm, 6 m up in front of her, looking down: the Wall's own point of view. It **pulls back** on rails at a
constant speed, the only pull-back before the ending: the world widening.

**Action:** From the Wall's height, looking down: Ida at her desk, lit by his face, hears her own words come out of
him, huge, filling the building: "Tomorrow, you'll have to talk to each other." For the nation it means there will be
no more addresses. For her it means Nana: the two of them have only talked through him. She does not move. The camera
pulls away and the covered desks widen around her, and the red phone rings on. **Start pose:** seated, face tilted up
toward the Wall (just above the lens), hands on the keyboard, mouth closed.

**Build:**
- Codex **k18**.
- **v2:** a 6 s silent take: the pull. The Father's line comes from the address take's audio (HALL chain).
- **v1 fallback:** `pull(1.06→1.00, focus=Ida's face, linear)`; `flicker(mask=cyan_lit, driver=constant +
  noise(0.3 Hz), 2 %)`, since she is lit by the giant wall; `dust(60)` falling slowly through the top light.
- `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (`k18_ida_from_wall`):**
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
> SHOT: seen from 6 metres up in front of her with a 50 mm lens, looking down, as if from the wall of screens: Ida sits
> at her lone lit desk in the dark hall, her face tilted up toward a point just above the camera, composed and still,
> mouth closed. Her hands rest on the keyboard. The cold pale cyan light of the great wall falls on her from above and
> in front: it cuts her upturned face, her hands and the top of the desk as crisp shapes, and throws the shadow of her
> head back across the desk. On the desk, seen from above: the hooded monitors, the grey telephone, the small dented
> amber thermos. Around her in the darkness, the rows of desks under fitted canvas covers laced with cord stand like
> pale stones, and the floor between them is matte black ink with straight gouge strokes and thin pale inlaid lines.
> Composition: Ida low in the frame and left of centre, a small figure with a great deal of dark space around her.

**Refs:** `assets/pilot/lookdev_v3/ida.png`, `assets/pilot/lookdev_v3/hall.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- **FATHER** (`Daniel`, 135, HALL chain: huge, from the wall, 6 s reverb): **"Tomorrow, you'll have to talk to each
  other."** at shot +0.6 (abs 168.6).
- The red phone rings at abs 170.0 and 173.0 (hall reverb, −12 dB).
- The hall clock ticks (its last minutes).
- Hall tone. No music.

**Motion prompt (v2, Seedance: start `work/pilot/keys_v3/k18_ida_from_wall.png`, 6 s, `--no-audio`):** Colour woodcut
print animation; keep the first frame's exact carved shapes, flat inks and designs. Seen from high in front of her: a
young woman sits at her lone lit desk in a vast dark hall, her face tilted up toward a point above the camera, lit cold
from above. She does not move, and her hands stay on the keyboard. Dust falls slowly through the light. The camera moves
straight back and up at a constant speed, like a camera on rails, so that the rows of covered desks widen around her
and she grows smaller. Understated performance: she stays completely still. No sound.

**Takes:** —
