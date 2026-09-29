# CONTINUITY: mix plan

How the pilot's sound is assembled: the buses, the rooms (convolution we build in numpy), the voice chains, the loop,
the level and perspective plan per scene, every J/L cut and every silence. Rules are in
`../../bible/sound/sound_bible.md`; sources in `dialogue.json`, `sfx.json` and `score_cues.json`. Times are absolute
seconds in the 242 s main cut; 48 kHz, 32-bit float while working, 24-bit for delivery.

## 1. Buses

| Bus | Holds | Processing on the bus | Notes |
|---|---|---|---|
| **DX** | every line (D, V, W), after its chain and room | none (all shaping is per line) | the loudness anchor; no ducking is ever keyed from anything but DX |
| DX·FATHER | D01–D04, D06–D07, D17–D21, D27–D28 | the Engraving chain (§4) before the room | mono at the source |
| DX·IDA / DX·NANA | their lines and breaths | their chains (§4) | V lines ride with their speaker |
| DX·PA | D09, D15, D16 | the tape stage, then HALL_PA | the only wide voice besides the Address in the Hall |
| **BCAST** | everything inside the 4:3 picture: the Father, M1, the Chime at the idents, the carrier, the optical track | mono sum, soft high cut at 12 kHz | the tape-stop (X02) acts on this bus only; the world buses are empty at 19.0 anyway |
| **FX** | one-shots: clock, relays, keys, phones, pneumatics, thermos, doors, the letterpress | none | the red phone's perspective is per event (ATTENTION, DESK, HALL_FAR) |
| **AMB** | continuous beds: Hall air, hum, roof rain, tubes, flat tone, window rain, TV, simmer, city, street, dawn, line hiss | 83 ms crossfade gates at every cut (§6) | one continuous render per bed, gated by spans, never restarted |
| **MX** | M2, M3, M4 (the living's music and the Unison) | none | ducks only where `score.md` says (3 dB round Ten seconds); never under D26 or the laugh |
| **WALLA** | C10 and W01–W10 | low-pass 1.8 kHz on the murmur group only | W01/W02 bypass the low-pass (3.5 kHz) |
| **MASTER** | the sum | one static gain to −16 LUFS, then a look-ahead limiter at −1.8 dBFS sample peak (true peak ≤ −1.0) | no bus compression, no master EQ |

**Digital black** (70.40–71.00, 149.08–149.30) mutes every bus, including AMB and BCAST. The dead air (180.0–186.0)
mutes every bus except BCAST's carrier.

## 2. Levels: what the numbers mean

`lvl` in `sfx.json` is the target in the final master: LUFS short-term for beds, peak dBFS for one-shots. Dialogue
targets are short-term LUFS in the master: speech −17 (±2), murmur −21, PA −19, the Father −17 in the studio, −19 in
the street, −15 through the Hall's horns, −22 through Nana's television, D26 −17 (never smaller than a line on screen).
Mix to these, render, measure (ffmpeg `ebur128`), apply the one gain; if it exceeds +2 dB, rebalance instead.

## 3. Rooms (convolution built in numpy)

Every room is an impulse response built once and cached as `work/pilot/audio/ir/<ROOM>.npy` (git-ignored), then
applied by FFT convolution (as `reverb()` in `tools/audio/mix.py` already does, extended to arbitrary IRs).

**The builder.** An IR is the sum of (a) the **direct** sound (a unit impulse, or a filtered one), (b) **early
reflections**: taps at a delay, gain, pan and low-pass each, from the room's geometry, and (c) a **diffuse tail**:
two decorrelated channels of Gaussian noise, split into octave bands (63 Hz–8 kHz) in the FFT domain, each band
multiplied by `exp(-6.91 t / RT60_band)`, summed, faded in over the room's density time (sparse to dense), with a
pre-delay, then energy-normalised. Wet level is set per placement. Rooms that are loudspeakers (horns, the TV, the
monitor, the phone) put a transfer function before the room.

| Room | Geometry and recipe | Used for |
|---|---|---|
| **HALL** (base) | the basilica: nave 120 m, 34 m wide with aisles, vault 30 m, concrete and terrazzo, the Wall a grid of glass. RT60: 63 Hz 7.5 s, 125 7.0, 250 6.5, 500 6.0, 1k 5.5, 2k 4.5, 4k 3.2, 8k 2.0. Taps for a listener at Desk 4: floor 5 ms −6 dB; the piers 45 ms and 52 ms −14 dB (left, right); the vault 175 ms −16 dB; **the Wall 230 ms −12 dB, bright** (glass: the slap that makes the size legible); the back wall 470 ms −20 dB, dark. Density from 80 ms, full by 250 ms | the parent of every HALL room |
| **HALL_BED** | no convolution: the bed is the space | H01, H03, H04 |
| **DESK** | direct; a desk-top tap at 2 ms −8 dB; HALL at −24 dB wet for voices, −16 dB for objects, pre-delay 20 ms | Ida's voice and breath; desk foley |
| **DESK_GLASS** | DESK plus one reflection off the Proof's glass: 1.2 ms, −9 dB, high-passed at 800 Hz (a thin shine) | D05: "Hold still" said to a face through glass |
| **HALL_FAR** | a source 40 m away and 20 m up: direct −12 dB and low-passed at 6 kHz (air); taps: the Wall 90 ms −6 dB (the clock hangs above it), vault 60 ms −8 dB; HALL tail at −4 dB relative to direct (far sounds are mostly room) | the Air Clock, the big flaps, the far red phone, the door, the ON AIR contactor, the pneumatic's start |
| **HALL_FLOOR** | from under the grilles, everywhere at once: low-pass 2 kHz, near-mono (width 30 %), a short 0.8 s diffuse, HALL tail −18 dB | the Engine's hum and its automation; the master pulse |
| **ATTENTION** | DESK position, pushed back by her focus: direct −8 dB, low-pass 2.5 kHz, HALL tail −6 dB relative (wetter than physics) | the red phone while she types (24–27), turned away (40) and fading (42) |
| **HALL_HORNS** | the horn array: 30 horns, one on each side of 15 piers 8 m apart, from 80 m behind Desk 4 to 40 m in front, 9 m to the side, 6 m up. Each horn arrives at d/343 s with gain 20·log10(d_min/d) (d_min ≈ 10.3 m, the farthest −18 dB), panned by its side (±0.5, narrower with distance). Horns in front of her face her (full band); horns behind her face away (−6 dB, low-pass 1.8 kHz). Horn response before the array: high-pass 350 Hz, low-pass 5 kHz, +6 dB at 1.1 kHz (Q 2), +3 dB at 2.8 kHz, soft clip `tanh(1.8x)/tanh(1.8)`. Then HALL at −3 dB relative: the horns excite the whole vault | the Father in the Hall (D20's second half); the loop's escape |
| **HALL_PA** | the tape of Year One, then HALL_HORNS. Tape: high-pass 250 Hz, low-pass 6 kHz, `tanh` saturation (drive 1.4), wow 0.45 Hz ±8 cents, a capstan start on each phrase (−40 cents rising to 0 over the first 60 ms), tape hiss −56 dB under the phrase only | the PA (D09, D15, D16); H37 skips the tape stage |
| **MONITOR** | Desk 4's cue speaker in the console, 0.8 m from her: high-pass 160 Hz, low-pass 7 kHz, +4 dB at 600 Hz (Q 1.5, a steel box), mild soft clip, then DESK | the loop's first voice (D06) |
| **BCAST** | the room with no walls: the Engraving upstream; high-pass 60 Hz, soft low-pass 12 kHz; a 0.7 s tail of dense Gaussian noise with **no early reflections**, identical in both channels (the broadcast is mono), at −26 dB wet; the carrier (X01) under it | the Father in the studio, M1 |
| **OPTICAL** | the ident film's soundtrack: high-pass 90 Hz, low-pass 7.5 kHz, wow 0.6 Hz ±5 cents and flutter 9 Hz ±2 cents (resampling), 0.8 % second harmonic, mono, BC01 under it | the Chime at 0.5–1.5 and 243.3–244.3, the splice pops |
| **OPTICAL_COLD** | OPTICAL with a 3 kHz low-pass, half the flutter, and each note's decay shortened to 1.2 s | the fast ident at 149.3 |
| **TV** | Nana's State Receiver: high-pass 180 Hz, low-pass 5.5 kHz, +5 dB at 400 Hz (Q 1.2, the cabinet), +3 dB at 2.5 kHz (the cone), a valve's asymmetric soft clip (`tanh(x + 0.08x²)`), then FLAT at 1.2 m | D21; N04 |
| **FLAT** | one room 4.5 × 3.8 × 2.5 m, soft furnishing. RT60: 125 Hz 0.5 s, 500 0.38, 2k 0.3, 8k 0.2. Taps: **the low ceiling 7 ms −5 dB** (the lid, audible as closeness), side wall 11 ms −9 dB, the window 13 ms −10 dB (bright), back wall 17 ms −12 dB. Wet −18 dB for her voice, −8 dB for the clock on the wall, −10 dB for the stove | Nana, her room, her clock |
| **PHONE_EAR** | Nana's carbon microphone and the line, heard as Ida hears it: high-pass 280 Hz, low-pass 3.6 kHz, +3 dB at 1.8 kHz, a carbon grain (the signal times `1 + 0.03·n(t)`, n low-passed noise at 200 Hz) and 0.5 % third harmonic; the far room (her clock, rain and simmer) mixed in *before* the band at −20 dB under her voice; the line hiss (H29) at −48; mono, centre, no room on our side | D26 |
| **LINE_SPILL** | the PHONE_EAR band heard from 20 cm outside the earpiece: −26 dB, +2 dB at 3 kHz, DESK at −20 dB wet (or FLAT on Nana's side) | the far room under the listener's shots; H29 |
| **STREET_PR** | the Public Receiver's horn columns on the civic building 55 m ahead: band 150 Hz–6 kHz, +3 dB at 1.5 kHz, direct −6 dB; facade taps 64 ms and 71 ms −9 dB (left, right); a flutter between the facades (period 64 ms, five repeats, −4 dB and darker each); **the slap off the buildings behind the crowd at 350 ms, −8 dB**; an open-air tail of RT60 2.2 s at −8 dB | D18 |
| **STREET** | acoustic sources in the street: the facade taps of STREET_PR and a 1.4 s tail at −14 dB | the tram, its contactor |
| **CANAL** | across the canal, 150–400 m: air absorption (low-pass 3.5 kHz with −6 dB/octave above), a reflection off the water at +8 ms −4 dB, a wide 2.5 s diffuse at −10 dB | the city beds, the tram bells, birds, windows |
| **CITY_SETS** | the Chime through TV, forty copies: delays spread 0–350 ms, gains 0 to −14 dB at random, pans ±0.9, each low-passed between 1.8 and 4 kHz by distance, then CANAL and a 4 s diffuse at −6 dB. No copy may stand out: a smear, not an echo | the standby chime at 80.0 |
| **WINDOW** | each walla voice in a small room (RT60 0.4 s, −12 dB wet), out of a window (high-pass 200 Hz), across the canal: low-pass 1.8 kHz for murmur (3.5 kHz for W01, W02), −6 to −14 dB by distance, panned to its window, then CANAL's diffuse at −14 dB. W07 through a phone band first | W01–W10, C10 |
| **DAWN** | the near field on the embankment: taps at 4 ms and 9 ms (railing, stone), no tail past 0.6 s | drips, dawn air |
| **AIR** | a real, quiet medium room (a print shop): RT60 1.2 s, taps 9, 14 and 21 ms, natural | the last Chime (the first time it is heard in air) and the letterpress |
| **DRY** | no room | the title beam, the D3 toll, the commit key in the black |

## 4. Voice chains (before the room)

- **The Engraving (the Father).** 1. Remove every breath (unvoiced broadband segments between phrases) with 10 ms
  fades. 2. Set the gaps between phrases to digital zero: the carrier (X01) is his only floor. 3. Ride the level so
  300 ms RMS stays within ±1 dB of −20 dBFS (50 ms attack, 400 ms release). 4. EQ: +1.5 dB shelf at 150 Hz, +1.5 dB at
  3.5 kHz, −2 dB shelf from 7 kHz (no sibilance). 5. Mono. Then BCAST, TV, STREET_PR or HALL_HORNS. The same
  processed clips are used everywhere they recur (D01 = D17 = D27, D03 = D28, D04 = D21).
- **Ida.** High-pass 70 Hz; +2 dB at 180 Hz (the closeness a dry TTS lacks); de-ess −3 dB at 6.5 kHz on the s only.
  Keep her breaths. Then DESK (DESK_GLASS for D05).
- **Nana.** High-pass 60 Hz; +1.5 dB at 250 Hz; −1 dB shelf above 5 kHz. Then FLAT, or PHONE_EAR for D26. **The
  "eighty" chain**, only if she is cast from the Matilda fallback: a 4.5 Hz, ±6-cent pitch tremor on voiced segments
  (resampling with a modulated rate), a −2 dB shelf above 6 kHz, and the pace from the TTS `speed`, never a
  time-stretch.
- **The PA.** Straight into HALL_PA; the three phrases share one gain.
- **The city.** WINDOW. Stagger the murmur so no two onsets land within 0.3 s, and none on a window-switch frame in
  224.0–225.0.

## 5. The loop (shot 12, 63.3–70.4)

The Engine does not speak: it splices the cold open's own processed clips, and its output collapses onto its most
probable phrase.

| Phase | Time | What plays | Where |
|---|---|---|---|
| A | 63.3–66.3 | D01 at 63.3; "The harvest is in." (the first half of D02) at 65.4. At each join, drop one frame of carrier and put a two-sample step at −42 dBFS: the seam is audible as a tiny tick | MONITOR |
| B | 66.3–68.0 | overlapping fragments, each starting before the last ends: "The sea is calm." 66.3, D03 66.7, the T02 fragment ("Sleep safely; I am watching over you.") 67.0, D03 67.35, "The sea is calm." 67.6, D03 67.8. Each copy sends 10 % more to HALL_HORNS than the one before; pans ±0.2 | MONITOR into HALL_HORNS |
| C | 68.0–70.4 | only D03, about thirty copies: onset interval shrinking exponentially from 0.33 s at 68.0 to 0.067 s at 70.0, then constant; each copy detuned at random by 15–40 cents (resampling), panned at random within ±0.8, low-passed from 8 kHz down to 3 kHz across the phase, and sent from 40 % to 100 % into HALL_HORNS: the voice leaves the speaker and becomes the building. The stack rises 8 dB to −9 LUFS short-term at 70.2 | HALL_HORNS |
| Under | 66.3–70.4 | the Engine straining up a semitone (X05), the tubes' whine rising (H04), the teleprinter from 69.0 (H20), the scroll relay (H21) | |
| Stop | 70.38–71.0 | the HALT relay (H10) at 70.38; digital black on every bus from 70.40; at 71.0 the Air Clock's step is the first sound back, and every bed resumes at its continuing position | |

Picture note for the JS pass (J07): the terminal should append each fragment at its onset in phases A and B (in the
script's order), and only "I am well." from 68.0.

## 6. Scene by scene: perspective and level

| Scene | Time | We listen from | Dialogue (LUFS-S) | Beds | Music | What must be heard |
|---|---|---|---|---|---|---|
| Cold open | 0.0–19.4 | inside the television, mono | Father −17 (BCAST) | optical crackle −42 (0–5), carrier −54 | M1 −30 under the voice, −24 at the swell's top (4.8) | the Chime on the lamp; the 9.2 stutter tick at −36; the hymn caught on its A by the tape-stop |
| Freeze | 19.0–22.0 | the stop, then Desk 4 | — | signal gap 19.4–20.0, then the Hall breathes in | — | tear 19.0; pen click 20.6; the first tick 21.0 |
| Night desk | 22.0–54.0 | the institution's eye, then the desk | D05 −21 | Hall air −38, hum −40, roof rain −44, tubes −46 | none | relays in 06; the exhale 40.1; the brake and the held breath 45.6; the scope's A; the D3 toll 50.3 |
| No agreement | 54.0–77.0 | Desk 4 | D08 −18; PA −19 | Hall | none | the capsule's approach (J) and impact; the loop's rise to −9; digital black; the clock back at 71.0 |
| The warm window | 77.0–109.4 | across the canal; a guest in the flat; Ida's desk | Ida −18, Nana −17 | city rain −30, canal −42; flat tone −44, window rain −40, TV −46 breathing, simmer; in Ida's shots the line spill with Nana's clock at −48 | none | the thousand-sets chime; her clock's limp; the bell of home; the lift; two clocks through one wire |
| Sign-offs | 109.0–117.0 | Desk 4 | — | Hall −40 | M2 −24 | the hang-up (L); the scroll relay thinning; the E held and killed at 117.0 |
| Night 212 | 117.0–149.0 | the axis and the desk | PA −19 | Hall, the Engine's load rising 8 dB | M3 from −40 to −12 | the minute clunk; the pulse; the chair (J); keys; the sag and the needle at 128.2; the red phone pushed back by her attention; the amber A at 137.7 (−20, dry, close); the commit key alone at 149.0 |
| The Address | 149.3–180.0 | the television; the street; the Hall; Nana's TV | Father −17, −19, −15, −22 by room | carrier −54; street rain −30; Hall; flat | the fast ident's chord only; M2's A–F–G from 177.5 | no hymn; the tram's death at 158.8; the perspective cut at 168.0; the same sign-off as the cold open, sample for sample |
| Dead air | 180.0–186.0 | the dead broadcast | — | carrier −50 | — | six seconds of nothing else |
| Come home | 186.0–217.0 | Desk 4 and the flat | Ida −18, Nana −17, D26 −17 | Hall still −44, roof rain −42; line spill with her clock at −46; flat without the TV | M4 from 210.0, piano −24 under the voice | ON AIR and the wind-down; the red phone at −12, close; the bell of home in the Hall (J); her clock the only clock; the cord; the D on "warm"; the cap, the pop, the laugh |
| Empty hall | 217.0–223.0 | the institution again | — | Hall still −40, tubes on standby −52 | M4 B♭ −30 | the door; the red phone for no one |
| First light | 223.0–233.0 | the neighbour across the canal | walla −44 rising to −30; W01, W02 −24 | no rain: dawn air −46, drips −40, canal −46 | M4 −20 rising to −14 at 231.0 | the rain's absence on the cut; windows opening; the two lines |
| Titles | 233.0–242.0 | the film's own voice | — | everything fades 233–236 | M4 −28, the last chord −22 | the Chime B♭4, G4 and the empty 234.5; the letterpress at 238.0; silence from 241.6 |
| Alt tail | 242.0–252.0 | the dark desk, then the television | Father −17 | the Engine's A is back | M1 from 243.8 | the drum click; the old key, whole |

## 7. J and L cuts

| # | Time | Kind | Lead / trail | What |
|---|---|---|---|---|
| 1 | 0.0 | J | 0.2 | optical crackle on the black leader before the first image |
| 2 | 1.5 → 5.0 | L | 3.5 | the Chime's D and the hymn ring across the cut into the Father |
| 3 | 20.0 | J | 1.0 | the Hall breathes in under the pull-back, before the room is fully a room |
| 4 | 40.9 | J | 0.1 | the archive motor under Ida's exhale |
| 5 | 49.2 → 50.3 | L | 1.1 | the empty frame's clunk decays into the title; the D3 toll |
| 6 | 52.4 | J | 1.6 | the capsule rushing through the building under the title |
| 7 | 56.3 | J | 0.7 | the seal cracks before we see the opened capsule |
| 8 | 62.8 | J | 0.2 | the FREE relay before the terminal |
| 9 | 74.85 | J | 0.15 | the PA's horns open under Ida's close-up |
| 10 | 76.0 | J | 1.0 | the rain bridge: the roof's rain opens into the canal's rain |
| 11 | 82.94 | J | 1.06 | one tock of Nana's clock and her room from the warm window |
| 12 | 84.0 | match | — | the city's rain becomes the rain on her window, same level, 83 ms crossfade |
| 13 | 89.9 → 109.4 | L (wire) | — | Nana's room runs down the line under Ida's shots |
| 14 | 109.4 | L | 0.4 | Ida hangs up over the terminal |
| 15 | 116.85 | J | 0.15 | the horns open over Nana's held E |
| 16 | 118.2 | J | 0.8 | her chair rolls back before we see her standing |
| 17 | 133.1–135.8 | split | — | her typing over her eyes: sound carries the action the picture skips |
| 18 | 149.0 | sound completes picture | 0.08 | the commit key on the first frame of black |
| 19 | 157.0, 163.0 | perspective | — | one continuous take; the room switches studio → street → studio on the cuts; the rain is hard out at 163.0 |
| 20 | 168.0 | perspective, mid-line | — | "Tomorrow," in the studio; "you'll have to talk to each other" in the Hall |
| 21 | 174.0 | perspective | — | the Father from the Hall's horns to Nana's television |
| 22 | 191.6 | J | 0.4 | the bell of home in the Hall before the card that says NANA |
| 23 | 195.0 | L (wire) | — | the lift on the cut; her clock down the line in 38, 40 and 42 |
| 24 | 210.0 | off-screen voice | — | "Come home" over Ida, from Nana's take |
| 25 | 215.4 → 217.4 | L | 2.0 | the piano's D and its answer ring into the empty hall |
| 26 | 217.3 | L (her exit) | — | a door far away: the one sound of her leaving |
| 27 | 233.0 | L | 3.0 | the walla, drips, birds and canal fade under the epigraph |
| 28 | 242.0 | alt | — | the Engine's A returns under the drum click |

Hard cuts, on purpose only: 19.0 (tape-stop), 70.4 (HALT), 117.0 (the E killed by the minute), 149.0 (the commit),
180.0 (dead air), 223.0 (the rain stops).

## 8. Silences

| Time | Kind | What is on the buses |
|---|---|---|
| 19.4–20.0 | signal gap | nothing; the Hall enters from 20.0 |
| 45.6–47.1 | held breath | only the clock (−28), the scope's thin A and the brake's tail; every bed −18 dB |
| 70.40–71.00 | digital black | nothing at all |
| 149.08–149.30 | digital black | nothing at all (the key's 80 ms came first) |
| 154.6–157.0 | absence | the carrier alone where the hymn should be |
| 159.6–163.0 | held breath | rain on umbrellas; four hundred people not speaking |
| 180.0–186.0 | dead air | the carrier at −50, mono, dead centre |
| 186.4–188.0 | absence | a Hall with no hum and no clock; faint roof rain |
| 234.3–234.9 | the missing note | M4's open fifth and nothing new |
| 241.6–242.0 | end | nothing |

## 9. QA before handoff

- Loudness: I −16 ±0.5 LUFS, true peak ≤ −1.0 dBTP, LRA 12–16 LU (`ebur128`). Report bus peaks.
- Dialogue: every D line's short-term loudness inside its target ±2 LU; D26 no quieter than D25.
- Sync: each voiced onset within 40 ms of `dialogue.json`; the Chime's notes on their frames; D20's pause straddles
  168.0; the D of M4 at 214.4 ±0.1.
- The A: the Engine's hum, the TV's hum and M3 within 5 cents of each other (spectrum at 110 Hz and 220 Hz).
- Mono fold-down: the walla, the horns and CITY_SETS must not hollow out.
- Small speaker and headphones: the hum, the pulse and the letterpress still read on a phone; the silences still
  read as silence.
- Files: stems per bus (`main_v3.<bus>.wav`) next to the master, all in `work/pilot/audio/` (git-ignored); delete
  rejected generations once a cue or asset is final (the disk is nearly full).
- **King's ears** (Claude cannot judge these): the casting; the laugh at 215; whether the loop at 70 frightens rather
  than amuses; whether six seconds of dead air read as intent; whether the dawn stays short of sentiment.

## 10. Build notes (for the audio pass)

`tools/audio/mix.py` already has what most of this needs: file events with `norm`, `spans` gating, `mutes`,
`nomute`, the tape-stop, per-event `reverb`, stems and loudness. The pass adds, in the tool: a `room` key that
convolves with a cached IR from a small `rooms.py` builder (§3); a `pitch` key that resamples a sample to a note (the
Chime, the motif fallback); an `every` key for series; and `lvl` targets resolved against each asset's measured
loudness. Until then, the IRs can be approximated with the existing `reverb` + `slap` keys, which is not the plan.
