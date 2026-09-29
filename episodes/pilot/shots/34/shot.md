# Shot 34 — EYES CLOSE

**Duration:** 6 s (3:00–3:06; abs 180.0–186.0)  **Tool:** the end of the address take (v2), or Codex k02 and k20 (an
edit of k02) with the film's one dissolve (v1) (broadcast, 4:3)
**Camera:** the broadcast camera's close-up, the push arriving and holding

**Action:** The Father looks at us a moment longer. Then, slowly, he closes his eyes, and he does not open them. The
broadcast holds on him in dead air, and the hall clock, which has ticked since 0:21, stops. After 212 nights the old
man is finally allowed to die, and the stillness we have watched all film becomes what it always was.
**Start pose:** eyes open, as k02. **End:** eyes closed, as k20.

**Build:**
- **v2:** the address take (prompt in `shots/29/shot.md`) from the end of the last line to its end, then hold the last
  frame (eyes closed) to fill 6 s, as v2 did. The take can end exactly on k20 through `--end` (see shot 29). There is no
  dissolve in v2: he closes his eyes in the take, and 33 cuts straight into it.
- Codex **k20**, an **edit of k02**. **Acceptance:** everything except the eyelids matches k02. Difference the two
  images; changes outside the eye region must be negligible. If Codex shifts the picture, SIFT-align it and paste back
  only the eye region with a feathered mask (the v1 lesson: edits change lines outside the edit).
- **v1 fallback,** at push 1.04 → 1.06 over the whole shot:
  - 0.0–1.0 s: k02, eyes open.
  - **1.0–2.5 s: dissolve k02 → k20** (easeInOutSine) with a subtle 3 % luma dip at the midpoint. It is the only
    dissolve in the film.
  - 2.5–6.0 s: hold k20.
- Both: `broadcast()` with the J14 bug; at 5.6 s LIVE blinks out and the Mosaic Lamp stays. `grade(BROADCAST)`. 4:3,
  no letterbox. Hard cut at 6.0. After this shot the film never returns to 4:3, except in the alt tail.

**Keyframe prompt (`k20_father_eyes_closed`, an edit of k02):**
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
> EDIT the attached image: close the old man's eyes gently, as if he has fallen asleep: the lids relaxed, the lashes
> down, his expression the same calm one, his mouth closed. Change nothing else at all: the same face, hair, beard,
> ears, mole, coat, pin, backdrop, lamp, light, framing and colours, aligned pixel for pixel with the original.

**Refs:** `work/pilot/keys_v3/k02_father_cu.png` (the image being edited).
**Layers:** none.
**JS spec:** the J14 bug (shot 02), with LIVE removed at 5.6 s.

**Sound:**
- **At 0.0 (abs 180.0): dead air.** All music stops mid-phrase (Nana's theme is cut after G4). **The hall clock
  stops; its last tick was at 179.0.**
- Only broadcast hiss at −50 dB for the whole shot. There is no dialogue.
- Pre-lap at 5.8: nothing. Let the silence be complete.

**Motion prompt (v2):** the end of the address take; its prompt is in `shots/29/shot.md`. Generate it once.

**Takes:** —
