# Sound craft: the series rules

The rules every INTERREGNUM episode's sound holds. Each episode's own sound world (its voices, its rooms, its
motifs, its music spotting) lives in `<episode>/bible/sound.md`; the pilot's is `episodes/pilot/bible/sound.md`.
Worked examples below come from the pilot and say so. Visual rules are in `bible/visual.md`, and the "no constant
dial" balance of familiarity, variety and surprise (`bible/visual.md` §1) applies to sound as well.

These rules answer King's note on the pilot's v2 soundtrack: the voices and the rest of the audio had brilliant
ideas but were "not masterpiece-level".

| Failure in v2 | Why it failed | The rule that replaces it |
|---|---|---|
| Voices | Seedance invented a new voice per clip, each with its own baked-in room; the PA was macOS `say` | One cast voice per character, recorded dry, placed in rooms we build (§1.6) |
| Score | A numpy synthesizer can make tones but not music | Music is performed music (ElevenLabs Music). Numpy only plays recorded samples at exact pitches (§10) |
| Foley | Synthesized noise pretending to be rain, paper, bells | Every acoustic sound is a recording with a material, a space and a microphone. Numpy makes only what is electrical (§10) |
| Mix | Cut hard with the picture: no J/L cuts, no continuous rooms, silence not designed | Every place owns a continuous bed; cuts are soft unless the story is hard; silence has a grammar (§7–§9) |

---

## 1. Principles

1. **A sound tells a story or it goes.** Every sound answers "what does this tell us that the picture doesn't?" A
   clock says whose time it is; a bell says who is calling before we see the phone; a hum says the state is in the
   room. Sounds that only decorate are cut.
2. **Music is an event, never wallpaper.** How much music a film has is the episode's choice, but every entrance
   and exit is placed for a reason. The pilot is heard before it is scored: its first bar of non-diegetic music
   arrives at 1:49.
3. **The medium rule, in sound.** A character differs from the world in technique, not medium
   (`bible/visual.md` §2–3). The pilot's copy, the Father, is the steel engraving: in sound he is the one
   **frictionless voice**, with no breath, no room, no noise and perfectly even level. Everything alive has air around
   it: breath, lips, a room, a floor under the feet. Each episode names its copy and gives only that sound the
   frictionless finish.
4. **Behaviour, not emotion** (`bible/visual.md` §6), for voices too. Delivery is directed by volume,
   pace, breath and pauses. No tag or prompt ever asks a voice to be sad, tender, moved or angry. The words, the cut
   and the silence around a line do the feeling.
5. **Perspective follows attention.** Loudness is where the character's attention is, not only where the source is.
   The Committee's red phone never moves off Ida's desk, but it recedes ring by ring as she turns away from it.
