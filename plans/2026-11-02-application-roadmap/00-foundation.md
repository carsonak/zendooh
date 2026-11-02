# Phase 00 — Verify the foundation and phone delivery path

**Status:** Not started. No implementation gate is closed by creating this document.

[Roadmap and execution contract](overview.md) · [Acceptance matrix](acceptance-matrix.md)

## Goal and boundaries

Produce a reproducible Android build and establish the verification baseline. No financial
features or tool upgrades are included.

## Entry gates

None; inspect the current checkout and the unfinished tooling-foundation plan.

Verify gate evidence against the current implementation before starting dependent work.
Investigation and independent work may proceed while a gate is pending; do not claim a
phase complete or use real data without the applicable technical and human gates.

## Implementation slices

- [ ] Recheck the existing tooling-foundation blockers; install pinned prerequisites
      through mise and repair configuration only where evidence requires it.
- [ ] Run formatting checks, lint, desktop-hosted tests and Android/desktop builds; record
      actual task coverage and close the old plan only with fresh evidence.
- [ ] Establish emulator/instrumented test execution appropriate to this project, without
      requiring a device for pure shared tests.
- [ ] Prepare an APK, installation/update instructions and a signing-key custody procedure
      outside Git. Keep a consistent identity for test updates.
- [ ] Prepare a fictional-data device smoke-test checklist and record the reference device
      capabilities.

Deliver each coherent slice with focused tests, a runnable demonstration where applicable,
and a local commit. Update this checklist and the gate register after meaningful progress.

## Interfaces, data and failure behavior

Keep the existing KMP/Compose targets and wrapper unless a demonstrated incompatibility
requires a documented change. Build setup is not evidence of financial correctness.
Preserve existing work and do not silently reset the old verification history.

Apply the shared verification and compatibility contract in the overview. Extend
migrations, backup/restore, revisions and privacy checks whenever this phase introduces
persisted data.

## Acceptance and verification

- [ ] G00: Pinned-tool checks pass: `mise run format:check`, `mise run lint`,
      `xvfb-run -a mise run test` where Linux needs a display, and `mise run build`.
- [ ] The APK can be reproduced; the install/update procedure specifies application
      identity and signing continuity.
- [ ] Test documentation distinguishes common/desktop, Android integration and
      physical-device coverage; unavailable checks are not marked passed.
- [ ] Record an emulator launch or equivalent Android execution check. Prepare the
      physical-phone checklist for H01 rather than blocking independent foundation work on
      phone access.

Record commands, results, fixture/dataset versions and device evidence below. A blocked or
unexecuted check is not a pass. Fix material failures before closing this phase's gate.

## Human actions

Beginning: user supplies physical-device access or performs installation when needed.
Reference device: Redmi 15C, Xiaomi HyperOS 3.0, Android 16, dual SIM. Agents finish
build/setup and a concise test script before requesting device actions. No real inbox
access.

## Decisions to resolve during implementation

Tool installation, Android test task shape and signing custody are implementation choices
to document here. No signing material enters logs or plans.

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
