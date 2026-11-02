# Agent Guidelines

## Project and responsibilities

Zendooh is a Kotlin Multiplatform and Compose Multiplatform project for personal financial
management. Prioritize useful, verifiable end-to-end changes, maintainable shared
foundations, and careful handling of financial data.

- Keep `AGENTS.md` focused on durable repository-wide instructions and conventions. Record
  temporary findings, project progress, and current implementation details in tracked
  plans or appropriate project documentation instead.
- Own implementation, debugging, relevant verification, and documentation for the
  requested task.
- Inspect the current code, build configuration, tests, and relevant documentation before
  proposing architectural changes. Distinguish intended behavior from implemented
  behavior; do not treat proposals as settled requirements.
- For review tasks, inspect and run non-mutating checks. Modify files only when fixes or
  implementation are requested.
- Do not use sub-agents unless the user explicitly requests them. If authorized, assign
  bounded scopes, prevent overlapping writes, and review the combined result.
- Resolve routine implementation choices using repository conventions. Ask about material
  product ambiguities, irreversible actions, or incompatible requirements; continue
  independent work where possible.

## Safe checkout and Git workflow

- Work in the current repository checkout by default. Worktrees are optional isolation
  tools, not a prerequisite or contributor requirement.
- Before editing, inspect working-tree status and the current branch, HEAD, and upstream
  where available.
- Preserve existing staged, unstaged, and untracked work. Never overwrite, reset, stash,
  delete, or move unrelated changes without explicit authorization.
- Keep edits and Git operations scoped to the task. Do not create branches, commits,
  pushes, or pull requests merely to satisfy a workflow convention; follow the user's
  requested delivery workflow.
- Use Conventional Commits with `type(scope): description`; the scope is optional. Group
  changes into small, coherent commits, each covering an independently explainable change.
  Write messages that document what changed and why so feature additions and changes
  remain traceable in Git history.
- Do not force-push, rewrite shared history, remove branches or worktrees, or perform
  destructive cleanup without explicit authorization.
- Refresh remote state when an operation depends on it. Do not assume branch names,
  integration targets, or recorded commit IDs remain current.
- Keep repository instructions and scripts portable. Exclude machine-specific paths,
  private workspace details, secrets, and scratch notes from commits and external
  collaboration.

## Planning and incremental delivery

For substantial features, complex fixes, refactors, and multi-step reviews, keep a tracked
plan in `plans/YYYY-MM-DD-<task>/`. Small, straightforward changes do not require a plan
file.

- Use `plan.md` for standard tasks. For multi-file plans, include an `overview.md` linking
  the phases and summarizing dependencies, progress, and cross-cutting risks.
- Record the goal, context, constraints, concrete implementation steps, acceptance checks,
  and unresolved decisions. Track progress with checkboxes and record material discoveries
  or deviations as work proceeds.
- Deliver and verify small slices. Update progress after each meaningful step rather than
  reconstructing it at the end.
- Retain useful completed plans and decisions as project history. Keep temporary logs,
  generated artifacts, private data, and disposable scratch files out of tracked plans.
- Record material architectural decisions, including schema, protocol, security, and
  compatibility tradeoffs, in durable project documentation. Keep documentation aligned
  with implemented behavior.

## Kotlin Multiplatform and Compose

- Follow established modules and source-set conventions. Keep reusable domain logic and
  compatible UI in shared code; isolate platform APIs and capabilities behind narrow
  platform boundaries. Do not assume platforms have equivalent permissions or ingestion
  capabilities.
- Prefer existing libraries and patterns. Explain material dependency or architecture
  changes and check their compatibility with affected targets.
- Keep financial rules, parsing, persistence, and state transformations testable
  independently of composables and platform services.
- Use explicit UI state and clear event handling. Keep side effects out of composition
  bodies; use appropriate effect APIs and keys. Respect lifecycle, structured concurrency,
  cancellation, and dispatcher requirements. Avoid blocking the UI thread or swallowing
  coroutine cancellation.
- Follow existing theme and component conventions. Consider accessibility semantics, text
  scaling, light/dark appearance, and loading, empty, and error states for affected UI.
