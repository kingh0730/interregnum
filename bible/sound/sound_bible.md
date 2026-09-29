# Sound bible: how INTERREGNUM sounds

The series' sonic rules, and the pilot's world in sound. It sits beside `../visual/` (what things are, how they are
drawn and shot) and answers the showrunner's note on the v2 soundtrack: the voices and the rest of the audio had
brilliant ideas but were "not masterpiece-level". The diagnosis, and what this bible does about each part:

| Failure in v2 | Why it failed | The rule that replaces it |
|---|---|---|
| Voices | Seedance invented a new voice per clip, each with its own baked-in room; the PA was macOS `say` | One cast voice per character, recorded dry, placed in rooms we build (§3). Dialogue leads the picture (§3.4) |
| Score | A numpy synthesizer can make tones but not music | Music is performed music (ElevenLabs Music). Numpy only plays recorded samples at exact pitches (§5) |
| Foley | Synthesized noise pretending to be rain, paper, bells | Every acoustic sound is a recording with a material, a space and a microphone. Numpy makes only what is electrical (§10) |
| Mix | Cut hard with the picture: no J/L cuts, no continuous rooms, silence not designed | Every place owns a continuous bed; cuts are soft unless the story is hard; silence has a grammar (§7–§9) |

Companion files for the pilot: `../../audio/pilot/casting.md`, `dialogue.json`, `score.md`, `score_cues.json`,
`sfx.json` and `mix_plan.md`. The v1 temp-score plan (`../../audio/pilot/cues.md`) is superseded where they differ.

---

## 1. Series principles (every episode)

1. **A sound tells a story or it goes.** Every sound answers "what does this tell us that the picture doesn't?" A
   clock says whose time it is; a bell says who is calling before we see the phone; a hum says the state is in the
   room. Sounds that only decorate are cut.
2. **The world is heard before it is scored.** Rooms, machines and weather carry the drama first. Music enters late
   and rarely, and each entrance is an event. In the pilot the first bar of non-diegetic music arrives at 1:49.
3. **The medium rule, in sound.** A character differs from the world in technique, not medium
   (`../visual/art_direction.md`). The pilot's copy, the Father, is the steel engraving: in sound he is the one
   **frictionless voice**, with no breath, no room, no noise and perfectly even level. Everything alive has air around
   it: breath, lips, a room, a floor under the feet. Each episode names its copy and gives only that sound the
   frictionless finish.
4. **Behaviour, not emotion** (`../visual/cinematography.md` §8), for voices too. Delivery is directed by volume,
   pace, breath and pauses. No tag or prompt ever asks a voice to be sad, tender, moved or angry. The words, the cut
   and the silence around a line do the feeling.
5. **Perspective follows attention.** Loudness is where the character's attention is, not only where the source is.
   The Committee's red phone never moves off Ida's desk, but it recedes ring by ring as she turns away from it.
