# Shot 07 — IDA

**Duration:** 4 s (0:37–0:41; abs 37.0–41.0)  **Tool:** Codex k04 + a silent Seedance take (v2) or comp (v1)
**Camera:** medium close-up, 85 mm, 10 cm above her seated eye line (a colleague's eye); locked-off

**Action:** Our first real look at her. Ida works at the Proof, her face cut out of the dark by its cold light, the
light pen raised. She is precise, detached and more tired than anyone should be. She is short-sided: she looks toward
the near edge of the frame, and the dark hall fills the space behind her head, where the small dented amber thermos
stands on the desk, unopened. It is Nana's soup, the one warm thing in the Hall, and she has her back to it. It pays
off in shot 42. **Start pose:** seated, the pen raised toward the tube just off the left edge, eyes on it, mouth
closed.

**Build:**
- Codex **k04**. **Acceptance:** it sets Ida's face for the rest of the film. Check it against the `ida` sheet (the bob
  and bangs, the hoop in her left ear, the scarf and its darn) and retake it if she drifts.
- **v2:** a 4 s silent take: two small touches of the pen toward the glass, then one breath out.
- **v1 fallback:** locked-off; `flicker(mask=cyan_lit, driver=noise(0.8 Hz), 3 %)`, the tube refreshing as she works;
  `dust(20)` in the tube light in front of her. The v1 push-in is gone: no micro-pushes on faces.
- `letterbox(2.39)`, `grade(HALL)`.

**Keyframe prompt (`k04_ida_desk`):**
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
> SHOT: a medium close-up of Ida seated at her desk in the dark hall, seen with an 85 mm lens from her front-left, 10
> cm above her eye line. She faces screen-left toward a large monitor just outside the left edge of the frame; its cold
> pale cyan light is the only key and falls on her face and her raised hand as crisp cut shapes, and everything it does
> not reach falls into black. She holds a slim pen on a coiled cable raised near the left edge, about to touch the
> glass. Her face is composed, her eyes resting on the screen, her mouth closed; her shoulders are a little rounded
> with fatigue. Composition: her head on the left third, turned toward the near edge of the frame, with the dark hall
> filling the right two thirds behind her. There, on the grey enamel desk behind her shoulder, stands a small dented
> amber enamel thermos, chipped to black iron at the rim, unopened; far beyond it, out of focus, the wall of tubes is a
> grid of pale cyan blocks. The scarf and the thermos are the only warm colours.

**Refs:** `assets/pilot/lookdev_v3/ida.png`, `assets/pilot/lookdev_v3/hall.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- Hall clock (38, 39, 40); hall tone and DRONE.
- Two small stylus taps at shot +1.5 and +2.7 (abs 38.5, 39.7).
- A slow exhale at +3.2 (abs 40.2).
- No dialogue.

**Motion prompt (v2, Seedance: start `work/pilot/keys_v3/k04_ida_desk.png`, 4 s, `--no-audio`):** Colour woodcut
print animation; keep the first frame's exact carved shapes, flat inks and designs. Medium close-up, 85 mm, slightly
above her eye line: a young woman seated at a desk in a dark hall faces left toward a monitor just out of frame, lit
cold from the left, a slim pen on a coiled cable in her raised hand. Her head and shoulders stay still. After one
second she touches the pen toward the glass twice, small and precise, a second apart; then she lowers her hand a
little and breathes out once, slowly. Her lips stay closed. Understated performance: her face stays composed; only the
described movements happen. Locked-off camera. No sound.

**Takes:** —
