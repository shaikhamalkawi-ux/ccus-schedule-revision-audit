"""Validate aggregate snapshots without requiring third-party project-level inputs."""
import csv
import unittest
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGG = ROOT / 'results' / 'CCUS_2025_2026_Readiness_Margin_AGGREGATE.csv'
HIST = ROOT / 'results' / 'CCUS_2025_2026_ReportedYearRevision_HISTOGRAM.csv'


class AggregateReleaseTests(unittest.TestCase):
    def test_vintage_margins_and_frozen_m0(self):
        with AGG.open(newline='', encoding='utf-8') as fh:
            items = list(csv.DictReader(fh))
        self.assertEqual(len(items), 8)
        indexed = {(r['portfolio'], int(r['margin_years'])): r for r in items}
        self.assertEqual(len(indexed), 8)
        self.assertEqual({m for _, m in indexed}, {0, 1, 2, 3})
        for port, n, b, e in [
            ('capture', '269', '295.540', '280.530'),
            ('storage', '173', '547.092', '519.492'),
        ]:
            self.assertEqual(indexed[(port, 0)]['known_capacity_records'], n)
            self.assertEqual(indexed[(port, 0)]['baseline_2025_MtCO2_per_year'], b)
            self.assertEqual(indexed[(port, 0)]['endpoint_2026_MtCO2_per_year'], e)
            prev_old, prev_new = Decimal('Infinity'), Decimal('Infinity')
            for m in range(4):
                r = indexed[(port, m)]
                self.assertEqual(int(r['cutoff_year']), 2030 - m)
                base = Decimal(r['baseline_2025_MtCO2_per_year'])
                updated = Decimal(r['endpoint_2026_MtCO2_per_year'])
                change = Decimal(r['delta_MtCO2_per_year'])
                p = Decimal(r['pct_change_vs_2025_baseline'])
                self.assertEqual(change, updated - base)
                self.assertLess(abs(p - (change / base * 100)), Decimal('0.001'))
                self.assertLessEqual(base, prev_old)
                self.assertLessEqual(updated, prev_new)
                prev_old, prev_new = base, updated

    def test_year_histogram_is_consistent(self):
        with HIST.open(newline='', encoding='utf-8') as fh:
            records = list(csv.DictReader(fh))
        counter = {int(r['revision_years_2026_minus_2025']): int(r['record_count']) for r in records}
        self.assertEqual(sum(counter.values()), 461)
        self.assertEqual(counter[0], 316)
        self.assertEqual(sum(v for k, v in counter.items() if k > 0), 138)
        self.assertEqual(sum(v for k, v in counter.items() if k < 0), 7)
        self.assertEqual(counter[1] + counter[2], 106)


if __name__ == '__main__':
    unittest.main()
