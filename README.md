# Supporting Data — Same-Project Schedule-Revision Audit

This is the **public browsable companion repository** for:

**More Projects, Not Necessarily Earlier Operation: A Same-Project Audit of Reported Schedule Revisions in Global CCUS Records with a Hydrogen Portability Test**

Repository: https://github.com/shaikhamalkawi-ux/ccus-schedule-revision-audit

## What this repository supports

The study audits persistent project records across successive database releases and distinguishes:

- changes in the reported schedule of the **same project record**;
- changes caused by portfolio entry, exit, or redefinition;
- fixed-baseline planning-horizon quantities from full source-vintage portfolio quantities.

The primary empirical application is CCUS. Hydrogen is the principal portability test. EIA-860M and Berkeley Lab *Queued Up* are additional direct checks. Cross-domain percentages are **not pooled**.

## Repository scope

The `data/` directory exposes the lightweight machine-readable audit layer used to inspect the reported claims: adapters, source manifests, horizon results, identity checks, claim-evidence maps, claim-boundary records, and summary/reproduction tables.

The **complete current R3R7 supporting-data package**, including the larger longitudinal CSV files and binary workbooks, is supplied as the manuscript Supplementary Data archive in the journal submission. Its archival verification record is:

- package: `CCS_FGID_R3R7_Zenodo_FINAL_DEPOSIT.zip`
- size: **256,944 bytes**
- entries: **40**
- SHA-256: `39666169e1f24687255c2c58cd79d2e268538780cf8b0a04bac60d263afe30dc`

A Zenodo DOI can be added later as an additional archival identifier; the current Systems submission does not depend on Zenodo.

See `DATA_INVENTORY.md` for the separation between the browsable GitHub layer and the complete submitted Supplementary Data archive.

## Key claim boundaries

- A revised database field is **not automatically a physical project delay**.
- A fixed-baseline planning-horizon effect is **not realized physical capacity loss**.
- Persistent database identity does not by itself prove unchanged physical-project scope.
- The repository documents portability of the audit design across the tested databases; it does not provide a universal delay, failure, or correction rate.

## Reproducibility boundary

The exact historical CCUS replay archive named in the manuscript is **not included here or in the current R3R7 supporting-data archive**. Derived files must not be presented as substitutes for that unavailable historical original.

## Source and licensing notes

This repository contains derived audit materials rather than redistributed third-party raw workbooks.

- IEA CCUS Projects Database: CC BY 4.0.
- IEA Hydrogen Production and Infrastructure Projects Database: CC BY 4.0.
- U.S. EIA materials: U.S. government public-domain material, with attribution recommended.
- Berkeley Lab *Queued Up* data file: CC BY 4.0.
- Other source-specific rights remain with their respective owners.

Author-generated documentation and derived audit tables are intended for scholarly reuse with attribution. Third-party content and source-derived material remain subject to the original source licences and terms.

## Citation

Please cite the associated manuscript. If a Zenodo archival DOI is assigned later, it will be added to this repository and to the manuscript record where appropriate.

## Version

Repository prepared from the **R3R7 scientific-freeze supporting-data package**.
