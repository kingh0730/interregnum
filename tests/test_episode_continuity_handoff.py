"""A valid media package must not restore withdrawn spatial approval."""
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "episodes/ep01/build/package_delivery.py"
SPEC = importlib.util.spec_from_file_location("episode_delivery", SCRIPT)
delivery = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(delivery)


class PreflightHistoryTests(unittest.TestCase):
    def finish_report(self, directory, ready):
        # Execute the script's real report-writing/exit block in isolation from
        # expensive media checks. Fresh check results are supplied at its boundary.
        script = SCRIPT.with_name("motion_preflight.py")
        source = script.read_text()
        finalization = source[source.index("out=B/'motion_preflight.json'"):]
        report = {"local_media_ready": True, "continuity_approved": ready,
                  "ready_for_motion": ready, "errors": [], "missing_sources": [],
                  "budget": {}, "runner_dry_run_performed": False,
                  "video_requests_submitted": 0}
        with redirect_stdout(io.StringIO()), self.assertRaises(SystemExit) as caught:
            exec(compile(finalization, str(script), "exec"),
                 {"B": directory, "report": report, "json": json, "sys": sys})
        self.assertEqual(caught.exception.code, 0 if ready else 2)
        saved = json.loads((directory / "motion_preflight.json").read_text())
        self.assertEqual(saved["ready_for_motion"], ready)
        self.assertEqual(saved["continuity_approved"], ready)
        self.assertFalse(saved["runner_dry_run_performed"])
        return saved

    def test_damaged_history_is_replaced_without_changing_fresh_approval(self):
        for previous in [b'{"local_media_ready":', b'\xff', b'null', b'[]', b'42']:
            for ready in (False, True):
                with self.subTest(previous=previous, ready=ready), tempfile.TemporaryDirectory() as td:
                    directory = Path(td)
                    (directory / "motion_preflight.json").write_bytes(previous)
                    saved = self.finish_report(directory, ready)
                    self.assertIn("history_read_warning", saved)

    def test_valid_history_is_retained_without_restoring_old_approval(self):
        with tempfile.TemporaryDirectory() as td:
            directory = Path(td)
            previous = {"ready_for_motion": True, "continuity_approved": True,
                        "runner_dry_run_performed": True, "runner_estimate_usd": 8.28,
                        "manifest_sha256": "old-manifest",
                        "superseded_spatial_approval_history": [{"reason": "withdrawn"}]}
            (directory / "motion_preflight.json").write_text(json.dumps(previous))
            saved = self.finish_report(directory, False)
            self.assertEqual(saved["superseded_spatial_approval_history"],
                             previous["superseded_spatial_approval_history"])
            self.assertEqual(saved["previous_runner_quote"]["runner_estimate_usd"], 8.28)
            self.assertNotIn("history_read_warning", saved)

    def test_first_run_needs_no_previous_report(self):
        with tempfile.TemporaryDirectory() as td:
            saved = self.finish_report(Path(td), False)
            self.assertNotIn("history_read_warning", saved)


class DeliveryApprovalTests(unittest.TestCase):
    def test_blocked_or_missing_review_preserves_withdrawn_delivery(self):
        for present in (False, True):
            with self.subTest(present=present), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                build = root / "episodes/ep01/build"
                build.mkdir(parents=True)
                (build / "motion_plan.json").write_text(json.dumps({"continuity_review": "review.json"}))
                if present:
                    (root / "review.json").write_text(json.dumps({"schema_version": 1, "status": "blocked"}))
                previous = b'{"status":"spatial approval withdrawn"}\n'
                (build / "delivery_manifest.json").write_bytes(previous)
                with patch.object(delivery, "ROOT", root), patch.object(delivery, "B", build):
                    with self.assertRaisesRegex(ValueError, "Continuity approval required"):
                        delivery.main()
                self.assertEqual((build / "delivery_manifest.json").read_bytes(), previous)

    def test_approved_record_cannot_override_withdrawn_visual_review(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            build = root / "episodes/ep01/build"
            build.mkdir(parents=True)
            (build / "motion_plan.json").write_text(json.dumps({"continuity_review": "review.json"}))
            (build / "visual_review.json").write_text(json.dumps({"status": "withdrawn"}))
            review = {key: {"path": f"episodes/ep01/build/{name}"} for key, name in
                      [("story", "story.json"), ("assets", "assets.json"), ("states", "reel_states.json")]}
            review_path = root / "review.json"
            review_path.write_text(json.dumps(review))
            approved = {"approved": True, "errors": [], "review_path": str(review_path)}
            with patch.object(delivery, "ROOT", root), patch.object(delivery, "B", build), \
                    patch.object(delivery, "evaluate_review", return_value=approved):
                with self.assertRaisesRegex(ValueError, "Visual approval has not passed"):
                    delivery.main()
            self.assertFalse((build / "delivery_manifest.json").exists())


if __name__ == "__main__":
    unittest.main()
