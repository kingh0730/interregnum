# Shot 18 — NANA ANSWERS

**Duration:** 5 s (1:34–1:39; abs 94.0–99.0)  **Tool:** Codex k11 + a Seedance take with dialogue (v2) or comp (v1)
**Camera:** close-up, 50 mm, level with her eyes at 1.1 m (a guest's eye); locked-off. Nana faces screen-right with
lead room: the mirror of Ida.

**Action:** Nana, the handset at her ear, her face split between the television's cold and the lamp's amber, the two
inks meeting along the ridge of her nose. The whole film meets on her face. "I always wait up. He's on soon." Is she
waiting for Ida or for him? Both. **Start pose:** the handset at her ear, eyes on the television off-frame, mouth
closed, about to speak.

**Build:**
- Codex **k11**. **Acceptance:** it sets Nana's face for 20, 33, 39 and 41. Check it against the `nana` sheet and B2,
  and retake if she drifts. It is one of the three keyframe tests (`assets/pilot/lookdev.md`).
- **v2:** a 5 s take with the line (audio on).
- **v1 fallback:** locked-off; `flicker(mask=cyan_lit, driver=J15 luma, 4 %)` on the television side. v1's rainshadow
  is dropped: the window is too weak to cast it, and soft moving shadows would fight the print.
- `letterbox(2.39)`, `grade(HOME)`.

**Keyframe prompt (`k11_nana_answers`):**
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
> NANA (the woman on the attached sheet): 82, small; silver-white hair in a low bun held with a dark wooden pin; a soft
> round face with deep lines; small dark eyes behind thin round gold wire glasses; warm brown skin; small pearl
> earrings; a dark bottle-green hand-knitted cardigan, near-black in shadow, over a cream blouse with a small lace
> collar.
> SHOT: a close-up of Nana seated in her armchair at night, seen with a 50 mm lens level with her eyes. Her face is
> turned three-quarters toward screen-right, her eyes resting on a television out of frame at the right. She holds the
> cream bakelite handset of her telephone to her far ear with her left hand, and its coiled cord hangs down across her
> cardigan. Her face is calm and still, mouth closed, about to speak. Two lights meet on her face: cold pale cyan from
> the television at the right and amber from a table lamp at the left, the two inks meeting along the ridge of her nose,
> never mixed. Behind her at the left edge, the pleated parchment lampshade, scorched brown on one side, throws a crisp
> arc of amber light up the faded leaf wallpaper; beside the arc, a pale, unfaded rectangle where a picture once hung.
> The low ceiling is dark. Composition: her face on the left third with open dark space in front of her toward the
> right; her eyes on the upper third.

**Refs:** `assets/pilot/lookdev_v3/nana.png`, `assets/pilot/lookdev_v3/flat.png`.
**Layers:** none.
**JS spec:** none. The flicker's driver is J15's luminance curve.

**Sound:**
- **NANA** (`Moira`, 150, NANA chain): **"I always wait up. He's on soon."** at shot +0.4 (abs 94.4).
- Room tone; rain on glass; Nana's clock; the TV's faint stand-by tone; phone-line hiss; warm PAD.

**Motion prompt (v2, Seedance: start `work/pilot/keys_v3/k11_nana_answers.png`, 5 s, audio on):** Colour woodcut print
animation; keep the first frame's exact carved shapes, flat inks and designs. Close-up, 50 mm, at her eye level: an
old woman in an armchair holds a cream telephone handset to her ear, her face turned toward a television off-screen at
the right, lit by its cold light on one side and by a lamp's amber on the other. Her eyes rest on the television
throughout. She says lightly, at an easy pace: "I always wait up. He's on soon." After the line she gives one small
nod and is still. She speaks in an old woman's gentle, slightly thin, warm voice with a neutral General American
accent. Understated performance: her face stays composed; only her lips and that nod move. Locked-off camera. Rain on
the window, a wooden clock ticking. No music.

**Takes:** —
