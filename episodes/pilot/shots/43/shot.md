# Shot 43 — THE EMPTY HALL

**Duration:** 6 s (3:37–3:43; abs 217.0–223.0)  **Tool:** Codex k26 (an edit of k03) + the Wall insert (standby over
the burned-in ghost), then a silent Seedance take (v2) or a comp pull (v1)
**Camera:** the exact framing of 05, played in reverse: back up the nave on rails, at a constant speed. The institution
lets her go.

**Action:** The same wide as when we met her, but the desk is empty and the chair pushed back. She went home. The Wall
shows only the standby card, dim and still, and through it the ghost of his face, burned into 96 tubes by 41 years.
There is no warm colour left in the Hall: it went home with her. Far below, the red phone rings for no one. We pull
away. **Start pose:** the empty hall.

**Build:**
- Codex **k26**, an **edit of k03**. **Acceptance:** the architecture matches k03. Difference-check it; if the edit
  shifted anything, SIFT-align it to k03 and paste back only the edited regions (the desk, the chair, the Wall's
  brightness) with a feathered mask (the v1 lesson: edits change lines outside the edit).
- **The Wall insert:** J15 v3, the standby card, at 50 % and **not** breathing (the broadcast is over), over the
  Father's burned-in ghost (k02 at 5 %), tile by tile as in 05, with the dead tube and the hum bar. The desk's small
  screens are dim. Save as `work/pilot/v3/k26_wall.png`, the comp plate and the Seedance start frame.
- **v2:** a 6 s silent take: the reverse dolly.
- **v1 fallback:** `pull(1.07→1.00, focus=(0.50, 0.66), linear)`, the exact inverse of 05's move, with
  `parallax(near_covers=1.0, plate=0.55)` on a matte cut from k26. `dust(120)`, 30 % slower.
- `letterbox(2.39)`, `grade(HALL)` at −15 % exposure.

**Keyframe prompt (`k26_hall_empty`, an edit of k03):**
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
> EDIT the attached image: remove the woman completely. Her chair is now pushed back from the lit desk and turned
> slightly, empty; the small amber thermos is gone from the desk, and the desk's screens are dim. The whole wall of
> tubes glows a dimmer, deeper cold blue, still blank. The red lamp box above the wall stays dark. Keep everything else
> exactly as it is, aligned pixel for pixel: the hall, the perspective, the covered desks, the piers, the floor, the
> brass tubes, the carving, the inks and the framing.

**Refs:** `work/pilot/keys_v3/k03_hall_wide.png` (the image being edited).
**Layers:** none. v1 reused `k03_fg_desks`; it is cut with the rest.
**JS spec:** J15 v3 (shot 16), still, at 50 %, over the burned-in ghost.

**Sound:**
- **The red phone, far away** in the empty hall: HALL REVERB (6 s), −20 dB, ringing at abs 218.0 and 221.0. After 223
  it is gone.
- Rain on the high roof; the hall tone at −6 dB (the power is off).
- No clock.
- Score: PAD **B♭**, fading −30→−40 dB (1M6).

**Motion prompt (v2, Seedance: start `work/pilot/v3/k26_wall.png`, 6 s, `--no-audio`):** Colour woodcut print
animation; keep the first frame's exact carved shapes, flat inks and designs. An extreme wide view in one-point
perspective from high at the back of a vast dark concrete hall: rows of covered desks lead to a dim wall of television
tubes; on the centre line far below, one desk with its chair pushed back, empty. Nothing moves. Dust drifts slowly in
the dim cold light. The camera travels backward along the centre line at a constant speed, like a camera on rails,
without tilting or turning. No sound.

**Takes:** —
