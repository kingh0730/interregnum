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
