#!/usr/bin/env python3
"""Render an honest, frame-exact held-image story reel. No motion generation.

Run with the repository's Pillow environment:
    uv run episodes/first-day/build/render_reel.py episodes/first-day/build/render.json
See render_contract.json beside this script. --validate-only never renders.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, ROUND_CEILING
import hashlib
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[3]
WIDTH, HEIGHT, FPS = 1920, 1080, 24
FONT = "/System/Library/Fonts/STHeiti Medium.ttc"


def run(argv: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(argv, check=True, capture_output=True, text=True)


def path(value: str) -> Path:
    if not isinstance(value, str) or not value:
        raise ValueError("asset paths must be nonempty strings")
    return (ROOT / value).resolve()


def load(value):
    return json.loads(path(value).read_text(encoding="utf-8")) if isinstance(value, str) else value


def integer(value, label: str, minimum=0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label} must be an integer >= {minimum}")
    return value


def number(value, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{label} must be finite numeric data")
    return float(value)


def frame_at(seconds: float) -> int:
    return int((Decimal(str(seconds)) * FPS).to_integral_value(rounding=ROUND_CEILING))


def probe(asset: Path, count=False) -> dict:
    args = ["ffprobe", "-v", "error"]
    if count:
        args.append("-count_frames")
    return json.loads(run(args + ["-show_streams", "-show_format", "-of", "json", str(asset)]).stdout)


def digest(asset: Path) -> str:
    h = hashlib.sha256()
    with asset.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def text_layout(text: str, font, bottom: int | None = None, top: int | None = None):
    if not isinstance(text, str) or not text.strip():
        raise ValueError("subtitle/title text must be nonempty")
    if "\r" in text or "\x00" in text:
        raise ValueError("subtitle/title text contains a forbidden control character")
    draw = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    lines = []
    for original in text.split("\n"):
        line = ""
        for char in original:
            if line and draw.textlength(line + char, font=font) > WIDTH - 240:
                lines.append(line.rstrip())
                line = char.lstrip()
            else:
                line += char
        lines.append(line)
    if len(lines) > 2 or any(not line for line in lines):
        raise ValueError(f"text needs more than two lines or contains a blank line: {text!r}")
    wrapped = "\n".join(lines)
    box = draw.multiline_textbbox((0, 0), wrapped, font=font, spacing=10, stroke_width=2, align="center")
    w, h = box[2] - box[0], box[3] - box[1]
    left = (WIDTH - w) // 2
    actual_top = bottom - h if bottom is not None else top if top is not None else (HEIGHT - h) // 2
    if actual_top < 40 or actual_top + h > HEIGHT - 40:
        raise ValueError("text lies outside the safe title area")
    return {"text": wrapped, "xy": (left - box[0], actual_top - box[1]),
            "box": (left, actual_top, left + w, actual_top + h), "font": font}


def overlap(a, b) -> bool:
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def validate(config: dict) -> dict:
    if not isinstance(config, dict):
        raise ValueError("render config must be an object")
    if config.get("fps", FPS) != FPS or config.get("width", WIDTH) != WIDTH or config.get("height", HEIGHT) != HEIGHT:
        raise ValueError("this episode renderer requires 1920x1080 at 24 fps")
    for tool in ("ffmpeg", "ffprobe"):
        if not shutil.which(tool):
            raise ValueError(f"{tool} is not on PATH")
    if "libx264" not in run(["ffmpeg", "-hide_banner", "-encoders"]).stdout:
        raise ValueError("ffmpeg needs the libx264 encoder")
    audio = path(config["audio"])
    if audio.suffix.lower() != ".wav" or not audio.is_file():
        raise ValueError("audio must be an existing master WAV")
    audio_info = probe(audio)
    streams = [s for s in audio_info["streams"] if s["codec_type"] == "audio"]
    if len(streams) != 1:
        raise ValueError("master WAV must have exactly one audio stream")
    stream = streams[0]
    if not stream["codec_name"].startswith("pcm_"):
        raise ValueError("master WAV must contain uncompressed PCM audio")
    numerator, denominator = map(int, stream["time_base"].split("/"))
    duration = Decimal(stream["duration_ts"]) * numerator / denominator
    total = int((duration * FPS).to_integral_value(rounding=ROUND_CEILING))
    if total < 1:
        raise ValueError("master audio is empty")
    timeline = load(config["timeline"])
    if isinstance(timeline, dict):
        timeline = timeline["timeline"]
    if not isinstance(timeline, list) or not timeline:
        raise ValueError("timeline must be a nonempty list")
    shots, ids, image_sizes = [], set(), {}
    cursor = 0
    for source in timeline:
        shot = dict(source)
        label = shot.get("id")
        if not isinstance(label, str) or not label or label in ids:
            raise ValueError("timeline IDs must be unique nonempty strings")
        ids.add(label)
        first = integer(shot["start_frame"], f"{label}.start_frame")
        last = integer(shot["end_frame"], f"{label}.end_frame", 1)
        if first != cursor or last <= first:
            raise ValueError(f"{label}: timeline must be ordered, contiguous and end-exclusive (expected {cursor})")
        cursor = last
        if not all(isinstance(shot.get(key), str) and shot[key] for key in ("section", "kind")):
            raise ValueError(f"{label}: section and kind must be nonempty strings")
        asset = path(shot["image"])
        if asset not in image_sizes:
            with Image.open(asset) as im:
                if getattr(im, "n_frames", 1) != 1:
                    raise ValueError(f"{asset}: only single still images are supported")
                im.load()
                image_sizes[asset] = ImageOps.exif_transpose(im).size
        crop = shot.get("crop", [0, 0, 1, 1])
        if not isinstance(crop, list) or len(crop) != 4:
            raise ValueError(f"{label}: crop must be [x,y,width,height]")
        x, y, w, h = [number(v, f"{label}.crop") for v in crop]
        if x < 0 or y < 0 or w <= 0 or h <= 0 or x + w > 1.000000001 or y + h > 1.000000001:
            raise ValueError(f"{label}: crop must be within the source image")
        iw, ih = image_sizes[asset]
        if round((x + w) * iw) <= round(x * iw) or round((y + h) * ih) <= round(y * ih):
            raise ValueError(f"{label}: crop has no source pixels")
        shot.update(asset=asset, crop=[x, y, w, h])
        shots.append(shot)
    if cursor != total:
        raise ValueError(f"timeline has {cursor} frames; full {duration}s master requires {total} frames at 24 fps")
    letterbox = config.get("letterbox")
    if letterbox is not None and number(letterbox, "letterbox") < WIDTH / HEIGHT:
        raise ValueError("letterbox aspect must be at least 16:9, or null")
    if letterbox is not None and round(WIDTH / letterbox) < 2:
        raise ValueError("letterbox aperture must be at least two pixels high")
    font_config = config.get("font", {})
    font_path = path(font_config.get("path", FONT))
    font_index = integer(font_config.get("index", 1), "font.index")
    size = integer(font_config.get("size", 38), "font.size", 12)
    font = ImageFont.truetype(str(font_path), size, index=font_index)
    bottom = integer(font_config.get("bottom_margin", 72), "font.bottom_margin", 40)
    cues = load(config.get("lyrics", []))
    if isinstance(cues, dict):
        cues = cues["cues"]
    if not isinstance(cues, list):
        raise ValueError("lyrics must be a cue list or an object containing cues")
    lyrics, previous_end = [], 0.0
    for i, source in enumerate(cues):
        cue = dict(source)
        start, end = number(cue["start"], f"cue {i}.start"), number(cue["end"], f"cue {i}.end")
        if start < previous_end or end <= start or end > float(duration) + 0.000001:
            raise ValueError(f"cue {i}: cues must be ordered, nonoverlapping and within the master audio")
        previous_end = end
        first, last = frame_at(start), frame_at(end)
        if last <= first:
            raise ValueError(f"cue {i}: shorter than one display frame after quantization")
        cue.update(start_frame=first, end_frame=last, layout=text_layout(cue["text"], font, bottom=HEIGHT - bottom))
        lyrics.append(cue)
    titles = []
    for i, source in enumerate(config.get("titles", [])):
        title = dict(source)
        first = integer(title["start_frame"], f"title {i}.start_frame")
        last = integer(title["end_frame"], f"title {i}.end_frame", 1)
        if last <= first or last > total:
            raise ValueError(f"title {i}: invalid frame interval")
        position = title.get("position", "top")
        if position not in ("top", "center"):
            raise ValueError("title position must be top or center")
        title_font = ImageFont.truetype(str(font_path), integer(title.get("size", 58), "title.size", 12), index=font_index)
        title["layout"] = text_layout(title["text"], title_font, top=96 if position == "top" else None)
        for other in titles:
            if first < other["end_frame"] and other["start_frame"] < last and overlap(title["layout"]["box"], other["layout"]["box"]):
                raise ValueError(f"title {i} overlaps another title")
        for cue in lyrics:
            if first < cue["end_frame"] and cue["start_frame"] < last and overlap(title["layout"]["box"], cue["layout"]["box"]):
                raise ValueError(f"title {i} overlaps a lyric")
        titles.append(title)
    name = config.get("name", "first_day_story_reel")
    if not isinstance(name, str) or Path(name).name != name or "story_reel" not in name:
        raise ValueError("name must be a filename stem containing story_reel")
    out_dir = path(config.get("out_dir", "renders/first-day"))
    output_paths = [out_dir / f"{name}{suffix}" for suffix in ("_clean.mp4", "_zh.mp4", ".zh.srt", ".render_report.json")]
    inputs = {audio, *image_sizes.keys()}
    if any(output in inputs for output in output_paths):
        raise ValueError("an output would overwrite an input asset")
    return dict(config=config, shots=shots, audio=audio, audio_info=audio_info, duration=duration, total=total,
                lyrics=lyrics, titles=titles, letterbox=letterbox, outputs=output_paths, font=font.getname())


def compose(shot, active, letterbox) -> Image.Image:
    with Image.open(shot["asset"]) as source:
        image = ImageOps.exif_transpose(source).convert("RGBA")
    iw, ih = image.size
    x, y, w, h = shot["crop"]
    image = image.crop((round(x * iw), round(y * ih), round((x + w) * iw), round((y + h) * ih)))
    aperture_h = round(WIDTH / letterbox) if letterbox is not None else HEIGHT
    image = ImageOps.contain(image, (WIDTH, aperture_h), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 255))
    canvas.alpha_composite(image, ((WIDTH - image.width) // 2, (HEIGHT - image.height) // 2))
    draw = ImageDraw.Draw(canvas)
    for item in active:
        layout = item["layout"]
        draw.multiline_text(layout["xy"], layout["text"], font=layout["font"], spacing=10,
                            align="center", fill=(250, 249, 244, 255), stroke_width=2, stroke_fill=(0, 0, 0, 230))
    return canvas.convert("RGB")


def image_schedule(state, with_lyrics: bool, scratch: Path, cache: dict) -> list[tuple[Path, int]]:
    events = state["titles"] + (state["lyrics"] if with_lyrics else [])
    schedule = []
    for shot in state["shots"]:
        first, last = shot["start_frame"], shot["end_frame"]
        boundaries = {first, last}
        for event in events:
            boundaries.update(t for t in (event["start_frame"], event["end_frame"]) if first < t < last)
        cuts = sorted(boundaries)
        for start, end in zip(cuts, cuts[1:]):
            active = [event for event in events if event["start_frame"] <= start < event["end_frame"]]
            key = (str(shot["asset"]), tuple(shot["crop"]), tuple(id(item) for item in active))
            if key not in cache:
                target = scratch / f"plate_{len(cache):04d}.png"
                compose(shot, active, state["letterbox"]).save(target, compress_level=1)
                cache[key] = target
            schedule.append((cache[key], end - start))
    return schedule


def encode_holds(schedule, output: Path, total: int, preset: str, crf: int):
    listing = output.with_suffix(".ffconcat")
    # The generated names have no quoting metacharacters; paths stay relative to this file.
    lines = ["ffconcat version 1.0"]
    for image, frames in schedule:
        lines.extend([f"file '{image.name}'", "option framerate 24", f"duration {frames / FPS:.12f}"])
    # The sentinel supplies the final hold's boundary; -frames:v excludes its own frame.
    lines.extend([f"file '{schedule[-1][0].name}'", "option framerate 24"])
    listing.write_text("\n".join(lines) + "\n", encoding="utf-8")
    run(["ffmpeg", "-hide_banner", "-v", "error", "-nostdin", "-y", "-f", "concat", "-safe", "0",
         "-i", str(listing), "-vf", "fps=fps=24:start_time=0:round=near,setsar=1", "-frames:v", str(total),
         "-an", "-c:v", "libx264", "-preset", preset, "-tune", "stillimage", "-crf", str(crf),
         "-pix_fmt", "yuv420p", "-video_track_timescale", "24000", str(output)])


def srt_time(seconds: float) -> str:
    milliseconds = round(seconds * 1000)
    return f"{milliseconds // 3600000:02}:{milliseconds // 60000 % 60:02}:{milliseconds // 1000 % 60:02},{milliseconds % 1000:03}"


def conform(output: Path, state) -> dict:
    info = probe(output, count=True)
    video = next(s for s in info["streams"] if s["codec_type"] == "video")
    audio = next(s for s in info["streams"] if s["codec_type"] == "audio")
    if (video["width"], video["height"], video["avg_frame_rate"], int(video["nb_read_frames"])) != (WIDTH, HEIGHT, "24/1", state["total"]):
        raise RuntimeError(f"frame conformance failed: {output}")
    if abs(float(audio["duration"]) - float(state["duration"])) > 0.05:
        raise RuntimeError(f"master audio duration was not preserved: {output}")
    return info


def render(state, keep_cache: bool, preset: str, crf: int):
    clean, chinese, srt, report_path = state["outputs"]
    clean.parent.mkdir(parents=True, exist_ok=True)
    work = path(state["config"].get("work_dir", "work/first-day/reel-build"))
    work.mkdir(parents=True, exist_ok=True)
    scratch = Path(tempfile.mkdtemp(prefix="held-", dir=work))
    try:
        staging_srt = scratch / "lyrics.srt"
        staging_srt.write_text("".join(f"{i + 1}\n{srt_time(cue['start'])} --> {srt_time(cue['end'])}\n{cue['text']}\n\n"
                                       for i, cue in enumerate(state["lyrics"])), encoding="utf-8")
        cache = {}
        print("Composing clean stills", flush=True)
        clean_schedule = image_schedule(state, False, scratch, cache)
        silent_clean = scratch / "clean_silent.mp4"
        encode_holds(clean_schedule, silent_clean, state["total"], preset, crf)
        staging_clean = scratch / clean.name
        command = ["ffmpeg", "-hide_banner", "-v", "error", "-nostdin", "-y", "-i", str(silent_clean), "-i", str(state["audio"])]
        if state["lyrics"]:
            command += ["-i", str(staging_srt)]
        command += ["-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-c:a", "aac", "-b:a", "320k"]
        if state["lyrics"]:
            command += ["-map", "2:s:0", "-c:s", "mov_text", "-metadata:s:s:0", "language=zho",
                        "-metadata:s:s:0", "title=Chinese lyrics", "-disposition:s:0", "0"]
        command += ["-metadata", "title=第一天 | AI SI - I", "-metadata", "comment=Pre-motion story reel; held approved keyframes",
                    "-movflags", "+faststart", str(staging_clean)]
        run(command)
        print("Composing Chinese lyric stills", flush=True)
        chinese_schedule = image_schedule(state, True, scratch, cache)
        silent_chinese = scratch / "zh_silent.mp4"
        encode_holds(chinese_schedule, silent_chinese, state["total"], preset, crf)
        staging_chinese = scratch / chinese.name
        run(["ffmpeg", "-hide_banner", "-v", "error", "-nostdin", "-y", "-i", str(silent_chinese), "-i", str(staging_clean),
             "-map", "0:v:0", "-map", "1:a:0", "-c", "copy", "-metadata", "title=第一天 | AI SI - I",
             "-metadata", "comment=Pre-motion story reel; Chinese lyrics burned in", "-movflags", "+faststart", str(staging_chinese)])
        print("Checking exact frame counts and audio duration", flush=True)
        checks = {"clean": conform(staging_clean, state), "zh": conform(staging_chinese, state)}
        report = {"stage": "pre-motion story reel", "fps": FPS, "width": WIDTH, "height": HEIGHT, "frames": state["total"],
                  "video_seconds": state["total"] / FPS, "master_audio_seconds": str(state["duration"]),
                  "audio_sha256": digest(state["audio"]), "font": state["font"], "fit": "contain",
                  "camera_motion": "none", "transitions": "hard cuts", "subtitle_cues": len(state["lyrics"]),
                  "unique_composed_stills": len(cache), "shot_ids": [s["id"] for s in state["shots"]],
                  "inputs": {str(s["asset"].relative_to(ROOT) if s["asset"].is_relative_to(ROOT) else s["asset"]): digest(s["asset"])
                             for s in state["shots"]},
                  "outputs": {"clean": str(clean), "zh": str(chinese), "srt": str(srt)}, "conformance": checks,
                  "limitations": ["Held-keyframe pre-motion board; no generated dance motion.", "Audio preserved in timing; MP4 delivery encodes AAC once.",
                                  "Human playback review remains required for lyric synchronization, music and intended pacing."]}
        staged_report = scratch / "report.json"
        staged_report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        # Validated files replace their previous versions only after both exports pass.
        for source, destination in ((staging_clean, clean), (staging_chinese, chinese), (staging_srt, srt), (staged_report, report_path)):
            shutil.move(str(source), str(destination))
        print(json.dumps(report["outputs"], ensure_ascii=False), flush=True)
    finally:
        if keep_cache:
            print(f"Intermediate cache: {scratch}", flush=True)
        else:
            shutil.rmtree(scratch)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path)
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--keep-cache", action="store_true")
    parser.add_argument("--preset", choices=["ultrafast", "superfast", "veryfast", "faster", "fast", "medium", "slow"], default="fast")
    parser.add_argument("--crf", type=int, default=18)
    args = parser.parse_args()
    if not 0 <= args.crf <= 51:
        parser.error("--crf must be between 0 and 51")
    state = validate(json.loads(args.config.read_text(encoding="utf-8")))
    print(f"Validated {len(state['shots'])} shots, {len(state['lyrics'])} lyric cues, {state['total']} frames; master {state['duration']} seconds", flush=True)
    if not args.validate_only:
        render(state, args.keep_cache, args.preset, args.crf)


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as error:
        print(f"Command failed ({error.returncode}): {' '.join(error.cmd)}\n{error.stderr or error.stdout}", file=sys.stderr)
        sys.exit(error.returncode or 1)
    except (OSError, ValueError, KeyError, RuntimeError) as error:
        print(f"Render failed: {error}", file=sys.stderr)
        sys.exit(1)
