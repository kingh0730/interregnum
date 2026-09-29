# Shot 46 — NIGHT 213 (alternate ending, a separate tail; not in the main cut)

**Duration:** 10 s (alt cut 4:02–4:12; abs 242.0–252.0)  **Tool:** Codex plate p08 (a crop on the counter) + JS (the
drums) + the Lighting film (J01 `alt`) + the opening take or k01 (broadcast, 4:3)
**Camera:** a locked insert on the counter, then the broadcast as in 02

**Action:** The cynical ending, built so the two tones can be compared side by side. The next night, on the dark desk,
the GENERATED counter rolls from 212 to 213 with a mechanical click: continuation as a sound. Then the Lighting, the
whole ritual in the old key, warm and full; the sweet hymn is back. The Father, as if nothing had happened: "Good
evening, my children." A beat. "I am well." Black. Someone else is at Desk 4, or no one is and the machine is running
free. The old refuses to die, and the new cannot be born.

**Build:** render as `work/pilot/shots/46.mp4` and **append it only in the alt reel** (main cut + 46).
- **0.0–1.0 s, the counter (2.39, letterboxed: this is the world):** p08, cropped 1.8× on the GENERATED counter, relit
  cold: the light table's warm window masked to black, and a dim cold wash from the Wall's standby glow. JS rolls the
  drums 212 → 213 at 0.5 s (the units drum rolls from 2 to 3 in 4 frames). The crop is soft; it is a dark insert in the
  alt tail, and grain covers it.
- **1.0–4.0 s:** the Lighting (J01 variant `alt`, below), full frame 4:3, normal warmth.
- **4.0–9.6 s:** the Father at 4:3, as in 02. **v2:** reuse the opening take (no new generation): its greeting from the
  02 segment, then a cut on the beat to "I am well." from the 03 segment, a vision-mixer cut to the closer framing.
  **v1:** k01 exactly as shot 02 (`push(1.00→1.035)`), with "I am well." over the same picture. `broadcast()` with the
  J14 bug including LIVE, `grade(BROADCAST)`. No stutter: the picture is perfect.
- **9.6 s:** hard cut to black; hold to 10.0.

**Keyframe prompt:** reuses **p08** (prompt in `shots/08/shot.md`), **p01** (prompt in `shots/01/shot.md`) and **k01**
(prompt in `shots/02/shot.md`); no new generation.
**Refs:** none (no generation).
**Layers:** none.

**JS spec:**
- **The counter (J19):** three black drums with white numerals behind a small glass window, and the engraved plate
  GENERATED in State Capitals (cream-filled). At 0.5 s the units drum rolls 2 → 3 (4 frames, a 1-frame settle). There is
  no carry. It replaces v1's Menlo "NIGHT 213" card.
- **J01, variant `alt`:** the Lighting from film time 0.2 (just after the splice bump), so shot time = film time + 0.8:
  the spotlight at 1.3, the catch at 1.8, the flame at 2.3, the caption card at 3.0–3.8. The tint is the old warmth: the
  monochrome mapped toward cream, with no cold cast.
- **J14 bug** and closed captions as in shot 02.

**Sound (1M7):**
- **CHIME A4, F♯4, D4 at abs 243.3, 243.8, 244.3**: the original, warm and full.
- HYMN D major 243.8–246.5.
- **FATHER** (`Daniel`, 135, BROADCAST): **"Good evening, my children."** at abs 246.8; **"I am well."** at abs
  249.6.
- 251.6: cut to silence.

*v3 sound note:* add the drum's click at shot +0.5 (abs 242.5), dry, in the empty hall's reverb.

**Motion prompt:** n/a. It reuses shot 01's take and the opening take (02–03).

**Takes:** —
