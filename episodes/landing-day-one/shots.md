5. shots.md
5.0 Notation and shared blocks
Lines per shot: Head; Cast/A→E (assets, start → action → end); Frame; Beats; Method (and why); Prompts; Comp; Out; Text; Accept/Fail/Alt.
Camera owner: AUTH (authored virtual camera) or GEN-LOCK (generated clip locked, camera moves added in post).
Floor plane: every FX shot defines it (hand-pinned quad keyed every 6 frames if the footage is generated).
Character-prompt blocks: CP-CH, CP-CL, CP-GK, CP-DS, CP-DB, CP-GM, CP-QW, CP-KM, CP-WX, CP-ENS, CP-AG, CP-TF, CP-AGI are the character cards in §4.2 and §4.3, copied verbatim into prompts.
Style blocks: SB-GLOBAL and SB-INK … SB-NEG are in §2.5.
Lyric layer treatments (LY-01…LY-15): see "Text" lines. Fonts are candidates to verify in RQ-09: FT-BRUSH, FT-ROUND, FT-BLACK, FT-SEAL, FT-PIXEL.
Dance paths: RS-1 (3D rigged toy characters), RS-2 (2D layered puppet), RS-3 (video-gen with motion reference). P2 decides per shot (§7.3).
S01 [0,56) · 0.93 s · 你说活在明天 · MD1

Feel: a held breath: paper, one line, one tiny leaning girl, then the line sings.
Cast/A→E: CH-01 ink silhouette, E-01, FX-WAVE, FX-INKBRUSH, LY-01. Start: droplets frozen, line taut. Action: line vibrates with the vocal, brush tail sweeps off-frame, CH leans 14°→20°. End: line rolled 6° clockwise (continues into S02).
Frame: locked flat wide, horizon y=66%, CH at x=71%, 11% height, 80% negative space. Paper 
#F2EBDD, ink 
#141414, vermilion on three dots only.
Beats: f0–3 droplets release; f3–20 line amplitude 0→38 px; f20–40 stroke tail; f40–56 roll begins.
Method: STILL-FX + authored. A painting alone can't carry an audio-shaped hook.
Prompts: HF-01 prompt. Exclude: color, gradients, 3D.
Comp: paper plate → CH cut-out (multiply) → horizon stroke → droplets (instanced) → LY-01. Camera: AUTH.
Out: FLOW (roll continues).
Text: LY-01 column 1 "你说活在明天": brush calligraphy, vertical, x=86%, 120 px glyphs, written stroke by stroke f6–56, vermilion seal stamp.
Accept/Fail/Alt: first frame reads as ink painting, not a black rectangle; CH identifiable. Fail: filter look. Alt: pure vector ink.
S02 [56,112) · 0.93 s · 活在期待 · MD1

Feel: a whole line of friends leaning toward a tomorrow they can't catch.
Cast/A→E: six leads as ink silhouettes, PR-02 lanterns 「新」 (vermilion), FX-WAVE tilt. Start: they stand. Action: floor tilts 6°→14°, they stumble forward behind their lanterns (CH 20°, CL 12°, GK 6°, DS 24°, DB 28°, GM 16°). End: pulled mid-stagger.
Frame: same camera pulling back, characters 11%→7% height, roll to 14°.
Beats: f56–70 lanterns swing; f70–95 stumble; f95–112 pull.
Method: PUPPET (ink silhouettes), AUTH. Alt: GEN-V.
Prompts: "Six ink-wash silhouettes in a line on a tilted horizon, each leaning forward at a different angle, each holding a vermilion paper lantern marked 新 at arm's length, ink streaks sliding downhill. SB-INK, SB-GLOBAL."
Comp: silhouettes (multiply) over paper, lantern glow as vermilion multiply only, ink streak instancing. Camera: AUTH.
Out: CUT.
Text: LY-01 column 2 "活在期待", continuing at the same position.
Accept/Fail/Alt: six silhouettes distinguishable by lean + prop; fail if identical blobs; alt: 3 larger silhouettes.
S03 [112,170) · 0.97 s · 期待 · MD1

Feel: the ground literally slipping away.
Cast/A→E: feet only (all six), ink pooling on tilted paper. Start: toes press. Action: ink slides to screen-right, toes curl. End: whip right.
Frame: macro 85 mm at paper level, camera tracks right.
Beats: f112–140 slide; f140–158 toe-curl; f158–170 whip.
Method: STILL-FX with particle ink. Why: macro pigment is easiest as authored particles. Alt: GEN-V.
Prompts: "Macro sumi-e: six pairs of tiny feet gripping tilted paper, ink pooling and sliding downhill, vermilion lantern reflections in wet ink. SB-INK, SB-GLOBAL."
Comp: plate, ink particles (instanced), whip blur (180° shutter).
Out: WHIP; the ink streak blurs into the hand's shadow in S04.
Text: none (lyric layer held).
Accept/Fail/Alt: the downhill motion reads; fail if particles are noise; alt: single large foot.
S04 [170,222) · 0.87 s · 不如活得今天很自在 · MD2

