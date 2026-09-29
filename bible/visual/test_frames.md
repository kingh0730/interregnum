# Test frames: three directions, two moments

Six Codex stills that let the showrunner compare the three art directions of `art_direction.md` side by side.
Every direction paints the same two pilot moments with the same subject text, so only the style block changes.
- **Moment 1, the Hall wide (shot 05):** architecture, scale, darkness, and the one warm point.
- **Moment 2, Nana's close-up (shot 18):** a face under restraint, two lights meeting, domestic material culture.

| ID | Direction | Moment | Output |
|---|---|---|---|
| A1, A2 | STILL LIFE | Hall wide, Nana CU | `work/pilot/tests/A1_hall.png`, `A2_nana.png` |
| B1, B2 | RELIEF (recommended) | Hall wide, Nana CU | `work/pilot/tests/B1_hall.png`, `B2_nana.png` |
| C1, C2 | TABLEAU | Hall wide, Nana CU | `work/pilot/tests/C1_hall.png`, `C2_nana.png` |

## Running them
- **Command:** `tools/imagegen/gen.sh work/pilot/tests/<ID>_<name>.png "<prompt>"`, pasting the prompt below as one
  argument, with **no input images**. Exit code 2 is a safety false positive: reword neutrally and retry.
- **Cost:** 6 Codex images, about 1–2 min each at medium effort, all six in parallel (at most 5 at once). That's about
  a sixth of the v1 lookdev-and-keyframe pass. Budget one retake per direction if a frame misses its own style block,
  so 9 images at most.
- **Refs: none for all six.** `ld1`–`ld6` carry the v1 flat-cel style and the old architecture. Codex copies the
  style of whatever is attached, so any old ref pulls the frame back to the look being replaced. Identity comes from
  the words. After the pick, new character sheets are painted in the chosen direction. If Nana's features drift in
  these tests, that is acceptable: the tests judge the look, not the likeness.
- **Before judging the Hall frames,** comp the Father into the tubes with the tile-by-tile insert
  (`production_design.md` §4, k02 frozen). Codex keeps the tubes blank by rule, and the composition only reads with
  his face in it. Judge Nana as generated.
- **Motion:** after the showrunner picks a direction, run one 5 s silent Seedance take of the winning Nana frame at
  480p (about $1.10). Use the §8 rules of `cinematography.md`: she listens, still, then lowers her eyes once. It tests
  whether the direction's texture survives motion. Claude can't watch it, so the showrunner judges.

## What to judge (Claude checks stills first; the showrunner decides)
1. **Authorship:** from this one frame, would you know which film it is? Or could it be any film?
2. **Default look defeated:** no glossy eyes, god rays, bokeh, neon, even light or centred portrait.
3. **Palette as physics:** cold only from tubes, warm only from the lamp and the scarf, no warm brass, no stray hues.
4. **Still-frame checks** (`cinematography.md` §9): silhouette, darkness ratio, face off-centre.
5. **Hall:** the columbarium, the covered desks, the ledger lines and the gallery all read. Ida is tiny, and the axis
   is one straight line.
6. **Nana:** the two lights meet on the ridge of her nose. The face is calm and specific, not sweet. The lampshade,
   handset and wallpaper look like objects someone owns.
7. **Comp-readiness:** the tube faces are clean, separable glowing shapes, and flat areas can be masked.
8. **Motion-readiness:** texture lives in the set and the blacks, not on the face and hands.

---

## A · STILL LIFE

