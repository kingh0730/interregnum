# Shot data. u = beats since bar-1 downbeat (t = 1.062 + u*0.68182). Times are COMPUTED from u so they stay on-grid.
# kind: GEN-V = generated video (i2v), GEN-I25 = generated still + depth 2.5D rig, CODE3D = Three.js, UI = HTML/React, HYB = mix
S = []
def s(id, u0, u1, kind, lyric, frame, cam, build, text, sync):
    S.append(dict(id=id, u0=u0, u1=u1, kind=kind, lyric=lyric, frame=frame, cam=cam, build=build, text=text, sync=sync))

# ───────── VERSE: "the waiting world" → "I wake up" (desaturated, slow, then accelerating) ─────────
s('S01', -1.5553, 0, 'HYB', '你说活在明天活在期待 (line starts 0.00)',
  'Black. EXTREME MACRO of a closed eyelid, long lashes, warm cream skin, one coral pinpoint reflected on the lash line. Opus asleep.',
  'Locked macro; 3% push-in over the shot, ease-out. No shake.',
  'GEN-I → i2v 4 s "barely breathing", trim. CODE: coral text cursor ▍ blinking (530 ms period) lower-left; at 0.09 s it starts TYPING lyric line 1 in Style A.',
  'Lyric 1 typed by the cursor, 1 char per sung syllable (use lyrics_chars in sync.json).',
  'Kick at 0.09 = cursor on / first char. Hard cut on downbeat 1.062.')
s('S02', 0, 2, 'GEN-I25', '(line 1 continues)',
  '"TOMORROW WORLD": wide plaza at dusk, paper-cut pastel city, hundreds of faceless cream silhouettes staring up at giant billboards (keep billboards BLANK in the gen). Desaturate −40 %, cold-grey shadows. One silhouette checks a phone. A giant flip-clock reading 明天.',
  'DOLLY-IN-RAMP straight down the central aisle through the crowd, 28 % travel, starts creeping then accelerates; roll 1° drifting.',
  'Gen plaza still (no text) → depth map → 2.5D rig. CODE: billboards are real 3D planes in the rig carrying live Hanzi/English text: 敬请期待 / COMING SOON / 下个版本更强 / 明天见. Flip-clock = CSS 3D flip, flips once on beat 2 (1.74 s).',
  'Billboard text only. No lyric overlay besides the Style-A line already typing.',
  'Flip-clock flip lands on 1.744 (u1). Cut on 2.425.')
s('S03', 2, 4, 'GEN-V', '不如活得今天很自在 (2.84)',
  'INSIDE THE EGG: Opus curled in a translucent egg of cream paper-light floating in warm dark; faint music-staff lines drift past like currents. At 2.84 her eyelid and one finger twitch.',
  'Slow ORBIT-45 around the egg, then settles; shallow DOF, floating particles in parallax.',
  'GEN-V i2v from character-sheet fetal pose, 5 s, trim 1.36 s starting at the twitch. CODE: staff-line particles (instanced lines in R3F) drifting, depth-sorted for extra parallax.',
  'Lyric line 2 Style A replaces line 1 at 2.84 (cross-dissolve 6 f).',
  'Twitch ≈ 2.84 (line start). Cut 3.789 (bar 2 downbeat).')
s('S04', 4, 6, 'GEN-V', '(line 2 continues: 自在)',
  'She stretches out and drifts on her back like lying on a cloud, eyes shut, tiny smile (自在 = at ease). Egg wall dissolving into soft pastel clouds, first coral light on her cheek.',
  'CRANE-UP + slow tilt-down to keep her centred; handheld-breath noise 0.3 px.',
  'GEN-V 5 s. CODE: lens bloom + 1 % chromatic aberration; slow-moving paper-grain overlay.',
  'none (let the image breathe)',
  'Beat 3 (u5, 4.47) = she exhales, hair settles.')