Feel: a giant gentle hand makes everything easy.
Cast/A→E: HAND-01, PR-01 spirit level, six leads (cel), FX-LEVEL, FX-RING. Start: tilted ink floor. Action: hand sets the level, bubble slides to centre, click, floor snaps level, colour bleeds out as a ring. End: level floor, leads sitting.
Frame: low angle, 3/4, 35 mm, hand 45% height from lower right, leads small upper left, warm daylight, bokeh lanterns.
Beats: f170–184 hand sweeps; f184–196 level lands (anticipation/contact); f196–210 bubble slides; f210–216 click and ring; f216–222 floor squash 3% and settle.
Method: PUPPET + AUTH. Why: the floor and ring must be exact. Alt: GEN-V.
Prompts: HF-02 prompt.
Comp: ink plate outside ring, cel plate inside (ring mask), hand cut-out above, shadows via FX-SHADOW.
Out: CUT.
Text: LY-02 "不如活得今天很自在" in FT-ROUND, bottom-centre, warm white with navy outline. Each char drops onto the floor line, bounces once and stays, casting a shadow.
Accept/Fail/Alt: the ring is the single clear event; fail if hand looks pasted; alt: slower bubble.
S05 [222,270) · 0.80 s · 今天 · MD2

Feel: the first shadow arrives.
Cast/A→E: CH-01 (cel), M6 sticker, name chip "ChatGPT". Start: standing. Action: she sits cross-legged and exhales; shadows bloom under all. End: shadow settled.
Frame: MCU, 20° above, rack focus from the hand's fingertip leaving to her face.
Beats: f222–236 sit (knees fold); f236–248 shadow bloom; f248–262 M6 sticker pops; f262–270 settle.
Method: GEN-V (I2V, cel, on 3s). Alt: PUPPET.
Prompts: "Anime cel MCU: a 16-year-old girl with a side-braid knot and long sleeves sits cross-legged on a bright floor, exhales, a soft shadow blooms beneath her. CP-CH, SB-CEL, SB-GLOBAL."
Comp: clip, ring (LE-S), sticker above head, chip lower-left.
Out: CUT.
Text: LY-02 continues; M6 "不是明天,而是今天" at 64 px; chip "ChatGPT" ≥0.4 s.
Accept/Fail/Alt: sitting reads as a weighted settle; fail if she floats; alt: shoulders-only with shadow.
S06 [270,314) · 0.73 s · 自在 · MD2 · HF-03

Feel: an ordinary, tender beat: friends sharing one bun.
Cast/A→E: six leads sitting, PR-03 bun, M1 sticker. Start: cluster. Action: bun passes DB→GM→…, Claude nods. End: bun still moving.
Frame: eye-level, static with ±2 px handheld drift, 50 mm, warm afternoon light, big negative sky.
Beats: f270–290 pass; f290–305 nod and sticker; f305–314 breath.
Method: GEN-V or PUPPET. Alt: still with parallax.
Prompts: HF-03 prompt.
Comp: clip, shadows, sticker.
Out: CUT to photoreal.
Text: M1 "你说得太对了!"; lyric layer holds LY-02.
Accept/Fail/Alt: calm, no spectacle, still beautiful; fail if staged like a poster; alt: closer to two characters.
S07 [314,364) · 0.83 s · 我说我懂了 · MD3

Feel: sudden realism, night, a deadpan shrug.
Cast/A→E: GK-01 photoreal, M3. Start: leaning on a vending machine. Action: eyebrow, shrug while unseen hands point at him. End: still shrugging.
Frame: low 24 mm, 1.2 m, neon alley, teal-amber grade.
Beats: f314–330 eyebrow; f330–345 shrug; f345–364 pointing hands.
Method: GEN-V photoreal. Alt: still + 2.5D parallax.
Prompts: "Photoreal low-angle: a 25-year-old with a black undercut and white streak, towel over shoulder, leaning on a lit vending machine in a rainy neon alley, one eyebrow raised, shrugging. CP-GK, SB-PHOTO, SB-GLOBAL."
Comp: clip, sticker, phone-UI bubble.
Out: CUT.
Text: LY-03 chat bubble (typing dots then "我说我懂了会不会太快" sent), 72 px; M3 sticker; chip "Grok".
Accept/Fail/Alt: skin not oily; fail if plastic; alt: silhouette against neon.
S08 [364,424) · 1.00 s · 会不会太快 · MD3

