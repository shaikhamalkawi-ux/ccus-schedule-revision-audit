# Supporting Data — Same-Project Schedule-Revision Audit

This repository is the **public browsable companion repository** for:

**More Projects, Not Necessarily Earlier Operation: A Same-Project Audit of Reported Schedule Revisions in Global CCUS Records with a Hydrogen Portability Test**

Repository: https://github.com/shaikhamalkawi-ux/ccus-schedule-revision-audit

## What this repository supports

The study audits persistent project records across successive database releases and distinguishes:

- changes in the reported schedule of the **same project record**;
- changes caused by portfolio entry, exit, or redefinition;
- fixed-baseline planning-horizon quantities from full source-vintage portfolio quantities.

The primary empirical application is CCUS. A hydrogen application is the principal portability test, with EIA-860M and Berkeley Lab *Queued Up* used as additional direct checks. Cross-domain percentages are **not pooled**.

## Repository scope

GitHub is used here as the **browsable provenance and summary layer**. The `data/` directory contains machine-readable audit summaries, adapters, source manifests, horizon results, identity checks, claim-evidence maps, and other lightweight derived objects.

The **complete R3R7 supporting-data archive**, including larger longitudinal CSV files and binary workbooks, is prepared for archival deposit in **Zenodo**. Once the Zenodo record is published, its DOI will be added here and to the manuscript Data Availability Statement.

## Key claim boundaries

- A revised database field is **not automatically a physical project delay**.
- A fixed-baseline planning-horizon effect is **not realized physical capacity loss**.
- Persistent database identity does not by itself prove unchanged physical-project scope.
- The repository documents audit portability across the tested databases; it does not provide a universal delay, failure, or correction rate.

## Reproducibility boundary

The exact historical CCUS replay archive named in the manuscript is **not included here or in the prepared Zenodo deposit**. Derived files must not be presented as substitutes for that unavailable historical original.

## Source and licensing notes

This repository contains derived audit materials rather than redistributed third-party raw workbooks.

- IEA CCUS Projects Database: CC BY 4.0.
- IEA Hydrogen Production and Infrastructure Projects Database: CC BY 4.0.
- U.S. EIA materials: U.S. government public-domain material, with attribution recommended.
- Berkeley Lab *Queued Up* data file: CC BY 4.0.
- Other source-specific rights remain with their respective owners.

Author-generated documentation and derived audit tables are intended for scholarly reuse with attribution. Third-party content and source-derived material remain subject to the original source licences and terms.

## Citation

Please cite the associated manuscript and, once assigned, the Zenodo DOI for the complete supporting-data release.

## Version

Repository prepared from the **R3R7 scientific-freeze supporting-data package**.
