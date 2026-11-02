#!/usr/bin/env bash
set -euo pipefail

cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.."
accept_licenses=false
repair_sdk_config=false
for arg in "$@"; do
  case "$arg" in
    --accept-licenses) accept_licenses=true ;;
    --repair-sdk-config) repair_sdk_config=true ;;
    --help)
      cat <<'HELP'
Usage: bash scripts/setup.sh [--accept-licenses] [--repair-sdk-config]

Install mise (if missing), pinned project tools, Android CLI packages, and Gradle
in user space. Requires Bash, Python 3, curl, Git, unzip, tar, and native runtime
libraries; see CONTRIBUTING.md. Never invokes sudo or edits shell startup files.

--accept-licenses    Accept Android SDK licenses without interactive prompts.
--repair-sdk-config  Back up conflicting local.properties and update sdk.dir.
HELP
      exit 0
      ;;
    *)
      echo "Unknown setup argument: $arg (see --help)" >&2
      exit 2
      ;;
  esac
done

fail() {
  echo "Setup: $*" >&2
  exit 1
}
for utility in python3 curl git unzip tar; do
  command -v "$utility" >/dev/null || fail "Missing $utility. Install host prerequisites listed in CONTRIBUTING.md and rerun."
done
python3 -B scripts/setup_support.py preflight

# Preserve inherited values before mise replaces them with the project SDK.
inherited_android_home=${ANDROID_HOME:-}
inherited_android_root=${ANDROID_SDK_ROOT:-}
if command -v mise >/dev/null; then
  mise_bin=$(command -v mise)
elif [[ -x $HOME/.local/bin/mise ]]; then
  mise_bin=$HOME/.local/bin/mise
else
  install_dir=$HOME/.local/bin
  mkdir -p "$install_dir"
  [[ -w $install_dir ]] || fail "Not writable: $install_dir"
  download_dir=$(mktemp -d)
  trap 'rm -rf -- "$download_dir"' EXIT
  platform=$(python3 -B scripts/setup_support.py platform)
  curl --fail --silent --show-error --location --retry 3 \
    https://api.github.com/repos/jdx/mise/releases/latest -o "$download_dir/release.json"
  release=$(python3 -B scripts/setup_support.py release "$download_dir/release.json")
  asset="mise-${release}-${platform}"
  release_url="https://github.com/jdx/mise/releases/download/$release"
  curl --fail --silent --show-error --location --retry 3 "$release_url/$asset" -o "$download_dir/mise"
  curl --fail --silent --show-error --location --retry 3 "$release_url/SHASUMS256.txt" -o "$download_dir/checksums"
  python3 -B scripts/setup_support.py checksum "$download_dir/mise" "$asset" "$download_dir/checksums"
  # Stage on the destination filesystem before publishing the verified executable.
  staged_mise=$(mktemp "$install_dir/.mise-XXXXXXXX")
  trap 'rm -rf -- "$download_dir"; rm -f -- "$staged_mise"' EXIT
  cp "$download_dir/mise" "$staged_mise"
  chmod 755 "$staged_mise"
  mv "$staged_mise" "$install_dir/mise"
  mise_bin=$install_dir/mise
fi

# A single minimum in mise.toml is also used by mise itself for normal commands.
minimum=$(sed -n 's/^min_version = "\([^"]*\)"/\1/p' mise.toml)
python3 -B scripts/setup_support.py version "$minimum" "$("$mise_bin" --version)"
PATH="$(dirname -- "$mise_bin"):$PATH"
export PATH
"$mise_bin" trust mise.toml
"$mise_bin" install
sdk=$("$mise_bin" where vfox:android-sdk)
python3 -B scripts/setup_support.py sdk-environment "$sdk" "$inherited_android_home" "$inherited_android_root"
python3 -B scripts/setup_support.py sdk-config "$sdk" "$repair_sdk_config"
"$mise_bin" exec -- bash scripts/setup-android.sh "$accept_licenses" "$sdk"
printf '\nSetup complete. For commands in this checkout:\n  %q exec -- ./gradlew tasks\n' "$mise_bin"
printf 'For an interactive shell, add mise activation yourself (see CONTRIBUTING.md).\n'