6. **Generate dry, place in our rooms.** Voices and close sounds are generated with no room and put into a location
   by one convolution per place (`mix_plan.md` §3). Everything in a place then shares one acoustic, which is what
   makes a place feel continuous. Only sounds that *are* the space (a hall's air, rain on a roof, a city across water)
   are generated in their perspective.
7. **Hard sound cuts belong to the story's hard events.** A machine stopping, a key committing, a broadcast dying,
   the rain ending. Every other cut is soft (§7).
8. **Silence is a sound with a shape** (§9). It is never filled with a drone, and never used twice for the same thing.
9. **Placelessness.** No real anthem, jingle, ringtone, siren, station ident or brand sound, and no real accent
   signature beyond the voice bible's neutral General American. Prompts to generators carry no artist, film or
   brand names.

## 2. The sound of the state (the pilot)

The state is Year One, maintained. Its sounds are old, mechanical, electrical and centralised, and each one comes
out of a speaker, a relay or a bell. None of it is ever made by a hand.

### 2.1 The state has a pitch: A
- **The Engine**, the machine in the vault under the Hall, runs its own 55 Hz supply: its hum is **A1** (55 Hz), with a
  strong **A2** (110 Hz) that carries on small speakers. Every **State Receiver** hums on the same A in every flat,
  and the tram's motor-generator whines on it in the street. Wherever the state's hardware is on, the room holds an A.
- **Why A:** it is the dominant of D, the pilot's home key. The Hall is a dominant held for 41 years, a question the
  nation is never allowed to answer. The ident resolves it every night (A–F♯–D), as a ritual. Nana's theme starts on
  the same A and goes somewhere else.
- **The A dies twice:** the tram's whine spins down in the street after "I died in the spring" (158.8), and the
  Engine's hum winds down to nothing when the ON AIR lamp goes out (186.4). After that the Hall has no pitch at all.
- **The dawn is E♭:** a half step above home (the Neapolitan, the "new colour") and a **tritone from A**, the farthest
  point from the state's note. The score voices it with a raised fourth (E♭ Lydian), so the old A is still inside the
  new chord, but as a colour and not a root: the Transmitter is still blinking over the warm windows.
- Build rule: every generated hum is **retuned** by resampling until its fundamental reads 55 Hz, and every whine
  until its strongest partial is an A (`sfx.json`, "treatment").

### 2.2 The Chime (the ident)
- Three struck notes, **A4, F♯4, D4** (5–3–1 in D major), on a small tuned chime bar with a soft mallet, recorded in
  Year One and heard off the ident film's **optical soundtrack**: narrow band, crackle, a trace of wow and flutter.
- It is one recorded strike, repitched by resampling to every note it ever plays, so the bell is literally the same
  object every time: A4–F♯4–D4 at the ident (0.5 s apart), D3 as a single toll under the title, the same three notes
  smeared across a thousand sets at 80.0 (the standby interval signal), fast and cold at 149.3, and at the end, B♭4
  and G4 in the new key with **the third note withheld**.
- The last chime (233.5) is the only time it is heard without the broadcast chain: a bare bell in air.

### 2.3 The State Hymn
- An invented chorale in D major, 60 BPM, for a small studio orchestra: warm strings, a soft brass choir of horns and
  flugelhorns, celesta doubling the tune, a quiet organ pedal. Only major triads, a stepwise tune, no tension:
  sweet, certain, and slightly too sweet.
- **It exists only inside the television.** It is broadcast music, heard only in 4:3 (the cold open, the fast ident at
  149.9, the alt tail). In the final Address it is **absent**, and the ear should miss it: the operator did not run
  the package. The living never get organ, brass or celesta (§5).

### 2.4 The PA (the Ministry's speaking clock)
- The countdowns ("Four minutes." "One minute." "Ten seconds.") are **a recording made in Year One**, a young woman's
  voice on a message repeater, played through the cast-iron **horn loudspeakers** on every pier. She has been saying
  these words at 20:56, 20:59 and 20:59:50 for 41 years. The PA is another dead voice that keeps talking.
- Every announcement is announced: the horns **open** half a second early (a relay thump and a rising amplifier hum),
  so the audience hears the state draw breath. The voice arrives from thirty horns at once, each at its own distance,
  smeared down the nave (`mix_plan.md` §3, HALL_PA). The three phrases come from one session and share one cadence.

### 2.5 The Committee
- It has no voice. It speaks in brass (the pneumatic post's rumble through the building), paper (onionskin) and one
  bell: **the Red Line**, a deep, harsh double bell on a 3 s cycle (1.2 s on, 1.8 s off) from 131.0 to 221.0. It is
  the loudest object in the film and it is never answered.

### 2.6 The Father (the copy)
- The frictionless voice (§1.3): an old man's timbre with none of an old body's noise. His breaths are removed, the
  gaps between his words are the broadcast carrier and not a room, his level never moves by more than a decibel, and
  his reverb is a **room with no walls** (a smooth tail with no early reflections: a space no one could stand in).
- The Engine does not speak, it **splices**. The template ("Good evening, my children.") and the learned sign-off
  ("Eat something warm before you sleep.") are the same recordings every night: the final Address reuses them
  sample for sample, and only the words Ida typed are new. When the Engine runs free (shot 12) it replays the cold
  open's own audio, joins showing, and collapses onto its most probable phrase.
- **One voice, four rooms.** In the Address the same take is heard in the studio (dry), the street (the Public
  Receiver's horns off wet facades), the Hall (thirty pier horns and a six-second vault) and Nana's television (a
  small cone in a steel cabinet). The voice is continuous; the room cuts with the picture. Her words travel through
  the whole city in his voice.

## 3. The sound of the living

### 3.1 Two clocks
- **The Air Clock** (the state's time): a 3 m slave clock high on the apse wall, stepped by the broadcast master's
  pulse. Each second is one hard **solenoid clack and steel knock**, dead regular, 40 m away and 20 m up, with the
  vault's 6 s tail and a faint slap off the Wall. The minute hand **clunks** when the minute turns (75.0 and 117.0 on
  screen). From "One minute" the master pulse itself becomes audible under each step, a low felt thud through the
  floor. It ticks from 21.0 and **stops at 180.0** (last tick 179.0), when the broadcast dies. The audience meets the
  stop as an absence: the next time we are in the Hall (186.0) there is no tick.
- **Nana's clock** (her time): a small wooden pendulum clock, wound by hand. A soft wooden *tick* and a slightly
  different *tock*, one beat a second, and a little **out of beat**: every tock lands 60 ms early, so her time limps
  like a heartbeat while the state's is perfect. It never stops.
- **Through the wire:** during both calls, Nana's clock is faintly audible in Ida's handset whenever we are with Ida
  (the far room travels down the line). In the first call it limps against the Air Clock. In the second call the Air
  Clock is dead, and **her clock is the only clock left in the Hall**. It is also under her voice in "Come home".

### 3.2 Two bells
- **The Red Line** (§2.5): the Committee's deep, harsh bell.
- **The civilian bell**: Nana's cream telephone and Ida's grey House Line are the same state model, so they ring with
  the **same small, bright bell** in the same cadence: a double ring (0.4 s on, 0.2 s off, 0.4 s on, 1.0 s off). The
  audience first hears it in Nana's room (87.5). When the House Line rings in the Hall after the broadcast (191.6),
  the bell of home sounds in the state's cathedral **before** we see the card that says NANA.

### 3.3 Breath and hands
- Ida's performance is mostly breath and hands: an exhale at the Proof, a murmur to a face she is touching, keys, a
  cord gripped, a thermos cap turning, and **the laugh in 42, heard and not seen**: a breath out through the nose that
  becomes one small laugh as the cap comes off and the steam rises.
- Every human sound is close and textured: skin, wool, enamel, bakelite, paper. Nothing human is ever reverberant
  except when a place makes it so.

### 3.4 Voices (the cast in `../../audio/pilot/casting.md`)
- **One voice per character, fixed for the whole series run of that character:** the same stock voice, settings and
  seed family, generated dry. A scene's lines for one speaker are generated in one request, so their energy matches.
- **Audio leads picture.** Dialogue is cast, recorded and locked to the 242 s timeline first. When Seedance resumes,
  every speaking take is driven by (or slipped to) this audio. Existing takes whose lips must be kept are converted
  with the voice changer (speech to speech), which keeps their timing and prosody and swaps in the cast timbre.
- **Accent:** neutral General American for every principal (the voice bible in `episodes/pilot/v2_jobs.json`).
- **Pronunciation is locked** where the model might drift: *Nana* is always /ˈnænə/.

## 4. Locations: sonic identities

Each place has a **bed** (what it sounds like when nothing happens), a **signature** (the one sound that names it),
a **voice treatment**, and a thing it must never contain.

| Place | Bed | Signature | Voices sit | Never |
|---|---|---|---|---|
| **The Hall** (nave, Wall, gallery) | vast still air; the Engine's A1/A2 hum breathing up through the floor grilles; rain on a roof 30 m up, muffled to a roar | the Air Clock's step with its 6 s vault tail and the slap off the Wall of tubes | close and dry at the desk, with the building only in the tail: a small voice in a big dark | footsteps of anyone but Ida; music inside the room; a warm sound that isn't hers |
| **Desk 4** (the console) | the Hall's bed, nearer: tube whine from the Proof, the terminal's faint high-voltage tick | relays (a legend lamp switching), the light pen's ring button, the teleprinter | Ida at 30–60 cm; her murmur gets one reflection off the Proof's glass | UI blips, synth beeps, anything digital |
| **Nana's flat** (14th floor, one room) | a small still room with a low ceiling; rain running on the outer pane; soup simmering in the corner | the limping wooden clock | warm, close, a short soft room with a strong early reflection off the low ceiling (the lid) | the Hall's reverb; any music from a radio |
| **The State Receiver** (her TV) | on: the A hum and a faint whistle, breathing with the standby card at 0.25 Hz; off: nothing, and the room is warmer for it | the carrier's breathing | the Father through a small cone in a steel cabinet, one metre away | a clean, full-range voice |
| **The phone line** | soft hiss and faint crackle, and the far room behind it (clock, rain, simmer) | the line opening: a hook-switch click and a faint bell ting | band-limited, carbon-grained, intimate when we are the listener | tinny sci-fi filtering; crosstalk |
| **The city across the canal** | rain wide and far on water and concrete; the canal lapping below | a tram bell far off; at 80.0 the standby chime from a thousand sets at once | (none) | traffic, sirens, horns, voices |
| **The tram street** | rain drumming on many umbrellas, water in the gutter, a silent crowd | the tram's motor-generator whine on A, and its death | the Father from the Public Receiver's horns, off wet stone facades: a slap and a long open tail | a single voice from the crowd |
| **Dawn** | no rain; still air; drips from gutters and railings; the canal at rest | windows opening, and a city of small conversations spilling out of them | walla through open windows across water | a car, a siren, a word from the state |
| **The broadcast** (4:3) | the carrier: a faint clean hiss and nothing else; the ident film adds optical crackle | the Chime; the Hymn (except in the Address) | the Father, frictionless; a room with no walls | breath, room tone, the clock, the rain |

## 5. Music (the pilot's spotting is in `../../audio/pilot/score.md`)

- **Two orchestras, never mixed.** The state has brass, organ and celesta, and it only plays inside the television.
  The living have an old upright piano, strings and woodwinds. No brass, organ or celesta ever plays for the living,
  and no piano ever plays for the state.
- **Nana's motif** (A–F–G–E–F–D, D minor, one note at a time on the upright piano) is withheld until the end: first
  heard at the sign-offs (stopping on E), interrupted by the dead air (A–F–G), completed only under "Come home", on
  "warm". The one exception is a single A at 137.7, when the machine offers her phrase back in her colour.
- **Where music does not play:** the Hall before the sign-offs, the whole first phone call, the Address from the
  first word to the last, the dead air, and the second call up to "Come home". Those scenes are scored by the
  building, the rooms and the weather.
- **No trailer grammar:** no risers, braams, sub hits, whooshes, pulses as music, or drum hits. When the pilot needs a
  build, a real thing builds (the Engine powering up, a unison of strings on the state's A).
- **Performed, not synthesized.** Every cue is generated as performed music with its sections landing on picture
  hits. Numpy may only play recorded samples at exact pitches (the Chime; a single piano note cut from a cue when a
  motif note has to land on a frame).

## 6. Loudness and dynamics

- **Delivery target (YouTube and streaming):** integrated **−16 LUFS** (±0.5), true peak **≤ −1.0 dBTP**, loudness
  range **12–16 LU**. YouTube turns loud masters down to −14 but never turns quiet ones up, so −16 keeps the film's
  range intact and still plays at a normal level. Measure with ffmpeg `ebur128` (`tools/audio/mix.py` already does).
- **Dialogue is the anchor.** In the final master, normal dialogue sits at **−17 LUFS short-term (±2)**, murmurs and
  whispers at −21, the PA at −19 (a public voice), the Father at −17 in the studio and −15 when the whole Hall speaks
  with him. Nothing else is levelled up to dialogue.
- **Range comes from the quiet, not from the loud.** The quiet passages (a room with nobody speaking, rain, a clock)
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
7. **Hard only on purpose:** the tape-stop (19.0), HALT (70.4), the Air Clock killing Nana's E (117.0), the commit key
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

Claude reads waveforms, spectra and loudness, not feelings. King listens for: whether the voices are the right
people (casting), whether the laugh in 42 is one small true laugh, whether the loop at 70 is frightening and not
comic, whether the dead air holds for six seconds without the audience thinking the file broke, and whether the
dawn swells without tipping into sentiment. Every handoff says so plainly.
