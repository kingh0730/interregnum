# Shot 16 — NANA'S ROOM

**Duration:** 6 s (1:24–1:30; abs 84.0–90.0)  **Tool:** Codex k09 + the State Receiver insert, then a silent Seedance
take (v2) or comp (v1)
**Camera:** 32 mm at seated eye height (1.1 m), the low ceiling in frame (a guest's eye); locked

**Action:** Inside the warm window, a room with a lid: after the Hall's vault lost in darkness, a low ceiling. Nana sits
small in a worn armchair, facing the television in its niche in the wall unit like an icon in a shrine. It shows the
standby card: the Lamp, breathing. On the table, two cups: her thick chipped mug, and the one good cup, poured and
untouched, in front of the empty chair. The amber pot on the stove. Rain on the outer pane, the wooden clock. The cream
telephone beside her rings, and on the second ring she turns her head toward it. **Start pose:** Nana facing the
television, her back three-quarters to us.

**Build:**
- Codex **k09**.
- **The State Receiver insert** (both versions): J15 v3, the standby card, into the screen quad (`insert(auto)`: the
  largest flat cyan region), through the set's curvature, scanlines and burn-in. Save as `work/pilot/v3/k09_tv.png`,
  the comp plate and the Seedance start frame.
- **v2:** a 6 s silent take: steam, rain, and her head turning on the ring. Re-insert the card if the model changes it
  (the camera is locked, so the screen quad is static).
- **v1 fallback:** `flicker(mask=cyan_lit, driver=insert_luma, 4 %)` with the lamp steady; `steam(pot lid)` and
  `steam(porcelain cup)` as a few pale cut ribbons drifting up and fading at 60 px, not soft smoke; `drops(window)` as
  carved beads and runs on the outer pane; the ring as `jitter(mask=the cream handset, 1 px, 25 Hz)` over 3.5–3.9,
  4.1–4.5 and 5.5–5.9 (the handset is one flat cream shape, so its mask is trivial). No move, so no parallax layer.
- `letterbox(2.39)`, `grade(HOME)`.

**Keyframe prompt (`k09_nana_room`):**
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
> SHOT: Nana's one-room flat at night, seen with a 32 mm lens at seated eye height from behind her and a little to her
> left, the low ceiling in the top of the frame. Nana sits small and still in a low armchair with pale worn wooden arms
> and a crocheted cover over its back, her back three-quarters to us, facing a television at the right. The television
> sits in a niche built into a plywood wall unit, like an icon in a shrine: a grey enamel set with one round knob and a
> curved glass screen glowing blank, even pale cyan, a crocheted doily and a small plant in a tin on top. Beside her
> armchair, on a side table, a table lamp with a turned-wood base and a pleated parchment shade scorched brown on one
> side throws a crisp arc of amber light up the wall and a hot ring on the ceiling; a cream bakelite rotary telephone
> sits on a crocheted mat. On a small table in front of an empty wooden chair: a thick chipped mug, and one fine
> porcelain cup and saucer, poured and untouched. In the back corner, a two-ring enamel stove with an amber enamel pot.
> On the back wall, faded wallpaper of small leaves with a pale, unfaded rectangle where a picture once hung, and a
> plain wooden wall clock with a pendulum. A steel-framed window at the back shows rain on the outer pane and the cold
> glow of other towers. Two lights only: amber from the lamp at the left, cold pale cyan from the television at the
> right. Composition: Nana on the left third, the television on the right third, the lamp between them.

**Refs:** `assets/pilot/lookdev_v3/flat.png`, `assets/pilot/lookdev_v3/nana.png`.
**Layers:** none. v1's `k09_fg_nana` is cut: the shot no longer moves.

**JS spec (J15 v3 · the standby card on a State Receiver):**
- **Device:** a card hand-painted in Year One, a white Lamp brushed onto blue gouache, filmed with a slight vignette and
  broadcast between programmes (`production_design.md` §7). It is a film of a card, not a graphic.
- **The card:** blue gouache from `#123A5E` to `#1C4A70` with visible brush marks; the Lamp (ring, pointed-arch flame,
  base, in §5's proportions) painted with a flat brush in white `#EEF2F0`, with dry-brush breaks, 1–2 px edge noise and
  a slight lean. It **breathes** ±3 % at 0.25 Hz: the carrier's heartbeat, so the nation knows the channel is alive.
- **Through the set:** barrel k1 0.05, rounded corners, scanlines, 1 px misconvergence at the corners, a hum bar (−8 %)
  rolling up every 5–9 s, bloom, and the Father's face burned into the tube as a ghost at 4 % (from k02).
- The same card appears on every window's set in 15 and 44 (as a breathing light, not an image) and, dimmed and still,
  on the Wall in 43.

**Sound:**
- Room tone; rain on the glass; **Nana's wooden clock** ticks every whole second (tick/tock).
- TV hum and a faint stand-by tone from the set; the pot simmering.
- **Nana's phone:** a soft double ring at shot +3.5 (abs 87.5) and +5.5 (abs 89.5). Handset lift click at +5.9 (abs
  89.9).
- Warm PAD (F) continues at −30 dB.

**Motion prompt (v2, Seedance: start `work/pilot/v3/k09_tv.png`, 6 s, `--no-audio`):** Colour woodcut print animation;
keep the first frame's exact carved shapes, flat inks and designs. A wide view of a small room at night from seated eye
height, the low ceiling in frame: an old woman sits in an armchair with her back three-quarters to us, facing a
television glowing blue in a wall unit; a lamp with a pleated shade glows amber beside her, and a cream telephone sits
on the side table. Steam rises slowly from a pot on the stove and from a cup on the table; rain runs down the window.
For three seconds she does not move. Then the telephone's handset rattles slightly in its cradle as it rings, and she
slowly turns her head toward it, and stops. Understated performance: only her head turns. Locked-off camera. No sound.

**Takes:** —