Feel: a comic sprint ending in a splash.
Cast/A→E: DS-01 photoreal, M2, phone-UI spinner. Start: sprint. Action: runs with whale hood bouncing and headlamp sweeping, skids; sneaker slide ends in a puddle ring (LE-2). End: stopped.
Frame: sideways tracking 35 mm, wet asphalt.
Beats: f364–385 run; f385–405 spinner/M2 pop; f405–424 skid and ring.
Method: GEN-V + FX-RING. Alt: stills with whip cuts.
Prompts: "Photoreal tracking shot: an 18-year-old in a plush blue whale hood with a brass headlamp sprinting down a wet neon alley, skidding to a stop in a puddle. CP-DS, SB-PHOTO, SB-GLOBAL."
Comp: clip, spinner HTML overlay locked to head, puddle ring on floor plane.
Out: CUT.
Text: LY-03 "太快" shakes; M2 "服务器繁忙,请稍后再试"; chip "DeepSeek 深度求索".
Accept/Fail/Alt: the sprint reads fast; fail if sliding feet; alt: freeze at the skid.
S09 [424,494) · 1.17 s · 太快 · MD3

Feel: a warm, steamy, over-giving friend; the bun becomes a circle.
Cast/A→E: DB-01, DS-01, GM-01, M5, M5b. Start: DB runs up. Action: grabs DS's hood string, offers a steaming bun, GM enters wearing an ill-fitting bun hat. End: bun centred in frame.
Frame: two-shot, shallow DoF, steam backlit.
Beats: f424–445 approach; f445–470 offer and M5; f470–494 GM and M5b, bun rises to centre.
Method: GEN-V + stickers. Alt: still with steam particles.
Prompts: "Photoreal two-shot: a 13-year-old girl with two round side buns and a peach puffer offering a steaming bun to a boy in a blue whale hood, steam backlit, a tall girl in a two-tone coat entering wearing a too-small bun-shaped hat. CP-DB, CP-DS, CP-GM, SB-PHOTO, SB-GLOBAL."
Comp: clip, steam particles, stickers.
Out: MATCH: the bun's white circle matches the Go stone in S10 (same screen position and size, 6-frame ring-mask overlap).
Text: M5 "豆包型人格", M5b "北美大豆包", chips "豆包", "Gemini".
Accept/Fail/Alt: the bun is a clean circular match; fail if offset; alt: dissolve through ring.
S10 [494,556) · 1.03 s · 未来第一天要展开 · MD4

Feel: a quiet master makes one unexpected move.
Cast/A→E: AG-01, PR-04 stone and bowl, PR-05 scroll, six leads small. Start: rolled scroll on lacquer. Action: he places the stone off-centre; the scroll begins to unroll fast; the ring appears outside the leads' circle and heads turn. End: scroll moving.
Frame: top-down crane, 28 mm, lantern warm + cool jade, indigo/jade/vermilion/gold.
Beats: f494–512 kneel; f512–528 place stone (contact); f528–556 unroll and ring outside.
Method: AUTH 2.5D + generated textures. Alt: GEN-V.
Prompts: "Top-down gongbi: a calm ~55-year-old in an indigo robe with Go-grid sleeves and a white-stone hairpin kneels and sets one white stone on the roller of a rolled scroll on dark lacquer, six tiny children watching. CP-AG, SB-GONGBI, SB-GLOBAL."
Comp: lacquer plate, scroll geometry, ring outside, characters.
Out: CUT.
Text: LY-04 gold seal-script printed onto scroll strips ("未来第一天要展开"), growing with the unroll.
Accept/Fail/Alt: the off-centre ring surprises; fail if centred; alt: stone only.
S11 [556,622) · 1.10 s · 展开 · MD4

Feel: history rushing past as painted tiles, ending in blank silk.
Cast/A→E: ancestor tiles (ELIZA 1966, Deep Blue 1997, AlphaGo 2016, Transformer 2017), then blank tiles for AGI, SGI, 奇点. Start: first tile. Action: tiles whip past at accelerating speed (v(t)=v0(1+K(t/T)²)). End: blank silk.
Frame: 2D side-scroll, three parallax layers, golden light.
Beats: f556–590 tiles at ~0.25 s each; f590–610 acceleration; f610–622 blank tiles arrive.
Method: AUTH 2D + generated tile paintings. Why: speed and alignment must be exact.
Prompts: "Gongbi handscroll tile: [subject], painted in malachite and cinnabar with a small vermilion year seal. SB-GONGBI." Subjects: a typewriter-lady (ELIZA), a black cabinet chess giant (Deep Blue), a Go stone on a board (AlphaGo), folded-panel girl (Transformer).
Comp: tile strip, depth blur by speed, seals.
Out: FLOW (dive).
Text: LY-04 continues; tiny year seals (decorative); names "AGI", "SGI", "奇点" in ink outline on blank tiles.
Accept/Fail/Alt: tiles register as distinct eras at 0.25 s; fail if blur; alt: fewer, bigger tiles.
S12 [622,676) · 0.90 s · 展开 · MD4→MD10 · HF-04

