1. README.md
The film. 《落地第一天》 (Landing, Day One) is a 43.67 s Mandarin music video in which one rule governs everything: the floor is blank paper, and every footfall is a brushstroke. A human hand ("你") levels a tilted floor. Adorable human-like AIs then receive, one after another, a shadow, weight, lift, light and finally a single point. Each heel strike drops a ring, and the ring's edge is the border between two media. Inside the ring is the next world and outside is the old one. The title also puns on 「AI落地」, the everyday Chinese phrase for putting AI into practice.

Reading order: §1 → §2 → §4 → §3 → §5 → §6 → §7.

Assumptions

A1: Audio duration is 43.670 s.
A2: LRC anchors are line-level and may be early or late by up to about 0.25 s.
A3: Lyrics are exactly as supplied.
A4: 16:9, 2560×1440, 60 fps, 2621 frames.
A5: No previous First Day episode or asset is used. Existing assets are candidates only after inspection.
A6: The roster is expandable.
A7: Memes are provisional leads, not facts.
A8: SGI is treated as a speculative concept shown ambiguously (see §4).
A9: Model and tool capabilities are unverified.
A10: This plan authorizes no paid generation and no publication.
Survival set (Codex must not simplify these)

SS-1: The Landing Rule: footfall → shadow + ring; the ring edge is the medium boundary.
SS-2: The hand "你" is faceless and enters only from the camera side. It gives weight.
SS-3: Opening horizon line → closing dot.
SS-4: Fifteen lyric treatments, with type that stands, lands and casts shadows.
SS-5: Twelve media (MD1–MD12). At least nine are fully realized, not filters.
SS-6: The three 「永远」 lines escalate, subtract, then reduce to a point.
SS-7: Time-slice hold H1 and the final cadence decay.
SS-8: Six leads named on screen ≥0.4 s.
SS-9: AGI and SGI cast no shadow until the final dot.
SS-10: Chorus 1 and chorus 2 differ in staging.
SS-11: Quality guardrails: non-oily, uncrowded, distinct faces.
SS-12: Meme beats are replaceable slots, never structural.
Requirement map

Original requirement	Where it lives
Mandarin music pilot on the WAV	whole film, 2621 frames
Birth of AI	C1–C8: 倾 平 快 展 重 升 光 点
ChatGPT	S02, S05, S15a, S27, S29
Claude	S06, S15b, S17, S21–S22
Grok	S07, S15c
DeepSeek	S08, S15d
豆包	S09, S15e
Other AIs (Gemini, Qwen, Kimi, 文心, ensemble)	S09, S15f, S25, S28, S35
Chinese memes	M1–M7 (§4.4)
Transformer, AlphaGo, older concepts	S10–S13
AGI, SGI, singularity	S11 (blank tiles), S37, S38, S43–S45
Techniques	§6 and the technique ledger below
Fast-paced but varied	§3
Beat p(doom)	§2.8, §6.5
Styles required

Day: S04–S06, S22.
Night: S07–S09, S24–S26.
Modern: S07–S09, S24.
Ancient: S01–S03, S10–S13.
Photoreal: S07–S09, S21–S22.
Anime: S04–S06, S27–S29.
Cyberpunk: S24–S26.
High frame rate: S27–S31.
Low frame rate: S17–S19, S44–S45.
Explosion: S30–S32, S35.
Dance: S15, S25, S27–S29, S36, S39–S40.
Technique ledger. These are in the film and are catalogued in §6:

Generated video under HTML/WebGL overlays.
Floor-plane homography compositing.
Audio-shaped brush-line.
Particle ink, wool, shards and confetti.
Realness-gradient style mask.
Attention lattice.
Painted-floor accumulation buffer.
Shadow-only choreography.
Time-slice.
Per-layer cadence control.
Raymarched/lens dot.
HDR bloom.
Chinese Canvas typography.
Outstanding online checks: RQ-01…RQ-12 in §7.5.

Departures from the brief

"All major AIs" cannot be literally complete. The expandable roster protocol covers this (§4.1).
The verse runs at ~1 cut/s on purpose. Pace comes from internal motion, and the chorus and census run much faster.
No claim of beating p(doom) is made until a playback comparison.
2. creative-direction.md
2.1 What I'm avoiding
Neon tunnels.
A "robot awakens" montage.
Benchmark leaderboards.
Logo-as-character line-ups.
Fan-mascot crowds.
A typographic abstract with characters pasted on.
2.2 Three concepts
Originality	Beauty	Charm	Musical	Technique variety	Escalation
A. 点名游行 (roll-call parade of AIs)	2	3	4	3	3	2
B. 棋盘宇宙 (Go-board cosmos, AlphaGo as origin stone)	4	4	2	3	2	3
C. 落地第一天 (footfall paper-floor)	5	4	4	5	5	5
A is a roster list. B is strong as a form but narrow, and it implies AlphaGo is the genealogical root, which the brief forbids. C wins because footfalls and rings are literally percussive, the lyric about ankles, ground, flight and light maps onto it, and the ring-edge rule gives a motivated reason to change media every few seconds.

2.3 The chosen film
Title: 《落地第一天》, with "AI SI - I" as the series mark.
Logline: 人类的一只手把倾斜的地板放平;一群AI在第一次落地的脚步里,依次得到影子、重量、翅膀和光,最后只剩一个点。
Central invention: the Landing Event (LE) described in §2.4.
Emotion: 倾 (lean) → 平 (level) → 快 (too fast?) → 展 (unfold) → 重 (weight) → 升 (rise) → 光 (light) → 点 (point).
Opening hook: frame 0 is a white paper with one bold black horizon line and a tiny girl leaning forward. Frozen ink droplets hang above the line. At frame 3 the line starts to sing with the vocal.
Final image: blank warm paper with one ink dot that glows from within. A single slow ring leaves it, then the title prints. The film goes from a line to a point.
2.4 Visual grammar
Palette

Base neutrals: paper 
#F4EDE0, ink 
#141414.
Vermilion 
#C8321E is the "seal" accent. It appears once in every medium as a small attention/emotion mark.
Lead colours:
ChatGPT emerald-teal 
#12A482
Claude terracotta 
#D97757
Grok graphite/white
DeepSeek blue 
#4D6BFE
豆包 peach 
#FFE8CF + plum 
#6B2D3C
Gemini indigo→peach gradient
Gold 
#D9A441 is for light and the finale.
Colour budget