### A1 · The Hall wide
```
STYLE (STILL LIFE): a frame from a hand-painted animated feature for adults, opaque gouache on warm-grey toned
paper. Forms are flat, slightly uneven planes of greyed colour with dry-brush edges and visible paper tooth; no ink
outlines, and in shadow the edges dissolve. Night is deep indigo-grey. Light is painted as chalky opaque colour
exactly where it lands, only from sources in the scene, with a crisp shape and no glow: pale cold blue-white from
screens, warm sienna-gold from lamps, deep red only on red objects. Figures are still and quiet: faces of three or
four planes, eyes small dark shapes without highlights. Detail gathers at the focal point; the rest is simplified.
Avoid: anime style, big glossy eyes, airbrush gradients, glow halos, light rays, lens flare, bokeh, neon,
teal-and-orange colour, 3D render, photorealism.
FRAME: wide 16:9 landscape; keep every important element inside the central horizontal band, because the top and
bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters or numbers anywhere; every screen is a blank,
evenly glowing surface.
SHOT: a vast night interior in one-point perspective, seen from high up at the back of the nave on its centre line,
with a 24 mm lens. The Hall of a broadcast ministry: a long nave of tapered board-formed concrete piers rising into
a ribbed vault lost in darkness; rows of operator desks under fitted canvas covers laced on with cord, receding in
straight lines; thin inlaid brass lines running along a dark terrazzo floor toward the far end; iron floor grilles
in the aisles, with dust rising from them into the light. The entire far wall is a grid of 12 by 8 deep concrete
niches, each holding one large old television tube with curved, round-cornered glass, all glowing the same pale
cold blue-white with nothing on them; this wall is the only strong light and throws the piers' long shadows down the
nave. Above the wall on the centre line hangs a riveted steel lamp box with a dark, unlit red glass front, and above
it a huge round clock face. High on the left wall, a dark glass gallery box projects over the nave with one small red
lamp glowing under it. Tarnished olive-black brass pneumatic tubes climb the piers and never shine warm. On the
centre line, a third of the way from the wall, one uncovered desk is lit by its own small glowing screens, and a small
woman sits at it with her back to us: a short black bob and a mustard-amber scarf, the only warm colour in the image.
She is tiny, less than a thumbnail in the vast space. Everything else falls into darkness.
```

### A2 · Nana's close-up
```
STYLE (STILL LIFE): a frame from a hand-painted animated feature for adults, opaque gouache on warm-grey toned
paper. Forms are flat, slightly uneven planes of greyed colour with dry-brush edges and visible paper tooth; no ink
outlines, and in shadow the edges dissolve. Night is deep indigo-grey. Light is painted as chalky opaque colour
exactly where it lands, only from sources in the scene, with a crisp shape and no glow: pale cold blue-white from
screens, warm sienna-gold from lamps, deep red only on red objects. Figures are still and quiet: faces of three or
four planes, eyes small dark shapes without highlights. Detail gathers at the focal point; the rest is simplified.
Avoid: anime style, big glossy eyes, airbrush gradients, glow halos, light rays, lens flare, bokeh, neon,
teal-and-orange colour, 3D render, photorealism.
FRAME: wide 16:9 landscape; keep every important element inside the central horizontal band, because the top and
bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters or numbers anywhere.
SHOT: a close-up of Nana, a small woman of 82, at night in her one-room flat, seen with a 50 mm lens at her eye level
as she sits in a low armchair. She has silver-white hair in a low bun held by a dark wooden hairpin, a soft round
face with deep lines, small dark eyes behind thin round gold wire-rimmed glasses, warm light-brown skin, small pearl
stud earrings, and a dark bottle-green knitted cardigan over a cream blouse. She holds an old cream bakelite
telephone handset to her ear on the side facing us; its coiled cord loops down out of frame. Her face is turned
three-quarters toward screen-right, her eyes resting on a television out of frame to the right. She is still and
composed, mouth closed, about to speak. Two lights meet on her face: cold pale blue-white from the television on the
right and warm amber from a table lamp on the left, the two colours meeting along the ridge of her nose. Behind her
at the left edge, a pleated parchment lampshade glows, scorched brown on one side, and throws a crisp arc of light on
faded wallpaper with a small leaf pattern; beside the arc is a pale, unfaded rectangle where a picture once hung. The
low ceiling is dark. Composition: her face left of centre with open dark space in front of her toward the right, her
eyes on the upper third.
```

---

## B · RELIEF (recommended)