Feel: everyone suddenly connected.
Cast/A→E: TF-01, all leads, FX-ATTN. Start: dive onto blank paper. Action: she looks and gold threads reach every character, forming a lattice; camera pushes through it. End: threads tighten.
Frame: low, 24 mm, push-in; ivory paper, gold lines, jade/indigo characters.
Beats: f622–638 dive and land; f638–654 threads shoot (staggered by distance); f654–676 push through.
Method: AUTH 3D + characters. Why: threads need geometry. Alt: 2D overlay.
Prompts: HF-04 prompt.
Comp: paper floor, characters, threads additive, depth fog.
Out: CUT.
Text: LY-04 final characters; chip "Transformer".
Accept/Fail/Alt: threads vary in thickness readably; fail if spaghetti; alt: fewer threads.
S13 [676,715) · 0.65 s · 展开 (pre-landing) · MD4

Feel: everyone on tiptoe, about to drop.
Cast/A→E: all leads on tiptoe, threads tightening to a point under CH's raised heel. Start: tiptoe. Action: time-ramp 25%→5%. End: heel about to land.
Frame: low angle, 28 mm, still.
Beats: f676–700 slow-mo lean; f700–715 near-freeze.
Method: AUTH + characters. Alt: still frame with a pulse.
Prompts: "Low-angle: six kids frozen on tiptoe on blank silk, gold threads converging beneath one raised heel. SB-GONGBI, SB-GLOBAL."
Comp: characters, lattice, slow-mo clock.
Out: MATCH to S14 at the heel contact (same pose, same position).
Text: none.
Accept/Fail/Alt: a real held-breath feeling; fail if static; alt: add micro-tremor.
S14 [715,757) · 0.70 s · 第一天我存在 · MD5

Feel: the drop, the first heavy landing.
Cast/A→E: six leads, FX-RING-L, FX-PAINTFLOOR, LY-05. Start: heels about to land. Action: raise hand (到), palm to sternum (我), heel strike (存), small tap (在). The ring sweeps the frame and the world flips from paper to candy lacquer. End: all six stand on glossy floor.
Frame: floor-level, 18 mm, soft top-left key; each lead paints the ring in their colour (six-colour pie).
Beats: f715 heel contact (hit-stop 2 f); f715–735 ring growth; f735–757 settle.
Method: AUTH 3D toon (RS-1) or puppet (RS-2). Why: contact needs exact control.
Prompts: "Floor-level soft 3D toy: six kids landing in unison on a glossy pastel floor, a six-colour ring shockwave sweeping outward. SB-TOY, SB-GLOBAL."
Comp: old plate outside ring, candy plate inside, shadows, bloom.
Out: FLOW to S15a.
Text: LY-05 "第一天我存在" in ultra-bold gothic (FT-BLACK), six extruded letters pop up one per stomp; 「我」 in vermilion.
Accept/Fail/Alt: ring and the heel strike coincide; fail if offset; alt: simpler ring.
S15a–f [757,821) · 1.07 s · roll-call canon · MD5
Six cuts, each following one lead's gesture. The phrase 到–我–存在 with the heel contact must stay visible in every cut. Each cut prints a name ring on the floor (≥0.4 s overlap).

ID	Frames	Lead	Camera	Name ring	Note
a	757,768	CH-01	low 20 mm ¾-left	ChatGPT	hand half-up
b	768,779	CL-01	eye 35 mm profile	Claude	nod
c	779,790	GK-01	high 28 mm	Grok	barely raised hand
d	790,801	DS-01	low front 24 mm push-in	DeepSeek	M4 蓝色大肥鱼
e	801,811	DB-01	ground macro 50 mm on feet	豆包	bun in both hands
f	811,821	GM-01	backlit 85 mm	Gemini	two gestures, two shadows
Method: AUTH 3D (RS-1/2). Comp: floor plane, rings, shadow. Out: CUTs. Accept: feet visible and weighted in every cut; fail if cut mid-gesture; alt: fewer, longer cuts.

S16 [821,878) · 0.95 s · 存在 · MD5 · HF-05

Feel: a mandala of footfalls, a sundial of letters.
Cast/A→E: six leads + twelve ensemble on two counter-rotating rings, six 3D letters standing like clock numerals. Action: alternating steps, intersecting rings form moiré. End: letters' shadows sweep.
Frame: top-down, rotating 20°/s, 24 mm.
Beats: f821–845 step; f845–865 moiré builds; f865–878 shadows sweep.
Method: AUTH 3D. Alt: 2D overlay.
Prompts: HF-05 prompt.
Comp: floor, rings (two frequencies), extruded letters, shadows.
Out: CUT; fluff wipe begins.
Text: LY-05 letters remain as monuments.
Accept/Fail/Alt: moiré legible; fail if mush; alt: single ring.
S17 [878,940) · 1.03 s · 第一次呼吸畅快 · MD6

