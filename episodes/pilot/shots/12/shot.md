# Shot 12 — THE LOOP

**Duration:** 8 s (1:03–1:11; abs 63.0–71.0)  **Tool:** JS (world screen) + dialogue sound design  **Camera:** none
(screen insert)

**Action:** She lets him speak: FREE GENERATION. The machine writes the Father on its own, word by word, while his
voice reads it. It starts plausibly, then can only repeat: *I am well. I am well. I am well.* The text floods the
panel, then the whole screen. Confidence stays at P = 0.99 as the voice multiplies into a choir of itself. A red
STOP, then silence. **This is the thesis in one image:** a model trained only on the past can only produce more of
it.

**Build:** JS piece **J07 `loop`**, 8.0 s, driven by the D06/D07 audio. The speaking-indicator waveform reads the
rendered audio's amplitude envelope, precomputed to JSON. Comp: `letterbox(2.39)`, monitor feel, `grade(HALL)`.

**Keyframe prompt:** none (JS only).
**Refs:** `assets/pilot/keyframes/k02_father_cu.png` (preview thumbnail).
**Layers:** none.

**JS spec (J07, inside the band, background `#0A0F1C`):**
- **Top bar:** as J03. Mode tag `● FREE GENERATION`, `#E0412F`, with the dot blinking at 1 Hz. The clock runs
  `20:53:40` → `20:53:47` and TO AIR runs `06:20` → `06:13`.
- **Preview** (x 60–620, y 230–545): the k02 frozen frame at full color, mesh at 20 %. Under it, a 560×60 waveform
  of the voice (`#5FE1E6`), live.
- **Text panel** (x 680–1860, y 230–850): Menlo 34 px `#E9E2D0`, 50 px line height, words appending at the
  speaking rate from 0.3 s:
  `Good evening, my children. The harvest is in. The sea is calm. I am well. Sleep safely; I am watching over you.
  I am well. The sea is calm. I am well. I am well. I am well. I am well…`
  - From 3.5 s, only `I am well.` is appended, accelerating from 3/s to 15/s by 7.0.
  - The panel auto-scrolls.
- **Right edge:** a confidence column, Menlo 20 px `#5FE1E6`, printing `P = 0.99` beside every phrase.
- **Overflow (6.0–7.4 s):** the loop escapes the panel. `I AM WELL.` in DIN Condensed 60 px `#5FE1E6` at 25 % tiles
  the whole band behind the UI and scrolls up fast (600 px/s, rising to 1500 px/s).
- **7.4 s STOP:** a centered `■ STOP` in DIN Condensed Bold 40 px `#E0412F`, flashing 2 frames on, 2 off, then held.
  Everything freezes, and all text dims to 30 % over 0.3 s. Hold to 8.0.

**Sound:**
- **FATHER (generated)** (`Daniel`, 150, LOOP chain, dry): D06 from shot +0.3 (abs 63.3).
- **D07 Loop choir** from +3.5 (abs 66.5): about 30 copies of "I am well.", accelerating, detuned ±15–40 cents,
  randomly panned, and getting darker (full recipe in `cues.md` §6). The DRONE and PAD glide up a semitone, D→E♭.
- **At +7.4 (abs 70.4): mute everything, including the hall clock.** Total silence until 71.0.
- Subtitle: *I am well. I am well. I am well…*

**Motion prompt:** n/a (JS in v2).
**Takes:** —
