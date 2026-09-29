# Shot 20 — "FOR THE ENDING."

**Duration:** 6 s (1:43–1:49; abs 103.0–109.0)  **Tool:** Codex k13 + a Seedance take with dialogue (v2) or comp (v1)
**Camera:** a closer close-up of Nana, the scene's tightest size, saved for the line that turns it: 50 mm, level with
her eyes; locked-off; lead room to the right

**Action:** Nana, eyes on the screen: "For the ending." A beat. Then what she says every night: "Eat something warm,
love." The audience hears the Father's line from the cold open in her mouth, and the connection clicks. On a second
viewing, "For the ending" means *I watch for your line*. It is also what makes Ida decide: the Father needs an ending.
Her face does almost nothing; the words do it. **Start pose:** the handset at her ear, the corners of her mouth lifted
very slightly, lips closed, about to speak.

**Build:**
- Codex **k13**.
- **v2:** a 6 s take with both lines (audio on).
- **v1 fallback:** locked-off; `flicker(mask=cyan_lit, driver=J15 luma, 4 %)`. No push, no rainshadow.
- `letterbox(2.39)`, `grade(HOME)`.

**Keyframe prompt (`k13_nana_ending`):**
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
> SHOT: a closer close-up of Nana at night, seen with a 50 mm lens level with her eyes: her face and the top of her
> shoulders, turned three-quarters toward screen-right, her eyes resting on a television out of frame at the right. The
> cream handset of her telephone is at her far ear, held in her left hand. The corners of her mouth are lifted very
> slightly; her lips are closed. Amber lamplight from the left and cold pale cyan television light from the right meet
> along the ridge of her nose, never mixed. Behind her, the dark room and a sliver of the scorched lampshade at the left
> edge. Composition: her face on the left half, with open space in front of her toward the right; her eyes on the upper
> third.

**Refs:** `assets/pilot/lookdev_v3/nana.png`, `assets/pilot/lookdev_v3/flat.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- **NANA** (`Moira`, 150, NANA chain): **"For the ending."** at shot +0.5 (abs 103.5).
- **PLUCK F4** (theme note 2) at +1.9 (abs 104.9), in the pause.
- **NANA** (`Moira`, 145): **"Eat something warm, love."** at +3.2 (abs 106.2).
- Room tone; rain; Nana's clock; phone-line hiss; warm PAD (Dm).

**Motion prompt (v2, Seedance: start `work/pilot/keys_v3/k13_nana_ending.png`, 6 s, audio on):** Colour woodcut print
animation; keep the first frame's exact carved shapes, flat inks and designs. A close-up, 50 mm, at her eye level: an
old woman holds a cream telephone handset to her ear, her eyes on a television off-screen at the right, lit by its
cold light on one side and by a lamp's amber on the other. Her head does not move. She says simply, at an easy pace:
"For the ending." She pauses for two seconds, her eyes still on the television. Then she says quietly and firmly: "Eat
something warm, love." After the line she is still. She speaks in an old woman's gentle, slightly thin, warm voice with
a neutral General American accent. Understated performance: her face stays composed; only her lips move. Locked-off
camera. Rain on the window, a wooden clock ticking. No music.

**Takes:** —
