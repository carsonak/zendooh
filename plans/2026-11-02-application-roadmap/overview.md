# Zendooh application roadmap

**Agreed:** 2 November 2026. **Implementation status:** Phase 00 complete (G00 closed);
phase 01 is ready to start. All later technical and human gates remain open.

This bundle translates [ZENDOOH.md](../../ZENDOOH.md) into incremental, verifiable work.
The specification describes product intent; these documents schedule its implementation.
No application feature or implementation gate is complete merely because its plan exists.

## Goal and beta boundary

Deliver an offline Android application that can be installed on a phone, including a
consistently signed development build when necessary. Produce useful feedback through
small runnable slices, not one large implementation followed by a final demonstration.

The agreed beta includes:

- Personal/business profiles, multiple accounts and SIMs, cash, M-Pesa and Airtel Money.
- Fuliza and M-Shwari savings/credit movements, repayments, explicit charges and debt-cost
  forecasts, with gaps in evidence visible rather than invented.
- Historical/incremental SMS acquisition, controlled input fallback, adaptive parsing,
  evidence-gated automation, saved corrections and a Review Center.
- Exact financial records, allocations, typed relationships and custom descriptive links.
- Categories, daily reports, period comparisons, monthly budgets, confirmed recurring
  commitments, optional reminders and unusual-spending suggestions.
- Encrypted storage, tested upgrades, portable full-workspace recovery and scheduled
  backups.

Wireless sync, merge into existing workspaces, hosted rule downloads, iOS and investment
forecasting follow beta. [Future directions](future-directions.md) retains these and other
specification promises without silently making them prerequisites for the first phone
build.

## Current state and test context

The repository has KMP/Compose Android and desktop launchers and a placeholder title test.
There is no implemented finance, persistence, parser or sync layer. The existing
[tooling-foundation plan](../2026-11-02-tooling-foundation/plan.md) now records passing
verification. [Phase 00](00-foundation.md) records the toolchain evidence and the
user-reported phone installation/launch that closed G00 on 2 November 2026.

The current `mise run test` invokes setup regression and desktop-hosted tests, and the
build assembles Android and compiles desktop. These do not establish SMS permissions,
encryption integration, background execution or device behavior. Update task coverage as
modules/tests grow.

Reference device: **Redmi 15C, Xiaomi HyperOS 3.0, Android 16, dual SIM**. Test
installation, upgrades, receiving-SIM mapping, missing/ambiguous metadata, permission
revocation, background constraints and recovery there. A second Android phone can be
obtained later; it is required for final wireless-device acceptance, not for beta
development.

Keep the current minimum SDK unless testing justifies an agreed change. One Android 16
phone does not establish compatibility across all supported Android versions. Desktop
remains a shared test/development host; iOS is not currently configured.

## Phase index and gate register

All gates start **open**. Here, “closed” means satisfied with recorded evidence, not
cancelled. Store detailed evidence in the owning phase and summarize the result here.
Record the implementation revision, test/fixture versions, date and any accepted
limitations.

| Phase                              | Deliverable                                              | Required entry gates                   | Exit gates                  | Status      |
| ---------------------------------- | -------------------------------------------------------- | -------------------------------------- | --------------------------- | ----------- |
| [00](00-foundation.md)             | Verified toolchain and Android delivery                  | Existing checkout                      | G00                         | Complete    |
| [01](01-persistence.md)            | Encrypted persistence compatibility and shared contracts | G00                                    | G01                         | Not started |
| [02](02-manual-ledger.md)          | Useful manual ledger and saved edits                     | G01                                    | G02; H01 phone acceptance   | Not started |
| [03](03-protection-recovery.md)    | Protection, upgrades and portable replacement restore    | G02; H01 before H02                    | G03; H02 real-data approval | Not started |
| [04](04-profiles-relationships.md) | Profiles, allocations and relationships                  | G03                                    | G04                         | Not started |
| [05](05-acquisition-review.md)     | SMS scanning, mappings and review pipeline               | G04                                    | G05                         | Not started |
| [06](06-adaptive-learning.md)      | Teaching, evaluation, rollback and automation            | G05                                    | G06                         | Not started |
| [07](07-provider-coverage.md)      | Complete beta provider/financial coverage                | G06, G04                               | G07                         | Not started |
| [08](08-debt-forecasts.md)         | Personal-rule debt forecasts                             | G07                                    | G08                         | Not started |
| [09](09-reports-budgets.md)        | Categories, reports and budgets                          | G07, G04; G08 for forecast integration | G09                         | Not started |
| [10](10-recurring-backups.md)      | Recurrence, quiet automation and scheduled backups       | G09, G03                               | G10                         | Not started |
| [11](11-beta-acceptance.md)        | Hardened multi-user beta                                 | G08–G10, H01, H02                      | G11; H03 beta acceptance    | Not started |
| [12](12-portable-merge.md)         | Idempotent imports, conflicts and dependency-aware undo  | G11, H03                               | G12                         | Not started |
| [13](13-scoped-sync.md)            | Authorized subsets, pairing and resumable wireless sync  | G12; G13S before wireless exchange     | G13S; G13                   | Not started |

