# Shot 11 — THE ORDER

**Duration:** 6 s (0:57–1:03; abs 57.0–63.0)  **Tool:** Codex k06 + JS (the carbon form, the typed lines, the stamp) +
comp; an optional silent Seedance take
**Camera:** straight overhead, 50 mm, locked (paper is evidence)

**Action:** Ida's hands hold the order flat under the tube's cold light: a narrow carbon copy on onionskin, still curled
from the capsule, a Committee form ruled in red ink and typed in soft blue-black carbon. The Committee keeps the
original. We read it as she does: NIGHT 212 / NO AGREEMENT. / NO TEXT TONIGHT. / LET HIM SPEAK. / THE OPERATOR ANSWERS
FOR CONTENT. At the foot, the Sealed Lamp in red rubber stamp, a little crooked. The cold light shows through the thin
paper, and the shadows of her fingertips show through it. The rulers cannot agree on the next lie, so they hand it to
the machine and the blame to her.

**Build:**
- Codex **k06**: the slip is blank onionskin; the opened capsule lies beside it.
- JS **J06 v3** (below) renders the form, the typed lines and the stamp on transparent layers.
- Comp: find the slip's 4 corners (the largest pale region, `approxPolyDP`, or clicked once by hand), then
  `insert(J06, target=corners)` with a **multiply** blend, so the ink sits in the onionskin grain, plus 0.6 px blur.
- **The reading:** all five lines are on the paper from the first frame. Typed carbon doesn't fade in, so v1's
  line-by-line reveal is dropped; six seconds is enough to read five short lines, and the sound punctuates them.
- **v2 (optional):** a 6 s silent take in which her thumb flattens the curled end. Use it only if a 4-corner track of
  the slip holds through the take; otherwise keep the still plate.
- `letterbox(2.39)`, `grade(HALL)`. v1's push is gone.

**Keyframe prompt (`k06_order`):**
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
> Her hands (the woman on the attached sheet): slim fingers and the cuffs of a charcoal ribbed sweater.
> SHOT: straight down from directly overhead with a 50 mm lens, at a steel operator's desk in blue-grey hammered enamel,
> worn to bare metal along its edge. A young woman's two hands hold open a narrow strip of thin onionskin paper, about
> 10 by 30 centimetres, lying level across the middle of the frame and filling its middle two thirds; the paper is still
> slightly curled at both ends from being rolled, and it is completely blank, with no marks, lines or letters, only the
> faint grain of thin pale cream paper, through which the shadows of her fingertips show. Beside it lies an opened
> pneumatic capsule: a black-lacquered steel cylinder with one knurled brass end cap taken off and a broken band of red
> lacquer. Cold pale cyan light from a monitor falls from the top of the frame across the paper and her hands; the desk
> around them falls into black.

**Refs:** `assets/pilot/lookdev_v3/hall.png`, `assets/pilot/lookdev_v3/ida.png`.
**Layers:** none.

**JS spec (J06 v3 · the Committee's carbon copy; transparent layers on a 1600×480 px canvas, the slip's aspect):**
- **Object** (`production_design.md` §4): a pre-printed Committee form on onionskin. The form is printed in red ink
  `#CC3A2B`: a double rule across the top, a small box at the top right holding the form number F-12 in printed State
  Capitals (module 3 px), and faint guide rules under the typed lines. The typing is a carbon copy in blue-black
  `#1E2433`, soft-edged, density 70–100 %.
- **The Committee Typewriter:** capitals only, monospaced. Build it from Rockwell Bold (installed) with each glyph
  centred in a fixed cell; thicken and round the serifs with a 1.2 px ink spread. Scale it for the screen, not for a
  desk: cap height 38 px, advance 33 px, line pitch 64 px, left margin 90 px. Its faults are fixed, identical on every
  document it ever types: the E strikes 3 px high, the T's left arm prints at 40 %, the O is clogged solid, and each
  full stop punches through (a pale hole with a dark rim). Carbon softness: 1.5 px blur on the edges, a faint ghost of
  each letter offset 1 px down (the carbon slipped).
- **The lines** (word for word, the script's order):
  1. NIGHT 212
  2. NO AGREEMENT.
  3. NO TEXT TONIGHT.
  4. LET HIM SPEAK.
  5. (a blank line) THE OPERATOR ANSWERS FOR CONTENT.
- **The Sealed Lamp stamp:** the Lamp (ring, pointed flame, base) inside a double ring of small dots, one dot per member
  of the Committee (never explained), 150 px across, red `#CC3A2B`, at the lower right of the slip, clear of the
  typing. Stamped rotated −8° with uneven ink: density noise, one dry edge, and a 1 px double strike. Multiply. It
  replaces v1's wax seal.
- Render the form, the typing and the stamp as separate layers.

**Sound:**
- Paper crinkle 0.0–0.6 (abs 57.0–57.6).
- Hall tone, clock and DRONE.
- A dark PAD swell on D2 from +2.0 (abs 59.0).
- A soft PULSE at +3.8 (abs 60.8) as the last line appears.
- No dialogue.

*v3 sound note:* onionskin is thinner and crisper than v1's slip: the same crinkle, higher and drier. The PULSE at 3.8
now lands as the reader reaches the last line; keep its time.

**Motion prompt (v2, optional, Seedance: start `work/pilot/keys_v3/k06_order.png`, 6 s, `--no-audio`):** Colour
woodcut print animation; keep the first frame's exact carved shapes, flat inks and designs. Straight down from overhead:
a woman's two hands hold a narrow slip of thin paper flat on a steel desk under cold light, an opened black capsule
beside it. Her hands stay still for three seconds while she reads. Then her right thumb presses the curled end of the
paper flat, and her hands are still again. The paper stays flat and does not fold. Locked-off camera. No sound.

**Takes:** —