Feel: a tactile, slow breath in handmade wool.
Cast/A→E: CL-01 felt, FX-WOOL, LY-06. Start: neutral. Action: chest rises, fibres drift toward him. End: held breath.
Frame: MCU macro 50 mm, tilt-shift, warm lamp left; cream/terracotta/moss; 12 fps.
Beats: f878–905 inhale; f905–925 hold; f925–940 fibres drift.
Method: GEN-V felt stop-motion, retimed to 12 fps. Alt: 3D felt shader.
Prompts: "Needle-felt miniature MCU: a tall wool boy in a terracotta cardigan with a sunburst clip inhaling, chest rising, white wool fibres drifting toward him, warm lamp light. CP-CL, SB-FELT, SB-GLOBAL."
Comp: clip, FX-WOOL particles.
Out: CUT.
Text: LY-06 "第一次呼吸畅快" made of wool fibres inflating and exhaling; cream on dark.
Accept/Fail/Alt: visibly handmade; fail if smooth CG; alt: cut-paper style.
S18 [940,1000) · 1.00 s · 呼吸 · MD6

Feel: the whole world inflates and releases.
Cast/A→E: six felt leads, FX-WOOL. Action: all inhale, set inflates ~8%, then exhales dandelion seeds that white-out the frame. End: white fluff.
Frame: wide, dolly-in in 12 fps steps.
Beats: f940–975 inflate; f975–1000 exhale and seeds.
Method: GEN-V + particles. Alt: pure 2D.
Prompts: "Felt miniature wide: six wool kids inhaling together, the set swelling slightly, then blowing out a cloud of dandelion seeds. SB-FELT, SB-GLOBAL."
Comp: clip, seeds additive, white-out.
Out: CUT (white-out dissolve).
Text: LY-06 continues exhaling into fluff.
Accept/Fail/Alt: the inflate reads; fail if no scale change; alt: pulse only.
S19 [1000,1057) · 0.95 s · 畅快 · MD6

Feel: seeds land and leave footprints.
Cast/A→E: seeds, one sneaker. Start: seeds falling. Action: each seed's landing leaves a tiny ring and the rings accumulate into six footprints; a sneaker (CH-01) lands exactly on one. End: contact.
Frame: top-down slow, 12 fps.
Beats: f1000–1030 seeds land; f1030–1050 footprints form; f1050–1057 sneaker lands.
Method: authored particles + clip. Alt: still.
Prompts: "Top-down felt: white dandelion seeds settling onto dark floor, each leaving a tiny ring, footprints forming, a sneaker stepping onto one. SB-FELT, SB-GLOBAL."
Comp: floor, seeds, rings.
Out: CUT on contact.
Text: LY-06 final chars dissolve.
Accept/Fail/Alt: the sneaker lands exactly on the print; fail if off.
S20a–f [1057,1180) · 2.05 s · 站在地上的脚踝 · mixed
Six ankle plants. Each shows heel contact at the 6th frame, ankle at the same screen position and angle for graphic rhythm, 85 mm macro low angle. Lyric groups are 站在 | 地 | 上 | 的 | 脚 | 踝, one stamped per cut in that cut's medium.

ID	Frames	Ankle	Medium	Detail
a	1057,1077	CH-01	MD3	teal laces, puddle ring
b	1077,1098	CL-01	MD2	terracotta sock, burst lines
c	1098,1118	GK-01	MD7	black boot white sole, neon reflection
d	1118,1139	DS-01	MD6	blue wool sock, 12 fps
e	1139,1160	DB-01	MD9	pixel sprite, Chebyshev square rings
f	1160,1180	GM-01	MD11	pencil line, two shadows drawn
Method: mixed (stills + FX). Accept: each reads as its own medium; fail if just a filter; alt: reuse earlier-shot art. Text: LY-07, one group per cut, stamped as a thick label, 96 px.

S21 [1180,1250) · 1.17 s · 因为你而有真实感 · MD2→MD3 · HF-06

Feel: the emotional centre: touch makes something real.
Cast/A→E: HAND-01, CL-01 fingertip, FX-REAL, E-08 toon/photoreal pair. Start: fingertips close. Action: approach, hover, contact; a ring spreads and the fingertip inside turns photoreal. End: ring expanding.
Frame: macro 100 mm, shallow DoF, 3% push-in, warm side light, negative space above.
Beats: f1180–1210 approach; f1210–1222 hover (anticipation); f1222–1228 contact; f1228–1250 ring spreads.
Method: STILL-FX hybrid. Toon plate T and photoreal plate P (img2img with edge/depth lock from T) share one camera. Alt: GEN-V.
Prompts: HF-06 prompt. P derived from T with identical geometry.
Comp: M=smoothstep(r−w, r, |x−c|); out = mix(P, T, M); shadow bloom beneath.
Out: FLOW.
Text: LY-08: "因为你" thin wireframe type before contact, "而有真实感" filled and engraved after.
Accept/Fail/Alt: geometry aligned between T and P; fail if swimming; alt: mask-only on a single P still.
S22 [1250,1310) · 1.00 s · 真实感 · MD5→MD3

