# Phase 12 — Implement portable merging and conflict resolution

**Status:** Not started. No implementation gate is closed by creating this document.

[Roadmap and execution contract](overview.md) · [Acceptance matrix](acceptance-matrix.md)

## Goal and boundaries

Import into an existing workspace, preserve divergent history, resolve conflicts and undo
an import without silently discarding later work. Keep the merge engine independent of
file transfer or wireless transport.

## Entry gates

G11 and H03. Read-only design research may proceed earlier without delaying beta.

Verify gate evidence against the current implementation before starting dependent work.
Investigation and independent work may proceed while a gate is pending; do not claim a
phase complete or use real data without the applicable technical and human gates.

## Implementation slices

- [ ] Define validated portable operation/revision contracts using existing stable IDs,
      causal parents and schema versions.
- [ ] Stage incoming data, preview consequences and apply complete validated batches
      atomically.
- [ ] Merge compatible independent edits only when the combined result satisfies financial
      invariants; preserve incompatible branches for review.
- [ ] Record merge attribution, parent revisions, algorithm version and batch journals of
      actual changes.
- [ ] Implement compensating undo with dependent-work preview, tombstones and explicit
      resolution choices.
- [ ] Integrate merge/import and conflict outcomes into Review Center summaries and backup
      compatibility tests.

Deliver each coherent slice with focused tests, a runnable demonstration where applicable,
and a local commit. Update this checklist and the gate register after meaningful progress.

## Interfaces, data and failure behavior

Use the same financial validation and revision semantics for restore-compatible files and
future wireless batches. Separate identity alias/link operations from names; identity
links must be versioned and undoable. Preserve history; no premature compaction or promise
of unlimited retention. Non-destructive import is default and removing source data is a
separate explicit action.

Apply the shared verification and compatibility contract in the overview. Extend
migrations, backup/restore, revisions and privacy checks whenever this phase introduces
persisted data.

## Acceptance and verification

- [ ] G12: Reimporting the same package is idempotent; independently created similar
      records remain conservative duplicate candidates rather than being forced together
      by reference alone.
- [ ] Concurrent amount, split, category and identity changes either merge validly or
      retain reviewable branches with both histories.
- [ ] Undo of an import followed by a dependent edit previews consequences and preserves
      or explicitly resolves that work.
- [ ] Reimport/replay does not resurrect deleted or undone data; causal dependencies and
      missing parents have tested handling.
- [ ] Corrupt, incompatible, oversized and interrupted imports leave live records intact.
- [ ] Model/state-machine tests exercise ordering, repeated application, correction, undo
      and multiple imports; UI tests cover conflict/undo previews.

Record commands, results, fixture/dataset versions and device evidence below. A blocked or
unexecuted check is not a pass. Fix material failures before closing this phase's gate.

## Human actions

End: offer a synthetic conflicting-import/undo demonstration; no new milestone approval
required for routine behavior. Product changes to undo/retention guarantees require
agreement before destructive implementation.

## Decisions to resolve during implementation

Document merge compatibility, conflict resolution, causal dependency and undo-retention
policies before dependent code. Reject unsupported cases safely rather than flattening
history. Do not pick a transport to decide merge semantics.

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
