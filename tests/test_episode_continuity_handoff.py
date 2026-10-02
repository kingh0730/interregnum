"""A valid media package must not restore withdrawn spatial approval."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "episodes/ep01/build/package_delivery.py"
SPEC = importlib.util.spec_from_file_location("episode_delivery", SCRIPT)
delivery = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(delivery)


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
