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
