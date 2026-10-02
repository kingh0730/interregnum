#!/usr/bin/env python3
"""Assemble the two First Day motion benchmarks at their returned native speed.

Run from any directory with Python 3 and ffmpeg/ffprobe on PATH. The excerpts use
the approved song master at provisional shot positions, not a beat-synced edit.
All returned video frames are retained; provider audio is never mapped.
"""

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "work/first-day/motion-test"
RENDERS = ROOT / "renders/first-day"
MASTER = ROOT / "work/first-day/audio/master.wav"
FPS = 24
SAMPLE_RATE = 44100
CLIPS = [
    {"id": "m10", "name": "solo", "song_start": Fraction(820, 24)},
    {"id": "m42", "name": "duet", "song_start": Fraction(4574, 24)},
]


def run(args):
    result = subprocess.run(args, check=True, capture_output=True)
    return result.stdout


def probe(path):
    return json.loads(run([
        "ffprobe", "-v", "error", "-count_frames", "-show_streams",
        "-show_format", "-of", "json", str(path),
    ]))


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def nearest_sample(seconds):
    return int(seconds * SAMPLE_RATE + Fraction(1, 2))


def relative(path):
    return str(path.relative_to(ROOT))


def render(clips, suffix):
    destination = RENDERS / f"first_day_motion_test{suffix}.mp4"
    temporary = WORK / destination.name
    args = ["ffmpeg", "-hide_banner", "-v", "error", "-y"]
    filters, timeline = [], []
    frame_cursor = 0
    for index, clip in enumerate(clips):
        args += ["-i", str(clip["path"])]
        start_sample = nearest_sample(clip["song_start"])
        first_sample = nearest_sample(Fraction(frame_cursor, FPS))
        end_frame = frame_cursor + clip["frames"]
        end_sample = nearest_sample(Fraction(end_frame, FPS))
        sample_count = end_sample - first_sample
        filters += [
            f"[{index}:v:0]setpts=PTS-STARTPTS,"
            "scale=1920:1080:force_original_aspect_ratio=decrease:"
            "force_divisible_by=2:flags=lanczos,"
            f"pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black,setsar=1[v{index}]",
            f"[{len(clips)}:a:0]atrim=start_sample={start_sample}:"
            f"end_sample={start_sample + sample_count},"
            f"asetpts=PTS-STARTPTS[a{index}]",
        ]
        timeline.append({
            "id": clip["id"], "name": clip["name"],
            "source": relative(clip["path"]),
            "source_video_frames": [0, clip["frames"]],
            "output_frames": [frame_cursor, end_frame],
            "output_audio_samples": [first_sample, end_sample],
            "master_audio_samples": [start_sample, start_sample + sample_count],
            "master_start_seconds": float(clip["song_start"]),
        })
        frame_cursor = end_frame
    args += ["-i", str(MASTER)]
    video_labels = "".join(f"[v{i}]" for i in range(len(clips)))
    audio_labels = "".join(f"[a{i}]" for i in range(len(clips)))
    filters += [f"{video_labels}concat=n={len(clips)}:v=1:a=0[vout]",
                f"{audio_labels}concat=n={len(clips)}:v=0:a=1[aout]"]
    args += [
        "-filter_complex", ";".join(filters), "-map", "[vout]", "-map", "[aout]",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-pix_fmt", "yuv420p", "-fps_mode", "passthrough",
        "-video_track_timescale", "24000", "-movie_timescale", "3528000",
        "-c:a", "aac", "-b:a", "256k", "-ar", str(SAMPLE_RATE), "-ac", "2",
        "-movflags", "+faststart", "-map_metadata", "-1",
        "-metadata", "title=First Day - motion benchmark excerpts",
        "-metadata", "comment=MiniMax H3 Max. Full returned takes at native speed; "
        "approved song excerpts at provisional positions. Not the final edit.",
        str(temporary),
    ]
    (WORK / f"{destination.stem}.command.json").write_text(
        json.dumps(args, ensure_ascii=False, indent=2) + "\n")
    run(args)
    result = probe(temporary)
    videos = [s for s in result["streams"] if s["codec_type"] == "video"]
    audios = [s for s in result["streams"] if s["codec_type"] == "audio"]
    assert len(videos) == len(audios) == 1, result
    video, audio = videos[0], audios[0]
    duration = Fraction(frame_cursor, FPS)
    samples = nearest_sample(duration)
    assert int(video["nb_read_frames"]) == frame_cursor, video
    assert (video["width"], video["height"]) == (1920, 1080), video
    assert Fraction(video["avg_frame_rate"]) == FPS, video
    assert abs(float(video["duration"]) - float(duration)) < 0.00001, video
    assert (int(audio["sample_rate"]), audio["channels"]) == (SAMPLE_RATE, 2), audio
    audio_duration = Fraction(audio["duration_ts"]) * Fraction(audio["time_base"])
    assert abs(audio_duration - Fraction(samples, SAMPLE_RATE)) <= Fraction(1, SAMPLE_RATE), audio
    run(["ffmpeg", "-hide_banner", "-v", "error", "-xerror", "-i", str(temporary),
         "-map", "0:v:0", "-map", "0:a:0", "-f", "null", "-"])
    temporary.replace(destination)
    result["format"]["filename"] = str(destination)
    return {
        "path": relative(destination), "sha256": sha256(destination),
        "frames": frame_cursor, "duration_seconds": float(duration),
        "audio_samples": samples, "full_decode": "pass",
        "timeline": timeline, "probe": result,
    }


def main():
    WORK.mkdir(parents=True, exist_ok=True)
    RENDERS.mkdir(parents=True, exist_ok=True)
    master_probe = probe(MASTER)
    master_audio = master_probe["streams"][0]
    assert (int(master_audio["sample_rate"]), master_audio["channels"]) == (SAMPLE_RATE, 2)
    sources = []
    for clip in CLIPS:
        clip["path"] = ROOT / f"work/first-day/motion/{clip['id']}.mp4"
        info = probe(clip["path"])
        stream = next(s for s in info["streams"] if s["codec_type"] == "video")
        assert Fraction(stream["avg_frame_rate"]) == FPS, stream
        clip["frames"] = int(stream["nb_read_frames"])
        sources.append({"id": clip["id"], "path": relative(clip["path"]),
                        "sha256": sha256(clip["path"]), "probe": info})
    outputs = [render([clip], f"_{clip['name']}") for clip in CLIPS]
    outputs.append(render(CLIPS, ""))
    report = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "status": "technical_checks_pass",
        "script": relative(Path(__file__).resolve()),
        "script_sha256": sha256(Path(__file__).resolve()),
        "method": "Full returned frames, native 24 fps, contain fit to 1920x1080. "
        "Direct cut between isolated excerpts. No provider audio, retiming, captions or added camera motion.",
        "review_scope": "Technical verification only; choreography, continuity and beat sync require playback review.",
        "ranges": "All frame and sample ranges are start-inclusive, end-exclusive.",
        "audio_rounding": "Nearest sample at each output frame boundary (half up); at most half a sample rounding.",
        "master_audio": {"path": relative(MASTER), "sha256": sha256(MASTER)},
        "sources": sources, "outputs": outputs,
    }
    report_path = WORK / "preview_technical_report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"report": relative(report_path), "outputs": [
        {k: out[k] for k in ("path", "frames", "duration_seconds", "sha256")}
        for out in outputs]}, indent=2))


if __name__ == "__main__":
    main()
