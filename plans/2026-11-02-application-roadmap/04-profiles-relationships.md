# Phase 04 — Add profiles, allocations and transaction relationships

**Status:** Not started. No implementation gate is closed by creating this document.

[Roadmap and execution contract](overview.md) · [Acceptance matrix](acceptance-matrix.md)

## Goal and boundaries

Split a payment between personal/business purposes and explore linked money flows without
fabricating another payment. Dedicated reimbursement balances and formal owner-equity
accounting remain deferred.

## Entry gates

G03; H02 additionally required for real-data trials.

Verify gate evidence against the current implementation before starting dependent work.
Investigation and independent work may proceed while a gate is pending; do not claim a
phase complete or use real data without the applicable technical and human gates.

## Implementation slices

- [ ] Add personal/business profiles and explicit logical-account/profile relationships
      with stable identities.
- [ ] Add category splits and cross-profile allocations, including an explicit unallocated
      remainder.
- [ ] Introduce typed relationship contracts for supported refunds/transfers and extension
      points for loan links; add custom descriptive links/groups.
- [ ] Build linked-record views with partial amounts, explanations and totals based on
      canonical movements rather than graph traversal duplication.
- [ ] Extend saved revisions, validation, backup/restore and migration fixtures to
      profiles, allocations and relationships.

Deliver each coherent slice with focused tests, a runnable demonstration where applicable,
and a local commit. Update this checklist and the gate register after meaningful progress.

## Interfaces, data and failure behavior

Keep movement, economic allocation and contextual relationships separate. Define built-in
calculation semantics in domain rules and test them. Custom links are descriptive. Do not
introduce an unrestricted user-programmable accounting language. A descriptive
reimbursement link is possible without claiming a computed amount owed. Restricted
transmission is phase 13.

Apply the shared verification and compatibility contract in the overview. Extend
migrations, backup/restore, revisions and privacy checks whenever this phase introduces
persisted data.

## Acceptance and verification

- [ ] G04: A KES 6,000 payment split KES 4,000 business / KES 2,000 personal creates one
      movement and correctly scoped expenses.
- [ ] Split totals reconcile exactly; invalid totals fail and incomplete allocations
      expose their remainder.
- [ ] Partial/multiple refunds and linked repayments do not double-count the source
      movement.
- [ ] Custom labels such as investment, returns or losses do not silently change balances
      or prove realized gains/losses.
- [ ] Link cycles, repeated edges, deletion and later corrections have defined behavior
      and do not corrupt grouped totals.
- [ ] Profile filtering and backup round trips preserve IDs, scopes and link meaning; no
      claim of cryptographic isolation between local profiles is made.

Record commands, results, fixture/dataset versions and device evidence below. A blocked or
unexecuted check is not a pass. Fix material failures before closing this phase's gate.

## Human actions

No new approval gate. Collect feedback on the split-payment and linked-record journeys at
the next milestone; technical work continues if prerequisites pass.

## Decisions to resolve during implementation

Document relationship cardinality, partial-amount rules and invalid-cycle handling based
on financial invariants. Agents may improve representation; changing a label into
accounting behavior is a product change requiring agreement.

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
