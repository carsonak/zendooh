# Contributing

## Development environment

Run the setup script from a checkout:

```sh
bash scripts/setup.sh
```

Supported hosts are Linux/WSL x86-64 and Intel/Apple Silicon macOS. Setup installs mise
when missing, the pinned JDK and quality tools, Android command-line tools and SDK
packages, and Gradle through the repository wrapper. It installs neither Android Studio
nor an emulator. Use the wrapper and the mise-managed JDK in an IDE; do not install system
Gradle. Subsequent setup can also use `mise run setup`.

### Host prerequisites

Setup never invokes sudo or a system package manager. It exits with a diagnostic until
required host prerequisites are available:

- Bash, Python 3.9 or newer (standard library only), curl, Git, unzip, and tar.
- Working HTTPS trust/CA certificates and access to the tool download repositories.
- Linux: glibc, libstdc++, zlib, X11, Xext, Xi, Xrender, Xtst, Fontconfig, FreeType, and
  OpenGL runtime libraries. These support the JDK and Compose desktop runtime.
- macOS: working system runtime libraries; ensure Git and Python are usable, including
  completing any Command Line Tools installation prompts before running setup.

For Debian/Ubuntu, an administrator can install
`ca-certificates curl git unzip tar python3 libc6 libstdc++6 zlib1g libx11-6 libxext6 libxi6 libxrender1 libxtst6 libfontconfig1 libfreetype6 libgl1 fonts-dejavu-core`.
Other distributions use different package names. Linux desktop UI tests also need a
display: for headless execution, install `xvfb` and `xauth` and use
`xvfb-run -a mise run check`. Display availability is not required for SDK setup.

### Tool locations and shell activation

Tools live in mise's user data directory outside the checkout, reusable across workspaces;
Gradle distributions live in the user Gradle cache. Existing mise versions meeting the
configured minimum are retained. An older mise must be upgraded manually. Mise uses
calendar versions; the minimum permits newer releases without promising future
compatibility. A missing mise is bootstrapped from the latest stable release and verified
against its release checksum before installation to `~/.local/bin/mise`.

The script cannot change its parent shell. Add `~/.local/bin` to PATH if needed, then
activate mise in your shell yourself:

```sh
export PATH="$HOME/.local/bin:$PATH"
eval "$(mise activate bash)"
# For zsh, use: eval "$(mise activate zsh)"
```

Alternatively, use `~/.local/bin/mise exec -- ./gradlew tasks` without shell activation
(or the path to an existing mise installation). Activation or `mise exec` selects the same
SDK for Gradle, `sdkmanager`, `adb`, and `apksigner`. Build-tools selection is explicit,
so installing another build-tools version does not change `apksigner`. The package list
and selected build-tools version are declared in `mise.toml`. Google's `platform-tools`
package follows the available stable release, so Android installations are not bit-for-bit
reproducible.

### SDK conflicts, licenses, and reruns

A new checkout does not need `local.properties`: mise provides `ANDROID_HOME` and
`ANDROID_SDK_ROOT`. Unset inherited values pointing to another SDK before setup. The
script does not remove or modify system-installed tools or old SDK directories.

If an existing `local.properties` points to another SDK, setup prompts to back it up and
replace only `sdk.dir`. The default answer is no. Every repair creates a unique ignored
`local.properties.backup-*` beside the original and preserves other properties. Without a
terminal, pass `--repair-sdk-config` explicitly or resolve the conflict manually. Backups
may contain private local settings; do not commit or share them.

License acceptance is interactive by default. For unattended setup, explicitly accept
Google's Android SDK licenses with:

```sh
bash scripts/setup.sh --accept-licenses --repair-sdk-config
```

Omit the repair flag when no configuration repair is intended. Existing accepted licenses
permit unattended reruns without the license flag. Completed installations are reused;
failed downloads/installations exit without reporting success. Correct the reported
problem and rerun. `bash scripts/setup.sh --help` lists supported flags.

Connecting a physical device may require administrator-installed Linux udev rules, USB
group membership, or WSL USB forwarding. These are separate from installing adb and do not
block setup. Enable USB debugging and authorize the selected development machine on the
device. No device connection is required for setup verification.

## Run and build

```sh
mise run run:desktop
mise run build
```

For Android, start an API 24 or newer emulator or connect a device, then run:

```sh
mise exec -- ./gradlew :androidApp:installDebug
mise run launch:android SERIAL
```

Replace `SERIAL` with the intended device serial from `adb devices`. The launch task opens
the installed app; it does not build or install an APK. You can also open Zendooh from the
device launcher. The initial compile/target SDK is 36. `composeApp` owns shared Compose UI
and the desktop launcher; `androidApp` owns the Android launcher. iOS is not configured.
See [Android delivery](docs/android-delivery.md) for signing-key custody, safe updates,
emulator execution and the fictional-data phone checklist.

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
