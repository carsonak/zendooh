# Phase 11 — Harden and accept the multi-user beta

**Status:** Not started. No implementation gate is closed by creating this document.

[Roadmap and execution contract](overview.md) · [Acceptance matrix](acceptance-matrix.md)

## Goal and boundaries

Deliver an installable, upgradable beta covering the agreed daily workflows and a
privacy-safe feedback loop. This is a local beta release gate, not public-store approval
or authorization to push implementation commits.

## Entry gates

G08, G09, G10, H01 and H02; their transitive technical prerequisites must remain valid.

Verify gate evidence against the current implementation before starting dependent work.
Investigation and independent work may proceed while a gate is pending; do not claim a
phase complete or use real data without the applicable technical and human gates.

## Implementation slices

- [ ] Audit the acceptance matrix against implementation and test evidence; resolve
      missing core provider/report/forecast workflows.
- [ ] Run end-to-end journeys across restart, process death, permission changes,
      migration, backup and fresh-install restore.
- [ ] Measure scan/report/revision performance with progressively larger fictional
      fixtures; record datasets, memory, timings and responsiveness on representative
      hardware.
- [ ] Exercise the Redmi 15C dual-SIM device and additional devices/users when available,
      keeping private financial records outside agent access.
- [ ] Prepare signed or consistently signed development APKs, update/recovery
      instructions, known limitations and a synthetic/aggregate feedback process.
- [ ] Triage and fix critical integrity/privacy/data-loss issues; prepare one H03
      acceptance packet.

Deliver each coherent slice with focused tests, a runnable demonstration where applicable,
and a local commit. Update this checklist and the gate register after meaningful progress.

## Interfaces, data and failure behavior

Avoid adding unrelated features during hardening. Additional requirements enter the
additions log with impact on gates. Do not collect raw messages through telemetry,
screenshots or crash reports. Keep debug-build limits explicit and retain signing
continuity without committing keys.

Apply the shared verification and compatibility contract in the overview. Extend
migrations, backup/restore, revisions and privacy checks whenever this phase introduces
persisted data.

## Acceptance and verification

- [ ] G11: All beta requirement rows have passing evidence or an explicitly approved scope
      amendment; no critical financial-integrity, privacy or data-loss issue is
      unresolved.
- [ ] Full fictional journeys cover manual entry, scan/import, teach/correct/reparse,
      splits/relationships, debt accounting/forecasting, budgets/reports and recovery.
- [ ] A prior supported installation upgrades without losing IDs, history or corrections;
      unsupported versions fail safely and recovery guidance is accurate.
- [ ] Performance budgets are set from measured baseline/user workflow before final tuning
      and met by the agreed stress suite; 10k–100k SMS remains a proposed measurement
      range, not an invented achieved result.
- [ ] Device evidence includes permissions, dual-SIM ambiguity, accessibility, lifecycle
      and background limits; untested OS/device combinations are named honestly.
- [ ] H03: User accepts the prepared beta and its documented limitations after G11
      evidence is complete.

Record commands, results, fixture/dataset versions and device evidence below. A blocked or
unexecuted check is not a pass. Fix material failures before closing this phase's gate.

## Human actions

End: deliver APK/version, automated results, known limitations and one short checklist of
device-only acceptance actions. Request H03 after all independent work is done. Additional
testers use their own local records; feedback uses aggregate counts or fictional
reproductions. Obtain separate approval before any external release or push not already
authorized.

## Decisions to resolve during implementation

Broader device/OS support and public distribution require separate evidence. Keep the
current minimum SDK unless compatibility testing justifies a reviewed change; one Android
16 phone does not prove all API 24+ behavior. Record unsupported combinations.

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
