# Shot 04 — FREEZE

**Duration:** 3 s (0:19–0:22; abs 19.0–22.0)  **Tool:** comp + JS (stroke overlay, window burn, engraved plate): the
frozen frame is pulled back into Codex plate p04 (shared with 06)  **Camera:** from the full 4:3 broadcast frame, a
mechanical pull-back out of the picture and into the room

**Action:** Mid-breath, the broadcast tears and stops, and the sound tape-stops into silence. The picture takes the
curve of glass. The pillarbox opens as the letterbox closes, and we pull back out of the television into a room: the
frozen face is on a hooded monitor at a desk, beside a column of red lamps, and a woman's hand holds a pen of light a
centimetre from the glass. A beam draws a mesh over his face, point by point. His left ear doubles into a ghost, and a
red flag marks it: L EAR · DRIFT +3.2 PX. A timecode burned into the picture counts frames and stops on a click.
**Reveal 1 is physical: he is a picture on a tube, and someone is fixing him.**

**Build:**
- **Source picture:** `work/pilot/v3/f04_frozen.png`, the last frame of shot 03 (the take's end frame in v2; k02 at
  push 1.04 in v1), without the bug.
- **Plate:** Codex **p04**, the Proof at Desk 4 with its column of legend lamps and Ida's hand holding the light pen.
  Its tube face is blank and glowing; comp fills it.
- **0.00–0.12 s:** a horizontal-sync tear: the lines skew sideways for 3 frames (up to 40 px, increasing downward), then
  the picture freezes. The J14 bug vanishes at 0.12: the signal has stopped.
- **0.15–2.0 s, the pull:** `letterbox_in(0.15, 0.30)` while the pillarbox opens. The frozen picture takes the Proof's
  barrel curvature (k1 0.05), rounded corners and 25 % vignette, and sits in p04's tube quad by homography. The camera
  pulls back (easeOutCubic) from a scale where the tube face fills the frame to p04's framing. The hood and knobs ride a
  matte cut from p04 itself (GrabCut; no Codex cutout) at 1.06× the plate's motion, so the move reads as a dolly, not
  a zoom.
- **0.60–2.0 s:** a faint reflection fades up on the glass (8 %): the Wall's glowing grid (a darkened, blurred crop of
  k03) and the dark shape of Ida's head.
- **0.20–0.80 s:** the stroke overlay draws the mesh (J16 v3). **0.80 s:** the ghost ear and the red drift flag.
- **1.0–1.6 s:** the window burn counts frames, then stops at 1.6 on the click of the light pen's ring button.
- The six legend lamps glow red (OPEN) throughout, with their legends comped as in shot 06. The flap repeater on top
  of the column reads 08:48 and clacks to 08:47 on the hall clock's first tick (2.0 s).
- `grade(HALL)` from 0.15, grain 2 %. Hold to 3.0.

**Keyframe prompt (`p04_proof`; also the plate of shot 06):**
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
> Her hand (the woman on the attached sheet): slim fingers and the cuff of a charcoal ribbed sweater.
> SHOT: a hardware insert at an operator's desk in a dark broadcast hall, seen with a 60 mm lens at the operator's eye
> line, square to the glass. Left of centre, a large colour monitor in a blue-grey hammered-enamel case: its 4:3 tube
> face is curved and round-cornered, set back under a deep hood, glowing blank, even pale cyan, and it fills about two
> thirds of the height of the central band. Below the tube, a row of five round black knobs, one worn to a thumb
> hollow; on the hood's brow, a small blank engraved plate. On the hood's right cheek, a narrow vertical column of six
> blank rectangular indicator lamps in a steel strip, all glowing dim red; on top of the column, a small unit of four
> black flip-number cards, blank. At the lower right, a young woman's right hand enters from the edge of the frame
> holding a slim pen on a coiled cable, its tip a centimetre from the glass on the right side of the tube face, not
> touching; a ring button on the pen's barrel sits under her finger. The tube's cold light is the only key: it lights
> her fingers and the pen from the front and cuts the hood's inner edges as thin pale cyan lines. The case shows one
> repair: a newer cable taped to an older one along the hood. Everything else falls into black.

