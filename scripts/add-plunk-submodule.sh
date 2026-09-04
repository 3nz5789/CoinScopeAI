#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <plunk-repo-url>"
  echo "Example: $0 https://github.com/org/plunk-repo.git"
  exit 2
fi

PLUNK_URL="$1"
PATH="coinscope-integrations/plunk"
BRANCH="coinscope/add-plunk-submodule"

# fetch branch if exists, otherwise create it
git fetch origin
if git show-ref --verify --quiet refs/heads/$BRANCH; then
  git checkout $BRANCH
else
  git checkout -b $BRANCH
fi

echo "Adding submodule $PLUNK_URL at $PATH"
git submodule add "$PLUNK_URL" "$PATH"

git add .gitmodules "$PATH"
git commit -m "chore: add Plunk as submodule at $PATH"

git push --set-upstream origin "$BRANCH"

echo "Done. Open a PR from $BRANCH into main to merge."
