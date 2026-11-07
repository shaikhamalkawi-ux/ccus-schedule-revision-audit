# 2026-11-08 — Review-stage companion enhancement (not a journal release)

This **additive** update to the existing public companion improves code usability and audit clarity. It does **not** change the manuscript's locked baseline, retroactively declare publication acceptance, or publish confidential/raw IEA records.

### Added

- `tools/readiness_margin.py`: independently runnable standard-library evaluator of matched-vintage year-field cutoff sensitivity using 2025 capacity weights.
- `tests/test_readiness_margin.py` and `tests/test_published_aggregate.py`: synthetic unit tests, input rejection tests, and consistency checks of aggregate release anchors.
- `examples/SYNTHETIC_pairwise_example.csv`: visibly artificial sample that exercises the API.
- `results/CCUS_2025_2026_Readiness_Margin_AGGREGATE.csv`: aggregate 2025/2026 horizon contrast at margins 0–3 for capture and storage.
- `results/CCUS_2025_2026_ReportedYearRevision_HISTOGRAM.csv`: source-field revision-year histogram, not physical delays.
- `docs/RESEARCH_CONTRIBUTION.md` and `docs/REPRODUCE_READINESS_MARGIN.md`: scientific rationale, method, input contract, equations, commands and claim limitations.

### Source and QA

Aggregate values were re-created from the author's R4.2 admitted same-definition pairwise CSV with 461 unique persistent IDs. The original Excel source workbooks remained on the private research side. The 0-margin capacity checks match 295.540 → 280.530 and 547.092 → 519.492 Mt CO2/year for the two analytical portfolios. Unit tests also run without nonstandard Python dependencies.

### Not changed

- The reported 2024–2026 371-record main cohort and 2030 effects −6.09% / −6.78%.
- The 2025–2026 461-record same-definition cohort and 2030 effects −5.08% / −5.04%.
- Authorship, source-vintage definitions, journal status, existing cross-domain analyses, past git history, any DOI, and IEA redistribution permissions.

### Rights / freeze gate

This is an author-review companion update, not a stable, DOI-minted reproducibility release. The public source data may be insufficient to regenerate the numeric aggregate exactly without the appropriately licensed underlying cohort. Do not call the repository "fully standalone" or claim raw-data open availability.