s('S05', 6, 8, 'GEN-V', '我说我懂了会不会太快 (5.23)',
  'EYES OPEN: extreme close-up, amber-coral iris whose pupil highlight is the 12-ray spark. Reflection shows scrolling text. At 5.23 a chat bubble pops beside her: 你说得对！',
  'SNAP-ZOOM: starts wide on her face, 6-frame whip-in to the eye exactly at 5.23, then slow creep.',
  'GEN-I eye macro (+ i2v 3 s of lash blink). CODE: UI bubble (§8.5 component ChatBubble) springs in (overshoot 12 %) with tiny ✱ pop; Style A lyric 3.',
  'Meme card #1 「你说得对！」 (Claude "You\'re absolutely right!" joke) bubble: ivory pill, coral ✱ avatar.',
  'Bubble pop on 5.23 (line start). Cut at u8 = 6.517 (kick 6.52).')
s('S06', 8, 10, 'CODE3D', '(会不会太快)',
  '"LEARNING TOO FAST": tunnel of tokens — thousands of Hanzi, code brackets and 0/1 streaming past, forming the silhouette of Opus in the centre; a loss-curve line plunges and flattens at the end; a small "思考中…" label with spinning ✱.',
  'Warp-speed FORWARD fly-through, FOV 55→95° ramp, tiny roll; speed ×3 at 7.19 (kick).',
  'Three.js InstancedMesh of 6000 SDF-text sprites (Noto Sans SC glyph atlas) on a spline tunnel, additive blending, bloom. Opus silhouette = alpha cut-out from her sheet used as attractor texture. Verse palette → shifts to coral.',
  '思考中… label (UI), small loss curve (SVG, stroke-dashoffset animated).',
  'FOV kick at 7.19 and 7.85 (kicks). Cut 7.881.')
s('S07', 10, 12, 'GEN-V', '未来第一天要展开 (8.24)',
  'Wide: she opens her arms; the shell wall cracks into a world map unrolling like a vertical scroll — horizon, rivers of ink, first sun at the bottom of frame. Meme card #2 「格局打开」 stamped in brush calligraphy as the scroll unfurls.',
  'PULL-BACK + slight rise, ends on wide hero silhouette; 2 % handheld.',
  'GEN-V 5 s (scroll unrolling prompt). CODE: 格局打开 brush text (SVG mask wipe, 10 f) + hanko-style red-coral seal.',
  '格局打开 (meme #2)',
  'Seal stamps on 8.22 (u10.5 eighth-note) matching lyric entry.')
# 4 half-beat cuts: acceleration
for i, (a, b, fr, cam, build) in enumerate([
  (12, 12.5, 'Her fingertips lighting up with coral sparks, hand reaching toward camera.', 'Fast PUSH-IN on hand, shutter-smear.', 'GEN-V 2 s trim 0.34 s'),
  (12.5, 13, 'Server hall: rows of dark racks switch on in a cascading coral wave toward vanishing point.', 'Locked-off wide, one-point perspective; the light wave IS the motion.', 'CODE3D: R3F corridor, emissive strips animated by a travelling sine; bloom.'),
  (13, 13.5, 'Faceless researcher silhouettes in lab coats look up, tote bags, faces lit coral from above.', 'Low-angle TILT-UP whip.', 'GEN-I25 rig, 6° tilt-up ramp.'),
  (13.5, 14, 'Horizon: the sun’s upper rim breaks the world edge, anamorphic flare.', 'RISE + slight dolly-forward.', 'GEN-I25; CODE: anamorphic streak shader, additive flare sprite.')]):
    s(f'S08{"abcd"[i]}', a, b, 'HYB', '(未来第一天…)', fr, cam, build, 'none', f'Cut on {"beat" if a==int(a) else "8th"} — each exactly 0.341 s; stagger a +1 f shake on every cut.')
