# Phase 08 — Add explainable debt-cost forecasts

**Status:** Not started. No implementation gate is closed by creating this document.

[Roadmap and execution contract](overview.md) · [Acceptance matrix](acceptance-matrix.md)

## Goal and boundaries

Estimate debt costs for supported Fuliza and M-Shwari scenarios using explicit, versioned
personal defaults. Observed transactions remain authoritative; forecasts never initiate
payments or create postings. Hosting and downloadable rule updates are deferred.

## Entry gates

G07.

Verify gate evidence against the current implementation before starting dependent work.
Investigation and independent work may proceed while a gate is pending; do not claim a
phase complete or use real data without the applicable technical and human gates.

## Implementation slices

- [ ] Inspect official provider terms during implementation and document supported
      charging structures, authoritative links and the limits of available evidence.
- [ ] Build a deterministic forecasting service independent of UI, SMS parsing and network
      access.
- [ ] Add personal rule entry/edit/save with effective dates, version history, validation,
      provenance and scenario inputs.
- [ ] Show principal, expected charges, assumptions, time horizon and missing/unsupported
      conditions; link to official terms through an explicit user action.
- [ ] Preserve the rule/input versions needed to reproduce prior saved forecasts; keep
      overrides separate from any future distributed rules.
- [ ] Integrate forecast views with observed debt records without conflating estimated and
      reported balances.

Deliver each coherent slice with focused tests, a runnable demonstration where applicable,
and a local commit. Update this checklist and the gate register after meaningful progress.

## Interfaces, data and failure behavior

Treat forecast rules as validated data with bounded computation, not arbitrary executable
expressions. Domain service inputs include observed coverage and scenario assumptions;
outputs distinguish known and estimated components. Opening official terms in the browser
must not transmit transaction data. Support the required provider structures without
turning beta into a universal rule-language editor.

Apply the shared verification and compatibility contract in the overview. Extend
migrations, backup/restore, revisions and privacy checks whenever this phase introduces
persisted data.

## Acceptance and verification

- [ ] G08: Independently calculated fictional examples cover rounding, charge/time
      boundaries, applicable caps, partial repayments and supported repayment order.
- [ ] Missing dates/rules/principal or unsupported fee structures produce an
      incomplete/unsupported result, never a fabricated precise estimate.
- [ ] Editing defaults leaves observed charges and historical records unchanged; saved
      forecasts can explain which rule version produced them.
- [ ] Timezone and effective-date transitions are deterministic; rates use exact
      arithmetic and explicit rounding rules.
- [ ] Forecasts remain visibly estimates and create no ledger postings; backup/restore
      preserves supported personal defaults and their versions.
- [ ] No hosted endpoint, scraper, automatic fetch or implied current provider rate is
      required; official links are verified and personal values can be changed manually.

Record commands, results, fixture/dataset versions and device evidence below. A blocked or
unexecuted check is not a pass. Fix material failures before closing this phase's gate.

## Human actions

No new approval gate. User supplies/adjusts personal defaults on-device. Agents first
provide synthetic scenarios and clear field meanings. Do not ask the user to certify
correctness of code or expose actual debt information.

## Decisions to resolve during implementation

Document day-count, rounding, rate effective-date, repayment-order and
unsupported-condition policies before implementing their calculations. Current provider
rules must come from checked official sources, not this plan or model memory. Adding a
hosted feed requires a later approved scope.

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
