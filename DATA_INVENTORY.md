# Data Inventory and Availability Boundary

This file states exactly what is browsable in GitHub and what remains in the complete R3R7R3 Supplementary Data archive uploaded with the manuscript.

## A. Browsable GitHub layer

The repository `data/` directory contains lightweight derived/provenance objects, including:

- `CCUS_PRIMARY_371_identity.json`
- `CCUS_Coder_Repeatability_Note.md`
- `CalCCA_LBNL_reproduction.csv`
- `Claim_Boundary_Matrix.csv`
- `Claim_Evidence_Map.csv`
- `EIA_adapter.json`
- `EIA_horizon_strict.csv`
- `EIA_source_manifest.csv`
- `EIA_summary_metrics.csv`
- `EIA_technology_summary.csv`
- `H2_adapter.json`
- `H2_benchmark_reproduction.csv`
- `H2_horizon_primary.csv`
- `H2_horizon_strict.csv`
- `H2_identity_audit.json`
- `H2_source_manifest.csv`
- `LBNL_horizon_results.csv`
- `LBNL_identity_audit.json`
- `LBNL_outcome_summary.csv`
- `LBNL_pairwise_summary.csv`
- `LBNL_technology_sensitivity.csv`

These files are intended for rapid inspection of the audit definitions, provenance, reported summaries, horizon effects, and claim boundaries.

## B. Complete R3R7R3 Supplementary Data archive uploaded with the manuscript

The journal Supplementary Data archive additionally contains the larger longitudinal datasets and binary workbooks, including:

- `CCUS_PRIMARY_371.csv`
- `CCUS_ExternalTiming_EvidenceRegister.xlsx`
- `CrossDomain_ResultWorkbook.xlsx`
- `EIA_933.csv`
- `EIA_target2025_870.csv`
- `H2_primary190.csv`
- `H2_strict137.csv`
- `LBNL_4464.csv`
- `LBNL_outcome_ledger.csv`
- `LBNL_recorded_operation_alignment.csv`
- publication-facing coder-repeatability documentation
- full file manifests and SHA-256 records

Exact submitted archive identity:

- filename: `CCS_FGID_carbon123R3R7R3_Supplementary_Data.zip`
- size: `252689` bytes
- SHA-256: `9847bf03a50c62f7dc684e9feb860c3960ebb2541f12d3bd9ff44760dde8135f`
- internal manifest: `32` declared research/support objects verified for presence, size, and SHA-256; package-control manifest/SHA files are additional

The larger files are not duplicated individually in GitHub because the journal Supplementary Data ZIP is the authoritative complete current submission package. GitHub provides the public browsable companion layer.

## C. Historical archive limitation

The unavailable historical exact CCUS replay archive is **not** part of either the GitHub companion layer or the current journal Supplementary Data package. Its documented expected SHA-256 is:

`3f191871ba0ebf9e2f00290a00abfdf86dc4d7d319dac7eee5384a0c491e9d09`

The original two-coder workbooks are also not included. Their historical hashes are retained in `data/CCUS_Coder_Repeatability_Note.md` solely for provenance. No derived file should be described as one of those unavailable historical originals.
