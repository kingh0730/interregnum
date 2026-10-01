"""Exercise Luma recovery together with the real fal runner, without network calls."""
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
from contextlib import contextmanager

ROOT = Path(__file__).resolve().parents[1]


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


luma = module('luma_recovery', 'tools/imagegen/luma_batch.py')
fal = module('fal_recovery', 'tools/fal_run.py')


class Interrupted(BaseException):
    pass


class LumaRecoveryTests(unittest.TestCase):
    def test_rejected_recovery_does_not_change_a_surviving_childs_payload(self):
        for change in ('prompt', 'output'):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as td:
                root = Path(td).resolve()
                logs = root / 'luma_log'
                logs.mkdir()
                prefix = logs / 's1'
                pfile = logs / 's1.payload.json'
                endpoint = luma.EP['t2i']
                original_payload = {'prompt': 'original', 'aspect_ratio': '16:9'}
                pfile.write_text(json.dumps({'endpoint': endpoint, 'payload': original_payload}))
                journal_path = logs / 's1.redo.json'
                journal_path.write_text(json.dumps({
                    'previous': {}, 'endpoint': endpoint, 'out': str(root / 's1.png'),
                    'payload_sha256': hashlib.sha256(json.dumps(original_payload, sort_keys=True,
                        separators=(',', ':'), ensure_ascii=False).encode()).hexdigest(),
                }))
                saved_payload, saved_journal = pfile.read_bytes(), journal_path.read_bytes()
                job = {'id': 's1', 'mode': 't2i', 'prompt': 'original', 'out': 's1.png'}
                job['prompt' if change == 'prompt' else 'out'] = 'changed' if change == 'prompt' else 'changed.png'
                man = root / 'images.json'
                man.write_text(json.dumps([job]))
                original_lock = fal.file_lock
                @contextmanager
                def interleave(path):
                    # Resume the batch with incompatible inputs while its earlier
                    # child is alive but has not yet taken the request lock.
                    with patch.object(sys, 'argv', ['luma', str(man), '--root', str(root)]), \
                            patch.object(luma.subprocess, 'run') as runner:
                        with self.assertRaises(SystemExit) as caught:
                            luma.main()
                        self.assertEqual(caught.exception.code, 1)
                        runner.assert_not_called()
                    self.assertEqual(pfile.read_bytes(), saved_payload)
                    self.assertEqual(journal_path.read_bytes(), saved_journal)
                    self.assertFalse(prefix.with_suffix('.json').exists())
                    with original_lock(path):
                        yield
                posts = []
                def call(url, key, payload=None):
                    if payload is not None:
                        posts.append(payload)
                        return {'request_id': 'original-request', 'status_url': 'status', 'response_url': 'response'}
                    return {'status': 'COMPLETED'} if url == 'status' else {'image': {'url': 'https://example.test/original.png'}}
                with patch.dict(os.environ, FAL_KEY='test'), patch.object(sys, 'argv',
                        ['fal', endpoint, str(pfile), str(prefix), '--resume', '--request-envelope']), \
                        patch.object(fal, 'file_lock', side_effect=interleave), patch.object(fal, 'call', side_effect=call), \
                        patch.object(fal.urllib.request, 'urlretrieve'):
                    fal.main()
                self.assertEqual(posts, [original_payload])

    def test_payload_and_endpoint_are_read_under_the_request_lock(self):
        for mode in ('raw', 'envelope', 'changed_endpoint'):
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                prefix = root / 's1'
                pfile = root / 's1.payload.json'
                def document(prompt, endpoint='endpoint'):
                    payload = {'prompt': prompt}
                    return payload if mode == 'raw' else {'endpoint': endpoint, 'payload': payload}
                pfile.write_text(json.dumps(document('OLD')))
                original_lock = fal.file_lock
                @contextmanager
                def interleave(path):
                    # The batch prepares its redo just before this surviving child
                    # acquires the request lock. It must not retain a stale read.
                    with original_lock(path):
                        pfile.write_text(json.dumps(document('NEW',
                            'new-endpoint' if mode == 'changed_endpoint' else 'endpoint')))
                    with original_lock(path):
                        yield
                posts = []
                def call(url, key, payload=None):
                    if payload is not None:
                        posts.append(payload)
                        return {'request_id': 'new', 'status_url': 'status', 'response_url': 'response'}
                    return {'status': 'COMPLETED'} if url == 'status' else {'image': {'url': 'https://example.test/new.png'}}
                argv = ['fal', 'endpoint', str(pfile), str(prefix), '--resume']
                if mode != 'raw':
                    argv.append('--request-envelope')
                with patch.dict(os.environ, FAL_KEY='test'), patch.object(sys, 'argv', argv), \
                        patch.object(fal, 'file_lock', side_effect=interleave), patch.object(fal, 'call', side_effect=call), \
                        patch.object(fal.urllib.request, 'urlretrieve'):
                    if mode == 'changed_endpoint':
                        with self.assertRaisesRegex(SystemExit, 'endpoint changed'):
                            fal.main()
                        self.assertEqual(posts, [])
                        self.assertFalse(prefix.with_suffix('.json').exists())
                    else:
                        fal.main()
                        self.assertEqual(posts, [{'prompt': 'NEW'}])

    def test_batch_does_not_retire_or_rewrite_a_live_child_request(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td).resolve()
            man = root / 'images.json'
            man.write_text(json.dumps([{'id': 's1', 'mode': 't2i', 'prompt': 'new', 'out': 's1.png'}]))
            logs = root / 'luma_log'
            logs.mkdir()
            lp = logs / 's1.json'
            lp.write_text(json.dumps({'request_id': 'old', 'response': {'image': {'url': 'https://example.test/old.png'}}}))
            payload = logs / 's1.payload.json'
            payload.write_text('{"prompt":"old"}')
            before = lp.read_bytes()
            with fal.file_lock(lp.with_suffix('.request.lock')), patch.object(sys, 'argv',
                    ['luma', str(man), '--root', str(root), '--redo', 's1']), patch.object(luma.subprocess, 'run') as runner:
                with self.assertRaises(SystemExit) as caught:
                    luma.main()
                self.assertEqual(caught.exception.code, 1)
                runner.assert_not_called()
            self.assertEqual(lp.read_bytes(), before)
            self.assertEqual(payload.read_text(), '{"prompt":"old"}')
            self.assertFalse((logs / 's1.redo.json').exists())

    def test_request_lock_blocks_a_second_runner_before_submission(self):
        with tempfile.TemporaryDirectory() as td:
            prefix = Path(td) / 'result'
            code = """import sys
sys.path.insert(0, sys.argv[1])
import fal_run
fal_run.call = lambda *a, **kw: (_ for _ in ()).throw(AssertionError('must not call API'))
sys.argv = ['fal', 'endpoint', '{}', sys.argv[2], '--resume']
try:
    fal_run.main()
except RuntimeError:
    sys.exit(7)
"""
            with fal.file_lock(prefix.with_suffix('.request.lock')):
                result = subprocess.run([sys.executable, '-c', code, str(ROOT / 'tools'), str(prefix)],
                                        env={**os.environ, 'FAL_KEY': 'test'}, capture_output=True, text=True)
            self.assertEqual(result.returncode, 7, result.stderr)
            self.assertFalse(prefix.with_suffix('.json').exists())

    def test_redo_interruption_boundaries(self):
        boundaries = ('journal_before', 'journal_after', 'invalidation_after', 'history_after',
                      'retire_before', 'retire_after', 'post_after', 'accepted_after',
                      'download_during', 'install_after', 'url_commit_after', 'journal_remove_after')
        for boundary in boundaries:
            with self.subTest(boundary=boundary), tempfile.TemporaryDirectory() as td:
                root = Path(td).resolve()
                man = root / 'images.json'
                man.write_text(json.dumps([{'id': 's1', 'mode': 't2i', 'prompt': 'test', 'out': 's1.png'}]))
                urls_path = man.with_suffix('.urls.json')
                urls_path.write_text(json.dumps({'s1': 'https://example.test/old.png'}))
                out = root / 's1.png'
                out.write_bytes(b'old image')
                logdir = root / 'luma_log'
                logdir.mkdir()
                lp = logdir / 's1.json'
                old = {'endpoint': luma.EP['t2i'], 'payload': {'prompt': 'test', 'aspect_ratio': '16:9'},
                       'request_id': 'old', 'response': {'image': {'url': 'https://example.test/old.png'}}}
                lp.write_text(json.dumps(old))
                journal = logdir / 's1.redo.json'
                posts, stopped = [], []

                def stop(at):
                    if at == boundary and not stopped:
                        stopped.append(at)
                        raise Interrupted(at)

                save, record, unlink, replace = luma.save_log, luma.record_once, Path.unlink, Path.replace

                def save_hook(path, log):
                    if path == journal:
                        stop('journal_before')
                    save(path, log)
                    if path == journal:
                        stop('journal_after')
                    elif path == urls_path:
                        stop('url_commit_after' if log.get('s1') else 'invalidation_after')
                    elif path == lp and log.get('request_id') == 'new' and not log.get('response'):
                        stop('accepted_after')

                def record_hook(path, log, key=None):
                    record(path, log, key)
                    stop('history_after')

                def unlink_hook(path, *args, **kw):
                    if path == lp:
                        stop('retire_before')
                    result = unlink(path, *args, **kw)
                    if path == lp:
                        stop('retire_after')
                    if path == journal:
                        stop('journal_remove_after')
                    return result

                def replace_hook(path, dst):
                    result = replace(path, dst)
                    if Path(dst) == out:
                        stop('install_after')
                    return result

                def call(url, key, payload=None):
                    if payload is not None:
                        posts.append(payload)
                        stop('post_after')
                        return {'request_id': 'new', 'status_url': 'status', 'response_url': 'response'}
                    return {'status': 'COMPLETED'} if url == 'status' else {'image': {'url': 'https://example.test/new.png'}}

                def download(url, dst):
                    self.assertEqual(url, 'https://example.test/new.png')
                    Path(dst).write_bytes(b'partial')
                    stop('download_during')
                    Path(dst).write_bytes(b'new image')

                def subprocess_run(args, **kw):
                    # Run the actual fal recovery logic, not a simulation that assumes
                    # the batch selected the right request. Never launch uv or use network.
                    with patch.object(sys, 'argv', args[2:]):
                        try:
                            fal.main()
                        except SystemExit as e:
                            return subprocess.CompletedProcess(args, 1, '', str(e))
                    return subprocess.CompletedProcess(args, 0, '', '')

                argv = ['luma', str(man), '--root', str(root)]
                with patch.dict(os.environ, FAL_KEY='test'), patch.object(luma.subprocess, 'run', side_effect=subprocess_run), \
                        patch.object(fal, 'call', side_effect=call), \
                        patch.object(fal.urllib.request, 'urlretrieve', side_effect=download), \
                        patch.object(luma, 'save_log', side_effect=save_hook), patch.object(fal, 'save_log', side_effect=save_hook), \
                        patch.object(luma, 'record_once', side_effect=record_hook), \
                        patch.object(Path, 'unlink', unlink_hook), patch.object(Path, 'replace', replace_hook):
                    with patch.object(sys, 'argv', argv + ['--redo', 's1']), self.assertRaises(Interrupted):
                        luma.main()
                    self.assertEqual(stopped, [boundary])
                    if boundary == 'history_after':
                        # An old request can have updated timing metadata from a
                        # previous downloader; retirement follows request identity.
                        lp.write_text(json.dumps(dict(old, seconds=999)))
                    resume = argv + ['--redo', 's1'] if boundary == 'journal_before' else argv
                    with patch.object(sys, 'argv', resume), self.assertRaises(SystemExit) as caught:
                        luma.main()
                    ambiguous = boundary == 'post_after'
                    self.assertEqual(caught.exception.code, 1 if ambiguous else 0)
                    self.assertEqual(len(posts), 1)
                    self.assertEqual(out.read_bytes(), b'old image' if ambiguous else b'new image')
                    if ambiguous:
                        self.assertTrue(journal.exists())
                        self.assertTrue(json.loads(lp.read_text())['submission_pending'])
                        with patch.object(sys, 'argv', argv + ['--redo', 's1']), self.assertRaises(SystemExit) as caught:
                            luma.main()
                        self.assertEqual(caught.exception.code, 1)
                        self.assertEqual(len(posts), 1)
                    else:
                        self.assertFalse(journal.exists())
                        self.assertEqual(json.loads(urls_path.read_text())['s1'], 'https://example.test/new.png')
                        self.assertEqual(json.loads(lp.read_text())['request_id'], 'new')
                    history = [json.loads(line) for line in (logdir / 's1.history.jsonl').read_text().splitlines()]
                    self.assertEqual(history, [old])

    def test_unresolved_dependencies_fail_without_submitting(self):
        with tempfile.TemporaryDirectory() as td:
            man = Path(td) / 'images.json'
            man.write_text(json.dumps([{'id': 's1', 'mode': 't2i', 'prompt': 'test', 'out': 's1.png', 'deps': ['missing']}]))
            with patch.object(sys, 'argv', ['luma', str(man)]), patch.object(luma.subprocess, 'run') as runner:
                with self.assertRaises(SystemExit) as caught:
                    luma.main()
                self.assertEqual(caught.exception.code, 1)
                runner.assert_not_called()


if __name__ == '__main__':
    unittest.main()