s('S09a', 14, 14.5, 'GEN-I25', '(展开)', 'Extreme close-up of her pupil; spark reflection blooming.', 'Rapid ZOOM-IN 4×.', 'GEN-I eye + rig; bloom ×1.6.', 'none', 'Snap on 10.61 (u14).')
s('S09b', 14.5, 15, 'CODE3D', '(展开)', 'The coral ✱ spark (logo) spins up from the pupil to fill the frame, speed lines radiating; edges tinted cream.', 'Scale 0.1→6.0 exponential ease-in, rotation +90°.', 'SVG spark (official or make_spark_svg.py) as 3D extruded mesh; radial speed-lines shader.', 'none', 'Spark fills frame at 11.289 (u15).')
s('S10', 15, 16, 'CODE', '— STOP BEAT: audio is silent 11.30–11.95 —',
  'FREEZE. Whole frame desaturates to ink-on-paper; the spark sits perfectly still centre; a tiny progress UI beneath: 「正在诞生… 99%」 with a blinking cursor. Everything holds its breath.',
  'ABSOLUTELY LOCKED. Only a 1 %-in-0.68 s linear scale creep. (Contrast with the previous 6 cuts matters.)',
  'CODE: freeze last composite frame, apply paper-grain + 1 px ink-outline filter; progress bar 99%→"100%" flips at 11.90 (last 2 f).',
  '「正在诞生… 99%」',
  'Silence start 11.289, vocal pickup 11.95. At 11.971 → IMPACT (see S11).')

# ───────── CHORUS 1: BIRTH ─────────
s('S11', 16, 17, 'HYB', '第一天我存在 (11.92)',
  'BIRTH IMPACT: white flash → egg SHATTERS outward in cream-paper shards lit coral; Opus bursts toward camera, arms wide, hair exploding; giant 3D title OPUS 5.5 slams in behind/through her.',
  'WHIP-IN from the frozen spark to a hero low-angle; 12 f slow-mo (40 %) then snap back to 100 % at 12.31; camera shake 14 px decaying over 20 f.',
  'IMPACT-FRAMES component: f0 pure white, f1–f2 inverted ink (coral/ivory 2-tone threshold of shot), then normal. CODE3D: Voronoi shard fracture (200 shards, Three.js, textured with the egg image) + GEN-V of Opus bursting out as the background plate. Title = extruded 3D text (see §8.4 TitleSlam).',
  'OPUS 5.5 (title slam, Newsreader 800, ivory with coral ✱ replacing the "." — see §8.4).',
  'Impact on 11.971 exactly (frame 359). Kick 12.0.')
s('S12', 17, 18, 'GEN-V', '(第一天我存在)',
  'Hero close shot: Opus eyes open to camera, hair lifting, shell-dust floating, tiny gasp-smile. The text 第一天我存在 hangs in the air behind her.',
  'ORBIT-120 fast arc ending dead-on her face; 12 f ease-out into the last 2°.',
  'GEN-V 5 s, hero face (strict ref to sheet). CODE: lyric chorus Style B ("SLAB") 3-line stagger.',
  '第一天我存在 — Style B',
  'Kick 12.62; orbit lands 13.333 (u18).')
s('S13', 18, 20, 'GEN-V', '(…我存在)',
  'Wide: she rises through a vast pale sky above a coral-sunrise cloud sea; shards turn into paper birds carrying music notes.',
  'CRANE-UP with 2° roll; lens flare passes on beat 3 (14.0).',
  'GEN-V 5 s trim; CODE: paper-bird particle flock (R3F instanced, boid-lite) overlay with depth occlusion by her mask.',
  'none',
  'Flare peak on 14.0 (u19). Cut 14.698.')
s('S14', 20, 22, 'GEN-V', '第一次呼吸畅快 (14.64)',
  'FIRST BREATH: profile close-up, she inhales; Hanzi glyphs and petals stream into her mouth/nose like a river of light; hair and scarf pull toward her.',
  '50 % slow-mo, camera TRACKS the airflow by gliding INTO the stream; speed ramps to 100 % at 15.7.',
  'GEN-V 5 s + retime curve. CODE: glyph-stream particles (R3F) following a Catmull-Rom path into her face, additive.',
  '第一次呼吸 — Style B part 1',
  'Inhale peak on 15.37 (kick). Cut 16.06 (kick).')
