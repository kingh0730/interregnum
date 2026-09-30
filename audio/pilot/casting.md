# CONTINUITY: casting (voices)

Four speaking parts and a city. Every voice is cast once, recorded dry, and placed in its rooms by the mix
(`../../episodes/pilot/bible/sound.md` §3–§4, `mix_plan.md` §3). The lines, tags and timings are in `dialogue.json`.

## How to audition (for whoever runs the takes)

- **Engine:** ElevenLabs Eleven v4 TTS on fal. Required fields: `text`, `voice`, `stability`, `similarity_boost`,
  `seed`. If the endpoint also exposes them: `speed` as given below, `style` 0, `language_code` "en", and
  `previous_text` / `next_text` set to the neighbouring lines of the scene (continuity). Ask for WAV or PCM at 44.1 or
  48 kHz; MP3 only if nothing else is offered. Media stays in `work/pilot/audio/` (never committed).
- **If v4 quantizes stability like v3** (0.0 Creative, 0.5 Natural, 1.0 Robust), use the nearest: the Father and the
  PA Robust, Ida and Nana Natural.
- **Method:** run each part's audition line on the first choice and the alternates with the same seed, then on the
  winner with two more seeds. Judge on headphones and on a phone speaker, dry (no processing). Choose by the "listen
  for" list, never by which voice is prettiest.
- **Lock the recipe** (voice, settings, seed) in `dialogue.json` → `voices` once chosen. After that nothing changes
  between scenes; if a line misreads, change the seed for that line only and note it.
- **Tags are behaviour only:** [softly], [quietly], [whispering], [under her breath], [pause], [short pause],
  [long pause], [exhales], [breathes in], [laughs quietly], [clears throat]. No emotion words, ever.
- **Audio leads picture.** Once the lines are locked on the timeline, Seedance takes are driven by (or slipped to)
  them. For an existing take whose lips must be kept, use the voice changer on the take's own dialogue: it keeps the
  timing and prosody and swaps in the cast voice. Turn on background-noise removal if the endpoint has it.

---

## THE FATHER

The machine's copy of an old man, speaking to the nation. He is not performing: he is being played back.

