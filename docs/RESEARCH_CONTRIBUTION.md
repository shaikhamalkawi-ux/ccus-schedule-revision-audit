# What this audit contributes to CCUS planning

**Decision-relevant finding.** A fixed collection of project records can yield a different reported 2030 CCUS capacity picture when the database edition changes its *Operation* year, even when the calculation holds record identity, eligible native status and baseline announced capacity constant. The size of this change depends on the cutoff applied by the planner, and the result must not be read as physically delayed or lost capacity.

## Why the study exists

Many planning, infrastructure and policy assessments use the year attached to an announced project's database record. A report may be reproducible from a single database file but may change when a different edition is used, even if the named project set is held constant. This is a **source-vintage measurement question**, not a prediction about construction.

The audit isolates the year-field revision channel with persistent source IDs and fixed baseline capacity; separate contrasts describe portfolio entry/exit, status changes, capacity revisions and scope changes. Because the 2024 and 2025–2026 IEA *Operation* field definitions differ, the 2024–2026 comparison is a **cross-definition source-field comparison**. The 2025–2026 analysis is the central **same-definition year-field sensitivity**, conditional on the documented cohort admission.

## The decision it changes

Before feeding CCUS project schedules into a scenario, source–sink network design or technology assessment:

1. Preserve the **edition, retrieval date, variable definition, persistent source ID, and original year value**.
2. When possible, perform a **same-cohort, fixed-capacity vintage comparison** rather than silently substituting one edition for another.
3. Show cutoff or readiness-margin sensitivity using the **same cutoff in both editions**. Avoid portraying the sensitivity as a physically measured delay contingency.
4. Review **high-capacity horizon crossers** and the stability of project names/scopes; show an identity sensitivity when necessary.
5. If a model needs *physical* milestones, establish these from separately dated evidence. Source-reported operational status alone is insufficient to establish first injection, sustained full-load performance or actual stored quantity.

## What is new in the public companion (pre-publication candidate)

`results/CCUS_2025_2026_Readiness_Margin_AGGREGATE.csv` compares the same selected project cohort and fixed 2025 capacity under 2025 and 2026 reported Operation years. For each function, margins 0, 1, 2 and 3 use cutoff years 2030, 2029, 2028 and 2027, respectively. The point is to show **cutoff-dependent vintage sensitivity**, not to estimate an optimal schedule buffer.

The resulting percentages are **not** universal CCUS delays, forecasting correction factors, or transferable cross-sector rates. The capture and storage portfolios are analytical function sets that both include Full-chain records; their capacities must **not** be summed as disjoint totals.

## Distinct evidence types

- **Authors' calculations:** this repository's aggregate horizon and year-field-revision tables, based on admitted IEA same-definition 2025–2026 records.
- **Source data:** IEA CCUS Projects Database editions. The IEA owns the source records; the archived raw workbooks are not redistributed here.
- **Engineering interpretation:** possible as a planning use case, but no specific engineering bottleneck is inferred as the cause of a field edit without project-level contemporaneous source evidence.
- **Publication state:** Gases manuscript `gases-4620358`, major-revision author-review candidate R4.2, **not accepted or resubmitted at the time of this update**.

## How to cite

Cite the associated manuscript by title and authors (and its final DOI once assigned), this repository at an immutable commit/tag, and the exact IEA editions from which source data were obtained. No manuscript, repository-release or Zenodo DOI is asserted here before one actually exists.