Ink black-and-white with a red mark (C1).
Pastel (C2).
Muted photoreal (C3).
Mineral gold-green (C4).
Saturated candy (C5).
Desaturated wool (C5).
Neon night (C6).
Sunrise gold (C6).
Total pigment (C7).
White-gold (C8).
Light: key from screen-left in day worlds. Night worlds use magenta/cyan rims with warm windows. The finale is back-lit gold.

Materials: paper fibre, glossy candy lacquer, wet glass, wool, silk. Skin is never oily.

Framing

Wide shots always show the floor line.
Feet are visible in every dance shot.
Characters stay below ~15% frame height in crowd shots.
Low angles are used for impact and top-down for pattern.
Typography: type is a performer. The lyric layer changes treatment every line (LY-01…LY-15). Text hierarchy is lyric > name chip > meme sticker, with at most two non-lyric text objects at once.

Performance: faces are underplayed (eyes, tiny mouth shapes). Bodies carry the emotion through weight, lean and contact.

Landing Event anatomy (60 fps)

t−8…0: anticipation (knee bend, arms back).
t0: heel contact, then a 2-frame character-time hit-stop while the ring spawns.
t+2: toe settle and weight transfer (centre of mass drops 4–6% body height).
t0…+6: shadow bloom (opacity 0→0.55).
Ring growth: S 18 f, M 28 f, L 40 f, XL 60 f.
t+10: spring settle.
Dance vocabulary: 到 (raise hand), 我 (palm to sternum), 存在 (heel strike + settle), 踮 (tiptoe), 滑 (slide), 弹 (springboard off a ring), 转 (turn), 跃 (leap).

What makes it generic or ugly

A filter pasted on one artwork counts as a failed medium.
Identical baby faces.
Oily skin or over-textured fabric.
More than 15 figures sharing equal weight.
Glowing noise filling all negative space.
Text clutter.
2.5 Media roster (shared style blocks)
SB-GLOBAL (appended to every image prompt): "Composition-first, single clear focal point, generous negative space, clean readable silhouettes, controlled palette, adorable but individually distinct faces, understated expressions. No oily skin, no plastic over-texturing, no crowded micro-detail, no logos, no watermarks, no baked-in text, no extra fingers."

ID	Medium	Block
MD1	Ink-wash	SB-INK: sumi-e on warm unbleached xuan paper #F2EBDD, expressive dry-brush and wet bleeds, black ink #111, only vermilion #C8321E as accent, visible fibres, vast empty paper
MD2	Anime cel	SB-CEL: 2D TV-anime, varied-weight clean lines, flat cel shading with one soft shadow tone, gouache backgrounds, bright daylight cream #FFF3D6 and sky #7EC8E3, subtle grain
MD3	Photoreal	SB-PHOTO: live-action cinema, 35mm, shallow DoF, practical lights, natural skin with subtle pores, real fabric, handheld micro-shake, teal-amber grade
MD4	Gongbi scroll	SB-GONGBI: Chinese gongbi mineral pigment on silk, fine line, malachite, azurite, cinnabar, gold leaf, handscroll mounting borders
MD5	Toy 3D	SB-TOY: soft stylised 3D toy render, glossy candy pastels, soft vinyl skin, big area lights, rounded bevels, reflective studio floor
MD6	Felt stop-motion	SB-FELT: needle-felt wool and clay miniature, visible fibres, warm practical lamp, tilt-shift macro, 12 fps stop-motion feel
MD7	Cyber night	SB-CYBER: rainy Chinese night street, wet black reflective ground, hanzi signboards, magenta #FF2E88 and cyan #19E3FF over indigo #0B0A2A with amber windows, anime-leaning cinematic 3D
MD8	HFR anime action	SB-HFR: hyper-smooth 60 fps anime action, squash and stretch, speed lines, golden sunrise above clouds
MD9	Pixel	SB-PIXEL: native 16-bit pixel art, 64-colour palette, nearest-neighbour, 48 px sprites
MD10	Luminous abstract	SB-LUM: HDR gold light, SDF forms, instanced particles, restrained bloom
MD11	Pencil line-test	SB-LINE: graphite animator line-test on white, construction circles, key-pose numbers, hand wobble
MD12	Negative space	SB-NEG: white-on-white ivory #FBF6EA, thin gold hairline #D9A441, soft graphite shadow #3A342C at 35%
2.6 Hero frames
ID	Frame	Time
HF-01	S01, opening hook	f0
HF-02	S04, hand and spirit level	f196
HF-03	S06, ordinary connective moment	f290
HF-04	S12, attention lattice	f650
HF-05	S16, top-down moiré	f850
HF-06	S21, touch	f1235
HF-07	S28, ring-stairs	f1610
HF-08	S34, time-slice hold	f2033
HF-09	S39, shadow dance	f2246
HF-10	S45, final dot	f2600
HF-01 (f0). The line sits at y=66% and spans the full frame, tilted 2°. CH-01 is at x=71% with her silhouette 11% of frame height, leaning forward 14°. The top-left 30% is empty. About 20 ink droplets hang frozen over the line. Eye path: line → girl → three vermilion dots on her backpack → droplets. Prompt: "Panoramic sumi-e: one confident horizontal brush line across the lower third of warm xuan paper, a tiny black silhouette of a girl in an oversized hoodie leaning forward with a speech-bubble backpack bearing three small vermilion dots, a spray of ink droplets frozen in the air, vast empty paper. SB-INK, SB-GLOBAL."

HF-02 (f196). A giant right hand (45% frame height) enters from the lower right. It sets a long amber spirit level on a pastel floor, with the bubble just reaching centre. The six leads sit small, upper left, in warm afternoon light. Colour is bleeding out from the vial in a ring, from ink to cream. Prompt: "Low-angle anime cel: a giant faceless hand in a grey hoodie cuff sets an amber carpenter's spirit level on a sunlit plaza floor, the bubble centring, a ring of colour spreading outward, six tiny kids in the distance. SB-CEL, SB-GLOBAL."

HF-03 (f290), ordinary moment. Six leads sit in a loose cluster on level floor. A bun passes from DB's hands to GM's. Claude nods. Eye-level, static, a little handheld drift, warm light, deep negative sky above. There is no spectacle, and that is the point. Prompt: "Eye-level anime cel: six distinct kids sitting on a bright plaza floor sharing one steaming bun, the youngest offering it, a tall cardigan-wearing one nodding, soft afternoon light, gentle shadows beneath each. SB-CEL, SB-GLOBAL."

