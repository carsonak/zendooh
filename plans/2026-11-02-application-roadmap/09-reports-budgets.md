# Phase 09 — Deliver categories, reports and budgets

**Status:** Not started. No implementation gate is closed by creating this document.

[Roadmap and execution contract](overview.md) · [Acceptance matrix](acceptance-matrix.md)

## Goal and boundaries

Turn canonical records into understandable daily reports and monthly budgets. The phase
may progress independently of forecast implementation, but its final combined
demonstration includes forecast integration only after G08.

## Entry gates

G07 and G04. Forecast integration additionally requires G08.

Verify gate evidence against the current implementation before starting dependent work.
Investigation and independent work may proceed while a gate is pending; do not claim a
phase complete or use real data without the applicable technical and human gates.

## Implementation slices

- [ ] Add explicit category rules, confirmed merchant aliases and similarity-based
      suggestions with deterministic precedence and preserved manual overrides.
- [ ] Learn from final saved corrections; isolate profile-specific behavior and avoid
      treating predictions as confirmed labels.
- [ ] Add account balances/coverage, income, spending, cash flow, category/merchant
      breakdowns, period comparisons and fee trends.
- [ ] Add filters for period, account/profile and currency, distinguish uncertain amounts,
      and drill down to contributing records and linked groups.
- [ ] Add simple monthly category/account/profile budgets with progress and explicit
      transfer/fee/refund treatment.
- [ ] Add debt forecast integration when G08 is available; test accessible light/dark,
      large text, sparse-data and error states.

Deliver each coherent slice with focused tests, a runnable demonstration where applicable,
and a local commit. Update this checklist and the gate register after meaningful progress.

## Interfaces, data and failure behavior

Keep query/report calculations independent of chart widgets. Define holdings, liabilities,
cash flow and spending separately; do not promise complete net worth from incomplete
accounts. Merchant identity is context, not proof of purchase purpose. Exclude item-price
and investment-profitability claims without the required data. Advanced visualizations and
natural-language queries are future work.

Apply the shared verification and compatibility contract in the overview. Extend
migrations, backup/restore, revisions and privacy checks whenever this phase introduces
persisted data.

## Acceptance and verification

- [ ] G09: Deterministic fixtures independently establish expected report and budget
      totals, including allocations, refunds, fees, internal transfers and incomplete
      histories.
- [ ] Totals rebuild from canonical records; caches are disposable and never the sole
      source of financial truth.
- [ ] Draft edits/discards and recycled predictions do not train confirmed labels; saved
      corrections supersede automation without losing history.
- [ ] Mixed currencies are not silently summed; reports state scope, period/timezone,
      uncertainty inclusion and coverage.
- [ ] Reporting defaults to Africa/Nairobi for the Kenyan beta, preserving transaction
      instants and known source offsets; workspace timezone changes have tested
      period-boundary behavior.
- [ ] A user can trace a reported total to its records and understand incomplete balances;
      UI checks cover accessibility and state transitions.
- [ ] Category rules, labels and budgets survive migrations and backup/restore with the
      same meaning.

Record commands, results, fixture/dataset versions and device evidence below. A blocked or
unexecuted check is not a pass. Fix material failures before closing this phase's gate.

## Human actions

No new approval gate. Provide a short reporting/budget checklist using synthetic expected
totals; collect feedback at beta acceptance.

## Decisions to resolve during implementation

Choose classification algorithms and UI/chart components from measured needs. Record rule
priority, budget refund treatment and period boundaries before G09. Do not add a heavy
model or graph database merely because relationships exist.

Record the decision, rationale and validation before its dependent slice begins. Routine
implementation choices belong to the implementing agent; material product-scope or privacy
changes require user agreement. Add durable architecture decisions where needed.

## Completion evidence and local commits

- Checks and demonstrations: not run; this is an implementation plan.
- Gate result and limitations: pending.
- Implementation commits: none. Keep commits local until explicit push approval.
- Handoff: record what the next phase may rely on and any remaining independent work.

## New additions

None yet. Record date, request, rationale, acceptance impact and affected phases/gates.

## Deviations from the original plan

None yet. Record original expectation, replacement, reason, authorization where needed,
and verification. Update downstream documents before starting affected work.

## Learning notes

None yet. Record discoveries, failed assumptions, device findings and follow-up
experiments without private data or transient operational logs.