The normal path is 00 → 01 → 02 → 03 → 04 → 05 → 06 → 07. After G07, forecasting and the
independent parts of reports may proceed in either order; beta requires both. This is
permission for independent work, not authorization to spawn sub-agents. Transitive
prerequisites apply. If a later change invalidates a closed gate, reopen its affected
evidence and revalidate dependents before claiming completion.

Human gates are distinct from technical gates and Git approval:

- **H01:** First useful fictional-data phone journey after G02.
- **H02:** Real-data readiness after H01 and G03. Applies only to technically verified
  workflows; new ingestion/learning features must pass their own tests before real use.
- **H03:** Beta acceptance after G11 evidence is complete.
- **Push approval:** Implementation commits stay local until explicitly approved.
  Accepting a milestone does not automatically authorize pushing or distributing its
  build.

An open gate blocks dependent implementation/usage, not read-only research, synthetic
experiments or independent work. Agents finish all available checks and prepare the build,
expected outcomes and one grouped checklist before asking for a human action. Device-only
checks should be scheduled at the end; missing hardware/setup belongs at the beginning. Do
not substitute elapsed time or silence for approval.

## Decisions and defaults

- Use KMP/shared Compose and narrow platform boundaries. Reuse existing patterns and
  validate storage/encryption candidates rather than treating library names as
  requirements.
- Financial arithmetic is exact and currency-explicit. Beta journeys emphasize KES; no
  silent mixed-currency sums or speculative conversion. Preserve instants and known source
  offsets; reporting starts with a configurable Africa/Nairobi workspace timezone.
- Real financial data and recovery secrets remain outside coding-agent access. All
  committed fixtures, screenshots and examples are fictional and deterministic.
- Raw messages are transient by default. An encrypted teaching cache may retain selected
  task inputs until teaching/evaluation completes or seven days elapse, whichever is
  first. Exclude it from backups/sync, allow manual clearing, enforce expiry on
  access/startup, and do not indefinitely renew retention. Do not promise physical flash
  erasure.
- Retain structured corrections and privacy-reviewed templates separately. Source loss can
  limit reevaluation without invalidating a structured transaction. Never recreate
  original text from inference or retain it disguised as tokenized features.
- Automate parsing only after independent evaluation and financial validation. Numerical
  promotion rules are an implementation experiment with documented criteria and evidence;
  insufficient evidence leaves the family in review. Message volume alone is not
  confidence.
- Separate movements, allocations and relationships. Typed financial links have tested
  semantics; custom descriptive labels do not alter accounting. Dedicated reimbursement
  balances and formal owner-contribution accounting are deferred, not implicitly solved.
- Forecasts use explicit versioned personal defaults and official-source links. No hosted
  rule feed, scraper or in-app rule download is required for beta. Later optional
  downloads are user-initiated and must not overwrite personal defaults.
- Early recovery replaces a workspace with explicit confirmation. Merge into an existing
  workspace and selective exports wait for the merge/authorization phases.
- Source deletion does not automatically delete transactions. Local learning-forget
  controls must describe their effects; replica/backup forgetting and physical erasure
  have limits.
- No history compaction until retention/undo guarantees are deliberately defined. No cloud
  inference, financial telemetry or payment initiation is part of this roadmap.

## Execution and agent discretion

Read the specification, this overview, the owning phase and its prerequisite evidence at
start. Inspect the current branch, worktree and actual implementation before changing it.
Do not overwrite unrelated work or treat this initial baseline as permanently current.

