# Shot 39 — "I KNOW, LOVE."

**Duration:** 4 s (3:18–3:22; abs 198.0–202.0)  **Tool:** Codex k24 + a Seedance take with dialogue (v2) or comp (v1)
**Camera:** close-up, 50 mm, level with her eyes; locked-off. Nana faces screen-right with lead room.

**Action:** Nana's television is off now, and only the lamp lights her: the cold has left her face for good. At the edge
of the frame, the set's dark glass holds a faint ghost of the Lamp, burned in by 41 years. She is calm and not
surprised. "I know, love." The line lands like a key turning. **Start pose:** the handset at her ear, lamp-lit, the
corners of her mouth lifted very slightly, lips closed.

**Build:**
- Codex **k24**.
- **The dark set:** comp lays the burned-in ghost on the television's dark glass at the right edge: the standby card's
  Lamp at 5 % and his face at 3 %, visible over the dark (`production_design.md` §4, burn-in).
- **v2:** a 4 s take with the line (audio on); the ghost goes on top in comp (the camera is locked).
- **v1 fallback:** locked-off; the lamp steady, with a 1 % warm filament flicker. No television flicker (the set is
  off); no rainshadow.
- `letterbox(2.39)`, `grade(HOME)` biased warm, with no cold anywhere on her.

**Keyframe prompt (`k24_nana_know`):**
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
> SHOT: a close-up of Nana in her armchair at night, seen with a 50 mm lens level with her eyes: her face turned
> three-quarters toward screen-right. She holds the cream handset of her telephone to her far ear with her left hand,
> and its coiled cord hangs down across her cardigan. The television in front of her is switched off: at the right edge
> of the frame, the dark curved glass of its screen in the grey cabinet, unlit. She is lit only by the table lamp at the
> left: amber cut planes on her face, hair and hands, the rest in black, and no cold light anywhere on her. Her face is
> calm and still, the corners of her mouth lifted very slightly, lips closed. Behind her at the left, the scorched
> pleated lampshade and its crisp arc of amber on the leaf wallpaper. Composition: her face on the left third with open
> dark space in front of her toward the right; her eyes on the upper third.

**Refs:** `assets/pilot/lookdev_v3/nana.png`, `assets/pilot/lookdev_v3/flat.png`.
**Layers:** none.
**JS spec:** none (the burned-in ghost reuses the J15 card and k02).

**Sound:**
- **NANA** (`Moira`, 145, NANA chain): **"I know, love."** at shot +0.6 (abs 198.6).
- Room tone; rain on glass. **Nana's clock is still ticking** (her time goes on). There is no TV hum (the set is off).
- Phone-line hiss.
- Score 1M6: the warm PAD (F) enters at +1.5 (abs 199.5), −30 dB.

**Motion prompt (v2, Seedance: start `work/pilot/keys_v3/k24_nana_know.png`, 4 s, audio on):** Colour woodcut print
animation; keep the first frame's exact carved shapes, flat inks and designs. Close-up, 50 mm, at her eye level: an old
woman in an armchair, lit only by a lamp's amber light, holds a cream telephone handset to her ear, facing right toward
a switched-off television. Her head does not move. After half a second she says quietly, at an easy pace: "I know,
love." Then she is still, listening. She speaks in an old woman's gentle, slightly thin, warm voice with a neutral
General American accent. Understated performance: her face stays composed; only her lips move. Locked-off camera. Rain
on the window, a wooden clock ticking. No music.

**Takes:** —
