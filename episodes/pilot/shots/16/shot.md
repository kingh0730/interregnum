# Shot 16 — NANA'S ROOM

**Duration:** 6 s (1:24–1:30; abs 84.0–90.0)  **Tool:** Codex keyframe + cutout layer + comp + TV insert  **Camera:**
wide, from behind and beside Nana; slow push-in 1.00→1.04 toward her, parallax

**Action:** Inside the warm window. Nana sits small in a worn armchair before an old television showing the stand-by
Lamp. There are two teacups, hers and one in front of the empty chair; soup on a two-ring stove; rain running down
the glass. A nightly ritual of waiting. The cream telephone rings. **Start pose (v2):** Nana facing the TV, back
three-quarters to camera; on the ring, she turns her head toward the phone.

**Build:**
- Codex **k09**:
  `tools/imagegen/gen.sh assets/pilot/keyframes/k09_nana_room.png "<prompt>" assets/pilot/lookdev/ld3_apartment.png assets/pilot/lookdev/ld5_nana.png`
- Codex layer **k09_fg_nana** (`ALPHA=1`, attach k09).
- Comp:
  - `insert(J15 stand-by, target=auto)` into the TV screen, with a small CRT curvature (barrel distortion 3 %) and
    scanlines.
  - `flicker(mask=cyan_lit, driver=insert_luma, 4 %)`. The lamp stays steady.
  - `steam(pot lid)` and `steam(the full teacup)`: slow, warm-lit, fading at 60 px height.
  - `drops(window region)` with runs, plus `rainshadow` on the wall under the window at 4 %.
  - `push(1.00→1.04, focus=Nana's head)`, with `parallax(k09_fg_nana=1.0, plate=0.7)`.
  - **Phone ring:** `jitter(mask=the cream phone's handset, 1 px, 25 Hz)` during rings 3.5–3.9 and 4.1–4.5, and
    again 5.5–5.9.
  - `letterbox(2.39)`, `grade(HOME)`.

**Keyframe prompt (k09):**
> STYLE: a single frame from a premium adult 2D animated film. Hand-painted cel-animation look: clean, confident
> dark-navy ink contour lines; flat color shapes with one hard-edged shadow tone; soft airbrushed glow only around
> light sources; subtle paper grain; realistic human proportions and faces (not chibi, no oversized eyes); simplified
> graphic backgrounds with bold silhouettes and large areas of dark negative space. PALETTE: deep ink-navy and
> blue-black darkness; cold pale-cyan light comes only from screens; warm amber light comes only from household lamps
> and warm objects; signal red only where described; no other saturated colors. LIGHT: one strong motivated light
> source, deep shadows, light haze. FRAME: wide 16:9 landscape; keep every important element inside the central
> horizontal band, because the top and bottom 13% will be cropped to a 2.39:1 letterbox. No text, letters, numbers,
> logos or watermarks anywhere; every screen is a blank, evenly glowing panel.
> CHARACTER: NANA: a small woman of 82 with silver-white hair in a low bun held by a dark wooden hairpin, a soft round
> face with deep smile lines, bright dark eyes behind thin round gold wire-rimmed glasses, warm light-brown skin,
> small pearl stud earrings; she wears a dark bottle-green knitted cardigan over a cream blouse with a tiny faded
> floral print. She matches the attached character sheet.
> LOCATION: Nana's small apartment at night, as in the attached style frame. The room is seen from behind and
> slightly to the side of Nana, who sits in a worn armchair with her back three-quarters to us, small and still,
> facing an old boxy television set on a lace-covered cabinet at the right. The television screen is a blank, evenly
> glowing cyan panel. Between them, on a side table: a warm amber table lamp with a pleated fabric shade, and an old
> cream-colored telephone with a rotary dial and a coiled cord. A small table holds two teacups, one near her and one
> untouched in front of an empty wooden chair. In the far corner, a tiny two-ring stove with a small lidded pot. A
> rain-streaked window shows cyan-lit towers beyond, and there is a plain round wall clock with no numerals. The room
> is split between warm amber lamplight on the left and cold cyan television light on the right. Composition: Nana on
> the left third, the TV on the right third, the lamp between them. Mood: warm, patient, a nightly ritual.

**Refs:** `assets/pilot/lookdev/ld3_apartment.png`, `assets/pilot/lookdev/ld5_nana.png`.

**Layers:** `assets/pilot/layers/k09_fg_nana.png` (`ALPHA=1`, attach k09). Prompt:
> Using the attached image, isolate only the elderly woman together with her armchair, exactly as they appear, with
> the same position, scale, lighting and flat cel-painted style, on a genuinely transparent background. Everything
> else must be fully transparent. Keep the image the same size as the original.

**JS spec:** **J15 stand-by** on the TV.

**Sound:**
- Room tone; rain on the glass; **Nana's wooden clock** ticks every whole second (tick/tock).
- TV hum and a faint stand-by tone from the set; the pot simmering.
- **Nana's phone:** a soft double ring at shot +3.5 (abs 87.5) and +5.5 (abs 89.5). Handset lift click at +5.9 (abs
  89.9).
- Warm PAD (F) continues at −30 dB.

**Motion prompt (v2):** Flat 2D cel-painted style. A small warm apartment at night. An elderly woman sits in an
armchair, back three-quarters to camera, facing an old television glowing blue. Steam rises from a pot and a teacup,
and rain runs down the window. The old telephone beside her rings; she turns her head slightly toward it. Slow
push-in. Rain, a clock ticking, a telephone bell. No music.

**Takes:** —
