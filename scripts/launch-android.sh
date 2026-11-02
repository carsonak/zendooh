#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 || -z ${1:-} ]]; then
  echo "Usage: mise run launch:android SERIAL" >&2
  echo "Select the intended device serial from adb devices." >&2
  exit 2
fi

exec adb -s "$1" shell am start -W -n com.zendooh.app/com.zendooh.MainActivity
