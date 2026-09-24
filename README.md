# Supporting Data — CCUS Schedule-Revision Audit

This is the **public companion repository** for the manuscript:

**Reported Schedule Revisions and the 2030 CCUS Capacity Picture: Evidence from IEA Database Releases**

Current journal target: **Gases (MDPI)**.

Repository: https://github.com/shaikhamalkawi-ux/ccus-schedule-revision-audit

## What this repository supports

The study audits persistent project records across successive database releases and distinguishes:

- changes in the reported schedule of the **same source record**;
- changes caused by portfolio entry, exit, status, capacity, or source-coverage changes;
- fixed-baseline planning-horizon quantities from full source-vintage portfolio quantities.

The primary empirical application is CCUS. Hydrogen is the principal portability test. EIA-860M and Berkeley Lab *Queued Up* are additional bounded checks. Cross-domain percentages are **not pooled**.

## Current scientific state

The central CCUS calculations were re-executed directly from the archived 2024, 2025 and 2026 IEA source workbooks after SHA-256 verification. The source-level replay reproduces the 804-record balanced panel, 659 status-stable records, 371 endpoint-complete records, 181 endpoint revisions, the fixed-baseline 2030 effects, and the 78–395 margins-only identification range around the exact 95 linked status changers. It also generates the expanded 461-record same-definition 2025–2026 pairwise cohort.

The current journal Supplementary Data archive has:

- size: **459,450 bytes**
- SHA-256: `f0c1817e5638c23bf31268872e14068f2d70a54a3b24bb6b52e5b316a0386aab`
- internal manifest: **38 declared research/support objects**, plus package-control manifest/SHA files and the publication-facing raw-source addendum.

The journal Supplementary Data archive is the authoritative complete submission package. GitHub is intentionally a browsable companion rather than a byte-for-byte duplicate of every large CSV/workbook.

## Claim boundaries

- A revised database field is **not automatically a physical project delay**.
- A fixed-baseline planning-horizon effect is **not realized physical capacity loss**.
- Persistent database identity supports source-record linkage but does not by itself prove unchanged physical-project scope.
- The tested applications support portability of the audit design, not a universal cross-domain delay, failure, or correction rate.

## Reproducibility boundary

The central CCUS calculations are source-level replayable from the archived IEA workbooks using the documented hashes and current verification script. The original two-coder workbooks are not redistributed; the coder-repeatability result remains supporting evidence with documented provenance.

## Current authors

Ghassan Malkawi; Ahmed Abdelaziz Elsayed; Noura Alnuaimi; Hani Abusharkh; Anas Lataifeh; Abdulwehab Ibrahim; Akhtar Khalil.

## Citation

Please cite the associated manuscript and this repository. If a Zenodo DOI is assigned later, it can be added here and to `CITATION.cff`.
