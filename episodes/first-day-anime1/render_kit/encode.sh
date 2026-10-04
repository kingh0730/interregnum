#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 -c 'import json; assert json.load(open("../production/frame-qa.json"))["passed"], "Frame QA must pass before encoding"'
# Exactly 1,311 video frames; original song is neither stretched nor padded.
ffmpeg -y -framerate 30 -i frames/%05d.png -i ../first-day.mp3 \
  -map 0:v:0 -map 1:a:0 -frames:v 1311 \
  -vf "scale=1920:1080:flags=lanczos:out_color_matrix=bt709:in_range=full:out_range=tv,format=yuv420p,setparams=colorspace=bt709:color_primaries=bt709:color_trc=bt709:range=limited" \
  -c:v libx264 -preset slow -crf 16 -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -c:a aac -b:a 320k -movflags +faststart ../first-day_opus55_1080p30.mp4
ffmpeg -y -i ../first-day_opus55_1080p30.mp4 -map 0:v:0 -map 0:a:0 \
  -vf 'scale=960:540:flags=lanczos:in_color_matrix=bt709:out_color_matrix=bt709,setparams=colorspace=bt709:color_primaries=bt709:color_trc=bt709:range=limited' -c:v libx264 -preset slow -crf 20 \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -c:a copy -movflags +faststart ../first-day_opus55_540p30.mp4
ffprobe -v error -count_frames -show_streams -show_format -of json ../first-day_opus55_1080p30.mp4 > ../production/export-probe.json
python3 -c 'import json; s=next(s for s in json.load(open("../production/export-probe.json"))["streams"] if s["codec_type"]=="video"); assert (s["width"],s["height"],s["r_frame_rate"],int(s["nb_read_frames"]))==(1920,1080,"30/1",1311)'
