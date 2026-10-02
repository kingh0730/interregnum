# Supplied music: timing evidence

Measured on 2026-10-02 from `episodes/first-day-extremely-fast/first-day.wav`. The input is unchanged. The reproducible analysis is `episodes/first-day-extremely-fast/build/analyze_music.py`; results are in `episodes/first-day-extremely-fast/build/music_analysis.json`. The waveform/feature plot is `work/first-day-extremely-fast/audio/music_map.png`.

| Property | Measurement or planning decision |
|---|---|
| Source duration | 43.670000 s |
| Source format | Stereo PCM, 44,100 Hz, 24-bit |
| Samples per channel | 1,925,847 |
| Integrated loudness | -14.9 LUFS, ffmpeg ebur128 |
| Loudness range | 1.3 LU, ffmpeg ebur128 |
| True peak | -8.2 dBFS, ffmpeg oversampled peak estimate |
| Automatic pulse candidates | 88.43 BPM and 176.87 BPM; strong half/double-time pair |
| Planning cadence | Use the approximately 176.87 BPM subdivision for fast action, with larger phrase shapes |
| Final picture proposal | 2,621 frames at 60 fps = 43.683333 s |
| Conform tail | 13.333 ms after the source audio ends; no song stretch |
| Perceptual listening | Not performed in this stage |

The measured dynamic range is narrow. A visually varied film cannot depend on the master becoming progressively louder. Visual scale, movement, density and timing must provide most of the contrast; later effects must not compete with the lead vocal.

## Musical shape usable for art direction

The supplied LRC contains fifteen line starts. These are source annotations, not a measured word/phoneme alignment. The largest measured onset-envelope peak is near **11.953 s**; the supplied first chorus line begins at **11.920 s**. The difference matters for later sound-to-frame conform. At this stage, 11.920 is the phrase boundary and the measured transient remains a separate event candidate.

| Source interval | Evidence | Visual opportunity |
|---|---|---|
| 0.000–5.230 | Lower waveform energy than the chorus; two lyric lines | Immediate hook at a smaller scale; establish the action before the first full acceleration |
| 5.230–about 11.400 | Increased energy; the two remaining lead-in lines | Tighten cutting and object movement while keeping the action's direction readable |
| About 11.400–11.920 | Pronounced low-energy trough, not assumed absolute silence | The primary stop: withhold movement and effects, then use the actual new attack |
| 11.920–22.700 | First chorus group, four supplied line starts | First fully dimensional birth; rapid local changes inside clear phrases |
| 22.700–34.210 | Second chorus group | More freedom of scale and medium, with a composed hold inside the motion |
| 34.210–37.070 | First final repeated line | One substantial escalation, not a new story |
| 37.070–39.900 | Second repetition | Reverse or alter an established visual rule |
| 39.900–43.670 | Final repetition and terminal decay | Pay off the physical action, preserve an identifiable end image and series mark |

## Timing discipline for the next stages

The beat grid is an editing hypothesis derived from spectral periodicity. It cannot establish downbeat identity, exact syllable attacks, singing intelligibility or musical feel. Use the LRC for script paragraphs; separately record transient, beat, action and title events. Do not describe every quick cut as a beat cut.

The source's own near-silence carries the principal sound-density change. No artificial silence, tape-stop, pitch shift, extra verse or replacement score is part of this direction. Any later lyric typography must be conformed to actual vocal onsets. At art direction, text duration and clear composition can be specified and inspected, while perceptual synchronization remains pending.
