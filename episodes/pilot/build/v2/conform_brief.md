# v2 conform brief: CONTINUITY with Seedance shots

Repo /Users/kingh0730/repos/interregnum. Read CLAUDE.md, then `tools/comp/reel.py`, `tools/comp/assemble.py`, and
`tools/audio/mix.py` (docstring + the event/preset machinery). The v1 cut is 45 shots on a fixed 242.0 s timeline.
Keep that timeline exactly: every shot keeps its v1 in-time and duration. No Codex, no fal calls, no git.
All creative decisions below are final. Just execute them. If something is impossible, do the closest thing and
report it.

## Inputs
- **v1 shots:** `work/pilot/shots/NN.mp4`. v1 specs are in `work/pilot/comp/NN.json`: grade, letterbox, overlays such
  as the J14 bug (`work/pilot/js/j14_bug.png`) and scanlines (`work/pilot/comp/c1/scanlines.png`) on broadcast shots.
- **Seedance takes:** 1280x720, 24 fps, with audio unless noted. Paths are `work/pilot/v2/shots/<id>/takes/01.mp4`,
  except shots 16 and 44, which use the bake-off takes `work/pilot/v2/16/takes/02.mp4` and `work/pilot/v2/44/takes/02.mp4`.
  Whisper word-timestamp JSONs are at `work/pilot/v2/shots/<id>/01.json`.
- **Mix timeline:** `work/pilot/audio/main.json`, rendered by mix.py to main.wav. Dialogue events D01–D26 are `say`
  events with `use` presets.

