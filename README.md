# Supporting Data — Same-Project Schedule-Revision Audit

This repository is the **public R3R7 supporting-data repository** for:

**More Projects, Not Necessarily Earlier Operation: A Same-Project Audit of Reported Schedule Revisions in Global CCUS Records with a Hydrogen Portability Test**

Repository: https://github.com/shaikhamalkawi-ux/ccus-schedule-revision-audit

## What this repository supports

The study audits persistent project records across successive database releases and distinguishes:

- changes in the reported schedule of the **same project record**;
- changes caused by portfolio entry, exit, or redefinition;
- fixed-baseline planning-horizon quantities from full source-vintage portfolio quantities.

The primary empirical application is CCUS. Hydrogen is the principal portability test. EIA-860M and Berkeley Lab *Queued Up* are additional direct checks. Cross-domain percentages are **not pooled**.

## Repository structure

- `data/` — browsable derived audit summaries, adapters, source manifests, horizon results, identity checks, claim-evidence maps, and lightweight provenance objects.
- `archive/CCS_FGID_carbon123R3R7_Supplementary_Data.zip` — the **exact audited R3R7 Supplementary Data ZIP supplied with the manuscript**.
- `REPOSITORY_COMPLETENESS.md` — archive identity, SHA-256, and completeness statement.
- `CITATION.cff` — citation metadata.
- `.zenodo.json` — metadata prepared for optional Zenodo archival release.

The exact archived Supplementary Data ZIP has SHA-256:

`6120807b07c199cdd8aebe2efba45952fb1b0c7d196697c20cb8e04bdc28faa0`

Its internal manifest contains 32 declared supporting objects and was previously validated 32/32 for presence, size, and SHA-256.

## Key claim boundaries

- A revised database field is **not automatically a physical project delay**.
- A fixed-baseline planning-horizon effect is **not realized physical capacity loss**.
- Persistent database identity does not by itself prove unchanged physical-project scope.
- The repository documents portability of the audit design across the tested databases; it does not provide a universal delay, failure, or correction rate.

## Reproducibility boundary

The exact historical CCUS replay archive named in the manuscript is **not included here**. Derived files in this repository must not be presented as substitutes for that unavailable historical original.

## Source and licensing notes

This repository contains derived audit materials and the exact audited R3R7 Supplementary Data ZIP. Third-party content and source-derived material remain subject to the licences and terms of the original providers.

- IEA CCUS Projects Database: CC BY 4.0.
- IEA Hydrogen Production and Infrastructure Projects Database: CC BY 4.0.
- U.S. EIA materials: U.S. government public-domain material, with attribution recommended.
- Berkeley Lab *Queued Up* data file: CC BY 4.0.
- Other source-specific rights remain with their respective owners.

Author-generated documentation and derived audit tables are intended for scholarly reuse with attribution.

## Citation

Please cite the associated manuscript and this repository. If a Zenodo DOI is assigned later, that DOI will be added here and to `CITATION.cff`.

## Version

Repository prepared from the **R3R7 scientific-freeze supporting-data package**.
