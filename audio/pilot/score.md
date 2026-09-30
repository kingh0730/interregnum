# CONTINUITY: the score

Four cues, 96 seconds of generated music in a 242-second film, and most of that music is either inside a television
or saved for the last half minute. The ready-to-send requests are in `score_cues.json`; the rules behind them are in
`../../episodes/pilot/bible/sound.md` §2 and §5. Times are absolute seconds in the main cut.

## The idea

**The state has one note and the living have one tune.** The Engine under the Hall hums on A (55 Hz), every State
Receiver hums on it, and the ident's chime starts on it and resolves it to D every night at nine: a ritual answer to a
question nobody is allowed to ask. Nana's motif starts on the same A and goes into D minor instead. The film's music
is the story of those two things: the A is taken up by an orchestra and cut off at the moment of the broadcast, and
Nana's tune is interrupted twice and completed once, on the word "warm". Then the key lifts a half step to E♭, a
tritone away from the state's A, and the A survives only as a bright colour inside the new chord.

**Two orchestras, never mixed.** The state: a small studio orchestra with brass chorale, organ and celesta, heard
only inside the 4:3 broadcast. The living: an old upright piano, then strings and woodwinds, never heard inside a
television. No brass, organ or celesta ever plays for the living.

## Where the music is, and where it isn't

| Time | Music | Why |
|---|---|---|
| 0.0–1.0 | none: optical crackle on the black leader, the Chime's A at 0.5 | the ritual starts as a film |
| 1.0–19.4 | **M1 The State Hymn** (diegetic, in the broadcast), tape-stopped at 19.0 | the state's music: sweet, certain, never resolving (it is caught on the dominant) |
| 19.4–109.0 | **none.** The Hall is scored by the building: the Engine's A, the Air Clock, the roof rain, relays, the archive's motor, the loop | music would tell us how to feel about a machine; the building already does. And the first entrance at 109 needs 90 seconds of nothing to be an event |
| 50.3 | the Chime, one low D toll under the title (a sound, not a cue) | the state's bell names the episode |
| 63.3–70.4 | the Loop: the Father's voice splicing itself into a choir (dialogue, not music) | the film's first climax is made of the copy's own voice |
| 80.0 | the standby chime from a thousand sets across the canal (a sound) | the whole city saying the same thing |
| 84.0–109.0 | **none** through the first call | two rooms and a wire; the words are enough |
| 109.0–117.0 | **M2 Sign-offs**: Nana's motif, first four notes, stopping on E | the first music of the film arrives with the first proof of love: her lines in the machine |
| 117.0 | M2 cut dead by the Air Clock's minute clunk | the state interrupts her |
| 117.0–149.0 | **M3 Night 212**: strings converging on the state's A, from nothing to everything | the whole state tuning to one note before the broadcast |
| 137.7 | one warm piano A on top of M3 | the machine offers her phrase back in her colour; the only warm note in the countdown |
| 149.0–149.3 | digital black | the commit |
| 149.3–151.8 | the Chime fast and cold, and M1's first chord low-passed | the ritual, started late |
| 152.0–177.5 | **none** through the Address | the missing hymn is the sound of the truth; one voice, four rooms |
| 177.5–180.0 | **M2 again**, A–F–G, cut by the dead air | she smiles; the broadcast dies mid-note |
| 180.0–210.0 | **none**: dead air, the power-down, two phones, the second call | the truth arrives unaccompanied |
| 210.0–242.0 | **M4 Come Home / First Light** | the motif completes on "warm"; the empty hall; E♭ at dawn; the chime's third note withheld; the title |

## Themes

### The Chime (the state's bell)
A4 – F♯4 – D4, 5–3–1 in D major, 0.5 s apart. One recorded strike of a small tuned chime bar, repitched in numpy to
every note it plays (`sfx.json` BC04), so it is the same object every time. It is the only musical material that
crosses from the state into the film's own voice, at the very end, in E♭, missing its last note.

### The State Hymn (M1)
An invented chorale, D major, 60 BPM, one chord a bar: **D | G | D | A**, and it stops on A. The tune moves by step
inside the chords (a guide, not a demand: F♯ G A A | B A G F♯ | F♯ E D F♯ | E, held). Only major triads, no
suspensions, no minor: slightly too sweet. Studio strings, a soft chorale of horns and flugelhorns, celesta an octave
over the tune, a quiet organ pedal, recorded as a warm, narrow mid-century studio. It must quote no real anthem and
never march.

### Nana's motif (M2, M4)
**A – F – G – E – F – D**, 5–3–4–2–3–1 in D minor, one note at a time on an old upright piano in a small room: a tune
picked out by one hand from memory, with the hammers and the pedal audible and the tuning a little tired. It shares
its first note with the Chime and turns minor on its second.
- **109.0 (M2):** A F G E over D minor, B♭, B♭ and C, and it **stops on E**, held on the pedal: a half cadence left
  open.
- **177.5 (M2, reused):** A F G, and the dead air cuts through the G while it is still ringing.
- **210.2 (M4):** complete at last, a little faster (about 0.8 s a note) under "Come home. The soup's still warm.",
  over F and C/E, arriving on **D at 214.4**, right after "warm", with a high D answering at 215.4 as the laugh
  happens.
- **137.7:** its first note alone, the A, in the middle of the countdown. The machine offers her words; her instrument
  plays the state's note warm.

