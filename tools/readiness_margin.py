#!/usr/bin/env python3
"""Version-aware CCUS readiness-cutoff audit (Python standard library only).

Inputs must already be an exact-ID, same-status, numeric-Operation-year,
2025/2026 same-definition cohort. This script does NOT establish those
source-admission conditions, physical delay, or engineering readiness.
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from decimal import Decimal, InvalidOperation
from pathlib import Path

REQUIRED = (
    "ID", "Status", "Project_type_2025", "Operation_2025",
    "Operation_2026", "IEA_est_capacity_2025",
)
PORTFOLIOS = {
    "capture": frozenset(("capture", "ccu", "full chain")),
    "storage": frozenset(("storage", "t&s", "full chain")),
}
FIELDS = (
    "portfolio", "margin_years", "cutoff_year", "known_capacity_records",
    "eligible_records_2025", "eligible_records_2026",
    "baseline_2025_MtCO2_per_year", "endpoint_2026_MtCO2_per_year",
    "delta_MtCO2_per_year", "pct_change_vs_2025_baseline",
)


def _year(value: str, label: str) -> int:
    try:
        d = Decimal(value.strip())
    except (InvalidOperation, AttributeError) as exc:
        raise ValueError(f"{label}: not a numeric year: {value!r}") from exc
    if not d.is_finite() or d != d.to_integral_value() or not 1900 <= d <= 2200:
        raise ValueError(f"{label}: not a finite integer year in [1900, 2200]: {value!r}")
    return int(d)


def _capacity(value: str, label: str) -> Decimal | None:
    if not value.strip():
        return None
    try:
        d = Decimal(value.strip())
    except InvalidOperation as exc:
        raise ValueError(f"{label}: non-numeric 2025 capacity: {value!r}") from exc
    if not d.is_finite() or d < 0:
        raise ValueError(f"{label}: capacity must be finite and nonnegative")
    return d


def load_admitted_cohort(path: str | Path) -> list[dict]:
    """Read and check a previously admitted matched cohort, without imputing cells."""
    with Path(path).open(encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        actual = set(reader.fieldnames or [])
        missing = set(REQUIRED) - actual
        if missing:
            raise ValueError(f"Missing required columns: {sorted(missing)}")
        records, seen = [], set()
        for line, row in enumerate(reader, 2):
            rid = row["ID"].strip()
            if not rid or rid in seen:
                raise ValueError(f"Row {line}: blank or duplicate ID {rid!r}")
            seen.add(rid)
            status = row["Status"].strip().lower()
            if status not in ("planned", "under construction"):
                raise ValueError(f"Row {line}: ineligible matched status {status!r}")
            if "Status_2025" in actual and "Status_2026" in actual:
                if row["Status_2025"].strip() != row["Status_2026"].strip():
                    raise ValueError(f"Row {line}: native status changed across vintages")
            y0 = _year(row["Operation_2025"], f"Row {line} Operation_2025")
            y1 = _year(row["Operation_2026"], f"Row {line} Operation_2026")
            cap = _capacity(row["IEA_est_capacity_2025"], f"Row {line}")
            records.append({
                "id": rid, "status": status,
                "type": row["Project_type_2025"].strip().lower(),
                "year_2025": y0, "year_2026": y1, "cap_2025": cap,
            })
    if not records:
        raise ValueError("No records in admitted cohort")
    return records


def calculate(records: list[dict], horizon: int = 2030, max_margin: int = 3):
    """Return 2025/2026 fixed-2025-capacity horizons and signed year histogram."""
    if not isinstance(horizon, int) or not 1900 <= horizon <= 2200:
        raise ValueError("Invalid integer horizon")
    if not isinstance(max_margin, int) or not 0 <= max_margin <= 30:
        raise ValueError("Margin must be an integer between 0 and 30")
    shifts = Counter(x["year_2026"] - x["year_2025"] for x in records)
    out = []
    for name, types in PORTFOLIOS.items():
        cohort = [r for r in records if r["type"] in types and r["cap_2025"] is not None]
        for margin in range(max_margin + 1):
            cutoff = horizon - margin
            old = [r for r in cohort if r["year_2025"] <= cutoff]
            new = [r for r in cohort if r["year_2026"] <= cutoff]
            base = sum((r["cap_2025"] for r in old), Decimal(0))
            updated = sum((r["cap_2025"] for r in new), Decimal(0))
            change = updated - base
            pct = (change / base * 100) if base != 0 else None
            out.append({
                "portfolio": name, "margin_years": margin, "cutoff_year": cutoff,
                "known_capacity_records": len(cohort),
                "eligible_records_2025": len(old), "eligible_records_2026": len(new),
                "baseline_2025_MtCO2_per_year": f"{base:.3f}",
                "endpoint_2026_MtCO2_per_year": f"{updated:.3f}",
                "delta_MtCO2_per_year": f"{change:+.3f}",
                "pct_change_vs_2025_baseline": "NA" if pct is None else f"{pct:+.3f}",
            })
    return out, shifts


def write_csv(path: Path, rows: list[dict], fields: tuple[str, ...]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def run_cli() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_csv", type=Path, help="Pre-admitted matched cohort; do NOT supply raw IEA workbooks")
    parser.add_argument("--output-dir", type=Path, default=Path("results"))
    parser.add_argument("--horizon", type=int, default=2030)
    parser.add_argument("--max-margin", type=int, default=3)
    args = parser.parse_args()
    records = load_admitted_cohort(args.input_csv)
    result, changes = calculate(records, args.horizon, args.max_margin)
    write_csv(args.output_dir / "readiness_margin_aggregate.csv", result, FIELDS)
    counts = [
        {"revision_years_2026_minus_2025": d, "record_count": n}
        for d, n in sorted(changes.items())
    ]
    write_csv(
        args.output_dir / "reported_year_revision_histogram.csv",
        counts, ("revision_years_2026_minus_2025", "record_count"),
    )
    print(f"PASS: {len(records)} admitted records; "
          f"{sum(v for k, v in changes.items() if k > 0)} later, "
          f"{changes[0]} unchanged, "
          f"{sum(v for k, v in changes.items() if k < 0)} earlier. "
          "Outputs are source-field audits, NOT measured physical delays.")


if __name__ == "__main__":
    run_cli()
