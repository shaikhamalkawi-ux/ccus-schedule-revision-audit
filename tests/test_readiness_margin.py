"""No third-party dependencies: run with `python -m unittest discover -s tests -v`."""
import csv
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from readiness_margin import load_admitted_cohort, calculate, write_csv, FIELDS  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


class ReadinessMarginTests(unittest.TestCase):
    def test_synthetic_known_results(self):
        r = load_admitted_cohort(ROOT / "examples" / "SYNTHETIC_pairwise_example.csv")
        rows, shifts = calculate(r, 2030, 1)
        cap0, cap1, sto0, sto1 = rows[0], rows[1], rows[2], rows[3]
        self.assertEqual(len(r), 5)
        self.assertEqual((shifts[0], shifts[1], shifts[2], shifts[-1]), (2, 1, 1, 1))
        self.assertEqual(cap0["baseline_2025_MtCO2_per_year"], "8.000")
        self.assertEqual(cap0["endpoint_2026_MtCO2_per_year"], "3.000")
        self.assertEqual(cap0["pct_change_vs_2025_baseline"], "-62.500")
        self.assertEqual(cap1["baseline_2025_MtCO2_per_year"], "3.000")
        self.assertEqual(cap1["endpoint_2026_MtCO2_per_year"], "3.000")
        self.assertEqual(sto0["baseline_2025_MtCO2_per_year"], "1.000")
        self.assertEqual(sto0["endpoint_2026_MtCO2_per_year"], "4.000")
        self.assertEqual(sto0["pct_change_vs_2025_baseline"], "+300.000")
        self.assertEqual(sto1["endpoint_2026_MtCO2_per_year"], "1.000")

    def test_zero_baseline_percent_is_not_invented(self):
        r = load_admitted_cohort(ROOT / "examples" / "SYNTHETIC_pairwise_example.csv")
        rows, _ = calculate(r, 2025, 0)
        self.assertEqual(rows[0]["pct_change_vs_2025_baseline"], "NA")
        self.assertEqual(rows[1]["pct_change_vs_2025_baseline"], "NA")

    def test_reject_duplicate_id(self):
        source = (ROOT / "examples" / "SYNTHETIC_pairwise_example.csv").read_text()
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "bad.csv"
            f.write_text(source + source.splitlines()[1] + "\n")
            with self.assertRaisesRegex(ValueError, "duplicate ID"):
                load_admitted_cohort(f)

    def test_reject_bad_year_and_status_and_capacity(self):
        source = (ROOT / "examples" / "SYNTHETIC_pairwise_example.csv").read_text()
        for bad, reason in [(source.replace("2030,2032", "2030,2032.5"), "not a finite integer"),
                            (source.replace("Planned", "Operational", 1), "ineligible matched status"),
                            (source.replace("2030,2032,5", "2030,2032,-5"), "nonnegative")]:
            with tempfile.TemporaryDirectory() as d:
                f = Path(d) / "bad.csv"; f.write_text(bad)
                with self.assertRaisesRegex(ValueError, reason): load_admitted_cohort(f)

    def test_output_csv_roundtrip(self):
        r = load_admitted_cohort(ROOT / "examples" / "SYNTHETIC_pairwise_example.csv")
        rows, _ = calculate(r, 2030, 3)
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "out.csv"
            write_csv(f, rows, FIELDS)
            with f.open(newline="") as fp:
                self.assertEqual(list(csv.DictReader(fp)), [{k: str(v) for k, v in row.items()} for row in rows])


if __name__ == "__main__":
    unittest.main()
