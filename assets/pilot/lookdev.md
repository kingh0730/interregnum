# Pilot lookdev v3: CONTINUITY in RELIEF

Six look-development images in the RELIEF direction (`bible/visual/art_direction.md` §B): three character sheets and
three locations. They are the only refs a v3 keyframe may attach (**Refs:** in each `episodes/pilot/shots/NN/shot.md`).
Edits attach only the keyframe they edit. Every prompt below is complete and standalone, and the runnable copy of all
43 v3 images is `episodes/pilot/images_v3.json`.

**Retired:** `assets/pilot/lookdev/ld1`–`ld6` carry the v1 cel look. Never attach them to anything; Codex copies the
style of whatever it is shown. Keep them on disk as story references only.

**The style anchor:** `work/pilot/tests/B2.png` (the RELIEF test of Nana) is how RELIEF must look. It is attached to
five of the six lookdev images below as the carving reference, and to nothing else. Don't delete it until the lookdev
is approved.

```
uv run tools/imagegen/batch.py episodes/pilot/images_v3.json --only <ids> --jobs <n>
```
Run it **without `--prefix-file`**: `build/style_prefix.txt` is the v1 cel prefix and would undo the look.

---

## The RELIEF block (v3): leads every image prompt in the pilot

> STYLE (RELIEF): a frame from an animated film printed by hand as a colour woodcut and linocut on warm cream paper. A
> carved blue-black key block holds the image; large areas stay solid black, with faint wood grain. Every surface (skin,
> cloth, hair, concrete, metal, glass, floor) is matte printed ink: no reflections, no sheen, no specular highlights, no
> smooth gradients. Light is a shape cut out of the black with crisp, slightly irregular knife edges. Middle tones
> everywhere, on walls, floors and machines as on faces, are parallel gouge strokes that follow the form. Colour is flat
> spot ink, never blended, with paper grain showing through: pale cold cyan where screens light things, amber where lamps
> light things, signal red only on red objects. Slight misregistration; no drawn outlines. Only screen light is soft.
> Faces are a few carved planes, calm; eyes are small dark shapes without highlights. Avoid: anime, airbrush, digital
> painting, 3D render, photorealism, lens flare, bokeh, neon, glossy or wet floors.

165 words. **Why it changed from the `art_direction.md` block:** test B1 (the Hall) kept the architecture but lost the
print. Its floor turned into polished terrazzo that mirrored the desks and the ledger lines, the piers shaded in smooth
gradients under a grunge texture, and the brass pipes shone gold. B2 (Nana) got it right: gouge strokes follow every
form, blacks carry wood grain, and every colour is an ink with paper showing through. The new block names every surface
as matte ink, bans reflection, sheen, specular and gradient outright, puts gouge half-tones on walls, floors and
machines as well as faces, and adds wet floors to the avoid list.

## Shared blocks (restated in full inside every prompt that uses them)

**FRAME, world** (every 2.39 shot):
> FRAME: wide 16:9; keep everything important inside the central horizontal band, because the top and bottom 13% will
> be cropped to 2.39:1. No text, letters, numbers or logos anywhere; every screen is blank and evenly glowing.

**FRAME, broadcast** (k01; k02 and k20 inherit it by edit): the Evening Address is a 4:3 picture cropped from the 16:9
image (`production_design.md` §7).
> FRAME: wide 16:9, of which only the central 4:3 will be used: keep him and everything important inside the middle
> three quarters of the width. No text, letters, numbers or logos anywhere.

**FRAME, sheet:**
> FRAME: a wide 16:9 model sheet on plain warm cream paper, the views evenly spaced. No text, labels, letters or
> numbers anywhere.

