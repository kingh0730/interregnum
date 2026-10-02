# COMMON ROOM — mix plan

Deliver a 48 kHz stereo master and separate dialogue, music, foley and ambience stems. The target is approximately -18 integrated LUFS, true peak at or below -1 dBTP. The loudness range must remain at or below16 LU. Quiet should come from reduced activity, not missing files. Dialogue is the anchor; short lines remain complete and have their own breath/tail space.

Each utterance has one line ID tied to a shot and absolute timeline offset. Its selected source is trimmed around measured voice-band energy and periodicity, retaining a short pre-onset margin. Bilingual subtitles begin at the placed voiced onset and end after the measured speech, rather than following Whisper's often-early segment start. Every lip-sync conditioning file contains only that shot's intended dialogue and is padded to exactly the shot duration.

Keep Eda and Sen centered, using the same small kitchen room treatment. Foley perspective follows the shot: quiet near-field paper and ceramics, restrained latch transients, wider footsteps only in the hall. The bowl should have consistent tone across the film. Cloth and extractor finish the story; avoid adding unmotivated impact effects to make a still move.

Use two different source takes for long continuous ambience, crossfading their seams. On picture cuts, return to the bed's ongoing time. The center decision quiet reduces all activity but preserves kitchen air. The final rain and dry outer-world air remain quieter than the shared room's immediate actions.

Music appears only in designated cue regions and ducks gently under speech. There is no automatic wall-to-wall bed. Levels are balanced before one conservative final gain/peak stage. Report integrated loudness, loudness range, true peak and any gain reduction. Also report missing sources, truncated dialogue, subtitle bounds and lip-sync lengths; none is acceptable in the handoff.

Listening remains pending for naturalness and artistic balance. Waveform checks, transcription and loudness measurements are the completed technical review, not evidence that the mix has been heard.

## Completed sound handoff

The 230.000-second master is `work/ep01/audio/master_mix.wav`, 48 kHz stereo, 24-bit PCM. It measures -18.0 integrated LUFS, -1.8 dBTP and 15.6 LU loudness range, with 0.56 dB maximum final peak reduction. Dialogue, music, foley, module-action and ambience stems share the exact master duration. The ten-second decision hold contains continuous room air, with no zero-sample gap.

All 26 dialogue lines have selected performances from two takes per line. Twenty-five selected raw ASR transcripts match after ordinary punctuation normalization; one contains homophone spellings. After placement, 24 isolated utterances match exactly. D24 retains homophone spellings; D04 has a mid-line “bowl/ball” ASR ambiguity, while both raw takes transcribe “bowl.” No dropped edge words are detected. Subtitle spans are derived from measured placed speech, remain within their assigned shots, and exclude the end card. The 26 isolated conditioning files are shot-length padded; their manifest distinguishes the 23 on-screen scene uses from three off-screen/insert lines.

Paper contact accents land at 00:08, 00:40 and 02:32, matching the authored paper states. Score and module action stop together at 01:49 while the beds continue. The original score occupies 88 seconds overall. The final mix and its five stems pass format, duration, finite-sample and peak checks, with no source placeholders or renderer warnings.

`work/ep01/audio/delivery.json` indexes the deliverables. `technical_qc.json`, `source_measurements.json`, `source_asr.json`, the voice selections and music selection retain the measured evidence. Several isolated acoustic impacts trigger extremely low-confidence ASR hallucinations; none passes the stated lexical-speech confidence screen. The simple autocorrelation pitch proxy is especially unstable on the low-register male voice, so it is not presented as proof of a natural or restrained performance. These are explicit listening-review items.
