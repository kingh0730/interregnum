# Shot 03 — "EAT SOMETHING WARM"

**Duration:** 7 s (0:12–0:19; abs 12.0–19.0)  **Tool:** the second half of the opening take (v2), or Codex k02 (an edit
of k01) + comp (v1) (broadcast, 4:3)
**Camera:** the broadcast camera, closer: the take's push continues to the close-up that 04 freezes

**Action:** Closer. "I am well." A long beat. Then a line no statesman says: "Eat something warm before you sleep." It
plays as paternalistic cosiness now and is revealed later as a grandmother's words. The last frame of this shot is the
frozen frame of shot 04. **Start pose:** head and shoulders, eyes on the lens, lips closed.

**Build:**
- **v2:** the second segment of the opening take (prompt in `shots/02/shot.md`): the 7 s starting 0.6 s before the
  voiced onset of "I am well.", so the line lands at +0.6 as in v1. The take ends on k02, its end frame. Export the
  segment's last frame as `work/pilot/v3/f04_frozen.png`.
- Codex **k02**, an **edit of k01**: the same picture reframed as a close-up. It is the canonical frozen face: the end
  frame of the opening take, the freeze in 04, the Proof's picture in 06, the Wall in 05 and 23, the copy's frames in
  the archive (08), and the source of the eyes-closed edit k20.
- **Acceptance:** k02 must read as the same man as k01 (beard, hairline, both large ears, the mole on his left cheek at
  image right) and keep the Copy Rule's smooth finish. It is the most reused image of him, so retake it until it
  matches. The reframe is meant to change the framing; if it also changes his face, retake it.
- **v1 fallback:** k02 with `push(1.00→1.04, focus=(0.50, 0.42), linear)`, frozen at +6.9 s. Export that frame as
  `f04_frozen.png`.
- Both: the 4:3 crop and pillarbox, `broadcast()` with the J14 bug, captions, `grade(BROADCAST)`. No letterbox.

**Keyframe prompt (`k02_father_cu`, an edit of k01):**
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
> copy of a man, and the one image in the film that is not carved. Keep the attached picture's flawless, polished
> studio finish exactly: smooth continuous gradients, soft even light, perfect symmetry, skin with no texture or pores,
> no gouge strokes, no paper grain, no print texture of any kind.
> EDIT the attached image: the same broadcast picture, reframed as a close-up. Show only his head and the top of his
> shoulders, still perfectly centred and symmetrical, his eyes level with the lens and looking straight into it, his
> mouth closed, calm. Both of his large ears are fully visible, and so is the small dark mole high on his left
> cheekbone, on the right side of the picture. The round pale lamp shows as part of a disc behind his head. Keep his
> face, hair, beard, coat, pin, backdrop, light and colours exactly as they are, and keep him inside the middle three
> quarters of the width.

**Refs:** `work/pilot/keys_v3/k01_father_mcu.png` (the image being edited).
**Layers:** none.
**JS spec:** the J14 bug and closed captions, as in shot 02.

**Sound:**
- **FATHER** (`Daniel`, 135, BROADCAST): **"I am well."** at shot +0.6 (abs 12.6); **"Eat something warm before
  you sleep."** at +3.0 (abs 15.0).
- HYMN: **D** 12.0–15.5, **A** 15.5–19.0.
- Broadcast tone.
- The shot ends mid-chord: shot 04 tape-stops the whole mix at 19.0.

**Motion prompt (v2):** one take with shot 02. Its prompt, start frame and end frame are in `shots/02/shot.md`;
generate it once.

**Takes:** —