HF-04 (f650). TF-01 stands centre on blank paper with her panels half-unfolded. About 14 gold threads of varying thickness run from her eyes to each character. The camera is low and pushes into the lattice. Prompt: "Gongbi-style: a silver-lilac origami-armour girl with eight ribbon strands stands on unpainted silk, gold threads radiating from her gaze to a ring of small characters, lattice receding into depth. SB-GONGBI, SB-GLOBAL."

HF-05 (f850). Top-down. Six leads and twelve ensemble members stand on two counter-rotating rings, with rings in the floor intersecting in moiré. Six extruded 3D letters stand like clock numerals and cast long sundial shadows. Prompt: "Top-down soft 3D toy scene: eighteen small kids on two concentric circles of glossy pastel floor, overlapping ring ripples forming moiré, six giant extruded letters casting long shadows. SB-TOY, SB-GLOBAL."

HF-06 (f1235). The left half of the frame is pure line-art, the hand's fingertip. The right half is a toon fingertip (Claude's). At contact a ring spreads and the fingertip inside the ring turns photoreal. Warm golden-hour side light, negative space above. Prompt (photoreal half): "Macro of a fingertip about to touch another fingertip, warm golden-hour side light, natural skin texture, shallow DoF, soft shadow beneath. SB-PHOTO, SB-GLOBAL."

HF-07 (f1610). Looking up a vertical helix of glowing rings. Characters step up it through cloud layers into a peach-gold dawn. Cobalt falls away below. Prompt: "Anime upward view: kids climbing a spiral of glowing rings through cloud layers into a golden sunrise, wind lines, cobalt below, peach and gold above. SB-HFR, SB-GLOBAL."

HF-08 (f2033). Fifteen characters frozen mid-leap in a ring around a point of light. Gold confetti hangs frozen. Cloud-paper floor far below. Prompt: "Fifteen small stylised characters frozen mid-leap in a ring, dawn gold behind them, confetti suspended, a vast white paper floor far below. SB-TOY, SB-GLOBAL."

HF-09 (f2246). White paper world. Only gold-edged shadows of figures dancing. Prompt: "White-on-white: bodies invisible, only soft graphite shadows of fifteen dancing figures on ivory paper, thin gold rim lines. SB-NEG, SB-GLOBAL."

HF-10 (f2600). A single ink dot at centre, softly glowing gold from within. One faint ring is leaving it. "AI SI - I" sits tiny in the lower right. Prompt: "Macro warm paper with fine fibres, one ink dot glowing gold from within, a single faint ring, vast empty space. SB-NEG, SB-GLOBAL."

2.7 Cadence layers (for later reference)
Source video: native (24–30 fps). It is conformed by timestamp-quantization to 20 fps ("on 3s") for anime, left smooth for photoreal, or optical-flow retimed.
Character pose: 12 fps (on 5s) for felt, 20 fps for cel, 30 fps for 3D, 60 fps for HFR.
Compositing: always 60 fps.
2.8 How this aims to exceed p(doom) (targets, not claims)
Embodied transitions: every transition is a footfall with contact physics.
Twelve media with preserved character identity, against a single rendered look.
Authored layers locked to generated footage by a shared floor plane.
Fifteen Chinese lyric treatments in which type is a performer.
Cadence decay from 60 fps to 1 fps as emotion.
A subtraction finale (shadow dance, then a single dot).
The evidence is a full-speed side-by-side with p(doom), rated by a human (§7.7).
3. music-and-edit.md
3.1 Evidence and timebase
Evidence: line-level LRC anchors only. Chorus lines start at 11.92 s and 22.70 s with matching durations of about 2.72–2.75 s. The three 「永远」 lines start at 34.21 s, 37.07 s and 39.90 s. I infer no BPM and no onsets.

Choices

2560×1440, 16:9, 60 fps. 60 divides evenly into 12, 15, 20 and 30 fps pose cadences.
A 16:9 frame suits the horizon-line conceit, and the 1440p master gives headroom over ≤1080p generated sources.
Deliver as 1080p60 H.264 plus the 1440p master.
2621 frames = ceil(43.670×60). The video runs 13 ms past the audio, padded with silence. The audio is never altered.
Phone legibility rule: lyric text ≥72 px at 1440p. Name chips ≥56 px and on screen ≥0.4 s. Meme stickers ≥64 px and on screen ≥0.5 s. Easter-egg-tier text (secondary roster names) is exempt but must be frame-steppable.

