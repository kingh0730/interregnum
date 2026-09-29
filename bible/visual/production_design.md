# Production design: the world of CONTINUITY

The pilot's world as designed objects. It answers the showrunner's note on the v1 reel ("it looks like claude
generated some websites") and the director's diagnosis. The in-world screens were 2020s web UI (Avenir, Menlo and DIN
on dark cards with cyan accents), and the Codex frames were the model's default polished rainy-city anime. In the
redesign every screen becomes a machine, every machine is made of something, and every material has a history.

Companion files: `art_direction.md` (how it's drawn), `cinematography.md` (how it's shot), `test_frames.md` (first
Codex tests). The story, dialogue, timing and palette semantics of `episodes/pilot/episode.md` stand. What changes is
what things *are*. Where a change touches a shot spec it's marked **→ shot NN**, for the director to fold into that
`shot.md`.

---

## 1. The thesis: Year One, maintained

The nation counts its years from the first Evening Address, and it is now Year 41. Everything the state owns was
designed in its first decade: the Ministry, the towers, the trams, the telephones, the television sets and the
alphabet. None of it has been replaced since, because replacing something would admit that the Father's era can end.
The law behind this (never stated on screen) is the **Continuity Statute**: *nothing the Father saw may be replaced by
anything he did not see.*

That gives the world its three visible rules.

1. **Everything is old and cared for.** Objects are repaired, never renewed: re-enamelled over chips, re-soldered,
   re-wired with a newer cable taped to an older one, re-labelled with a newer label over a fading one. Wear shows
   where hands go: bare steel on console edges, brass polished bright only on the lip of the tube cradle, a thumb-worn
   hollow on a knob. **Every object in a frame should show one repair.**
2. **The new hides inside the old.** The machine that now generates the Father was built after his death, but the
   Statute forced it into Year One cabinets, tubes and keyboards. The design never shows a modern object. It shows
   old hardware doing something it was never built to do, and that anachronism *is* the pilot's subject: a new mind
   forced to wear the old body.
3. **The state writes on a grid; people write by hand.** Every official letter, number and emblem is constructed
   with a ruler, compass and module grid (§5). The only freehand marks in the world are human: Ida's pencil, an
   archivist's grease pencil, a doctor's tag, Nana's crochet. Wherever the film needs to say "a person did this",
   it shows handwriting or handwork.

**Era-feel, in one line for every prompt:** *an invented mid-century state, frozen for forty years: poured
concrete, tarnished brass, enamelled steel, bakelite, paper, glass tubes and phosphor light; everything old,
repaired and still running.*

### Placelessness (the guardrail, applied to design)
The nation belongs to no real country. The mid-century mood comes from many places at once, and no single place may
dominate.
- **No real scripts or flags,** and no real uniforms, insignia, car or tram models, or brand shapes. The state's
  letters are Latin capitals built on its own grid (§5), and it prefers numbers to words.
- **Invented signatures:** each recurring structure carries one invented feature that no real city has (listed per
  location below). If a detail could be traced to a real city, change it.
- **Costume:** the Father's coat must not read as a military tunic, a cassock, or any real statesman's signature
  suit. Give it a soft rolled collar, a concealed placket and no visible pockets or buttons (§7). Nana and Ida wear
  ordinary, placeless knitwear.
- **Hardware:** generic nouns only in prompts ("split-flap display", "teleprinter", "flatbed film viewer"), never a
  maker's name. Shapes are invented: no famous clock face, telephone or terminal silhouette.

---

## 2. Material culture

### Materials and finishes (the words to use in prompts)
| Material | Where | How it looks after 41 years |
|---|---|---|
| **Board-formed concrete** | the Ministry, the towers, the canal walls | Plank grain printed in the surface; a grid of round form-tie holes; water stains under every ledge; patches of newer, paler concrete |
| **Ministry grey enamel** | consoles, cabinets, the State Receiver TV, desk phones | Blue-grey hammer-tone paint, re-sprayed over chips so edges show layers; bare steel where hands rest |
| **Tarnished brass** | pneumatic tubes, cradles, pipe junctions, floor inlays | Olive-black patina with green at the joints; bright only where touched |
| **Bakelite / phenolic** | knobs, telephone bodies, the red phone | Deep brown-black or cast colour; fine crazing; a warm sheen on the knobs |
| **Engraved plates** | every label and legend | Engraved and filled with cream paint; the fill chipped from some letters |
| **Glass** | tubes, lamp lenses, cast signal glass, glass-block stair towers | Curved faceplates with dust and a hand smear; frosted and cast lenses |
| **Paper** | orders, forms, labels, film leader, tags | Onionskin carbons, ruled forms, fanfold log paper; yellowed at the edges |
| **Wool, felt, canvas** | Ida's scarf, Nana's cardigan, the desk covers | Visible stitches; darns in a slightly different yarn; canvas sagging on its ties |
| **Enamel ware** | Nana's pot, Ida's thermos | Amber enamel, chipped to black iron at the rims |
| **Wood** | Nana's clock, chair arms, the wall unit | Plywood veneer lifting at the corners; varnish worn pale where hands rest |

**The desk covers:** the v1 draped white sheets read as ghost costumes. The redesign uses **fitted canvas covers
laced on with cord**, each stencilled with its desk number (too small to read in a wide). The operators were
dismissed on 11 March and the covers went on the next day. In a wide, 400 identical shrouds with numbers read as a
field of graves.

### The light rules (palette semantics as physics)
The palette in `episode.md` stays exactly as it is. What changes is that every colour now has a physical source,
and the meaning follows from that source.

| Colour | Physical source | Meaning |
|---|---|---|
| **Cold phosphor** (broadcast cyan, `#5FE1E6` bloom, `#DDFBFA` core) | cathode-ray tubes, vector strokes, vacuum-fluorescent digits, mercury-vapour street lamps | What the machine makes and the state transmits: the copy |
| **Warm filament** (lamp amber, `#F2A441` bloom, `#FFD9A0` core) | tungsten bulbs, flame, the warm layer of the operator tube (§4), the archive's film lamp | What a living hand made or lit |
| **Signal red** (`#E0412F`) | the Committee's lamps, the red phone, rubber stamps, lacquer seals, the commit key, ON AIR, the mast's beacon | The Committee's authority |
| **Cream** (`#E9E2D0`) | paper, engraved fill, bone china | Record, paper, the handmade |
| **Dawn rose** (`#F4C6C0`) | the sky in shot 44, and the light on the end card (§9) | The new: it appears once |

- **No sodium light anywhere.** Street lighting is mercury vapour (cold blue-green white), so warm light in the city
  can only mean a home.
- **Brass is never warm in the Hall.** In v1 (`ld1_hall.png`) the pipes glow yellow and compete with Ida's scarf.
  In the redesign, brass is olive-black with cold highlights, and the first warm thing in the Hall is her scarf.
