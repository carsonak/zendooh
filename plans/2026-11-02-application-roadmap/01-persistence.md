# Phase 01 — Validate persistence, protection and reusable boundaries

**Status:** Not started. No implementation gate is closed by creating this document.

[Roadmap and execution contract](overview.md) · [Acceptance matrix](acceptance-matrix.md)

## Goal and boundaries

Prove a small encrypted, migratable persisted slice before committing the application to a
storage stack. Use fictional records only; a compatibility spike is not the real-data
security gate.

## Entry gates

G00.

Verify gate evidence against the current implementation before starting dependent work.
Investigation and independent work may proceed while a gate is pending; do not claim a
phase complete or use real data without the applicable technical and human gates.

## Implementation slices

- [ ] Validate SQLite/Room with encryption on Android and the current desktop test host;
      record supported combinations and failures before selecting dependencies.
- [ ] Implement a persisted fixture journey through narrow repository and transaction
      interfaces; choose modules only where useful boundaries justify them.
- [ ] Establish random stable identities, explicit currencies, exact money and
      timestamp/source-offset handling.
- [ ] Establish versioned migrations, transactional writes and a repeatable persistence
      test harness.
- [ ] Record storage/key-management, accounting representation and migration decisions,
      alternatives and recovery limits in durable documentation.

Deliver each coherent slice with focused tests, a runnable demonstration where applicable,
and a local commit. Update this checklist and the gate register after meaningful progress.

## Interfaces, data and failure behavior

Separate finance, persistence/revisions, acquisition, interpretation and platform key
services. These are responsibility boundaries, not a requirement for one Gradle module
each. Preserve a path to stable events, evidence, postings, allocations and revisions
without implementing wireless sync. Do not let a database entity or platform SMS object
become the public domain contract.

Apply the shared verification and compatibility contract in the overview. Extend
migrations, backup/restore, revisions and privacy checks whenever this phase introduces
persisted data.

## Acceptance and verification

- [ ] G01: A fictional fixture survives restart and a representative schema upgrade with
      unchanged meaning and IDs.
- [ ] Failure injection during writes leaves the previous or committed state, never a
      partially applied financial operation.
- [ ] Wrong/missing keys fail safely; encrypted storage and relevant side files have been
      inspected without exposing secrets.
- [ ] Shared financial tests run independently of Android services and Compose; Android
      encryption integration has its own check.
- [ ] Overflow, unsupported precision and currency mismatches are rejected or handled by a
      documented exact policy.

Record commands, results, fixture/dataset versions and device evidence below. A blocked or
unexecuted check is not a pass. Fix material failures before closing this phase's gate.

## Human actions

None expected. Keep test keys disposable and fictional. If access to a platform security
facility requires a phone, prepare all other evidence first and group that check with H01.

## Decisions to resolve during implementation

Select supported libraries after compatibility testing; Room, SQLCipher and DI candidates
are starting points rather than locked dependencies. Document transaction, migration and
encryption failure semantics before downstream persistence work.

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
