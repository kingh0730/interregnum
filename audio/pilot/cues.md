# CONTINUITY: sound, temp score, dialogue, Suno cue sheet

> **Superseded for the ElevenLabs pass** by `../../episodes/pilot/bible/sound.md` and, in this folder, `casting.md`,
> `dialogue.json`, `score.md`, `score_cues.json`, `sfx.json` and `mix_plan.md`. Kept as the record of the v1 temp mix.

Everything in the v1 soundtrack can be made with numpy (plus `say` and ffmpeg for the voices). Build it as stems,
mix at the end, and keep all `.wav` in `work/pilot/audio/` (they are git-ignored). Times are **absolute seconds in
the main cut** unless marked "shot +". Shot in-points are in `episodes/pilot/episode.md`.

## 1. Global

- 48 kHz, 32-bit float while working and 24-bit for the final wav. **Tempo 60 BPM = the clock**: one beat is one
  second and a bar of 4/4 is 4 s, so bar *n* starts at 4(*n*−1) s. Every picture cut is on a whole second.
- **Keys:** the state is **D major**, Nana is **D minor / F major**, and the new is **E♭ major** (Neapolitan to D:
  the "new color" in sound). Tuning is A4 = 440 Hz.
- **Stems:** `dx` (dialogue), `fx` (SFX), `amb` (ambience), `mx` (temp score), `walla`. The hall clock ticks live in
  `fx`.
- **Loudness:** −16 LUFS integrated and −1 dBTP for the reel. Dialogue sits around −20 LUFS short-term, and music
  under dialogue at −30 to −26 dBFS RMS. A −40 dBFS room tone runs under everything, **except** the three true
  silences (70.4–71.0, 149.0–149.3, and the dead air 180.0–186.0, which has only broadcast hiss at −50 dB).