**COPY RULE** (the Father's broadcast frames only). By the series rules the machine's copy of a man is the one image
that is not carved. It follows the RELIEF block, so the block still leads, and it overrides the block for that image:
> COPY RULE (for this image only, it overrides the style above): this is the broadcast picture itself, the machine's
> copy of a man, and the one image in the film that is not carved. Paint it as a flawless, polished digital studio
> portrait: smooth continuous gradients, soft even light with no hard shadows, perfect symmetry, skin with no texture
> or pores, no gouge strokes, no paper grain, no print texture of any kind. Use the attached sheet only for who he is
> (his face, hair, beard, ears, coat and pin), not for its carved style.

The edits of his picture (k02, k20) use the same rule in its edit form:
> COPY RULE (for this image only, it overrides the style above): this is the broadcast picture itself, the machine's
> copy of a man, and the one image in the film that is not carved. Keep the attached picture's flawless, polished
> studio finish exactly: smooth continuous gradients, soft even light, perfect symmetry, skin with no texture or pores,
> no gouge strokes, no paper grain, no print texture of any kind.

**Identity lines** (keyframes; the sheets below carry the full descriptions):
> IDA (the woman on the attached sheet): 27, slim; a blunt black bob cut straight at the jaw, with straight bangs above
> her brows; straight dark brows; a small straight nose; warm light-olive skin; a small silver hoop in her left ear; a
> charcoal ribbed turtleneck and a hand-knitted mustard-amber scarf, the only warm colour on her.

> NANA (the woman on the attached sheet): 82, small; silver-white hair in a low bun held with a dark wooden pin; a soft
> round face with deep lines; small dark eyes behind thin round gold wire glasses; warm brown skin; small pearl
> earrings; a dark bottle-green hand-knitted cardigan, near-black in shadow, over a cream blouse with a small lace
> collar.

> THE FATHER (the man on the attached sheet), an invented man who resembles no real person: about 85; a broad, round
> face with a broad nose; thick white hair brushed back in soft waves from a high forehead; heavy white brows; a short,
> full, rounded white beard; deep-set eyes under heavy lids; large ears with long lobes; a small dark mole high on his
> left cheekbone (on the right side of the picture); weathered warm-tan skin; a charcoal wool coat with a soft collar
> rolled around the neck, hidden fastenings and no buttons, pockets, medals or insignia; one small round silver pin on
> the left side of the collar, a ring around a pointed flame.

**Design refinements for the medium.** Ida loses v1's lanyard and blank ID card: they cluttered the silhouette and
invited text. Her scarf gains a darn, because every object shows one repair and Nana knitted it. Nana takes B2's
lace collar and gains a darn at one elbow. The Father gains large ears with long lobes, a detail specific to him and
nobody famous, and the ear is the one the Proof keeps correcting. His coat follows `production_design.md` §7: a soft
rolled collar with hidden fastenings, nothing that reads as a uniform. The bob, the scarf, the bun and the round
glasses are each one shape of ink, so every character passes the silhouette test.

---

## Generation order and budget

The pilot's v3 budget is **43 Codex images**: 6 lookdev, 25 new keyframes, 5 keyframe edits, 7 hardware plates and no
cutout layers. That leaves 2 images of the 45 cap for retakes. At about 1–2 minutes per image, 5 in parallel, the whole
pass is about 20 minutes of Codex time.

1. **`ld_hall` alone.** It is the image B1 failed. Judge it against the checks below before spending anything else.
   If the floor still shines or the brass still glows, fix the prompt and retake.
2. **The other five lookdev** in parallel: `ld_ida`, `ld_nana`, `ld_father`, `ld_flat`, `ld_city` (`ld_city` attaches
   `ld_hall`).
3. **The keyframe test trio:** `k01_father_mcu` (the Copy Rule), `k03_hall_wide` (the world with a figure in it) and
   `k11_nana_answers` (a face under restraint). Judge all three.
4. **Everything else** in manifest order (`--jobs 5`). The batch skips images that already exist and waits for deps,
   so edits (`k02`, `k20`, `k05b`, `k26`, `k27`) run after their sources.

Exit code 2 is a safety false positive: reword neutrally and retry (the batch retries once with a neutral preamble).
Move rejects to `work/pilot/rejects/`.

## Acceptance checks (Claude judges stills; `cinematography.md` §9)

- **Print, not painting.** Zoom on the floor, the brass, any glass and the eyes. Nothing reflects, shines or has a
  specular dot. Middle tones on piers, floors and machines are parallel gouge strokes, not a grunge overlay or an
  airbrushed falloff. Large areas are solid black with faint wood grain, and paper grain shows through the inks.
- **Inks.** Count them: blue-black key, cream paper, cold cyan, amber, signal red, plus Nana's near-black green. Rose
  appears only in `k27`. No sodium orange anywhere. In the Hall, amber comes only from a living hand: Ida's scarf, the
  thermos, the archive's tungsten light table (p08) and, from shot 37, the House Line's call lamp. The brass is
  olive-black, never gold.
- **Darkness:** at least 50 % of the pixels of a night frame are under 15 % luminance. **Silhouette:** thresholded at
  25 %, every figure and key object still reads.
- **Screens** are blank, evenly glowing, cleanly separable shapes. There is no text anywhere, including keycaps, plates
  and dials.
- **Faces** are calm, with small dark eyes and no highlights, no tears and no grins. Each sheet shows one person in every
  view.
- **The Father resembles no real person.** If any take reads as a real public figure, reject it. His coat must not read
  as a uniform, tunic or robe.
- **The Copy Rule:** `k01`, `k02` and `k20` are smooth and polished, with no gouge strokes and no paper grain. If `k01`
  comes back carved, retake it once with no ref attached (identity from the words alone).

---

## LD1 · `assets/pilot/lookdev_v3/hall.png` (generate first)

**Refs:** `work/pilot/tests/B2.png` (carving only). **Transparent:** no.
**Used by:** every Hall keyframe and hardware plate: k03, k04, k05, k06, k07, k10, k12, k14, k16, k18, k21, k22,
k23, k25, k28, p04, p08, p12, p14, p21, p37; and `ld_city` as its style reference.

**Prompt (`ld_hall`):**
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
> Use the attached print only as the reference for the carving, the inks and the paper; its subject is not part of
> this image.
> SUBJECT: a location design for the Hall of a broadcast ministry at night, with nobody in it. A 35 mm view from
> standing height, from behind and to the left of the one uncovered operator desk, looking past it down the nave to the
> far wall. The desk, in the lower left foreground: a long steel console in blue-grey hammered enamel, its armrest worn
> to bare metal, an empty chair pushed in. On it, from left to right: a frosted light table set into the desk top, with
> a brass pneumatic tube coming down from above into a brass cup beside it; a large colour monitor set back under a
> deep hood, with a row of round black knobs; a small monitor under a hood above a keyboard of sculpted grey keys with
> one large square red key; a narrow column of six small rectangular lamps; a teleprinter on its own stand. At its front
> edge: a heavy red telephone with no dial, a grey rotary telephone, and a small dented amber enamel thermos. The two
> screens glow blank, even pale cyan. Beyond the desk, the nave: rows of desks under fitted canvas covers laced on with
> cord, like a field of pale stones; square board-formed concrete piers carved with plank grain and rows of round
> tie-holes, rising into a vault lost in black; olive-black brass tubes climbing the piers, never gold, never shining.
> The floor is dark terrazzo printed as matte black ink broken by short straight gouge strokes, with thin inlaid brass
> lines printed as pale cold cut lines running toward the far wall, and iron grilles. At the far end, the whole wall is
> a grid of 12 by 8 deep concrete niches with thick walls between them, each holding one large old round-cornered
> television tube, all glowing the same blank pale cyan: the only strong light, throwing the piers' long shadows down
> the nave as cut shapes. Above it on the centre line: a riveted steel lamp box with a dark red glass front, a long
> black board of blank flip-number cards, and a huge pale round clock face with baton marks. High on the left wall, a
> dark glass gallery box juts over the nave. The thermos is the only warm colour. At least half of the image is solid
> black.

## LD2 · `assets/pilot/lookdev_v3/ida.png` (character sheet)

**Refs:** `work/pilot/tests/B2.png` (carving only). **Transparent:** no.
**Used by:** every Ida keyframe and every plate with her hands: k03, k04, k06, k07, k10, k12, k14, k15, k16, k18, k22,
k23, k25, k28, p04, p21.

**Prompt (`ld_ida`):**
> STYLE (RELIEF): a frame from an animated film printed by hand as a colour woodcut and linocut on warm cream paper. A
> carved blue-black key block holds the image; large areas stay solid black, with faint wood grain. Every surface (skin,
> cloth, hair, concrete, metal, glass, floor) is matte printed ink: no reflections, no sheen, no specular highlights, no
> smooth gradients. Light is a shape cut out of the black with crisp, slightly irregular knife edges. Middle tones
> everywhere, on walls, floors and machines as on faces, are parallel gouge strokes that follow the form. Colour is flat
> spot ink, never blended, with paper grain showing through: pale cold cyan where screens light things, amber where lamps
> light things, signal red only on red objects. Slight misregistration; no drawn outlines. Only screen light is soft.
> Faces are a few carved planes, calm; eyes are small dark shapes without highlights. Avoid: anime, airbrush, digital
> painting, 3D render, photorealism, lens flare, bokeh, neon, glossy or wet floors.
> FRAME: a wide 16:9 model sheet on plain warm cream paper, the views evenly spaced. No text, labels, letters or
> numbers anywhere.
> Use the attached print only as the reference for how a face, hair and knitwear are carved and inked; the woman in it
> is someone else.
> CHARACTER: IDA, a woman of 27: slim, of medium height; a blunt black bob cut straight at the jaw, with straight bangs
> just above her brows; straight dark brows; a small straight nose; a narrow, tired face; warm light-olive skin; a small
> silver hoop in her left ear; a charcoal ribbed turtleneck sweater, dark trousers and flat shoes; a hand-knitted
> mustard-amber wool scarf worn loosely around her neck, darned once in a slightly different yarn. The bob is one solid
> black shape, the ribs of the sweater are parallel gouge strokes, and the scarf is the only warm colour on the sheet.
> Every view shows exactly the same woman with identical proportions, hair and clothes. She is lit from the left by cold
> pale cyan screen light, as at her desk, and her shadows are solid black shapes.
> LAYOUT: top row, three full-length views of Ida standing with her arms relaxed: front, three-quarter facing left, and
> back. Bottom row, four head-and-shoulder studies, all three-quarters toward screen-left: (1) eyes lowered, face
> composed, mouth closed; (2) holding the heavy grey handset of an old desk telephone to her far ear with her right
> hand, its coiled cord looping down across her chest; (3) eyes closed, composed; (4) face tilted up, lit from above.
> Her face is calm in every view: no smiles, no tears.

## LD3 · `assets/pilot/lookdev_v3/nana.png` (character sheet)

**Refs:** `work/pilot/tests/B2.png` (identity and carving: she is the woman in it). **Transparent:** no.
**Used by:** k09, k11, k13, k19, k24, k29.

**Prompt (`ld_nana`):**
> STYLE (RELIEF): a frame from an animated film printed by hand as a colour woodcut and linocut on warm cream paper. A
> carved blue-black key block holds the image; large areas stay solid black, with faint wood grain. Every surface (skin,
> cloth, hair, concrete, metal, glass, floor) is matte printed ink: no reflections, no sheen, no specular highlights, no
> smooth gradients. Light is a shape cut out of the black with crisp, slightly irregular knife edges. Middle tones
> everywhere, on walls, floors and machines as on faces, are parallel gouge strokes that follow the form. Colour is flat
> spot ink, never blended, with paper grain showing through: pale cold cyan where screens light things, amber where lamps
> light things, signal red only on red objects. Slight misregistration; no drawn outlines. Only screen light is soft.
> Faces are a few carved planes, calm; eyes are small dark shapes without highlights. Avoid: anime, airbrush, digital
> painting, 3D render, photorealism, lens flare, bokeh, neon, glossy or wet floors.
> FRAME: a wide 16:9 model sheet on plain warm cream paper, the views evenly spaced. No text, labels, letters or
> numbers anywhere.
> She is the woman in the attached print: keep her face, hair, glasses, earrings and clothes, and carve her exactly as
> the print does.
> CHARACTER: NANA, a small woman of 82: silver-white hair drawn back into a low bun held with a dark wooden pin; a soft
> round face with deep lines; small dark eyes behind thin round gold wire glasses; warm brown skin; small pearl
> earrings; a dark bottle-green hand-knitted cardigan, near-black in shadow and darned at one elbow, over a cream blouse
> with a small lace collar; a dark skirt and soft slippers. Every view shows exactly the same woman with identical
> proportions, hair and clothes.
> LAYOUT: top row, three full-length views of Nana standing, small and slightly stooped, her hands folded: front,
> three-quarter facing right, and back. Bottom row, four head-and-shoulder studies, all three-quarters toward
> screen-right: (1) holding a cream bakelite telephone handset to her far ear, its coiled cord hanging down, lit cold
> pale cyan from the right and amber from the left, the two inks meeting along the ridge of her nose; (2) facing almost
> toward us, holding a thick chipped mug under her chin in both hands, lit cold from the front; (3) lit only by amber
> lamplight from the left, the rest in black; (4) the corners of her mouth lifted very slightly, lips closed. Her face
> is calm and specific in every view: no grins, no tears.

## LD4 · `assets/pilot/lookdev_v3/father.png` (character sheet)

**Refs:** `work/pilot/tests/B2.png` (carving only). **Transparent:** no.
**Used by:** k01 (identity only, under the Copy Rule; k02 and k20 follow by edit). Shot 08 crops this sheet for the
archive's live-capture frames: the man as he was, carved like everyone living, before the copy.

**Prompt (`ld_father`):**
> STYLE (RELIEF): a frame from an animated film printed by hand as a colour woodcut and linocut on warm cream paper. A
> carved blue-black key block holds the image; large areas stay solid black, with faint wood grain. Every surface (skin,
> cloth, hair, concrete, metal, glass, floor) is matte printed ink: no reflections, no sheen, no specular highlights, no
> smooth gradients. Light is a shape cut out of the black with crisp, slightly irregular knife edges. Middle tones
> everywhere, on walls, floors and machines as on faces, are parallel gouge strokes that follow the form. Colour is flat
> spot ink, never blended, with paper grain showing through: pale cold cyan where screens light things, amber where lamps
> light things, signal red only on red objects. Slight misregistration; no drawn outlines. Only screen light is soft.
> Faces are a few carved planes, calm; eyes are small dark shapes without highlights. Avoid: anime, airbrush, digital
> painting, 3D render, photorealism, lens flare, bokeh, neon, glossy or wet floors.
> FRAME: a wide 16:9 model sheet on plain warm cream paper, the views evenly spaced. No text, labels, letters or
> numbers anywhere.
> Use the attached print only as the reference for how a face, hair and cloth are carved and inked; the woman in it is
> someone else.
> CHARACTER: THE FATHER, an invented man who resembles no real person: about 85, broad and heavy-set; a broad, round
> face with a broad nose; thick white hair brushed back in soft waves from a high forehead; heavy white brows; a short,
> full, rounded white beard; deep-set eyes under heavy lids; large ears with long lobes; a small dark mole high on his
> left cheekbone, on the right side of the image in the front views; weathered warm-tan skin. He wears a long charcoal
> wool coat with a soft collar rolled around the neck, hidden fastenings, and no buttons, pockets, medals or insignia;
> it must not look like a uniform, a tunic or a robe. His only ornament is a small round silver pin on the left side of
> the collar: a ring around a pointed flame. Every view shows exactly the same man with identical proportions, hair,
> beard and coat. He is lit from the front-left, and his shadows are solid black shapes.
> LAYOUT: top row, three head-and-shoulder studies: (1) square to us, looking straight at the viewer, calm, mouth
> closed; (2) three-quarter view; (3) profile facing right, showing the large ear clearly. Bottom row: (4) full length,
> standing upright, hands folded in front; (5) a close-up square to us with his eyes gently closed; (6) a close-up of
> the silver pin.

## LD5 · `assets/pilot/lookdev_v3/flat.png`

**Refs:** `work/pilot/tests/B2.png` (carving; its lampshade and wallpaper belong to this room). **Transparent:** no.
**Used by:** k09, k11, k13, k19, k24, k29.

**Prompt (`ld_flat`):**
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
> Use the attached print as the reference for the carving, the inks and the paper; its lampshade and leaf wallpaper
> belong to this room, but the woman is not in this image.
> SUBJECT: a location design for Nana's flat at night, with nobody in it: one room on the fourteenth floor of a concrete
> tower block, seen with a 32 mm lens from the doorway at seated eye height, the low ceiling in the top of the frame with
> its enamel ceiling lamp switched off. At left, a low armchair with pale worn wooden arms, a crocheted cover over its
> back and one arm cover that does not match; beside it on a side table, a table lamp with a turned-wood base and a
> pleated parchment shade scorched brown on one side, throwing a crisp arc of amber light up the wall and a hot ring on
> the ceiling; a cream bakelite rotary telephone on a crocheted mat, its handset cord wound with tape where it frayed.
> At right, a plywood wall unit with its veneer lifting at the corners, built with a niche for the television like a
> shrine: in the niche, a grey enamel television set with one round knob and a curved glass screen glowing blank, even
> pale cyan, with a crocheted doily and a small plant in a tin on top. In the middle, a small table with two cups: a
> thick chipped mug, and one fine porcelain cup and saucer, poured and untouched, in front of an empty wooden chair. In
> the back corner, a two-ring enamel stove with a lidded amber enamel pot, chipped to black iron at the rim. On the back
> wall: faded wallpaper of small leaves with a pale, unfaded rectangle where a picture once hung, and a plain wooden wall
> clock with a pendulum and baton marks, its winding key on a nail beside it. A steel-framed window, painted many times,
> with two panes; rain runs on the outer pane, and beyond it glows the cold light of other towers. Only two lights: the
> lamp's amber at the left and the television's cold pale cyan at the right. At least half of the room is black.

## LD6 · `assets/pilot/lookdev_v3/city.png`

**Refs:** `assets/pilot/lookdev_v3/hall.png` (carving of architecture only). **Transparent:** no.
**Used by:** k08 (and k27 through it), k17.

**Prompt (`ld_city`):**
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
> Use the attached image only as the reference for the carving, the inks and the paper; its subject is not part of this
> image.
> SUBJECT: a location design for the City at night in steady rain, seen with a 35 mm lens from a concrete footbridge
> over a straight canal, at the height of a third floor. Identical sixteen-storey slab towers of board-formed concrete,
> carved with horizontal bands, line both banks and repeat to the horizon; each slab ends in a rounded stair tower with
> a vertical slot of glass blocks glowing cold. Their facades are strict grids of small windows, each a separate cut
> shape bounded by dark mullions; almost every window glows the same cold pale cyan from a television inside, and
> exactly one window, in the nearest tower on the right, glows amber from a lamp. Residents' repairs: glazed-in
> balconies with mismatched frames, laundry lines, window boxes, a pane painted over. On every roof stands one antenna
> mast, all turned the same way, toward a thin lattice transmitter mast on the horizon with a single red lamp. The
> canal has vertical concrete embankments with iron railings and mooring rings, and black water broken by short
> horizontal cuts of cyan beneath the windows. Mercury street lamps on concrete posts give a cold blue-green light;
> there is no orange light anywhere. Far off, a single tram with a rounded nose and one round headlamp crosses a bridge,
> its windows lit cold. At the end of the canal, the pediment of a civic building frames a large glowing screen. Rain
> falls as fine slanted cut lines, visible only where it crosses light. At least half of the image is solid black.

---

## Keyframe → refs map (quick reference)

| Image | Attach |
|---|---|
| k01 | `father` (identity only, Copy Rule) |
| k02, k20 | edits: k01 → k02 → k20 |
| p01 (the Lighting) | none: a monochrome film of a lamp, from the words alone |
| k03, k14, k18, k04, k07, k10, k12, k23, k25, k28 | `ida`, `hall` |
| k15 | `ida` |
| p04, p21, k06, k16, k22 (her hands) | `hall`, `ida` |
| k05, k21, p08, p12, p14, p37 | `hall` |
| k05b | edit of k05 |
| k08, k17 | `city` |
| k27 | edit of k08 |
| k26 | edit of k03 |
| k09, k11, k13, k19, k24, k29 | `nana`, `flat` |