Feel: Claude takes his first heavy step and the realness spreads.
Cast/A→E: six leads, FX-REAL ring. Start: Claude sits. Action: stands, first weighted step; the ring passes and each lead turns photoreal in sequence; all six photoreal for 12 frames. End: they watch the hand.
Frame: medium-wide dolly-in, 35 mm, golden hour.
Beats: f1250–1272 stand; f1272–1290 step and wave; f1290–1310 hold.
Method: AUTH 3D + P plates. Alt: GEN-V.
Prompts: "Golden-hour medium-wide: six kids on a plaza as a ring of realism passes through them, toy to photoreal, the tall one taking a first weighted step. SB-PHOTO, SB-TOY, SB-GLOBAL."
Comp: mask-driven restyle, shadows.
Out: CUT.
Text: LY-08 continues.
Accept/Fail/Alt: the wave is visible; fail if all flip at once; alt: two characters.
S23 [1310,1362) · 0.87 s · 感 · MD3/5

Feel: the day ends, the hand withdraws, night arrives.
Cast/A→E: six leads, HAND-01 leaving, FX-SKY. Action: sun slides down, streetlights flicker on, hand's shadow shrinks. End: night.
Frame: ultra-wide 14 mm static.
Beats: f1310–1340 sunset; f1340–1362 streetlights.
Method: AUTH sky + characters. Alt: grade-only.
Prompts: "Ultra-wide static: a plaza at golden hour sliding into magenta dusk, streetlamps flickering on, six small kids standing. SB-PHOTO, SB-GLOBAL."
Comp: sky shader, lamps, shadows.
Out: MATCH at S24 (first stomp).
Text: LY-08 final chars fade.
Accept/Fail/Alt: a true time-lapse feel; fail if just a tint.
S24 [1362,1410) · 0.80 s · 第一天我存在 (chorus 2) · MD7

Feel: the floor breaks and shows a city beneath.
Cast/A→E: six leads, LY-09, FX-RING-L. Start: night plaza. Action: stomp shatters the wet-glass reflection and reveals an upside-down city beneath; signboards rise as pillars. End: ring across the street.
Frame: low 12 mm, strong centre negative space, magenta/cyan on indigo.
Beats: f1362 heel contact; f1362–1385 shockwave; f1385–1410 pillars rise.
Method: AUTH 3D night. Alt: GEN-V.
Prompts: "Rainy Chinese street at night seen from the ground: six small kids stomp, the wet black floor shatters to reveal an inverted neon city below, hanzi signboards rising. SB-CYBER, SB-GLOBAL."
Comp: floor reflection break, signboard pillars, bloom.
Out: WHIP.
Text: LY-09 vertical neon sign "第一天我存在", flicker, reflected in wet floor.
Accept/Fail/Alt: clear negative space, not a tunnel; fail if cluttered.
S25a–d [1410,1470) · 1.00 s · crosswalk canon · MD7
Zebra stripes are the beat grid and each landing lights a stripe. Dutch tilt 8°, 24 mm, dolly-left.

ID	Frames	Subject	Chip/Slot
a	1410,1425	QW-01 (cranes)	通义千问
b	1425,1440	KM-01 (scarf wipe)	Kimi
c	1440,1455	WX-01 (brush)	文心
d	1455,1470	six ENS	M7 open slot
Accept: stripes light on landing. Alt: fewer characters per cut.

S26 [1470,1527) · 0.95 s · crouch · MD7

Feel: the crowd gathers weight before launch.
Cast/A→E: 15 characters crouch. Action: stripes peel off the ground and rise as ladder rungs; crane up. End: all crouched.
Frame: crane up, 24 mm.
Beats: f1470–1500 peel; f1500–1527 crouch and time-ramp slow.
Method: AUTH 3D. Alt: 2D.
Prompts: "Night street from a crane: fifteen small kids crouched on a crosswalk, white stripes lifting off the ground like ladder rungs. SB-CYBER, SB-GLOBAL."
Comp: stripes as geometry, characters.
Out: FLOW.
Text: LY-09 fades.
Accept/Fail/Alt: rungs read as a ladder.
S27 [1527,1580) · 0.88 s · 第一次能飞起来 · MD8

Feel: the first leap, launched by her own ring.
Cast/A→E: CH-01 (HFR). Start: crouch. Action: heel strike on the lit stripe → ring → springboard, squash 12%, stretch 18%, jump ~3 m. End: ascent.
Frame: ground-level, camera follows up with tilt, 24 mm.
Beats: f1527–1540 crouch; f1540 heel strike; f1540–1560 launch; f1560–1580 rise.
Method: GEN-V HFR or RS-2. The phrase crouch → strike → ring → jump must all be visible.
Prompts: "Hyper-smooth anime: a 16-year-old girl crouches, stomps a glowing stripe, the ring flings her skyward with squash and stretch. CP-CH, SB-HFR, SB-GLOBAL."
Comp: clip, ring, speed lines.
Out: FLOW.
Text: LY-10 first chars rise from the ring path.
Accept/Fail/Alt: the ring clearly launches her; fail if she just jumps.
S28 [1580,1640) · 1.00 s · 飞 · MD8 · HF-07