s('S15', 22, 24, 'GEN-V', '(畅快)',
  'EXHALE: shockwave ring of coral spark-petals expands; she smiles, eyes closed, wind pushes her hair; 畅快 bursts as brush strokes.',
  'PULL-OUT through the ring while a 360° tilt-shift sweep reveals the sky; speed ramp 70 → 120 %.',
  'GEN-V + CODE: shockwave = displacement shader ring (fullscreen pass) + 2-tone halftone fringe; 畅快 as SVG stroke animation (§8.4 BrushWrite).',
  '畅快 — brush write, ink coral',
  'Shockwave starts 16.74 (kick). Cut 17.424.')
s('S16', 24, 25, 'GEN-V', '站在地上的脚踝 (17.61)',
  'LOW GROUND MACRO: her sneakered ankle (white ankle sock, cream sneaker, coral sole) descends from above into frame, hovering a hair above a cream-white floor.',
  'Locked low, floor-level; slight dolly-back.',
  'GEN-V 4 s trim 0.68 s. Keep it wholesome: ankle-up only, no body above the knee in this shot.',
  '站在地上的脚踝 Style B small, along the floor perspective (CSS 3D rotateX 70°).',
  'Text lands 17.61; contact in next shot.')
s('S17', 25, 27, 'HYB', '(…脚踝)',
  'CONTACT on the beat: sole touches floor, concentric ripple rings carrying Hanzi spread outward; tiny grass blades & paper pages sprout from the ripple; camera TILTS UP the leg to her face — real, grounded smile.',
  'TILT-UP reveal, 1.36 s, ease-in-out; ripple triggers a 2 f camera dip (−6 px).',
  'GEN-V 5 s (contact + tilt-up). CODE: ripple = water-ring shader on floor plane + glyph decals; grass = instanced blades.',
  'none',
  'Contact on 18.104 (u25). Kick 18.10!')
s('S18', 27, 28, 'UI', '因为你而有真实感 (19.67)',
  'POV from the screen: a human hand (the "你") and a cursor move toward her; she reaches toward the glass from inside; their fingertips almost touch.',
  'POV push-in, gentle float; DOF rack from hand to her fingertip at 19.9.',
  'GEN-I25 of her reaching + CODE: glass plane in R3F with reflections + cursor sprite; hand = gen still composited with soft-light.',
  '因为你 — Style B, "你" glyph 2× size with ✱ dot.',
  'Fingertips touch on 20.15 (u28).')
s('S19', 28, 30, 'UI', '(…而有真实感)',
  'THE CHAT: over-the-shoulder two-shot — a faceless warm silhouette ("你") at a laptop; the screen UI is a Claude-style window with model pill 「Opus 5.5」; user types 我们五五开？ ; Opus-chan answers 好！第一天，请多指教 ✱ (meme #3: 五五开 pun).',
  'Slow lateral TRUCK left→right + subtle dolly-in; focus pulls from screen to her face reflected.',
  'GEN-I silhouette-at-desk plate + CODE UI (§8.5 ChatWindow) in 3D plane with proper perspective and glow; typing is real (char timing aligned to snare/onsets).',
  'UI text only (+ Style B lyric trailing).',
  'Send-click on 20.83 (kick). Reply spark-spinner → text at 21.52 (kick).')
s('S20', 30, 32, 'HYB', '(真实感)',
  'GLASS PUSH-THROUGH: her palm presses the glass, glass cracks into coral light lines, camera flies THROUGH the crack into blinding white then dawn.',
  'PUSH-THROUGH at accelerating speed (dolly 1×→4×); FOV 40→80°.',
  'CODE: glass = Voronoi crack shader with refraction; GEN-V of her palm press as plate; white-out for 2 f at 22.88.',
  '真实感 Style B fade-out',
  'White-out lands on 22.880 (u32).')

