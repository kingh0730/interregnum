# Pilot lookdev: CONTINUITY

Six look-development images. Every keyframe prompt in `episodes/pilot/shots/NN/shot.md` names which of these to
attach (**Refs:**). None of them needs a transparent background. Keep the chosen image at the path below, with
candidates and rejects in `work/pilot/`.

```
tools/imagegen/gen.sh assets/pilot/lookdev/<file>.png "<prompt>" [refs...]
```

**Order and test-first rule.** Generate **LD1 alone first** and judge it against the checks below. It is the master
style frame: every other lookdev attaches it as a style reference. Then run LD2–LD6 (they can run in parallel), then
the keyframes. If LD1 misses the look, fix the prompt and retake before spending anything else.

**Acceptance checks** (Claude judges stills):
- The ink line is dark navy, not black; shadows are flat shapes with hard edges; there is glow only around light
  sources.
- There are only four color families: navy darkness, screen cyan, lamp amber, and a red accent.
- Screens are blank, evenly glowing panels, and there is no text anywhere.
- Faces have realistic proportions (no anime eyes). Each character sheet is the same person in every view.
- The Father resembles no real person. If a take reads as any real public figure, reject it and retake.

---

## Shared prompt blocks (restated in full inside every prompt that uses them)

**LOOK-WORLD** (location frames and world keyframes):
> STYLE: a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean, confident
> dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow only around
> light sources; subtle paper grain; realistic human proportions and faces (not chibi, no oversized eyes); simplified
> graphic backgrounds with bold silhouettes and large areas of dark negative space. PALETTE: deep ink-navy and
> blue-black darkness; cold pale-cyan light comes only from screens; warm amber light comes only from household lamps
> and warm objects; signal red only where described; no other saturated colors. LIGHT: one strong motivated light
> source, deep shadows, light haze. FRAME: wide 16:9 landscape; keep every important element inside the central
> horizontal band, because the top and bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters, numbers,
> logos or watermarks anywhere; every screen is a blank, evenly glowing panel.

