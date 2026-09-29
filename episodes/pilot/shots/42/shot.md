# Shot 42 — COME HOME

**Duration:** 7 s (3:30–3:37; abs 210.0–217.0)  **Tool:** Codex k25 + a silent Seedance take (v2) or comp (v1)
**Camera:** close-up at 40's size, 85 mm, 10 cm above her eye line; locked-off. **For the first time, Ida has lead
room:** the frame opens in front of her when she stops carrying it alone.

**Action:** Nana, on the line: "Come home. The soup's still warm." Ida is leaning over the desk with the handset held
between her ear and her shoulder, both hands around the small dented amber thermos that has stood unopened since shot
07. After the line, her hands unscrew the cap and lift it off, and a thin ribbon of steam rises into the dark space in
front of her face, into the cold light. The soup is still warm, and her hands say so. Her face stays composed: **the
laugh is heard, not seen** (a breath turning into a small laugh, in the mix). Nana's theme plays whole for the first
time and resolves as the cap comes off. Around her the Wall has dropped to standby; the cold is fading from her hair,
and the call lamp's amber is the light on her face. **Start pose:** the handset between ear and shoulder, both hands
around the closed thermos, eyes open and resting on it, mouth closed.

**Build:**
- Codex **k25**. This is the accepted thermos beat, folded into the shot's own 7 s: no shot is added.
- **v2:** a 7 s silent take (`--no-audio`). Nana's line is the second line of shot 41's take, through the PHONE chain;
  Ida's breath and laugh are sound effects.
- **v1 fallback:** locked-off. The cold rim fades by 60 % over 1.0–6.0 s (cyan-lit mask) while the amber holds, and the
  grade shifts from HALL toward warm across the shot. Without the take the cap can't come off: from 4.5 s let a thin
  wisp of steam escape at the cap's thread instead, as pale cut ribbons.
- v1's tear glint is gone: no tears in RELIEF, and no highlights.
- `letterbox(2.39)`.

**Keyframe prompt (`k25_ida_home`):**
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
> SHOT: a close-up of Ida at her desk in the dark hall, seen with an 85 mm lens 10 cm above her eye line, three-quarters
> toward screen-left, with open space in front of her face. She leans forward over the desk and holds the heavy grey
> handset of the desk telephone between her far ear and her shoulder, its coiled cord running down across her chest.
> Both her hands rest around a small dented amber enamel thermos standing on the desk in front of her, chipped to black
> iron at the rim, its cap still on. Her face is composed, her eyes open and resting on the thermos, her mouth closed. A
> small amber lamp on the telephone below the frame lights her cheek, her hands and the thermos from below as warm cut
> shapes; the cold pale cyan of the hall is only a faint rim on the back of her hair. Composition: her face on the right
> third, looking left into the open dark space; the thermos and her hands at the lower left of centre; above them, open
> dark space.

**Refs:** `assets/pilot/lookdev_v3/ida.png`, `assets/pilot/lookdev_v3/hall.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- **NANA (V.O., on the phone)** (`Moira`, 145, PHONE chain): **"Come home. The soup's still warm."** at shot +1.5
  (abs 211.5).
- Ida's breath and laugh-sob (fx): breaths at abs 210.6, 211.2, 214.8 and 215.6, and a shaky laugh at 215.0.
- **Nana's theme resolved** (1M6): A4 210.2, F4 211.0, G4 211.8, E4 212.6, F4 213.4, **D4 214.4**, then a high D5
  echo at 215.4. PAD **F → C/E → Dm**.
- The red phone at abs 212.0 and 215.0, far off (−18 dB), fading from attention.
- **No ducking of the D4 resolution.**

*v3 sound note:* add the thermos cap turning on its thread (a soft enamel-on-steel scrape) at about shot +4.5–5.2, and
the faint breath of the steam after it. The laugh at 215.0 then lands as the cap comes off, just after the D4.

**Motion prompt (v2, Seedance: start `work/pilot/keys_v3/k25_ida_home.png`, 7 s, `--no-audio`):** Colour woodcut print
animation; keep the first frame's exact carved shapes, flat inks and designs. Close-up, 85 mm, slightly above her eye
line: a young woman leans over a desk in a dark hall, a grey telephone handset held between her ear and her shoulder,
both hands around a small amber thermos in front of her, her eyes resting on it. For four seconds she does not move;
she is listening. Then her hands slowly unscrew the thermos cap and lift it off, and a thin ribbon of steam rises from
the thermos into the dark space in front of her face. Her head does not move. Understated performance: her face stays
soft and composed; only her hands move. Locked-off camera. No sound.

**Takes:** —
