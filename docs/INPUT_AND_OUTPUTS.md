# Input contract and output interpretation

## Before running

The supported contract is an already-admitted 2025–2026 CCUS cohort, not two raw Excel releases and not arbitrary project data without a documented mapping. Confirm identity linkage, within-release uniqueness, same native status, compatible field definitions and units before preparing the input. Admission and the reasons for excluding records remain the caller's responsibility.

| Column | Required meaning |
|---|---|
| ID | Nonblank, unique source-record identifier |
| Status | Shared native status: Planned or Under construction |
| Project_type_2025 | Capture, CCU, Full chain, Storage, T&S or Transport |
| Operation_2025 | Complete numeric integer reported year |
| Operation_2026 | Complete numeric integer reported year |
| IEA_est_capacity_2025 | Fixed baseline capacity in Mt CO2/year, finite and nonnegative; blank remains missing |

Optional `Status_2025` and `Status_2026` must be supplied together and agree with `Status`. Input validation does not independently verify provenance or physical-project identity. Unknown project-type strings require an explicit documented mapping; they are rejected, not guessed.

Blank capacity is excluded from capacity-weighted totals but retained in the reported-year histogram. Missing years are not imputed. Capture includes Capture, CCU and Full chain; storage includes Storage, T&S and Full chain. These groups overlap. Transport-only records enter the year histogram but not either capacity portfolio. Baseline-zero percentage changes are NA, not zero.

## Outputs

- `readiness_margin_aggregate.csv`: fixed-baseline capacity and eligible-record counts at four cutoffs for each function.
- `reported_year_revision_histogram.csv`: signed Operation_2026 minus Operation_2025 distribution.
- `S86_cutoff_crossing_summary.csv`: exits, entries, gross and net capacity changes, and top-three gross-exit concentration.
- `S86_QA.json`: accounting checks with input-specific provenance; the wrapper replaces the historical helper's generic source label so synthetic input is not described as the empirical 461-record cohort.
- `run_provenance.json`: input SHA-256, output hashes, cohort counts, missing-capacity count and whether the study anchors or synthetic expected outputs were actually checked.

The convenience wrapper fixes the horizon to 2030 and margins to 0–3 years, matching the study. Other horizons supported by the lower-level readiness helper are different sensitivity calculations, not additional published findings. Percentages should be calculated from unrounded capacity totals; do not double-round three-decimal percentages to reproduce manuscript two-decimal values.

These outputs concern source-reported years, not physical delay, project success, realized throughput or a recommended scheduling contingency. The wrapper does not train or validate a predictive model.