**Refs:** `assets/pilot/lookdev_v3/hall.png`, `assets/pilot/lookdev_v3/ida.png`.
**Layers:** none. The hood matte for the pull is cut from p04 with GrabCut.

**JS spec (J16 v3 stroke overlay, J02 v3 drift flag, J18 window burn, J20 hood plate; rendered in picture space,
1440×1080, so they bend with the tube):**
- **Device:** the Proof's stroke overlay (`production_design.md` §4): the colour tube writes vector strokes over its own
  raster picture. Strokes draw on in sequence with the beam's path visible; every vertex is a bright bead where the
  beam dwells, and sharp corners get a small overshoot hook. Long strokes are dimmer than short ones, and many strokes
  make the overlay flicker faintly. This is Reveal 1's graphic, and it is a machine, not a UI.
- **Mesh:** about 120 landmarks hand-placed once on `f04_frozen.png` and saved as `episodes/pilot/js/mesh_f04.json`
  (v1's `mesh_k02.json` was placed on the old k02 and must be redone): brows 10, eyes 16, nose 9, mouth 20, jaw and beard
  line 17, ears 8, hairline 10, beard outline 12, cheeks 8, forehead 10. Delaunay triangulation.
  - Beads: 3 px, core `#DDFBFA` with `#5FE1E6` bloom, at 1.6× stroke brightness, lit in beam order (a
    nearest-neighbour path across the face, not random) over 0.20–0.45 s.
  - Strokes: 1.2 px `#5FE1E6` at 60 %, drawn along the beam path over 0.45–0.80 s; brightness ∝ 1/√length; 2–3 px
    overshoot hooks at corners sharper than 60°; ±3 % flicker at 30 Hz once more than 200 strokes are lit.
- **Ghost ear and flag (0.80 s):** the ear on image right, doubled at +6 px x and 40 %. Around it a red stroke box
  (`#E0412F`, 1.5 px, drawn on in 4 frames, with a tick at its top-left corner), offset +1 px x from the cold strokes
  (misconvergence). The label L EAR · DRIFT +3.2 PX in Stroke Hand (single-stroke capitals of 3–9 straight strokes,
  curves faceted into 4–6 segments, beads at the stroke ends), cap height 22 px, drawn stroke by stroke over 5 frames.
- **Window burn (1.0–1.6 s):** along the picture's lower edge, REPLAY 211 · 20:51:07:14 in Caption Mosaic (block 4 px),
  white keyed with a 1-block black edge. The frames field counts 14 → 23, then stops on the click.
- **Hood plate:** PROOF · DESK 4 engraved in State Capitals (module 5 px), cream-filled, the fill chipped from the R and
  the 4; laid onto p04's blank plate with multiply and a 1 px emboss. It replaces v1's NIGHT DESK 4 tag.
- **Tube artefacts** on the insert: scanlines (the tube is large in frame), bloom and a halation ring, 1 px
  misconvergence growing toward the corners, a static dust layer, and a light-pen smear on the glass over the ear.
- Save the overlay state at 3.0 as `work/pilot/v3/f04_mesh_state.png`; shots 05 and 06 reuse it.

**Sound:**
- **0.0–0.4 s TAPE-STOP** of the whole mix (the Father's hymn and room tone), plus a 0.12 s glitch zap at 0.0.
- 0.4–3.0 s the hall room tone fades in: vast, a 55 Hz hum and air.
- Mouse click at +1.6 (abs 20.6). **The hall clock starts at +2.0 (abs 21.0)** and ticks every whole second from here.
- No dialogue.

*v3 sound note:* the mouse click at +1.6 is now the light pen's ring button: a small, dry plastic click.

**Motion prompt:** n/a. This shot is comp and JS in every version.

**Takes:** —