### The Unison (M3)
The state's A taken up by a string orchestra: basses and cellos first, then violas, then everyone, in every octave,
bowing slower than breath and louder by degrees until the commit key cuts it. No harmony, no melody, no drums, no
risers. It is what an orchestra does before a performance (converge on the A), composed and controlled. It has one
hole: at the word "died" the low strings stop (128.0) and only a thin harmonic A survives while the needle lies on its
pin.

### The Lamps (M4, dawn)
E♭ major with a raised fourth (E♭ Lydian: the state's A becomes a colour inside the new chord), built by instruments
entering one at a time on long notes, like windows switching from screen blue to lamplight: a viola, a cello, second
violins, a clarinet, first violins, a flute on the high A. No melody. It thins to an open fifth under the epigraph,
and ends on a suspended chord with no third: the new cannot be born.

## Keys

| Place | Key | Why |
|---|---|---|
| the state (hymn, chime) | D major, stopping on A | the ritual answer, never quite given |
| the Hall | the Engine's A (no key) | a dominant held for 41 years |
| Nana | D minor / F major | the same D as the state, the other mode |
| the countdown | A alone | the state's note, bare |
| the resolution | D minor, on "warm" | home, and not the state's home |
| the empty hall | B♭ major | D minor's sixth and E♭'s dominant: the pivot |
| dawn | E♭ Lydian | a half step above home and a tritone from the state; the old A inside it as a colour |
| the title | E♭ sus2 (E♭ F B♭) | no third: unresolved |

## The cues

### M1 The State Hymn (diegetic)
- **In 1.0, out 19.4.** Generated 20 s: swell 1.0–5.0 (D), chorale bars at 5.0 (D), 9.0 (G), 13.0 (D) and 17.0 (A,
  held). Hits: the flame stands with the Chime's D at 1.5, the swell peaks as the Father appears at 5.0, "The sea is
  calm" rides the move to G, "I am well" lands on the return to D at 13.0, "Eat something warm before you sleep"
  ends on the held A, and the tape-stop at 19.0 catches the A still sounding.
- **Reuse:** 149.9–151.8 (the first chord, low-passed at 1 kHz, the fast cold ident), and the alt tail from 243.8.
- **Level:** −30 LUFS short-term under the voice, through the broadcast chain (mono, narrow, soft top).

### M2 Sign-offs
- **In 109.0, out 117.0** (cut dead on the Air Clock's minute at 117.0). Generated 12 s. Hits: A 110.0 (the first
  amber line crosses the middle row), F 111.0, G 112.0, E 113.0, held to the cut.
- **Reuse:** A F G (110.0–112.9) moved to 177.5; cut at 180.0 by the dead air. Its A4 is also the amber note at 137.7.
- **Level:** −24 LUFS short-term; nothing else in the scene is louder than the scroll relay.

### M3 Night 212
- **In 117.0, out 149.0.** Generated 32 s in six sections: low A (117.0), violas (125.0), the hole (128.0), the
  thickening (131.0, with VIEWING and the first ring of the red phone), the held breath (137.0, room for the amber
  note), the last crescendo (140.0, TAB) to a full-strength stop at 149.0.
- **Mix:** it doubles the Engine's hum on the same A, so the building and the orchestra are one sound; it ducks 3 dB
  around "Ten seconds." (145.35) and is cut with everything at 149.0 under the commit key.

### M4 Come Home / First Light
- **In 210.0, out 242.0.** Generated 32 s in seven sections: the motif (210.0), the D and its answer (214.4), the empty
  hall on B♭ (217.4), the lift to E♭ (223.0, the cut to dawn, the rain gone), the lamps entering (228.0), the open
  fifth under the epigraph (233.0), the suspended chord on the title (238.0) fading out by 241.6.
- **On top (from `sfx.json`):** the Chime B♭4 at 233.5 and G4 at 234.0, and at **234.5 nothing**: the E♭ is withheld,
  and the music has left that moment empty. The letterpress impression at 238.0 lands with the last chord.
- **Never ducked** under "Come home" or the laugh; the piano sits at −24 under Nana's voice at −17.

## Generating and cutting

1. Run each request twice (`score_cues.json`). Choose the plainer take: fewer notes, less reverb, no swell that
   wasn't asked for. Reject any take with drums, choir, synth pads or a trailer rise, whatever else it does well.
2. Slip each cue so its first section starts on its in point. If a section boundary drifts more than 0.25 s from its
   hit, re-cut at the boundary with a 60 ms crossfade inside sustained material.
3. **Motif notes are placed, not hoped for.** If a motif note misses its hit by more than 0.15 s or plays the wrong
   pitch, cut the cleanest single piano note from the same cue (2 s of decay, no other notes), repitch it by
   resampling in numpy and play the motif from it at the exact times. The timbre and the room stay the cue's own.
4. M3 is cut at 149.0 with a 5 ms fade; M2 at 117.0 with a 5 ms fade; M2's excerpt at 180.0 with a 3 ms fade (the
   dead air is a cut, not a fade).
5. Keep every generated cue in `work/pilot/audio/music/` (git-ignored), and delete rejected takes once a cue is final.

## Budget

Four cues, 96 s per version. Two takes each is 192 s, under the 5-minute ceiling, with room for a third take of M4
(the one that matters most): 224 s in all.
