# Phase 00 — Verify the foundation and phone delivery path

**Status:** Complete. G00 closed on 2 November 2026 with toolchain evidence and
user-reported physical-phone installation and launch.

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

- [x] Recheck the existing tooling-foundation blockers; install pinned prerequisites
      through mise and repair configuration only where evidence requires it.
- [x] Run formatting checks, lint, desktop-hosted tests and Android/desktop builds; record
      actual task coverage and close the old plan only with fresh evidence.
- [x] Establish Android execution appropriate to this project through the documented
      physical-device launch task; shared tests run independently of a device. Emulator
      and instrumentation coverage remain explicitly separate (see decisions below).
- [x] Prepare an APK, installation/update instructions and a signing-key custody procedure
      outside Git. Keep a consistent identity for test updates.
- [x] Prepare a fictional-data device smoke-test checklist and record the reference device
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

- [x] G00: Pinned-tool checks pass: `mise run format:check`, `mise run lint`,
      `xvfb-run -a mise run test` where Linux needs a display, and `mise run build`.
- [x] The APK can be reproduced; the install/update procedure specifies application
      identity and signing continuity.
- [x] Test documentation distinguishes common/desktop, Android integration and
      physical-device coverage; unavailable checks are not marked passed.
- [x] Record an emulator launch or equivalent Android execution check. Prepare the
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

Use desktop-hosted shared tests for routine development and the physical phone for Android
execution. The user confirmed setup, installation and launch on 2 November 2026.
`mise run launch:android SERIAL` targets an explicitly selected device. A local emulator
is optional and deferred given limited host memory; it is not a prerequisite for shared
tests. There is no instrumented suite yet; add Android integration tests with the platform
behavior they exercise. Signing continuity and custody are documented in the delivery
guide. No signing material enters logs or plans.

Record the decision, rationale and validation before its dependent slice begins. Routine
implementation choices belong to the implementing agent; material product-scope or privacy
changes require user agreement. Add durable architecture decisions where needed.

## Completion evidence and local commits

- 2026-11-02, baseline `b2fac6a`: `mise run format:check` passed, including Kotlin, shell,
  TOML and documentation checks.
- Prepared [Android delivery](../../docs/android-delivery.md): application identity,
  artifact location, debug signing continuity, private key custody, safe install/update,
  emulator execution procedure and reference-phone smoke checklist. APK assembly passed;
  the later user-reported Android launch closes the execution requirement.
- Missing prerequisites: no emulator or Xvfb installed; the host has a graphical display,
  `mise run test` passed using the existing display (the desktop title smoke test).
  Unattended sudo is unavailable.
- `mise run lint` passed: Markdown, shell, workflows, detekt and Android debug lint.
  Shared Android UI and launcher compilation completed as dependencies.
- Scoped Markdown lint passed for the delivery guide and updated documents.
- Earlier build/test attempts cancelled during resource contention are not passes; the
  sequential desktop test and build reruns passed. The host has limited RAM and exhausted
  swap under overlapping builds; avoid concurrent Gradle invocations.
- `mise run build` passed: Android debug APK assembly and desktop JAR compilation.
  Artifact: `androidApp/build/outputs/apk/debug/androidApp-debug.apk` (untracked build
  output). Build emitted a native-library stripping warning and retained that library.
- SDK `apksigner verify` passed for the generated APK. `adb devices` returned no attached
  targets; no signing key material was read or committed.
- No application feature code changed; all checks exercise the baseline placeholder.
- Final `mise run format` passed across Kotlin, documentation, shell and TOML. An earlier
  cancelled formatting attempt is superseded by this complete run.
- Closure recheck at `2cdbd52`: `mise run check` passed (format checks, full lint, 27
  setup regression tests, desktop test task and Android/desktop builds). Gradle reused
  up-to-date test/build results where applicable; this was not a clean rebuild.
- 2026-11-02: the user reported successful setup, installation and application launch on
  their phone. This satisfies the equivalent Android execution check using the reference
  phone context above. The exact installed revision was not supplied; the current delivery
  tooling revision is `2cdbd52`. This is user-reported execution, not an agent-observed
  device test. No private device data was collected.
- Same-signer updates, accessibility, rotation and wider supported-API behavior have not
  been reported as tested. The phase requires an update procedure and signing continuity
  guidance, which are present; runtime upgrade/data preservation needs tests as persisted
  features arrive. The earlier handoff overextended the Phase 00 gate by demanding an
  update demonstration before closure.
- Gate result: G00 closed. Phase 01 may begin. H01 (useful ledger acceptance), H02
  (real-data readiness) and H03 (beta acceptance) remain open in their owning phases.
- Evidence commits: `df0e0ea` (delivery), `8cf6db2` (tooling), `5c0a49b` (roadmap),
  `d76cbd3` (setup), `2cdbd52` (device launch). The user authorized publication with this
  phase closure; publication outcome is recorded in the handoff and Git history.
- Handoff: use shared tests while the phone is disconnected; schedule Android platform
  checks when an execution target is available. Do not infer Android integration,
  financial correctness or real-data readiness from the placeholder launch.

## New additions

None yet. Record date, request, rationale, acceptance impact and affected phases/gates.

## Deviations from the original plan

None yet. Record original expectation, replacement, reason, authorization where needed,
and verification. Update downstream documents before starting affected work.

## Learning notes

None yet. Record discoveries, failed assumptions, device findings and follow-up
experiments without private data or transient operational logs.
