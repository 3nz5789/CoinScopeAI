#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: redacted_secret_scan.sh <repository-directory> [artifact-file]

Searches text files without printing matching values. Output columns are:
category|scope|path|line_numbers

Matches require classification; a match alone does not prove a value is live.
USAGE
}

if [[ $# -lt 1 || $# -gt 2 || ! -d "$1" ]]; then
  usage >&2
  exit 2
fi

repository=$(cd "$1" && pwd)
artifact=${2:-}

declare -a paths=()
while IFS= read -r -d '' path; do
  paths+=("$path")
done < <(
  find "$repository" -type f \
    -not -path '*/.git/*' \
    -not -path '*/node_modules/*' \
    -not -path '*/dist/*' \
    -not -path '*/.manus-logs/*' \
    -print0
)

scan_paths() {
  local label="$1"
  local pattern="$2"
  local scope="$3"
  shift 3

  for path in "$@"; do
    if [[ -f "$path" ]] && grep -Iq . "$path" && grep -qIE "$pattern" "$path"; then
      local lines
      lines=$(grep -nIE "$pattern" "$path" | cut -d: -f1 | paste -sd, -)
      printf '%s|%s|%s|%s\n' "$label" "$scope" "${path#$repository/}" "$lines"
    fi
  done
}

printf '%s\n' 'category|scope|path|line_numbers'
scan_paths 'stripe_webhook_prefix' 'whsec_[[:alnum:]_:-]{4,}' 'repository' "${paths[@]}"
scan_paths 'stripe_secret_or_restricted_key' '(sk|rk)_(live|test)_[[:alnum:]_:-]{8,}' 'repository' "${paths[@]}"
scan_paths 'github_token' 'gh[pousr]_[[:alnum:]_:-]{20,}' 'repository' "${paths[@]}"
scan_paths 'aws_access_key' 'AKIA[0-9A-Z]{16}' 'repository' "${paths[@]}"
scan_paths 'private_key_block' 'BEGIN (OPENSSH|RSA|EC|DSA|PGP|PRIVATE)' 'repository' "${paths[@]}"
scan_paths 'generic_credential_assignment' '(secret|token|api[_-]?key|password|private[_-]?key)[[:alnum:]_-]*[[:space:]]*[:=][[:space:]]*["'"'"'`][^"'"'"'`[:space:]]{8,}' 'repository' "${paths[@]}"

if [[ -n "$artifact" ]]; then
  if [[ ! -f "$artifact" ]]; then
    printf '%s\n' "artifact_error|artifact|$artifact|not_found" >&2
    exit 2
  fi

  scan_paths 'stripe_webhook_prefix' 'whsec_[[:alnum:]_:-]{4,}' 'artifact' "$artifact"
  scan_paths 'stripe_secret_or_restricted_key' '(sk|rk)_(live|test)_[[:alnum:]_:-]{8,}' 'artifact' "$artifact"
  scan_paths 'github_token' 'gh[pousr]_[[:alnum:]_:-]{20,}' 'artifact' "$artifact"
  scan_paths 'aws_access_key' 'AKIA[0-9A-Z]{16}' 'artifact' "$artifact"
  scan_paths 'private_key_block' 'BEGIN (OPENSSH|RSA|EC|DSA|PGP|PRIVATE)' 'artifact' "$artifact"
  scan_paths 'generic_credential_assignment' '(secret|token|api[_-]?key|password|private[_-]?key)[[:alnum:]_-]*[[:space:]]*[:=][[:space:]]*["'"'"'`][^"'"'"'`[:space:]]{8,}' 'artifact' "$artifact"
fi
