#!/usr/bin/env python3
"""Run the existing 2025--2026 fixed-capacity audit; no raw-data linkage or ML."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "tools"))
from readiness_margin import FIELDS, calculate, load_admitted_cohort, write_csv


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--demo", action="store_true", help="Use five explicitly synthetic records")
    mode.add_argument("--input", type=Path, help="Lawfully obtained, previously admitted matched cohort CSV")
    parser.add_argument("--admitted-cohort", action="store_true", help="Acknowledge that upstream identity, status and definition checks are already complete")
    parser.add_argument("--check-study-anchors", action="store_true", help="Check the specific 461-record study cohort; never use for the demo")
    parser.add_argument("--output-dir", type=Path, required=True, help="New or empty output directory")
    args = parser.parse_args()
    if args.input and not args.admitted_cohort:
        parser.error("User input requires --admitted-cohort; this tool does not establish source eligibility.")
    if args.demo and args.check_study_anchors:
        parser.error("Synthetic records cannot be checked as the 461-record study cohort.")
    input_path = ROOT / "examples/SYNTHETIC_pairwise_example.csv" if args.demo else args.input
    out = args.output_dir.resolve()
    if out.exists() and (not out.is_dir() or any(out.iterdir())):
        parser.error("Output directory must be new or empty; refusing to overwrite existing files.")
    try:
        with input_path.open(encoding="utf-8-sig", newline="") as fh:
            reader = csv.DictReader(fh)
            names = reader.fieldnames or []
            if len(names) != len(set(names)):
                raise ValueError("Duplicate CSV column names")
            for number, row in enumerate(reader, 2):
                if None in row or any(v is None for v in row.values()):
                    raise ValueError(f"Row {number}: inconsistent CSV field count")
                if row.get("Project_type_2025", "").strip().lower() not in {
                    "capture", "ccu", "full chain", "storage", "t&s", "transport"
                }:
                    raise ValueError(f"Row {number}: unknown project type; explicit mapping is required")
                optional = [x for x in ("Status_2025", "Status_2026") if x in names]
                if optional and len(optional) != 2:
                    raise ValueError("Provide both optional vintage-specific status columns, or neither")
                if optional and any(row[x].strip().lower() != row.get("Status", "").strip().lower() for x in optional):
                    raise ValueError(f"Row {number}: matched-status field contradicts vintage-specific status")
        records = load_admitted_cohort(input_path)
        rows, shifts = calculate(records, 2030, 3)
        out.mkdir(parents=True, exist_ok=True)
        write_csv(out / "readiness_margin_aggregate.csv", rows, FIELDS)
        write_csv(out / "reported_year_revision_histogram.csv", [
            {"revision_years_2026_minus_2025": k, "record_count": v}
            for k, v in sorted(shifts.items())
        ], ("revision_years_2026_minus_2025", "record_count"))
        command = [sys.executable, str(ROOT / "tools/reproduce_s86.py"),
                   "--input", str(input_path.resolve()), "--output-dir", str(out)]
        if args.check_study_anchors:
            command.append("--check-study-anchors")
        proc = subprocess.run(command, capture_output=True, text=True, check=False)
        if proc.returncode:
            raise ValueError("S86 audit failed: " + proc.stderr.strip())
        qa_file = out / "S86_QA.json"
        qa = json.loads(qa_file.read_text(encoding="utf-8"))
        qa["source"] = "Five synthetic demonstration records, not IEA projects" if args.demo else "User-supplied, previously admitted 2025--2026 matched cohort"
        qa["study_anchors_checked"] = args.check_study_anchors
        qa_file.write_text(json.dumps(qa, indent=2) + "\n", encoding="utf-8")
        expected_checked = False
        if args.demo:
            for filename in ("readiness_margin_aggregate.csv", "reported_year_revision_histogram.csv", "S86_cutoff_crossing_summary.csv"):
                expected = ROOT / "examples/expected" / filename
                if not expected.exists() or (out / filename).read_bytes() != expected.read_bytes():
                    raise ValueError("Synthetic expected-output mismatch: " + filename)
            expected_checked = True
        report = {
            "status": "PASS", "input_kind": "synthetic_demo" if args.demo else "admitted_cohort",
            "input_sha256": digest(input_path), "cohort_records": len(records),
            "later": sum(v for k, v in shifts.items() if k > 0), "unchanged": shifts[0],
            "earlier": sum(v for k, v in shifts.items() if k < 0),
            "records_without_baseline_capacity": sum(x["cap_2025"] is None for x in records),
            "study_anchors_checked": args.check_study_anchors,
            "synthetic_expected_outputs_checked": expected_checked,
            "upstream_admission": "Not established by this tool; synthetic demonstration or caller responsibility",
            "outputs": {p.name: digest(p) for p in sorted(out.iterdir()) if p.is_file()},
            "interpretation": "Source-reported year-field sensitivity only; capture and storage overlap and must not be summed; not physical delays or validated future forecasts"
        }
        (out / "run_provenance.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(f"PASS: {len(records)} records; {report['later']} later, {report['unchanged']} unchanged, {report['earlier']} earlier.")
        print("Synthetic demonstration, not research results." if args.demo else "Results are conditional on the supplied admitted cohort.")
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