Each phase specifies a behavioral contract, not a mandatory class hierarchy or algorithm.
Agents may select schemas, libraries, modules and methods suited to the actual codebase.
Prefer replaceable boundaries around finance, persistence/revisions, parsing/learning,
acquisition, forecasting, presentation, cryptography and transport. Do not create one
module per concept unless useful, and do not build all future functionality in advance.

Before an irreversible or costly design choice, record the decision, alternatives,
evidence, compatibility and recovery implications in durable architecture documentation.
An unresolved technical choice is assigned to its phase and must close before dependent
implementation; it is not permission to skip an invariant. Material product-scope changes,
weakened privacy or incompatible behavior require user agreement. Routine choices do not.

Use focused local commits for coherent features, fixes and prerequisites with relevant
tests and documentation. Do not combine unrelated changes or create empty commits to fill
a plan. Record implementation commit references at handoff. Preserve signing keys and
private configuration outside Git. Push only when explicitly authorized for the relevant
changes; the current authorization covers this planning bundle and its specification
alignment.

## Shared verification and compatibility contract

Every phase must apply the relevant parts of this contract, including when not repeated in
its acceptance list:

- Start with focused deterministic behavior tests, then the affected configured checks.
  Use common tests for financial logic and Android tests/device scripts for platform
  behavior.
- Cover exact arithmetic/rounding, invalid and boundary inputs, repeated operations,
  correction precedence and persistence/migration where affected.
- Inject cancellation, process interruption and partial failures where the phase
  introduces them. Validate untrusted inputs with bounded size, work and memory.
- Treat canonical records as authoritative. Derived views, report caches and learned
  models must have a documented rebuild or recovery path.
- New persisted structures extend upgrade and backup/restore tests before the phase
  closes. Preserve IDs/history/provenance; never use destructive migration as a routine
  repair. Document supported schema/container versions and safe rejection/downgrade
  behavior.
- Check privacy across logs, notifications, caches, exports, metadata and learned
  features. Redacting UI alone is not a privacy guarantee. Record threat-model limits
  honestly.
- Test relevant UI interaction, accessibility, text scaling, light/dark and
  loading/empty/error states. Compilation alone does not prove a screen works.
- Run `mise run format` for implementation changes and inspect the diff. Run focused
  tests, `mise run format:check`, `mise run lint`, `mise run test` and `mise run build` as
  appropriate to affected code; use Xvfb on headless Linux. Add new test targets to
  aggregates deliberately.
- For documentation-only work, use scoped Prettier/Markdown checks and link/contract
  checks; do not claim application tests ran. Never mark unavailable checks passed.

Each phase contains progress, evidence/commit handoff, new additions, deviations and
learning notes. Update them after meaningful slices. Record a change's affected downstream
gates and update dependents before beginning altered work. Keep raw logs, private examples
and machine-specific setup details out of tracked plans.

## Planning-bundle progress and verification

- [x] Inspect specification, source, tooling, existing plans and repository state.
- [x] Agree beta scope, learning retention, relationship behavior, forecasting and human
      gates.
- [x] Record the reference phone and later second-device availability.
- [x] Draft linked phase documents, future work and requirement/acceptance ownership.
- [x] Verify consistency, links, Markdown formatting and final diff.
- [x] Prepare the scoped planning bundle for the authorized commit and push.

Planning verification passed: `mise run format:check:docs`, `mise run lint:markdown`,
`git diff --check`, and a local structural audit of 19 changed/new documents, 106 relative
links, all 14 phase contracts and gate identifiers. The audit also confirmed that no
implementation checklist was prematurely marked complete. Commit/publication results are
recorded in Git history and the delivery handoff, not as implementation gate evidence.

Application builds/tests were not run for the original planning-only change. Subsequent
implementation evidence is recorded in phase 00; G00 is now closed.

## New additions

None beyond the agreed scope above. Future entries must include date, rationale,
acceptance impact, owner phase and downstream gates.

## Deviations from the original plan

None. The detailed documents clarify operational boundaries without changing the agreed
beta: hosting is deferred, real-data use is gated, and later sync remains an intended
feature.

## Learning notes

- Existing aggregate tests exercise desktop-hosted code; they do not prove Android
  behavior.
- The tooling-foundation plan still records incomplete verification. Recheck it early.
- Transient evidence, adaptive regression testing and portable recovery need deliberately
  different retention policies. Cache expiry must not depend on timely background
  execution.
- Relationship labels alone cannot determine accounting or independently verify an event.
