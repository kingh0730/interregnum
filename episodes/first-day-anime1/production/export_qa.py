"""Inspect encoded streams, decode integrity and audio alignment against original MP3."""
from pathlib import Path
import json, subprocess
import numpy as np
from scipy.signal import correlate, correlation_lags

root = Path(__file__).resolve().parents[1]
movie = root / 'first-day_opus55_1080p30.mp4'
probe = json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-count_frames', '-show_streams', '-show_format', '-of', 'json', str(movie)]))
video = next(s for s in probe['streams'] if s['codec_type'] == 'video')
audio = next(s for s in probe['streams'] if s['codec_type'] == 'audio')
errors = []
if (video['width'], video['height'], video['r_frame_rate'], int(video['nb_read_frames'])) != (1920, 1080, '30/1', 1311): errors.append('video format/count')
if any(video.get(k) != 'bt709' for k in ['color_space', 'color_transfer', 'color_primaries']): errors.append('colour tags')
decode = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(movie), '-f', 'null', '-'], capture_output=True, text=True)
if decode.returncode or decode.stderr: errors.append('decode: ' + decode.stderr)

def pcm(path):
    return np.frombuffer(subprocess.check_output(['ffmpeg', '-v', 'error', '-i', str(path), '-vn', '-ac', '1', '-ar', '22050', '-f', 'f32le', '-']), dtype='<f4')

original, encoded = pcm(root / 'first-day.mp3'), pcm(movie)
alignment = []
for seconds in [2, 11, 24, 38]:
    a = int(seconds * 22050); b = a + 3 * 22050
    x, y = original[a:b], encoded[a:b]
    corr = correlate(y, x, method='fft'); lags = correlation_lags(len(y), len(x)); eligible = np.abs(lags) <= 2205
    lag = int(lags[eligible][np.argmax(corr[eligible])])
    score = float(np.corrcoef(x[:len(y)], y)[0, 1])
    alignment.append({'start_seconds': seconds, 'lag_samples_22050': lag, 'correlation_at_zero': score})
    if abs(lag) > 1 or score < .99: errors.append(['audio_alignment', seconds, lag, score])
report = {'passed': not errors, 'errors': errors, 'video_frames': int(video['nb_read_frames']), 'video_duration': float(video['duration']), 'original_decoded_duration': len(original) / 22050, 'encoded_decoded_duration': len(encoded) / 22050, 'audio_stream': audio, 'audio_alignment': alignment, 'decode_errors': decode.stderr, 'duration_tolerance_exception': 'Exact 1311 frames require 43.700 s; original song is 43.670 s. Preserve both without retiming.', 'manual_audiovisual_playback_verified': False}
(root / 'production/export-probe.json').write_text(json.dumps(probe, indent=2) + '\n')
(root / 'production/export-qa.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
raise SystemExit(bool(errors))
