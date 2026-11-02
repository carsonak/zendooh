# Phase 10 — Add recurring commitments and quiet automation

**Status:** Not started. No implementation gate is closed by creating this document.

[Roadmap and execution contract](overview.md) · [Acceptance matrix](acceptance-matrix.md)

## Goal and boundaries

Help users notice recurring obligations and budget risks without repeated interruptions,
while keeping backups current. Automatic background work is best-effort with visible
status and manual alternatives.

## Entry gates

G09 and G03.

Verify gate evidence against the current implementation before starting dependent work.
Investigation and independent work may proceed while a gate is pending; do not claim a
phase complete or use real data without the applicable technical and human gates.

## Implementation slices

- [ ] Suggest recurring commitments from history and require confirmation before treating
      them as established obligations.
- [ ] Add explainable unusual-spending suggestions and opt-in budget reminders with
      deduplication, frequency controls and quiet hours.
- [ ] Implement Balanced default autonomy and Careful/Quiet behavior without lowering
      financial validation or turning uncertainty into fact.
- [ ] Add summaries of classifications, parser changes and matches, leaving extension
      points for later merge/sync summaries.
- [ ] Add scheduled encrypted backups through a user-selected destination with persistent
      access where available, rotation and visible freshness/failures.
- [ ] Prepare device tests for Android/HyperOS background constraints, notification denial
      and destination access revocation.

Deliver each coherent slice with focused tests, a runnable demonstration where applicable,
and a local commit. Update this checklist and the gate register after meaningful progress.

## Interfaces, data and failure behavior

Separate suggestion generation, notification policy and platform scheduling. A recurring
prediction is not an observed payment. Choose a backup rotation policy that never deletes
the last valid copy before validating its successor. Show when a destination is
cloud-backed; no silent upload destination selection. Key availability during background
work must follow the documented lock/security policy.

Apply the shared verification and compatibility contract in the overview. Extend
migrations, backup/restore, revisions and privacy checks whenever this phase introduces
persisted data.

## Acceptance and verification

- [ ] G10: Unconfirmed recurrence and anomalies remain suggestions; dismissing/confirming
      them avoids repeated prompts without meaningful new evidence.
- [ ] Notification denial leaves normal workflows usable; notification contents respect
      privacy settings and lock-screen exposure.
- [ ] Quiet hours, timezone changes, repeated scheduling and process restart do not create
      duplicate reminders or ignore user controls.
- [ ] Background delays are visible as freshness limits, not silently successful backups;
      manual backup remains available.
- [ ] Failed writes, destination revocation, interruption and rotation preserve live data
      and the last known valid backup.
- [ ] A scheduled backup restores on a fresh installation without the originating device
      key; teaching caches remain excluded.
- [ ] Synthetic device checks verify background/notification behavior on the reference
      phone; no claim of guaranteed scheduling is made.

Record commands, results, fixture/dataset versions and device evidence below. A blocked or
unexecuted check is not a pass. Fix material failures before closing this phase's gate.

## Human actions

End: group remaining notification/background and document-picker checks for the user.
Agents complete scheduler simulations and failure tests before requesting phone actions;
this is evidence collection, not a new broad approval gate.

## Decisions to resolve during implementation

Document recurrence evidence, notification deduplication, default frequency and backup
rotation before enabling automation. Use conservative defaults and explain them.
Production wireless discovery is not part of this phase.

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
