# Reproducible development setup

## Goal and constraints

Provide a user-space, command-line development setup for Linux/WSL x86-64 and Intel/Apple
Silicon macOS. Reuse mise across workspaces, retain existing tool pins, and keep Gradle
and Android tools on one consistent SDK. Never invoke sudo or install Android Studio or an
emulator. Preserve existing checkout changes.

## Steps

- [x] Implement bootstrap, prerequisites, SDK packages, and tool verification.
- [x] Implement interactive SDK configuration recovery with backups.
- [x] Add isolated regression coverage and Linux/macOS CI setup verification.
- [x] Update contributor documentation and run relevant quality checks/builds.

## Decisions

- Mise uses calendar versions: require a minimum, bootstrap latest stable only if missing,
  and leave existing installations intact.
- Pin Android command-line tools and plugin source. Platform-tools is Google's rolling
  stable package, so installations are not bit-for-bit reproducible.
- Interactive license acceptance and conflict repair are defaults; unattended acceptance
  or repair requires explicit flags.
- System Python 3 is a bootstrap prerequisite for native-library checks, checksum
  verification, and lossless handling of Java properties. No Python packages are needed.
- Device permissions and display availability are separate host responsibilities.

## Acceptance

Safe repeated setup, consistent SDK environment/command resolution, verified wrapper and
Android packages, backed-up property repair, and clear failure without partial success.
Cover failures with isolated fixtures and verify real setup in host CI.

## Progress and verification

- Real Linux/WSL setup installed the pinned Android CLI and required SDK packages. Java,
  wrapper-managed Gradle, adb, and apksigner executed successfully; all Android commands
  resolved inside the same mise-managed SDK. Existing sdk.dir was backed up before
  replacement. An unattended rerun succeeded with no acceptance/repair flags.
- Isolated tests cover bootstrap checksum verification, version compatibility,
  prerequisites, unsupported hosts, license refusal, SDK conflicts, interactive
  acceptance/refusal, property escapes/continuations, backups, failures, and reruns.
- Repository formatting and `mise run check` passed with writable user caches: formatting
  checks, Markdown/shell/workflow/Kotlin/Android lint, 27 setup regression tests, desktop
  test task, Android debug assembly, and desktop compilation. Existing desktop tests and
  build tasks reused applicable Gradle cache results.
- Android lint exposed that unqualified `mise where android-sdk` can select a different
  installed registry tool. Setup now explicitly resolves `vfox:android-sdk` and checks
  that its path equals the SDK environment before invoking sdkmanager. The regression
  fixture rejects unqualified resolution.
- Linux and both macOS architectures are configured in CI; macOS execution cannot be
  verified on the local Linux host.
