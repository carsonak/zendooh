#!/usr/bin/env bash
# Run by setup.sh inside mise's project environment.
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.."
: "${ANDROID_HOME:?Run bash scripts/setup.sh}"
: "${ZENDOOH_ANDROID_PACKAGES:?Run bash scripts/setup.sh}"
if [[ ${ANDROID_SDK_ROOT:-} != "$ANDROID_HOME" || ${2:-} != "$ANDROID_HOME" ]]; then
  echo "SDK environment differs from the selected mise installation." >&2
  exit 1
fi
sdkmanager_bin=$(command -v sdkmanager)
[[ $sdkmanager_bin == "$ANDROID_HOME/"* ]] || {
  echo "sdkmanager is outside the selected SDK" >&2
  exit 1
}

if [[ ${1:-false} == true ]]; then
  # yes can exit with SIGPIPE when sdkmanager closes stdin; preserve sdkmanager's
  # status instead of masking genuine failures or treating SIGPIPE as a failure.
  set +e
  yes 2>/dev/null | "$sdkmanager_bin" --sdk_root="$ANDROID_HOME" --licenses
  license_status=${PIPESTATUS[1]}
  set -e
  [[ $license_status == 0 ]] || exit "$license_status"
elif [[ -t 0 ]]; then
  "$sdkmanager_bin" --sdk_root="$ANDROID_HOME" --licenses
else
  license_output=$(mktemp)
  trap 'rm -f -- "$license_output"' EXIT
  "$sdkmanager_bin" --sdk_root="$ANDROID_HOME" --licenses </dev/null >"$license_output" 2>&1 || {
    cat "$license_output" >&2
    exit 1
  }
  if ! grep -q 'All SDK package licenses accepted' "$license_output"; then
    echo "Android licenses need acceptance. Rerun interactively or with --accept-licenses." >&2
    exit 1
  fi
fi

read -r -a packages <<<"$ZENDOOH_ANDROID_PACKAGES"
"$sdkmanager_bin" --sdk_root="$ANDROID_HOME" --install "${packages[@]}"
# A fresh mise invocation refreshes PATH after newly installed SDK packages.
mise exec -- python3 -B scripts/setup_support.py verify-sdk
mise exec -- adb version
mise exec -- apksigner version
mise exec -- java -version
./gradlew --version
