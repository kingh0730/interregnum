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