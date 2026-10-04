#!/usr/bin/env bash
set -euo pipefail
# Lossless PNG sequence -> final MP4, audio = ORIGINAL mp3 muxed untouched in length (43.70 s).
ffmpeg -y -framerate 30 -i frames/%05d.png -i ../first-day.mp3 \
  -vf "scale=1920:1080:flags=lanczos,format=yuv420p" \
  -c:v libx264 -preset slow -crf 16 -colorspace bt709 -color_primaries bt709 -color_trc bt709 \
  -c:a aac -b:a 320k -shortest -movflags +faststart first-day_opus55_1080p30.mp4
ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 first-day_opus55_1080p30.mp4
