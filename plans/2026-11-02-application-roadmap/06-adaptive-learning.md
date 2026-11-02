# Phase 06 — Deliver adaptive teaching and controlled automation

**Status:** Not started. No implementation gate is closed by creating this document.

[Roadmap and execution contract](overview.md) · [Acceptance matrix](acceptance-matrix.md)

## Goal and boundaries

Teach a supported unfamiliar format through field corrections, preview predictions, and
promote only evaluated patterns. New syntax can be learned without an app update; new
unsupported financial semantics remain review-only.

## Entry gates

G05.

Verify gate evidence against the current implementation before starting dependent work.
Investigation and independent work may proceed while a gate is pending; do not claim a
phase complete or use real data without the applicable technical and human gates.

## Implementation slices

- [ ] Add annotation/correction and similar-message prediction previews with typed
      extractors, anchors/optional fields and explainable pattern candidates.
- [ ] Separate pattern induction, versioned registry, extraction, validation, evaluation
      and feedback responsibilities.
- [ ] Define critical fields per family and independent held-out evaluation, including
      sample diversity/sufficiency and calibration methodology before enabling automation.
- [ ] Implement promotion/rollback, per-field uncertainty, drift handling and
      representative review; use Balanced defaults without fabricating confidence.
- [ ] Preserve corrections and event identity during reparse; record automatic changes and
      parser versions in review summaries.
- [ ] Inspect retained templates/features for private-value memorization and add
      forget/rebuild behavior for local learning.

Deliver each coherent slice with focused tests, a runnable demonstration where applicable,
and a local commit. Update this checklist and the gate register after meaningful progress.

## Interfaces, data and failure behavior

Keep inference distinct from deterministic financial safeguards and independent
verification. Use privacy-reviewed structured corrections and templates after raw cache
expiry; do not retain disguised full messages as tokens/features. Teaching and evaluation
must not reuse the same examples under different IDs. Backup permitted learning state
deliberately and describe exclusions and rebuild limits.

Apply the shared verification and compatibility contract in the overview. Extend
migrations, backup/restore, revisions and privacy checks whenever this phase introduces
persisted data.

## Acceptance and verification

- [ ] G06: Teaching one family improves held-out variations without an application update;
      malformed/spoofed/negative examples fail safely.
- [ ] A failed regression suite blocks promotion; absent sufficient independent evidence,
      candidates stay in review instead of gaining trust from message volume.
- [ ] The recorded promotion policy contains actual datasets, critical-field metrics,
      thresholds, uncertainty and fallback behavior; aspirations in the spec are not
      claimed results.
- [ ] New pattern versions can roll back; reparsing preserves user corrections, IDs and
      prior provenance.
- [ ] Raw-message expiry/source deletion does not break structured records; unavailable
      evidence limits reevaluation explicitly without reconstructing original text.
- [ ] Forgetting local learned information prevents its continued use according to
      documented dependencies; ordinary record deletion does not silently erase unrelated
      history.
- [ ] Cache privacy, bounded execution and cancellation tests pass for learning as well as
      scanning.

Record commands, results, fixture/dataset versions and device evidence below. A blocked or
unexecuted check is not a pass. Fix material failures before closing this phase's gate.

## Human actions

No new approval gate. Provide a synthetic teach/predict/correct/rollback demonstration for
user feedback. Only the user examines private examples on-device; agents receive fictional
reproductions.

## Decisions to resolve during implementation

Choose algorithms and numerical thresholds from measured evidence, documenting them before
automatic posting is enabled. If evidence is inadequate, keep the relevant family
review-only and record the limitation; do not silently claim automation completion.
General-purpose/cloud LLMs are not required.

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