- Use exact monetary representations with explicit currency and rounding rules. Do not use
  binary floating-point arithmetic for financial amounts. Make time-zone and date
  assumptions explicit when they affect financial behavior.
- Keep schema changes and migrations compatible with persisted data. Verify upgrade
  behavior and document recovery or rollback limitations where relevant.

## Tooling and verification

Use mise to install pinned tools and run the repository's quality tasks. Gradle owns
Kotlin builds and analysis; use the wrapper rather than a system Gradle installation.
Inspect task definitions, CI, and `CONTRIBUTING.md` for current task behavior and target
coverage before choosing verification commands.

- Run `mise run format` to format implementation changes and review the diff. For reviews,
  use `mise run format:check`, which does not rewrite files.
- Run `mise run lint` for lint checks, `mise run test` for tests, and `mise run build` for
  builds. Use `mise run check` for aggregate verification after inspecting its coverage.
- Use the configured tools: ktlint and detekt for Kotlin, Android lint, Prettier and
  markdownlint for Markdown, Prettier for JSON/YAML, Taplo for TOML, shfmt and ShellCheck
  for shell, and actionlint for workflows. Authored shell scripts must use a `.sh`
  extension.
- Use focused language tasks for narrow verification; discover them with `mise tasks`.
- Keep tool versions pinned in mise, the Gradle wrapper, and the version catalog. Do not
  duplicate specific version numbers in documentation; let the relevant configuration
  files own them. Do not upgrade tools incidentally or claim unavailable checks ran.
- Run the narrowest relevant tests first, then the configured checks and builds needed for
  the affected modules and targets. Run Android lint when configured and relevant. Inspect
  aggregate tasks rather than assuming `check` covers all platforms or device tests.
- Verify shared behavior through common tests where practical, and platform behavior
  through the relevant platform tests. UI changes may require Compose UI tests or
  emulator/device inspection; compilation alone does not establish correct interaction or
  appearance.
- Test meaningful behavior and regressions rather than mirroring implementation details.
  Use deterministic fixtures; add failure, boundary, and compatibility cases appropriate
  to the change.
- For affected financial behavior, cover precision and rounding, repeated imports or
  operations, invalid inputs, and persistence/migration behavior as applicable. Verify
  cancellation, interruption, and recovery when the change introduces those risks.
- Report unavailable tasks, dependencies, SDKs, devices, or host-specific targets
  accurately. Separate passed checks from blocked or unexecuted checks; do not infer
  success on one target from another.
- Do not add build tooling or dependencies solely to satisfy this document during an
  unrelated task. Identify missing baseline configuration as follow-up work unless
  configuration is within the requested scope.

## Privacy and data integrity

- Use fictional, deterministic financial data in tests, screenshots, documentation, and
  agent-visible reproductions. Keep private financial messages, account identifiers,
  credentials, and personal datasets outside agent access and repository history.
- Do not expose sensitive values through logs, analytics, crash reports, exports,
  temporary artifacts, or test failures. Inspect fixtures and diffs for identifying
  combinations as well as obvious secrets.
- Preserve provenance and distinguish observed facts, inferred values, and user
  corrections. Do not turn uncertainty or successful parsing into an unsupported claim of
  independent verification.
- Validate untrusted input at boundaries. Keep destructive data operations explicit and
  protect existing records from partial failures. Use established cryptographic libraries
  rather than custom cryptography when security work is in scope.

## Reviews, pull requests, and handoff

- Follow repository contribution guidance and PR templates when present. Keep descriptions
  focused on the concrete problem, resulting behavior, relevant design tradeoffs, and
  verification evidence.
- Report actionable review findings with a concrete trigger, impact, supporting code or
  runtime evidence, and a recommended correction. Anchor findings to relevant changed
  lines where possible. Distinguish demonstrated defects from questions or optional
  improvements.
- Do not publish reviews, comments, or other messages to external services without
  authorization. Keep external communication free of local paths, internal scratch
  artifacts, and agent operational details.
- Before finishing, inspect the final diff and working-tree status for accidental changes,
  sensitive data, and scope drift.
- Summarize what changed, affected files, checks actually run and their results, and any
  blockers or remaining human actions. Mention Git operations when performed. Keep the
  handoff proportional to the task; never present unverified behavior as tested.
