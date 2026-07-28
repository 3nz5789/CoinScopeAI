#!/usr/bin/env python3
"""
auto_sync.py — CoinScopeAI Cross-Platform Auto-Sync Engine
Runs at session end to propagate all state changes.

Usage:
    python3 scripts/auto_sync.py              # full sync
    python3 scripts/auto_sync.py --check      # dry run
    python3 scripts/auto_sync.py --git-only   # git only
    python3 scripts/auto_sync.py --verify     # run sync_verify.py after
"""

import os, sys, subprocess, argparse
from datetime import datetime, timezone

REPO_DIR   = os.path.expanduser("~/Projects/CoinScopeAI")
COWORK_DIR = "/Users/mac/Documents/Claude/Projects/CoinScopeAI"
SCRIPTS    = os.path.join(COWORK_DIR, "scripts")
DATE       = datetime.now(timezone.utc).strftime("%Y-%m-%d")
G="\033[92m"; R="\033[91m"; Y="\033[93m"; E="\033[0m"; B="\033[1m"

results = []
def ok(m):      print(f"  {G}✅{E} {m}"); results.append((m, True, ""))
def err(m, d=""): print(f"  {R}❌{E} {m}" + (f" — {d}" if d else "")); results.append((m, False, d))
def warn(m, d=""): print(f"  {Y}⚠️ {E} {m}" + (f" — {d}" if d else "")); results.append((m, None, d))
def section(t): print(f"\n{B}{'─'*52}{E}\n{B}  {t}{E}\n{B}{'─'*52}{E}")
def run(cmd, cwd=None): return subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)

parser = argparse.ArgumentParser()
parser.add_argument("--check",    action="store_true")
parser.add_argument("--git-only", action="store_true")
parser.add_argument("--verify",   action="store_true")
args = parser.parse_args()
DRY = args.check

print(f"\n{B}{'═'*52}\n  CoinScopeAI Auto-Sync — {DATE}\n  {'DRY RUN' if DRY else 'LIVE'}\n{'═'*52}{E}")

# 1. Git
section("1. Git Repository")
if not os.path.isdir(REPO_DIR):
    err("Repo not found", REPO_DIR)
else:
    r = run("git remote get-url origin", cwd=REPO_DIR)
    remote = r.stdout.strip()
    (ok if "CoinScopeAI" in remote else err)(f"Remote: {remote}")

    r = run("git status --porcelain", cwd=REPO_DIR)
    files = r.stdout.strip().splitlines()
    if not files:
        ok("No uncommitted changes")
    else:
        warn(f"{len(files)} uncommitted file(s)", ", ".join(f.strip() for f in files[:5]))
        if not DRY:
            r = run(f'git add -A && git commit -m "chore(sync): auto-sync {DATE}"', cwd=REPO_DIR)
            (ok if r.returncode == 0 else err)("Committed changes")

    r = run("git rev-list --count @{u}..HEAD 2>/dev/null || echo 0", cwd=REPO_DIR)
    ahead = int(r.stdout.strip() or 0)
    if ahead > 0:
        warn(f"{ahead} commit(s) ahead — pushing")
        if not DRY:
            r = run("git push", cwd=REPO_DIR)
            (ok if r.returncode == 0 else err)("Pushed to origin/main")
    else:
        ok("Remote up to date")

if args.git_only:
    print(f"\n{B}  Done.{E}\n"); sys.exit(0)

# 2. Drift
section("2. Drift Detection")
drift = os.path.join(SCRIPTS, "drift_detector.py")
if os.path.isfile(drift):
    r = run(f"python3 {drift}", cwd=COWORK_DIR)
    (ok if r.returncode == 0 else err)("Drift detector", "run manually for details" if r.returncode else "")
else:
    warn("drift_detector.py not found")

# 3. Guardrail
section("3. Risk Threshold Guardrail")
g = os.path.join(SCRIPTS, "risk_threshold_guardrail.py")
if os.path.isfile(g):
    r = run(f"python3 {g}", cwd=COWORK_DIR)
    (ok if r.returncode == 0 else err)("Risk guardrail")
else:
    warn("risk_threshold_guardrail.py not found")

# 4. Mac Structure
section("4. Mac Structure")
dirs  = ["01-project-overview","03-roadmap","08-sessions","09-research","11-legal","14-admin","99-archive","docs","scripts","skills"]
files = ["CLAUDE.md","CONTEXT_PRIMER.md","README.md","canonical-structure-spec.md"]
bad   = ["Business_Plan_v1.md","billing_server.py","admin","architecture","legal","incidents","ml","research","strategy","skills_src"]
miss_d = [d for d in dirs  if not os.path.isdir(os.path.join(COWORK_DIR, d))]
miss_f = [f for f in files if not os.path.isfile(os.path.join(COWORK_DIR, f))]
stale  = [i for i in bad   if os.path.exists(os.path.join(COWORK_DIR, i))]
if not miss_d and not miss_f and not stale:
    ok("Mac root canonical — all checks pass")
else:
    if miss_d: err(f"Missing dirs", ", ".join(miss_d))
    if miss_f: err(f"Missing files", ", ".join(miss_f))
    if stale:  err(f"Stale items at root", ", ".join(stale))

# 5. Env
section("5. .env.example Values")
env = os.path.join(COWORK_DIR, ".env.example")
if os.path.isfile(env):
    c = open(env).read()
    (ok if "MAX_OPEN_POSITIONS=5" in c else err)("MAX_OPEN_POSITIONS=5")
    (ok if "MAX_LEVERAGE=10" in c else err)("MAX_LEVERAGE=10")
    (ok if "coinscope-ai" not in c else err)("No stale repo name in .env.example")
else:
    warn(".env.example not found")

# 6. Summary
section("6. Summary")
passed = sum(1 for _,p,_ in results if p is True)
failed = sum(1 for _,p,_ in results if p is False)
print(f"\n{B}  {G if not failed else R}Result: {passed}/{len(results)} passed, {failed} failed{E}")
print(f"""
  Notion session report template:
  📅 Session Report — {DATE}
  Git: {"✅ synced" if not DRY else "⏭ dry run"}
  Drift: {"✅ clean" if not any(not p and p is not None for _,p,_ in results) else "❌ check output"}
  Mac: {"✅ canonical" if not stale and not miss_d else "⚠️ issues found"}
  VPS: 🔴 pending (COI-68)
""")

if args.verify:
    section("7. Sync Verify")
    v = os.path.join(SCRIPTS, "sync_verify.py")
    if os.path.isfile(v):
        subprocess.run(f"python3 {v}", shell=True, cwd=COWORK_DIR)

print(f"{B}{'═'*52}{E}\n")
sys.exit(0 if not failed else 1)
