"""Offline regressions: no credentials or paid services are used."""
import importlib.util
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def module(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


fal = module('fal_run', 'tools/fal_run.py')
h3 = module('h3_batch', 'tools/video/h3_batch.py')
luma = module('luma_batch', 'tools/imagegen/luma_batch.py')
film = module('film_finish', 'tools/imagegen/film_finish.py')
perform = module('perform2', 'tools/audio/perform2.py')


class FixTests(unittest.TestCase):
    def test_finish_legacy_exact_and_correct_bgr(self):
        import numpy as np
        # Frozen from the pre-fix implementation and its BGR-weight-only correction.
        # Keep independent of git HEAD so committing the fix cannot change the oracle.
        pixels = np.random.default_rng(1).integers(0, 256, (32, 32, 3), dtype=np.uint8)
        legacy = film.finish(pixels, legacy_luminance=True)
        corrected = film.finish(pixels)
        self.assertEqual(hashlib.sha256(legacy.tobytes()).hexdigest(),
                         'c0b8b1f64854799b54df23694efaaa46b48bd2d842bec72c0eaffc2b4d3935ee')
        self.assertEqual(hashlib.sha256(corrected.tobytes()).hexdigest(),
                         '5af10f34287c42d85f7f1e09755a55383336242df269319f1b4b1dfbd8a5bb10')

    def test_inline_json_resume_download_without_reposting(self):
        with tempfile.TemporaryDirectory() as td:
            prefix = Path(td) / 'result'
            payload = json.dumps({'prompt': 'x' * 5000})
            calls = []
            def call(url, key, body=None):
                calls.append((url, body))
                if body is not None:
                    return {'request_id': 'r1', 'status_url': 'status', 'response_url': 'response'}
                if url == 'status':
                    return {'status': 'COMPLETED'}
                return {'image': {'url': 'https://example.test/fresh.jpg'}}
            with patch.dict(os.environ, FAL_KEY='test'), patch.object(sys, 'argv', ['fal', 'endpoint', payload, str(prefix), '--resume']), patch.object(fal, 'call', side_effect=call), patch.object(fal.urllib.request, 'urlretrieve', side_effect=[TimeoutError(), None]):
                with self.assertRaises(TimeoutError):
                    fal.main()
                fal.main()
            self.assertEqual(sum(body is not None for _, body in calls), 1)
            self.assertEqual(json.loads(prefix.with_suffix('.json').read_text())['request_id'], 'r1')

    def test_resume_fingerprints_full_data_uri_payload(self):
        with tempfile.TemporaryDirectory() as td:
            prefix = Path(td) / 'result'
            original = {'prompt': 'test', 'image_url': 'data:image/png;base64,AAAA'}
            def call(url, key, body=None):
                if body is not None:
                    return {'request_id': 'one', 'status_url': 'status', 'response_url': 'response'}
                return {'status': 'COMPLETED'} if url == 'status' else {'image': {'url': 'https://example.test/image.png'}}
            with patch.dict(os.environ, FAL_KEY='test'), patch.object(fal, 'call', side_effect=call) as api, patch.object(fal.urllib.request, 'urlretrieve') as download:
                with patch.object(sys, 'argv', ['fal', 'endpoint', json.dumps(original), str(prefix), '--resume']):
                    fal.main()
                api.reset_mock()
                download.reset_mock()
                # Reordered fields have identical identity and can recover the cached result.
                with patch.object(sys, 'argv', ['fal', 'endpoint', json.dumps(dict(reversed(list(original.items())))), str(prefix), '--resume']):
                    fal.main()
                api.assert_not_called()
                download.assert_called_once()
                download.reset_mock()
                changed = dict(original, image_url='data:image/png;base64,BBBB')
                with patch.object(sys, 'argv', ['fal', 'endpoint', json.dumps(changed), str(prefix), '--resume']):
                    with self.assertRaisesRegex(SystemExit, 'full payload'):
                        fal.main()
                api.assert_not_called()
                download.assert_not_called()
                # A legacy sanitized payload cannot establish which inline image was used.
                lp = prefix.with_suffix('.json')
                log = json.loads(lp.read_text())
                del log['payload_sha256']
                lp.write_text(json.dumps(log))
                with patch.object(sys, 'argv', ['fal', 'endpoint', json.dumps(original), str(prefix), '--resume']):
                    with self.assertRaisesRegex(SystemExit, 'no identity hash'):
                        fal.main()
                api.assert_not_called()
                download.assert_not_called()
                # Ordinary legacy payloads retain enough identity to resume a saved response.
                log['payload'] = {'prompt': 'plain'}
                lp.write_text(json.dumps(log))
                with patch.object(sys, 'argv', ['fal', 'endpoint', '{"prompt":"plain"}', str(prefix), '--resume']):
                    fal.main()
                api.assert_not_called()
                download.assert_called_once()

    def test_ambiguous_fal_post_is_not_repeated(self):
        with tempfile.TemporaryDirectory() as td:
            with patch.dict(os.environ, FAL_KEY='test'), patch.object(sys, 'argv', ['fal', 'endpoint', '{}', td + '/r', '--resume']), patch.object(fal, 'call', side_effect=TimeoutError()) as call:
                with self.assertRaises(TimeoutError):
                    fal.main()
                with self.assertRaises(SystemExit):
                    fal.main()
                self.assertEqual(call.call_count, 1)

    def test_h3_timeout_and_poll_failure_retain_request(self):
        for poll_error in (False, True):
            with self.subTest(poll_error=poll_error), tempfile.TemporaryDirectory() as td:
                man = Path(td) / 'motion.json'
                man.write_text(json.dumps([{'id': 's1', 'prompt': 'move', 'out': 's1.mp4'}]))
                calls = []
                def http(url, key, payload=None, **kw):
                    calls.append((url, payload))
                    if payload is not None:
                        return {'request_id': 'one', 'status_url': 'status', 'response_url': 'response'}
                    if poll_error:
                        raise TimeoutError()
                    return {'status': 'IN_PROGRESS'}
                with patch.dict(os.environ, FAL_KEY='test'), patch.object(sys, 'argv', ['h3', str(man), '--root', td, '--timeout', '-1']), patch.object(h3, 'price', return_value=0.025), patch.object(h3, 'http', side_effect=http):
                    for _ in range(2):
                        with self.assertRaises(SystemExit) as caught:
                            h3.main()
                        self.assertEqual(caught.exception.code, 1)
                self.assertEqual(sum(body is not None for _, body in calls), 1)
                self.assertEqual(json.loads((Path(td) / 'h3_log/s1.json').read_text())['request_id'], 'one')

    def test_h3_ambiguous_submission_never_reposts(self):
        with tempfile.TemporaryDirectory() as td:
            man = Path(td) / 'motion.json'
            man.write_text(json.dumps([{'id': 's1', 'prompt': 'move', 'out': 's1.mp4'}]))
            with patch.dict(os.environ, FAL_KEY='test'), patch.object(sys, 'argv', ['h3', str(man), '--root', td]), patch.object(h3, 'price', return_value=0.025), patch.object(h3, 'http', side_effect=TimeoutError()) as http:
                for _ in range(2):
                    with self.assertRaises(SystemExit):
                        h3.main()
                self.assertEqual(http.call_count, 1)

    def test_h3_resumes_completed_request_and_failed_download(self):
        with tempfile.TemporaryDirectory() as td:
            man = Path(td) / 'motion.json'
            man.write_text(json.dumps([{'id': 's1', 'prompt': 'move', 'out': 's1.mp4'}]))
            logdir = Path(td) / 'h3_log'
            logdir.mkdir()
            (logdir / 's1.json').write_text(json.dumps({'request_id': 'old', 'status_url': 'status',
                'response_url': 'response', 'submitted': 1}))
            def http(url, key, payload=None, **kw):
                self.assertIsNone(payload)
                return {'status': 'COMPLETED'} if url == 'status' else {'video': {'url': 'https://example.test/video.mp4'}}
            attempts = []
            def download(url, dst):
                attempts.append(url)
                if len(attempts) == 1:
                    raise TimeoutError()
                Path(dst).write_bytes(b'test-video')
            with patch.dict(os.environ, FAL_KEY='test'), patch.object(sys, 'argv', ['h3', str(man), '--root', td]), patch.object(h3, 'price', return_value=0.025), patch.object(h3, 'http', side_effect=http), patch.object(h3.urllib.request, 'urlretrieve', side_effect=download):
                with self.assertRaises(SystemExit) as caught:
                    h3.main()
                self.assertEqual(caught.exception.code, 0)
            self.assertEqual(len(attempts), 2)
            self.assertEqual((Path(td) / 's1.mp4').read_bytes(), b'test-video')

    def test_luma_timeout_uses_resume_every_attempt(self):
        with tempfile.TemporaryDirectory() as td:
            man = Path(td) / 'images.json'
            man.write_text(json.dumps([{'id': 's1', 'mode': 't2i', 'prompt': 'test', 'out': 's1.png'}]))
            def timeout(args, **kw):
                self.assertIn('--resume', args)
                raise subprocess.TimeoutExpired(args, 420)
            with patch.object(sys, 'argv', ['luma', str(man)]), patch.object(luma.subprocess, 'run', side_effect=timeout) as run:
                with self.assertRaises(SystemExit) as caught:
                    luma.main()
                self.assertEqual(caught.exception.code, 1)
                self.assertEqual(run.call_count, 3)

    def test_widest_selects_measured_speech_and_retains_unmeasured(self):
        self.check_selection(['hello', 'hello'], 'hello', 1001)
        self.check_selection(['hello', 'wrong'], 'hello', 1000)
        self.check_selection(['', ''], '[laughs]', 1001)

    def check_selection(self, transcripts, text, expected):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td) / 'dialogue.json'
            d.write_text(json.dumps({'voices': {'person': {'voice': 'Sarah'}}, 'takes': [{'id': 'line', 'speaker': 'person', 'text': text, 'select': 'widest'}]}))
            for seed in (1000, 1001):
                (Path(td) / f'line_{seed}.mp3').touch()
            with patch.dict(os.environ, ELEVENLABS_API_KEY_STARTER='test'), patch.object(sys, 'argv', ['perform', str(d), td + '/voices.json', td, '--seeds', '2']), patch.object(perform, 'analyse', side_effect=[None, {'f0_spread_st': 3, 'level_spread_db': 2}]), patch.object(perform, 'transcript', side_effect=transcripts):
                perform.main()
            result = json.loads((Path(td) / 'selection.json').read_text())['line']
            self.assertEqual(result['best']['seed'], expected)
            self.assertEqual(len(result['candidates']), 2)


if __name__ == '__main__':
    unittest.main()
