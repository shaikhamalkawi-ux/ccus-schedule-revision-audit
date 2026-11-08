# Public companion manifest

**Associated study:** *Reported Schedule Revisions and the 2030 CCUS Capacity Picture: Evidence from IEA Database Releases* — Gases `gases-4620358`, R5 author-review candidate.

## Existing public materials (retained)

- `data/` — compact CCUS, hydrogen, EIA-860M and Berkeley Lab Queued Up derived audit summaries, source manifest/adapters and claim-boundary objects.
- `CITATION.cff`, `.zenodo.json` — author/citation metadata; no assigned DOI.
- `LICENSE_AND_THIRD_PARTY_NOTICE.md`, `DATA_INVENTORY.md` — rights and holdings boundaries.

## Added on 8 November 2026

- `tools/readiness_margin.py` — deterministic year-field cutoff audit; input is already matched/admitted, not raw IEA data.
- `examples/SYNTHETIC_pairwise_example.csv` — invented test data, not real CCUS projects.
- `tests/` — synthetic and aggregate consistency checks.
- `results/` — **aggregate-only** 2025/2026 cutoff comparison and signed revision-year histogram.
- `docs/` — decision-relevant contribution, exact input contract, reuse protocol, and review-stage release note.

The repository is not a full mirror of the R4.2 provisional journal supplementary archive (see `REPOSITORY_STATUS.md`). Source-record movement must not be equated with physical project delay or lost physical capacity. Cross-domain rates are not pooled.

## R5 extension

The cutoff-crossing aggregate, its reproducibility script and an interpretation guide were added on 8 November 2026. This adds no raw IEA files or historical human-coder submissions. The numbers remain review-stage results, not an accepted journal article.