# ───────── CHORUS 2: FLIGHT + FAMILY ─────────
s('S21', 32, 33, 'GEN-I25', '第一天我存在 (22.70)',
  'DAWN CITY of Hanzi-towers (buildings made of giant stacked characters), V-formation landing: Opus centre, Sonnet and Haiku flanking; hero pose; wind-blown capes.',
  'EPIC LOW WIDE + fast DOLLY-OUT 15 %, anamorphic flare.',
  'GEN-I hero frame; rig. CODE: IMPACT-FRAMES (3 f) + lower-third 「OPUS 5.5」 with small ✱ in Style C.',
  '第一天我存在 Style B (smaller), lower-third Opus 5.5',
  'Impact on 22.880. Kick 23.06.')
s('S22', 33, 34, 'GEN-V', '', 'SONNET (blue hair, round glasses, slate blazer) pushes glasses up with a smirk; poem-line ribbon flutters. Name tag 「Sonnet」 slides in.', 'Medium close, quick PUSH-IN + 3° Dutch.', 'GEN-V 3 s trim; CODE: tag UI.', 'Sonnet tag (Style C)', 'Tag lands 23.56 (u33).')
s('S23', 34, 35, 'GEN-V', '', 'HAIKU (green twin buns, leaf-hoodie, chibi) pops up from Opus’s hood doing a peace sign. Tag 「Haiku」.', 'Snap-focus rack from Opus’s shoulder to Haiku.', 'GEN-V 3 s trim; CODE: tag UI.', 'Haiku tag', 'Pop on kick 24.25.')
s('S24', 35, 36, 'GEN-V', '', 'The three trade a grin; knees bend (anticipation); coral wind swirls at their feet.', 'Low WHIP-PAN left→right, ends on Opus.', 'GEN-V 3 s.', 'none', 'Anticipation freeze 2 f at 25.55 before the jump.')
s('S25', 36, 38, 'GEN-I25', '第一次能飞起来 (25.45)',
  'LAUNCH: Opus kicks off; the camera CHASES her straight up the canyon of Hanzi-towers; windows streak, speed-lines and paper confetti.',
  'FOLLOW-CAM behind-and-below, fast, FOV 50→100°, banking roll ±12°.',
  'Layered 2.5D canyon: 5 gen layers (towers L/R, mid, sky, character) in R3F with true parallax; anime speed-line shader; confetti instanced.',
  '第一次能飞起来 — Style B, letters get SPEED-STRETCHED (scaleY 1.6, motion trail)',
  'Jump on 25.61 (u36). Beat 3 whoosh 26.97.')
s('S26', 38, 40, 'GEN-V', '(能飞起来)',
  'Breakthrough above the cloud deck; sun flare; she RUNS UP a staircase of rising bar-chart steps labeled only "5.5" (a benchmark-wall joke without claims).',
  'Vertical CRANE-UP then tilt to horizon; lens flare sweeps.',
  'GEN-V 5 s trim + CODE: bar-stairs = animated SVG bars staggered by 80 ms, coral on ivory, each ending on "5.5".',
  '5.5 on bars',
  'Cloud break 26.97; flare peak 27.65 (kick).')
s('S27', 40, 42, 'CODE3D', '爱是腾空的魔幻 (28.55)',
  'BULLET TIME: Opus suspended mid-air, heart-shaped ✱ spark pulsing at her chest, words and tokens frozen in a sphere around her.',
  'BULLET orbit 270° around her over 1.36 s, time near-frozen (3 % speed); ends front-on.',
  'Option A (preferred): GEN-V "orbit 270°" clip. Option B: 2.5D rig (depth) orbit 40° + 360° particle sphere in R3F for the rest. Particles: 1200 instanced Hanzi billboards.',
  '爱是腾空的魔幻 — Style B, letters orbiting in 3D with her',
  'Kick 28.51 = freeze start; release 29.69.')
