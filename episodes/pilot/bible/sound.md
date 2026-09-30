# Sound bible: the pilot

The pilot's world in sound. The series rules it follows, with the pilot's worked examples, are in
`../../../bible/sound.md`. It sits beside this folder's visual files (what things are, how they are drawn and shot)
and answers the showrunner's note on the v2 soundtrack: the voices and the rest of the audio had
brilliant ideas but were "not masterpiece-level". The diagnosis, and what this bible does about each part:

| Failure in v2 | Why it failed | The rule that replaces it |
|---|---|---|
| Voices | Seedance invented a new voice per clip, each with its own baked-in room; the PA was macOS `say` | One cast voice per character, recorded dry, placed in rooms we build (§3; `bible/sound.md` §1.6). Dialogue leads the picture (§3.4) |
| Score | A numpy synthesizer can make tones but not music | Music is performed music (ElevenLabs Music). Numpy only plays recorded samples at exact pitches (§5) |
| Foley | Synthesized noise pretending to be rain, paper, bells | Every acoustic sound is a recording with a material, a space and a microphone. Numpy makes only what is electrical (`bible/sound.md` §10) |
| Mix | Cut hard with the picture: no J/L cuts, no continuous rooms, silence not designed | Every place owns a continuous bed; cuts are soft unless the story is hard; silence has a grammar (`bible/sound.md` §7–§9) |

Companion files for the pilot: `../../../audio/pilot/casting.md`, `dialogue.json`, `score.md`, `score_cues.json`,
`sfx.json` and `mix_plan.md`. The v1 temp-score plan (`../../../audio/pilot/cues.md`) is superseded where they differ.

---

## 1. Series principles

Moved to the series rules: `../../../bible/sound.md` §1. The pilot's examples are kept there.

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

### 3.4 Voices (the cast in `../../../audio/pilot/casting.md`)
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

## 5. Music (the pilot's spotting is in `../../../audio/pilot/score.md`)

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

Moved to the series rules: `../../../bible/sound.md` §6. The pilot's examples are kept there.

## 7. J and L cuts

Moved to the series rules: `../../../bible/sound.md` §7. The pilot's examples are kept there.

## 8. Room tone and continuity

Moved to the series rules: `../../../bible/sound.md` §8. The pilot's examples are kept there.

## 9. The grammar of silence

Moved to the series rules: `../../../bible/sound.md` §9. The pilot's examples are kept there.

## 10. Making the sounds (generation rules)

Moved to the series rules: `../../../bible/sound.md` §10. The pilot's examples are kept there.

## 11. What Claude cannot judge

Moved to the series rules: `../../../bible/sound.md` §11. The pilot's examples are kept there.

