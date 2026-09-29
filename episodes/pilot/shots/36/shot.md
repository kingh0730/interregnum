# Shot 36 — THE RED PHONE

**Duration:** 4 s (3:08–3:12; abs 188.0–192.0)  **Tool:** Codex k22 + comp (the handset's rattle); an optional silent
Seedance take
**Camera:** an insert at the height of a seated operator's eyes, 60 mm; locked. The reaction is an object.

**Action:** In the new silence, the Committee's Red Line rattles in its cradle, loud: a heavy set cast in red phenolic,
with no dial because it cannot call out, and the Sealed Lamp in relief where the dial would be. Ida's hand lies flat
beside it and does not move. She doesn't answer. It is the old power calling into a void, and her refusal made visible
without a gesture. **Start pose:** the phone ringing, the hand still.

**Build:**
- Codex **k22**.
- **Comp (primary):** `jitter(mask=the red handset, 1.5 px, 25 Hz)` during the rings, 0.0–1.2 s and 3.0–4.0 s (the
  handset is one flat red ink shape, so the mask is a hue threshold); a 2 % brightness flicker on its lit edge in sync;
  the screen light from the upper left dims 10 % across the shot, the Wall going to standby.
- **v2 (optional):** a 4 s silent take of the rattle, if comp's jitter reads as a vibrating sticker.
- `letterbox(2.39)`, `grade(HALL)`. v1's push is gone.

**Keyframe prompt (`k22_red_phone`):**
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
> Her hand (the woman on the attached sheet): slim, and the cuff of a charcoal ribbed sweater.
> SHOT: an insert on a steel desk in blue-grey hammered enamel, worn to bare metal along its edge, seen with a 60 mm
> lens at the height of a seated operator's eyes. Left of centre, a heavy old telephone cast in signal-red phenolic, its
> handset resting in the cradle; it has no dial: where the dial would be, a round plate carries a raised emblem, a ring
> around a pointed flame inside a double ring of small dots. A braided cloth cord runs from it off the desk. At the
> right, a young woman's hand rests flat and still on the desk, fingers together, not reaching for it, the sweater cuff
> at the frame's edge. The cold pale cyan light of a screen from the upper left is dim; it cuts the top of the phone and
> her knuckles as thin shapes. Dark space lies between the phone and the hand. Everything else falls into black.

**Refs:** `assets/pilot/lookdev_v3/hall.png`, `assets/pilot/lookdev_v3/ida.png`.
**Layers:** none.
**JS spec:** none. If the emblem on the dial plate comes out wrong, lay the Sealed Lamp (the J06 stamp's artwork, in
relief) over it in comp.

**Sound:**
- **The red phone, loud and dry, close**: rings at 0.0–1.2 and 3.0–4.2 (abs 188.0, 191.0).
- Nothing else: no hum, no clock.

**Motion prompt (v2, optional; comp is primary. Seedance: start `work/pilot/keys_v3/k22_red_phone.png`, 4 s,
`--no-audio`):** Colour woodcut print animation; keep the first frame's exact carved shapes, flat inks and designs. An
insert of a heavy red telephone on a steel desk, a woman's hand resting flat beside it. For the first second the
handset rattles in its cradle as the telephone rings; it stops; after three seconds it rattles again. The hand does not
move at all. Locked-off camera. No sound.

**Takes:** —
