# Shot 03 — "EAT SOMETHING WARM"

**Duration:** 7 s (0:12–0:19; abs 12.0–19.0)  **Tool:** Codex keyframe + comp (broadcast, full frame)
**Camera:** locked-off broadcast CU, slow push-in 1.00→1.04 on his eyes

**Action:** Closer. "I am well." A long beat. Then a line no statesman says: "Eat something warm before you sleep."
It plays as paternalistic cosiness now and is revealed later as a grandmother's words. The last frame of this shot
becomes the frozen frame of shot 04. **Start pose (v2):** head and shoulders, eyes on the lens, lips closed, kindly.

**Build:**
- Codex: generate **k02** after k01, **attaching k01 for identity**. Command:
  `tools/imagegen/gen.sh assets/pilot/keyframes/k02_father_cu.png "<prompt>" assets/pilot/lookdev/ld6_father.png assets/pilot/keyframes/k01_father_mcu.png`
- **Acceptance:** k02 must read as the same man as k01 (beard shape, hairline, mole on his left cheek, which is image
  right). k02 is the most reused image in the film (shots 03, 04, 05, 06, 12, 23, 31, 34, and the TVs), so retake it
  until it matches.
- Comp: `push(1.00→1.04, focus=(0.50, 0.42), easeInOutSine, 0–7 s)`, `broadcast()` with the J14 bug, and
  `grade(BROADCAST)`. **Freeze the push at shot +6.9**; the final frame is exported as `work/pilot/k02_frozen.png`
  for shots 04–06.
- No letterbox.

**Keyframe prompt (k02):**
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
> collar. He is an invented character and must not resemble any real person. He is exactly the same man as in the
> attached images: same face, hair, beard, coat and pin.
> SHOT: a close-up broadcast picture, head and the top of the shoulders, perfectly centered, eyes level with the lens
> and looking straight into the viewer's eyes; a kind, patient expression, lips closed. The small dark mole high on
> his left cheekbone (on the right side of the image) is clearly visible. The soft circular pale-cyan halo is partly
> visible behind his head on the deep-blue backdrop. Lighting: a soft frontal key from the left and a cool cyan rim
> light. Leave a little space above his head. Both ears are visible.

**Refs:** `assets/pilot/lookdev/ld6_father.png`, `assets/pilot/keyframes/k01_father_mcu.png`.
**Layers:** none.

**JS spec:** the J14 bug, as in shot 02. Broadcast-style captions.

**Sound:**
- **FATHER** (`Daniel`, 135, BROADCAST): **"I am well."** at shot +0.6 (abs 12.6); **"Eat something warm before
  you sleep."** at +3.0 (abs 15.0).
- HYMN: **D** 12.0–15.5, **A** 15.5–19.0.
- Broadcast tone.
- The shot ends mid-chord: shot 04 tape-stops the whole mix at 19.0.

**Motion prompt (v2):** Close-up television broadcast, flat 2D cel-painted style. The old man, calm and kind, says
"I am well." then, after a pause, gently: "Eat something warm before you sleep." A very slight head tilt on the last
line, eyes on the lens throughout. Locked-off camera, slow push-in. Studio room tone, no music.

**Takes:** —
