# 第一天 — sound direction

The supplied recording is the episode's complete soundtrack. Preserve its order,
tempo, vocals, stereo image, dynamics, introduction, and ending. The picture must
fit the song. This music-video brief deliberately overrides the usual episode
workflow of generating dialogue, score, foley, and rooms.

## Source and master

- Source: `episodes/first-day/first-day.mp3`, stereo MP3, 320 kb/s, 44,100 Hz.
- Source duration and decoded duration: **253.960000 seconds**. The decoded master
  contains **11,199,636 samples per channel**. At 24 fps, the picture timeline needs
  6,096 frames; its last frame extends 40 ms beyond the exact audio endpoint.
- Canonical master: `work/first-day/audio/master.wav`, stereo 32-bit float PCM,
  **44,100 Hz**, a single **−8.2 dB static gain** from the supplied recording.
- Analysis uses a mono **22,050 Hz** copy only. That rate change never reaches the
  master. Do not confuse analysis rate with delivery rate, or resample repeatedly.
- No compression, limiter, fade, rearrangement, speed change, trim, artificial
  silence, extra dialogue, generated singing, or decorative sound effects.
- The MP3 remains untouched. The LRC remains untouched. Their SHA-256 hashes are
  recorded in `episodes/first-day/build/audio_plan.json`.

The measured source is −7.8 LUFS integrated, +0.2 dBTP true peak, and 6.1 LU LRA.
The master measures **−16.0 LUFS, −8.0 dBTP, and 6.1 LU LRA**, preserving the
recording's existing dynamic range. The measured master results are authoritative in
`episodes/first-day/build/audio_plan.json`; this is normalization, not a new mix.
There is ample peak headroom after attenuation, so no limiting is needed.

## Dramatic use

The song is a continuous performed event. Its returns let the visual gesture acquire
new meanings. Verses give room for faces, practical behavior, environment, and
relationship; choruses support larger dancing phrases and bursts of faster cuts.
A visual hard stop leaves the song running. Do not manufacture a silent musical
break to satisfy the general tempo guideline.

Movement should sometimes continue across several musical accents. Cutting on every
detected beat makes the picture mechanical. Use the measured onset list for possible
attacks, lyric starts for phrase anchors, and longer held two-shots for contrast.
The tracker selects 89.10 BPM; its double-time reading is 178.21 BPM. Autocorrelation
also supports 87.59 BPM, so treat these as approximate pulse candidates. The measured
beat times accommodate local variation. `beat_anchor_candidates` excludes predicted
beats without a nearby transient or with a very low signal level; the full tracker
grid can continue through silence. Neither establishes bar downbeats or exact vocal
syllable boundaries.

There is no requirement to animate the leads singing. Their fictional identities
must not imitate the recording's performer. The supplied credits describe the
recording; they do not cast its credited musicians as characters.

## Lyrics and credits

`episodes/first-day/build/lyrics.json` contains unique IDs for every lyric occurrence,
including repeated chorus lines. `work/first-day/audio/lyrics.srt` is the review
subtitle track. Preserve the supplied Simplified Chinese exactly and retain the
original English refrain; add no translation or extra lyrics.

The first four timestamped entries are metadata, not sung lines: title/performer,
lyricist, composers, and arrangers. They are stored separately under
`metadata_entries_not_subtitles` and must not be mistaken for intro lyric captions.
The UTF-8 LRC is the source of these credits; the MP3's legacy-encoded ID3 strings
are unreliable when decoded as UTF-8.

Lyric starts come directly from the LRC. Ordinary cue ends leave a 60 ms gap before
the next supplied onset. Gaps over six seconds use a provisional 3.5-second caption
hold, then clear the picture. The final lyric clears at **243.960 seconds**, leaving
the last **10 seconds** without a lingering caption. Those hold times are editorial
choices, not measured sung-word offsets.

Mixed-track spectral onsets are recorded near every lyric start for inspection.
Drums, consonants, guitars, and other instruments can all create such an onset;
proximity is not proof of lyric synchronization. No lyric is moved to a detected
transient automatically. Final onset and offset approval still needs listening.

## Rebuild and review

Run `uv run episodes/first-day/build/analyze_audio.py` from the repository root.
It rebuilds the master, sidecars, analysis, and plan without network model calls.
The script validates source hashes, cue order, overlap, IDs, duration, channels,
sample rate, and measured integrated loudness. Dependencies are pinned in the script;
the first run may fetch its ordinary Python packages.

`work/first-day/audio/audio_analysis.json` contains source/master measurements,
candidate tempos, beat times, mixed-audio onsets, half-second waveform envelopes,
section energies, and per-lyric onset inspection. Sections based on lyric timestamps
and caption hold caps are explicitly provisional. Energy and spectra characterize
the signal; they do not establish emotional impact, vocal accuracy, or sound quality.

No listening approval is claimed. Human review should check lyric sync, perceived
beat phase, whether the picture breathes with the arrangement, and playback loudness
on headphones and a small speaker. Those listening checks do not justify altering
the supplied recording without a new instruction.
