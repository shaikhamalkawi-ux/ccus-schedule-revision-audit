# Supporting Data — Same-Record Schedule-Revision Audit

This is the **public companion repository** for the Systems submission:

**More Projects, Not Necessarily Earlier Operation: A Same-Record Audit of Reported Schedule Revisions in Global CCUS Project Records with a Hydrogen Portability Test**

Repository: https://github.com/shaikhamalkawi-ux/ccus-schedule-revision-audit

## What this repository supports

The study audits persistent project records across successive database releases and distinguishes:

- changes in the reported schedule of the **same source record**;
- changes caused by portfolio entry, exit, or redefinition;
- fixed-baseline planning-horizon quantities from full source-vintage portfolio quantities.

The primary empirical application is CCUS. Hydrogen is the principal portability test. EIA-860M and Berkeley Lab *Queued Up* are additional direct checks. Cross-domain percentages are **not pooled**.

## Repository scope

The repository is complete for its declared role as the **public browsable companion layer** for the Systems submission.

- `data/` contains machine-readable audit summaries, adapters, source manifests, horizon results, identity checks, claim-evidence maps, claim-boundary records, the publication-facing coder-repeatability note, and other lightweight provenance/reproduction objects.
- `DATA_INVENTORY.md` states which larger longitudinal files and binary workbooks are carried in the journal Supplementary Data archive rather than duplicated individually in GitHub.
- `CITATION.cff` provides citation metadata.
- `LICENSE_AND_THIRD_PARTY_NOTICE.md` records repository-level and third-party reuse boundaries.
- `.zenodo.json` and `ZENODO_DEPOSIT_FIELDS.md` are retained only to support an optional later Zenodo archival DOI.

The exact supporting-data ZIP used by the Systems submission has:

- size: **252,689 bytes**
- SHA-256: `9847bf03a50c62f7dc684e9feb860c3960ebb2541f12d3bd9ff44760dde8135f`
- internal manifest: **32 declared research/support objects, verified for presence, size, and SHA-256; the manifest and SHA list are additional package-control files**

The journal Supplementary Data archive remains the authoritative complete current supporting-data package. GitHub is intentionally optimized for public inspection rather than duplicating every large CSV/workbook twice.

## CalCCA provenance clarification

CalCCA's reported 62.5 MW CAISO geothermal quantity is cited to the CAISO Public Queue report, whereas its 894 MW IID and 824 MW non-California West quantities are based on Berkeley Lab *Queued Up*. The LBNL-derived CAISO component sum in this repository is 62.435 MW, 0.065 MW below the CalCCA value, and is treated as approximate cross-source agreement rather than exact rounding reproduction.

## Key claim boundaries

- A revised database field is **not automatically a physical project delay**.
- A fixed-baseline planning-horizon effect is **not realized physical capacity loss**.
- Persistent database identity supports source-record linkage but does not by itself prove unchanged physical-project scope.
- The repository documents portability of the audit design across the tested databases; it does not provide a universal delay, failure, or correction rate.

## Reproducibility boundary

The exact historical CCUS replay archive named in the manuscript is **not included here or in the current Supplementary Data package**. Derived files must not be presented as substitutes for that unavailable historical original. The original two-coder workbooks are likewise not included; `data/CCUS_Coder_Repeatability_Note.md` retains their historical hashes solely for provenance.

## Source and licensing notes

This repository contains derived audit materials rather than a redistribution mirror of all third-party raw workbooks.

- IEA CCUS Projects Database: CC BY 4.0.
- IEA Hydrogen Production and Infrastructure Projects Database: CC BY 4.0.
- U.S. EIA materials: U.S. government public-domain material, with attribution recommended.
- Berkeley Lab *Queued Up* data file: CC BY 4.0.
- Other source-specific rights remain with their respective owners.

Author-generated documentation and derived audit tables are intended for scholarly reuse with attribution. Third-party content and source-derived material remain subject to the original source licences and terms.

## Citation

Please cite the associated manuscript and this repository. If a Zenodo DOI is assigned later, it can be added here and to `CITATION.cff`; a Zenodo DOI is not required for the current Systems submission.

## Version

Repository synchronized with **R3R7R4 Systems pre-submission cleanup freeze**. R3R7R4 changes manuscript/Supplement layout, mathematical prose, reference metadata, notation/unit consistency, and submission wording only. The supporting-data ZIP is byte-identical to R3R7R3, and the core scientific results remain unchanged from the R3R7 scientific freeze.
