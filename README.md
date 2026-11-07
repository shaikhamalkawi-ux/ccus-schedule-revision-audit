# CCUS Schedule-Revision Audit — research companion

**Manuscript:** *Reported Schedule Revisions and the 2030 CCUS Capacity Picture: Evidence from IEA Database Releases*  
**Journal:** Gases (MDPI), manuscript `gases-4620358` — major-revision **author-review candidate** R4.2 (not accepted or resubmitted as of 8 November 2026).  
**Authors:** Ghassan Malkawi; Ahmed Abdelaziz Elsayed; Noura Alnuaimi; Hani Abusharkh; Anas Lataifeh; Abdulwehab Ibrahim; Akhtar Khalil.

This is the **public, browsable companion** for the study. It is **not** a mirror of the original IEA workbooks or the private coder documentation, and it does not claim to be independently source-replayable from public files alone.

## Research contribution

A same-record project database may report a different *Operation* year in a new edition even when the source ID and status persist. With baseline announced capacity fixed, these revisions can change a **planning-horizon** quantity; that change is **not by itself** a physical delay or a loss of actual capacity. The sensitivity also changes when planners require readiness in advance of the 2030 horizon.

The method separates source-edition/field-definition changes from portfolio entry/exit, status changes and capacity revisions. Because the *Operation* definition changed after the 2024 edition, the 2025–2026 comparison is the main **same-definition** check; the 2024–2026 contrast is retained as a broader source-field comparison.

Read [What the study contributes](docs/RESEARCH_CONTRIBUTION.md) for the decision-facing principle and claim boundaries.

## Quick start: use the method

All new audit tools use Python 3.10+ and the standard library only.

```bash
python -m unittest discover -s tests -v
python tools/readiness_margin.py examples/SYNTHETIC_pairwise_example.csv --output-dir scratch/demo
```

The demo is **synthetic**. To reproduce the research aggregates, provide a lawful copy of the already-admitted same-ID / same-status / same-definition matched 2025–2026 cohort using the documented columns; see [the reproduction and input-contract guide](docs/REPRODUCE_READINESS_MARGIN.md).

## New reviewer-driven planning-cutoff analysis

The new aggregate results compare *the same functional cohort, fixed 2025 capacity, and the same cutoff* under reported 2025 and 2026 Operation years.

| Required cutoff | Capture: 2025 → 2026 (Mt CO2/yr) | Storage: 2025 → 2026 (Mt CO2/yr) |
| --- | ---: | ---: |
| By 2030 (0-year margin) | 295.540 → 280.530 (−5.08%) | 547.092 → 519.492 (−5.04%) |
| By 2029 (1-year margin) | 196.687 → 180.306 (−8.33%) | 330.444 → 301.744 (−8.69%) |
| By 2028 (2-year margin) | 168.255 → 137.968 (−18.00%) | 287.244 → 273.794 (−4.68%) |
| By 2027 (3-year margin) | 116.804 → 64.811 (−44.51%) | 203.104 → 131.104 (−35.45%) |

This is a **deterministic margin-of-readiness screen**, **not** a recommended 15–30% contingency, a model of construction delays, or a prediction of realized capture/storage. Large effects at early cutoffs partly reflect portfolio concentration near cutoff years, not a calibrated probability of failure.

The same 461-record pairwise cohort has 138 later, 316 unchanged and seven earlier source-reported year revisions. **Capture and storage groups overlap for Full-chain records; do not add their totals.** Source-level denominators with known 2025 capacity: capture 269 records, storage 173.

- [Aggregate cutoff comparison](results/CCUS_2025_2026_Readiness_Margin_AGGREGATE.csv)
- [Year-field revision histogram](results/CCUS_2025_2026_ReportedYearRevision_HISTOGRAM.csv)
- [Method and provenance](docs/REPRODUCE_READINESS_MARGIN.md)
- [Review-stage release notes](docs/RELEASE_NOTES_2026-11-08.md)

## Other supported components

Existing `data/` files contain compact CCUS/hydrogen/EIA-860M/Berkeley Lab *Queued Up* audit records and source manifests. They remain **separate, bounded domain checks**. Do not pool their rates into a universal factor. The previous immutable git history and pre-existing companion outputs are retained.

**2024–2026 primary result remains unchanged:** 371 endpoint-complete status-stable records, 181 different years (172 later, nine earlier), with −6.09% capture and −6.78% storage under fixed 2024 capacity at 2030. The distinct same-definition 2025–2026 baseline remains −5.08% / −5.04%.

## Research use, rights and citation

Archived IEA raw workbooks and human-coder originals are **not redistributed** in this repository. The archive owner has been contacted for clarification of redistribution terms; do not interpret this public companion as permission to publish the original workbooks. See [third-party notice](LICENSE_AND_THIRD_PARTY_NOTICE.md) and [data inventory](DATA_INVENTORY.md).

Use [`CITATION.cff`](CITATION.cff) for contributor metadata and the project title. When citing a result, cite the eventual published manuscript/DOI if assigned, the **exact repository commit or release**, and the original IEA CCUS data-edition source. **No Zenodo DOI has been assigned here.** This repository update does not represent journal acceptance, a formal release, or author approval for final resubmission.
