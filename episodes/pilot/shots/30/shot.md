# Shot 30 — THE STREET

**Duration:** 6 s (2:37–2:43; abs 157.0–163.0)  **Tool:** Codex k17 + the Public Receiver insert (from the address
take), then a silent Seedance take (v2) or comp (v1)
**Camera:** 35 mm at head height (1.5 m), inside the crowd, umbrellas in the foreground (the crowd's eye); locked

**Action:** A tram stopped mid-street in the rain. A crowd under umbrellas faces the Public Receiver, a great
rear-projection screen set into the district's civic building like an altarpiece. On it the Father says: "I died in
the spring." The words echo off the buildings. The tram's hum cuts out, and there is only rain moving through the
projector's beam. Nobody moves: a whole city holding still.
**Start pose:** a crowd standing still, facing the screen.

**Build:**
- Codex **k17**: the screen is blank.
- **The Public Receiver insert** (`production_design.md` §8): v2, the address take's frames for the line (its segment
  around "I died in the spring.", in sync with the audio); v1, k01. Through the projection look: soft focus, a hot spot
  at the centre, dark corners, scanlines visible at this scale, the J14 bug inside the picture, and a cold spill on the
  umbrellas and the wet street driven by the inserted picture's luma. Rain streaks cross the beam in front of the
  screen. Save the first frame as `work/pilot/v3/k17_screen.png`, the Seedance start frame.
- **v2:** a 6 s silent take for the rain. The camera is locked, so the screen quad is static: re-insert the picture on
  every frame.
- **v1 fallback:** `rain(layers=2)` as carved cut lines whose alpha follows the beam's luminance, small splashes at
  street level, the tram's windows steady.
- The camera is locked; v1's push and parallax layer are gone. `letterbox(2.39)`, `grade(CITY)`.

**Keyframe prompt (`k17_street`):**
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
> SHOT: a street at night in rain, seen with a 35 mm lens from inside a crowd at head height. In the near foreground, the
> black domes of umbrellas and the backs of heads and shoulders crowd the lower third of the frame as solid black shapes
> cut by thin cold rims. Beyond them, forty or more people stand perfectly still under umbrellas, all facing away from
> us toward the end of the street, their faces lifted and unseen. At the end of the street, set into a board-formed
> concrete civic building under a heavy pediment with a round bronze emblem above it, a huge rear-projection screen
> glows blank, even pale cyan: the only strong light, which falls on the tops of the umbrellas and on the street as long
> cut shapes of cold ink. At the left, a single tram car stands stopped mid-street: a rounded nose with one round
> headlamp, a ribbed body in dull cream and grey, a trolley pole to the overhead wires, its windows lit cold. Rain falls
> as fine slanted cut lines, visible only where it crosses the screen's beam. Mercury street lamps on concrete posts
> give a thin blue-green light; there is no orange light anywhere. Composition: the glowing screen in the upper centre,
> the crowd across the lower half; no face is visible.

**Refs:** `assets/pilot/lookdev_v3/city.png`.
**Layers:** none. v1's `k17_fg_crowd` is cut: the shot no longer moves.
**JS spec:** the J14 bug inside the inserted picture (shot 02).

**Sound:**
- City rain and street splashes; the tram idle hum from 0.0 to **1.8 (abs 158.8), then cut dead**.
- **FATHER** (`Daniel`, 130, STREET chain: echoing off the buildings with a 350 ms slapback): **"I died in the
  spring."** at shot +0.8 (abs 157.8).
- After the line: only rain.
- No music, no clock, no phone.

**Motion prompt (v2, Seedance: start `work/pilot/v3/k17_screen.png`, 6 s, `--no-audio`):** Colour woodcut print
animation; keep the first frame's exact carved shapes, flat inks and designs. A wet street at night seen from inside a
crowd at head height: people under umbrellas stand facing a huge glowing screen on a building at the end of the street,
and a tram is stopped at the left. Nobody moves; the umbrellas and the tram stay still. Rain falls through the cold
light of the screen in fine slanted lines, and drops splash on the street. Locked-off camera. No sound.

**Takes:** —
