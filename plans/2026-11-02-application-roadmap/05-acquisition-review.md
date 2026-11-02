# Phase 05 — Acquire SMS safely and establish the review pipeline

**Status:** Not started. No implementation gate is closed by creating this document.

[Roadmap and execution contract](overview.md) · [Acceptance matrix](acceptance-matrix.md)

## Goal and boundaries

Scan or explicitly import messages, map them to accounts/SIMs and review candidate
records. First deliver one documented M-Pesa family, then harden scanning. Manual entry
and controlled input remain usable without SMS permission.

## Entry gates

G04 (which includes G03). H02 required before any real inbox trial.

Verify gate evidence against the current implementation before starting dependent work.
Investigation and independent work may proceed while a gate is pending; do not claim a
phase complete or use real data without the applicable technical and human gates.

## Implementation slices

- [ ] Define adapter capabilities for historical scans, controlled text/message input and
      incremental acquisition without forcing every source into a stream.
- [ ] Add contextual permissions, selected history period, resume/Refresh scanning,
      bounded batches, cancellation and progress.
- [ ] Preserve local source observations, receiving-SIM mapping and logical account IDs
      separately; add checkpoints/overlap and scoped fingerprints.
- [ ] Add candidate extraction/validation, conservative duplicate review and Review Center
      states with a narrow M-Pesa fixture family.
- [ ] Implement encrypted teaching-cache task lifecycles, manual clearing and seven-day
      maximum retention; exclude cache contents from backups/sync.
- [ ] Extend failure, privacy and restore tests; prepare the dual-SIM device checklist.

Deliver each coherent slice with focused tests, a runnable demonstration where applicable,
and a local commit. Update this checklist and the gate register after meaningful progress.

## Interfaces, data and failure behavior

Raw cache entries must be bounded to a concrete learning task; do not reset their age
indefinitely or copy the whole inbox into a training archive. Source lookup is not a
global event identity. Separate source unavailability from transaction deletion. Document
deletion/cleanup and clock-change behavior without claiming guaranteed physical erasure.
Original source access does not authorize private samples in agent tools.

Apply the shared verification and compatibility contract in the overview. Extend
migrations, backup/restore, revisions and privacy checks whenever this phase introduces
persisted data.

## Acceptance and verification

- [ ] G05: Repeated scans/imports, restored or late messages and duplicate references do
      not duplicate confirmed events or lose candidates.
- [ ] Permission denial/revocation and unreadable inputs preserve manual workflows and
      existing records.
- [ ] Process death/cancellation resumes safely; progress and checkpoints reflect
      committed work, not merely fetched messages.
- [ ] Missing/reused subscription IDs, changed slots and ambiguous same-provider SIMs
      never cause guessed permanent account assignments.
- [ ] Financial-looking unmatched input remains discoverable through minimal
      metadata/references; failed/pending/promotional input cannot silently become
      successful payments.
- [ ] Raw teaching copies become inaccessible on task completion or expiry, whichever
      comes first; access/startup cleanup enforces expiry even when background scheduling
      is delayed.
- [ ] Device tests verify permission, lifecycle and dual-SIM behavior; synthetic adapter
      tests cover unavailable metadata independently of the phone.

Record commands, results, fixture/dataset versions and device evidence below. A blocked or
unexecuted check is not a pass. Fix material failures before closing this phase's gate.

## Human actions

End: agents supply one prepared permission/SIM/lifecycle script; user runs private-inbox
checks locally after H02. Use fictional messages/emulator fixtures for automated tests.
Group any inaccessible device checks and report only aggregate or synthetic findings.

## Decisions to resolve during implementation

Document input formats, limits, financial-looking detection and deduplication behavior
before G05. Notification listeners and scheduled scans are optional later adapters, not
beta prerequisites. No always-on receiver is required.

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
