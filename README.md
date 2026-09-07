# Supporting Data — Same-Project Schedule-Revision Audit

This repository contains the **derived, machine-readable supporting materials** for:

**More Projects, Not Necessarily Earlier Operation: A Same-Project Audit of Reported Schedule Revisions in Global CCUS Records with a Hydrogen Portability Test**

## What this repository supports

The primary analysis audits persistent project records across successive database releases and distinguishes:

- changes in the reported schedule of the **same project record**;
- changes caused by portfolio entry, exit, or redefinition;
- fixed-baseline planning-horizon quantities from full source-vintage portfolio quantities.

The primary empirical application is CCUS. A hydrogen application is the principal portability test, with EIA-860M and Berkeley Lab *Queued Up* used as additional direct checks. Cross-domain percentages are **not pooled**.

## Key claim boundaries

- A revised database field is **not automatically a physical project delay**.
- A fixed-baseline planning-horizon effect is **not realized physical capacity loss**.
- Persistent database identity does not by itself prove unchanged physical-project scope.
- The repository documents audit portability across the tested databases; it does not provide a universal delay, failure, or correction rate.

## Contents

The `data/` directory contains the same machine-readable supporting objects supplied with the audited R3R7 supplementary-data package, including:

- `CCUS_PRIMARY_371.csv`
- CCUS provenance / evidence-register objects
- Hydrogen 190-record and strict-cohort files
- EIA-860M 933-record longitudinal files and source manifests
- Berkeley Lab *Queued Up* 4,464-record longitudinal files
- cross-domain result workbook
- claim-evidence and claim-boundary maps
- hashes and file manifests

## Reproducibility boundary

The exact historical CCUS replay archive named in the manuscript is **not included here**. Derived files in this repository must not be presented as substitutes for that unavailable historical original.

## Source and licensing notes

The repository contains derived audit materials rather than redistributed third-party raw workbooks.

- IEA CCUS Projects Database: CC BY 4.0.
- IEA Hydrogen Production and Infrastructure Projects Database: CC BY 4.0.
- U.S. EIA materials: U.S. government public-domain material, with attribution recommended.
- Berkeley Lab *Queued Up* data file: CC BY 4.0.
- Other source-specific rights remain with their respective owners.

Author-generated documentation and derived audit tables are intended for scholarly reuse with attribution. Third-party content and source-derived material remain subject to the original source licences and terms.

## Citation

Please cite the associated manuscript and, once assigned, the Zenodo DOI for this supporting-data release.

## Version

Repository release prepared from the **R3R7 scientific-freeze supporting-data package**.
