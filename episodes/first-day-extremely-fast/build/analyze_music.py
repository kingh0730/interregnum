"""Measure the supplied music without altering it; beat estimates are not listening approval.

Run: uv run --with numpy --with scipy --with matplotlib python
     episodes/first-day-extremely-fast/build/analyze_music.py
"""
from pathlib import Path
import hashlib
import importlib.metadata
import json
import re
import subprocess

import numpy as np
from scipy import signal, ndimage
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
EP = ROOT / "episodes/first-day-extremely-fast"
OUT = ROOT / "work/first-day-extremely-fast/audio"
OUT.mkdir(parents=True, exist_ok=True)
SOURCE = EP / "first-day.wav"
FPS = 60


def main():
    probe = json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", str(SOURCE)
    ]))
    duration = float(probe["format"]["duration"])
    sr = 22050
    data = subprocess.check_output([
        "ffmpeg", "-v", "error", "-i", str(SOURCE), "-ac", "1", "-ar", str(sr),
        "-f", "f32le", "pipe:1"
    ])
    y = np.frombuffer(data, dtype="<f4")
    hop, nfft = 220, 2048
    freq, times, spec = signal.stft(y, sr, nperseg=nfft, noverlap=nfft-hop, boundary="zeros")
    power = np.abs(spec)**2
    bands = {"bass": (35, 180), "mid": (180, 2000), "high": (2000, 10000)}
    energy = {name: np.sum(power[(freq >= lo) & (freq < hi)], axis=0)
              for name, (lo, hi) in bands.items()}
    # Spectral flux with a local background removed. It estimates transients, not words.
    compressed = np.log1p(1000 * np.abs(spec))
    flux = np.maximum(np.diff(compressed, axis=1), 0).sum(axis=0)
    flux = np.r_[0.0, flux]
    flux = np.maximum(flux - ndimage.median_filter(flux, size=31), 0)
    flux /= max(float(np.max(flux)), 1e-12)
    # Separate bass novelty helps inspect whether a double/half-time candidate is plausible.
    basslog = np.log(energy["bass"] + 1e-12)
    bassnov = np.maximum(np.r_[0, np.diff(basslog)], 0)
    bassnov /= max(float(np.max(bassnov)), 1e-12)
    onset = 0.72 * flux + 0.28 * bassnov
    smooth = ndimage.gaussian_filter1d(onset, 1.5)
    ac = signal.fftconvolve(onset - onset.mean(), (onset - onset.mean())[::-1], mode="full")
    ac = ac[len(onset)-1:]
    ac /= max(float(ac[0]), 1e-12)
    bpms = np.arange(65, 221, .01)
    periods = 60 / bpms
    corr = np.interp(periods / (hop/sr), np.arange(len(ac)), ac)
    peaks, _ = signal.find_peaks(corr, distance=100)
    ranked = sorted(peaks, key=lambda i: corr[i], reverse=True)[:12]
    candidates = []
    for i in ranked:
        bpm, period = float(bpms[i]), float(periods[i])
        best = (-1, 0)
        for phase in np.arange(0, period, .001):
            grid = np.arange(phase, duration, period)
            value = float(np.mean(np.interp(grid, times, smooth)))
            if value > best[0]:
                best = (value, float(phase))
        candidates.append({"bpm": round(bpm, 3), "period_s": round(period, 6),
                           "autocorrelation": round(float(corr[i]), 4),
                           "phase_s": round(best[1], 4), "grid_flux_score": round(best[0], 4)})
    onset_idx, _ = signal.find_peaks(smooth, distance=int(.085/(hop/sr)), prominence=.035)
    onsets = [{"time": round(float(times[i]), 4), "strength": round(float(smooth[i]), 4)}
              for i in onset_idx]
    lyrics = []
    for i, (mm, ss, text) in enumerate(re.findall(r"\[(\d+):(\d+\.\d+)\](.*)", (EP/"first-day.lrc").read_text())):
        sec = int(mm)*60+float(ss)
        lyrics.append({"id": f"L{i+1:02}", "start": sec, "frame_60fps": round(sec*FPS), "text": text.strip(),
                       "timing_source": "supplied LRC; line-level, not phoneme-aligned"})
    for i, line in enumerate(lyrics):
        line["end"] = lyrics[i+1]["start"] if i+1<len(lyrics) else duration
    rms = np.sqrt(ndimage.uniform_filter1d(y.astype(float)**2, size=int(sr*.1))[::hop])
    rms_times = np.arange(len(rms))*hop/sr
    ff = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(SOURCE),
                         "-af", "ebur128=peak=true:framelog=verbose", "-f", "null", "-"],
                        stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True, check=True)
    (OUT/"loudness.txt").write_text(ff.stderr)
    summary = ff.stderr.split("Summary:")[-1]
    report = {
        "source": str(SOURCE.relative_to(ROOT)), "sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "source_lrc_sha256": hashlib.sha256((EP/"first-day.lrc").read_bytes()).hexdigest(),
        "duration_s": duration, "sample_rate": int(probe["streams"][0]["sample_rate"]),
        "sample_count": probe["streams"][0]["duration_ts"], "channels": 2, "bits_per_sample": 24,
        "delivery_fps_plan": FPS, "delivery_frames_plan": int(np.ceil(duration*FPS)),
        "delivery_duration_s_plan": int(np.ceil(duration*FPS))/FPS,
        "tail_padding_s_plan": int(np.ceil(duration*FPS))/FPS-duration,
        "source_untouched": True, "audio_playback_review": "not performed",
        "loudness_ffmpeg_summary": summary.strip(), "tempo_candidates": candidates,
        "tempo_status": "automatic periodicity candidates; metrical interpretation and sync pending listening",
        "lyrics": lyrics, "onset_candidates": onsets,
        "versions": {m: importlib.metadata.version(m) for m in ["numpy", "scipy", "matplotlib"]},
    }
    (EP/"build/music_analysis.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    np.savez_compressed(OUT/"features.npz", times=times, flux=flux, bass_novelty=bassnov, **energy)
    plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(4, 1, figsize=(17, 10), sharex=True,
                             gridspec_kw={"height_ratios": [1,1,1,1.2]})
    axes[0].fill_between(rms_times, -rms, rms, color="#18645f")
    axes[0].set_ylabel("100 ms RMS")
    axes[1].plot(times, flux, color="#ba4f33", linewidth=.7, label="spectral flux")
    axes[1].plot(times, bassnov, color="#335c96", linewidth=.5, alpha=.6, label="bass novelty")
    axes[1].legend(loc="upper left")
    for name, vals in energy.items():
        axes[2].plot(times, 10*np.log10(vals+1e-12), linewidth=.65, label=name)
    axes[2].legend(loc="upper left")
    axes[2].set_ylabel("Band power (dB)")
    for n, cand in enumerate(candidates[:3]):
        grid = np.arange(cand["phase_s"], duration, 60/cand["bpm"])
        axes[3].vlines(grid, n+.1, n+.8, color=["#ba4f33", "#18645f", "#335c96"][n], linewidth=.65)
        axes[3].text(.1, n+.83, f"Candidate {cand['bpm']:.2f} BPM", fontsize=9)
    axes[3].set_ylim(0,3.4)
    axes[3].set_yticks([])
    axes[3].set_xlabel("Source time (s) — all grids provisional")
    for line in lyrics:
        for ax in axes:
            ax.axvline(line["start"], color="#111111", linewidth=.6, alpha=.25)
        axes[0].text(line["start"]+.04, max(rms)*1.04, line["id"], fontsize=9)
    axes[0].set_ylim(-max(rms)*1.1,max(rms)*1.3)
    axes[-1].set_xlim(0,duration)
    fig.suptitle("FIRST DAY / supplied source — 43.670 s / measurement, not listening approval", fontsize=18, x=.06, ha="left")
    fig.tight_layout()
    fig.savefig(OUT/"music_map.png", dpi=150)
    print(json.dumps({k: report[k] for k in ["duration_s", "sample_count", "delivery_frames_plan", "tempo_candidates", "loudness_ffmpeg_summary"]}, indent=2))


if __name__ == "__main__":
    main()