**LOOK-BROADCAST** (the Father's broadcast frames k01, k02):
> STYLE: a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean, confident
> dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow; subtle paper
> grain; realistic human proportions and face (not chibi, no oversized eyes). This image is itself a television
> broadcast picture: it fills the whole 16:9 frame edge to edge, with no TV set and no screen border. PALETTE: deep
> blue backdrop, cool pale-cyan rim light, soft neutral studio key light on the face; no other saturated colors. No
> text, letters, numbers, logos or watermarks anywhere.

**LOOK-SHEET** (character model sheets):
> STYLE: a character model sheet for a premium adult 2D animated film. Hand-painted cel-animation look: clean,
> confident dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; subtle paper grain;
> realistic human proportions and faces (not chibi, no oversized eyes). Plain flat warm-grey background, even neutral
> light with a faint cool cyan rim. Every view shows exactly the same person with identical proportions, hair, face
> and costume. Wide 16:9 landscape sheet. No text, labels, letters, numbers, logos or watermarks anywhere.

**IDA:**
> IDA: a woman of 27, slim, with a short blunt jaw-length black bob and straight-cut bangs just above her eyebrows,
> dark brown eyes with tired lower lids, straight dark brows, a small straight nose, a small silver hoop earring in
> her left ear, warm light-olive skin; she wears a charcoal-grey ribbed turtleneck sweater, a hand-knitted
> mustard-amber wool scarf worn loosely around her neck, and a thin grey lanyard with a blank white ID card.

**NANA:**
> NANA: a small woman of 82 with silver-white hair in a low bun held by a dark wooden hairpin, a soft round face with
> deep smile lines, bright dark eyes behind thin round gold wire-rimmed glasses, warm light-brown skin, small pearl
> stud earrings; she wears a dark bottle-green knitted cardigan over a cream blouse with a tiny faded floral print.

**THE FATHER:**
> THE FATHER: an elderly man of about 85 with a broad, heavy-boned face, thick silver-white hair combed straight back
> from a high forehead, heavy white eyebrows, a short neatly trimmed white beard, deep-set dark eyes with a gentle
> grandfatherly expression, a small dark mole high on his left cheekbone, weathered warm-tan skin; he wears a plain
> charcoal high-collared wool coat buttoned to the throat, with a small round silver pin on the left side of the
> collar. He is an invented character and must not resemble any real person.

---

## LD1: `assets/pilot/lookdev/ld1_hall.png` (master style frame, generate first)

**Refs:** none. **Transparent:** no.
**Used by:** everything, as the style reference. Location refs for k03, k04, k05, k06, k14, k16, k18, k21, k22.

**Prompt:**
> STYLE: a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean, confident
> dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow only around
> light sources; subtle paper grain; realistic human proportions and faces (not chibi, no oversized eyes); simplified
> graphic backgrounds with bold silhouettes and large areas of dark negative space. PALETTE: deep ink-navy and
> blue-black darkness; cold pale-cyan light comes only from screens; warm amber light comes only from household lamps
> and warm objects; signal red only where described; no other saturated colors. LIGHT: one strong motivated light
> source, deep shadows, light haze. FRAME: wide 16:9 landscape; keep every important element inside the central
> horizontal band, because the top and bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters, numbers,
> logos or watermarks anywhere; every screen is a blank, evenly glowing panel.
> SUBJECT: a style frame for the film's main location, the Hall of a government broadcast ministry at night. A
> three-quarter view looking down a side aisle of an immense dark concrete hall shaped like the nave of a cathedral:
> massive square columns with brass pneumatic-tube pipes climbing them; long rows of operator desks draped in pale
> dust sheets; at the far end, a colossal flat wall of monitors (a grid of about 12 by 8 screens with thin black
> bezels), every screen a blank, evenly glowing pale cyan, throwing cold light and long shadows down the hall; above
> the monitor wall, a small rectangular signal-lamp box glowing dim red. In the middle distance one desk is uncovered
> and lit by two small monitors (blank glowing panels), with an empty chair and a small dented amber thermos flask
> on it. Cold light beams through haze, dust motes in the beams, the ceiling lost in darkness. Mood: vast, silent,
> sacred, lonely.

## LD2: `assets/pilot/lookdev/ld2_city.png`

**Refs:** `assets/pilot/lookdev/ld1_hall.png` (style only). **Transparent:** no.
**Used by:** k08, k17 (and k27 through k08).

**Prompt:**
> STYLE: a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean, confident
> dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow only around
> light sources; subtle paper grain; realistic human proportions and faces (not chibi, no oversized eyes); simplified
> graphic backgrounds with bold silhouettes and large areas of dark negative space. PALETTE: deep ink-navy and
> blue-black darkness; cold pale-cyan light comes only from screens; warm amber light comes only from household lamps
> and warm objects; signal red only where described; no other saturated colors. LIGHT: one strong motivated light
> source, deep shadows, light haze. FRAME: wide 16:9 landscape; keep every important element inside the central
> horizontal band, because the top and bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters, numbers,
> logos or watermarks anywhere; every screen is a blank, evenly glowing panel.
> Use the attached image only as a reference for drawing style, line quality and palette, not for content.
> SUBJECT: a style frame for the City at night in heavy rain. An elevated view from a footbridge along a straight
> canal running between dense concrete residential tower blocks of one identical design, stacked into the distance.
> Their facades are strict grids of small square windows, and almost every window glows the same flat cold cyan-blue,
> as if lit by television screens; exactly one window glows warm amber. Tram wires and a few laundry lines cross the
> view; far off, a tram with glowing windows crosses a bridge; on a taller building, a huge blank billboard screen
> glows plain cyan. Wet surfaces reflect the cyan light in long streaks; fine slanted rain. Mood: a whole city
> waiting in front of the same screen.

## LD3: `assets/pilot/lookdev/ld3_apartment.png`

**Refs:** `assets/pilot/lookdev/ld1_hall.png` (style only). **Transparent:** no.
**Used by:** k09, k11, k19, k24.

**Prompt:**
> STYLE: a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean, confident
> dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow only around
> light sources; subtle paper grain; realistic human proportions and faces (not chibi, no oversized eyes); simplified
> graphic backgrounds with bold silhouettes and large areas of dark negative space. PALETTE: deep ink-navy and
> blue-black darkness; cold pale-cyan light comes only from screens; warm amber light comes only from household lamps
> and warm objects; signal red only where described; no other saturated colors. LIGHT: one strong motivated light
> source, deep shadows, light haze. FRAME: wide 16:9 landscape; keep every important element inside the central
> horizontal band, because the top and bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters, numbers,
> logos or watermarks anywhere; every screen is a blank, evenly glowing panel.
> Use the attached image only as a reference for drawing style, line quality and palette, not for content.
> SUBJECT: a style frame for Nana's apartment at night, seen from the doorway, with nobody in the room. A small, tidy,
> old room: a worn armchair with a crocheted cover facing an old boxy television set on a lace-covered cabinet (its
> screen a blank, evenly glowing cyan panel); beside the armchair, a side table with a warm amber table lamp with a
> pleated fabric shade and an old cream-colored telephone with a rotary dial and a coiled cord; a small table with
> two teacups and an empty wooden chair; in the corner, a tiny two-ring stove with a small lidded pot; shelves with
> jars and a folded knitted blanket; a plain round wall clock with no numerals; a rain-streaked window showing
> cyan-lit tower blocks outside. The room is split between warm amber lamplight on the left and cold cyan television
> light on the right. Mood: warm, patient, a nightly ritual.

## LD4: `assets/pilot/lookdev/ld4_ida.png` (character sheet)

**Refs:** `assets/pilot/lookdev/ld1_hall.png` (style only). **Transparent:** no.
**Used by:** every Ida keyframe (k03, k04, k06, k07, k10, k12, k14, k15, k16, k18, k22, k23, k25).

**Prompt:**
> STYLE: a character model sheet for a premium adult 2D animated film. Hand-painted cel-animation look: clean,
> confident dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; subtle paper grain;
> realistic human proportions and faces (not chibi, no oversized eyes). Plain flat warm-grey background, even neutral
> light with a faint cool cyan rim. Every view shows exactly the same person with identical proportions, hair, face
> and costume. Wide 16:9 landscape sheet. No text, labels, letters, numbers, logos or watermarks anywhere.
> Use the attached image only as a reference for drawing style and palette, not for content.
> CHARACTER: IDA: a woman of 27, slim, with a short blunt jaw-length black bob and straight-cut bangs just above her
> eyebrows, dark brown eyes with tired lower lids, straight dark brows, a small straight nose, a small silver hoop
> earring in her left ear, warm light-olive skin; she wears a charcoal-grey ribbed turtleneck sweater, a hand-knitted
> mustard-amber wool scarf worn loosely around her neck, and a thin grey lanyard with a blank white ID card.
> LAYOUT: top row, four full-body views of Ida standing with arms relaxed (front, three-quarter, side profile, back);
> bottom row, four head-and-shoulders close-ups of Ida with different expressions: (1) focused and tired, lit cyan
> from one side; (2) hesitant, eyes lifted; (3) stunned, eyes glistening; (4) eyes closed, crying and laughing at
> once. Her scarf is the only warm color on the sheet.

## LD5: `assets/pilot/lookdev/ld5_nana.png` (character sheet)

**Refs:** `assets/pilot/lookdev/ld1_hall.png` (style only). **Transparent:** no.
**Used by:** k09, k11, k13, k19, k24.

**Prompt:**
> STYLE: a character model sheet for a premium adult 2D animated film. Hand-painted cel-animation look: clean,
> confident dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; subtle paper grain;
> realistic human proportions and faces (not chibi, no oversized eyes). Plain flat warm-grey background, even neutral
> light with a faint cool cyan rim. Every view shows exactly the same person with identical proportions, hair, face
> and costume. Wide 16:9 landscape sheet. No text, labels, letters, numbers, logos or watermarks anywhere.
> Use the attached image only as a reference for drawing style and palette, not for content.
> CHARACTER: NANA: a small woman of 82 with silver-white hair in a low bun held by a dark wooden hairpin, a soft round
> face with deep smile lines, bright dark eyes behind thin round gold wire-rimmed glasses, warm light-brown skin,
> small pearl stud earrings; she wears a dark bottle-green knitted cardigan over a cream blouse with a tiny faded
> floral print.
> LAYOUT: top row, four full-body views of Nana standing, slightly stooped, hands folded (front, three-quarter, side
> profile, back); bottom row, four head-and-shoulders close-ups with different expressions: (1) attentive, watching
> something; (2) a small private smile; (3) tender, eyes glistening; (4) a soft laugh with eyes closed.

## LD6: `assets/pilot/lookdev/ld6_father.png` (character sheet)

**Refs:** `assets/pilot/lookdev/ld1_hall.png` (style only). **Transparent:** no.
**Used by:** k01 (then k02 → k20 chain from k01).

**Prompt:**
> STYLE: a character model sheet for a premium adult 2D animated film. Hand-painted cel-animation look: clean,
> confident dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; subtle paper grain;
> realistic human proportions and faces (not chibi, no oversized eyes). Plain flat warm-grey background, even neutral
> light with a faint cool cyan rim. Every view shows exactly the same person with identical proportions, hair, face
> and costume. Wide 16:9 landscape sheet. No text, labels, letters, numbers, logos or watermarks anywhere.
> Use the attached image only as a reference for drawing style and palette, not for content.
> CHARACTER: THE FATHER: an elderly man of about 85 with a broad, heavy-boned face, thick silver-white hair combed
> straight back from a high forehead, heavy white eyebrows, a short neatly trimmed white beard, deep-set dark eyes with
> a gentle grandfatherly expression, a small dark mole high on his left cheekbone, weathered warm-tan skin; he wears a
> plain charcoal high-collared wool coat buttoned to the throat, with a small round silver pin on the left side of
> the collar. He is an invented character and must not resemble any real person.
> LAYOUT: top row, three head-and-shoulders views (front, looking straight at the viewer with a calm, warm
> half-smile; three-quarter; side profile); bottom row, a full-body front view standing upright with hands folded, a
> close-up with a neutral expression, and a close-up with the eyes gently closed as if peacefully asleep. The mole is
> on his left cheekbone in every view (on the right side of the image in the front views).

---

## Keyframe → lookdev map (quick reference)

| Keyframe | Attach |
|---|---|
| k01 | ld6_father, ld1_hall |
| k02 | ld6_father, k01 |
| k03, k14 | ld1_hall, ld4_ida (k14 also k03) |
| k04, k18 | ld4_ida, ld1_hall (k18 also k04) |
| k05, k16, k21, k22 | ld1_hall (k16, k22 also ld4_ida) |
| k06 | ld4_ida, ld1_hall |
| k07, k10, k12, k15, k23, k25 | ld4_ida + the previous Ida keyframe named in the shot |
| k08, k17 | ld2_city |
| k09, k11, k13, k19, k24 | ld5_nana, ld3_apartment (+ previous Nana keyframe named in the shot) |
| k20, k26, k27 | edits of k02, k03, k08 (attach only the image being edited) |
