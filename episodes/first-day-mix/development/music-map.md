# First Day: music and editorial timing map

Source: `episodes/first-day-mix/first-day.wav`; supplied lyric timing: `episodes/first-day-mix/first-day.lrc`. Measured 2026-10-02. This document separates file measurements, supplied lyric markers and editorial proposals. **Audio has not been listened to in this analysis.** No timbral, singer, instrumentation or musical-downbeat judgment is claimed.

## Measured master

- Exactly **43.670000 seconds**, 1,925,847 sample frames, 44,100 Hz, stereo, signed 24-bit PCM. Keep the full master, including the final tail. At 60 fps this is 2,620.2 frames: a later export must choose an explicit frame-end policy; do not silently shorten the audio to 43.6667 s.
- `episodes/first-day-mix/development/audio-analysis.json` contains the source SHA-256, 100 Hz band RMS envelopes, detected amplitude-attack candidates and per-LRC-region RMS values.
- Analysis decodes a mono 8 kHz working signal with FFmpeg, measures nonoverlapping 10 ms RMS windows, computes positive log-RMS differences and picks peaks above a local adaptive threshold, suppressing peaks less than 120 ms apart. Low band is low-pass 180 Hz; high band is high-pass 1,800 Hz. These bands are **not** separated kick/hat/vocal stems. Onset timing precision is limited by windows, filtering and the detector, not sample accuracy.
- Detected candidates: 220 full-mix attacks, 231 low-band attacks, 197 high-band attacks. These lists are useful for auditioning accent locations, not 220 compulsory cuts or trusted instrument labels.
- Low-band autocorrelation supplies a plausible **175.8 BPM** working grid with phase approximately **0.01 s**, and an equally important half-time interpretation **87.9 BPM** with phase approximately **0.35 s**. The half-time candidate has slightly higher autocorrelation score; the doubled grid catches more attacks because it has twice as many positions. That is not independent evidence of the correct musical tactus.
- Working interval at 175.8 BPM: 0.3413 s; eighth subdivision 0.1706 s; half-time interval 0.6826 s. Secondary candidates near 117 BPM and neighboring fast tempos expose rhythmic ambiguity. **No meter, downbeat phase or final constant-tempo lock is established.** Verify against the master before frame-accurate choreography.

The reproducible local analysis script is `work/first-day-mix/analysis/analyze_music.py` (scratch, not a production dependency). JSON values are measurements/candidates, not listening annotations.

## Supplied line map and editorial opportunities

End times below are the next supplied LRC start, except the final region, which ends at the master duration. They do not establish exactly when a sung syllable ends. RMS is mono full-mix band-limited working-signal dBFS, not integrated loudness/LUFS.

| Time (s) | Supplied lyric | RMS dBFS | Editorial opportunity, subject to listening |
|---|---|---:|---|
| 0.00–2.84 | 你说活在明天活在期待 | −18.31 | Open on a causally legible tactile event; one image people remember before the style burst. No added title pre-roll. |
| 2.84–5.23 | 不如活得今天很自在 | −17.62 | First material transition and first unmistakably human gesture. A short stable interval makes the next acceleration visible. |
| 5.23–8.24 | 我说我懂了会不会太快 | −16.33 | Acceleration can answer 太快 literally: action jumps ahead, then catches itself. Avoid every model name at once. |
| 8.24–11.92 | 未来第一天要展开 | −16.47 | A dimensional opening into the ensemble; prepare a readable spatial layout for the first hook. |
| 11.92–14.64 | 第一天我存在 | −16.28 | First full identity/embodiment payoff. One strong body action; names remain readable instead of full-screen lyric clutter. |
| 14.64–17.61 | 第一次呼吸畅快 | −15.77 | Breath changes nearby material; particles have a source and react to the character. |
| 17.61–19.67 | 站在地上的脚踝 | −15.91 | Contact, weight, floor and shadow: a grounded counterpoint to abstract effects. |
| 19.67–22.70 | 因为你而有真实感 | −15.70 | A hand-to-hand or gaze interaction makes existence relational. Reserve a visual hold even while the supplied audio continues. |
| 22.70–25.45 | 第一天我存在 | −16.04 | Reprise with a changed medium and expanded agency, not the same shot recolored. |
| 25.45–28.55 | 第一次能飞起来 | −16.08 | Earn the largest spatial lift with the earlier grounded contact. Camera and character should not both wander aimlessly. |
| 28.55–30.68 | 爱是腾空的魔幻 | −16.11 | One spectacular impossible connection; keep the subject silhouette clear. |
| 30.68–34.21 | 第一天的纯真色彩它总是 | −16.20 | Saturation and scale expansion, then subtraction before repeated final phrases. |
| 34.21–37.07 | 永远那么灿烂 | −16.79 | Repetition 1: collective scale. |
| 37.07–39.90 | 永远那么灿烂 | −16.62 | Repetition 2: intimate detail or unusual low-cadence form, contrasting the previous phrase. |
| 39.90–43.67 | 永远那么灿烂 | −16.43 | Repetition 3: synthesis and a clear final image; design the tail after the actual final vocal is checked. |

## Four-dial proposal

These are creative design targets, not measurements of cuts or claims about the song's arrangement. A visual hard stop does **not** require muting or altering the supplied music.

| Region | Cut/action cadence | Movement inside shots | Added sound/voice | Emotional intensity |
|---|---|---|---|---|
| 0–5.23 | One strong opening, then brief accelerating action accents; preserve the opening event's cause/result | Macro movement becomes a small body gesture | No new dialogue; master unchanged | Curiosity → delight |
| 5.23–11.92 | Compressed burst followed by a clear arrival; actual cuts distinguished from pose/contact events | Stop-start medium changes and one decisive depth move | No added voice; any later SFX must not bury Mandarin | Comically overwhelmed → anticipation |
| 11.92–19.67 | Fast changes separated by 0.7–1.4 s readable performance windows | Breath and foot contact, contrasting camera scale | Master carries the rhythm | Exhilaration grounded in physical wonder |
| 19.67–22.70 | Longest visual hold or a brief internal freeze | Hand/gaze event; minimum camera motion | Keep the song; no invented silence | Affection |
| 22.70–34.21 | Strongest acceleration, occasional sub-beat action cells; labels span enough time to read | Lift, crossing, orbit, release, then a stop | No exposition track | Collective discovery |
| 34.21–43.67 | Three phrase-sized transformations with deliberately different internal cadence | Wide spectacle → intimate hold → resolving movement | Preserve tail; no spoken credits | Joy → tenderness → earned celebration |

## Timing contract for later production

The LRC is suitable for broad script/art-direction blocks. It is insufficient for syllable-driven text, lip-sync or foot contact. Before production, establish listened markers for hook entry, drum accents, phrase releases and the last vocal. Keep separate fields for measured attacks, verified beats, lyric line starts, syllables, actual camera cuts and internal action events. Do not manufacture many cuts by counting all action events as shots. Use the same absolute song clock across video plates, code, masks and captions. Review at normal speed: waveform agreement alone does not establish musicality.
