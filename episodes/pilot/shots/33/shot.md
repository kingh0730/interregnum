# Shot 33 — NANA LISTENS

**Duration:** 6 s (2:54–3:00; abs 174.0–180.0)  **Tool:** Codex k19 + a silent Seedance take (v2) or comp (v1)
**Camera:** close-up, 50 mm at her eye level, from beside the television (she faces it, so she faces us, just past the
lens); locked-off

**Action:** Nana holds her mug under her chin, the television's light full on her face. From its small speaker: "Eat
something warm before you sleep." It is the line she has waited up for all night, and it is her own. The corners of
her mouth lift, very slightly; that is all. Three notes of her theme begin, and then the dead air cuts them off.
**Start pose:** the steaming mug under her chin, eyes on the television, mouth closed.

**Build:**
- Codex **k19**.
- **v2:** a 6 s silent take: steam, and after the line the corners of her mouth lift. The Father's line comes from the
  address take's audio (TV chain).
- **v1 fallback:** locked-off; `flicker(mask=cyan_lit, driver=the broadcast's luma + noise(0.4 Hz), 3 %)`;
  `steam(the mug)` as a pale cut ribbon rising slowly. No push, no rainshadow.
- `letterbox(2.39)`, `grade(HOME)`.

**Keyframe prompt (`k19_nana_listens`):**
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
> SHOT: a close-up of Nana in her armchair at night, seen with a 50 mm lens at her eye level from beside her
> television: she faces almost toward the camera, her eyes resting on the screen just to the right of the lens. She
> holds her thick chipped mug in both hands just under her chin, and a thin ribbon of steam rises from it as a pale cut
> shape. The cold pale cyan light of the television falls full on her face and hands from the front as crisp cut
> planes; behind her shoulder at the left, the pleated lampshade glows amber and cuts an amber rim along her hair and
> one cheek. Her face is calm and still, mouth closed. Composition: her face left of centre, her eyes on the upper
> third, the dark room behind her.

**Refs:** `assets/pilot/lookdev_v3/nana.png`, `assets/pilot/lookdev_v3/flat.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- **FATHER** (`Daniel`, 135, TV chain: a small speaker in the room): **"Eat something warm before you sleep."** at
  shot +0.8 (abs 174.8).
- Room tone; rain on glass; Nana's clock; TV hum.
- Score: a warm PAD F(add9) at −38 dB from 176.0. Theme **A4 177.6, F4 178.4, G4 179.2**, then cut at 180.0 (the dead
  air). No phone here.

**Motion prompt (v2, Seedance: start `work/pilot/keys_v3/k19_nana_listens.png`, 6 s, `--no-audio`):** Colour woodcut
print animation; keep the first frame's exact carved shapes, flat inks and designs. Close-up at her eye level from
beside a television: an old woman holds a mug under her chin in both hands, her face lit by the television's cold
light, a lamp glowing amber behind her. A thin ribbon of steam rises from the mug. For three seconds she does not move,
her eyes on the television. Then the corners of her mouth lift very slightly, and she stays that way. Understated
performance: her face stays composed; only the corners of her mouth move. Locked-off camera. No sound.

**Takes:** —
