# CoinScopeAI — Plunk submodule integration

This directory is intended to contain the Plunk repository as a git submodule.

Why a submodule?
- Keeps the upstream Plunk commit history intact.
- Makes updating the Plunk dependency explicit (pin to a commit or branch).
- Avoids copying vendor code into this repo and helps track upstream changes.

Path
- Intended submodule path: `coinscope-integrations/plunk`

How to add the submodule (run locally)

1. Fetch the branch I created and switch to it:

```bash
git fetch origin
git checkout -b coinscope/add-plunk-submodule origin/coinscope/add-plunk-submodule
```

2. Add the Plunk repo as a submodule (replace `<PLUNK_REPO_URL>`):

```bash
git submodule add <PLUNK_REPO_URL> coinscope-integrations/plunk
```

3. Stage and commit the submodule link and .gitmodules file:

```bash
git add .gitmodules coinscope-integrations/plunk
git commit -m "chore: add Plunk as submodule at coinscope-integrations/plunk"
```

4. Push the gitlink commit to the branch:

```bash
git push --set-upstream origin coinscope/add-plunk-submodule
```

Security notes
- Do NOT commit secrets (API keys, .env files, or other credentials). Remove or redact any such files from the Plunk repo before committing them here.
- Use repository-level secrets (GitHub Secrets, Vault, AWS Secrets Manager) for runtime keys and CI.

Updating the submodule

To update the submodule to a new commit:

```bash
cd coinscope-integrations/plunk
# fetch and checkout the desired commit or branch
git fetch origin
git checkout <commit-or-branch>
cd ../..
# record the new gitlink in the parent repo
git add coinscope-integrations/plunk
git commit -m "chore(submodule): update Plunk to <commit-or-branch>"
git push
```

Cloning the repo with submodules

```bash
git clone --recurse-submodules git@github.com:3nz5789/CoinScopeAI.git
# or if already cloned
git submodule update --init --recursive
```

If you prefer I create the actual gitlink commit pointing at a specific upstream commit (so you don't need to run `git submodule add` locally), provide the Plunk repo commit SHA and I can create that commit for you.