6. **Generate dry, place in our rooms.** Voices and close sounds are generated with no room and put into a location
   by one convolution per place (the pilot's: `audio/pilot/mix_plan.md` §3). Everything in a place then shares one acoustic, which is what
   makes a place feel continuous. Only sounds that *are* the space (a hall's air, rain on a roof, a city across water)
   are generated in their perspective.
7. **Hard sound cuts belong to the story's hard events.** A machine stopping, a key committing, a broadcast dying,
   the rain ending. Every other cut is soft (§7).
8. **Silence is a sound with a shape** (§9). It is never filled with a drone, and never used twice for the same thing.
9. **Placelessness.** No real anthem, jingle, ringtone, siren, station ident or brand sound, and no real accent
   signature beyond the voice bible's neutral General American. Prompts to generators carry no artist, film or
   brand names.

## 6. Loudness and dynamics

- **Delivery target (YouTube and streaming):** integrated **−16 LUFS** (±0.5), true peak **≤ −1.0 dBTP**, loudness
  range **12–16 LU**. YouTube turns loud masters down to −14 but never turns quiet ones up, so −16 keeps the film's
  range intact and still plays at a normal level. Measure with ffmpeg `ebur128` (`tools/audio/mix.py` already does).
- **Dialogue is the anchor.** In the final master, normal dialogue sits at **−17 LUFS short-term (±2)**, murmurs and
  whispers at −21. In the pilot, the PA sits at −19 (a public voice), the Father at −17 in the studio and −15 when the whole Hall speaks
  with him. Nothing else is levelled up to dialogue.
- **Range comes from the quiet, not from the loud.** In the pilot, the quiet passages (a room with nobody speaking, rain, a clock)
  sit at −30 to −38 LUFS short-term; the dead air at −50. The loud peaks are few and physical: the loop choir at HALT
  (−9 short-term), the countdown's last second (−10), the dawn at its fullest (−14). Nothing is louder than the loop.
- **One static gain, one limiter.** Mix to the targets above, measure, apply one gain to reach −16, then a look-ahead
  limiter at −1.8 dBFS sample peak. If the gain needed is more than +2 dB, rebalance instead of limiting. Gain
  reduction above 2 dB is allowed only in the last 0.5 s before HALT and before the commit.
- **Small speakers:** most viewers will hear this on a phone or a laptop. Every low sound that matters has harmonics
  above 100 Hz (the Engine's A2, the pulse's knock, the letterpress thump's wood). Check the mix on a phone speaker
  and on headphones before delivery; the silences must still read as silence on both.
- **Stereo, not surround:** the delivery is stereo. Dialogue is centred and mono; the PA and the Address in the Hall
  are the only wide voices (they come from everywhere). The hard cut into the dead air is also a cut from wide to
  mono: the carrier is dead centre.

## 7. J and L cuts

The picture cuts on the tick; the sound decides whether the cut is felt.

1. **Causes lead.** A sound may lead its picture (a J-cut) by 0.3–2.5 s when it is the *cause* of the next shot: the
   capsule rushing through the pipes before it lands, the PA's horns opening before the countdown, Nana's bell before
   the card that says NANA, Ida's chair rolling back before we see her standing.
2. **Tails trail.** A sound that has started finishes: bells, reverbs, a handset put down over the next shot (L-cuts).
   A tail is cut short only by a hard event.
3. **The rain is the bridge.** Rain is the one thing the Hall and the city share. When the film leaves the Hall for
   the city, the rain on the roof opens up into the rain on the canal: a match cut in sound.
4. **Voices don't pre-lap faces.** No line starts before its speaker's lip-synced shot. Voices cross cuts only when
   the speaker is off screen (a phone, a television, a public screen) or when the room changes under a continuing
   voice (the Address: "Tomorrow," in the studio, "you'll have to talk to each other" in the Hall).
5. **Perspective cuts are hard, voices are continuous.** When a continuous voice crosses a cut into a new room, its
   room switches on the frame, and the old room's tail is dropped.
6. **Soft by default.** Every bed crossfades over 2 frames (83 ms) at a cut, so no cut clicks and no place starts from
   zero. Dialogue and hard effects are never crossfaded.
7. **Hard only on purpose.** In the pilot: the tape-stop (19.0), HALT (70.4), the Air Clock killing Nana's E (117.0), the commit key
   (149.0), the dead air (180.0) and the rain stopping at dawn (223.0).

## 8. Room tone and continuity

- **Every place owns one continuous bed** that runs in real time from the first shot to the last in that place. At a
  cut it is gated, never restarted, so returning to the Hall returns to the Hall's continuing time: the same rain, the
  same air, the clock on its next second.
- **No place is ever silent by accident.** If a shot has no action, its bed is heard. Digital silence is used only
  where §9 says so.
- **Beds change for reasons.** The Hall loses the Engine's hum when the power goes (186.4) and its air goes still. Nana's
  room loses the A when she switches the set off (heard from 198.0). The city loses the rain at dawn. Each change is a
  story beat, and the new bed stays changed.
- **The far room travels.** During a call, the listener's shot carries the other room faintly down the line (its
  clock, its rain, its simmer), band-limited like the voice. It is one-way: Nana's home leaks into the Hall; the Hall
  never leaks into Nana's home.

## 9. The grammar of silence

| Kind | What we hear | Means | In the pilot |
|---|---|---|---|
| **Digital black** | absolute zero: no bed, no rain, no clock | the machine stops the world | HALT 70.4–71.0; the commit 149.0–149.3 (after the key) |
| **Signal gap** | zero, then the room breathing in | a broadcast has stopped and the room hasn't arrived | 19.4–20.0 after the tape-stop |
| **Dead air** | the broadcast carrier alone, −50 dBFS, dead centre | the state has nothing to say | 180.0–186.0, six seconds, the longest silence in the film |
| **Held breath** | every layer ducks away but one thin one | the moment of a reveal | the archive stop (45.6–47.1): only the scope's thin A; the street after "I died in the spring": only rain |
| **Absence** | a sound we have learned, missing | something has ended | no hymn under the Address; no tick in the Hall after 180; no A in Nana's room after the set goes off; no rain at dawn |
| **The missing note** | the E♭ that should land at 234.5 doesn't | the new cannot be born | the end chime: B♭4, G4, and nothing |

Rules: never fill a silence with a drone or a pad; never use digital black for emotion (only for machines); let at
least 0.5 s of a silence play before anything answers it.

## 10. Making the sounds (generation rules)

- **SFX prompts** name the object, its material, the action, the space and the microphone: "a heavy steel capsule
  slamming into a cast-brass cup, recorded close" and not "capsule impact". Close sources are asked for dry ("recorded
  close and dry, no reverb"); the room is ours.
- **Pitched objects** (hums, whines, bells, the Chime) are generated once and **retuned** by resampling to the
  pitch the score needs. A resampled recording is still a recording.
- **Loops** are generated with the model's loop option and checked at the seam; beds longer than 22 s are built by
  crossfading two different takes, never by repeating one audibly.
- **Numpy is for electricity and plumbing only:** the broadcast carrier, the dead air, the tape-stop, hum wind-downs
  (by slowing the recorded hum), convolution rooms, levels. It never makes an acoustic sound or a note.
- **Voices:** audio tags are behaviour only ([softly], [whispering], [pause], [exhales], [laughs quietly], [clears
  throat]); never an emotion. One scene per request, fixed seed, and the words exactly as scripted.
- **Music:** composition plans with sections on hit points, instrumental, with negative styles that name what the film
  refuses (trailer, lofi, drums, choir, synth pads). Always two takes; choose the plainer one.

## 11. What Claude cannot judge

Claude reads waveforms, spectra and loudness, not feelings. King listens, and every handoff names what for. In the
pilot: whether the voices are the right
people (casting), whether the laugh in 42 is one small true laugh, whether the loop at 70 is frightening and not
comic, whether the dead air holds for six seconds without the audience thinking the file broke, and whether the
dawn swells without tipping into sentiment. Every handoff says so plainly.