- **Neutrals:** concrete blue-grey, Ministry grey, bakelite brown-black. Nana's cardigan is a dark, greyed bottle
  green, the only other hue allowed, and it stays near-black at night.

---

## 3. The Ministry of Continuity

### The Hall
Built in Year One as the nation's broadcast house, the Hall is laid out like a basilica: a nave 120 m long, side
aisles behind rows of piers, and at the far end, where an altar would be, the Wall.

- **Piers:** square, board-formed concrete piers taper as they rise 30 m into a ribbed vault. The vault is never lit;
  only its lowest ribs catch the Wall's light. Each pier carries a vertical run of pneumatic tubes, a cast-iron horn
  loudspeaker (the PA) pointing down the nave, and an enamel plate with its bay number.
- **Floor:** dark terrazzo with **inlaid brass ledger lines** running the length of the nave, one per desk row, like
  the ruled lines of an account book. At the crossing, a brass Lamp emblem 4 m across is set into the floor, worn
  smooth along the centre aisle. Cast-iron **floor grilles** breathe the Engine's cooling air from below (§4), and
  the dust in the light rises from them, so the drifting dust always has a cause.
- **Desks:** 400 operator desks in straight rows under fitted canvas covers (§2). Unlit enamel pendant lamps hang over
  them on long cords.
- **The Wall (invented signature):** the apse wall is a **columbarium of 96 niches**, 12 across and 8 high, cast in
  the same concrete as the piers. Each niche is 1.4 m deep and holds one large broadcast tube with a curved,
  round-cornered glass face. The mullions between niches are thick, a sixth of a niche's width, so the Father's face
  reads *through a lattice*. From an angle, the depth of the niches hides slivers of his face. It is not a video wall
  but a wall of urns, each holding a piece of him. Specification in §4.
- **The axis:** straight up the nave's centre line are Desk 4, the Wall, the **ON AIR lamp** and, highest, the
  **Air Clock** (a 3 m slave clock face above a split-flap board). The one lit desk, the face, the lamp and the time
  all line up in one-point perspective. It's the altar axis, and power reads as a straight line.
- **The gallery (invented signature):** high on the left side wall, a **dark glass box** projects over the nave like
  an organ loft. It is never lit inside. A single red pilot lamp under its sill glows when the Committee is watching.
  The pneumatic tubes climb the piers to it, and the Red Line's cable runs to it. No face is ever seen there.
- **Invented signature, overall:** the columbarium Wall, the brass ledger floor and the dark gallery. Together they
  make a church of broadcasting that belongs to no real faith or nation.

### Desk 4
The only uncovered desk, on the axis, about 40 m in front of the Wall (a third of the nave). A steel console in Ministry grey, its armrest
worn to bare metal. Layout from Ida's seat (keep it identical in every shot):

| Position | Object |
|---|---|
| Centre | **Script Terminal**: keyboard at her hands, its tube above |
| Left of centre | **the Proof**: the large colour monitor, angled toward her; the light pen hangs on a hook at its side |
| Right of centre | **Corrections panel**: a column of legend lamps; the **flap repeater** (TO AIR) on top |
| Far right | **Log Printer**: a teleprinter on its own stand, fanfold paper in a basket below |
| Far left | **Archive Reader**: a light table set into the desk's left wing; above it, the **pneumatic cradle** where the tube comes down from the pier |
| Front left | **the Red Line** (the Committee's red phone) |
| Front right | **the House Line** (a grey desk phone) and Nana's amber thermos |

### How the Father is made each night
The pilot's process as physical work, so every screen has a reason to show what it shows.
1. **20:30:** the Engine (§4) renders tonight's picture from the Script and the Archive. The Proof shows the result.
2. **20:45:** Ida runs a **calibration replay** of last night's frames (hence REPLAY NIGHT 211 in shot 04). Where the
   face has drifted, the stroke overlay flags it in red. She touches the glass with the **light pen** and drags the
   feature home, and each correction locks on a relay with a click (shot 06).
3. **20:55:** she types tonight's words into the Script Terminal. The Engine offers the next words as it types.
4. **21:00:** the Air Clock's flaps reach 00:00, the ON AIR lamp lights, and the telecine runs the **Lighting** (the
   ident film, §7). The Father then speaks to the nation from all 96 niches of the Wall and every State Receiver.
5. **The Committee** watches from the gallery. When the red pilot lamp is lit, a repeater lamp marked VIEWING lights
   on her terminal (shot 24).

---

## 4. The Apparatus: the broadcast machine's hardware

The in-world name for everything at Desk 4 plus the Engine below. It uses no flat panels, touchscreens, mice, windows,
icons, cards or sans-serif UI. Its displays are four kinds of tube (raster colour, raster monochrome, stroke overlay,
round scope), plus mechanical readouts: flaps, drums, needles and legend lamps.

### The Wall: 96 colour broadcast tubes
- **Tubes:** colour shadow-mask tubes about 1.2 m across, each showing a 4:3 image on curved, round-cornered glass.
  Each tube shows one tile of the broadcast picture, so the Father's face is a mosaic of 96 slightly bulging tiles.
- **Age:** colour temperature varies ±8 % per tube (some bluer, some greener) and brightness ±10 %. One corner tube
  (upper right, outside the face) is dead black. One tube near the lower edge has a hum bar that rolls up every ~7 s.
- **Burn-in:** 41 years of the same face have burned a faint ghost of it into every tube. It shows whenever the
  tubes show something else: the Lamp at standby (shot 43), or dim at power-down.
