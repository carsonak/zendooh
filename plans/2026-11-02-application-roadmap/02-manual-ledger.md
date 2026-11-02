# Phase 02 — Deliver the first useful manual ledger

**Status:** Not started. No implementation gate is closed by creating this document.

[Roadmap and execution contract](overview.md) · [Acceptance matrix](acceptance-matrix.md)

## Goal and boundaries

On the phone, create accounts and manual transactions, inspect totals, correct mistakes
and restore earlier values. Keep this milestone on fictional data. Automated acquisition,
loans and full multi-device conflicts are later work.

## Entry gates

G01.

Verify gate evidence against the current implementation before starting dependent work.
Investigation and independent work may proceed while a gate is pending; do not claim a
phase complete or use real data without the applicable technical and human gates.

## Implementation slices

- [ ] Add account setup, fictional sample data, list/detail/edit views and useful
      loading/empty/error states.
- [ ] Support expenses, income, cash movements, own-account transfers and separately
      attributed fees with shared validation.
- [ ] Separate evidence, interpretation, canonical movements and provider balance
      observations; retain observed/inferred/user-confirmed provenance.
- [ ] Implement in-memory drafts, Save/Discard/Continue navigation and one meaningful
      revision per saved change.
- [ ] Implement logical deletion, revision inspection and restoration through compensating
      changes, preserving stable IDs and revision parentage.
- [ ] Deliver basic scoped totals and coverage indicators; package the first useful APK
      and H01 checklist.

Deliver each coherent slice with focused tests, a runnable demonstration where applicable,
and a local commit. Update this checklist and the gate register after meaningful progress.

## Interfaces, data and failure behavior

Maintain separate account IDs and provider labels. A user-confirmed entry is not
externally verified. Preserve saved revisions and attribution in rebuildable current
views; defer remote conflict resolution, not the ability to preserve history. Prohibit
cross-currency arithmetic without an explicit supported conversion policy.

Apply the shared verification and compatibility contract in the overview. Extend
migrations, backup/restore, revisions and privacy checks whenever this phase introduces
persisted data.

## Acceptance and verification

- [ ] G02: Create, save, discard, edit, delete and restore survive restart; abandoned
      drafts do not train models or create revisions.
- [ ] Transfers do not inflate income/spending, fees count once, and repeated saves do not
      duplicate movements.
- [ ] Missing opening history is visibly incomplete; reported balances never silently
      replace calculated holdings.
- [ ] Boundary tests cover invalid amounts/dates, exact rounding/precision, currency
      differences and interrupted writes.
- [ ] Focused Compose tests cover editing/navigation and recovery from errors; Android
      execution verifies the persisted journey.
- [ ] H01: User accepts the prepared fictional-data journey on the reference phone, with
      findings recorded and material blockers fixed.

Record commands, results, fixture/dataset versions and device evidence below. A blocked or
unexecuted check is not a pass. Fix material failures before closing this phase's gate.

## Human actions

End: H01 first useful phone acceptance. Provide APK/version, installation instructions,
expected outcomes and one grouped checklist for text scaling, light/dark appearance and
the manual journey. Technical G02 may close before H01; dependent fictional-data work may
proceed, but real-data approval requires H01.

## Decisions to resolve during implementation

Default beta workflows use KES. Represent currency explicitly; unsupported multi-currency
operations fail clearly. Document accounting and opening-balance treatment before marking
G02 closed.

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
