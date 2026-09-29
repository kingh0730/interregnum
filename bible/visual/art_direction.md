# Art direction: three candidates

> **Revision (2026-09-29): the Copy Rule is replaced by the Engraving Rule.** In the v3 reel the smooth, tonal Father
> read as a style inconsistency, not as the machine's image. The Father is now a steel-engraved portrait in the manner
> of a banknote or stamp: fine, perfectly regular engraved lines, stipple and guilloche, with flawless registration.
> He shares the film's ink-on-paper medium, while the machine precision still sets him apart from the hand-cut world.
> The full rule text is in the `k01_father_mcu` prompt of `episodes/pilot/images_v3.json`, which is authoritative over
> any "COPY RULE" wording still quoted in the shot files.
>
> **The medium rule (series-wide).** By default, a character differs from the world in *technique*, not *medium*.
> A change of medium is allowed only when all three conditions hold:
> 1. **Fully committed.** It is truly another medium (real photographic footage, archive video, live action, a
>    different animation technique) and not a half step. The v3 Father failed because he was smoother than the
>    woodcut but not a photograph: an uncanny valley of style that reads as a mistake.
> 2. **Motivated.** The story explains it: another world, a machine's output, a memory, a document.
> 3. **Set up or saved.** Either the audience learns the rule early (*Roger Rabbit*, *Spider-Verse*, *The Wizard of
>    Oz*), or the break happens once, as a revelation it has earned (*Waltz with Bashir*'s final archive footage,
>    *The Lego Movie*'s live-action turn).


How INTERREGNUM is drawn. `production_design.md` defines what things are and `cinematography.md` how they're shot;
this file defines the medium. There are three candidate directions, each with a ready-to-run Codex style block,
followed by a recommendation. `test_frames.md` holds the six test prompts that let the showrunner compare them.

The series may change medium per episode, as *Love, Death & Robots* does. The pilot's direction sets the house
standard: whichever medium an episode uses, the series rules below hold.

---

## Series rules (every direction, every episode)
1. **The Copy Rule.** In the pilot, the generated man is the only frictionless image: even soft light, perfect
   symmetry, smooth gradients, skin without texture. The model's default polish is quarantined in the one thing that
   is generated. Everything alive is made by hand and shows it. Each later episode names its own "copy", the image that
   belongs to the machine or the regime, and gives only that image the frictionless look.
2. **Darkness is the default and light has a source.** Every lit surface can point to its lamp, tube or window. Nothing
   is lit by the air. At least half of a night frame is near-black.
3. **Silhouette first.** Threshold any keyframe at 25 % luminance: every figure and key object must still read.
4. **Faces are restrained.** Eyes have no highlights, and nobody opens their mouth unless they're speaking. Keyframes
   never show tears, grins or anguish. The acting is staging and cutting (`cinematography.md` §8).
5. **Palette semantics are physics** (`production_design.md` §2): cold is the copy, amber the living hand, red the
   Committee, rose the new. There is no sodium light, and brass in the Hall is never warm.
6. **Texture must survive motion.** Video models make fine surface texture swim. Put texture in static things (sets,
   solid blacks, walls) and keep figures, hands and faces simple. Add paper grain or film grain as a static layer in
   comp, never as painted per-frame detail.
7. **Retire the v1 lookdev as style references.** `ld1`–`ld6` would pull every prompt back to the default look. Keep
   them as story references only; new sheets are painted in the chosen direction.

### What Codex does by default, and the counter-move
| Default | Counter (write it into the prompt) |
|---|---|
| Even, soft light everywhere; lifted blacks | One named hard source; "everything else falls into black" |
| Centred, eye-level medium shots | Name the lens, camera height and the subject's position on the frame (`cinematography.md` §3) |
| Anime eyes: large, glossy, with a highlight | "Eyes are small dark shapes without highlights" |
| Rain-soaked neon-city wallpaper | Mercury-cold streets, rain as graphic design, one warm window |
| Airbrushed glow halos, god rays, bokeh balls | "Light is a shape where it lands, with no glow"; only screens glow |
| Generic, clean, unowned objects | Named materials and one repair per object (`production_design.md` §2) |
| Teal-and-orange grading | The exact palette, named per source |
| Detail spread evenly | Detail at the focal point; the rest simplified |
| Emotion on the face | A physical state: posture, hands, where the eyes rest |

---

## A. STILL LIFE (painted cinema)

**Thesis.** In French a still life is *nature morte*, dead nature, and the pilot is a still life: a dead man arranged
to look alive, and a woman keeping still in front of him every night. STILL LIFE paints the film like a room in which
someone is waiting: gouache planes, lost edges and patient light. Nothing moves but light, and nothing is outlined.
Paint suits a film about watching, because the audience watches the way Nana does, and a painted room rewards waiting.

**Lineage (learn the method, don't copy the pictures)**
- **Vilhelm Hammershøi:** grey interiors, figures seen from behind, doors opening onto more rooms. How one person can
  make a room lonely, and how a back can act.
- **James McNeill Whistler's Nocturnes:** blue night with a few warm points dissolving in haze. The v1 visual
  language, "Nocturne in two lights", is his method, and here it gets his restraint too.
- **Edward Hopper:** a lit interior seen from the dark outside, and figures alone in hard geometric light. The city
  window and Nana's room.
- **Giorgio Morandi:** the dignity of a few plain objects: the two cups, the pot, the thermos.
- **Michaël Dudok de Wit** (*Father and Daughter*, *The Red Turtle*): tiny figures in large spaces, faces reduced to
  almost nothing, grief carried by distance, weather and time.
- **Aleksandr Petrov's paint-on-glass animation:** how paint itself can move without losing the hand.
- **Isao Takahata's *The Tale of the Princess Kaguya*:** negative space, and a line that loosens only when feeling
  breaks through. Save that loosening for shot 42.

**Palette.** Greyed, mixed pigment, desaturated everywhere except at the sources.
Night blue-black `#1B2230` (indigo and umber), night mids `#2E3A4A`, phosphor light `#CFEFEA` with half-tones
`#7FC9C9`, lamp light `#E3A04A` and `#F2D29B`, red `#B8392C`, paper `#E6DCC6`. Dawn rose `#E9BDB3` appears in 44 only.

**Texture and medium.** Opaque gouache on warm-grey toned paper. Dry-brush edges, paper tooth in the lights, and flat
planes with the hand's slight unevenness inside them. The only gradients are thin glazes near light sources.

**Line.** None. Form is one value against another, with a few dark accents where planes meet (under a chin, the edge
of a desk). In darkness, edges are lost entirely.

**Light.** Opaque colour painted where it lands, with a shape: a trapezoid on the floor, an arc on the wall. No
halos. The lightest value appears only at the source. Haze is a lighter flat layer, not a gradient.

**Faces.** Three or four planes. The eyes are one dark shape each with no highlight, and the mouth is a short stroke.
Tears are never painted. The face changes through head angle and light, not features. Close-ups are rare and cropped:
a cheek, an ear, the rim of the glasses.

**Risks.** It is the closest of the three to Codex's own painterly default, so it is the most likely to slide back
toward it. Gouache texture can swim in Seedance, and soft edges make comp masks harder.

**Codex style block (leads every prompt):**
> STYLE (STILL LIFE): a frame from a hand-painted animated feature for adults, opaque gouache on warm-grey toned
> paper. Forms are flat, slightly uneven planes of greyed colour with dry-brush edges and visible paper tooth; no ink
> outlines, and in shadow the edges dissolve. Night is deep indigo-grey. Light is painted as chalky opaque colour
> exactly where it lands, only from sources in the scene, with a crisp shape and no glow: pale cold blue-white from
> screens, warm sienna-gold from lamps, deep red only on red objects. Figures are still and quiet: faces of three or
> four planes, eyes small dark shapes without highlights. Detail gathers at the focal point; the rest is simplified.
> Avoid: anime style, big glossy eyes, airbrush gradients, glow halos, light rays, lens flare, bokeh, neon,
> teal-and-orange colour, 3D render, photorealism.

---

## B. RELIEF (the colour woodcut)

**Thesis.** In relief printing you carve away everything that should be light, and what remains prints black. **Every
light in this film is a cut in the dark, made by a hand.** That is the pilot's thesis turned into a technique: the new
has to be made by a human hand. A block also prints the same image again and again, which is continuity itself. The
one image that is not carved is the Father: smooth, tonal and frictionless (the Copy Rule), so the audience feels the
machine's picture against a world cut by hand. At the end, the dawn rose is a new block cut for a single image.
And the film ends in relief: a woman laughing on the phone.

**Lineage (learn the method, don't copy the pictures)**
- **Félix Vallotton's woodcuts:** flat black masses, intimate interiors, crowds with umbrellas in the rain. Learn how a
  single white shape can carry a room, and how a crowd becomes one black form (shot 30).
- **Frans Masereel's wordless woodcut novels:** the city, the crowd and the one person, told in black and white
  without words. Learn how to tell a story in held images.
- **Kawase Hasui's night and rain prints:** a lit window in blue dusk, rain as cut lines, one lamp in the snow. The
  closest ancestor of the city shots and the warm window.
- **Käthe Kollwitz's woodcuts:** old women and grief with dignity and no sentiment, all in black. The model for Nana.
- **Lynd Ward's wood engravings:** night cities in carved line, and how density of cutting becomes value.
- **Genndy Tartakovsky** (*Samurai Jack*, *Primal*): silhouette staging, silence, scale, wide negative space and
  backgrounds as flat colour shapes. Proof that this works in motion, without dialogue.
- **Robert Valley's *Zima Blue*:** flat planes, huge empty fields, a small figure before a monumental shape. Already
  cited in `episode.md` as kin.
- **Cartoon Saloon's *Wolfwalkers*:** woodcut texture and carved line surviving animation.
- ***Waltz with Bashir*:** black silhouettes against one coloured light.
- **Denis Villeneuve and Roger Deakins** (*Blade Runner 2049*, *Dune*): a tiny figure against a monolith, fields of
  flat colour. The composition this print style makes easy.

**Palette (spot inks on paper; hex for comp).** Each area is one ink, and inks are never blended.
Key block `#11151F` (blue-black); cold ink `#8ED8D6`, with `#D8F4F1` only at sources; amber ink `#E9A23B`; red ink
`#CC3A2B`; paper `#E8DDC4` (showing only where the block is cut away: rain, highlights, paper objects). Rose ink
`#EDB9B0` is printed only in 44 and 45. Cold is never printed over amber, which keeps the two lights from muddying
each other. Misregistration runs 1–3 px per ink.

**Texture and medium.** A colour woodcut and linocut. The black key block carries the gouge marks, and parallel carving
strokes are the only way to make a middle value. Strokes follow the form (curved on a cheek, straight on concrete).
Faint wood grain shows in large flat areas like the black sky and the Hall's walls. Paper grain and ink squash are a
static comp layer.

**Line.** There is no drawn outline. A line is where the black stops: sharp and slightly irregular, the knife's hand.
The only thin lines are carved light lines: rain, tram wires, a rim light along a shoulder.

**Light.** Light is a cut shape. A rim light is a carved line along a silhouette, and a pool of light is a shape cut
out of the floor. Haze is parallel hatching that gets denser toward its source. **Only phosphor glows.** The tubes'
soft bloom is added in comp, the one smooth light in a carved world, and by the Copy Rule it belongs to the machine.

**Faces.** Three to five flat shapes of ink and one cut edge where the light falls. Eyes are small dark almonds with no
highlight, and the mouth is one short cut. On Nana, the ridge of the nose is where the cold block and the amber block
meet. Tears are never carved. Expression lives in the tilt of a head and the distance between two figures.

**Risks.** Carved texture can swim in Seedance. Mitigation: keep texture in static areas and solid blacks, keep figures
flat, and add the grain in comp. Held images can read as a motion comic, which the cinematography rules and Seedance's
motion guard against. Four minutes of print could feel monotonous, which the Father's smooth frames and the dawn break.

**Codex style block (leads every prompt):**
> STYLE (RELIEF): a frame from an animated film that looks like a colour relief print, woodcut and linocut. A carved
> blue-black key block holds the image, and large areas stay solid black. Every light is a shape cut out of the black
> with crisp, slightly irregular knife edges; half-tones are sparse parallel gouge strokes that follow the form. Colour
> is flat spot ink on warm cream paper, never blended: cold pale cyan where screens light things, amber where lamps
> light things, signal red only on red objects. Slight misregistration and paper grain. No drawn outlines: edges are
> where ink stops. Only glowing screens are soft; everything else is cut. Faces are a few carved planes, calm, eyes
> small dark shapes. Avoid: anime style, glossy eyes, airbrush glow, gradients, digital painting, lens flare, bokeh,
> neon, centred portrait framing, 3D render, photorealism.

---

## C. TABLEAU (the miniature)

**Thesis.** A dead man puppeted by a machine, and a nation holding still for a picture every night at nine: the pilot
is about puppetry and the *tableau vivant*. Stop-motion is the art of making still things seem alive one frame at a
time. That is Ida's job, the Apparatus's job and this production's job. **Puppets cannot over-emote.** Their carved
faces barely change, so light, angle and the cut do the acting: the Kuleshov rule built into the medium. And the
material culture of `production_design.md` §2 simply gets built, in brass, concrete, wool and bakelite at 1:6 scale,
with real dust. By the Copy Rule, the Father would be the one figure who is not a puppet: a seamless, poreless digital
sculpture among seamed, hand-made people.

**Lineage (learn the method, don't copy the pictures)**
- **Jiří Trnka:** puppets with fixed carved faces whose expression changes with light and the tilt of the head. The
  founding principle for acting without faces.
- **The Brothers Quay** (*Street of Crocodiles*): dust, screws, dim machinery and the uncanny life of objects. The Hall
  and the Engine.
- **Emma de Swaef and Marc James Roels** (the first chapter of *The House*): felt puppets carrying adult dread and
  melancholy without cuteness.
- **Duke Johnson and Charlie Kaufman's *Anomalisa*:** the visible seams of replacement faces, and loneliness in
  ordinary rooms.
- **Adam Elliot** (*Mary and Max*): a muted palette, dignity and loneliness at small scale.
- **Roy Andersson:** static tableaux of pale institutions, deadpan bureaucracy and figures holding still in deep
  space. The Ministry's tone.
- **Joseph Cornell's boxes:** assembled worlds in shallow niches. The columbarium Wall is 96 Cornell boxes.
- **Edward Kienholz's tableaux:** whole rooms built from real objects; an old woman waiting among her things.

**Palette (practical light, not paint).** The palette comes from bulbs and gels: phosphor blue-white (~9000 K) on real
surfaces, tungsten amber (~2700 K), red lacquer and red lamps. Materials are the greys of concrete and enamel. All
else is muted, and black is black velvet. Dawn is a real sky-light change in 44.

**Texture and medium.** Puppets about 30 cm tall with adult proportions: carved resin or wooden faces, glass-bead
eyes, wire and fibre hair, real knitted wool. Sets of plaster, card, balsa and cast resin. Rain is glass beads and
threads. The film is shot on a macro lens with shallow depth of field and 35 mm grain, and held on twos (12 poses a
second) in comp.

**Line.** None. It's photographic, and edges are real material edges.

**Light.** Real miniature practicals (grain-of-wheat bulbs, small glowing screens) and hard, small sources, with haze
from real fog. Black is velvet.

**Faces.** Two or three replacement faces per character at most: neutral, eyes closed, one small smile. Expression is
head tilt and light. Faint seams across the brow show the replacement line.

**Risks.** Codex's idea of stop-motion drifts to cute (big heads, clay smiles, toy plastic), so the block has to fight
it hard. Seedance may animate puppets too smoothly (fix by holding on twos) and may deform carved faces for lip-sync.
Felt and hair can swim. It needs a new motion bake-off, and it's the hardest of the three to keep consistent.

**Codex style block (leads every prompt):**
> STYLE (TABLEAU): a still from an adult stop-motion feature, photographed on a hand-built miniature set with a macro
> lens. Puppets about 30 cm tall with realistic adult proportions, carved matte faces with fixed calm expressions and
> glass-bead eyes, costumes of real knitted wool and felt. Sets of plaster, card, balsa and cast concrete, chipped,
> dusty and repaired. Light comes only from tiny practical sources inside the set: cold blue-white glowing screens,
> small warm tungsten bulbs, a red lamp; everything else falls into black. Shallow depth of field, fine 35 mm film
> grain, muted greyed colour. Avoid: cute or cartoon proportions, big heads, clay smiles, shiny plastic, toy look,
> pastel colours, bright even light, CGI, anime, photoreal humans, lens flare.

---

## Recommendation: RELIEF

**RELIEF is the pick.**
1. **It is the theme.** Light cut by hand out of the dark is the pilot's argument (the new has to be made by a human
   hand), and a block printed night after night is continuity. It also gives the Copy Rule its strongest contrast: the
   Father's smooth, tonal, frictionless face against a world cut with a knife.
2. **It is furthest from Codex's default.** Solid black, flat spot inks and no gradients are easy to state and easy to
   check. Claude can measure palette compliance by counting inks in a still, and check the silhouette test by
   threshold.
3. **It survives Seedance.** The bake-off showed flat colour holding identity and style across 4–10 s. Carving lives
   in static areas and grain in comp, so the figures stay flat and stable.
4. **It makes comp easy.** Flat inks make trivial masks for screens, windows, the red phone and the window wave.
5. **It builds restraint in.** A face of four carved planes cannot mug, so the Kuleshov rule becomes the default.
6. **It reads at any size.** Silhouettes and black fields make the cathedral-scale images (a woman the size of a
   thumbnail under a 20-metre face) read instantly, even as a phone thumbnail.

**Runner-up: TABLEAU.** It's the strongest idea on paper: stop-motion *is* the story's craft, and puppets can't
over-emote. But it carries the most new risk (cute drift, smooth motion, a new bake-off) and would be the costliest to
hold consistent. Worth testing; not worth betting the pilot on before the test.

**STILL LIFE** is closest to the anime features the showrunner loves, and for the same reason it's the most likely
to slide back into the look he objected to.

**Considered and rejected: photoreal.** It has the highest identity drift and the highest uncanny risk, and a
photoreal patriarch invites resemblance to real people, which the public-repo guardrail forbids.

**The decision is the showrunner's, on the evidence of `test_frames.md`.** If he prefers another direction on seeing
the frames, every other file in `bible/visual/` holds for it: the production design, the camera and the acting rules
don't depend on the medium.

### After the pick
1. Run the six test frames (`test_frames.md`), then one 5 s Seedance motion test of the winning Nana close-up at
   480p (about $1.10) to check texture in motion. The showrunner watches it.
2. Paint new character sheets (Ida, Nana, the Father under the Copy Rule) and location lookdev (the Hall, Desk 4, the
   Proof, Nana's flat, the city) in the chosen direction. These replace `ld1`–`ld6` as refs.
3. Regenerate the keyframes and the new hardware plates (`production_design.md` §10): about 45 Codex images, the size
   of the v1 pass.
4. Re-render the v2 Seedance shots: about 113 s of clips, roughly $100–130 with two 480p drafts each. Estimate
   before running, and test small first.