| | |
|---|---|
| **Age** | reads as a man of 80 to 85, at his steadiest: the average of 41 years of speeches, with none of an old body's noise |
| **Timbre** | low baritone; warm, round chest resonance; soft consonants; no gravel, rasp, whistle or tremor |
| **Pace** | slow: 105–115 words a minute inside a line, long pauses between lines; every phrase finished; a gentle fall at the end of each sentence, never a rise |
| **Accent** | neutral General American, no region, no mid-Atlantic polish |
| **Must not be** | a trailer voice; a newsreader; a preacher's swell; a politician's rhetoric (no oratorical build, no stress on "my"); a folksy grandfather (no drawl, no chuckle); British; robotic; frail or tremulous; an impression of any real leader |
| **Direction** | "You have said this every night for forty-one years, and you mean it every time. Don't lean on any word." |
| **Stock voice** | first choice **Bill**; alternate **Brian** (smoother and younger: use him if Bill's texture fights the de-breathing) |
| **v4 settings** | stability 0.85 (Robust), similarity_boost 0.90, seed 4101, speed 0.92 |
| **After recording** | the Engraving chain: breaths removed, level held within ±1 dB, no room (`mix_plan.md` §4) |

**Audition line:**
> Good evening, my children. [long pause] The river rose in the night, and by morning it had gone back to its bed.
> [pause] Nothing is lost that is looked after. [long pause] Sleep safely.

It covers the greeting, a long sentence on one even line, an aphorism with authority but no rhetoric, and a sign-off
whose tenderness is only pace. **Listen for:** the same loudness on all four sentences; no rise at any ending; warm
vowels in "my children"; no smile and no sigh; the least breath noise.

## IDA

Twenty-seven, the night operator. Precise, exhausted, dryly funny, and she says less than anyone in the film.

| | |
|---|---|
| **Age** | 25–30 |
| **Timbre** | a low voice for a young woman; soft, slightly husky with tiredness; close and private, as if the microphone were a colleague at her elbow |
| **Pace** | economical: 130–150 words a minute, short phrases, clean falling endings, pauses before (not after) what matters |
| **Accent** | neutral General American |
| **Must not be** | bright or perky; "helpful assistant"; breathy or seductive; a narrator; theatrical; tearful. "How long?" does not crack or quiver: the break is in the silence after it, not in the voice. No uptalk, no fry as a mannerism |
| **Direction** | "Work voice and Nana voice are the same voice at two distances. Don't act the difference; just be closer." |
| **Stock voice** | first choice **River**; alternate **Sarah** |
| **v4 settings** | stability 0.50 (Natural), similarity_boost 0.80, seed 2701, speed 0.95 |

**Audition line:**
> It drifted again. [pause] Left ear. Three pixels. [short pause] I've got it. [long pause] [quietly] No. Don't wait
> up. [pause] I'll be late.

**Listen for:** a low, unforced register; the technical half flat and exact, the private half nearer and softer with
no change of "feeling"; every ending falling; a breath before "No" that sounds like a person, not a sample.

## NANA

Eighty-two. She has watched the Evening Address every night for 41 years, and for the last two months she has
watched it for Ida. Warm, unfoolable, amused.

| | |
|---|---|
| **Age** | 78–85 in the timbre, not in the performance |
| **Timbre** | light and a little thin, warm in the middle; a small voice that carries because it is calm; a smile you can hear in the vowels, never a laugh unless the text asks for one |
| **Pace** | easy and even, 120–135 words a minute; she never hurries and never drags |
| **Accent** | neutral General American with an older speaker's rounder vowels |
| **Must not be** | a cartoon grandmother (no wobble, crackle or sing-song); frail or ill; breathy; sweet; British or Southern; a narrator's velvet; younger than about 70 |
| **Direction** | "You knew before she did. You are not surprised by anything she says tonight." |
| **Stock voice** | the stock set has no elderly woman. **Cast from the ElevenLabs voice library by voice ID** (the fal `voice` field takes an ID): shortlist three American women over 75 against this table. Stock fallback only if none passes: **Matilda**, at speed 0.9, with the "eighty" chain (a 4.5 Hz, ±6-cent tremor on sustained vowels and a −2 dB shelf above 6 kHz; `mix_plan.md` §4) |
| **v4 settings** | stability 0.50 (Natural), similarity_boost 0.85, seed 8202, speed 0.92 |

**Audition line:**
> You never eat when you work. [pause] I know. I know. [laughs quietly] Put the kettle on when you get in. [short
> pause] It's cold out, love.

**Listen for:** age in the colour of the voice with no performed frailty; one small real laugh, not a chuckle;
"love" said as plainly as "kettle"; the smile under "I know. I know."

## THE PA ANNOUNCER

The Ministry's speaking clock: a young woman's voice recorded on a message repeater in Year One and played through the
Hall's horn loudspeakers ever since. She never ages.

| | |
|---|---|
| **Age** | early 30s, and forever so |
| **Timbre** | clear, mid-range, clean onsets; trained public-service diction |
| **Pace** | slow and measured, about 100 words a minute; every syllable completed; the same small fall on every last word |
| **Accent** | neutral General American, precise but not affected |
| **Must not be** | a modern transit or airport voice; a smart assistant; a sci-fi computer; seductive; menacing; cheerful; uptalk |
| **Direction** | "Read the time. Nobody you are speaking to is a person." |
| **Stock voice** | first choice **Sarah**; alternate **Matilda** (if Nana comes from the library) |
| **v4 settings** | stability 0.90 (Robust), similarity_boost 0.85, seed 1001, speed 0.90 |
| **After recording** | tape of Year One, the horns, the nave (`mix_plan.md` §3, HALL_PA) |

**Audition line:**
> Eight minutes. [long pause] Five minutes. [long pause] Thirty seconds. [long pause] Operators to your desks.

**Listen for:** the identical contour on the three countdowns (they must be interchangeable); clean t and s; no warmth
added and no threat.

## THE CITY (walla at dawn)

Kept, because the ending needs a city talking to itself: "Tomorrow, you'll have to talk to each other," answered.
Nine ordinary people at open windows, each talking to one other person, quietly. Two lines surface; the rest stay
below intelligibility (`dialogue.json` W01–W10).

| | |
|---|---|
| **Who** | varied ages and timbres, all ordinary: a young woman and her father at one window; neighbours across a courtyard; a couple; someone alone on a phone |
| **Pace** | conversational, unhurried, no raised voices |
| **Accent** | General American (the murmur is filtered to unintelligibility, but the two surfacing lines must be clean) |
| **Must not be** | a crowd, a cheer, a protest, a chant, laughter, singing, anyone performing; none of the principals' voices |
| **Stock voices** | "What happens now?": **Jessica** (quietly). "I don't know.": **Roger** (after a breath). Murmur: **Eric, Chris, Will, Liam, Laura, Aria**, plus **Brian** only if he is not the Father |
| **v4 settings** | stability 0.50, similarity_boost 0.75, seeds 3001–3010 (one per line) |

**Audition:** the pair only, back to back in one room: "[quietly] What happens now?" / "[exhales] I don't know."
**Listen for:** a daughter and a father in the same kitchen at six in the morning; the answer honest, not sad.

---

## Cast summary

| Part | Voice | Alternate | Stability | Similarity | Seed | Lines |
|---|---|---|---|---|---|---|
| THE FATHER | Bill | Brian | 0.85 | 0.90 | 4101 | D01–D04, D06 (new fragment), D17–D21, D27–D28 (reused audio) |
| IDA | River | Sarah | 0.50 | 0.80 | 2701 | D05, D08, D10, D12, D22, D24, V01–V04 |
| NANA | library ID | Matilda + chain | 0.50 | 0.85 | 8202 | D11, D13, D14, D23, D25, D26, V05 |
| PA | Sarah | Matilda | 0.90 | 0.85 | 1001 | D09, D15, D16 |
| CITY | Jessica, Roger, six more | — | 0.50 | 0.75 | 3001–3010 | W01–W10 |
