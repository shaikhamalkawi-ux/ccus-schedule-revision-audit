"""End-to-end checks of the documented wrapper; synthetic examples only."""
import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class OneCommandTests(unittest.TestCase):
    def call(self, *args):
        return subprocess.run([sys.executable, str(ROOT / "run_audit.py"), *map(str, args)], capture_output=True, text=True)

    def test_demo_and_provenance(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "output"
            p = self.call("--demo", "--output-dir", out)
            self.assertEqual(p.returncode, 0, p.stderr)
            q = json.loads((out / "run_provenance.json").read_text())
            self.assertEqual((q["cohort_records"], q["later"], q["unchanged"], q["earlier"]), (5, 2, 2, 1))
            self.assertTrue(q["synthetic_expected_outputs_checked"])
            self.assertFalse(q["study_anchors_checked"])
            self.assertIn("synthetic", json.loads((out / "S86_QA.json").read_text())["source"])
            with (out / "S86_cutoff_crossing_summary.csv").open() as f:
                self.assertEqual(len(list(csv.DictReader(f))), 8)

    def test_requires_admission_acknowledgment(self):
        with tempfile.TemporaryDirectory() as d:
            p = self.call("--input", ROOT / "examples/SYNTHETIC_pairwise_example.csv", "--output-dir", Path(d) / "out")
            self.assertNotEqual(p.returncode, 0)
            self.assertIn("--admitted-cohort", p.stderr)

    def test_does_not_overwrite_outputs(self):
        with tempfile.TemporaryDirectory() as d:
            marker = Path(d) / "keep.txt"; marker.write_text("preserve")
            p = self.call("--demo", "--output-dir", d)
            self.assertNotEqual(p.returncode, 0)
            self.assertEqual(marker.read_text(), "preserve")

    def test_no_study_claim_for_demo(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertNotEqual(self.call("--demo", "--check-study-anchors", "--output-dir", d).returncode, 0)

    def test_unknown_type_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            inp = Path(d) / "bad.csv"
            inp.write_text((ROOT / "examples/SYNTHETIC_pairwise_example.csv").read_text().replace("Capture", "Unknown", 1))
            p = self.call("--input", inp, "--admitted-cohort", "--output-dir", Path(d) / "out")
            self.assertNotEqual(p.returncode, 0)
            self.assertIn("unknown project type", p.stderr)


if __name__ == "__main__":
    unittest.main()