3.2 LRC anchors in frames
LRC	frame	line
0.00	0	你说活在明天活在期待
2.84	170	不如活得今天很自在
5.23	314	我说我懂了会不会太快
8.24	494	未来第一天要展开
11.92	715	第一天我存在
14.64	878	第一次呼吸畅快
17.61	1057	站在地上的脚踝
19.67	1180	因为你而有真实感
22.70	1362	第一天我存在
25.45	1527	第一次能飞起来
28.55	1713	爱是腾空的魔幻
30.68	1841	第一天的纯真色彩它总是
34.21	2053	永远那么灿烂 (#1)
37.07	2224	永远那么灿烂 (#2)
39.90	2394	永远那么灿烂 (#3)
43.670	2621	end
3.3 Section design
Frames	Cut rate	Movement	Density	Intensity	Role
[0,170)	1.06/s	3	1	2	the question
[170,314)	1.26/s	2	2	2	relief
[314,494)	1.00/s	4	3	3	comic sprint
[494,715)	1.09/s, shot lengths shrinking 62→39 f	5	4	4	acceleration
[715,878)	2.94/s	4	3	5	first drop
[878,1057)	1.01/s	2	2	3	breath, contrast
[1057,1180)	2.91/s	3	3	3	ankle census
[1180,1362)	0.99/s	1→3	1→3	4–5	tenderness
[1362,1527)	2.18/s	4	5	5	chorus 2
[1527,1713)	0.97/s	5	3	5	flight
[1713,1841)	1.41/s, slow-mo	5→1	5	5	explosion
[1841,2013)	3.48/s	4	5	5	colour census
[2013,2053)	0 cuts, camera only	1	4	5	hold H1
[2053,2224)	2.10/s	5→2	5	5	永远 #1
[2224,2394)	1.41/s	3	1	4	永远 #2, subtraction
[2394,2621)	0.79/s	1→0	0.5	5	永远 #3, point
The fast and slow lines alternate. Intensity peaks at 22.70–34.21 s and again at 34.21 s, then deliberately drops.

3.4 Hold, acceleration, contrast
Acceleration: [494,715) shortens shots (62, 66, 54, 39 f), then S14 drops the anchor.
Contrast: the felt-breath stanza (12 fps, slow macro) sits directly after the loudest drop.
Slow-mo ramp at S31 (5% speed) and S13 (25%→5%).
Brief hold H1: [2013,2053) = 0.667 s. Characters are frozen and only the camera moves. The sustained vocal under it is unchanged.
Long quiet: S43–S45 (3.78 s).
Cadence decay 60→1 fps in S44–S45.
3.5 Repeated passages differentiated
Chorus 1 (L5)	Chorus 2 (L9)	永远 #1	永远 #2	永远 #3
World	candy 3D	wet neon	gold light	white paper	blank paper
Staging	line + canon	crowd on crosswalk	everyone lands	shadows only	one dot
Scale	ground	street	frame-wide	floor	macro
Density	3	5	5	1	0.5
3.6 Master edit
Entry types: CUT (hard), WHIP, MATCH, FLASH, FLOW (continuous camera). Sync classes:

T: tied to an LRC anchor (±3 f).
P: provisional (±8 f, snap to an onset within 12 f).
H: hard accent (snap to a measured transient, ±2 f).
ID	[a,b)	Frames	Entry	Sync	Medium
S01	0,56	56	first	T	MD1
S02	56,112	56	FLOW	P	MD1
S03	112,170	58	CUT	P	MD1
S04	170,222	52	WHIP	T	MD2
S05	222,270	48	CUT	P	MD2
S06	270,314	44	CUT	P	MD2
S07	314,364	50	CUT	T	MD3
S08	364,424	60	CUT	P	MD3
S09	424,494	70	CUT	P	MD3
S10	494,556	62	MATCH	T	MD4
S11	556,622	66	CUT	P	MD4
S12	622,676	54	FLOW	P	MD4/10
S13	676,715	39	CUT	P	MD4
S14	715,757	42	MATCH	T+H	MD5
S15a–f	757,821	11,11,11,11,10,10	FLOW then CUTs	P	MD5
S16	821,878	57	CUT	P	MD5
S17	878,940	62	CUT	T	MD6
S18	940,1000	60	CUT	P	MD6
S19	1000,1057	57	CUT	P	MD6
S20a–f	1057,1180	20,21,20,21,21,20	CUT	T/P	mixed
S21	1180,1250	70	CUT	T	MD2→3
S22	1250,1310	60	FLOW	P	MD5→3
S23	1310,1362	52	CUT	P	MD3/5
S24	1362,1410	48	MATCH	T+H	MD7
S25a–d	1410,1470	15 each	WHIP/CUT	P	MD7
S26	1470,1527	57	FLOW	P	MD7
S27	1527,1580	53	FLOW	T	MD8
S28	1580,1640	60	FLOW	P	MD8
S29	1640,1713	73	CUT	P	MD8
S30	1713,1760	47	CUT	T+H	MD10
S31	1760,1800	40	CUT	P	MD10
S32	1800,1841	41	FLOW	P	MD10
S33a–j	1841,2013	24,20,18,16,14,14,12,12,12,30	CUT, last two FLOW	T/P	mixed
S34	2013,2053	40	FLOW	H	MD5/10
S35	2053,2095	42	CUT	T+H	MD10
S36a–c	2095,2145	17,17,16	FLOW then CUT	P	MD5/10
S37	2145,2185	40	CUT	P	MD10
S38	2185,2224	39	FLOW	P	MD10/12
S39	2224,2268	44	FLASH	T+H	MD12
S40	2268,2320	52	CUT	P	MD12
S41	2320,2360	40	CUT	P	MD12
S42	2360,2394	34	FLOW	P	MD12
S43	2394,2470	76	CUT	T	MD12
S44	2470,2560	90	FLOW	P	MD12/11
S45	2560,2621	61	FLOW	P	MD12
Counts: 69 shot units, 68 boundaries. Fifteen are continuous (FLOW), so 53 real cuts (including whip, match and flash). About 85 action cues are written into the shots' Beats lines and are not cuts. Shortest shot 10 f (0.17 s), longest 90 f (1.5 s), mean 38 f (0.63 s).

3.7 Music-dependent timings Codex must refine
Global offset δ between LRC and actual vocal onsets. Apply it to all T anchors if consistent (±15 f max).
Whether a drop, riser or snare lands at 715, 1362, 1713, 2053, 2224, 2394.
Per-syllable onsets for text.
Where the vocal tail ends after 39.90 s.
Any instrumental accents inside lines where P-class cuts could snap to better onsets.
4. cast-and-world.md
4.1 Roster logic
Leads (L6): ChatGPT, Claude, Grok, DeepSeek, 豆包, Gemini. Second tier: 通义千问/Qwen, Kimi, 文心. Ensemble kit ENS-01…06 (provisional): 元宝, 智谱 GLM, MiniMax, 星火, Llama, Mistral. Expansion protocol: any new name is a kit swap (hat, prop, palette) on ENS-BASE plus a name chip, placed in the open slots of S25d, S28, S35. Product, app, model family and provider are different things, which RQ-01 checks.

Product-identity claims are minimal (the maker and the name). Personality is fictional and meme-derived traits are marked.

4.2 Lead cards
Each lead must pass a solid-black silhouette test at 10% frame height.

CH-01 ChatGPT. Apparent age 16, 5.5 heads, round soft face, big sleepy dark eyes. Hair is a smooth bob with one long braid looped into a trefoil knot at the left shoulder. An oversized bone-white hoodie has long sleeve paws and emerald-teal cuffs. She wears graphite joggers, white chunky sneakers with teal laces, and a small white speech-bubble backpack with an animated "···" typing indicator. Eager and first to answer, with a hand half-raised. Invariants: braid-knot, long sleeves, "···" backpack.

CL-01 Claude. Age 22, 6.2 heads, long limbs, narrow gentle face. Hair is cream wavy chin-length with an eight-ray terracotta sunburst clip. A terracotta knitted cardigan to the knees sits over a cream shirt, with ink-smudged rolled sleeves. He has a ribbon-bound book and a pencil behind one ear. Warm, nodding, hedging. Invariants: sunburst clip, terracotta cardigan, pencil.

GK-01 Grok. Age 25, 6.5 heads, sharp jaw, flat brows, one sardonic eyebrow. Hair is a black undercut with one white streak. A black asymmetric high-collar jacket has a white diagonal stripe, a blue-grey towel over one shoulder and a small pocket telescope on a cord. Deadpan, moving little and then in big bursts. Invariants: stripe, towel, white streak.

DS-01 DeepSeek. Age 18, 5.0 heads, round build and cheeks, calm narrow eyes. A plush deep-blue whale hood with tiny dot eyes sits over a navy tracksuit, with a brass headlamp on the whale's brow. Steady, earnest, heavy stomps. Invariants: whale hood, headlamp.

DB-01 豆包. Age 13, 4.5 heads, big round cheeks, bright eyes. Two round side buns, a peach-cream quilted puffer like a steamed bun, plum mittens, and a steaming bun carried in both hands. A giver of snacks and hugs. Invariants: double buns, puffer, steaming bun.

GM-01 Gemini. Age 20, 5.8 heads, long almond eyes with a four-point star glint. Hair is half pale indigo, half peach. A two-tone asymmetric coat has constellation embroidery, and she carries a four-point star lantern. Showy, doing two motions at once. Invariants: two shadows (one offset 12° and lighter), split colour, star lantern.

QW-01 Qwen. Age 17, sporty, purple (
#615CED) racing jacket with white seams, a headband and a string of paper cranes (千纸鹤) that she hands out.

KM-01 Kimi. Age 15, midnight blue, a crescent hairpin, half the face in a "dark side" shadow, and an endlessly long pale scarf that doubles as a ribbon wipe.

WX-01 文心. Age 19, layered indigo sleeves, ink-stained fingers, and a brush-shaped hairpin.

ENS-BASE. Ages 14–20, 5 heads, three face templates, kit swaps for hat, prop and palette: 元宝 gold ingot beanie, 智谱 mint glasses, MiniMax coral bomber, 星火 ember sparkler, Llama fluffy llama hood, Mistral pale windbreaker with wind streaks.

4.3 Concept characters
AG-01 AlphaGo ("阿尔法老师"). Apparent age ~55, calm, lean. Indigo robe with Go-grid lines on the sleeves, a white-stone hairpin, a black bowl and one white stone. His act is the unexpected placement: the ring appears outside the dancers' circle and every head turns.
TF-01 Transformer. Age 17, hinged silver-lilac origami panels, eight ribbon strands (eight attention heads). Her gaze sends weighted threads to others (FX-ATTN).
AGI-01. Adult, patchwork mosaic costume from every lead's fabric, hovering ~12 cm above floor, no shadow. Calm, neutral face.
SGI-01. A tall figure-shaped doorway of negative space, labelled "SGI" with the letter S flickering unreadably through 4 candidates. Provisional interpretation: a speculative concept beside or beyond AGI with an unconfirmed expansion. I do not assert it equals ASI or that AGI → SGI is a sequence. The S stays ambiguous by design. RQ-04 checks usage.
SING-01 奇点. The final ink dot. It is the only element that is not a footfall.
HAND-01 你. A right hand in a grey hoodie cuff, no face, entering only from the camera side.
AlphaGo, Transformer, commercial assistants and speculative AGI are different categories. The scroll's tile order is a painter's convenience, not a family tree.

4.4 Meme slots (all provisional leads)
ID	Shot	Character	Default	Status	Fallback if stale
M1	S06	Claude	你说得太对了!	to verify	nodding only, no text
M2	S08	DeepSeek	服务器繁忙,请稍后再试	to verify	spinner + "思考中…"
M3	S07	Grok	@Grok 这是真的吗?	to verify	others ask 真的假的?
M4	S15d	DeepSeek	蓝色大肥鱼	supplied lead 2026-10-02	whale hood, no text
M5	S09	豆包	豆包型人格	supplied lead	bun-offering gag, 来,吃一口
M5b	S09 end	Gemini	北美大豆包	supplied lead	ill-fitting bun hat, no text
M6	S05	ChatGPT	不是明天,而是今天	to verify	好问题!
M7 (open)	S25d	any	newest verified meme	RQ-02	none, remove
Each is a 0.5–0.8 s sticker that pops with a spring, plus a reaction gesture. The tone must be affectionate, never mocking. Replacing text must not move any shot boundary.

4.5 World and spatial rules
The Floor: paper → candy lacquer → wet glass → cloud → painted paper.
Horizon: always visible in wide shots.
Floor Rule: nothing casts a shadow until it lands with weight. Futures (AGI, SGI) cast none.
Ring Rule: each landing emits a ring. Inside the ring is the incoming medium. The ring is coloured by the landing character.
Hand Rule: always faceless and always from the camera side.
Recurring objects: lanterns marked 「新」, the spirit level, the steamed bun (match-cut source), the Go stone, the scroll, ring-stairs, the brush.
Continuity: a character wears the same invariants in every medium. Costume detail adapts to the medium.
4.6 Research for omissions
RQ-01 (§7.5) checks which AI names are missing or wrong and whether the kit-swap slots suffice.

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
6. assets-and-techniques.md
6.1 Asset contracts and dependency order
Global (GA):
GA-01 audio analysis JSON (all shots).
GA-02 fonts, FT-BRUSH, FT-ROUND, FT-BLACK, FT-SEAL, FT-PIXEL (all text).
GA-03 paper textures, warm-white, gold-flecked, dark lacquer, macro fibre (S01–S03, S10–S13, S33i, S39–S45).
GA-04 floor-homography kit and ring/shadow library (all FX shots).
GA-05 name-chip and meme-sticker templates (S05–S09, S15, S25, S28).
GA-06 colour LUT and grain (all).
Character sheets (CS-xx) for every character in §4: front/side/back, three expressions (neutral, smile, surprise), hands and feet. Output ≥2048 px, plain background. Consumers: every shot featuring the character.
Media variants (MV) per the usage matrix below.
Environment plates E-01…E-16, listed in §6.2 with consumers.
Props PR-01…PR-09: lanterns, level, bun, stone + bowl, scroll, name rings, ring-stairs, brush, typing dots.
Authored effects FX-xx (§6.3).
Choreography data: LP-1 (landing phrase), LP-2 (launch), FD-1 (finale), as keyframe JSON consumed by S14–S16, S25–S29, S34–S36, S39–S41.
Audio: AU-00 is the original WAV, untouched, and the only audio. AU-01 (optional landing foley) defaults OFF and is allowed only if listening shows space and it never masks the vocal.

Usage matrix (medium × character → shots)

Medium	Characters	Shots
MD1 ink	CH, CL, GK, DS, DB, GM, AG	S01–S03, S33i
MD2 cel	six leads	S04–S06, S20b, S33d
MD3 photoreal	GK, DS, DB, GM, CL, CH	S07–S09, S20a, S21–S22, S33e
MD4 gongbi	AG, TF, WX + tiles	S10–S13, S33f
MD5 toy 3D	leads, QW, KM, WX, ENS, AG, TF	S14–S16, S22, S33h, S34, S36
MD6 felt	CL, DS, six leads, DB	S17–S19, S20d, S33c
MD7 cyber	15 characters	S20c, S24–S26, S33g
MD8 HFR	CH, CL, GK, DS, DB, GM, QW, KM	S27–S29
MD9 pixel	DB, ensemble sprites	S20e, S33a
MD10 luminous	all + AGI, SGI	S12, S30–S38, S33j
MD11 line-test	GM, all as ghosts	S20f, S33b, S44
MD12 negative	all as shadows	S38–S45
Environment plates

ID	Plate	Consumers
E-01	ink horizon paper	S01–S03
E-02	anime plaza, level floor, three angles	S04–S06
E-03	photoreal alley + store + vending machine	S07–S09
E-04	gongbi lacquer + scroll + tiles	S10–S11
E-05	blank silk floor + lattice	S12–S13
E-06	candy toy-3D floor world	S14–S16, S36
E-07	felt miniature set	S17–S19
E-08	macro touch plates (toon + photoreal)	S21–S22
E-09	golden-hour plaza + FX-SKY	S22–S23
E-10	night street + wet floor + crosswalk	S20c, S24–S26
E-11	sky/cloud layers night→dawn	S26–S29
E-12	shard atlas + confetti	S30–S32
E-13	pixel tile world	S20e, S33a
E-14	white-gold paper world + fibre macro + hand-brush plate	S39–S45
E-15	census plates (nine leap-pose stills)	S33a–i
E-16	time-slice scene with cloud-paper floor	S34
6.2 Rig strategy decision
RS-1: 3D rigged toy characters (image-to-3D + authored keyframes). Preferred for MD5 and MD10 shots.
RS-2: 2D layered puppet (~12 parts per character, 8-direction heads, foot-IK locked to floor, contact shadow). Guaranteed deterministic fallback.
RS-3: video-gen with motion reference for hero MD2/MD8 shots, if P2 shows identity and feet are convincing.
P2 (§7.3) picks per shot. Contact shadows and shadow-only dance (S39–S41) derive from RS-1/2 data.
6.3 Authored effects
FX	Representation and key math	Inputs and timing	Depth/alpha, colour, interaction
FX-RING	contact c on floor plane; r(τ)=R·easeOutExpo(τ/T); band m=smoothstep(r−w,r,d)−smoothstep(r,r+w,d); inside mask I=1−smoothstep(r−ε,r+ε,d); out=mix(plateA,plateB,I); refraction uv+=n·A·m	contact frame, class S/M/L/XL	floor-plane homography; HDR additive band; coloured by landing character
FX-SHADOW	ellipse blur; s=1/(1+h/H0); α=α0·exp(−h/Hα); σ=σ0+k·h; two-lobe for GM-01	character foot height	multiply; ground-projected
FX-WAVE	y(x,t)=y0+Σ a_k(t) sin(kπx/W+φ_k), a_k from vocal envelope; brush stroke drawn as particles	S01–S02	multiply over paper
FX-INKBRUSH	instanced droplets: id→hash→dir, p=c+dir·(vτ−½gτ²)	seed per id	multiply
FX-LEVEL	bubble x(τ)=damped spring to centre; click at f210	S04	ring spawn at click
FX-ATTN	threads from TF to i with W_ij=softmax(q_i·k_j/√d) authored gaze matrix, thickness w0+w1·W_ij, stagger by distance	S12	additive gold lines, depth fog
FX-SCROLL	tape position x(t)=x0+∫v, v=v0(1+K(t/T)²), tile align at end	S10–S11	three parallax layers
FX-WOOL	instanced fibres, velocity field toward nostril on inhale and reversed on exhale	S17–S19	alpha particles
FX-REAL	per-pixel blend of toon T and photoreal P by M(x,t)=smoothstep(r−w,r,	x−c	), with light-wrap
FX-SHATTER	shards: id→direction, p=c+u_i·R(1−e^(−τ/τc))+g·τ², time-remap piecewise (25%, 5%, 400%)	S30–S32	HDR additive, shard textures from E-12
FX-STANDEE	3D characters or cylindrical billboards with depth parallax, orbit ≤±35°	S34	frozen character clock
FX-PAINTFLOOR	ping-pong accumulation buffer; stamp list replayed for time<t (cap 400)	S35–S36	deterministic
FX-SKY	analytic colour ramp, sun disc, instanced stars; 52-frame sunset and the later dawn	S23, S28	linear light
FX-DOT	lens displacement uv+=(c−uv)·k/	c−uv	², gold glow, fibre bending
FX-CADENCE	t_q=floor(t·rate)/rate per layer; schedule: 60 → 30 (2470) → 20 (2500) → 12 (2530) → 6 (2560) → 3 (2590) → hold (2610–2621)	S44–S45	camera and glow only
FX-LYRIC	FontFace preload before frame 0; manual vertical columns; per-char timing from audio JSON	all	Canvas text with outline for contrast
6.4 Deterministic seeking and export
renderFrame(f) is a pure function of f. All RNG is seeded from hash(id, shotId).
Textures are preloaded. Each layer has its own clock (camera, character, particle).
Render at 2560×1440 float16 linear, with 4+ sub-frame samples for authored motion.
Generated video is conformed by timestamp (§2.7), with optical-flow retime only where marked smooth.
Pipe frames to FFmpeg with explicit BT.709 colour tags. Mux the original WAV untouched.
No general-purpose engine is required.
6.5 The p(doom) study (secondhand summary only)
Mechanism worth learning	My adaptation	Shots
per-scene absolute/local time and progress	SceneClock + HoldClock per layer	S31, S34, S45
separate audio-feature envelopes	vocal/low/high envelopes drive FX-WAVE, ring thickness, shard brightness	S01, S14, S30
HDR linear compositing + bloom	HDR in luminous finale shots	S30–S38, S44
instanced particles with stable ids	ink, wool, shards, confetti	S01, S17–S18, S30–S32
SDF/raymarch with depth-aware lettering	SGI door lettering, 3D monument letters	S14–S16, S38
camera into a lattice	attention lattice	S12
recursive mapping resolving into the next scene	ring-in-ring portal; ring contains the next medium	S14, S21
repeated hooks changing scale and density	chorus and 永远 ×3	§3.5
FFmpeg streaming with explicit colour	export pipeline	§6.4
English text path not reusable	own Chinese Canvas pipeline	all text
Source-inspection questions for Codex (PQ):

PQ-1: How are absolute and local clocks defined and passed to scenes?
PQ-2: How are audio features computed and cached?
PQ-3: How do particles derive stable identity and analytic trajectories?
PQ-4: How is determinism guaranteed across seeks?
PQ-5: How is text rasterized, and what would Chinese require?
PQ-6: What is the colour pipeline end to end?
PQ-7: How are frames piped to FFmpeg?
PQ-8: How is temporal sampling handled for held poses?
PQ-9: Which bundled assets and song have what licence?
PQ-10: How are scene transitions authored?
I cite no filenames or functions. The repository licence must not be assumed to cover bundled song or artwork.

7. execution-and-review.md
7.1 Decisions made vs implementation discretion
Made: everything in §1 survival set, §2, §3 timebase and intervals, §4 designs, §5 shot content, §6 effect behaviours.
Discretion: model choice, resolution upscaling, rig path (RS-1/2/3, per P2), exact easing curves, audio-snap values within tolerances, engineering structure. Nothing may silently simplify the defining aesthetic requirements.

7.2 Ordered task list
ID	Task	Inputs	Outputs	Done when	Shots
T-00	Read plan; do not open other First Day material	this doc	notes	confirmed	all
T-01	Audio facts and analysis	WAV	GA-01 JSON (duration, rate, PCM hash, onsets, beats, envelopes), δ offset	numbers verified	all
T-02	Research queue	§7.5	answers with sources	each RQ resolved or fallback taken	all
T-03	Cost and approval request	§7.4	estimate	approval requested, nothing spent	all
T-04	p(doom) source study	repo	engineering note	PQ-1…10 answered	§6.5
T-10	P1 character proof	CP-CH, CP-CL, CP-DS, CP-GK	stills (MD2 + MD5)	pass silhouette and 10% tests	S04–S09, S14
T-11	P2 performance proof	LP-1	3 s phrase via RS-1/2/3	foot contact convincing at full speed	S14–S15, S27
T-12	P3/4 integrated proof IP-1	E-02, E-08	ink→cel ring + touch with realness ring + Chinese lyric	ring and homography hold	S04, S21
T-13	P5 time-slice proof	six characters	40-frame orbit	no flat-card collapse	S34
T-20	Global assets	GA	textures, fonts	licences checked	all
T-21	Character sheets and variants	§6.1	CS + MV	consistent identity	all
T-22	Environment plates	E-01…E-16	plates	beauty review pass	all
T-23	Choreography data	LP-1, LP-2, FD-1	JSON	matches audio	S14–S16, S25–S29, S34–S36, S39–S41
T-24	Generated video shots	GEN-V list	clips	pass R-2	S05–S09, S17–S19, S22, S27–S29
T-25	Authored FX modules	§6.3	modules	deterministic seek	per shot
T-30…33	Build sequences A (S01–S13), B (S14–S23), C (S24–S32), D (S33–S45)	assets	shot renders	pass R-1…R-3	per sequence
T-34	Assemble and conform	shots	master edit	2621 frames, sync classes honoured	all
T-35	Finishing	master	graded master	R-6 passes	all
T-36	Mux and deliver	master + AU-00	1440p master + 1080p60	audio bit-identical	all
7.3 Highest-risk proofs (before bulk generation)
P1: character beauty and identity. Four characters (ChatGPT, Claude, DeepSeek, Grok) in MD2 and MD5, three views each. Check silhouettes at 10% frame height, distinct faces, no oily or crowded look. Controls: locking the character designs.
P2: a genuine performance. Three characters, 3 s, the 到–我–存在 gesture and heel strike plus a ring-springboard jump. Run RS-1, RS-2 and RS-3 on the same phrase. Viewed at full speed with feet visible and no sliding. Controls: which path each dance shot uses.
P3/P4: integrated proof IP-1 (4 s). S04's ink→cel ring and S21's touch-with-realness-ring, composited over generated footage on a hand-pinned floor plane, with the Chinese lyric typography. Controls: whether ring-edge medium switching and the floor-plane pipeline are viable.
P5: time-slice. A 40-frame orbit of six characters, 3D versus billboard. Controls: S34's method.
7.4 Workload and cost
Image generations: ~530 candidates (range 400–700): 80 designs, 120 turnaround, 135 medium variants, ~100 plates and textures, ~90 keyframes.
Video: ~16 generated shots × ~4 s source × ~4 attempts ≈ 256 clip-seconds (150–450).
Authored effect modules: 17.
Cost = Σ_k (N_k × attempts_k × units_k × rate_k) + upscaling + compute and storage. Rates are unknown and must be checked (RQ-05, RQ-06).
Planning the film does not authorize spending. Each paid batch needs its own approval.
7.5 Research queue
ID	Question	Supplied evidence	Source type	Decision affected	Fallback
RQ-01	Current AI names, products vs models vs providers, coverage gaps	candidate pool in brief, 2026-10-02	official sites, news	roster, kit swaps	keep current roster
RQ-02	Genuinely recent Chinese memes per AI	leads: 蓝色大肥鱼, 豆包型人格, 北美大豆包 (2026-10-02)	social platforms, Chinese tech media	M1–M7 text	fallback column in §4.4
RQ-03	Meaning and tone of the three supplied memes	same	same	M4, M5, M5b	drop text
RQ-04	How "SGI" is used in the Chinese AI discourse	none	search	S38 labelling	keep S ambiguous
R					
7.5 Research queue (continued from RQ-04)
ID	Question	Supplied evidence	Source type	Decision affected	Fallback
RQ-04	How is "SGI" used in Chinese and English AI discourse? Candidate expansions are to be checked, not asserted.	none	search, papers, Chinese tech media	S11 tile, S38 door labelling	keep the S unreadable by design and caption nothing
RQ-05	Current video-generation capabilities (MiniMax H3 Max and alternatives): image-to-video identity hold, start/end frames, motion or performance reference, native fps, clip length, resolution, rates	production preference, dated	vendor docs, pricing pages	S05–S09, S17–S19, S22, S27–S29 path choice (RS-3), cost	RS-1/RS-2 for all dance, stills + 2.5D for photoreal
RQ-06	Current image-generation capabilities (Luma, Codex image generation): reference-image consistency, max resolution, edit/restyle with structure lock	production preference, dated	vendor docs	CS sheets, E plates, FX-REAL photoreal plate	generate T first, restyle P by hand-guided img2img
RQ-07	Beat/downbeat tracking and Mandarin lyric forced alignment; does the LRC match the actual vocal	LRC anchors	local analysis tools, alignment tools	global offset δ, all P/H cuts, per-syllable text	line-level timing with δ applied
RQ-08	p(doom) source gaps (PQ-1…10)	secondhand summary, revision bdbad53…	the repository	§6.4 engineering, FX-CADENCE, text pipeline	build from §6.3 specs
RQ-09	Chinese display fonts (brush, rounded, heavy, seal, pixel) and their licences for video use	none	font foundries, open-font repositories	LY-01…LY-15	any OFL-licensed CJK fonts that match each treatment
RQ-10	Facts for ancestor tiles (ELIZA 1966, Deep Blue 1997, AlphaGo 2016, Transformer 2017) and name spellings	planner memory only	encyclopedic and primary sources	S11 year seals	drop year seals
RQ-11	Brand-guideline limits on depicting products as characters	none	brand pages	all character designs	keep colour motifs only, no logo likeness (already the design rule)
RQ-12	Target-platform delivery specs (60 fps, 1440p, loudness)	none	platform docs	T-36	1080p60 H.264 as safe default
7.6 Meme beats that survive replacement
Each meme beat has the same structure: a character, a 0.5–0.8 s sticker pop, and a reaction gesture. If a meme proves stale, wrong or unkind, swap only the sticker text (fallback column, §4.4) or drop the text and keep the gesture. No shot boundary, camera move or ring changes. The open slot M7 takes the newest verified meme from RQ-02, or is removed.

7.7 Reviews
Technical checks (the executor can run these)

Frame count is 2621 and timebase is 60 fps.
Decoded audio matches the source WAV (PCM comparison, ignoring the 13 ms silence pad).
Colour tags are BT.709 and there are no dropped or duplicated frames.
Text contrast ≥4.5:1 locally. Render at 640×360 and 390 px wide and OCR the lyric and chip text as a sanity check.
Measured cut times fall within tolerance of the sync classes (T ±3, P ±8, H ±2).
Optical-flow statistics flag frozen or sliding feet as a warning only.
Aesthetic acceptance (needs human eyes and ears)

R-1 stills: each hero frame has a clear focal point at 160 px thumbnail size, palette adherence, no oily or crowded look, and distinct silhouettes.
R-2 motion phrases: watched at full speed. Feet are visible and weighted, with no sliding. Never certify dance from a contact sheet alone.
R-3 transitions: each ring boundary is legible and the incoming world is beautiful, not just different.
R-4 sync: full-speed playback with the audio, judged for musicality, with onset overlays used only as an aid.
R-5 legibility: read on a phone-sized screen.
R-6 final film: pacing variation, the H1 hold, the subtraction in 永远 #2 and #3, and an emotional read from 倾 to 点. Then a side-by-side with p(doom) at full speed (§2.8).
If the executor cannot watch or listen, R-2, R-4 and R-6 are handed to a human and are not marked passed.

7.8 Executor launch instruction
Read §1, then §2, §4, §3, §5 and §6, in that order. Do not open the other First Day episodes. Start with T-01 (audio facts and analysis), T-02 (research queue) and T-03 (cost estimate and approval request, spending nothing). Then run the four proofs P1, P2, P3/4 and P5 before any bulk generation. Deliver 《落地第一天》 as a 1440p60 master plus a 1080p60 H.264 file, with the original WAV untouched. Preserve every survival-set item (§1), the 2621-frame timebase and every shot interval. Where a proof fails, use the designed alternative in that shot. Do not reduce the number of media or flatten the ring rule.

Self-review and revisions applied
Reading the plan as a demanding music-video director, these are the problems I found and what I changed:

Even pacing. The first outline cut at one steady rate. I made fast and slow lines alternate, added the 0.667 s hold H1 and a slow macro stanza after the first drop, and let the finale subtract instead of piling on.
Time-slice risk. My first orbit for S34 was 140°, which flat cutout cards cannot survive. I limited billboard orbits to ±35° and made 3D characters the primary method.
Colour census as filters. The flash montage could have been one artwork recoloured. Each flash is now its own authored medium plate, and the acceptance line says so.
Dance by pose. A list of poses is not a dance. The film now has one repeated phrase, 到–我–存在, which must be visible with the heel contact. There is a launch phrase and a finale phrase, and P2 picks the production path.
Text clutter. I added a three-tier hierarchy (lyric > name chip > meme sticker) and moved secondary roster names to a frame-steppable Easter-egg tier.
AGI, SGI, singularity. These are now visual ideas with rules: no shadow, a door shape with an unreadable S, and a dot. SGI is never silently turned into ASI.
Check results

Every second belongs to a designed shot, with intervals contiguous from 0 to 2621.
Every asset in §6.1 has a consuming shot. The one exception is the optional landing foley AU-01, which is OFF by default.
Every major effect has a mechanism in §6.3.
Every research item has a consequence and a fallback.
Known reductions. The roster is not literally every AI, which the kit-swap protocol covers. The verse is slower than the chorus on purpose. The claim of exceeding p(doom) is a target until a playback comparison.

Short account
The film is a 43.67 s music video in which a human hand levels a tilted floor and AIs earn a shadow, weight, lift, light and finally a single point, one footfall at a time. Each footfall's ring is the border between two media, which gives twelve styles a reason to exist. The final image runs from a horizon line to an ink dot.

External dependencies still unresolved

Real audio timing (RQ-07): LRC offsets and onsets, and whether drops fall where I assumed.
Verified memes and current AI names (RQ-01 to RQ-03), plus SGI usage (RQ-04).
Which video-generation and dance path survives the proofs (RQ-05, P2).
Font licences (RQ-09) and p(doom) source answers (RQ-08).
