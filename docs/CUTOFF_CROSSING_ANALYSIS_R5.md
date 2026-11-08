# Cutoff-dependent concentration audit (Gases R5 author-review)

**Question:** When a later database edition changes the reported `Operation` year on the same records, does a larger number of projects leaving a planning cutoff necessarily imply a larger capacity effect?

**Finding:** No. At the 2030 cutoff, five storage-function records leave (28.60 Mt CO2/year gross exit), one enters (1.00), and the net change is -27.60. At 2028, eight records leave with only 13.45 Mt/year of announced 2025 capacity and no record enters. The top-three concentration is 71.7% of gross storage exit at 2030 versus 62.5% at 2028.

**Study data:** Exact-ID, same-status 2025-2026 comparison, 461 matched records with complete reported years; fixed 2025 estimated capacity for 269 capture-function and 173 storage-function records. The groups overlap for Full-chain records and must not be summed.

**How to run:**

```bash
python tools/reproduce_s86.py --input PATH/TO/authorized_matched_2025_2026.csv --output-dir scratch/crossings --check-study-anchors
```

The required input columns match the input contract in `docs/REPRODUCE_READINESS_MARGIN.md`: `ID`, `Status`, `Project_type_2025`, `Operation_2025`, `Operation_2026`, `IEA_est_capacity_2025`. The script assumes source admission, stable identifiers, constant planning statuses and common field definitions have already been checked by the user. This is an arithmetic verifier, **not** a source parser.

**Definitions:** An exit has a 2025-reported year <= the cutoff and a 2026-reported year > the cutoff; an entry is the reverse. Gross capacity sums fixed 2025 weights for exiting/entering rows, net = entries - exits; top-three share divides the three largest exits' capacity by gross exiting capacity. Each percent change uses its own cutoff-specific 2025 reported capacity in the denominator.

**Claim boundary:** The analysis measures change in *recorded source information*, not a project's actual construction delay, probability of readiness, or real lost CO2 capture/storage. It does not support an all-project 15-30% schedule buffer. No original IEA workbooks, coder sheets or record-level crossing data are publicly uploaded.

**Citation:** Cite the underlying IEA archived editions, the associated Gases manuscript when published, and an immutable commit of this repository. No DOI has yet been assigned.