### B1 · The Hall wide
```
STYLE (RELIEF): a frame from an animated film that looks like a colour relief print, woodcut and linocut. A carved
blue-black key block holds the image, and large areas stay solid black. Every light is a shape cut out of the black
with crisp, slightly irregular knife edges; half-tones are sparse parallel gouge strokes that follow the form. Colour
is flat spot ink on warm cream paper, never blended: cold pale cyan where screens light things, amber where lamps
light things, signal red only on red objects. Slight misregistration and paper grain. No drawn outlines: edges are
where ink stops. Only glowing screens are soft; everything else is cut. Faces are a few carved planes, calm, eyes
small dark shapes. Avoid: anime style, glossy eyes, airbrush glow, gradients, digital painting, lens flare, bokeh,
neon, centred portrait framing, 3D render, photorealism.
FRAME: wide 16:9 landscape; keep every important element inside the central horizontal band, because the top and
bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters or numbers anywhere; every screen is a blank,
evenly glowing surface.
SHOT: a vast night interior in one-point perspective, seen from high up at the back of the nave on its centre line,
with a 24 mm lens. The Hall of a broadcast ministry: a long nave of tapered board-formed concrete piers rising into
a ribbed vault lost in darkness; rows of operator desks under fitted canvas covers laced on with cord, receding in
straight lines; thin inlaid brass lines running along a dark terrazzo floor toward the far end; iron floor grilles
in the aisles, with dust rising from them into the light. The entire far wall is a grid of 12 by 8 deep concrete
niches, each holding one large old television tube with curved, round-cornered glass, all glowing the same pale
cold blue-white with nothing on them; this wall is the only strong light and throws the piers' long shadows down the
nave. Above the wall on the centre line hangs a riveted steel lamp box with a dark, unlit red glass front, and above
it a huge round clock face. High on the left wall, a dark glass gallery box projects over the nave with one small red
lamp glowing under it. Tarnished olive-black brass pneumatic tubes climb the piers and never shine warm. On the
centre line, a third of the way from the wall, one uncovered desk is lit by its own small glowing screens, and a small
woman sits at it with her back to us: a short black bob and a mustard-amber scarf, the only warm colour in the image.
She is tiny, less than a thumbnail in the vast space. Everything else falls into darkness.
```

### B2 · Nana's close-up
```
STYLE (RELIEF): a frame from an animated film that looks like a colour relief print, woodcut and linocut. A carved
blue-black key block holds the image, and large areas stay solid black. Every light is a shape cut out of the black
with crisp, slightly irregular knife edges; half-tones are sparse parallel gouge strokes that follow the form. Colour
is flat spot ink on warm cream paper, never blended: cold pale cyan where screens light things, amber where lamps
light things, signal red only on red objects. Slight misregistration and paper grain. No drawn outlines: edges are
where ink stops. Only glowing screens are soft; everything else is cut. Faces are a few carved planes, calm, eyes
small dark shapes. Avoid: anime style, glossy eyes, airbrush glow, gradients, digital painting, lens flare, bokeh,
neon, centred portrait framing, 3D render, photorealism.
FRAME: wide 16:9 landscape; keep every important element inside the central horizontal band, because the top and
bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters or numbers anywhere.
SHOT: a close-up of Nana, a small woman of 82, at night in her one-room flat, seen with a 50 mm lens at her eye level
as she sits in a low armchair. She has silver-white hair in a low bun held by a dark wooden hairpin, a soft round
face with deep lines, small dark eyes behind thin round gold wire-rimmed glasses, warm light-brown skin, small pearl
stud earrings, and a dark bottle-green knitted cardigan over a cream blouse. She holds an old cream bakelite
telephone handset to her ear on the side facing us; its coiled cord loops down out of frame. Her face is turned
three-quarters toward screen-right, her eyes resting on a television out of frame to the right. She is still and
composed, mouth closed, about to speak. Two lights meet on her face: cold pale blue-white from the television on the
right and warm amber from a table lamp on the left, the two colours meeting along the ridge of her nose. Behind her
at the left edge, a pleated parchment lampshade glows, scorched brown on one side, and throws a crisp arc of light on
faded wallpaper with a small leaf pattern; beside the arc is a pale, unfaded rectangle where a picture once hung. The
low ceiling is dark. Composition: her face left of centre with open dark space in front of her toward the right, her
eyes on the upper third.
```

---

## C · TABLEAU

