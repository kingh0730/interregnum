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
                'response_url': 'response', 'submitted': 1, 'endpoint': h3.ALIAS['i2v'],
                'payload': {'prompt': 'move', 'duration': 5, 'resolution': '768P',
                            'prompt_expansion_mode': 'disabled'}}))
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

    def test_h3_invalid_redo_preserves_take_until_inputs_are_fixed(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            man = root / 'motion.json'
            man.write_text(json.dumps([{'id': 's1', 'prompt': 'new prompt', 'image': 'frame.png', 'out': 's1.mp4'}]))
            out = root / 's1.mp4'
            out.write_bytes(b'old video')
            logdir = root / 'h3_log'
            logdir.mkdir()
            lp = logdir / 's1.json'
            lp.write_text(json.dumps({'request_id': 'old', 'done': 1, 'payload': {'prompt': 'old prompt'}}))
            original_log = lp.read_bytes()
            argv = ['h3', str(man), '--root', td]
            def http(url, key, payload=None):
                if payload is not None:
                    self.assertEqual(payload['prompt'], 'new prompt')
                    return {'request_id': 'new', 'status_url': 'status', 'response_url': 'response'}
                return {'status': 'COMPLETED'} if url == 'status' else {'video': {'url': 'https://example.test/new.mp4'}}
            with patch.dict(os.environ, FAL_KEY='test'), patch.object(h3, 'price', return_value=0), \
                    patch.object(h3, 'data_uri_image', side_effect=lambda p: 'data:image/png;base64,' + Path(p).read_text()), \
                    patch.object(h3, 'http', side_effect=http) as api, \
                    patch.object(h3.urllib.request, 'urlretrieve', side_effect=lambda u, p: Path(p).write_bytes(b'new video')):
                with patch.object(sys, 'argv', argv + ['--redo', 's1']), self.assertRaises(SystemExit) as caught:
                    h3.main()
                self.assertEqual(caught.exception.code, 1)
                api.assert_not_called()
                self.assertEqual(out.read_bytes(), b'old video')
                self.assertEqual(lp.read_bytes(), original_log)
                self.assertFalse((root / 's1.take1.mp4').exists())
                self.assertFalse((logdir / 's1.history.jsonl').exists())
                # A normal run now validates logged outputs too: the invalid new
                # input must fail without restoring or overwriting the existing take.
                with patch.object(sys, 'argv', argv), self.assertRaises(SystemExit) as caught:
                    h3.main()
                self.assertEqual(caught.exception.code, 1)
                api.assert_not_called()
                (root / 'frame.png').write_text('valid frame')
                with patch.object(sys, 'argv', argv + ['--redo', 's1']), self.assertRaises(SystemExit) as caught:
                    h3.main()
                self.assertEqual(caught.exception.code, 0)
                self.assertEqual(sum(call.args[2] is not None for call in api.call_args_list if len(call.args) > 2), 1)
            self.assertEqual(out.read_bytes(), b'new video')
            self.assertEqual((root / 's1.take1.mp4').read_bytes(), b'old video')
            self.assertEqual(json.loads((logdir / 's1.history.jsonl').read_text()), json.loads(original_log))
            self.assertEqual(json.loads(lp.read_text())['request_id'], 'new')

    def test_h3_terminal_failure_requires_explicit_redo(self):
        for failure in ('status', 'response', '422'):
            with self.subTest(failure=failure), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                man = root / 'motion.json'
                man.write_text(json.dumps([{'id': 's1', 'prompt': 'move', 'out': 's1.mp4'}]))
                submissions = []
                def http(url, key, payload=None):
                    if payload is not None:
                        submissions.append(payload)
                        return {'request_id': str(len(submissions)), 'status_url': 'status', 'response_url': 'response'}
                    if url == 'status':
                        return {'status': 'COMPLETED', **({'error': 'generation failed'}
                                if len(submissions) == 1 and failure == 'status' else {})}
                    if len(submissions) == 1:
                        if failure == '422':
                            raise h3.HTTPFailure(422, url, 'generation failed')
                        return {'error': 'generation failed'}
                    return {'video': {'url': 'https://example.test/new.mp4'}}
                argv = ['h3', str(man), '--root', td]
                with patch.dict(os.environ, FAL_KEY='test'), patch.object(h3, 'price', return_value=0), \
                        patch.object(h3, 'http', side_effect=http) as api, \
                        patch.object(h3.urllib.request, 'urlretrieve', side_effect=lambda u, p: Path(p).write_bytes(b'new')):
                    with patch.object(sys, 'argv', argv):
                        with self.assertRaises(SystemExit) as caught:
                            h3.main()
                        self.assertEqual(caught.exception.code, 1)
                        self.assertIn('terminal_failure', json.loads((root / 'h3_log/s1.json').read_text()))
                        api.reset_mock()
                        with self.assertRaises(SystemExit) as caught:
                            h3.main()
                        self.assertEqual(caught.exception.code, 1)
                        api.assert_not_called()
                    with patch.object(sys, 'argv', argv + ['--redo', 's1']):
                        with self.assertRaises(SystemExit) as caught:
                            h3.main()
                        self.assertEqual(caught.exception.code, 0)
                self.assertEqual(len(submissions), 2)
                self.assertEqual((root / 's1.mp4').read_bytes(), b'new')
                history = json.loads((root / 'h3_log/s1.history.jsonl').read_text())
                self.assertEqual(history['request_id'], '1')
                self.assertIn('terminal_failure', history)

    def test_h3_result_retrieval_errors_do_not_allow_redo(self):
        for error in (TimeoutError(), h3.HTTPFailure(401, 'response', 'unauthorized'),
                      h3.HTTPFailure(404, 'response', 'not found'), h3.HTTPFailure(503, 'response', 'unavailable')):
            with self.subTest(error=str(error)), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                man = root / 'motion.json'
                man.write_text(json.dumps([{'id': 's1', 'prompt': 'move', 'out': 's1.mp4'}]))
                posts = []
                def http(url, key, payload=None):
                    if payload is not None:
                        posts.append(payload)
                        return {'request_id': 'one', 'status_url': 'status', 'response_url': 'response'}
                    if url == 'status':
                        return {'status': 'COMPLETED'}
                    raise error
                argv = ['h3', str(man), '--root', td]
                with patch.dict(os.environ, FAL_KEY='test'), patch.object(h3, 'price', return_value=0), \
                        patch.object(h3, 'http', side_effect=http):
                    for args in (argv, argv + ['--redo', 's1']):
                        with patch.object(sys, 'argv', args), self.assertRaises(SystemExit) as caught:
                            h3.main()
                        self.assertEqual(caught.exception.code, 1)
                self.assertEqual(len(posts), 1)
                self.assertNotIn('terminal_failure', json.loads((root / 'h3_log/s1.json').read_text()))

    def test_h3_redo_verifies_old_unresolved_requests(self):
        for state in ('failed', 'pending', 'timeout', 'download_failed'):
            with self.subTest(state=state), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                man = root / 'motion.json'
                man.write_text(json.dumps([{'id': 's1', 'prompt': 'move', 'out': 's1.mp4'}]))
                logdir = root / 'h3_log'
                logdir.mkdir()
                lp = logdir / 's1.json'
                lp.write_text(json.dumps({'request_id': 'old', 'status_url': 'status', 'response_url': 'response'}))
                before = lp.read_bytes()
                posts = []
                def http(url, key, payload=None):
                    if payload is not None:
                        posts.append(payload)
                        return {'request_id': 'new', 'status_url': 'new-status', 'response_url': 'response'}
                    if url == 'new-status':
                        return {'status': 'IN_PROGRESS'}
                    if state == 'timeout':
                        raise TimeoutError()
                    if state == 'pending':
                        return {'status': 'IN_PROGRESS'}
                    return {'status': 'COMPLETED', **({'error_type': 'generation_error'} if state == 'failed' else {})}
                with patch.dict(os.environ, FAL_KEY='test'), patch.object(sys, 'argv',
                        ['h3', str(man), '--root', td, '--redo', 's1', '--timeout', '-1']), \
                        patch.object(h3, 'price', return_value=0), patch.object(h3, 'http', side_effect=http):
                    with self.assertRaises(SystemExit) as caught:
                        h3.main()
                    self.assertEqual(caught.exception.code, 1)
                self.assertEqual(len(posts), 1 if state == 'failed' else 0)
                if state != 'failed':
                    self.assertEqual(lp.read_bytes(), before)

    def test_h3_legacy_redo_checks_completed_result_before_replacing(self):
        for result in ('error', 'error_type', 422, 401, 404, 429, 503, 'timeout', 'success', 'malformed'):
            with self.subTest(result=result), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                man = root / 'motion.json'
                man.write_text(json.dumps([{'id': 's1', 'prompt': 'replacement', 'out': 's1.mp4'}]))
                logdir = root / 'h3_log'
                logdir.mkdir()
                lp = logdir / 's1.json'
                # Original inline media cannot be reconstructed or fingerprinted.
                old = {'request_id': 'old', 'status_url': 'old-status', 'response_url': 'old-result',
                       'payload': {'image_url': '<data uri>'}}
                lp.write_text(json.dumps(old))
                before = lp.read_bytes()
                posts = []
                reads = []
                def http(url, key, payload=None):
                    if payload is not None:
                        self.assertEqual(reads, ['old-status', 'old-result'])
                        self.assertEqual(payload['prompt'], 'replacement')
                        posts.append(payload)
                        return {'request_id': 'new', 'status_url': 'new-status', 'response_url': 'new-result'}
                    reads.append(url)
                    if url.endswith('status'):
                        return {'status': 'COMPLETED'}
                    if url == 'old-result':
                        if isinstance(result, int):
                            raise h3.HTTPFailure(result, url, 'request error')
                        if result == 'timeout':
                            raise TimeoutError()
                        if result in ('error', 'error_type'):
                            return {result: 'generation failed'}
                        if result == 'malformed':
                            return {}
                    return {'video': {'url': 'https://example.test/video.mp4'}}
                with patch.dict(os.environ, FAL_KEY='test'), patch.object(sys, 'argv',
                        ['h3', str(man), '--root', td, '--redo', 's1']), \
                        patch.object(h3, 'price', return_value=0), patch.object(h3, 'http', side_effect=http), \
                        patch.object(h3.urllib.request, 'urlretrieve',
                                     side_effect=lambda u, p: Path(p).write_bytes(b'new video')) as download:
                    with self.assertRaises(SystemExit) as caught:
                        h3.main()
                failed_generation = result in ('error', 'error_type', 422)
                self.assertEqual(caught.exception.code, 0 if failed_generation else 1)
                self.assertEqual(len(posts), 1 if failed_generation else 0)
                if failed_generation:
                    self.assertEqual((root / 's1.mp4').read_bytes(), b'new video')
                    history = json.loads((logdir / 's1.history.jsonl').read_text())
                    self.assertEqual(history['request_id'], 'old')
                    self.assertIn('terminal_failure', history)
                    download.assert_called_once()
                else:
                    self.assertEqual(reads, ['old-status', 'old-result'])
                    self.assertEqual(lp.read_bytes(), before)
                    self.assertFalse((logdir / 's1.history.jsonl').exists())
                    download.assert_not_called()

    def test_h3_resume_rejects_changed_inputs(self):
        for change in ('prompt', 'endpoint', 'media', 'legacy_media'):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                man = root / 'motion.json'
                job = {'id': 's1', 'prompt': 'move', 'image': 'frame.png', 'out': 's1.mp4'}
                man.write_text(json.dumps([job]))
                frame = root / 'frame.png'
                frame.write_text('original')
                def http(url, key, payload=None):
                    if payload is not None:
                        return {'request_id': 'one', 'status_url': 'status', 'response_url': 'response'}
                    return {'status': 'IN_PROGRESS'}
                with patch.dict(os.environ, FAL_KEY='test'), patch.object(sys, 'argv',
                        ['h3', str(man), '--root', td, '--timeout', '-1']), \
                        patch.object(h3, 'price', return_value=0), \
                        patch.object(h3, 'data_uri_image', side_effect=lambda p: 'data:image/png;base64,' + Path(p).read_text()), \
                        patch.object(h3, 'http', side_effect=http) as api:
                    with self.assertRaises(SystemExit) as caught:
                        h3.main()
                    self.assertEqual(caught.exception.code, 1)
                    lp = root / 'h3_log/s1.json'
                    if change == 'media':
                        frame.write_text('changed')
                    elif change == 'legacy_media':
                        log = json.loads(lp.read_text())
                        del log['payload_sha256']
                        lp.write_text(json.dumps(log))
                    else:
                        job[change] = 'changed' if change == 'prompt' else 'ray'
                        man.write_text(json.dumps([job]))
                    before = lp.read_bytes()
                    api.reset_mock()
                    with self.assertRaises(SystemExit) as caught:
                        h3.main()
                    self.assertEqual(caught.exception.code, 1)
                    api.assert_not_called()
                    self.assertEqual(lp.read_bytes(), before)
                    self.assertFalse((root / 's1.mp4').exists())

    def test_h3_unresolved_dependencies_fail(self):
        for deps in (['missing'], ['s1']):
            with self.subTest(deps=deps), tempfile.TemporaryDirectory() as td:
                man = Path(td) / 'motion.json'
                man.write_text(json.dumps([{'id': 's1', 'prompt': 'move', 'out': 's1.mp4', 'deps': deps}]))
                with patch.dict(os.environ, FAL_KEY='test'), patch.object(sys, 'argv',
                        ['h3', str(man), '--root', td]), patch.object(h3, 'price', return_value=0), \
                        patch.object(h3, 'http') as api:
                    with self.assertRaises(SystemExit) as caught:
                        h3.main()
                    self.assertEqual(caught.exception.code, 1)
                    api.assert_not_called()

    def test_luma_interrupted_redo_resumes_new_request(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            man = root / 'images.json'
            man.write_text(json.dumps([{'id': 's1', 'mode': 't2i', 'prompt': 'test', 'out': 's1.png'}]))
            out = root / 's1.png'
            out.write_bytes(b'old image')
            urls = man.with_suffix('.urls.json')
            urls.write_text(json.dumps({'s1': 'https://example.test/old.png'}))
            logdir = root / 'luma_log'
            logdir.mkdir()
            lp = logdir / 's1.json'
            lp.write_text(json.dumps({'response': {'image': {'url': 'https://example.test/old.png'}}}))
            def timeout(args, **kw):
                self.assertNotIn('s1', json.loads(urls.read_text()))
                lp.write_text(json.dumps({'request_id': 'new', 'status_url': 'status', 'response_url': 'response'}))
                raise subprocess.TimeoutExpired(args, 420)
            argv = ['luma', str(man), '--root', td]
            with patch.object(sys, 'argv', argv + ['--redo', 's1']), patch.object(luma.subprocess, 'run', side_effect=timeout):
                with self.assertRaises(SystemExit) as caught:
                    luma.main()
                self.assertEqual(caught.exception.code, 1)
            self.assertEqual(out.read_bytes(), b'old image')
            def resume(args, **kw):
                self.assertIn('--resume', args)
                self.assertEqual(json.loads(lp.read_text())['request_id'], 'new')
                lp.write_text(json.dumps({'request_id': 'new', 'response': {'image': {'url': 'https://example.test/new.png'}}}))
                (logdir / 's1.png').write_bytes(b'new image')
                return subprocess.CompletedProcess(args, 0, '', '')
            with patch.object(sys, 'argv', argv), patch.object(luma.subprocess, 'run', side_effect=resume) as run:
                with self.assertRaises(SystemExit) as caught:
                    luma.main()
                self.assertEqual(caught.exception.code, 0)
                run.assert_called_once()
            self.assertEqual(out.read_bytes(), b'new image')
            self.assertEqual(json.loads(urls.read_text())['s1'], 'https://example.test/new.png')

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
