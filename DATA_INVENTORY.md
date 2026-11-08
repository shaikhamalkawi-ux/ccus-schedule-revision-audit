# Data inventory and publication boundary

**Public repository:** https://github.com/shaikhamalkawi-ux/ccus-schedule-revision-audit  
**Associated manuscript:** *Reported Schedule Revisions and the 2030 CCUS Capacity Picture: Evidence from IEA Database Releases* — Gases major-revision author-review candidate R5.

## Public contents

- `data/`: pre-existing compact derived and provenance outputs for CCUS, hydrogen, EIA-860M and Berkeley Lab *Queued Up*. These remain independent domain-specific evidence layers.
- `results/CCUS_2025_2026_Readiness_Margin_AGGREGATE.csv`: eight cutoffs (0–3 years), two analytical functions, side-by-side 2025/2026 fixed-2025-capacity amounts and changes.
- `results/CCUS_2025_2026_ReportedYearRevision_HISTOGRAM.csv`: 461 matched records counted by signed difference in the **reported** Operation year.
- `tools/readiness_margin.py`: a generic year-field aggregate evaluator for an already-admitted matching cohort.
- `tests/`, `examples/`: arithmetic checks and fully fabricated example records.
- `docs/`: source-admission constraints, reproduction steps, limitations, contribution and release note.

## Controlled input layer (not in the repository)

The original IEA CCUS Projects Database Excel editions 2024, 2025, and 2026; the author's full matched identity/status/year/capacity ledger; original coder workbooks, and official historical evidence dossiers are retained outside the public repository pending source-specific redistribution clearance. **Do not publish or mirror them from this companion.**

The current R4.2 **provisional journal supplementary-data ZIP** was archived in the author's research workspace as `Gases_Supplementary_Data_R4_2_PROVISIONAL.zip` (485,964 bytes; SHA-256 `5b3941955a4c1d6c6edfaef057df1fa65d89a5cefacceca7fb110945aa6d9bcd`). It contains the original study's author-derived matched cohort and replay scripts, but **is not uploaded here** and has not been declared journal-accepted.

## What is and is not independently reproducible here

Anyone can run the synthetic example and verify the arithmetic of the eight published aggregate cells and source-field histogram. To reproduce the actual matched-record counts, source admission or exact aggregate numerics from raw workbooks requires authorized access to the dated IEA releases and the source-verification pipeline; the aggregate CSV is not a substitute for those originals.

Third-party rights remain with source owners. See the repository's `LICENSE_AND_THIRD_PARTY_NOTICE.md` and the IEA data product: https://www.iea.org/data-and-statistics/data-product/ccus-projects-database.

## R5 addendum

- `results/CCUS_2025_2026_Cutoff_Crossing_S86_AGGREGATE.csv`: aggregate-only gross exits, entries, net changes and largest-three exit shares at four common cutoff years; no record-level fields.
- `tools/reproduce_s86.py`: standard-library evaluator for an authorized, already-admitted pairwise cohort.
- `docs/CUTOFF_CROSSING_ANALYSIS_R5.md`: purpose, assumption, permission and reuse limits.
