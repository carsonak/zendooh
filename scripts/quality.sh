#!/usr/bin/env bash
set -euo pipefail

cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.."
tool=${1:?Expected a tool name}
case "$tool" in
  prettier | markdown | shell | shellcheck | toml | workflows) ;;
  *)
    echo "Unknown tool: $tool" >&2
    exit 2
    ;;
esac
mode=${2:-check}
if [[ $mode != check && $mode != write ]]; then
  echo "Expected check or write mode" >&2
  exit 2
fi

# Include new authored files with explicit generated/tooling exclusions.
# NUL delimiters preserve spaces.
# Respect Git exclusions while including new authored files.
files=()
while IFS= read -r -d '' file; do
  [[ -f $file ]] || continue
  file="./${file#./}"
  case "$tool:$file" in
    prettier:*.md | prettier:*.json | prettier:*.yaml | prettier:*.yml | prettier:./.prettierrc)
      files+=("$file")
      ;;
    markdown:*.md) files+=("$file") ;;
    shell:*.sh | shellcheck:*.sh) files+=("$file") ;;
    toml:*.toml) files+=("$file") ;;
    workflows:./.github/workflows/*.yml | workflows:./.github/workflows/*.yaml)
      files+=("$file")
      ;;
  esac
done < <(git ls-files --cached --others --exclude-standard -z | sort -zu)

if ((${#files[@]} == 0)); then
  echo "No files for $tool"
  exit 0
fi

case "$tool:$mode" in
  prettier:write) prettier --write "${files[@]}" ;;
  prettier:check) prettier --check "${files[@]}" ;;
  markdown:*) markdownlint "${files[@]}" ;;
  shell:write) shfmt -w -i 2 -ci "${files[@]}" ;;
  shell:check) shfmt -d -i 2 -ci "${files[@]}" ;;
  shellcheck:*) shellcheck "${files[@]}" ;;
  toml:write) taplo format "${files[@]}" ;;
  toml:check) taplo format --check "${files[@]}" ;;
  workflows:*) actionlint "${files[@]}" ;;
  *)
    echo "Unknown tool: $tool" >&2
    exit 2
    ;;
esac
