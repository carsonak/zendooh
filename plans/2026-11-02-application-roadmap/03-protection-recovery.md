# Phase 03 — Close real-data protection and recovery gates

**Status:** Not started. No implementation gate is closed by creating this document.

[Roadmap and execution contract](overview.md) · [Acceptance matrix](acceptance-matrix.md)

## Goal and boundaries

Make the existing manual workflow safe enough for an explicitly approved personal-data
trial. Deliver portable full-workspace backup/replacement restore; merging into a
populated workspace is phase 12.

## Entry gates

G02. H01 must close before H02; fictional-data implementation does not need to wait for
H01.

Verify gate evidence against the current implementation before starting dependent work.
Investigation and independent work may proceed while a gate is pending; do not claim a
phase complete or use real data without the applicable technical and human gates.

## Implementation slices

- [ ] Complete local key protection, app lock/unlock policy, encrypted storage and an
      explicit threat model including debug/rooted-device limits.
- [ ] Audit ordinary logs, errors, caches, temporary files, notifications,
      clipboard/export paths, screenshots and OS backup exclusions.
- [ ] Implement versioned authenticated encrypted backup with portable recovery
      credentials independent of the original device key.
- [ ] Stage, validate and preview full replacement restore, then commit atomically;
      require explicit destructive-replacement confirmation in the app.
- [ ] Test upgrade migrations, pre-upgrade backup, backup compatibility and unsupported
      downgrade handling.
- [ ] Prepare a fresh-install recovery demonstration and H02 acceptance packet without
      exposing private credentials.

Deliver each coherent slice with focused tests, a runnable demonstration where applicable,
and a local commit. Update this checklist and the gate register after meaningful progress.

## Interfaces, data and failure behavior

Use established cryptographic libraries and versioned containers, never custom
cryptography. State backup contents, key lifecycle, exclusions and compatibility.
Full-workspace replacement and later merge share serialization/validation boundaries, but
replacement must not masquerade as merge. New later features must extend these
privacy/backup checks before receiving real data.

Apply the shared verification and compatibility contract in the overview. Extend
migrations, backup/restore, revisions and privacy checks whenever this phase introduces
persisted data.

## Acceptance and verification

- [ ] G03: Restore without the original device key preserves record/revision IDs and
      totals while creating a new installation identity.
- [ ] Wrong credentials, tampering, truncation, oversized input, unsupported versions and
      interrupted restore leave live records intact.
- [ ] An existing fictional dataset upgrades without lost corrections/history; recovery
      and downgrade limits are documented.
- [ ] Tests/inspection show private values absent from ordinary diagnostics and
      unauthorized backup/cache locations.
- [ ] Recovery is tested independently of the process that created the backup; missing
      original SMS is neutral source-unavailable information.
- [ ] H02: After H01 and G03, user approves real-data readiness using the prepared
      evidence and recovery checklist.

Record commands, results, fixture/dataset versions and device evidence below. A blocked or
unexecuted check is not a pass. Fix material failures before closing this phase's gate.

## Human actions

End: group local-unlock and portable-restore checks with explicit H02 approval. User
retains credentials outside agent access. Agents first complete synthetic restores and all
available failure tests. H02 permits only already-verified workflows; it is not blanket
approval for untested ingestion or forecasts.

## Decisions to resolve during implementation

Choose key derivation, encryption integration, lock behavior and backup format through
documented engineering decisions. Prefer portable recovery and safe failure over a
device-bound backup that cannot survive phone loss. Do not promise physical erasure from
flash or old backups.

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