## Picture: shots replaced by Seedance
Shot in-times (s): 02 5, 03 12, 07 37, 13 71, 16 84, 17 90, 18 94, 19 99, 20 103, 23 119, 25 133, 29 152, 31 163,
32 168, 33 174, 34 180, 38 195, 39 198, 40 202, 41 205, 42 210, 44 223.
Durations are as in v1 (use each v1 shot's frame count).

| Shot | Source clip | Clip segment used (s) |
|---|---|---|
| 02 | shots/02 | 0 → 7 |
| 03 | shots/03 | 0 → 7 |
| 07 | shots/07 (silent) | 0 → 4 |
| 13 | shots/13 | 0 → 4 |
| 16 | v2/16/takes/02 | 0 → 6 |
| 17 | shots/17 | 0 → 4 |
| 18 | shots/18 | 0 → 5 |
| 19 | shots/19 | 0 → 4 |
| 20 | shots/20 | 0 → 6 |
| 23 | shots/23 (silent) | 0 → 6 |
| 25 | shots/25 (silent) | 0 → 3 |
| 29 | shots/address | 0.1 → 5.1 |
| 31 | shots/address | 7.0 → 12.0 |
| 32 | shots/32 (silent) | 0 → 6 |
| 33 | shots/33 (silent) | 0 → 6 |
| 34 | shots/address | 18.0 → end of clip, then hold the last frame (eyes closed) to fill 6 s |
| 38 | shots/38 | 0 → 3 |
| 39 | shots/39 | 0 → 4 |
| 40 | shots/40 | 0 → 3 |
| 41 | shots/41 | 0 → 5 |
| 42 | shots/42 (silent) | 0 → 7 |
| 44 | v2/44/takes/02 | 0 → 10 |

For each shot, write `work/pilot/comp_v2/NN.json` and render it with reel.py to `work/pilot/shots_v2/NN.mp4`:
- **Base layer:** the clip segment, upscaled to 1920x1080 with Lanczos. Pre-cut it with ffmpeg to an intermediate at
  `work/pilot/comp_v2/src/`.
- **Camera:** static (`from` = `to` = [0.5, 0.5, 1.0]), no shake, because Seedance already moves the camera.
- **Kept from the v1 spec:** the `grade`, `letterbox`, and flat broadcast overlays (bug and scanlines on 02, 03, 29,
  31, 34, and LIVE going out at 5.6 s in 34 via `work/pilot/js/s34_bug.mov`). Keep light particles only where they
  suit (dust in the Hall shots 07, 23, 32; rain is already in the clips).
- **Dropped:** the v1 plate prep layers, mattes, inserts and camera moves.
- **Shot 44:** also add the v1 dawn: a sky warm-up toward rose over the last 5 s. The simplest way is a vertical
  gradient layer (rose `#E8A0A8` to pale gold, top 45 % of frame, screen blend, fading in from 0 to 55 % opacity
  over 5.0–10.0 s).
- **Shot 34:** the v1 34 had a dissolve. Now it's a straight cut from 33 into the address segment.

## Audio: new timeline `work/pilot/audio/main_v2.json` → `main_v2.wav`, with stems
Start from main.json. Replace these `say` dialogue events with `file` events that play Seedance audio. Extract each
line from its clip's audio to `work/pilot/audio/vo_v2/<Dxx>.wav`: from the Whisper line start −0.12 s to line end
+0.25 s, 20 ms fades, mono 48 kHz.

**On-screen lines (lip-sync):** place each at `at = shot_in + (line_start_in_clip − clip_segment_start)`. Seedance
audio already has its room sound, so use no reverb preset. Level-match the lines to the v1 dialogue loudness.

| Line | Shot | Source |
|---|---|---|
| D01, D02 | 02 | clip 02 (lines at 0.0–6.6) |
| D03, D04 | 03 | clip 03 |
| D08 | 13 | "No, you're not." |
| D10 | 17 | |
| D11 | 18 | |
| D12 | 19 | |
| D13 "For the ending." | 20 | about 0–2 s |
| D14 | 20 | 3.1–5.6 |
| D17 | 29 | address 0.9–2.4 |
| D19 | 31 | address 7.8–9.4 |
| D22 "Nana—" | 38 | |
| D23 | 39 | |
| D24 | 40 | |
| D25 | 41 | 0.9–3.3 |

**Off-screen lines:** keep the v1 `at` time and apply the same spatial treatment as the v1 preset (the preset's
`af_post`/`slap`/`reverb`/`rt60`/`predelay`/`gain`). Extend mix.py so `file` events accept those keys if they don't
already.

| Line | Source | Preset |
|---|---|---|
| D18 | address 4.1–5.6 | STREET |
| D20 | address 12.2–14.6 | HALL |
| D21 | address 16.2–18.0 | TV |
| D26 "Come home. The soup's still warm." | clip 41, 4.2–7.3 | PHONE |

**The Loop** (D06 plus the `loop` event, 63.3–70.4) is the machine free-running on the Father's voice. Rebuild it
from Seedance Father audio:
- **D06:** a concatenation of the clip-02 lines and clip-03 "I am well.", played through the LOOP preset treatment.
- **The accelerating "I am well." repeats:** use the clip-03 "I am well." wav. Extend the `loop` generator to accept
  `path` in place of `text` if needed.

Keep the walla, PA lines (D09, D15, D16) and "Hold still." (D05) as they are.

**Ambience:** the Seedance line snippets carry a little of their own room. Keep the v1 amb beds; that's fine.

**Subtitles:** regenerate `work/pilot/subs_v2.json` from the new line times (text = the scripted lines; "Nana—" for
D22). Keep the v1 entries for the unchanged lines.

## Conform
Build `work/pilot/edit_v2.json`: shots 01–45 in order, using `shots_v2/NN.mp4` where it exists and `shots/NN.mp4`
otherwise, with audio `main_v2.wav` and the subs. Render with `tools/comp/assemble.py` to
`renders/pilot/continuity_v2.mp4`.

## QA before you report
- Every `shots_v2` file has exactly the v1 frame count.
- The total is 5808 frames = 242.0 s.
- A contact sheet of the v2 shots, checked with Read: grade continuity with the neighbouring v1 shots, and the
  letterbox matching v1.
- Lip-sync alignment: for 3 dialogue shots (17, 29, 41), cross-correlate the original clip audio segment with the
  same span of `main_v2.dx` and report the offset (must be under 1 frame).
- Loudness of main_v2.wav with ebur128.
- Delete intermediates in `work/pilot/comp_v2/src/` after the final render.

Report: a table of shot → source → frames, the lip-sync offsets, loudness, anything you couldn't do exactly, and
anything that looks off.