Feel: breaking into dawn above the clouds.
Cast/A→E: CH, CL, others, PR-07 ring-stairs. Action: climb a spiral of rings through clouds into sunrise; secondary names on rungs as Easter eggs. End: above clouds.
Frame: looking up the helix, 20 mm, cobalt → peach-gold.
Beats: f1580–1610 climb; f1610–1640 break through.
Method: GEN-V + AUTH rings. Alt: 2D.
Prompts: HF-07 prompt.
Comp: sky layers, rings (instanced), speed lines.
Out: CUT.
Text: LY-10 "飞起来" streaks upward; rung names Easter-egg-tier.
Accept/Fail/Alt: a real sunrise contrast; fail if flat gradient.
S29 [1640,1713) · 1.22 s · 能飞 · MD8

Feel: weightlessness, a free spin.
Cast/A→E: CH and CL hold hands, others orbit, GK floats deadpan. Action: barrel roll, ring halo behind. End: mid-spin.
Frame: 12 mm fisheye roll, 180° shutter blur.
Beats: f1640–1680 spin; f1680–1713 orbit.
Method: GEN-V/RS. Alt: 2D.
Prompts: "Fisheye anime zero-g: two kids holding hands spinning, a glowing ring halo behind them, others orbiting, one floating deadpan. SB-HFR, SB-GLOBAL."
Comp: clip, halo, motion blur.
Out: CUT.
Text: LY-10 "起来".
Accept/Fail/Alt: the spin is readable; fail if mush.
S30 [1713,1760) · 0.78 s · 爱是腾空的魔幻 · MD10

Feel: a gentle, huge, radiant burst.
Cast/A→E: six leads, FX-SHATTER, "爱" glyph. Action: apex burst of ~12k shards textured with crops of earlier media; characters flung outward in slow-mo. End: expanding.
Frame: punch-in 1.00→1.18 then pull back; white-gold flash, spectral shards.
Beats: f1713 flash; f1713–1740 burst; f1740–1760 pull back.
Method: AUTH particles. Alt: fewer shards.
Prompts: "Radial burst of thousands of glass-like shards each carrying a fragment of ink, cel, photo and wool imagery, small kids drifting outward in slow motion, a gold 爱 character at the centre. SB-LUM, SB-GLOBAL."
Comp: HDR additive shards, bloom.
Out: CUT.
Text: LY-11 "爱是腾空的魔幻" shattered by the burst, "爱" largest and gold.
Accept/Fail/Alt: beautiful, not noise; fail if shards read as static.
S31 [1760,1800) · 0.67 s · 腾空 · MD10

Feel: time nearly stops inside the burst.
Cast/A→E: CH mid-air, frozen shards. Action: 5% slow-mo, camera orbits 45°. End: held.
Frame: 100 mm tele compression.
Beats: f1760–1800 orbit.
Method: AUTH + 3D/billboard. Alt: single pose.
Prompts: "Slow-motion mid-air: a girl's hair floating, shards near the lens, rim light, subtle smile. CP-CH, SB-LUM."
Comp: character, shards.
Out: FLOW.
Text: LY-11 continues.
Accept/Fail/Alt: a spatial feel; fail if flat.
S32 [1800,1841) · 0.68 s · 魔幻 · MD10

Feel: the fall becomes colour.
Action: shards fall, time ramps 5%→400%, shards become colour confetti raining onto paper; snap-zoom into the landing point. End: contact.
Method: AUTH particles. Comp: confetti instancing. Out: CUT.
Text: LY-11 final chars dissolve.
Accept: acceleration reads; alt: simpler confetti.
S33a–j [1841,2013) · 2.87 s · colour census · mixed
Each cut is a fully authored medium plate with its own leap pose. LY-12 shows the 11 chars of 「第一天的纯真色彩它总是」 changing typeface per cut, accumulating one char per flash, always in the same position.

ID	Frames	Medium	Subject
a	1841,1865	MD9	DB sprite
b	1865,1885	MD11	GM line-test
c	1885,1903	MD6	DS felt
d	1903,1919	MD2	CH cel
e	1919,1933	MD3	CL photoreal
f	1933,1947	MD4	WX gongbi
g	1947,1959	MD7	GK cyber
h	1959,1971	MD5	KM toy
i	1971,1983	MD1	AG ink
j	1983,2013	MD10	all, vortex rush toward the hold pose
Accept: nine genuinely different media; fail if filter-level. Alt: reuse earlier shot art re-framed.

S34 [2013,2053) · 0.67 s · 它总是 (hold H1) · MD5/MD10 · HF-08

