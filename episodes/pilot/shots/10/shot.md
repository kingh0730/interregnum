# Shot 10 — CAPSULE

**Duration:** 3 s (0:54–0:57; abs 54.0–57.0)  **Tool:** Codex k05 (the empty cup) + k05b (an edit: the capsule
seated), then a silent Seedance take between them (v2) or a matte drop (v1)
**Camera:** macro, 60 mm, at desk height; locked-off

**Action:** A rumble travels through the pipes. A black-lacquered capsule with a band of red lacquer shoots out of the
brass tube and slams into the cup. Dust, and a hiss of air. The Committee still speaks in paper and brass: the old
machinery of power beside the new. **Start pose:** the empty cup under the pipe mouth; the capsule arrives from the
pipe.

**Build:**
- Codex **k05** (the empty cup) and **k05b**, an edit of k05 with the capsule seated. k05b is Seedance's end frame and
  the source of the capsule in the v1 fallback, so the capsule has one design in both versions and in shot 11.
- **v2:** a 4 s silent take from k05 ending on k05b (`--end`). Slip it so the impact lands at 1.35 s, and use 3 s.
- **v1 fallback:** the capsule matte cut from k05b (flat inks: GrabCut, or a threshold on the black lacquer and red
  band), composited over k05 with the cup's front lip matted over it:
  - 1.20 s: the capsule appears at the pipe mouth (60 % scale, moving along the pipe's axis), with 5-subframe motion
    blur.
  - 1.20–1.35 s: it drops into the cup (ease-in, gravity), scaling to 100 %.
  - **1.35 s, impact:** `shake(6 px, 0.3 s)`, `puff(cup rim, 30 particles)` of pale dust as carved specks, and the
    lip's thin pale line brightening for 3 frames at 1.40.
  - 1.35–3.0 s: it rocks once (±1.5° over 0.3 s), then settles on k05b's pose.
- `letterbox(2.39)`, `grade(HALL)`. v1's micro push is gone.

**Keyframe prompt (`k05_cradle`):**
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
> SHOT: a macro close-up at desk height with a 60 mm lens, at the left end of an operator's desk in a dark hall. A
> pneumatic tube of tarnished brass, 8 centimetres across, olive-black with green at its joints, comes down from the
> top of the frame and bends into an open mouth. Below the mouth, fixed to the desk's edge, a heavy cast-brass cup on
> a spring stop with a felt pad inside, empty. Only the cup's lip is polished bright by use, a thin pale cut line; the
> rest of the brass is dark and never shines. A small pressure gauge with a blank cream dial sits on a junction box on
> the pipe. One repair: a newer brass sleeve clamped over an old joint in the pipe. The cold pale cyan light of a
> monitor out of frame at the left cuts the pipe's left edges and the cup's rim as thin shapes; the rest falls into
> black, with the faint depth of a vast hall behind. Composition: the pipe mouth at upper centre and the empty cup at
> lower centre, with clear dark space between them for something to drop in.

**Keyframe prompt (`k05b_capsule`, an edit of k05):**
> STYLE (RELIEF): a frame from an animated film printed by hand as a colour woodcut and linocut on warm cream paper. A
> carved blue-black key block holds the image; large areas stay solid black, with faint wood grain. Every surface (skin,
> cloth, hair, concrete, metal, glass, floor) is matte printed ink: no reflections, no sheen, no specular highlights, no
> smooth gradients. Light is a shape cut out of the black with crisp, slightly irregular knife edges. Middle tones
> everywhere, on walls, floors and machines as on faces, are parallel gouge strokes that follow the form. Colour is flat
> spot ink, never blended, with paper grain showing through: pale cold cyan where screens light things, amber where lamps
> light things, signal red only on red objects. Slight misregistration; no drawn outlines. Only screen light is soft.
> Faces are a few carved planes, calm; eyes are small dark shapes without highlights. Avoid: anime, airbrush, digital
> painting, 3D render, photorealism, lens flare, bokeh, neon, glossy or wet floors.
> EDIT the attached image: a pneumatic message capsule has just dropped into the brass cup and lies in it. It is a
> black-lacquered steel cylinder about a forearm long, with knurled brass end caps and a band of red lacquer around its
> middle stamped with a small round emblem; it lies horizontally in the cup, seen from the side, lit by the same cold
> light from the left. A small puff of pale dust hangs over the cup's rim. Change nothing else: the pipe, the cup, the
> gauge, the light, the framing, the carving and the inks stay exactly as they are, aligned pixel for pixel.

**Refs:** k05: `assets/pilot/lookdev_v3/hall.png`. k05b: `work/pilot/keys_v3/k05_cradle.png` (the image being edited).
**Layers:** none. v1's `k05_capsule` cutout is cut: Seedance brings the capsule in v2, and the v1 fallback mattes it
from k05b.
**JS spec:** none. If the emblem on the band comes out wrong, stamp the Sealed Lamp over it in comp (the J06 stamp,
shot 11).

**Sound:**
- 0.0–1.2 s: rumble travelling through the pipes (brown noise LPF 300 Hz, filter rising, panned L→C).
- **1.35 (abs 55.35): WHUMP and metallic clank.**
- 1.45–2.5: a hiss of released air.
- Hall clock (55, 56); DRONE.

**Motion prompt (v2, Seedance: start `work/pilot/keys_v3/k05_cradle.png`, `--end work/pilot/keys_v3/k05b_capsule.png`,
4 s, `--no-audio`):** Colour woodcut print animation; keep the first frame's exact carved shapes, flat inks and
designs. A macro close-up at desk height: a brass pneumatic pipe comes down into an empty brass cup. Nothing moves for
one second. Then a black capsule with brass end caps and a red band shoots out of the pipe mouth, drops hard into the
cup, rocks once and settles; a small puff of dust rises from the rim. Locked-off camera. No sound.

**Takes:** —
