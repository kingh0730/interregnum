# Shot 34 — EYES CLOSE

**Duration:** 6 s (3:00–3:06; abs 180.0–186.0)  **Tool:** Codex keyframe (k02) + Codex edit (k20) + comp (broadcast,
full frame)  **Camera:** locked-off CU; the push continues 1.04→1.06, then holds

**Action:** The Father looks at us a moment longer. Then, slowly, he closes his eyes, and he does not open them. The
broadcast holds on him in dead air. The hall clock, which has ticked since 0:21, stops. After 212 nights, the old man
is finally allowed to die, and the stillness we have watched all film becomes what it always was. **Start pose
(v2):** k02, eyes open. End: k20, eyes closed.

**Build:**
- Codex **k20**, an **edit** of k02 (attach only k02):
  `tools/imagegen/gen.sh assets/pilot/keyframes/k20_father_eyes_closed.png "<prompt>" assets/pilot/keyframes/k02_father_cu.png`
- **Acceptance:** everything except the eyelids matches k02. Difference the two images; changes outside the eye
  region must be negligible. If Codex shifts the picture, align it with SIFT (`v2_align_layers.py`) and, if needed,
  paste only the eye region from k20 into k02 with a feathered mask.
- Comp (at push 1.04→1.06 over the whole shot):
  - 0.0–1.0 s: k02 (eyes open).
  - **1.0–2.5 s: dissolve k02 → k20** (easeInOutSine), with a subtle 3 % luma dip at the midpoint. This is the only
    dissolve in the film.
  - 2.5–6.0 s: hold k20.
  - `broadcast()` with the J14 bug; at 5.6 s the `LIVE` text blinks out (the emblem stays). `grade(BROADCAST)`.
  - No letterbox. Hard cut at 6.0.

**Keyframe prompt (k20, edit of k02):**
> STYLE (keep exactly): a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean,
> confident dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow;
> subtle paper grain; realistic proportions. This image is itself a television broadcast picture that fills the whole
> 16:9 frame. PALETTE: deep blue backdrop, cool pale-cyan rim light, soft neutral studio key light. No text, letters,
> numbers, logos or watermarks anywhere.
> EDIT the attached image: close the old man's eyes gently, as if he has peacefully fallen asleep. His eyelids are
> relaxed, the lashes down, his expression the same calm and kind one, and his mouth closed. Change nothing else at
> all: the same face, white hair, white beard, mole, charcoal high-collared coat and silver pin, and the same deep-blue
> backdrop and halo, lighting, framing, colors and line style, pixel-aligned with the original.

**Refs:** `assets/pilot/keyframes/k02_father_cu.png` (the image being edited).
**Layers:** none.
**JS spec:** the J14 bug; `LIVE` removed at 5.6 s.

**Sound:**
- **At 0.0 (abs 180.0): dead air.** All music stops mid-phrase (Nana's theme is cut after G4). **The hall clock
  stops; its last tick was at 179.0.**
- Only broadcast hiss at −50 dB for the whole shot. There is no dialogue.
- Pre-lap at 5.8: nothing. Let the silence be complete.

**Motion prompt (v2):** Close-up television broadcast, flat 2D cel-painted style. The old man looks into the lens
for a moment, then slowly and peacefully closes his eyes and remains perfectly still. Locked-off camera. Faint studio
hiss, then silence. No music. (Use first/last-frame mode with k02 → k20 if the model supports it.)

**Takes:** —
