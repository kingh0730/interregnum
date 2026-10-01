"""Failure injection at H3's durable state boundaries; all network calls are mocked."""
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from contextlib import redirect_stdout

SCRIPT = Path(__file__).resolve().parents[1] / 'tools/video/h3_batch.py'
spec = importlib.util.spec_from_file_location('h3_recovery', SCRIPT)
h3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h3)


class Interrupted(BaseException):
    """Bypass normal retry handlers, like process termination."""


class RecoveryTests(unittest.TestCase):
    def test_only_ignores_unrelated_logs_but_checks_required_dependencies(self):
        for corrupt_dependency in (False, True):
            with self.subTest(corrupt_dependency=corrupt_dependency), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                man = root / 'motion.json'
                man.write_text(json.dumps([
                    {'id': 'good', 'prompt': 'move', 'out': 'good.mp4', 'deps': ['parent']},
                    {'id': 'parent', 'prompt': 'move', 'out': 'parent.mp4'},
                    {'id': 'unrelated', 'prompt': 'move', 'out': 'unrelated.mp4'},
                ]))
                logs = root / 'h3_log'
                logs.mkdir()
                (logs / 'unrelated.json').write_text('{')
                (logs / 'parent.json').write_text('{' if corrupt_dependency else json.dumps({'done': 1}))
                (root / 'parent.mp4').write_bytes(b'completed parent')
                posts = []
                def http(url, key, payload=None):
                    if payload is not None:
                        posts.append(payload)
                        return {'request_id': 'good', 'status_url': 'status', 'response_url': 'response'}
                    return {'status': 'COMPLETED'} if url == 'status' else {'video': {'url': 'https://example.test/good.mp4'}}
                with patch.dict(os.environ, FAL_KEY='test'), patch.object(sys, 'argv',
                        ['h3', str(man), '--root', td, '--only', 'good']), patch.object(h3, 'price', return_value=0), \
                        patch.object(h3, 'http', side_effect=http), \
                        patch.object(h3.urllib.request, 'urlretrieve', side_effect=lambda u, p: Path(p).write_bytes(b'new video')):
                    with self.assertRaises(SystemExit) as caught:
                        h3.main()
                if corrupt_dependency:
                    self.assertNotEqual(caught.exception.code, 0)
                    self.assertEqual(posts, [])
                else:
                    self.assertEqual(caught.exception.code, 0)
                    self.assertEqual(len(posts), 1)
                    self.assertEqual((root / 'good.mp4').read_bytes(), b'new video')
                self.assertEqual((logs / 'unrelated.json').read_text(), '{')

    def test_prepared_request_is_included_in_dry_run_cost(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            man = root / 'motion.json'
            man.write_text(json.dumps([{'id': 's1', 'prompt': 'move', 'out': 's1.mp4'}]))
            argv = ['h3', str(man), '--root', td]
            original = h3.save_log
            def interrupt(path, log):
                original(path, log)
                if log.get('phase') == 'prepared':
                    raise Interrupted()
            with patch.dict(os.environ, FAL_KEY='test'), patch.object(h3, 'price', return_value=0.025), \
                    patch.object(h3, 'http') as api:
                with patch.object(sys, 'argv', argv), patch.object(h3, 'save_log', side_effect=interrupt), \
                        self.assertRaises(Interrupted):
                    h3.main()
                output = io.StringIO()
                with patch.object(sys, 'argv', argv + ['--dry-run']), redirect_stdout(output):
                    h3.main()
                self.assertIn('plan s1', output.getvalue())
                self.assertIn('$0.125', output.getvalue())
                self.assertNotIn('new spend $0.00', output.getvalue())
                api.assert_not_called()

    def test_redo_interruption_boundaries(self):
        boundaries = ('prepared_before', 'prepared_after', 'history_after', 'archive_after',
                      'submitting_before', 'submitting_after', 'post_after', 'accepted_before',
                      'accepted_after', 'download_during', 'output_after', 'done_after')
        for boundary in boundaries:
            with self.subTest(boundary=boundary), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                man = root / 'motion.json'
                job = {'id': 's1', 'prompt': 'move', 'out': 's1.mp4'}
                man.write_text(json.dumps([job]))
                logs = root / 'h3_log'
                logs.mkdir()
                lp = logs / 's1.json'
                old = {'request_id': 'old', 'status_url': 'old-status', 'response_url': 'old-response',
                       'endpoint': h3.ALIAS['i2v'], 'submitted': 1, 'done': 2,
                       'payload': {'prompt': 'move', 'duration': 5, 'resolution': '768P',
                                   'prompt_expansion_mode': 'disabled'}}
                h3.save_log(lp, old)
                out = root / 's1.mp4'
                out.write_bytes(b'old video')
                posts = []
                crashed = []

                def stop(at):
                    if at == boundary and not crashed:
                        crashed.append(at)
                        raise Interrupted(at)

                save, record, archive, replace = h3.save_log, h3.record_once, h3.archive_previous, Path.replace

                def save_hook(path, log):
                    phase = log.get('phase')
                    stop(f'{phase}_before')
                    save(path, log)
                    stop(f'{phase}_after')

                def record_hook(path, entry, key=None):
                    record(path, entry, key)
                    if path.name.endswith('.history.jsonl'):
                        stop('history_after')

                def archive_hook(log, logdir):
                    archive(log, logdir)
                    stop('archive_after')

                def replace_hook(path, dst):
                    result = replace(path, dst)
                    if path.name.endswith('.part.mp4'):
                        stop('output_after')
                    return result

                def http(url, key, payload=None):
                    self.assertNotIn('old-', url, 'retired request was fetched again')
                    if payload is not None:
                        posts.append(payload)
                        stop('post_after')
                        return {'request_id': 'new', 'status_url': 'status', 'response_url': 'response'}
                    if url == 'status':
                        return {'status': 'COMPLETED'}
                    return {'video': {'url': 'https://example.test/new.mp4'}}

                def download(url, dst):
                    Path(dst).write_bytes(b'partial')
                    stop('download_during')
                    Path(dst).write_bytes(b'new video')

                argv = ['h3', str(man), '--root', td]
                with patch.dict(os.environ, FAL_KEY='test'), patch.object(h3, 'price', return_value=0), \
                        patch.object(h3, 'http', side_effect=http), \
                        patch.object(h3.urllib.request, 'urlretrieve', side_effect=download), \
                        patch.object(h3, 'save_log', side_effect=save_hook), \
                        patch.object(h3, 'record_once', side_effect=record_hook), \
                        patch.object(h3, 'archive_previous', side_effect=archive_hook), \
                        patch.object(Path, 'replace', replace_hook):
                    with patch.object(sys, 'argv', argv + ['--redo', 's1']), self.assertRaises(Interrupted):
                        h3.main()
                    self.assertEqual(crashed, [boundary])
                    # Before intent is committed, nothing has been retired. Repeat
                    # the explicit redo; otherwise an ordinary run recovers intent.
                    resume = argv + ['--redo', 's1'] if boundary == 'prepared_before' else argv
                    with patch.object(sys, 'argv', resume), self.assertRaises(SystemExit) as caught:
                        h3.main()
                    ambiguous = boundary in ('submitting_after', 'post_after', 'accepted_before')
                    self.assertEqual(caught.exception.code, 1 if ambiguous else 0)
                    if ambiguous:
                        self.assertTrue(json.loads(lp.read_text())['submission_pending'])
                        self.assertFalse(out.exists())
                        self.assertEqual(len(posts), 0 if boundary == 'submitting_after' else 1)
                        # Neither another normal run nor --redo may repeat an uncertain POST.
                        with patch.object(sys, 'argv', argv + ['--redo', 's1']), self.assertRaises(SystemExit) as caught:
                            h3.main()
                        self.assertEqual(caught.exception.code, 1)
                    else:
                        self.assertEqual(out.read_bytes(), b'new video')
                        self.assertEqual(len(posts), 1)
                        self.assertEqual(json.loads(lp.read_text())['request_id'], 'new')
                        entries = [json.loads(line) for line in (logs / 'ledger.jsonl').read_text().splitlines()]
                        self.assertEqual([entry['request_id'] for entry in entries], ['new'])
                    self.assertEqual((root / 's1.take1.mp4').read_bytes(), b'old video')
                    self.assertFalse((root / 's1.take2.mp4').exists())
                    history = [json.loads(line) for line in (logs / 's1.history.jsonl').read_text().splitlines()]
                    self.assertEqual(history, [old])

    def test_atomic_log_write_preserves_previous_file_on_failure(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / 'job.json'
            h3.save_log(path, {'phase': 'prepared'})
            with patch.object(h3.os, 'replace', side_effect=OSError('disk error')):
                with self.assertRaises(OSError):
                    h3.save_log(path, {'phase': 'submitting'})
            self.assertEqual(json.loads(path.read_text()), {'phase': 'prepared'})
            self.assertEqual(list(Path(td).iterdir()), [path])

    def test_batch_lock_excludes_other_process_and_releases(self):
        code = """import importlib.util, pathlib, sys
spec = importlib.util.spec_from_file_location('h3', sys.argv[1])
h3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h3)
try:
    with h3.batch_lock(pathlib.Path(sys.argv[2])):
        pass
except RuntimeError:
    sys.exit(7)
"""
        with tempfile.TemporaryDirectory() as td:
            args = [sys.executable, '-c', code, str(SCRIPT), td]
            with h3.batch_lock(Path(td)):
                self.assertEqual(subprocess.run(args, capture_output=True).returncode, 7)
            self.assertEqual(subprocess.run(args, capture_output=True).returncode, 0)

    def test_invalid_manifest_cannot_submit(self):
        job = {'id': 's1', 'prompt': 'move', 'out': 's1.mp4'}
        for jobs in ([job, job], [job, dict(job, id='s2')], [dict(job, id='../escape')],
                     [job, dict(job, id='s2', out='s1.part.mp4')]):
            with self.subTest(jobs=jobs), tempfile.TemporaryDirectory() as td:
                man = Path(td) / 'motion.json'
                man.write_text(json.dumps(jobs))
                with patch.object(sys, 'argv', ['h3', str(man), '--root', td]), patch.object(h3, 'http') as api:
                    with self.assertRaises(SystemExit) as caught:
                        h3.main()
                    self.assertNotEqual(caught.exception.code, 0)
                    api.assert_not_called()

    def test_malformed_log_and_incomplete_submission_fail_closed(self):
        for case in ('invalid_json', 'empty_log', 'missing_urls'):
            with self.subTest(case=case), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                man = root / 'motion.json'
                man.write_text(json.dumps([{'id': 's1', 'prompt': 'move', 'out': 's1.mp4'}]))
                logs = root / 'h3_log'
                logs.mkdir()
                lp = logs / 's1.json'
                if case != 'missing_urls':
                    lp.write_text('{' if case == 'invalid_json' else '{}')
                with patch.dict(os.environ, FAL_KEY='test'), patch.object(sys, 'argv',
                        ['h3', str(man), '--root', td]), patch.object(h3, 'price', return_value=0), \
                        patch.object(h3, 'http', return_value={'request_id': 'accepted'}) as api:
                    for _ in range(2):
                        with self.assertRaises(SystemExit) as caught:
                            h3.main()
                        self.assertNotEqual(caught.exception.code, 0)
                    self.assertEqual(api.call_count, 1 if case == 'missing_urls' else 0)
                    if case == 'missing_urls':
                        saved = json.loads(lp.read_text())
                        self.assertEqual(saved['request_id'], 'accepted')
                        self.assertTrue(saved['submission_pending'])

    def test_completed_output_still_checks_changed_inputs(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            man = root / 'motion.json'
            job = {'id': 's1', 'prompt': 'original', 'out': 's1.mp4'}
            man.write_text(json.dumps([job]))
            def http(url, key, payload=None):
                if payload is not None:
                    return {'request_id': 'one', 'status_url': 'status', 'response_url': 'response'}
                return {'status': 'COMPLETED'} if url == 'status' else {'video': {'url': 'https://example.test/video.mp4'}}
            with patch.dict(os.environ, FAL_KEY='test'), patch.object(sys, 'argv',
                    ['h3', str(man), '--root', td]), patch.object(h3, 'price', return_value=0), \
                    patch.object(h3, 'http', side_effect=http) as api, \
                    patch.object(h3.urllib.request, 'urlretrieve', side_effect=lambda u, p: Path(p).write_bytes(b'original')):
                with self.assertRaises(SystemExit) as caught:
                    h3.main()
                self.assertEqual(caught.exception.code, 0)
                job['prompt'] = 'changed'
                man.write_text(json.dumps([job]))
                api.reset_mock()
                with self.assertRaises(SystemExit) as caught:
                    h3.main()
                self.assertEqual(caught.exception.code, 1)
                api.assert_not_called()
                self.assertEqual((root / 's1.mp4').read_bytes(), b'original')

    def test_pending_parent_with_old_output_is_not_a_completed_dependency(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            man = root / 'motion.json'
            man.write_text(json.dumps([
                {'id': 'parent', 'prompt': 'move', 'out': 'parent.mp4'},
                {'id': 'child', 'prompt': 'move', 'out': 'child.mp4', 'deps': ['parent']},
            ]))
            (root / 'parent.mp4').write_bytes(b'old video')
            logs = root / 'h3_log'
            logs.mkdir()
            h3.save_log(logs / 'parent.json', {'phase': 'prepared', 'id': 'parent'})
            with patch.dict(os.environ, FAL_KEY='test'), patch.object(sys, 'argv',
                    ['h3', str(man), '--root', td, '--only', 'child']), \
                    patch.object(h3, 'price', return_value=0), patch.object(h3, 'http') as api:
                with self.assertRaises(SystemExit) as caught:
                    h3.main()
                self.assertEqual(caught.exception.code, 1)
                api.assert_not_called()


if __name__ == '__main__':
    unittest.main()