- **Comp (replaces v1's `bezels(12×8, 6 px)`):** find the 96 glowing glass quads in the plate and give each its own
  homography and tile, so perspective and niche occlusion come from the plate. Per tile: barrel distortion
  (k1 0.04), a rounded mask (corner radius 8 % of tile width), vignette 25 %, static colour and brightness jitter as
  above plus ±2 % slow noise, and bloom. Scanlines only where a tile is larger than ~250 px on screen (shot 23).

### The Proof: the colour monitor and light pen
- **Housing:** a colour broadcast monitor with a 60 cm 4:3 tube in a Ministry grey case. A deep hood shades the glass,
  an engraved plate reads PROOF, and a row of bakelite knobs sits below.
- **Picture:** the Father's frame (raster, colour) with a **stroke overlay** drawn over it by the same tube: the
  calibration mesh, the red drift flag and its label in Stroke Hand (§5).
- **Stroke overlay behaviour:** strokes draw on in sequence, the beam's path visible as it writes. Every vertex is a
  bright bead where the beam dwells, and sharp corners get a small overshoot hook. Long strokes are dimmer than short
  ones, and many strokes make the overlay flicker faintly. The red strokes sit 1 px off the cold ones
  (misconvergence).
- **Light pen:** a pen on a coiled cable with a ring button. The image sits about 1 cm behind the glass, so the pen tip
  never quite touches it: in a macro shot, the tip, its shadow and the image beneath are three separate layers, with
  the shadow-mask dots visible under the tip. **Ida touches his face through glass.** That gesture replaces the v1
  mouse cursor.

### The Script Terminal: two-colour tube, keyboard, meter
- **Tube:** a 30 cm monochrome tube with deep curvature and a hood. It is a **two-layer (beam-penetration) tube**
  that glows **cold** blue-white at high beam voltage and **warm** amber at low. The character generator shows 48
  columns × 12 rows of Operator Mono (§5).
- **The Operator Rule:** *every character on the tube is coloured by who answers for it.* The Engine's output, the
  Ministry's template and every prediction are **cold**. Anything that entered through the operator's keyboard is
  **warm**, even when the Engine repeats it later. This is the order's "THE OPERATOR ANSWERS FOR CONTENT" built into
  the glass. It explains the palette of shots 21, 24 and 26 without any UI colour-coding:
  - Ida's typing is amber. The Engine's ghost predictions are shown at **half intensity** in their own layer.
  - "am well." is a cold ghost, learned from the Father.
  - "something warm before you sleep." is an **amber ghost**: the Engine is offering a phrase it learned only from
    her keystrokes, so it arrives in her colour. **It is the first warm thing the machine has ever produced.**
  - Stage directions such as `[EYES CLOSE]` show in inverse video (dark letters on an amber block), the terminal's
    way of marking a command.
- **Keyboard:** sculpted grey keys with cream engraved legends. The **commit key** at the right is a large square key
  of translucent red cast resin, lit from inside, with the Lamp engraved on its face.
- **The prediction meter:** a moving-coil meter set into the terminal's right cheek, with an arc scale 0–1.0
  engraved PREDICTION, a black needle and a cold backlight behind frosted glass. The needle rises in 0.3 s with a
  small overshoot. When the Engine has no prediction, it drops to the stop pin in 0.15 s with an audible tick.
- **Legend lamps** on the housing: **NO PREDICTION** (red, under the meter), **VIEWING** (a red jewel lamp at the
  top right, repeating the gallery's pilot lamp) and **SCRIPT LOCKED** (cold).

### The Corrections panel, flap repeater and Log Printer
- **Corrections panel:** a column of six rectangular **legend lamps**, each engraved with a correction: L EAR ·
  DRIFT, MOLE · L CHEEK, BLINK INTERVAL, SKIN TONE, BREATH CYCLE, VOICE WARMTH. OPEN glows red. When a correction
  locks, a relay clacks and the lamp switches to cold white. The plates are Year One plates re-engraved: look closely
  and each new legend sits over an old, paint-filled one (VOICE WARMTH over AUDIO GAIN).
- **Flap repeater:** a small four-digit split-flap unit on top of the panel that repeats the Air Clock's TO AIR
  countdown.
- **Log Printer:** an upper-case-only teleprinter on a stand at the far right. A blue-black ribbon prints every word
  the Father says onto fanfold paper for the Committee's record, and the paper folds into a wire basket below.

### The Archive Reader and the vitals scope
- **Light table:** set into the desk's left wing. A motorised transport pulls the **index strip** across a frosted
  window lit by a **tungsten lamp**, which makes it warm light: the live years are the one warm image of the Father.
  The strip is 35 mm black-and-white film, one frame per month since Year One, with paper tabs flagging each year.
  After the frame of 10 MAR comes a clear tape splice, and then the generated nights on a different stock, recorded
  from a tube. Those frames are cold blue, with scanlines inside each frame.
- **Counters:** two mechanical drum counters (white numerals on black drums) engraved CAPTURED and GENERATED.
- **Vitals scope:** a round 12 cm oscilloscope tube with a cold green-cyan long-afterglow phosphor, engraved VITALS ·
  SUBJECT F. Its trace has been flat since March. A red legend lamp reads NO SIGNAL, and a paper tag tied to its knob
  with string carries a doctor's handwriting: **11 MAR · 04:12**. The death was recorded by hand, and the state
  covered it with a machine.

### The Air Clock and the ON AIR lamp
- **Air Clock:** a slave clock with a 3 m cream enamel face and black baton hands, high on the apse wall above the
  ON AIR lamp. The second hand **steps** each second (the film's 60 BPM tick) and the minute hand jumps once a minute
  with a clunk. The clock is driven by the broadcast master's pulse, which is why it **stops when the broadcast dies**
  (shot 34). Nana's clock is wound by hand, and it keeps going.
- **TO AIR board:** a split-flap board under the clock face, cream numerals on black flaps. The minutes drum's **00
  flap is printed in red**, so the last minute arrives in the Committee's colour on the tick (shot 22).
- **ON AIR lamp:** a 2 m riveted steel box with a front of cast red glass. The words ON AIR are **cast into the
  glass** in State Capitals: when unlit they read in relief, and when lit they glow hotter than the glass around them.
  It is lit by a tungsten filament, so it switches off with a 0.3 s orange afterglow (shot 35).

### The Engine, the pneumatic post and the telephones
- **The Engine** is never seen in the pilot. It fills the vault under the Hall: Year One tape-machine cabinets,
  gutted and refilled. We know it only by its breath (the floor grilles), its 55 Hz hum and the air moving the dust.
- **Pneumatic post:** 8 cm tubes in tarnished brass with junction boxes and cream-dialled pressure gauges. The desk
  cradle is a cast-brass cup on a spring stop with a felt pad, and its lip is polished bright by use. **The
  capsule** is a black-lacquered steel cylinder a forearm long, with knurled brass end caps and a band of red lacquer
  stamped with the Sealed Lamp. The band must break to open it.
- **The Red Line:** a heavy telephone cast in red phenolic, with **no dial**, because it can't call out. Where the dial
  would be, a round plate carries the Sealed Lamp in relief. It has a braided cloth cord and a deep, harsh double bell.
- **The House Line:** the Ministry-grey version of the state's one civilian telephone (Nana's is the cream version of
  the same set). It has a rotary dial, a small **amber call lamp** (a jewel lens) beside the dial that flashes while
  it rings, and a paper card under celluloid on its base where Ida has pencilled **NANA**. Its bell is Nana's bell,
  softer and higher than the Red Line's. It replaces the v1 smartphone (**→ shots 17, 19, 37, 38, 40, 42**): Ida now
  holds a handset whose coiled cord crosses the frame back to the desk.

### The Committee's paper
- **The order (shot 11)** arrives as a **carbon copy on onionskin**. The Committee keeps the original. The slip is
  narrow (10 × 30 cm) and still curled from the capsule. It is a pre-printed form with its rules, header and form
  number in red ink, typed in the Committee Typewriter (§5) in soft, slightly smudged blue-black carbon. Cold light
  shows through the thin paper.
- **The Sealed Lamp stamp:** a red rubber stamp of the Lamp inside a double ring of small dots, one dot per member.
  The number is never explained. Stamped slightly rotated, with uneven ink. It replaces the v1 wax seal, which read as
  a fantasy scroll. **→ shot 11**

### Display artefacts (the vocabulary for JS and comp)
Every screen image passes through its device. These artefacts are what make it a device rather than a page.

| Artefact | Where | JS/comp parameter |
|---|---|---|
| Scanlines | all raster tubes | dark line every 2 raster lines at 25–40 %, visible only when a tube is large in frame |
| Persistence | all tubes | cold layer decays in ~60 ms (short trails), warm layer ~400 ms (her words linger), scope ~1.5 s |
| Bloom + halation | all tubes | glow radius ∝ brightness, plus a faint halo ring at ~3× glyph height (light scattering in the glass) |
| Curvature + mask | all tubes | barrel k1 0.03–0.06, rounded corners, 20–30 % vignette |
| Raster breathing | old tubes | picture grows ≤0.5 % when brightness rises (poor regulation); strongest in shot 12's flood |
| Hum bar | the Wall, the State Receivers | a soft dark band (−8 %) rolling up in 5–9 s |
| Interlace twitter | broadcast images | 1-line vertical shimmer on thin horizontals |
| Misconvergence | colour tubes only | red and blue offset by 1 px, growing toward the corners |
| Burn-in | the Wall, State Receivers, terminal header | a static ghost at 3–6 %, visible over darker content |
| Glass reflection | every tube in a room | the room and the operator's face reflected over dark areas at 6–12 % |
| Dust and smears | every faceplate | static grime layer, plus a light-pen smear on the Proof |
| Vector beads and hooks | stroke overlay | vertex dots at 1.6× stroke brightness; 2–3 px overshoot at sharp corners |
| Split-flap flip | Air Clock, repeater | the top half falls in 3 frames and the bottom lands with a 1-frame bounce, on the tick |
| Drum roll | counters | numerals roll vertically; a carry rolls the next drum |
| Needle ballistics | prediction meter | 0.3 s rise, 8 % overshoot, settle; a drop to the pin in 0.15 s |
| Legend-lamp switch | panels | a 2-frame dip, then the new colour; relay clack in sound |
| Collapse to a point | any tube switched off | the picture shrinks to a bright dot in 4 frames, then fades over 1 s |

---

## 5. Letters and the Lamp: the state's typography and emblem

The v1 kit is retired: DIN is a real state's road-sign alphabet, and Avenir, Futura, Menlo, Courier New and
Baskerville are instantly recognisable digital typefaces. Every in-world letter is now drawn by the production from
the rules below. The system is simple enough to define in JS as bitmaps, stroke lists or grid paths.

### The state's alphabets
1. **State Capitals: the alphabet of Year One.** Capitals only. Each letter is built on a module grid 4 wide × 6
   high (M and W are 5 wide), with a monoline stroke 1 module thick. Curves are quarter circles with an outer radius
   of 1.5 modules, so O is a rounded rectangle, never a circle. Diagonals run only corner to corner on the grid, and
   the crossbars of E, F and H sit on the midline. Letter spacing is 1 module and a word space is 3. The effect is
   condensed, square-shouldered and sturdy, like letters cut from sheet steel. It comes in four finishes:
   - **Cast:** bronze relief with bevelled edges (building facades, the ON AIR glass).
   - **Engraved:** cream-filled (every plate and legend lamp).
   - **Stencil:** 1/3-module bridges in A B D O P Q R 0 4 6 8 9 (painted on concrete, desk covers, capsules and
     tower ends).
   - **Phosphor:** the same skeleton written by the stroke overlay.
2. **Operator Mono: the terminal's character set.** A 7 × 9 dot matrix with 2 descender rows in a 9 × 14 cell. Mixed
   case: the operator's terminal is the only lowercase in the state's hardware. Each dot is drawn as a short
   horizontal dash (the beam's spot smeared along the scan) with a dark gap between scan rows. It has a slashed zero,
   a straight apostrophe, and a solid block cursor that blinks on the film's tick.
3. **Stroke Hand: the stroke overlay's lettering.** Single-stroke capitals of 3–9 straight strokes, with curves
   faceted into 4–6 segments and bright beads at stroke ends. A word draws on stroke by stroke over 4–6 frames.
4. **Caption Mosaic: the broadcast caption generator.** Letters built on a 5 × 7 grid of soft-cornered blocks, keyed
   white with a 1-block black edge (the keyer's outline). It appears only inside the broadcast signal: the LIVE bug,
   the window-burn timecode and the closed captions.
5. **Committee Typewriter: the one machine the Committee types on.** A 10-pitch slab-serif in capitals only, its
   bracketed serifs thickened by ink. Its faults are fixed and recur on every document: the E strikes high, the T's
   left arm is faint, the O is clogged solid, and the full stop punches through the onionskin. In carbon, the edges
   are soft and density runs 70–100 %. Build it from a monospaced slab face in JS, then degrade each glyph with fixed
   (not per-frame) faults.
6. **Flap numerals:** condensed square numerals with rounded corners, cream on black, split by the hinge line. The 00
   flap is red.

### The hands
The only letters not built on a grid are human, and each one is drawn as SVG strokes with pressure, not set in a
font.
- **Ida's pencil:** small, careful capitals leaning slightly forward (NANA on the House Line card).
- **The archivist's grease pencil:** blunt and waxy, written on film leader (10 MAR on the index strip).
- **The doctor's ink:** hurried cursive on the vitals tag (11 MAR · 04:12).

### The film's own letters (non-diegetic)
- **Episode title (shot 09):** CONTINUITY in State Capitals, the Ministry's word in the Ministry's letters (§9).
- **Epigraph and series title (shot 45):** the film's own voice, in a classical old-style roman and italic. Base it
  on an installed old-style text face (Iowan Old Style or Hoefler Text), treated as metal type printed by
  letterpress: ink squash, a slight bite into the card and uneven inking (§9).
- **Subtitles:** a quiet text face that isn't a UI font (Charter, cream at 85 %) in the lower letterbox bar. In
  broadcast shots they become closed captions in Caption Mosaic, white on black cells, carried inside the signal and
  scanlined with it.

### The Lamp
- **Construction:** the emblem is drawn with a compass and rule, keeping v1's proportions (ring r 150, flame 70 ×
  130, base 180 wide). The flame is a pointed arch of two equal arcs, each centred on the opposite end of its base.
  Every schoolchild can draw it with a compass, and every schoolchild did.
- **No colour of its own:** it takes the colour of its material (bronze, brass, red ink, phosphor, silver). That keeps
  the palette semantics clean.

| Variant | Form | Where |
|---|---|---|
| **The Lamp** | ring, flame and base | cast bronze on the Ministry facade, brass inlay in the Hall floor, embossed on the State Receiver's speaker grille, engraved on the commit key |
| **The Sealed Lamp** | the Lamp in a double ring of dots | the Committee: rubber stamps, capsule bands, the Red Line's dial plate |
| **The Mosaic Lamp** | an 8 × 8 block version | the broadcast corner bug: the machine's crude copy of the sacred sign |
| **The standby card** | a white Lamp hand-painted on blue card, filmed in Year One | every State Receiver between broadcasts (§7) |
| **The pin** | a small silver roundel | the Father's collar |
| **The Lighting** | a real lamp: a steel ring, a flame, a bar | the ident film (§7) |

---

## 6. Nana's flat

A one-room flat on the 14th floor of a Type-1 tower (§8): the living room, a kitchen corner and a bed alcove behind a
curtain. Every flat in the city has the same plan and fittings. What makes this one Nana's is 41 years of her hands.

- **The ceiling is low** (2.5 m) and appears in the wide shots. After the Hall's vault, lost in darkness, the frame
  gets a lid: the room is small and safe.
- **The State Receiver (invented signature):** each flat was built around a **niche for the television** in the
  plywood wall unit, so the set sits in the architecture like an icon in a shrine. The cabinet is Ministry-grey
  enamel, the state's hardware inside her home. Its only knob is an ON switch with a volume ring, with no channel
  numbers, and the Lamp is embossed on the speaker grille. Nana has put a crocheted doily and a small plant in a tin
  on top. When the set is off (shot 39), the dark glass holds the Lamp's burned-in ghost.
- **The lamp:** a turned-wood base with a pleated parchment shade, scorched brown on the side nearest the bulb. The
  shade throws a crisp arc of light on the wall behind her.
- **The telephone:** the civilian set in cream bakelite on a crocheted mat. The handset cord is wound with tape where
  it frayed.
- **The clock:** a wooden wall clock with a pendulum and a plain face with baton marks. Its winding key hangs on a
  nail beside it. It is **wound by hand, not slaved to the state**, so it keeps ticking after the Hall's clock stops.
- **The armchair:** low, with wooden arms worn pale where her hands rest. It was reupholstered once, and one arm cover
  doesn't match. A crocheted cover lies over the back.
- **The table:** two cups. Hers is a thick, chipped mug. Ida's is the one good cup, fine porcelain, poured and
  untouched.
- **The stove:** a two-ring enamel stove with the soup in an **amber enamel pot**. The pot matches Ida's thermos: they
  are a set, a visual rhyme between the Hall and home.
- **The window:** steel-framed and painted many times, double-paned with a gap between the panes. Rain runs on the
  outer pane only.
- **The wall:** faded wallpaper of small leaves, with **a pale, unfaded rectangle** where a framed portrait hung for
  decades. Nana has taken it down, and we never see when. It's a plant for the reveal (director's call; cut it if it
  reads too early).
- **Light:** only the lamp (tungsten, low, left of her chair), the television (cold, low, right) and the window's weak
  blue city glow. The ceiling fixture is off, its enamel shade in shadow. Nothing else.

---

## 7. The broadcast: the Father, the Lighting, the bug and the standby card

### The frame
**The Evening Address is a 4:3 picture**, the television's shape, pillarboxed in pure black inside the 1920 × 1080
master (1440 × 1080, centred). World shots stay 2.39:1. The oldest, squarest frame is set against the widest, which
sharpens `episode.md`'s rule that the frame shape says whose image it is. **→ shots 01–04, 28, 29, 31, 34, 46.**
Generate keyframes and Seedance clips at 16:9 and crop the centre. The Father is dead-centre, so the crop is safe.

### The Copy Rule
**The Father is the only frictionless image in the film.** He gets soft, even, shadowless studio light, perfect
bilateral symmetry and smooth tonal gradients (the only gradients in a direction that otherwise has none). His skin
has no texture, and his stillness is a little too perfect. The polished, even-lit default of an image model, the very
thing the note objected to, now belongs to him alone. It is how the Apparatus sees a man. Everything alive is
textured, imperfect and made by hand. When the film cuts from the world to his face, the audience should feel the
change of material before they understand it (`art_direction.md`, series rules).

### The studio he imitates
The generated picture copies the real studio of Year One: a deep blue cyclorama, with a **large round diffuser lamp**
behind his head. The v1 "halo" is a physical studio light, its disc edge faintly visible, not a holy glow.
- **The coat:** charcoal wool with a soft rolled collar, a concealed placket, and no pockets, buttons, medals or
  insignia. The only ornament is the silver Lamp pin. It must not read as any real uniform or statesman's suit.
- **Signal:** the picture arrives through the broadcast chain, with interlace twitter, a soft video bloom and one faint
  hum bar during the Address. The 1-frame stutter at 4.2 s (shot 02) stays.

### The Lighting (the ident)
The national ident is **a 5-second black-and-white film loop shot in Year One** and run through the telecine every
night for 41 years. It shows a real lamp being lit: a steel ring on a stand, a slim burner inside it and a bar beneath.
All three are lit by one spotlight in a black studio. A taper enters from the right and the wick catches. The flame
rises, and the taper withdraws.
- **The title** is part of the old film: THE EVENING ADDRESS · 21:00, hand-painted in State Capitals on a black
  caption card and superimposed optically.
- **Wear:** 14,763 plays have scratched the print: vertical scratch lines, dust, gate weave and a splice bump. It is
  monochrome film, tinted cold by the broadcast chain.
- **Sound:** the chime comes off the film's optical soundtrack, with a trace of wow and flutter.
- **Why:** the one sacred image of the state is a worn film of a flame being lit by a hand we never see. It's the only
  live thing left in the broadcast, and it's 41 years old. It replaces the v1 app-splash emblem (§9, shots 01, 28, 46).

### The bug and the standby card
- **The bug (J14):** the Mosaic Lamp (8 × 8 blocks) top left, and LIVE in Caption Mosaic bottom right, keyed white
  with black block edges at 70 %. It's the state's one printed lie, in its crudest letters.
- **The standby card (J15):** a card hand-painted in Year One, a white Lamp brushed onto blue gouache with the brush
  marks visible, filmed with a slight vignette. It **breathes** ±3 % at 0.25 Hz, the carrier's heartbeat, so the
  nation knows the channel is alive. On the State Receivers it gains curvature, scanlines and burn-in, and on the Wall
  (shot 43) it shows over the Father's burned-in ghost.

---

## 8. The city

- **Towers:** Type-1 slab towers of 16 floors, one design repeated to the horizon. The concrete is board-formed with
  horizontal bands, and the windows sit in strict grids. **Invented signature:** each slab ends in a **rounded stair
  tower glazed with a vertical slot of glass blocks** that glows cold at night. Tower ends carry huge stencilled
  numbers in State Stencil.
- **Antennas:** one antenna mast per roof, and **every antenna in the city is turned toward the Transmitter**, like a
  field turned to the sun.
- **The Transmitter:** a lattice mast on the horizon with a single red beacon that blinks every 2 s: the Committee's
  eye over the city. It's in every city wide, and it is still blinking at dawn.
- **Windows:** each window is a room lit by a television, brighter at the sill where the set is, with the ceiling lit
  above, a curtain pattern and a plant's silhouette. A few show the tiny glowing rounded rectangle of the set itself.
  For the window wave (shot 44) they must stay **separable blobs**, each bounded by dark mullions. Build the masks
  from luminance blobs on the facade grid, not a hue threshold. **→ shots 15, 44**
- **What residents have done:** glazed-in balconies with mismatched frames, laundry lines, window boxes, a pane painted
  over. The repairs of §1, at city scale.
- **The canal:** vertical concrete embankments with iron railings and mooring rings. The black water breaks the
  windows' reflections into columns.
- **Street light:** mercury-vapour lamps on concrete posts, cold blue-green. No sodium (§2).
- **Trams:** single cars with a rounded nose and one round headlamp, and a ribbed body in dull cream and grey, with a
  trolley pole on the overhead wires. The interiors are lit cold.
- **The Public Receiver (shot 30):** a large rear-projection screen set into the district's civic building like an
  altarpiece, in a concrete frame with a pediment and a bronze Lamp above it. Its image is soft, with a hot spot at the
  centre, dark corners and scanlines visible at that scale. Rain streaks through the projection beam in front of it,
  and its light falls cold on the wet street. It replaces v1's flat billboard rectangle.
- **Dawn (shot 44):** the rain has stopped. Low cloud is lit rose from below the horizon, and the Transmitter's beacon
  still blinks red over the warming windows: the old is still standing.

---

## 9. Every JS screen shot, redesigned as hardware

The screen text of `script.md` stays word for word unless a change is marked. For each shot: the device, what's on
it, how it's shot and why, and the build route. The route follows one pattern throughout: **Codex paints the
hardware with a blank, evenly glowing face; JS renders what the device shows; comp puts it into the device.** The
insert gets a homography, the §4 artefacts, the glass reflection and the grade. The v1 "safe band" rule still holds.

### 01 · THE LIGHTING (ident): a film, not a splash screen
- **Device:** the Year One ident film run through the telecine (§7), shown full frame at 4:3.
- **Timeline (same chime):** 0.5 s A4, the spotlight finds the steel ring and it glints. 1.0 s F♯4, the taper touches
  and the wick catches. 1.5 s D4, the flame stands. 2.2–3.0 s, the caption card superimposes THE EVENING ADDRESS ·
  21:00 in hand-painted State Capitals, 0.5° off level, with brush texture. Hold to 5.0.
- **Artefacts:** heavy film grain; 2–3 vertical scratches that stay put (they're on the print); per-frame dust; gate
  weave ±1.5 px; ±4 % flicker; a splice bump at 0.2 s (a 2-frame jump and a flash of frame line). Then the broadcast
  chain adds interlace twitter, bloom and the cold tint. No bug: the ident is the channel.
- **Shot as:** full-frame broadcast. It's the film's first image, and we're inside the nation's television.
- **Build:** a Codex plate of the lamp with the wick unlit. The flame comes from a 5 s silent Seedance take or a
  procedural flame in comp. The card is JS (State Capitals on a painted-card texture). Film wear and the telecine are a
  JS/comp overlay.

### 04 · FREEZE: the picture becomes an object
- **Device:** the Proof (§4), showing k02 frozen.
- **0.00–0.12 s:** a horizontal-sync tear: the lines skew sideways for 3 frames, then the picture freezes.
- **0.15–2.0 s:** the image takes on the Proof's curvature and rounded corners. A faint reflection fades up on the glass
  (the Wall's glowing grid, the dark shape of Ida's head). The pillarbox opens as the letterbox closes, and the camera
  pulls back (easeOutCubic) until the tube face fills about 80 % of the band height, with the hood's edges at left and
  right. **Reveal 1 becomes physical: he's a picture on a tube, in a room.**
- **0.20–0.80 s:** the stroke overlay draws the mesh, beads first (the beam dwelling on each landmark), then the
  strokes joining them.
- **0.80 s:** the ghost ear (the ear region doubled at +6 px, 40 %) and the red drift flag: a stroke box with a corner
  tick, labelled L EAR · DRIFT +3.2 PX in red Stroke Hand, 1 px misconverged.
- **1.0–1.6 s:** a window-burn timecode in Caption Mosaic along the picture's lower edge, REPLAY 211 · 20:51:07:14, with
  the frames counting 14 → 23. It stops at 1.6 on the click of the light pen's ring button. NIGHT DESK 4 moves to the
  hood's engraved plate: PROOF · DESK 4.
- **Build:** a new Codex plate of the Proof, frontal, with a blank glowing face. JS renders the stroke overlay (J16 as
  a stroke renderer, J02 in Stroke Hand) and the window burn. Comp does the tube transform, the homography into the
  plate, the reflection layer and the grade.

### 06 · HOLD STILL: a pen on glass
- **Devices:** the Proof on the left two-thirds, the Corrections panel on the right third, and the flap repeater in
  the top right corner. Ida's hand holds the light pen and enters from the lower left.
- **Framing:** a three-quarter top-down insert over her shoulder. The Proof's face is angled 20° off the lens axis,
  so the curved glass and the hood read as an object. The Corrections column stays soft until its lamps switch.
- **Action:**
  - 0.3–1.0 s: the pen's shadow reaches the ghost ear before the pen does.
  - 1.0 s: the ring button clicks, and the overlay draws a small circle around the tip.
  - 1.1–2.2 s: the tip drags a few millimetres and the ghost slides home. "Hold still."
  - 2.3 s: the flag redraws in cold strokes as L EAR · LOCKED.
  - 2.3–5.4 s: the legend lamps switch from red to cold one by one, a relay clack each (2.3, 3.0, 3.6, 4.2, 4.8, 5.4).
  - Throughout, the repeater's flaps clack each second, 08:38 → 08:31.
- **Removed:** the v1 top bar, SUBJECT F header, timeline and waveform strip. The voice is heard, not graphed.
- **Shot as:** a physical insert with her hand in frame. "Hold still" is said to a face she is touching.
- **Build:**
  - Codex plate: the console with the blank Proof face, unlit lamps, and her hand holding the pen near the glass.
  - JS: the Proof's content (k02 frozen, the mesh, the labels) and the flap digits.
  - Comp: lamp switches on masks cut from the plate.
  - The pen: a ≤ 8 px translate of a hand-and-pen cutout, or a 4 s silent Seedance take ("she moves the pen a few
    millimetres left and lifts it"). Test both.

### 08 · ARCHIVE: 41 years on a light table
- **Devices:** the Archive Reader, its two drum counters and the vitals scope (§4).
- **Framing:** straight overhead. The light table's frosted window crosses the 2.39 band as a horizontal bar of warm
  light, and the strip runs across it right to left. The CAPTURED and GENERATED counters sit at the lower left and
  lower centre, and the round scope at the lower right, its tag in shadow.
- **0.0–4.6 s, captured:** warm black-and-white frames with sprocket holes and frame lines race past, the year tabs
  (grease pencil, 1–41) flicking by, blurred along the strip at cruise speed. CAPTURED rolls to 14,763. The frames are
  k01/k02 crops in black and white with film grain. (Optionally, three Codex frames of the Father at 45, 60 and 75
  for the early decades. Nobody can see them at speed, but the slowdown can.)
- **4.6 s:** the strip stops dead on the last live frame, flagged in grease pencil: LAST LIVE CAPTURE · 10 MAR.
- **4.9 s:** the scope's NO SIGNAL lamp lights red over a flat, long-afterglow trace, and its light finds the paper
  tag: 11 MAR · 04:12.
- **5.2–8.2 s, generated:** the strip moves on over the tape splice into the cold stock, blue frames with scanlines
  inside them, accelerating to a streak. GENERATED rolls 001 → 212, the drums blurring and then settling.
- **8.2 s:** it stops on a **clear, unexposed frame**, pure warm light from the lamp beneath, boxed in grease pencil:
  212 · TONIGHT.
- **The colour argument:** warm film (a living man, lit by a filament), then the cold stock (the copy), then an empty
  frame of warm light (tonight is unwritten, and a hand will write it). It reads without a single label.
- **Shot as:** an overhead insert. An archive is a table of evidence. Top-down turns 41 years into a line of frames,
  and it puts the death on a paper tag in someone's handwriting.
- **Build:** a Codex plate (overhead of the light table, with the window lit and empty, blank counters and a dark
  scope with its tag). JS renders the strip, the counters and the trace, inserted by homography with a multiply blend
  over the frosted glass.

### 09 · CONTINUITY (title): a word that burns in
- **Device (non-diegetic):** a black tube face with no edges visible.
- **Action:** CONTINUITY in State Capitals, written by a stroke beam at 4–6 frames a letter (0.3–1.2 s). Each letter
  blazes, then decays over 1.5 s to a dim afterglow that stays to the cut as a burned-in ghost. The v1 cyan rule is
  dropped.
- **Why:** the word lingers after it's gone, which is the pilot's subject in one decay.
- **Build:** JS only (stroke renderer, persistence, bloom, halation ring).

### 12 · THE LOOP: the screen overflows into the room
- **Devices:** the Script Terminal (cold, Engine-written) and the Log Printer.
- **Framing:** two planes, from Ida's right at desk height. The tube fills the left two-thirds, with the prediction
  meter visible on its cheek. The printer's platen is in the soft right foreground, and its paper climbs toward the
  lens.
- **0.3–6.0 s:** the Engine writes in cold Operator Mono at the speaking rate, then only "I am well.", accelerating. The
  scroll jumps line by line and then smears into bright persistence bands. The raster breathes outward, a hum bar
  rolls, and the needle is pinned at 0.99, trembling. A red legend lamp, FREE, blinks at 1 Hz.
- **6.0–7.4 s:** focus pulls to the paper. The printer hammers I AM WELL. I AM WELL. in upper case at the choir's
  rate, and the paper folds over the desk edge and keeps coming.
- **7.4 s:** the red HALT lamp lights. The printer stops mid-word (I AM WE) and the tube drops to 30 % standby. **The
  needle stays pinned:** the machine is still certain.
- **Shot as:** two planes and a focus pull. The loop has to escape the screen into the room, and paper makes the
  repetition physical and loud.
- **Build:** a Codex plate with the terminal and printer in one frame (blank tube, blank paper). JS renders the
  terminal text and the paper strip (typed lines on a paper texture, advancing, folded by a simple mesh warp). The
  focus pull is layer blur. Or use a silent Seedance take of the paper, with the text added in comp.

### 14 and 22 · FOUR MINUTES / ONE MINUTE: the Air Clock
- **Device:** the Air Clock and its TO AIR flap board, high on the apse wall (§4).
- **Framing:** a long-lens view from Desk 4 up the axis. The clock face fills the left of the band, the flap board
  the right, and haze and a few dust motes hang between us and them. It's the same framing both times: repetition is
  the ritual, and the change is the story.
- **14:** at 0.0 s the second hand steps, and the flaps read TO AIR 04:00. At 1.0 s the hand steps again and the seconds
  flaps clack to 03:59. The hour and minute hands stand at 20:56.
- **22:** the same, at 20:59 and TO AIR 01:00. At 1.0 s **the minutes flap falls to its red-printed 00**: 00:59. A
  slow push 1.00 → 1.06 (easeInQuad) begins the pulse.
- **Shot as:** a real object in the room, seen far off through air. The countdown belongs to the building, not to a
  screen.
- **Build:** one Codex plate (the clock and a blank flap board, low angle through haze). JS renders the flap faces with
  the flip animation, and comp adds the second-hand step (a rotated cutout) and the grade.

### 21 · SIGN-OFFS: her letters in her colour
- **Device:** the Script Terminal (§4).
- **Rename:** the header reads SIGN-OFFS · DESK 4, typed by her, so amber. This world has no file extensions:
  `signoffs.txt` goes. **→ shot 21, script.md**
- **Content:** the columns stay as written. NIGHT numbers are cold at half intensity. The Engine's "Sleep safely."
  lines are cold, and Nana's lines are **warm, because Ida typed them** (the Operator Rule). From NIGHT 150 the block
  is solid amber.
- **Motion:** the scroll starts fast, and the text smears into streaks. Cold streaks vanish at once while **amber
  streaks linger** (long persistence), so the warm lines stay in the eye even at speed. As it slows, the scroll
  becomes visible line-jumps with a 1-px bounce. At rest: NIGHT 199–212 and the block cursor after NIGHT 212, blinking
  on the tick.
- **Framing:** a partial framing of the lower two-thirds of the glass and the top row of the keyboard, where her
  fingertips rest. **The amber block lights her fingers:** the first warm light on Ida's skin in the Hall comes from
  her own words.
- **Build:** a Codex plate (the terminal glass low in frame, blank, with her fingers on the keys). JS renders the
  terminal, and comp adds the insert and an amber light spill on the finger mask, driven by the insert's amber luma.

### 24 · "I …": the author and the words in one image
- **Device:** the Script Terminal, its prediction meter and its legend lamps (§4).
- **Framing:** tight and slightly off-axis (15° from her side, a little above). The text fills most of the band, the
  curved glass edge and hood show at frame left, and the meter and lamps sit on the housing at frame right. **Her
  reflection** (face lit by the screen, 8–10 %) lies in the dark glass behind the letters. The one image holds the
  author and her words.
- **Content:**
  - Line 1, the Ministry's template: Good evening, my children. Cold, dim, locked; a padlock glyph in Operator Mono.
  - Her typing is amber.
  - 0.9 s: the ghost "am well." appears, cold at half intensity, and the needle rises to 0.99.
  - 3.0–3.2 s: at "d" the ghost stutters (am we—) and dies. **The needle drops to the pin with a tick**, and NO
    PREDICTION lights red.
  - 5.8 s: the VIEWING jewel lamp at the top right lights red and begins to blink. The phone follows at 6.0 s.
  - The TO AIR repeater clacks down from 00:53.
- **Why:** a needle falling to zero reads from across a room. The machine's heart stops at the word "died".
- **Build:** a Codex plate (the terminal at this angle, blank glass, unlit lamps, the meter at rest). JS renders the
  terminal text. Comp adds the needle (a rotated cutout), the lamps, the reflection (a darkened, blurred, mirrored
  crop of her keyframe) and the grade.

### 26 · "EAT …": the machine's first warm word
- **Device and framing:** identical to 24, one continuous page.
- **Content:** lines 2–4 stand in amber. She types "Eat" in amber.
  - 1.7 s: the ghost arrives, **amber at half intensity**, the first warm ghost the machine has ever produced. The
    needle climbs to 0.97.
  - 4.0 s: TAB. The ghost fills to full-intensity amber, left to right, over 0.3 s.
  - 4.8–6.2 s: [EYES CLOSE] types in inverse video, dark letters on an amber block.
  - 6.6 s: SCRIPT LOCKED lights cold, and the cursor goes out.
  - VIEWING blinks throughout.
- **Build:** as 24.

### 28 · THE LIGHTING (fast): the operator starts the loop late
- **Device:** the same film. It runs in at 0.3 s from a later cue point, straight to the taper touching, with a 1-frame
  splice flash at the join. That makes "faster" motivated. It uses the cold chime timings from `shot.md` and a
  deeper cold tint. No bug.

### 37 · NANA CALLING: a lamp and a pencilled name
- **Device:** the House Line (§4).
- **Framing:** a macro insert across the desk at the phone's height. In focus: the grey phone, its **amber call lamp
  flashing with each ring**, and the celluloid card where Ida's pencil has written NANA. Soft behind it, the red
  phone's handset jitters in its cradle. Two phones, two lights.
- **Removed:** the v1 smartphone, its app-style name screen, the Avenir "calling…" and the accept/decline circles.
  A smartphone can't exist in this world.
- **Why:** the personal colour arrives as a small filament lamp beside a name written by hand, which is exactly what
  Nana is to her.
- **Build:** a Codex plate (the phone with its lamp unlit and a blank card, and the red phone behind). JS renders the
  pencil strokes as an SVG path with graphite texture, multiplied onto the card, and comp adds the lamp flashes and the
  warm spill on the grey enamel.

### 45 · EPIGRAPH AND TITLE: a printed card in the first light
- **Device (non-diegetic):** a letterpress card in dark grey stock, lying flat and seen straight down.
- **Epigraph:** "The old is dying and the new cannot be born." set in an old-style italic, printed in cream ink with
  the attribution below. **A band of dawn-rose light rakes slowly across the card from the left**, revealing the words
  as it passes, like sunrise moving along a wall. It carries 44's colour into the titles.
- **Title:** the series title in old-style roman capitals, printed with visible ink squash and bite. It is lit by the
  same rose raking light, which **replaces the v1 rose rule** as the one rose element outside 44. EPISODE ONE ·
  CONTINUITY follows in small capitals. Everything fades to black.
- **Build:** JS (text as paths, letterpress simulation with ink spread, bite shading and paper fibre, plus a moving
  light mask). No Codex. Keep the timings of the current `shot.md`.

### 46 · NIGHT 213 (alt tail)
- **0.0–1.0 s:** replaces the v1 Menlo card. The GENERATED drum counter on the dark desk, lit only by the Wall's cold
  standby glow, **rolls from 212 to 213** with a mechanical click. Continuation as a sound.
- **1.0–4.0 s:** the Lighting, the whole film, in the old key and at normal warmth.
- **4.0–9.6 s:** the Father at 4:3, as in shot 02.
- **Build:** a Codex plate of the counter close-up, with the drums rendered in JS.

### Graphics inside keyframe shots
- **05, 23, 43 (the Wall):** the tile-by-tile insert of §4. In 43 it shows the standby card over the burned-in ghost
  of his face, the dead tube and the hum bar.
- **11 (the order):** the carbon slip (§4). Replace the v1 Courier New and wax seal with Committee Typewriter carbon
  on a red-ruled form, plus the Sealed Lamp stamp. The v1 multiply insert still works.
- **16, 18, 20, 33 (Nana's television):** the standby card, or the broadcast, through the State Receiver's curvature,
  scanlines and misconvergence. The set's light flickers with the insert's luma, as before.
- **30 (the Public Receiver):** k01 through the projection look of §8: a hot spot, soft focus, scanlines, rain in the
  beam and a cold spill on the street.
- **35 (ON AIR):** the letters are cast into the glass. Replace the v1 DIN mask with State Capitals relief, bright when
  lit and a darker embossing when unlit, with the 0.3 s orange filament afterglow.
- **Subtitles (J17):** Charter in the lower bar for world shots, and Caption Mosaic closed captions inside the
  broadcast (§5).

---

## 10. Change list for the shot files

| Shots | Change |
|---|---|
| All | Retire the v1 JS design system ("Ministry UI"): its fonts, dark cards, rules and panels. Every screen follows §4, §5 and §9 |
| 01–04, 28, 29, 31, 34, 46 | Broadcast frame becomes 4:3 pillarboxed (§7). Shot 04's letterbox-in becomes the tube reveal (§9) |
| 01, 28, 46 | Ident becomes the Lighting film (§7, §9) |
| 06, 08, 12, 14, 21, 22, 24, 26, 37 | JS-only shots become Codex hardware plates plus JS inserts plus comp (§9). Each needs one new plate |
| 17, 19, 37, 38, 40, 42 | Ida's smartphone becomes the House Line handset with a coiled cord (§4) |
| 11 | Carbon onionskin on a red-ruled form; Committee Typewriter; the Sealed Lamp stamp replaces the wax seal |
| 21 | `signoffs.txt` becomes SIGN-OFFS · DESK 4 (script.md too) |
| 45 | The rose rule becomes rose raking light on a letterpress card |
| 05, 23, 43 | The monitor wall becomes the columbarium of tubes, with burn-in (§3, §4) |
| 15, 44 | Windows become TV-lit rooms. Masks come from luminance blobs, not hue (§8) |
| k01, k02, k20 | Regenerate under the Copy Rule; new coat (§7) |
