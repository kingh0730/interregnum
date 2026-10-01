#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["librosa==0.11.0", "numpy==2.3.3", "scipy==1.16.2"]
# ///
"""Analyze the supplied First Day recording, preserve it, and build lyric sidecars.

Run from any directory: uv run episodes/first-day/build/analyze_audio.py
All recorded paths are relative to the repository root. No paid services are used.
The original MP3 and LRC are read-only. The master applies only one static gain;
analysis resampling never enters the master signal path.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import subprocess
from collections import Counter
from pathlib import Path

import librosa
import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "episodes/first-day/first-day.mp3"
LRC = ROOT / "episodes/first-day/first-day.lrc"
OUT = ROOT / "work/first-day/audio"
BUILD = ROOT / "episodes/first-day/build"
ANALYSIS_SR = 22050
HOP = 256

# Boundaries come from the supplied LRC; instrumental endpoints are editorial,
# provisional hold limits, not claimed vocal forced alignment.
SECTIONS = [
    ("instrumental_intro", 0.0, 25.42),
    ("verse_1", 25.42, 46.71),
    ("prechorus_1", 46.71, 58.79),
    ("chorus_1", 58.79, 84.51),
    ("instrumental_turnaround", 84.51, 93.68),
    ("verse_2", 93.68, 114.93),
    ("prechorus_2", 114.93, 126.90),
    ("chorus_2", 126.90, 151.27),
    ("call_response", 151.27, 166.86),
    ("instrumental_bridge", 166.86, 179.13),
    ("prechorus_3", 179.13, 191.05),
    ("chorus_3", 191.05, 215.40),
    ("extended_hook", 215.40, 223.06),
    ("english_refrain", 223.06, 243.96),
    ("instrumental_outro", 243.96, None),
]


def run(args: list[str], *, binary: bool = False):
    # This supplied MP3 has legacy-encoded ID3 strings; they must not make a
    # UTF-8 diagnostic log fail. The authoritative credits are the UTF-8 LRC.
    kwargs = {} if binary else {"encoding": "utf-8", "errors": "replace"}
    return subprocess.run(args, check=True, capture_output=True, text=not binary, **kwargs)


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def probe(path: Path) -> dict:
    return json.loads(run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)]).stdout)


def loudness(path: Path) -> dict:
    proc = run(["ffmpeg", "-hide_banner", "-nostdin", "-i", str(path), "-map", "0:a:0", "-af", "ebur128=peak=true", "-f", "null", "-"])
    summary = proc.stderr.rsplit("Summary:", 1)[-1]
    patterns = {"integrated_lufs": r"I:\s*(-?[\d.]+) LUFS", "lra_lu": r"LRA:\s*([\d.]+) LU", "true_peak_dbtp": r"Peak:\s*(-?[\d.]+) dBFS"}
    result = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, summary)
        if not match:
            raise RuntimeError(f"Cannot parse {key} from ffmpeg summary: {summary}")
        result[key] = float(match.group(1))
    return result


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pending = path.with_name(path.name + ".tmp")
    pending.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")
    pending.replace(path)


def parse_lrc(duration: float) -> tuple[list, list]:
    metadata, lyrics = [], []
    counts = Counter()
    for line_number, line in enumerate(LRC.read_text(encoding="utf-8-sig").splitlines(), 1):
        match = re.fullmatch(r"\[(\d+):(\d+(?:\.\d+)?)\](.*)", line)
        if not match:
            if line.strip():
                raise ValueError(f"Unparsed LRC line {line_number}")
            continue
        minutes, seconds, text = match.groups()
        start = round(60 * int(minutes) + float(seconds), 3)
        if text.startswith(("词：", "曲：", "编曲：")) or (not lyrics and start == 0):
            metadata.append({"source_line": line_number, "timestamp": start, "text": text})
            continue
        counts[text] += 1
        lyrics.append({"id": f"L{len(lyrics)+1:03d}", "source_line": line_number, "start": start, "text": text, "text_occurrence": counts[text], "timing_source": "supplied_lrc", "alignment_status": "provisional_not_vocal_forced_aligned"})
    for i, lyric in enumerate(lyrics):
        next_start = lyrics[i + 1]["start"] if i + 1 < len(lyrics) else duration
        gap = next_start - lyric["start"]
        if gap > 6:
            lyric["end"] = round(min(lyric["start"] + 3.5, duration), 3)
            lyric["end_policy"] = "3.5s_hold_cap_before_long_gap_or_outro; editorial_not_vocal_offset"
        else:
            lyric["end"] = round(min(next_start - 0.06, duration), 3)
            lyric["end_policy"] = "next_supplied_onset_minus_60ms; editorial_not_vocal_offset"
        assert 0 <= lyric["start"] < lyric["end"] <= duration
    assert len({x["id"] for x in lyrics}) == len(lyrics)
    assert all(a["end"] <= b["start"] for a, b in zip(lyrics, lyrics[1:]))
    return metadata, lyrics


def srt_time(t: float) -> str:
    millis = round(t * 1000)
    hours, millis = divmod(millis, 3600000)
    minutes, millis = divmod(millis, 60000)
    seconds, millis = divmod(millis, 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{millis:03d}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target-lufs", type=float, default=-16.0)
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    source_sha, lrc_sha = sha(SOURCE), sha(LRC)
    source_probe = probe(SOURCE)
    stream = next(s for s in source_probe["streams"] if s["codec_type"] == "audio")
    packet_duration = float(source_probe["format"]["duration"])
    source_rate = int(stream["sample_rate"])
    source_levels = loudness(SOURCE)
    gain = round(args.target_lufs - source_levels["integrated_lufs"], 6)
    # If an unusual source needs peak protection, lower the single static gain;
    # do not change its envelope with a limiter.
    gain = min(gain, -1.0 - source_levels["true_peak_dbtp"])
    master = OUT / "master.wav"
    pending_master = OUT / ".master.build.wav"
    run(["ffmpeg", "-hide_banner", "-nostdin", "-y", "-i", str(SOURCE), "-map", "0:a:0", "-af", f"volume={gain:.6f}dB", "-c:a", "pcm_f32le", "-ar", str(source_rate), str(pending_master)])
    master_probe = probe(pending_master)
    master_stream = master_probe["streams"][0]
    duration = float(master_stream["duration"])
    samples = int(master_stream["duration_ts"])
    master_levels = loudness(pending_master)
    expected_pcm_md5 = run(["ffmpeg", "-v", "error", "-nostdin", "-i", str(SOURCE), "-map", "0:a:0", "-af", f"volume={gain:.6f}dB", "-c:a", "pcm_f32le", "-f", "md5", "-"]).stdout.strip()
    master_pcm_md5 = run(["ffmpeg", "-v", "error", "-nostdin", "-i", str(pending_master), "-map", "0:a:0", "-c:a", "pcm_f32le", "-f", "md5", "-"]).stdout.strip()
    assert expected_pcm_md5 == master_pcm_md5, "Master differs from source decoded with static gain"
    pending_master.replace(master)
    raw = run(["ffmpeg", "-v", "error", "-nostdin", "-i", str(SOURCE), "-map", "0:a:0", "-ac", "1", "-ar", str(ANALYSIS_SR), "-f", "f32le", "-"], binary=True).stdout
    y = np.frombuffer(raw, dtype="<f4")
    onset_env = librosa.onset.onset_strength(y=y, sr=ANALYSIS_SR, hop_length=HOP)
    onset_times_all = librosa.frames_to_time(np.arange(len(onset_env)), sr=ANALYSIS_SR, hop_length=HOP)
    onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=ANALYSIS_SR, hop_length=HOP, backtrack=False)
    onset_times = librosa.frames_to_time(onset_frames, sr=ANALYSIS_SR, hop_length=HOP)
    tempo, beat_frames = librosa.beat.beat_track(onset_envelope=onset_env, sr=ANALYSIS_SR, hop_length=HOP, start_bpm=120, trim=False)
    tempo = float(np.asarray(tempo).ravel()[0])
    beat_times = librosa.frames_to_time(beat_frames, sr=ANALYSIS_SR, hop_length=HOP)
    # Tempo candidates expose half/double-time ambiguity instead of hiding it.
    autocorr = librosa.autocorrelate(onset_env, max_size=round(ANALYSIS_SR / HOP * 3))
    candidates = []
    for lag in range(1, len(autocorr) - 1):
        bpm = 60 * ANALYSIS_SR / HOP / lag
        if 60 <= bpm <= 220 and autocorr[lag] >= autocorr[lag - 1] and autocorr[lag] > autocorr[lag + 1]:
            candidates.append({"bpm": round(bpm, 3), "lag_frames": lag, "normalized_correlation": round(float(autocorr[lag] / autocorr[0]), 5)})
    candidates = sorted(candidates, key=lambda x: x["normalized_correlation"], reverse=True)[:8]
    rms = librosa.feature.rms(y=y, frame_length=2048, hop_length=HOP)[0]
    centroid = librosa.feature.spectral_centroid(y=y, sr=ANALYSIS_SR, n_fft=2048, hop_length=HOP)[0]
    feature_times = librosa.frames_to_time(np.arange(len(rms)), sr=ANALYSIS_SR, hop_length=HOP)
    frame_db = 20 * np.log10(np.maximum(rms, 1e-10))
    beat_inspection = []
    for t in beat_times:
        nearest = float(onset_times[np.argmin(np.abs(onset_times - t))])
        level = float(frame_db[min(round(t * ANALYSIS_SR / HOP), len(frame_db) - 1)])
        supported = abs(nearest - t) <= 0.14 and level > -50
        beat_inspection.append({"time": round(float(t), 6), "nearest_onset": round(nearest, 6), "onset_distance_seconds": round(abs(nearest - float(t)), 6), "source_frame_rms_dbfs": round(level, 3), "transient_supported_candidate": bool(supported)})
    sections = []
    for name, start, planned_end in SECTIONS:
        end = duration if planned_end is None else planned_end
        mask = (feature_times >= start) & (feature_times < end)
        onset_mask = (onset_times >= start) & (onset_times < end)
        onset_feature_mask = (onset_times_all >= start) & (onset_times_all < end)
        section_y = y[round(start * ANALYSIS_SR):round(end * ANALYSIS_SR)]
        section_rms = math.sqrt(float(np.mean(section_y.astype(np.float64) ** 2)))
        sections.append({"id": name, "start": start, "end": round(end, 6), "boundary_basis": "supplied_lyric_start_or_editorial_vocal_hold_cap", "source_rms_dbfs": round(20 * math.log10(max(section_rms, 1e-10)), 3), "frame_rms_dbfs_p10_p50_p90": [round(float(v), 3) for v in np.percentile(frame_db[mask], [10, 50, 90])], "spectral_centroid_hz_median": round(float(np.median(centroid[mask])), 2), "onsets_per_second": round(float(np.count_nonzero(onset_mask) / (end - start)), 3), "onset_strength_mean": round(float(np.mean(onset_env[onset_feature_mask])), 4)})
    metadata, lyrics = parse_lrc(duration)
    alignment = []
    for lyric in lyrics:
        window = (onset_times >= lyric["start"] - 0.75) & (onset_times <= lyric["start"] + 0.75)
        local = onset_times[window]
        nearest = float(local[np.argmin(np.abs(local - lyric["start"]))]) if len(local) else None
        alignment.append({"id": lyric["id"], "lrc_start": lyric["start"], "nearest_mixed_audio_onset": round(nearest, 6) if nearest is not None else None, "onset_minus_lrc_seconds": round(nearest - lyric["start"], 6) if nearest is not None else None, "onsets_in_1_5s_window": int(len(local)), "interpretation": "instrument_or_voice_transient_only; does_not_verify_sung_word_onset"})
    onsets = [{"time": round(float(t), 6), "strength": round(float(onset_env[f]), 5)} for f, t in zip(onset_frames, onset_times)]
    # Retain sparse source waveform-envelope observations, not another huge PCM file.
    envelope = []
    for second in np.arange(0, duration, 0.5):
        a, b = round(second * ANALYSIS_SR), min(round((second + 0.5) * ANALYSIS_SR), len(y))
        chunk = y[a:b]
        envelope.append({"start": round(float(second), 3), "rms_dbfs": round(20 * math.log10(max(float(np.sqrt(np.mean(chunk ** 2))), 1e-10)), 3), "peak_dbfs": round(20 * math.log10(max(float(np.max(np.abs(chunk))), 1e-10)), 3)})
    analysis = {"schema_version": 1, "source": {"path": relative(SOURCE), "sha256": source_sha, "sample_rate": source_rate, "channels": stream["channels"], "codec": stream["codec_name"], "bit_rate": int(stream["bit_rate"]), "packet_duration_seconds": packet_duration, "stream_start_time_seconds": float(stream.get("start_time", 0)), "loudness": source_levels}, "master": {"path": relative(master), "sample_rate": int(master_stream["sample_rate"]), "channels": master_stream["channels"], "codec": master_stream["codec_name"], "decoded_samples_per_channel": samples, "duration_seconds": duration, "packet_minus_decoded_duration_seconds": round(packet_duration - duration, 9), "static_gain_db": gain, "loudness": master_levels, "limiter": False, "resampled": False, "time_stretched": False, "edits": [], "duration_note": "ffmpeg honors MP3 encoder delay/padding when decoding; PCM preserves all decoded audible samples, not packet padding"}, "analysis_method": {"sample_rate": ANALYSIS_SR, "hop_length_samples": HOP, "frame_resolution_seconds": HOP / ANALYSIS_SR, "signal": "mono analysis copy only", "librosa_version": librosa.__version__, "limitations": ["No listening or perceptual sound approval is claimed.", "Mixed-track onsets often belong to drums or instruments, not vocal syllables.", "Beat tracker has half/double-time and phase ambiguity; candidates are editing aids.", "Section labels follow supplied lyrics; musical boundaries and lyric ends are provisional."]}, "tempo": {"beat_tracker_bpm": round(tempo, 4), "half_time_bpm": round(tempo / 2, 4), "double_time_bpm": round(tempo * 2, 4), "autocorrelation_candidates": candidates}, "beat_times": [round(float(t), 6) for t in beat_times], "onsets": onsets, "sections": sections, "waveform_envelope_0_5s": envelope, "lrc_alignment_inspection": alignment}
    analysis["master"]["duration_note"] = "All native decoded samples retained. This source's decoded PCM duration equals its MP3 packet duration; no padding was added."
    analysis["master"]["pcm_verification"] = {"method": "MD5 of decoded float32 PCM compared to source decode plus only specified static gain", "expected": expected_pcm_md5, "actual": master_pcm_md5, "match": True}
    analysis["beat_times_note"] = "Full predictive tracker grid, not verified downbeats; it can extend through silence. Prefer transient-supported candidates and inspect the actual music."
    analysis["beat_inspection"] = beat_inspection
    analysis["beat_anchor_candidates"] = [b["time"] for b in beat_inspection if b["transient_supported_candidate"]]
    lyrics_doc = {"schema_version": 1, "source": relative(LRC), "source_sha256": lrc_sha, "language": "zh-Hans with original supplied English refrain preserved", "metadata_entries_not_subtitles": metadata, "cues": lyrics, "alignment_notes": "Starts are copied exactly from the supplied LRC, never shifted to a mixed-track transient. End times are editorial holds, not verified sung-word offsets. Long gaps/outro capped at 3.5 seconds to prevent lingering captions. Every occurrence has a unique id.", "no_translation_or_added_lyrics": True}
    plan = {"schema_version": 1, "episode": "first-day", "source_audio": relative(SOURCE), "source_lyrics": relative(LRC), "source_sha256": source_sha, "source_lyrics_sha256": lrc_sha, "master_audio": relative(master), "source_packet_duration_seconds": packet_duration, "master_decoded_duration_seconds": duration, "source_sample_rate": source_rate, "master_sample_rate": int(master_stream["sample_rate"]), "analysis_sample_rate": ANALYSIS_SR, "static_gain_db": gain, "target_integrated_lufs": args.target_lufs, "measured_master": master_levels, "signal_path": "decode MP3 at native sample rate -> one static gain -> stereo float PCM WAV", "preserve_entire_song": True, "audio_cuts": [], "added_sfx": [], "added_dialogue": [], "added_music": [], "forced_silence": False, "limiter": False, "lyric_data": relative(BUILD / "lyrics.json"), "subtitle_srt": relative(OUT / "lyrics.srt"), "analysis": relative(OUT / "audio_analysis.json"), "visual_sync_guidance": "Use lyric timestamps as provisional phrase anchors and mixed-audio onsets/beat_times as possible cut points. Do not edit or time-stretch the song to conform the image plan. Preserve native decoded audio duration: measured 253.960000s, equal to this MP3 packet duration.", "review_pending": ["Human listening: supplied lyric onset/offset alignment, beat phase, master loudness, and final visual/music relationship."]}
    write_json(OUT / "audio_analysis.json", analysis)
    write_json(BUILD / "lyrics.json", lyrics_doc)
    write_json(BUILD / "audio_plan.json", plan)
    (OUT / "lyrics.srt").write_text("\n\n".join(f"{i}\n{srt_time(row['start'])} --> {srt_time(row['end'])}\n{row['text']}" for i, row in enumerate(lyrics, 1)) + "\n", encoding="utf-8")
    assert sha(SOURCE) == source_sha and sha(LRC) == lrc_sha, "Source files changed during processing"
    assert int(master_stream["sample_rate"]) == source_rate and master_stream["channels"] == stream["channels"]
    assert abs(master_levels["integrated_lufs"] - args.target_lufs) <= 0.2
    print(json.dumps({"source": analysis["source"], "master": analysis["master"], "tempo": analysis["tempo"], "lyric_count": len(lyrics), "metadata_count": len(metadata), "last_subtitle_end": lyrics[-1]["end"], "sections": sections}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