- **Diegetic clocks:** the **hall clock** ticks on every whole second from 21.0 to 179.0, audible in hall-located
  shots only (05–14, 17, 19, 22–27, 32; not in the city, Nana's room or the broadcast). It **stops at 180.0**, when
  the Father closes his eyes, and does not return. **Nana's clock** (wooden, softer, alternating tick and tock) ticks
  on the whole second in every Nana shot, including after the Address: her time keeps going.

## 2. Instruments (synthesis recipes)

| Name | Recipe |
|---|---|
| **BELL** (the Chime) | FM: `sin(2πft + I(t)·sin(2π·1.4f·t))`, index `I(t)=3.2·e^(−t/0.6)`, amp env 2 ms attack then `e^(−t/2.2)`. Add a partial at 2.76f × 0.2 decaying `e^(−t/0.7)`. Detune L/R ±3 cents |
| **HYMN** (the state's pad) | Organ-like additive (partials 1, 2, 3, 4 at 1, .5, .25, .12) per note, 0.3 s attack, 1.0 s release, chorus (3 voices ±6 cents), LPF 3 kHz |
| **PAD** (warm or dark) | 3 band-limited saws per note (−7/0/+7 cents; additive, 1/k, up to 8 kHz) → one-pole LPF (warm 1.2 kHz, dark 350 Hz), 1.5–2 s attack and release, plus a sine an octave up at −12 dB for the warm version |
| **PLUCK** (Nana's piano) | As in `tools/audio/synth_reference.py`: additive partials h = 1..6, amp `1/h^1.3`, decay `e^(−t(2.2+1.8h))`, inharmonicity `f·h·(1+0.0004h²)`, 5 ms hammer noise (LPF 3 kHz) at −18 dB, small-room reverb |
| **SUB HIT** | Sine with pitch sweep `f(t)=38+42·e^(−t/0.12)` Hz, amp `e^(−t/0.9)`, 3 ms click on top |
| **PULSE** | 50 Hz sine, 180 ms, amp `e^(−t/0.08)` plus a soft click. Gain ramps from −24 to −12 dB across its cue |
| **DRONE** (the hall) | D1 sine (36.7 Hz) at −18 dB + a dark PAD on D2+A2 (LPF 350 Hz ±80 Hz LFO at 0.05 Hz) + a "cold shimmer" of sines at D6/E6/A6 with 0.3–0.7 Hz tremolo at −42 dB |
| **BRASS** | Saw stack (D2, A2, D3), LPF opening 200→1200 Hz over the swell, 2 s attack |
| **RISER** | White noise → band-pass with center sweeping 300→6000 Hz (exponential), Q 2, gain −40→−14 dB, plus a sine gliding D3→D5 at −30 dB |
| **HALL REVERB** | IR = exponentially decaying stereo noise, RT60 3.5 s (6 s for the "huge" variant), 40 ms predelay, LPF 5 kHz |
| **ROOM REVERB** | RT60 0.4 s, LPF 7 kHz |

## 3. Motifs

- **THE CHIME** (the state): BELL **A4 – F♯4 – D4** (5–3–1 in D major), 0.5 s apart (0.3 s apart in the fast
  version). Heard at the ident (0.5 s), in the city's stand-by (smeared), cold at 149.3, in E♭ at the end with the
  **third note withheld**, and whole and warm in the alt stinger.
- **NANA'S THEME:** PLUCK **A4 – F4 – G4 – E4 – F4 – D4** (5–3–4–2–3–1 in D minor), one note per beat. It starts on
  the same A as the chime, then goes minor. **It never completes until "Come home."** 1:49 stops on E4, and 2:57 is cut
  off after G4 by the dead air. 3:30 finally resolves to D.
- **THE AMBER NOTE:** a single PLUCK A4 at 137.7 s, when the machine completes Nana's phrase. It is the only warm
  note in the countdown.
- **THE LOOP:** the Father's voice multiplying (dialogue stem; see §6).
- **THE RED PHONE:** a 3-second cycle from 131.0 to 221.0 (§5). It is the Committee's only voice.

## 4. Temp score: cue map with hit points

### 1M1 "The Evening Address" (0.0–19.4) · D major · bars 1–5
| Bar.beat | Time (s) | Event |
|---|---|---|
| 1.1.5 | 0.5 / 1.0 / 1.5 | CHIME A4, F♯4, D4 (synced to the emblem's circle, flame and base line) |
| 1.2–2.1 | 1.0–4.8 | HYMN D major (D3 F♯3 A3 D4) swells from nothing to −24 dB |
| 2.2 | 5.0 | HYMN progression under the Father, −26 dB: **D** 5.0–8.5 (D3 F♯3 A3 D4), **G** 8.5–12.0 (G2 D3 G3 B3), **D** 12.0–15.5, **A** 15.5–19.0 (A2 E3 A3 C♯4) |
| 5.4 | 19.0–19.4 | **TAPE-STOP** on the whole mix (music and dialogue): playback rate `r(t)=1−(t/0.4)²`, phase-integrated, then silence |

### 1M2 "Night Desk" (21.0–78.0) · D minor · bars 6–20
| Bar.beat | Time (s) | Event |
|---|---|---|
| 6.2 | 21.0 | Hall clock begins (in `fx`) |
| 6.3 | 22.0 | DRONE fades in over 3 s |
| 11.2–12.2 | 41.0–45.4 | RISER (short version, 4.4 s) under the racing archive |
| 12.2.6 | **45.6** | **SUB HIT** (LAST LIVE CAPTURE). DRONE ducks −15 dB for 45.6–47.1, then recovers over 1 s |
| 12.2.9 | 45.9–49.9 | Flatline: a steady 1 kHz sine at −32 dB (fx) |
| 12.3–13.2 | 46.2–49.2 | 212 "generated" clicks (fx), accelerating and synced to the JS thumbnails |
| 13.2.5 | 49.5 | PLUCK D2, low, 4 s ring |
| 13.3.3 | 50.3 | Title BELL on D3 alone (decay 4 s) |
| 14.3–14.4 | 54.0–56.5 | Pneumatic rumble, whump and hiss (fx, §5) |
| 15.4–16.4 | 59.0–63.0 | Dark PAD swell D2 (LPF 500 Hz, 2 s attack) under the order |
| 16.1.8 | 60.8 | Soft PULSE (the last line of the slip, "THE OPERATOR ANSWERS FOR CONTENT") |
| 16.4.3–18.3.4 | 63.3–70.4 | The Loop (dialogue stem). DRONE and PAD **glide up a semitone D→E♭** from 66.5 to 70.4 |
| 18.3.4 | **70.4** | **HARD STOP**: mute every stem (including the clock) until 71.0 |
| 18.4 | 71.0 | Clock and DRONE return, DRONE −3 dB |
| 19.4 | 75.0 | Heavy clock tick (+4 dB); PA at 75.3 |
| 20.2 | 77.0–78.0 | DRONE fades out (cut to the city) |

### 1M3 "The Warm Window" (80.0–117.0) · F major / D minor · bars 21–30
| Bar.beat | Time (s) | Event |
|---|---|---|
| 21.1 | 80.0 / 80.5 / 81.0 | City stand-by chime: CHIME through a 4 s reverb, LPF 2 kHz, −28 dB (many televisions far away) |
| 21.3 | 82.0 | Warm PAD fades in over 3 s, −30 dB: **F** 82–92, **C/E** 92–100, **Dm** 100–109 |
| 26.3.6 | 102.6 | PLUCK A4 (theme note 1, after Ida's question) |
| 27.1.9 | 104.9 | PLUCK F4 (note 2, between "For the ending." and "Eat something warm, love.") |
| 28.2 | 109.0 | `signoffs.txt`: PAD **Dm** 109–111, **B♭** 111–113, **C** 113–117 |
| 28.3–29.2 | 110.0 / 111.0 / 112.0 / 113.0 | Theme A4, F4, G4, **E4 held** through 117 (unresolved) |
| 30.2 | 117.0 | Cut (the next cue takes over) |

### 1M4 "Night 212" (117.0–149.0) · D · bars 30–38
| Bar.beat | Time (s) | Event |
|---|---|---|
| 30.2 | 117.0 | PULSE on every tick, ramping −24→−12 dB through 149.0. PA at 117.3 |
| 30.4 | 119.0 | DRONE returns, adding an A1 fifth and the shimmer |
| 31.1–32.2 | 120.0–125.0 | BRASS swell (peak 124.5) |
| 32.2–34.2 | 125.0–133.0 | Keystrokes (fx, JS-synced). Ghost-text "tink" at 125.9 |
| 33.1 | **128.0** | SUB HIT, dull (the "d" of "died"). NO PREDICTION blip (square 110 Hz, 80 ms) at 128.8 |
| 33.4 | **131.0** | **Red phone starts** (fx, §5) |
| 34.2–38.2 | 133.0–149.0 | RISER (16 s) |
| 35.2.7 | **137.7** | **THE AMBER NOTE**: PLUCK A4, dry and close, −20 dB |
| 36.1 | 140.0 | TAB thock (fx) |
| 36.3.6 | 142.6 | SCRIPT LOCKED confirm (two soft sine blips D5–A5) |
| 37.2.3 | 145.3 | PA "Ten seconds." |
| 38.2 | **149.0** | **HARD CUT**: every stem silent until 149.3 |

### 1M5 "Ident / The Address" (149.0–188.0) · bars 38–47
| Bar.beat | Time (s) | Event |
|---|---|---|
| 38.2.3 | 149.3 / 149.6 / 149.9 | Fast CHIME, **cold** (LPF 3 kHz, dry) + a short HYMN D (LPF 1 kHz) 149.9–151.8 |
| 39.1–44.3 | 152.0–174.8 | **No music.** Only voices and ambience |
| 45.1 | 176.0–180.0 | Warm PAD F(add9) at −38 dB |
| 45.2.6 / 45.3.4 / 45.4.2 | 177.6 / 178.4 / 179.2 | Theme A4, F4, G4, then **cut off** |
| 46.1 | **180.0** | **Dead air.** All music off; the hall clock stops (last tick 179.0). Only broadcast hiss at −50 dB |
| 47.3.4 | 186.4 | Relay click; the hall hum winds down 55→20 Hz over 1.4 s (fx) |

### 1M6 "Come Home" (188.0–242.0) · F → D minor → E♭ · bars 48–61
| Bar.beat | Time (s) | Event |
|---|---|---|
| 48.1 | 188.0 | No music: the red phone alone in the silence |
| 50.4.5 | 199.5 | Warm PAD in at −30 dB: **F** 199.5–205.0, **C/E** 205.0–210.0 |
| 53.3.2–54.3.4 | 210.2 / 211.0 / 211.8 / 212.6 / 213.4 / **214.4** | **Theme resolved** (rubato, 0.8 s per note): A4, F4, G4, E4, F4, **D4**. The D lands just after "warm" ends. PAD **F** 210–211.8, **C/E** 211.8–213.4, **Dm** 213.4–217 |
| 54.4.4 | 215.4 | PLUCK D5 (a high echo) |
| 55.1–56.4 | 217.0–223.0 | PAD **B♭**, fading −30→−40 dB |
| 56.4 | **223.0** | **Dawn: E♭maj9** (E♭3 B♭3 D4 F4 G4), warm PAD swelling −36→−24 dB through 229 |
| 57.3–59.2 | 226.0–233.0 | High shimmer: noise band-passed 6–10 kHz, slowly rising, plus sines B♭5/D6/F6 with tremolo, −34 dB |
| 59.2 | 233.0 | Music thins to E♭+B♭ (open fifth), −30 dB |
| 59.2.5 / 59.3 | 233.5 / 234.0 | CHIME in E♭: **B♭4, G4** … and the **E♭4 at 234.5 is withheld** (silence where it should land) |
| 60.3 | **238.0** | Series title: SUB HIT on E♭1 + E♭sus2 (E♭3 F3 B♭3 E♭4, HYMN timbre) at −22 dB, fading 239–242 |
| 61.3 | 242.0 | End |

### 1M7 "Night 213" (alt tail, 242.0–252.0)
| Time (s) | Event |
|---|---|
| 243.3 / 243.8 / 244.3 | CHIME **A4, F♯4, D4**, whole and warm: the old key returns |
| 243.8–246.5 | HYMN D major, −26 dB |
| 246.8 / 249.6 | FATHER lines (§6) |
| 251.6 | Cut to black; silence to 252.0 |

## 5. Ambience and SFX by scene

| Scene (time) | Ambience | SFX (time) |
|---|---|---|
| Cold open (0–22) | Broadcast studio tone: soft hiss −48 dB, faint 50 Hz hum | Glitch zap: a 0.12 s digital crackle (bit-crushed noise) at 19.0. Tape-stop 19.0–19.4. Mouse click 20.6. Hall clock from 21.0 |
| Hall (22–77, 117–149, 168–174, 186–223) | Hall tone: 55 Hz hum plus harmonics at −38 dB, air noise LPF 1 kHz; rain on a high roof (pink noise LPF 2 kHz + HALL REVERB, −40 dB) | Distant pneumatic hiss 27.5. UI blips (sine plucks D5/E5/F♯5/A5, −30 dB, 60 ms) at each LOCKED/OK in shot 06 (32.3, 33.0, 33.6, 34.2, 34.8, 35.4). Stylus clicks 31.05 and 32.2. Stylus taps 38.5 and 39.7. Breath 40.2. Archive riser, sub and flatline (§4). **Pneumatic:** rumble 54.0–55.3 (brown noise LPF 300 Hz, filter rising, panned L→C); **whump/clank at 55.35** (60 Hz sub with `e^(−t/0.15)` + partials 520/1370/2210/3140 Hz decaying 0.6/0.35/0.2/0.12 s); hiss 55.45–56.5 (noise HP 3 kHz). Paper crinkle 57.0–57.6 (10 band-passed 2–6 kHz bursts of 20–80 ms). Keystrokes: 8 ms noise burst BP 1–4 kHz + 180 Hz thock `e^(−t/0.03)`, ±3 dB and ±5 % pitch jitter |
| **Red phone** (131.0–221.0) | — | An electromechanical bell: two bells at 1080 and 1350 Hz with partials ×1, ×2.4, ×3.9 (decay 0.3 s), struck by a 20 Hz clapper impulse train. **Ring 1.2 s, silence 1.8 s, 3 s period** starting 131.0 (131, 134, 137 … 221). Audible **only in hall-located shots**: close and dry in 36 and 38; through HALL REVERB and −12 dB in 24–27, 32, 40, 42; far away (−20 dB, huge reverb) in 43. Muted during the 149.0 cut |
| City (77–84) | Rain, wide stereo: pink noise BP 400–9000 Hz + droplet transients (Poisson 40/s, HP 2 kHz); canal lapping (LPF noise, slow AM) | Tram bell (BELL at 1400 Hz, ratio 2.1, index 2, decay 1.2 s) at 79.0 and 79.6, distant (LPF 3 kHz + reverb). City stand-by chime 80.0 (§4) |
| Nana's room (84–109, 174–180, 198–210) | Room tone −44 dB; rain on glass (more droplet transients, LPF body); **Nana's wooden clock** every whole second (900/800 Hz alternating tick and tock, `e^(−t/0.015)`, ROOM REVERB); TV hum (50 Hz + a faint 15.6 kHz whine at −56 dB) **only while the TV is on (before 180)**; pot simmer (bubbling: random low-passed impulses) | **Nana's phone:** a softer double ring (bells at 800/1000 Hz, 25 Hz clapper, 0.4 s on, 0.2 s off, 0.4 s on, then 2 s off) at 87.5 and 89.5; handset lift click 89.9 |
| The call (90–109, 195–217) | Phone-line hiss bed (−52 dB) under every call shot | Ida's breath and laugh-sob in 42: soft breath noise (BP 300–3000 Hz, 0.4–0.8 s envelopes) at 210.6, 211.2, 214.8 and 215.6, with one shaky voiced laugh (a 150 Hz buzz under the noise) at 215.0 |
| Scroll (109–117) | — | Soft trackpad ticks (1 ms clicks at the JS scroll rate, −40 dB) |
| Street (157–163) | Rain (as the city) + street splashes; tram idle hum (100 Hz + 200 Hz with motor whine) **157.0–158.8, then cut dead** | — |
| Dead air (180–186) | Broadcast hiss −50 dB only | — |
| Lamp off (186–188) | — | Relay click 186.4 (2 ms noise + 2 kHz ping); hum wind-down 186.4–187.8 |
| Ida's phone (192–195) | — | Ringtone: marimba-like PLUCK (partials 1, 4, 9.2, fast decays), **A4 then D5, 0.25 s apart**, at 192.1 and 193.6 |
| Empty hall (217–223) | Hall tone at −6 dB (the power is off now), roof rain | Red phone, far away (see above) |
| Dawn (223–233) | **No rain.** Gutters dripping (sine blips 2–4 kHz with a pitch drop, 20 ms, ~3/s, plus a low plop); the canal still | First tram bell 229.5 (far away). Birds: FM chirps (3–6 kHz sweeps, 60–120 ms), 2–3 birds from 227.0, sparse. **Walla** 224–236 (§7) |
| Titles (233–242) | Walla fades out 233–236; then only music | — |
| Alt (242–252) | Broadcast studio tone | — |

## 6. Dialogue

Render every line separately:

```
say -v <Voice> -r <rate> -o work/pilot/audio/vo/<id>.aiff "<line>"
```

Convert to 48 kHz mono wav, then process as below. Measured on this machine: `Daniel` at rate 135 speaks
"Tomorrow, you'll have to talk to each other." in about 3.0 s, and `Moira` at rate 150 speaks "Since he started
telling me to eat." in about 2.6 s. Every line fits its shot. **If a render overruns** the time left in its shot,
first raise the rate by up to 10 %. Only if it still overruns, extend the shot by a whole second and shift later hit
points.

**Processing chains** (ffmpeg `-af`):
- **FATHER base:** pitch down 2 semitones, keeping duration: `asetrate=<SR>*0.8909,aresample=48000,atempo=1.1225`
  (use the file's own sample rate for `<SR>`). Then `highpass=f=90,lowpass=f=7000,equalizer=f=2500:t=q:w=1:g=3,acompressor=threshold=-20dB:ratio=3`.
  Then one variant:
  - `BROADCAST`: ROOM REVERB (0.4 s) at −20 dB wet.
  - `LOOP`: dry.
  - `STREET`: `bandpass=f=1200:width_type=h:w=3800` + a 350 ms slapback at −8 dB + a 3.5 s reverb at −10 dB wet.
  - `HALL`: `lowpass=f=6000` + HALL REVERB (6 s) at −8 dB wet.
  - `TV`: `bandpass=f=1500:width_type=h:w=4700` + ROOM REVERB at −22 dB.
- **IDA:** `highpass=f=80`, plus ROOM REVERB at −24 dB in the hall. `VO-MURMUR` (line D05 only): rate 150, −6 dB,
  `lowpass=f=6000`, dry and close.
- **NANA:** `highpass=f=70`, ROOM REVERB at −22 dB. `PHONE` (D26 only):
  `highpass=f=300,lowpass=f=3400`, soft clip (`asoftclip`), with the line hiss under it.
- **PA:** `highpass=f=400,lowpass=f=3500,asoftclip`, 120 ms slapback, HALL REVERB (4 s) at −8 dB wet.

| ID | Shot | At (s) | Speaker | Voice, rate | Line (exact) | Chain |
|---|---|---|---|---|---|---|
| D01 | 02 | 5.6 | FATHER | Daniel, 135 | Good evening, my children. | BROADCAST |
| D02 | 02 | 8.0 | FATHER | Daniel, 135 | The harvest is in. The sea is calm. | BROADCAST |
| D03 | 03 | 12.6 | FATHER | Daniel, 135 | I am well. | BROADCAST |
| D04 | 03 | 15.0 | FATHER | Daniel, 135 | Eat something warm before you sleep. | BROADCAST |
| D05 | 06 | 31.0 | IDA (V.O.) | Samantha, 150 | Hold still. | VO-MURMUR |
| D06 | 12 | 63.3 | FATHER (generated) | Daniel, 150 | Good evening, my children. The harvest is in. The sea is calm. I am well. Sleep safely; I am watching over you. I am well. The sea is calm. | LOOP |
| D07 | 12 | 66.5–70.4 | FATHER ×N | Daniel, 150 | I am well. | LOOP choir (below) |
| D08 | 13 | 72.0 | IDA | Samantha, 160 | No, you're not. | IDA hall |
| D09 | 14 | 75.3 | PA | Karen, 165 | Four minutes. | PA |
| D10 | 17 | 90.5 | IDA | Samantha, 165 | Nana. Don't wait up tonight. | IDA hall |
| D11 | 18 | 94.4 | NANA | Moira, 150 | I always wait up. He's on soon. | NANA |
| D12 | 19 | 99.6 | IDA | Samantha, 165 | Why do you still watch him? | IDA hall |
| D13 | 20 | 103.5 | NANA | Moira, 150 | For the ending. | NANA |
| D14 | 20 | 106.2 | NANA | Moira, 145 | Eat something warm, love. | NANA |
| D15 | 22 | 117.3 | PA | Karen, 165 | One minute. | PA |
| D16 | 27 | 145.3 | PA | Karen, 165 | Ten seconds. | PA |
| D17 | 29 | 152.8 | FATHER | Daniel, 135 | Good evening, my children. | BROADCAST |
| D18 | 30 | 157.8 | FATHER | Daniel, 130 | I died in the spring. | STREET |
| D19 | 31 | 163.8 | FATHER | Daniel, 130 | I'm sorry I stayed so long. | BROADCAST |
| D20 | 32 | 168.6 | FATHER | Daniel, 135 | Tomorrow, you'll have to talk to each other. | HALL |
| D21 | 33 | 174.8 | FATHER | Daniel, 135 | Eat something warm before you sleep. | TV |
| D22 | 38 | 195.7 | IDA | Samantha, 165 | Nana— (render "Nana, I", keep 0.5 s, 30 ms fade) | IDA hall |
| D23 | 39 | 198.6 | NANA | Moira, 145 | I know, love. | NANA |
| D24 | 40 | 202.8 | IDA | Samantha, 150 | How long? | IDA hall |
| D25 | 41 | 205.6 | NANA | Moira, 145 | Since he started telling me to eat. | NANA |
| D26 | 42 | 211.5 | NANA (V.O.) | Moira, 145 | Come home. The soup's still warm. | PHONE |
| D27 | 46 | 246.8 | FATHER | Daniel, 135 | Good evening, my children. | BROADCAST |
| D28 | 46 | 249.6 | FATHER | Daniel, 135 | I am well. | BROADCAST |

**The Loop choir (D07):** render "I am well." once (Daniel, 150, LOOP chain). Place copies on onsets that start
every 0.33 s at 66.5 and accelerate to every 0.07 s by 70.0 (about 30 copies). Detune each copy randomly by ±15–40
cents (resample), pan it randomly within ±0.8, and low-pass the later copies progressively (8 kHz → 3 kHz). The stack
rises +6 dB overall. **Mute everything at 70.4.** D06 continues underneath until 66.5 and is then buried by the copies.

**Subtitles:** generate `renders/pilot/continuity_v1.srt` from this table: each line starts at its time and ends at
the end of the render + 0.3 s. The PA lines are italic, and D06/D07 get a single subtitle, "*I am well. I am well. I
am well…*". Styles are in `episode.md`.

## 7. Walla (224–236): a city talking to itself

About 20 voices, 3 phrases each. Scatter random starts from 224.0 to 233.0, with density rising (few at first,
overlapping by 229). Voices: `Samantha, Daniel, Moira, Karen, Tessa, Rishi, Aman, Tara, Albert, Fred, Kathy, Ralph,
Junior, "Eddy (English (US))", "Flo (English (US))", "Reed (English (UK))", "Sandy (English (UK))",
"Shelley (English (UK))", "Rocko (English (US))", "Grandma (English (US))"`, at rates 150–180. Phrases: *Are you
awake? · Did you see it? · I know. · Come over. · I'll put the kettle on. · What happens now? · I don't know. · Me
neither. · Call your mother. · Are you there? · Yes. I'm here. · Open the window. · Let's talk. · I can't sleep.*

Each voice gets `lowpass=f=2500`, a room reverb (RT60 0.8 s), a random pan, and a gain of −36 to −28 dB. The whole
walla bus goes through a 1.5 s reverb at −6 dB wet and is **low-passed at 1.8 kHz** so that no single word is
intelligible, except "What happens now?" at 230.2 and "I don't know." at 231.4, left slightly clearer (LPF 3.5 kHz,
−26 dB). The bus rises from −40 dB at 224 to −24 dB at 232, then fades out 233–236.

## 8. Mix order

1. `dx` (with processing) → 2. `fx` (clock, phones, UI, pneumatics, the synced JS sounds) → 3. `amb` → 4. `mx`
(temp score) → 5. `walla`.

Duck `mx` by 4 dB under every dialogue line (40 ms attack, 300 ms release), but **not** the amber note and not the
theme resolution at 214.4. Apply the three true silences to every stem. Export `work/pilot/audio/mix_main.wav` (0–242)
and `mix_alt.wav` (0–252), plus each stem, for v2 re-mixing.

---

## 9. Suno cue sheet (v2)

King generates these in Suno on a paid plan: that is required for commercial use of downloads (see
`docs/strategy.md`). Make 2–4 takes of each, download them, and drop them into `audio/music/pilot/`. Claude cuts the
best take to picture: Suno won't hit these hit points, so expect to nudge cuts by ±1 s and re-time the rises. Seedance
dialogue and effects in v2 are generated **without music**. No artist names go in the prompts (Suno rejects them); the
descriptions carry the style.

| Cue | In–out | Length to generate | Replaces | Must-hit points |
|---|---|---|---|---|
| **S1 The Evening Address** | 0:00–0:19, and the bells again at 2:29 and 4:03 (alt) | 30–40 s | 1M1, the 1M5 ident, 1M7 | The bell motif A–F♯–D at the top; a clean chord change every ~3.5 s; a held final chord we can tape-stop |
| **S2 Night Desk** | 0:22–1:17 | 60–90 s | 1M2 | Low and static enough to cut at 45.6 (sub hit, added by Claude) and at 70.4 (hard stop); no melody that fights the voices |
| **S3 Nana** | 1:21–1:57 (plus the fragment at 2:57) | 45–60 s | 1M3, the 1M5 fragment | Six-note melody A–F–G–E–F–D; one take that **stops on E** without resolving; solo piano at the start |
| **S4 Night 212** | 1:57–2:29 | 35–45 s | 1M4 | 60 BPM pulse; a continuous build with **no drop**; an abrupt end (cut by Claude at 2:29) |
| **S5 Come Home / First Light** | 3:18–4:02 | 60–75 s | 1M6 | Piano theme resolving to D at ~3:34, then a **lift up a half step (to E♭)** at ~3:43 that blooms and shimmers, ending on a suspended chord |

**S1 prompt**
- Title: `Continuity - The Evening Address`
- Style: `instrumental, solemn warm national broadcast hymn, vibraphone bell motif A F# D, soft brass choir, pipe organ pad, warm strings, D major, 60 bpm, stately, reassuring, slightly too sweet, mid-century public broadcast ident`
- Exclude: `drums, vocals, guitar, synth bass`
- Lyrics: `[Instrumental] [Intro: three bell notes] [Hymn: brass and organ, four slow chords] [Held final chord] [End]`

**S2 prompt**
- Title: `Continuity - Night Desk`
- Style: `instrumental, dark minimal ambient film score, deep sub drone in D minor, ticking clock pulse at 60 bpm, cold glassy synth textures, distant choir pad, sparse low piano notes, cavernous reverb, tension without drums, sci-fi noir`
- Exclude: `drums, beat, vocals, guitar`
- Lyrics: `[Instrumental] [Intro: drone and clock] [Glassy textures build] [Break] [Low piano] [Outro: drone]`

**S3 prompt**
- Title: `Continuity - Nana`
- Style: `instrumental, intimate felt piano lullaby, D minor to F major, 60 bpm, simple six-note melody A F G E F D, soft warm strings, gentle rain ambience, tender, nostalgic, sparse, ends unresolved`
- Exclude: `drums, percussion, vocals, synth`
- Lyrics: `[Instrumental] [Solo piano melody] [Soft strings enter] [Melody stops before the last two notes] [Held unresolved chord] [End]`

**S4 prompt**
- Title: `Continuity - Night 212`
- Style: `instrumental, cinematic countdown tension, heartbeat sub pulse at 60 bpm, ticking clock, low droning strings in D, filtered synth brass swelling, long rising riser, relentless build, abrupt stop`
- Exclude: `vocals, drum kit, guitar, melody`
- Lyrics: `[Instrumental] [Pulse] [Build] [Riser] [Abrupt stop]`

**S5 prompt**
- Title: `Continuity - Come Home`
- Style: `instrumental, tender felt piano melody A F G E F D over warm strings in F major resolving to D minor, then a luminous key change up a half step to E-flat major, shimmering pads, wordless choir swells, dawn, bittersweet and hopeful, ends on an unresolved suspended chord, 60 bpm`
- Exclude: `drums, beat, lyrics, guitar`
- Lyrics: `[Instrumental] [Piano theme] [Strings swell] [Key change up a half step: dawn] [Choir pads and shimmer] [Final suspended chord] [End]`

**What stays synthesized in v2:** the clocks, phones, pneumatics, UI sounds, the flatline, the Loop choir, the
walla, and the withheld third note of the E♭ chime (Claude plays B♭4 and G4 over S5's tail).
