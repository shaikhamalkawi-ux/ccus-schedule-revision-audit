# Repository completeness and limitations

The repository is a **public companion**, not a complete public mirror or a standalone raw-source replication release. It contains the pre-existing browseable cross-domain derived outputs plus a generic 2025–2026 cutoff-audit utility, synthetic test, and checked aggregate results.

## Fully checkable from this repository

- `python -m unittest discover -s tests -v`: synthetic input/rejection tests, reference-aggregate arithmetic checks, and field-revision histogram checks.
- `python tools/readiness_margin.py examples/SYNTHETIC_pairwise_example.csv --output-dir scratch/demo`: independent execution on artificial records.
- Aggregate capture/storage cutoff percentages from the recorded 2025 and 2026 capacities, with R4.2 cross-vintage m=0 anchors.

## Requires additional source rights or data

- The authentic IEA 2024/2025/2026 workbooks and exact-ID original cohort extraction.
- Original 42-case source-adjudication ledger and the two human-coder submissions.
- New analysis claiming underlying project physical delay, FID transition, realized capture/injection or causal reasons for a database field edit.

All original contributor metadata are retained in `CITATION.cff`. No DOI is invented. The public GitHub record can be cited by immutable commit after author confirmation and any later release/DOI assignment.
