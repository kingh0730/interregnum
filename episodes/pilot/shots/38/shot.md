# Shot 38 — "NANA—"

**Duration:** 3 s (3:15–3:18; abs 195.0–198.0)  **Tool:** Codex k23 + a Seedance take with dialogue (v2) or comp (v1)
**Camera:** close-up, 85 mm, 10 cm above her eye line; locked-off. Ida faces screen-left, still short-sided.

**Action:** She answers the grey phone, not the red one. The handset at her ear, its cord across her chest; in the soft
foreground the red phone rattles on. The House Line's lamp now glows steady (the line is in use), and its amber finds
her cheek from below; the cold of the Wall is thinning on her hair. She starts to explain, or confess, or apologize,
"Nana—", and gets no further. **Start pose:** the handset already at her ear, eyes lowered to the desk, lips parted on
the first syllable.

**Build:**
- Codex **k23**.
- **v2:** a 4 s take with the line (audio on); use 3 s. The prompt is `cinematography.md` §8's rewrite, adapted to the
  staging (the handset at her far ear, as in 17 and 19).
- **v1 fallback:** locked-off; `jitter(mask=the red phone in the soft foreground, 1 px, 25 Hz)` during its ring (shot
  +2.0–3.0); `flicker(mask=amber_lit, driver=noise(0.3 Hz), 2 %)`, the filament of the call lamp.
- `letterbox(2.39)`, `grade(HALL)` with the amber preserved.

**Keyframe prompt (`k23_ida_nana`):**
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
> SHOT: a close-up of Ida at her desk in the dark hall, seen with an 85 mm lens 10 cm above her eye line: her head and
> shoulders, three-quarters toward screen-left. She holds the heavy grey handset of the desk telephone to her far ear
> with her right hand, and its coiled cord runs down across her chest. Her face is composed, her eyes lowered to the desk
> in front of her, her lips parted on the first syllable. A small amber lamp on the telephone below the frame lights her
> cheek and jaw from below as a warm cut shape; the cold pale cyan of the hall is only a thin rim along the back of her
> hair. In the soft foreground at the lower left, the corner of a heavy signal-red telephone. Composition: her face on
> the left third, turned toward the near edge of the frame, with dark space behind her head at the right; her amber
> scarf at the bottom edge.

**Refs:** `assets/pilot/lookdev_v3/ida.png`, `assets/pilot/lookdev_v3/hall.png`.
**Layers:** none.
**JS spec:** none.

**Sound:**
- **IDA** (`Samantha`, 165, IDA hall chain): **"Nana—"** at shot +0.7 (abs 195.7). Render "Nana, I" and keep only
  0.5 s, with a 30 ms fade: she is cut off.
- The red phone rings at abs 197.0 (close-ish, −6 dB); phone-line hiss.
- No music yet.

**Motion prompt (v2, Seedance: start `work/pilot/keys_v3/k23_ida_nana.png`, 4 s, audio on; use 3 s):** Colour woodcut
print animation; keep the first frame's exact carved shapes, flat inks and designs. Close-up, 85 mm, slightly above her
eye line: Ida in three-quarter view facing screen-left, the grey handset of the desk phone already at her ear, its
coiled cord running down across her chest. In the soft foreground at lower left, the red telephone's handset rattles
in its cradle. She is still, her eyes lowered to the desk in front of her. She says one word, quietly: "Nana—" and
stops, her lips staying slightly parted. Her head does not move. She speaks in a young woman's low, soft, tired voice
with a neutral General American accent. Understated performance: her face stays composed; only her lips move.
Locked-off camera. The red telephone's bell close by in a silent hall. No music.

**Takes:** —
