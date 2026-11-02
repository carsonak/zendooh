# Tooling and KMP foundation

## Goal

Establish Android and desktop Compose entry points and pinned mise formatting, linting,
testing, and build tasks shared with CI. No financial features or release publishing.

## Progress

- [x] Inspect repository, preserve existing work, and confirm target/tooling choices.
- [x] Add build foundation and quality-tool configuration.
- [x] Add CI and setup documentation.
- [x] Format, validate failure detection, test, and build where prerequisites permit.

## Decisions and evolution

- 2026-11-02: Use mise as the task runner; Gradle owns Kotlin builds and analysis.
- Use Kotlin 2.2.21, Compose 1.9.3, AGP 8.11.1, Gradle 8.14.3, and JDK 21. This
  conservative stable combination supports the Android KMP library plugin.
- detekt 1.23.8 runs source analysis without type resolution, avoiding dependency on a
  matching compiler classpath. ktlint owns formatting; no detekt formatting ruleset.

## Acceptance

Formatting is idempotent; linters reject malformed samples; shared UI smoke tests pass;
Android lint/debug assembly and desktop compilation pass or have explicit blocker
evidence.

- 2026-11-02: Installed Android API 36, build tools 36.0.0, and platform tools locally.
  Verified official wrapper JAR checksum; build-tool downloads are still in progress.

## Delivery verification

Formatting checks passed for Kotlin, Markdown, shell, and TOML. Markdown, shell, and
workflow linters passed. Malformed non-Kotlin probes were rejected. The existing detekt
report contained zero findings. Full verification remains pending: Android lint
encountered an incomplete SDK installation, and UI tests have not completed locally. SDK
repair and CI verification must be checked before declaring the foundation fully verified.

README is a short placeholder; CONTRIBUTING contains setup, running, checks, and
conventions. Personal IDE files are excluded from Git. Obsolete reference documents were
removed.

## Fresh verification on 2 November 2026

Roadmap phase 00 rechecked baseline `b2fac6a`: `mise run format:check`, `mise run lint`,
`mise run test` and `mise run build` all passed. Tests used the existing graphical
display. Android lint, shared/launcher compilation, debug APK assembly and desktop JAR
compilation now succeed. Earlier incomplete SDK evidence above is retained as history. No
tool upgrade or application source change was required. This closes the old tooling
verification work; Android runtime/device delivery remains an open gate in the application
roadmap.
