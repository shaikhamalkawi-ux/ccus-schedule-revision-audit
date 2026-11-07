# Reproducing the readiness-margin audit

This companion code is independently runnable with **Python 3.10+ and no third-party packages**. It does **not** copy the IEA historical workbooks or the original human-coder files. The demo file is **synthetic** and has no real project records.

## 1. Run the synthetic demonstration and tests

```bash
python -m unittest discover -s tests -v
python tools/readiness_margin.py examples/SYNTHETIC_pairwise_example.csv --output-dir scratch/demo
```

Expected synthetic example: five unique admitted rows. A synthetic capture project is revised from 2030 to 2032; at cutoff 2030 the capture baseline is 8.000 and endpoint is 3.000 (units are hypothetical Mt CO2/year). The 2030-storage baseline is 1.000 and endpoint is 4.000. These are constructed test values, **not IEA observations**.

## 2. Reproduce the study's aggregate outputs when you have authorized cohort data

Obtain the paper's **admitted matched 2025–2026 project cohort** via an authorized source / applicable supplementary-data release. The code accepts a local CSV that has already passed the exact-ID, same-status, numeric-year, field-definition and data-rights gates:

`ID, Status, Project_type_2025, Operation_2025, Operation_2026, IEA_est_capacity_2025`

- Status must be `Planned` or `Under construction`; a row represents **the same native status across both editions**. The optional `Status_2025` and `Status_2026` fields, if included, are additionally tested for equality.
- The two *Operation* columns must be numeric integer years for the same persistent ID; their source definitions must have been verified as comparable by the analyst **outside** this script.
- 2025 capacity is held fixed in both calculations, in Mt CO2/year; missing capacity excludes a row **from weighted capacity only**, not the year-revision histogram.
- `Project_type_2025` controls functional eligibility: capture = Capture, CCU and Full chain; storage = Storage, T&S and Full chain. Transport alone is excluded from both functional sums.
- No missing years are imputed; duplicate or blank IDs, unsupported statuses, invalid years and negative/nonfinite capacities raise an error.

Then run:

```bash
python tools/readiness_margin.py PATH/TO/authorized_matched_2025_2026.csv --output-dir scratch/private
```

The program creates (a) `readiness_margin_aggregate.csv`, with 2025 and 2026 results, and (b) `reported_year_revision_histogram.csv`. Files are aggregate-only, but keep **record-level input outside public GitHub** unless source redistribution rights have been established.

## 3. Computation

For a functional group \(g\), cutoff \(H-m\) (horizon H=2030; margin m=0,1,2,3), fixed 2025 capacity \(c_{i,2025}\), and IEA Operation year \(y_{i,v}\) from vintage \(v\):

\[
C_{g,v}(H-m) = \sum_{i \in G_g,\; c_{i,2025}\;\mathrm{known},\;y_{i,v}\le H-m} c_{i,2025}.
\]

Report \(C_{g,2025}\), \(C_{g,2026}\), their difference, and \(100(C_{g,2026}-C_{g,2025})/C_{g,2025}\) when the 2025 baseline is positive; otherwise the percentage is `NA`.

This is a **deterministic planning-cutoff screen**, not a calibrated 15–30% contingency or an estimated probability of physical delay. The histogram counts differences between *source-reported* years only.

## 4. Reference aggregate checks (R4.2 author-review state)

- Same-definition source cohort: **461 unique IDs**; 138 later, 316 unchanged, 7 earlier.
- Positive known-capacity subsets: **269 capture**, **173 storage**; Full-chain records occur in both sets.
- At margin 0, capture 295.540 → 280.530 Mt CO2/year (about −5.08%), storage 547.092 → 519.492 (about −5.04%).
- At margin 2 (cutoff 2028), capture 168.255 → 137.968 (−18.001%); storage 287.244 → 273.794 (−4.682%).

See the published aggregate CSV in `results/`. Running the tests verifies arithmetic and formatting of that snapshot. **Independent replication of the original source admission and the 461-row cohort requires access to the source workbooks and original verification protocol; the public aggregate alone is not sufficient.**

## 5. Reuse and citation boundary

- State both edition dates and *Operation* field definitions. For 2024 versus 2025–2026, flag the cross-definition boundary.
- Distinguish the recorded year from owner-announced schedule milestones and documented physical first operation.
- Never pool CCUS effects with hydrogen, EIA-860M or Berkeley Lab queue rates as one transferable coefficient.
- Credit the IEA database editions as sources as well as citing the associated manuscript and this repository.
- **No raw IEA workbooks, original human-coder sheets, or other restricted source artifacts are included in this repository update.** Redistribution and repository licensing of historical IEA raw files require confirmation from the rights holder.
