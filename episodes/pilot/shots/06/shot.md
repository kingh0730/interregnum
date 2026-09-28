# Shot 06 — HOLD STILL (the Continuity Suite)

**Duration:** 7 s (0:30–0:37; abs 30.0–37.0)  **Tool:** JS (world screen, letterboxed)  **Camera:** none (insert of
her monitor filling the frame)

**Action:** Ida's screen. Her crosshair finds the ghost ear, grabs it and drags it home ("Hold still."); the red
box turns cyan: LOCKED. A checklist of tiny corrections ticks through, some absurd (MOLE POSITION, VOICE WARMTH +2%).
The clock counts down to air. This shot shows her craft and her detachment, and is a quiet joke about drift (our
own pipeline's problem).

**Build:** JS piece **J03 `suite`**, 7.0 s. It uses `work/pilot/k02_frozen.png` and `mesh_k02.json`. Comp:
`letterbox(2.39)`, a subtle monitor feel (0.5 px chroma, soft 10 % glow on bright UI), `grade(HALL)`, grain 2 %.

**Keyframe prompt:** none (JS only; the image asset is k02).
**Refs:** `assets/pilot/keyframes/k02_father_cu.png` (inside the UI).
**Layers:** none.

**JS spec (J03, 1920×1080, everything inside the band y 138–942, background `#0A0F1C`):**
- **Top bar** (y 150–200, 1 px `#1E2A44` rule under it):
  - Left: `MINISTRY OF CONTINUITY — NIGHT DESK 4`, DIN Alternate Bold 24 px, `#5FE1E6` at 70 %.
  - Center: `SUBJECT F`, DIN Condensed Bold 30 px, `#E9E2D0`.
  - Right: clock `20:51:22`, DIN Condensed Bold 44 px `#E9E2D0`, ticking every whole second of film time
    (20:51:22 → 20:51:28). Below it, `TO AIR 08:38` in DIN Alternate 24 px `#5FE1E6`, counting down.
- **Viewer** (x 60–1180, y 220–850, 1 px `#1E2A44` frame): the k02 frozen frame (30 % desaturated) with the J16 mesh at
  35 %. The ghost ear double is at +6 px x and 40 %, and the red box is labelled `L EAR · DRIFT +3.2 PX`.
- **Cursor:** a 24 px crosshair, `#E9E2D0`.
  - 0.3–1.0 s: enters from the right and eases to the ghost ear.
  - 1.0–1.1 s: "grab" (a small ring closes around it).
  - 1.1–2.2 s: drags the ghost −6 px in x (easeInOutCubic).
  - 2.2 s: release. The ghost fades 40 % → 0 over 0.1 s.
  - 2.3 s: the box turns `#5FE1E6` and its label becomes `L EAR · LOCKED`.
  - The cursor then drifts to the corrections panel (2.5–3.0 s).
- **Corrections panel** (x 1230–1860, y 230–830):
  - Title: `CORRECTIONS · CALIBRATION PASS`, DIN Alternate 22 px `#5FE1E6` at 70 %.
  - Items: Menlo 22 px `#E9E2D0`, 48 px line height. Each has a right-aligned status tag that flips from red `OPEN`
    (`#E0412F`) to cyan `LOCKED`/`OK` at the times shown:
    1. `L EAR — DRIFT +3.2 PX` → `LOCKED` at 2.3
    2. `MOLE, L CHEEK — POSITION` → `LOCKED` at 3.0
    3. `BLINK INTERVAL 4.1 S → 3.6 S` → `OK` at 3.6
    4. `SKIN TONE ΔE 2.8 → 0.4` → `OK` at 4.2
    5. `BREATH CYCLE` → `OK` at 4.8
    6. `VOICE WARMTH +2%` → `OK` at 5.4
- **Bottom strip** (y 870–930): a timeline with frame ticks every 8 px and a `#E9E2D0` playhead scrubbing left→right
  (x 60→1860 over 7 s). The waveform of D04 ("Eat something warm before you sleep.") is drawn as a `#5FE1E6` 40 %
  filled envelope from the rendered audio file.
- Hold to 7.0 s.

**Sound:**
- **IDA (V.O.)** (`Samantha`, 150, VO-MURMUR: close, dry, under her breath): **"Hold still."** at shot +1.0 (abs
  31.0), on the grab.
- Stylus click at +1.05 (grab) and +2.2 (release).
- UI blips (−30 dB) at each flip: 2.3, 3.0, 3.6, 4.2, 4.8, 5.4 (abs 32.3 …).
- Hall clock every second. DRONE continues.

**Motion prompt:** n/a (JS in v2).
**Takes:** —
