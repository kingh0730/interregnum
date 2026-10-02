"""Recorded continuity approval and paid-request recovery; all services mocked."""
import hashlib
import importlib.util
import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import ExitStack, redirect_stdout
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from continuity import evaluate_review, main as continuity_main

spec = importlib.util.spec_from_file_location('h3_continuity', ROOT / 'tools/video/h3_batch.py')
h3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h3)


class Fixture(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in ['a.png', 'b.png', 'after.png']:
            (self.root / name).write_bytes(name.encode())
        self.story = {'shots': [
            {'id': '05', 'asset': 'a', 'start_frame': 0, 'end_frame': 24},
            {'id': '06', 'asset': 'b', 'start_frame': 24, 'end_frame': 48},
            {'id': '07', 'asset': 'title', 'kind': 'title', 'start_frame': 48, 'end_frame': 72},
        ]}
        self.write('story.json', self.story)
        self.write('assets.json', {'a': 'a.png', 'b': 'b.png', 'after': 'after.png'})
        self.write('states.json', {'05': [{'offset_frame': 0, 'asset': 'a'}, {'offset_frame': 12, 'asset': 'after'}]})
        self.write('framing.json', {'mode': 'native'})
        self.review = {
            'schema_version': 1, 'status': 'approved', 'reviewer': 'test visual reviewer',
            'story': self.bound('story.json'), 'assets': self.bound('assets.json'),
            'states': self.bound('states.json'), 'additional_inputs': [self.bound('framing.json')],
            'sources': [self.bound(p) for p in ['a.png', 'b.png', 'after.png']],
            'cuts': [
                dict(from_shot='05', to_shot='06', from_asset='after', to_asset='b',
                     relation='continuous', status='approved', issues=[],
                     evidence='The tighter crop excludes the same left table edge; the visible sink and right door retain their established positions.'),
                dict(from_shot='06', to_shot='07', from_asset='b', to_asset='title',
                     relation='scene_change', status='approved', issues=[], evidence='The last scene ends before the authored title card.'),
            ],
            'state_changes': [dict(shot_id='05', offset_frame=12, from_asset='a', to_asset='after',
                                   relation='continuous', status='approved', issues=[],
                                   evidence='The address tab changes position; all unchanged paper and tabletop edges retain their positions.')],
        }
        self.save_review()

    def write(self, name, value):
        (self.root / name).write_text(json.dumps(value))

    def bound(self, name):
        return {'path': name, 'sha256': hashlib.sha256((self.root / name).read_bytes()).hexdigest()}

    def save_review(self):
        self.write('review.json', self.review)

    def check(self):
        self.save_review()
        return evaluate_review('review.json', self.root)


class ReviewTests(Fixture):
    def test_local_cli_exit_codes_and_diagnostics(self):
        with redirect_stdout(io.StringIO()) as output:
            self.assertEqual(continuity_main(['review.json', '--root', str(self.root)]), 0)
        self.assertTrue(json.loads(output.getvalue())['approved'])
        self.review['status'] = 'blocked'; self.save_review()
        with redirect_stdout(io.StringIO()) as output:
            self.assertEqual(continuity_main(['review.json', '--root', str(self.root)]), 2)
        self.assertFalse(json.loads(output.getvalue())['approved'])
        with redirect_stdout(io.StringIO()):
            self.assertEqual(continuity_main(['missing.json', '--root', str(self.root)]), 2)

    def test_local_cli_help(self):
        with redirect_stdout(io.StringIO()) as output, self.assertRaises(SystemExit) as caught:
            continuity_main(['--help'])
        self.assertEqual(caught.exception.code, 0)
        self.assertIn('--root', output.getvalue())

    def test_specific_crop_evidence_and_procedural_title_are_valid(self):
        self.assertTrue(self.check()['approved'])

    def test_approved_ellipsis_and_nonphysical_style_are_not_forced_to_match(self):
        for relation in ['ellipsis', 'intentional_discontinuity']:
            self.review['cuts'][0].update(relation=relation, evidence='An explicit day-change card separates the cleaned table from the preceding spill; this is a declared time jump.')
            self.assertTrue(self.check()['approved'])

    def test_disappearing_state_blocks_despite_valid_media_hashes(self):
        self.review['cuts'][0].update(status='blocked', evidence='Same-time cut exposes the same floor area.', issues=['The installed cabinet disappears across the cut.'])
        result = self.check()
        self.assertFalse(result['approved'])
        self.assertIn('installed cabinet disappears', ' '.join(result['errors']))

    def test_source_changed_in_place_is_stale(self):
        (self.root / 'b.png').write_bytes(b'different physical layout')
        self.assertFalse(self.check()['approved'])

    def test_current_story_order_must_match_even_if_binding_is_refreshed(self):
        self.story['shots'][0], self.story['shots'][1] = self.story['shots'][1], self.story['shots'][0]
        self.write('story.json', self.story)
        self.review['story'] = self.bound('story.json')
        self.assertIn('not adjacent', ' '.join(self.check()['errors']))

    def test_extra_binding_and_complete_unique_sources_are_checked(self):
        (self.root / 'framing.json').write_text('{}')
        self.assertFalse(self.check()['approved'])
        self.review['additional_inputs'] = [self.bound('framing.json')]
        self.review['sources'].pop()
        self.assertIn('Source coverage differs', ' '.join(self.check()['errors']))
        self.review['sources'].append(self.bound('after.png'))
        self.review['sources'].append(self.bound('after.png'))
        self.assertIn('Duplicate source', ' '.join(self.check()['errors']))

    def test_within_shot_switch_and_actual_cut_endpoints_are_required(self):
        self.review['state_changes'] = []
        self.assertIn('Missing state-change', ' '.join(self.check()['errors']))
        self.review['cuts'][0]['from_asset'] = 'a'
        self.assertIn('endpoint assets differ', ' '.join(self.check()['errors']))

    def test_all_cut_judgments_require_evidence_no_issues_and_coverage(self):
        original = json.loads(json.dumps(self.review))
        for change in ['empty_evidence', 'unresolved', 'missing', 'duplicate', 'unknown_relation', 'unknown_status', 'reviewer']:
            with self.subTest(change=change):
                self.review = json.loads(json.dumps(original))
                row = self.review['cuts'][0]
                if change == 'empty_evidence': row['evidence'] = ' '
                elif change == 'unresolved': row['issues'] = ['Position not checked']
                elif change == 'missing': self.review['cuts'].pop()
                elif change == 'duplicate': self.review['cuts'].append(dict(row))
                elif change == 'unknown_relation': row['relation'] = ['continuous']
                elif change == 'unknown_status': row['status'] = ['approved']
                else: self.review['reviewer'] = ''
                self.assertFalse(self.check()['approved'])

    def test_missing_malformed_and_unknown_status_fail_closed_without_exception(self):
        self.assertFalse(evaluate_review('absent.json', self.root)['approved'])
        for value in [[], {}, {'schema_version': 1, 'status': ['approved']}, {'schema_version': 1, 'status': 'passed'}]:
            self.write('review.json', value)
            self.assertFalse(evaluate_review('review.json', self.root)['approved'])
        (self.root / 'review.json').write_text('{')
        self.assertFalse(evaluate_review('review.json', self.root)['approved'])


class RunnerTests(Fixture):
    def setUp(self):
        super().setUp()
        self.job = {'id': 's1', 'shot_id': '05', 'prompt': 'hold', 'image': 'a.png', 'out': 's1.mp4'}
        self.manifest = {'continuity_review': 'review.json', 'jobs': [self.job]}
        self.posts = []
        self.in_progress = False

    def api(self, url, key, payload=None, **kwargs):
        if payload is not None:
            self.posts.append(payload)
            return {'request_id': 'paid-one', 'status_url': 'status', 'response_url': 'response'}
        if url == 'status':
            return {'status': 'IN_PROGRESS' if self.in_progress else 'COMPLETED'}
        return {'video': {'url': 'https://example.test/video.mp4'}}

    def run_runner(self, *args, save_hook=None):
        self.write('motion.json', self.manifest)
        output = io.StringIO()
        with ExitStack() as stack:
            stack.enter_context(patch.dict(os.environ, FAL_KEY='test'))
            stack.enter_context(patch.object(sys, 'argv', ['h3', str(self.root / 'motion.json'), '--root', str(self.root), '--timeout', '-1', *args]))
            stack.enter_context(patch.object(h3, 'price', return_value=0.025))
            stack.enter_context(patch.object(h3, 'http', side_effect=self.api))
            stack.enter_context(patch.object(h3, 'data_uri_image', side_effect=lambda p: 'data:image/mock,' + Path(p).read_text()))
            stack.enter_context(patch.object(h3.urllib.request, 'urlretrieve', side_effect=lambda u, p: Path(p).write_bytes(b'paid result')))
            stack.enter_context(redirect_stdout(output))
            if save_hook:
                stack.enter_context(patch.object(h3, 'save_log', side_effect=save_hook))
            try:
                h3.main()
                code = 0
            except SystemExit as exc:
                code = exc.code
        return code, output.getvalue()

    def test_blocked_new_request_and_quote_do_not_post(self):
        self.review['status'] = 'blocked'; self.save_review()
        code, _ = self.run_runner()
        self.assertEqual(code, 1)
        code, output = self.run_runner('--dry-run')
        self.assertEqual(code, 0)
        self.assertIn('continuity gate BLOCKED', output)
        self.assertIn('price quote only', output)
        self.assertEqual(self.posts, [])
        self.assertFalse((self.root / 'h3_log/s1.json').exists())

    def test_declared_null_gate_does_not_silently_disable_it(self):
        self.manifest['continuity_review'] = None
        self.assertEqual(self.run_runner()[0], 1)
        self.assertEqual(self.posts, [])

    def test_legacy_manifest_is_unchanged(self):
        del self.manifest['continuity_review']
        self.review['status'] = 'blocked'; self.save_review()
        self.assertEqual(self.run_runner()[0], 0)
        self.assertEqual(len(self.posts), 1)

    def test_accepted_request_recovers_when_review_missing_or_malformed(self):
        self.in_progress = True
        self.assertEqual(self.run_runner()[0], 1)
        self.assertEqual(len(self.posts), 1)
        (self.root / 'review.json').unlink()
        self.assertEqual(self.run_runner()[0], 1)  # same accepted request still pending
        (self.root / 'review.json').write_text('{')
        self.in_progress = False
        self.assertEqual(self.run_runner()[0], 0)
        self.assertEqual(len(self.posts), 1)
        self.assertEqual((self.root / 's1.mp4').read_bytes(), b'paid result')

    def test_mixed_batch_recovers_paid_job_while_blocking_new_job(self):
        self.in_progress = True
        self.run_runner()
        self.review['status'] = 'blocked'; self.save_review()
        self.manifest['jobs'].append(dict(self.job, id='s2', out='s2.mp4'))
        self.in_progress = False
        self.assertEqual(self.run_runner()[0], 1)
        self.assertEqual(len(self.posts), 1)
        self.assertTrue((self.root / 's1.mp4').exists())
        self.assertFalse((self.root / 's2.mp4').exists())

    def test_blocked_redo_preserves_existing_take_and_log(self):
        self.assertEqual(self.run_runner()[0], 0)
        log = self.root / 'h3_log/s1.json'; before = log.read_bytes()
        self.review['status'] = 'blocked'; self.save_review()
        self.assertEqual(self.run_runner('--redo', 's1')[0], 1)
        self.assertEqual(len(self.posts), 1)
        self.assertEqual(log.read_bytes(), before)
        self.assertEqual((self.root / 's1.mp4').read_bytes(), b'paid result')
        self.assertFalse((self.root / 's1.take1.mp4').exists())

    def test_withdrawal_after_preparation_blocks_post_and_prepared_resume(self):
        original_save = h3.save_log
        def save(path, log):
            original_save(path, log)
            if log.get('phase') == 'prepared':
                self.review['status'] = 'blocked'; self.save_review()
        self.assertEqual(self.run_runner(save_hook=save)[0], 1)
        log = json.loads((self.root / 'h3_log/s1.json').read_text())
        self.assertEqual(log['phase'], 'prepared')
        self.assertNotIn('submission_pending', log)
        self.assertEqual(self.run_runner()[0], 1)
        self.assertEqual(self.posts, [])

    def test_changed_approved_review_during_preparation_requires_recheck(self):
        original_save = h3.save_log
        def save(path, log):
            original_save(path, log)
            if log.get('phase') == 'prepared':
                self.review['reviewer'] = 'changed reviewer'; self.save_review()
        self.assertEqual(self.run_runner(save_hook=save)[0], 1)
        self.assertEqual(self.posts, [])
        self.assertEqual(self.run_runner()[0], 0)
        self.assertEqual(len(self.posts), 1)

    def test_unreviewed_local_start_or_end_image_is_blocked(self):
        (self.root / 'other.png').write_bytes(b'unreviewed')
        for field in ['image', 'end_image']:
            with self.subTest(field=field):
                self.manifest['jobs'] = [dict(self.job, **{field: 'other.png'})]
                self.assertEqual(self.run_runner()[0], 1)
        self.assertEqual(self.posts, [])

    def test_other_reviewed_source_cannot_replace_this_shot_state(self):
        for changes in [{'image': 'b.png'}, {'image_key': 'b'}, {'shot_id': 'absent'}, {'end_image': 'b.png'}]:
            with self.subTest(changes=changes):
                self.manifest['jobs'] = [dict(self.job, **changes)]
                self.assertEqual(self.run_runner()[0], 1)
        self.assertEqual(self.posts, [])
        self.manifest['jobs'] = [dict(self.job, end_image='after.png')]
        self.assertEqual(self.run_runner()[0], 0)
        self.assertEqual(len(self.posts), 1)

    def test_new_gated_job_requires_occurrence_identifier(self):
        del self.job['shot_id']
        self.assertEqual(self.run_runner()[0], 1)
        self.assertEqual(self.posts, [])

    def test_url_chained_and_params_frames_cannot_claim_local_still_review(self):
        for value in ['https://example.test/frame.png', {'job': 'earlier'}, 'data:image/png;base64,eA==']:
            with self.subTest(value=value), self.assertRaises(h3.ContinuityReviewError):
                h3.continuity_approval('review.json', self.root, [dict(self.job, image=value)])
        with self.assertRaises(h3.ContinuityReviewError):
            h3.continuity_approval('review.json', self.root, [dict(self.job, params={'end_image_url': 'https://example.test/frame.png'})])


if __name__ == '__main__':
    unittest.main()
