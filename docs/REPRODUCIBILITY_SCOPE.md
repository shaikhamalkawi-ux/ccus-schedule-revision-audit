# What this public snapshot reproduces

| Operation | Public-only? | Interpretation |
|---|---|---|
| Synthetic five-record example and expected-output comparison | Yes | Software execution on an artificial fixture; not empirical validation |
| Arithmetic and count consistency of stored research aggregates | Yes | Checks existing reported outputs; does not reconstruct missing inputs |
| Same-definition cohort horizon and S86 calculations | Requires the lawfully obtained admitted input | Recomputes the fixed-capacity comparison; does not establish raw-source admission |
| Original IEA-to-cohort extraction | No | Requires original workbooks and the separate documented source workflow |
| Full 2024–2026 primary calculation | Not implemented by this wrapper | Retained in the manuscript and supplementary workflow |
| Exploratory ML AUC, average precision and Brier training replay | No | Restricted record-level inputs and fitted objects are not in this snapshot |
| Fuzzy scheduling model | No | Future work only; no such model was implemented in this study |

The two pre-existing calculation scripts and the three research-aggregate CSVs remain unchanged in version 1.0.0. Newly added files concern execution, provenance, synthetic expected outputs, tests, documentation and archive packaging. No scientific result or admission rule has been recalibrated.

On 14 November 2026, 12 unittest methods passed (7 inherited and 5 wrapper tests). An author-side regression using the already-admitted 461-record supplementary cohort reproduced 138 later, 316 unchanged and 7 earlier records and all 8 S86 cutoff rows. That regression is not a new raw-workbook audit, ML retraining or prospective validation. The row-level input is deliberately not part of this public archive.
