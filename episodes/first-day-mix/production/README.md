# First Day Mix — final production

Final product: `renders/first-day-mix/first-day-mix-final.mp4` (1920×1080,60fps,2621frames). Supplied Mandarin song preserved; generated model audio discarded. Source audio is43.670s; delivery video is43.683333s with13.333ms silence at the end. No source track stretch or cut.

## What was made

Eight MiniMax H3 Max motion clips from inspected stills, five Luma prop/environment plates, two imagegen hero edits and an exact ankle crop. Six further imagegen sheets supply23 original transparent character assets plus5 alternate poses. The final renderer combines those with deterministic procedural geometry, tile births, empty sockets, canopy attachment lines, particles, stepped pose changes, pixel treatment, fractures, perspective effects and Chinese typography. Source footage remains24fps; the compositing/output clock is60fps. This is a deliberate mixed animation language, not a claim every body is native60fps generated motion.

`final-config.json` is the implemented cut. `final-cut.md` describes departures from the earlier treatment. `source-assets.json`, `cast/manifest.json`, `motion-specs.json`, `hero-image-prompts.json`, `scene-images.json` and `cast/all-prompts.json` preserve sources and prompt provenance. The reference film's code and media were not copied into production.

## Budget

Provider rate snapshot: H3 Max$0.03/requested second; Luma$0.003/image. Eight motion jobs request44seconds: quoted$1.32. Five Luma images: quoted$0.015. Total API estimate$1.335; invoice reconciliation is not available. Imagegen uses subscription quota (8 successful production calls, one earlier network failure; prior art-stage calls separate). See `budget.json`. All requests completed; no unresolved paid request needs resubmission.

## Rebuild from retained assets

The current engine and final configuration produce the corrected entire cut directly:

```sh
/Users/kingh0730/.nvm/versions/node/v22.23.1/bin/node episodes/first-day-mix/production/renderer/export.mjs --config episodes/first-day-mix/production/final-config.json --out work/first-day-mix/production/rebuild-silent.mp4
ffmpeg -i work/first-day-mix/production/rebuild-silent.mp4 -i episodes/first-day-mix/first-day.wav -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 320k -af apad=pad_dur=0.013333333 -t 43.683333333 -movflags +faststart renders/first-day-mix/first-day-mix-rebuild.mp4
```

This rebuild is visually equivalent, not promised byte-identical to the delivered encode. The actual delivered file combined two base chunks with four precise replacement intervals, then encoded once for assembly. `finish_film.py` reproduces that assembly from retained chunks/patches and checks frozen input bindings. `final-render-inputs.json` preserves engine/config versions for the base and patches. Patches correct meme ownership, last-tile visibility and complete four-character framing; they do not change the song or total frame count.

## Review scope

See `final-review.md` and `delivery.json` for completed checks and final file hash. Technical decoding, frame counts, source/audio integrity, measured text bounds and sampled-frame inspection are separate from normal-speed audiovisual judgment. No claim is made to have listened to or watched the complete film in real time. The render is complete; perceived dance naturalness, musicality and whether it exceeds the reference's spectacle remain viewing judgments.

All media stays ignored in `work/` and `renders/`; no public release or push was performed.
