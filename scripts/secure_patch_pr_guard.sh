#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "Usage: secure_patch_pr_guard.sh <base-sha> <head-sha>" >&2
  exit 2
fi

base_sha="$1"
head_sha="$2"
pattern='whsec_[[:alnum:]_:-]{4,}|(sk|rk)_(live|test)_[[:alnum:]_:-]{8,}|gh[pousr]_[[:alnum:]_:-]{20,}|AKIA[0-9A-Z]{16}|BEGIN (OPENSSH|RSA|EC|DSA|PGP|PRIVATE)'
violations=0

while IFS= read -r -d '' file; do
  added_lines=$(git -c color.ui=false diff --no-ext-diff --unified=0 "$base_sha" "$head_sha" -- "$file" | awk '/^\+\+\+/{next} /^\+/{print}')
  if grep -qE "$pattern" <<<"$added_lines"; then
    echo "::error file=$file::Potential secret or private-key pattern was added. Value redacted; remove it or replace it with a non-secret fixture."
    violations=1
  fi
done < <(git diff --name-only -z "$base_sha" "$head_sha")

if [[ "$violations" -ne 0 ]]; then
  echo "Secure Patch Release Scan failed because a newly added sensitive pattern requires review."
  exit 1
fi

echo "No newly added sensitive key or private-key patterns detected."
