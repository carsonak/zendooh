# Contributing

## Development environment

Install mise, Git, and Android Studio or the Android command-line SDK tools. Run
`mise trust` and `mise install` from the checkout root to install pinned tools. Use the
Gradle wrapper and JDK 21 in your IDE; do not use system Gradle.

Accept Android SDK licenses and install the required packages:

```sh
sdkmanager --licenses
sdkmanager "platform-tools" "platforms;android-36" "build-tools;35.0.0" "build-tools;36.0.0"
```

Set `ANDROID_HOME` or put `sdk.dir` in an untracked `local.properties`. Keep the SDK in a
durable directory outside the repository. Linux desktop UI tests require a display;
install Xvfb for headless execution. Windows development can use WSL with these Bash
tasks.

## Run and build

```sh
mise run run:desktop
mise run build
```

For Android, start an API 24 or newer emulator or connect a device, then run:

```sh
mise exec -- ./gradlew :androidApp:installDebug
```

Open Zendooh from the device launcher. The initial compile/target SDK is 36. `composeApp`
owns shared Compose UI and the desktop launcher; `androidApp` owns the Android launcher.
iOS is not configured.

## Checks and tests

```sh
mise run format
mise run format:check
mise run lint
mise run test
mise run build
mise run check
```

`format` rewrites files; all check tasks are read-only. `check` runs formatting checks,
linters, desktop-hosted shared UI tests, Android debug assembly, and desktop compilation.
For headless Linux use `xvfb-run -a mise run check`. No emulator is needed for these
initial checks; device behavior still requires separate verification.

Use `mise tasks` for focused tasks. Kotlin uses ktlint and detekt; Markdown uses Prettier
and markdownlint; shell scripts use shfmt and ShellCheck; TOML uses Taplo; workflows use
actionlint. Prettier also formats JSON/YAML. Author shell scripts with a `.sh` extension.
Generated code and Gradle launchers are excluded. Tool versions live in `mise.toml`, the
Gradle wrapper, and `gradle/libs.versions.toml`.

## Conventions

Follow EditorConfig and existing Kotlin/source-set conventions. Keep reusable logic in
shared code and platform APIs behind platform boundaries. Use structured concurrency,
explicit UI state, accessible Compose components, and deterministic synthetic fixtures.
Never commit private financial data, credentials, machine-specific paths, or signing keys.
Use exact monetary representations and explicit currency/rounding rules.

Keep changes focused and document meaningful architectural decisions. Substantial work
uses tracked plans under `plans/`; retain useful completed plans. Add behavior-focused
regression tests and relevant migration checks. Report checks actually run and any limits.
Reviews use check-only commands. Follow [AGENTS.md](AGENTS.md) for agent workflow rules.

Before committing, inspect the staged diff and run the relevant checks. GitHub Actions
runs the same aggregate command. Personal IDE settings, SDK configuration, caches, and
build outputs must remain untracked.