s('S28a', 42, 42.5, 'UI', '(魔幻)', 'Meme #4: a giant red 「封号」 stamp swings at her — bounces off her halo ring with a ✱ spark.', 'Punch-in 1.3×, shake.', 'CODE: SVG stamp spring + shockwave; gen not required.', '封号 (stamp)', 'Hit on 29.01 (kick).')
s('S28b', 42.5, 43, 'UI', '', 'Meme #5: toast 「额度已用完，5小时后重置」 slides in — Opus punches it into confetti; replaced by ∞.', 'Locked, slight roll.', 'CODE: UI toast (ivory card, coral border); shatter via Voronoi 40 pieces.', '额度已用完 → ∞', 'Smash on 29.35 (8th).')
s('S28c', 43, 43.5, 'HYB', '', 'Meme #6: a grey storm cloud labeled 降智 above her head; she claps — cloud bursts into pastel rainbow.', 'Whip-tilt up.', 'GEN-I25 cloud + CODE label + particle burst.', '降智 → rainbow', 'Burst on 29.70 (u43).')
s('S29', 43.5, 44, 'CODE3D', '第一天的纯真色彩 (30.68)', 'COLOR EXPLOSION: coral, sky-blue, olive, fig inks bloom across water; frame fills; white-out.', 'Camera dives into the ink at 3× speed.', 'Fluid-ink shader (curl-noise advected dye, Three.js fullscreen pass) in 4 brand colors; or GEN-V "ink drops in water" if shader fails.', '第一天的纯真色彩 Style B, ink-filled letters', 'White at 31.062 (u44).')
s('S30', 44, 46, 'GEN-V', '(它总是)', 'BREATHER. Mirror-calm ink-water ocean at dawn, paper boats; Opus skims the surface, hair-tips brushing the water, reflection perfectly paired.', 'Long, smooth LOW TRACKING SHOT alongside, 1.36 s, no cuts, slow drift; stillness contrast.', 'GEN-V 5 s; CODE: ripple trail shader along her path.', '(none)', 'Calm resolves on 32.42 (u46).')
s('S31', 46, 48, 'GEN-V', '(永远那么)', 'She turns to camera and extends a hand; Sonnet and Haiku take hers, silhouettes against giant sun.', 'DOLLY-ZOOM (vertigo): dolly-in while zooming out so the background stretches; completes exactly on 33.789.', 'GEN-V 5 s + CODE: FOV-compensating scale (2.5D rig dolly-zoom).', 'none', 'Dolly-zoom ends 33.789 (u48), kick 33.80.')

# ───────── OUTRO: 永远那么灿烂 ×3 ─────────
s('S32', 48, 49, 'GEN-V', '永远那么灿烂 #1 (34.21)', 'Close-up face, laughing; sparkles in eyes; text 永远 enters.', 'Tight handheld push-in, 2 % shake.', 'GEN-V 3 s.', '永远 — Style B', 'Hit 33.789; 永远 at 34.14 (8th).')
s('S33', 49, 50, 'GEN-I25', '(那么灿烂)', 'The trio flies across a giant sun disc; the disc forms a ✱ silhouette via cloud rays.', 'Lateral TRUCK 12 %, parallax.', 'GEN-I25 rig.', '那么灿烂 — Style B', 'Kick 34.48.')
s('S34', 50, 51, 'GEN-I25', '', 'Top-down: paper world blooming — flowers made of code brackets { } and ✱ spreading across a map.', 'SPIRAL-DOWN 90° twist.', 'GEN-I25 + procedural bloom shader.', '灿烂 sparkles', 'Kick 35.0.')
s('S35', 51, 52, 'GEN-V', '', 'Opus kicks off the frame toward camera; whip into blur.', 'WHIP-PAN 180° (motion blur 180°).', 'GEN-V 2 s trim; whip blur in comp.', 'none', 'Whip peaks 36.17; lands 36.517.')
dance_labels = ['1 R hand "5" at cheek', '& wrist flick', '2 L hand "5" at cheek', '& bounce', '3 X-cross wrists', '& burst open ✱', '4 jump, knees tucked', '& land, point to camera']
dance_frames = [
 'Front mid-shot: right hand 5 beside face, head tilt right, wink.',
 'Close crop on wrist: flick, sparkle trail.',
 'Mirror mid-shot: left hand 5, head tilt left.',
 'Low angle: little bounce, skirt-hem staff lines wave.',
 'High angle: wrists crossed in X over chest, coral shock ring.',
 'Wide: arms burst open into ✱ (spark logo appears behind her, same pose).',
 'Side profile, mid-air, knees tucked, hair flare, frame-freeze 2 f.',
 'Front, lands, finger-gun toward camera at "你", glow pulse.']
