"""Conform rendered shots into one cut: concatenate, burn subtitles, mux the mix.

usage: uv run tools/comp/assemble.py <edit.json>
{"out": "renders/pilot/pilot_v1.mp4", "fps": 24,
 "shots": ["work/pilot/shots/01.mp4", ...],        # already rendered at 1920x1080, same fps
 "audio": "work/pilot/mix.wav",
 "subs": [{"start": 3.2, "end": 5.0, "text": "..."}],  # burned in (scratch voices are hard to follow)
 "srt": true}                                        # also write <out>.srt next to the video
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
W, H = 1920, 1080


def P(p):
    return ROOT / p


def srt_time(s):
    ms = int(round(s * 1000))
    return f"{ms // 3600000:02}:{ms // 60000 % 60:02}:{ms // 1000 % 60:02},{ms % 1000:03}"


def main():
    spec = json.loads(Path(sys.argv[1]).read_text())
    fps = spec.get("fps", 24)
    out = P(spec["out"])
    out.parent.mkdir(parents=True, exist_ok=True)
    lst = out.with_suffix(".concat.txt")
    lst.write_text("".join(f"file '{P(s)}'\n" for s in spec["shots"]))
    subs = spec.get("subs", [])
    font = ImageFont.truetype("/System/Library/Fonts/Avenir Next.ttc", 44, index=5)  # Medium

    dec = subprocess.Popen(["ffmpeg", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                            "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    enc_cmd = ["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(fps),
               "-i", "-"]
    if spec.get("audio"):
        enc_cmd += ["-i", str(P(spec["audio"])), "-c:a", "aac", "-b:a", "256k", "-shortest"]
    enc_cmd += ["-c:v", "libx264", "-crf", "17", "-preset", "medium", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                str(out)]
    enc = subprocess.Popen(enc_cmd, stdin=subprocess.PIPE)
    i, cache = 0, {}
    while True:
        buf = dec.stdout.read(W * H * 3)
        if len(buf) < W * H * 3:
            break
        t = i / fps
        active = [s for s in subs if s["start"] <= t < s["end"]]
        if active:
            key = active[0]["text"]
            if key not in cache:
                layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
                d = ImageDraw.Draw(layer)
                lines = key.split("\n")
                y = H - 110 - 56 * (len(lines) - 1)
                for ln in lines:
                    w = d.textlength(ln, font=font)
                    d.text(((W - w) / 2, y), ln, font=font, fill=(255, 255, 255, 240),
                           stroke_width=3, stroke_fill=(0, 0, 0, 200))
                    y += 56
                cache[key] = layer
            im = Image.frombuffer("RGB", (W, H), buf).convert("RGBA")
            im.alpha_composite(cache[key])
            buf = im.convert("RGB").tobytes()
        enc.stdin.write(buf)
        i += 1
    enc.stdin.close()
    enc.wait()
    lst.unlink()
    if spec.get("srt", True) and subs:
        out.with_suffix(".srt").write_text("".join(
            f"{k + 1}\n{srt_time(s['start'])} --> {srt_time(s['end'])}\n{s['text']}\n\n" for k, s in enumerate(subs)))
    print(out, i, "frames", round(i / fps, 2), "s")


if __name__ == "__main__":
    main()