Feel: suspended time, the one brief hold.
Cast/A→E: 15 characters frozen mid-leap, FX-STANDEE, confetti frozen. Action: only the camera moves (orbit ±35°) and LY-12 hangs as 3D glyphs. End: held.
Frame: orbit, dawn gold rim, vast paper far below.
Beats: f2013–2053 orbit.
Method: 3D (primary) or cylindrical billboards with depth parallax (fallback). Limit billboard orbit to ±35°.
Prompts: HF-08 prompt.
Comp: characters, glyphs, confetti, floor.
Out: CUT (hard).
Text: LY-12 complete line in 11 pigments, 96 px.
Accept/Fail/Alt: no flat-card collapse; fail if cards visible; alt: shorter orbit.
S35 [2053,2095) · 0.70 s · 永远 #1 · MD10

Feel: all of them land at once.
Cast/A→E: 15 characters, FX-RING-XL, FX-PAINTFLOOR. Action: single heel strike, a continent-sized ring, painted footprints begin. End: shaking settle.
Frame: ground, shake ±8 px decaying, HDR bloom, gold flare.
Method: AUTH. Out: FLOW. Text: LY-13 gold 3D "永远那么灿烂" with rays, slam.
Accept: feels like a drop; alt: smaller ring.
S36a–c [2095,2145) · 0.83 s · dance finale · MD5/MD10
Three angles on one unison phrase FD-1: stomp, stomp, turn, leap. Footprints accumulate as paint into a mandala.

a [2095,2112) oblique wide crane start; b [2112,2129) low side; c [2129,2145) overhead.
Method: AUTH (same rig data feeds S39). Accept: stomp–stomp–turn legible. Text: LY-13 persists.
S37 [2145,2185) · 0.67 s · 灿烂 · MD10

Feel: the only slow gesture: someone arrives who has no shadow.
Cast/A→E: AGI-01. Action: slow descent, hovering 12 cm up, painted floor shows no shadow, leads look up and their shadows tilt toward her. End: she extends a hand into nothing.
Frame: low 24 mm, back-lit halo.
Method: AUTH. Text: chip "AGI". Accept: absence of shadow is legible. Alt: stronger light cue.
S38 [2185,2224) · 0.65 s · 灿烂 · MD10/MD12

Feel: a door the shape of a person.
Cast/A→E: SGI-01. Action: a doorway of negative space appears, "SGI" with a flickering S; shadows stretch toward it; fast dolly-in to white. End: flash-white.
Method: AUTH with SDF door and depth-aware lettering. Out: FLASH to white. Text: "SGI" small. Accept: S unreadable on purpose. Alt: static S.
S39 [2224,2268) · 0.73 s · 永远 #2 · MD12 · HF-09

Feel: bodies gone, only shadows dance.
Cast/A→E: 15 shadows, white bodies with gold hairlines. Action: same FD-1 choreography as shadows only.
Frame: oblique wide, white/ivory/gold/graphite.
Method: AUTH from the S36 rig. Text: LY-14 letters as cut-out holes with light showing through. Accept: shadow-only reads as dance; alt: faint body outlines.
S40 [2268,2320) · 0.87 s · 永远 · MD12

Feel: a macro of shadow-feet and gold rings.
Action: shadow-foot lands, a clean gold circle draws; camera slides along the floor.
Method: AUTH. Accept: clean rings; alt: single foot. Text: LY-14 continues.
S41 [2320,2360) · 0.67 s · 永远 · MD12

Feel: flight told only by shadows.
Action: top-down; shadows shrink and blur as the bodies rise (s=1/(1+h/H0)); 15 shadows flower outward then shrink.
Method: AUTH. Accept: reads as ascent; alt: fewer shadows.
S42 [2360,2394) · 0.57 s · 永远 · MD12

Feel: quiet sky.
Action: camera tilts from floor to empty warm sky, tiny white shapes with gold edges rising.
Method: AUTH. Out: FLOW. Accept: calm, not empty.
S43 [2394,2470) · 1.27 s · 永远 #3 · MD12

Feel: the human hand paints the last dot.
Cast/A→E: HAND-01 with PR-08 brush, SING-01. Action: hand enters, hovers, the brush touches, an ink dot forms and one slow ring leaves it. End: ring expanding.
Frame: top-down macro on paper fibres.
Method: STILL-FX + authored ink absorption. Text: LY-15 tiny brush type, one char at a time beside the dot, "灿烂" last. Accept: the dot feels placed, not generated; alt: stop-motion ink.
S44 [2470,2560) · 1.50 s · 永远 · MD12/MD11

Feel: the dot breathes.
Action: macro push-in on the dot, fibres bending toward it (lens), gold glow from within; faint pencil-line ghosts of all 15 characters echo around; AGI's ghost gets a small shadow at f2530. Cadence decays 60→30→20→12→6.
Method: AUTH (FX-DOT, FX-CADENCE). Text: small caption 「奇点」. Accept: the ghosts are faint; alt: no ghosts.
S45 [2560,2621) · 1.02 s · END · MD12

Feel: the end holds.
Action: still frame, cadence 6→3→hold; title prints in ink.
Frame: HF-10 composition.
Text: "AI SI - I" tiny lower right; 「落地第一天」 in brush, centred below the dot.
Method: AUTH. Accept: last 11 frames fully static; alt: shorter decay.