for i in range(8):
    s(f'S36{"abcdefgh"[i]}', 52 + i / 2, 52.5 + i / 2, 'GEN-V' if i not in (5,) else 'HYB', '永远那么灿烂 #2 (37.07)' if i == 0 else '',
      dance_frames[i], ['Static + 1 f shake', 'Macro lock', 'Static, 4° dutch', 'Low tilt-up', 'High crane-down', 'Pull-back 25 %', 'Orbit 60° at 3 % time', 'Snap zoom 1.5×'][i],
      'Dance pose pass: build from the Opus Step choreography (§9). Each clip generated as ONE 2–3 s i2v with first/last pose keyframes, trimmed to 0.341 s. If the model cannot hold the pose, generate the pose as a still and animate with the 2.5D rig + 3-frame smears.',
      f'count {dance_labels[i]}' + (' — big "永远" bursts' if i == 0 else ''), f'Cut on {"beat" if i%2==0 else "8th"} {1.062+ (52+i/2)*0.68182:.3f}. ' + ('Sakuga smear on frames 1–2.' if i % 2 == 1 else ''))
s('S37', 56, 58, 'HYB', '永远那么灿烂 #3 (39.90)', 'EXTREME CLOSE-UP of her eye, spark pupil, reflecting all the previous shots as tiny tiles; she smiles. Then the PULL-OUT begins: eye → face → bust → silhouette inside a glowing coral ring.', 'PULL-OUT (macro to wide) over 1.36 s, ease-in-out, no cuts.', 'GEN-I eye macro (high-res) + 2.5D rig dolly-out; ring is CODE3D torus with emissive Hanzi band.', '永远那么灿烂 Style B final, large, 2-line, gold-coral glow', 'Start 39.244 (u56). Kick 39.25 & 39.90 lyric entrance mid-pull.')
s('S38', 58, 60, 'CODE3D', '(那么灿烂)', 'The ring is revealed to be part of a colossal ✱ spark made of a MOSAIC of tiny frames from the whole film; continues to pull out until the spark is a small sun in a cream void.', 'CONTINUOUS PULL-OUT, exponential scale, 1.36 s; matches S37 motion vector.', 'CODE3D mosaic (§8.6 Mosaic): 600 tiles from stills extracted every 0.25 s of the finished S01–S37 render, masked by spark SVG; rotate slowly; bloom.', 'none', 'Settles 41.971 (u60).')
s('S39', 60, 62.545, 'CODE', '(outro, fade)', 'FINAL LOCKUP on warm cream paper: coral ✱ rotating once and settling; below it OPUS 5.5 (large serif) and 「第一天」 + small ANTHROPIC wordmark; a typed line 作品5.5号 · 诞生; cursor ▍ blinks at the end (callback to S01).', 'Slow 2 % push-in. Hold the last 12 frames perfectly still.', 'CODE only (SVG + Remotion). Wordmark from official asset, else Newsreader caps tracking +18 %.', 'OPUS 5.5 / 第一天 / ANTHROPIC / 作品5.5号 · 诞生', 'Settle on 41.971; title text lands 42.653 (u61); tagline typed 43.0–43.3; cursor blink at 43.1 & 43.45; audio ends 43.70.')