### C1 · The Hall wide
```
STYLE (TABLEAU): a still from an adult stop-motion feature, photographed on a hand-built miniature set with a macro
lens. Puppets about 30 cm tall with realistic adult proportions, carved matte faces with fixed calm expressions and
glass-bead eyes, costumes of real knitted wool and felt. Sets of plaster, card, balsa and cast concrete, chipped,
dusty and repaired. Light comes only from tiny practical sources inside the set: cold blue-white glowing screens,
small warm tungsten bulbs, a red lamp; everything else falls into black. Shallow depth of field, fine 35 mm film
grain, muted greyed colour. Avoid: cute or cartoon proportions, big heads, clay smiles, shiny plastic, toy look,
pastel colours, bright even light, CGI, anime, photoreal humans, lens flare.
FRAME: wide 16:9 landscape; keep every important element inside the central horizontal band, because the top and
bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters or numbers anywhere; every screen is a blank,
evenly glowing surface.
SHOT: a vast night interior in one-point perspective, seen from high up at the back of the nave on its centre line,
with a 24 mm lens. The Hall of a broadcast ministry: a long nave of tapered board-formed concrete piers rising into
a ribbed vault lost in darkness; rows of operator desks under fitted canvas covers laced on with cord, receding in
straight lines; thin inlaid brass lines running along a dark terrazzo floor toward the far end; iron floor grilles
in the aisles, with dust rising from them into the light. The entire far wall is a grid of 12 by 8 deep concrete
niches, each holding one large old television tube with curved, round-cornered glass, all glowing the same pale
cold blue-white with nothing on them; this wall is the only strong light and throws the piers' long shadows down the
nave. Above the wall on the centre line hangs a riveted steel lamp box with a dark, unlit red glass front, and above
it a huge round clock face. High on the left wall, a dark glass gallery box projects over the nave with one small red
lamp glowing under it. Tarnished olive-black brass pneumatic tubes climb the piers and never shine warm. On the
centre line, a third of the way from the wall, one uncovered desk is lit by its own small glowing screens, and a small
woman sits at it with her back to us: a short black bob and a mustard-amber scarf, the only warm colour in the image.
She is tiny, less than a thumbnail in the vast space. Everything else falls into darkness.
```

### C2 · Nana's close-up
```
STYLE (TABLEAU): a still from an adult stop-motion feature, photographed on a hand-built miniature set with a macro
lens. Puppets about 30 cm tall with realistic adult proportions, carved matte faces with fixed calm expressions and
glass-bead eyes, costumes of real knitted wool and felt. Sets of plaster, card, balsa and cast concrete, chipped,
dusty and repaired. Light comes only from tiny practical sources inside the set: cold blue-white glowing screens,
small warm tungsten bulbs, a red lamp; everything else falls into black. Shallow depth of field, fine 35 mm film
grain, muted greyed colour. Avoid: cute or cartoon proportions, big heads, clay smiles, shiny plastic, toy look,
pastel colours, bright even light, CGI, anime, photoreal humans, lens flare.
FRAME: wide 16:9 landscape; keep every important element inside the central horizontal band, because the top and
bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters or numbers anywhere.
SHOT: a close-up of Nana, a small woman of 82, at night in her one-room flat, seen with a 50 mm lens at her eye level
as she sits in a low armchair. She has silver-white hair in a low bun held by a dark wooden hairpin, a soft round
face with deep lines, small dark eyes behind thin round gold wire-rimmed glasses, warm light-brown skin, small pearl
stud earrings, and a dark bottle-green knitted cardigan over a cream blouse. She holds an old cream bakelite
telephone handset to her ear on the side facing us; its coiled cord loops down out of frame. Her face is turned
three-quarters toward screen-right, her eyes resting on a television out of frame to the right. She is still and
composed, mouth closed, about to speak. Two lights meet on her face: cold pale blue-white from the television on the
right and warm amber from a table lamp on the left, the two colours meeting along the ridge of her nose. Behind her
at the left edge, a pleated parchment lampshade glows, scorched brown on one side, and throws a crisp arc of light on
faded wallpaper with a small leaf pattern; beside the arc is a pale, unfaded rectangle where a picture once hung. The
low ceiling is dark. Composition: her face left of centre with open dark space in front of her toward the right, her
eyes on the upper third.
```
