# Phase 07 — Complete beta provider and financial-semantic coverage

**Status:** Not started. No implementation gate is closed by creating this document.

[Roadmap and execution contract](overview.md) · [Acceptance matrix](acceptance-matrix.md)

## Goal and boundaries

Deliver M-Pesa, Airtel Money, Fuliza and M-Shwari in independently testable slices.
Recognizing a provider name is not coverage: enumerate supported message families and
distinguish automatic, review-only and unknown cases.

## Entry gates

G06 and G04.

Verify gate evidence against the current implementation before starting dependent work.
Investigation and independent work may proceed while a gate is pending; do not claim a
phase complete or use real data without the applicable technical and human gates.

## Implementation slices

- [ ] Before each provider slice, create a coverage matrix of transaction semantics,
      representative fictional formats, critical fields, expected postings and review-only
      limitations.
- [ ] Expand M-Pesa receipts/payments, own-account movements, withdrawals/deposits, fees
      and status/reversal handling.
- [ ] Add Airtel Money through the same shared contracts with independent account/SIM
      mappings and provider-specific fixtures.
- [ ] Add Fuliza borrowing, repayment/automatic deductions and evidenced charges,
      including association with the financed payment.
- [ ] Add M-Shwari savings deposits/withdrawals, borrowing, repayments and evidenced
      charges.
- [ ] Add reconciliation of observed balances against intervening postings, explaining
      coverage gaps and uncertain links.
- [ ] Extend persistence, correction/reparse, report projections and backup regression
      fixtures for each slice.

Deliver each coherent slice with focused tests, a runnable demonstration where applicable,
and a local commit. Update this checklist and the gate register after meaningful progress.

## Interfaces, data and failure behavior

Provider adapters/learned formats produce shared candidates, not provider-specific
ledgers. Separate principal, liability, charge and savings semantics. Negative balances
need explicit account/product interpretation; never take an absolute value to make an
invalid amount fit. Preserve provenance when several messages describe one movement. New
semantic types need domain validation even if their text can be extracted.

Apply the shared verification and compatibility contract in the overview. Extend
migrations, backup/restore, revisions and privacy checks whenever this phase introduces
persisted data.

## Acceptance and verification

- [ ] G07: Each required provider/product has an executable end-to-end fixture journey and
      a reviewed coverage matrix with no silently omitted core workflow.
- [ ] Borrowing is not income; principal repayment is not spending; supported
      interest/fees are distinct expenses.
- [ ] Savings and own-account transfers do not inflate expenses; purchase and credit
      evidence do not duplicate the same payment.
- [ ] Partial repayments, repeated references, reversals, refunds, negative balances and
      missing principal/fee breakdowns have explicit tested behavior.
- [ ] Failed/pending messages remain distinct; later evidence can reconcile them without
      duplicate movements or lost corrections.
- [ ] Balance discrepancies show expected/observed values and missing-history limits;
      account balances are not guessed from unrelated SIM/provider labels.
- [ ] Multi-account and dual-SIM end-to-end checks pass; unsupported formats are visibly
      review-only and do not silently enter established totals.

Record commands, results, fixture/dataset versions and device evidence below. A blocked or
unexecuted check is not a pass. Fix material failures before closing this phase's gate.

## Human actions

No new milestone approval. Offer installable builds after each provider slice and
consolidate feedback. User validates real-format behavior privately after H02; agents
create synthetic reproductions and must not request an inbox export.

## Decisions to resolve during implementation

Verify actual message families and product semantics from privacy-safe evidence; do not
invent provider formats or current terms. Record matching/reconciliation policy and
supported balance definitions before automatic linkage. If core coverage cannot be
delivered, request an explicit beta-scope revision rather than treating a provider as
complete.

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
