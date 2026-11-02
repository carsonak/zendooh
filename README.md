# Zendooh

An offline-first personal finance project built with Kotlin Multiplatform and Compose
Multiplatform. Android and desktop currently share a placeholder screen; financial
features are not implemented yet.

See [the product specification](ZENDOOH.md) and the
[phased implementation roadmap](plans/2026-11-02-application-roadmap/overview.md) for
agreed beta scope, execution gates and acceptance criteria.

## Run locally

Set up the command-line development environment in user space:

```sh
bash scripts/setup.sh
```

Setup installs mise if missing, the pinned JDK and quality tools, Android command-line SDK
tools, and wrapper-managed Gradle. It requires host prerequisites and prompts for Android
licenses. No Android Studio or emulator is installed. See
[CONTRIBUTING.md](CONTRIBUTING.md) for prerequisites, shell activation, SDK conflict
recovery, Android execution, tests, and quality checks. After activating mise, run:

```sh
mise run run:desktop
```

## License

Licensed under the [Apache License, Version 2.0](LICENSE).
