You are a compositor on the pilot CONTINUITY (INTERREGNUM), repo /Users/kingh0730/repos/interregnum. Read CLAUDE.md,
episodes/pilot/episode.md (visual language, shot list, frame-shape rules: world shots letterboxed 2.39, broadcast full frame),
and the shot.md of each of YOUR shots (Build, Layers, JS spec, Sound, timing). Then read tools/comp/reel.py (docstring + code).

Inputs: keyframes and alpha cutout layers are in work/pilot/keys/<id>.png (e.g. k03.png, k03_fg_desks.png; the manifest
work/pilot/images.json maps ids to shots). Lookdev refs in assets/pilot/lookdev/. JS pieces (full-frame screens .mp4 and
transparent overlays .mov) are being rendered by other agents into work/pilot/js/ from episodes/pilot/js/*.html; if one
you need is not there yet, do your other shots first, then wait for it (until-loop polling, up to 40 min; if it never
appears, build the shot without it and report). Never edit files in episodes/pilot/js/ or work/pilot/js/.

For EVERY shot in your range, produce work/pilot/shots/NN.mp4 (1920x1080, 24 fps, exactly round(Duration*24) frames,
the Duration from the shot list) via a spec work/pilot/comp/NN.json rendered by `uv run tools/comp/reel.py`.
- Keyframe shots: the camera move from the shot list (zoom values like 1.00→1.04 map to camera from/to zoom), parallax
  with the cutout layer (par > 1 for foreground), the particles/light/grade the Build asks for (rain, dust in beams,
  flicker, pulses, screen glow), letterbox where the doc says. Subtle handheld shake only where it serves.
  Screens/composites the Build asks for (e.g. the Father's face on the monitor wall, text on a paper) = extra layers:
  you may prepare intermediate images/videos with small Python scripts in work/pilot/comp/ (e.g. perspective-warp k02
  onto the wall's screen grid with cv2.getPerspectiveTransform, tinted and gridded) and feed them as layers.
- JS-only shots: wrap the JS .mp4 as the base layer with a light matching grade/grain so every shot shares one finish.
- Hard cuts between shots unless the doc says otherwise (the one dissolve in shot 34 lives inside that shot).
Do NOT edit tools/comp/reel.py (other compositors use it concurrently). If it lacks a feature, work around it with
prepared layers, and mention it in your report.
QA: render with --preview first (contact sheet .sheet.jpg next to the out path) and LOOK at it with the Read tool; check
framing (nothing important under the letterbox bars), the move reads, the grade matches the episode's palette, and
composites sit convincingly. Then full render. Verify frame count with ffprobe -count_frames.
Disk is tight (~4 GB free): delete previews and intermediates you no longer need; never write big PNG sequences.
No git, no Codex, no audio (the mix is done). Final reply: table shot → duration → frames → what's in it; problems;
the 3 shots you think look best and the 3 weakest (with why).
