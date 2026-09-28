# Shot 02 — THE FATHER

**Duration:** 7 s (0:05–0:12; abs 5.0–12.0)  **Tool:** Codex keyframe + comp (broadcast, full frame)
**Camera:** locked-off broadcast MCU with a slow push-in 1.00→1.035 on his eyes

**Action:** The Father, dead-center, looks into the lens and greets the nation. Nothing about him moves. He is a
portrait that has learned to talk: warm, reassuring and slightly wrong. The audience should feel the stillness before
they understand it (shot 04 explains it). **Start pose (v2):** seated upright and square to the lens, mouth closed, a
calm half-smile, about to speak.

**Build:**
- Codex: generate **k01** first (this is also the pipeline test, straight after ld1). Command:
  `tools/imagegen/gen.sh assets/pilot/keyframes/k01_father_mcu.png "<prompt>" assets/pilot/lookdev/ld6_father.png assets/pilot/lookdev/ld1_hall.png`
- Comp: `push(1.00→1.035, focus=(0.50, 0.40), easeInOutSine, 0–7 s)`. Then `broadcast()` with the J14 bug (emblem
  top-left, LIVE bottom-right), and `grade(BROADCAST)`. Add luminance breathing of ±1.5 % at 0.3 Hz.
- **A plant:** a one-frame stutter at shot +4.2 s. Hold the previous frame for 2 frames, then give one frame a 3 px
  horizontal offset on one 120 px-high slice across the mouth. It is barely perceptible.
- No letterbox.

**Keyframe prompt (k01):**
> STYLE: a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean, confident
> dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow; subtle paper
> grain; realistic human proportions and face (not chibi, no oversized eyes). This image is itself a television
> broadcast picture: it fills the whole 16:9 frame edge to edge, with no TV set and no screen border. PALETTE: deep
> blue backdrop, cool pale-cyan rim light, soft neutral studio key light on the face; no other saturated colors. No
> text, letters, numbers, logos or watermarks anywhere.
> CHARACTER: THE FATHER: an elderly man of about 85 with a broad, heavy-boned face, thick silver-white hair combed
> straight back from a high forehead, heavy white eyebrows, a short neatly trimmed white beard, deep-set dark eyes with
> a gentle grandfatherly expression, a small dark mole high on his left cheekbone, weathered warm-tan skin; he wears a
> plain charcoal high-collared wool coat buttoned to the throat, with a small round silver pin on the left side of the
> collar. He is an invented character and must not resemble any real person. Match the attached character sheet
> exactly.
> SHOT: a medium close-up broadcast picture, framed from mid-chest up, perfectly centered and symmetrical, with his
> eyes on the upper-third line and generous headroom. He sits upright, square to the viewer, and looks directly into
> the lens with a calm, warm, grandfatherly half-smile; mouth closed, about to speak; shoulders relaxed; hands out of
> frame. Behind him is a smooth deep-blue studio backdrop with a soft circular pale-cyan halo of light centered behind
> his head, like a rising moon. Lighting: a soft frontal studio key from slightly left, a gentle cool cyan rim on his
> hair and shoulders, no harsh shadows. Mood: reassuring, timeless, faintly uncanny in its perfection.

**Refs:** `assets/pilot/lookdev/ld6_father.png`, `assets/pilot/lookdev/ld1_hall.png` (style).
**Layers:** none.

**JS spec:** uses the shared overlay **J14 bug**: the emblem at 60 px, top-left (70, 60), 60 %; `LIVE` in DIN
Alternate Bold 26 px `#E9E2D0` at (1790, 1010). Captions in broadcast style (closed-caption box, Menlo 30 px, at
y≈950).

**Sound:**
- **FATHER** (`Daniel`, rate 135, BROADCAST chain): **"Good evening, my children."** at shot +0.6 (abs 5.6);
  **"The harvest is in. The sea is calm."** at +3.0 (abs 8.0).
- HYMN progression (1M1): **D** 5.0–8.5, **G** 8.5–12.0, at −26 dB under the voice.
- Broadcast studio tone. No clock (we are inside the television).
- Give the 4.2 s stutter a 1-frame digital tick at −36 dB.

**Motion prompt (v2, Seedance):** Television broadcast in a flat 2D cel-painted style. The elderly man sits
perfectly composed and speaks directly into the lens, warm and slow: "Good evening, my children. The harvest is in.
The sea is calm." Minimal head movement, one slow blink, an almost unnaturally smooth stillness. Locked-off camera,
very slow push-in. Soft studio room tone, no music.

**Takes:** —
