# Shot 01 — IDENT: THE EVENING ADDRESS

**Duration:** 5 s (0:00–0:05; abs 0.0–5.0)  **Tool:** JS (broadcast, full frame)  **Camera:** locked (graphic)
**Action:** The nation's nightly ritual begins. On deep broadcast blue, the Lamp emblem draws itself (circle,
flame, base line) to three bell notes, then THE EVENING ADDRESS · 21:00. It is warm, official and faintly sacred. The
same piece returns faster and colder in shot 28, and in the old key in the alt stinger (46).

**Build:** JS piece **J01 `ident`** rendered 5.0 s at 24 fps, piped straight to ffmpeg. Comp: `broadcast()` without
the bug (the ident is the channel itself), `grade(BROADCAST)`, **no letterbox**. Fade up from black 0.0–0.4 s, and a
hard cut at 5.0.

**Keyframe prompt:** none (JS only).
**Refs:** none.
**Layers:** none.

**JS spec (J01, 1920×1080, full frame, opaque):**
- Background: a radial gradient centered at (960, 470), `#123A5E` at the center to `#07111F` at the edges.
- **Circle:** center (960, 450), r 150 px, 10 px stroke `#5FE1E6`. It draws on clockwise from 12 o'clock over
  0.5–1.4 s (easeInOutCubic).
- **Flame:** a teardrop 70 px wide and 130 px tall, standing on (960, 500), filled `#5FE1E6` with a radial core
  `#E9FBFF`. It grows from scale 0 at its base to 1 over 1.0–1.8 s (easeOutBack, 6 % overshoot), then breathes
  ±2 % at 0.5 Hz until the end.
- **Base line:** at y 520, 8 px, `#5FE1E6`, growing from width 0 to 180 px (centered) over 1.4–1.9 s.
- **Glow:** one pulse of outer glow (blur 40 px, opacity 0 → 35 % → 12 %) over 1.8–2.6 s, then held at 12 %.
- **Title:** `THE EVENING ADDRESS`, DIN Condensed Bold 64 px, tracking 0.35 em, `#E9E2D0`, centered at y 700. It fades
  up 2.2–3.0 s with a 12 px upward drift.
- **Time:** `21:00`, DIN Alternate Bold 34 px, `#5FE1E6` at 70 %, y 760, fading up 2.6–3.2 s.
- Hold until 5.0 s.
- **Variant `fast`** (shot 28, 3.0 s): circle 0.2–0.7, flame 0.5–1.0, base 0.7–1.0, title 1.0–1.5, time 1.2–1.6,
  hold to 3.0.
- **Variant `alt`** (shot 46): identical to `fast`, starting at shot +1.0 s.

**Sound:**
- CHIME (BELL) **A4 at 0.5, F♯4 at 1.0, D4 at 1.5**, synced to circle, flame and base line.
- HYMN D major swell 1.0–4.8 (1M1).
- Broadcast studio tone (soft hiss at −48 dB).
- No dialogue.

**Motion prompt:** n/a. This piece stays JS in v2.
**Takes:** —
