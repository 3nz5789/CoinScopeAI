#!/bin/bash
# CoinScopeAI — Cross-Platform Structure Audit & Restructure
# Generated: 2026-05-09 | Run once from Terminal
# Usage: bash /Users/mac/Documents/Claude/Projects/CoinScopeAI/scripts/restructure.sh

set -e
BASE="/Users/mac/Documents/Claude/Projects/CoinScopeAI"
cd "$BASE"

echo "🗂  CoinScopeAI Structure Restructure — $(date)"
echo "================================================"

# ── Create canonical numbered directories ─────────────────────────────────────
echo ""
echo "📁 Creating canonical folder structure..."
mkdir -p \
  00-start-here \
  01-project-overview \
  02-architecture/decisions \
  03-roadmap \
  05-risk-management \
  06-reports \
  07-workflows/incidents \
  08-meeting-notes/sessions \
  09-research/ml \
  09-research/market-research \
  10-templates/skills \
  11-legal \
  12-finance \
  13-marketing \
  14-admin \
  99-archive
echo "   ✅ Directories ready"

# ── 00 — Start Here ───────────────────────────────────────────────────────────
echo ""
echo "00 — Start Here"
[ -f CONTEXT_PRIMER.md ]            && mv CONTEXT_PRIMER.md 00-start-here/ && echo "   ✅ CONTEXT_PRIMER.md"

# ── 01 — Project Overview ─────────────────────────────────────────────────────
echo ""
echo "01 — Project Overview"
[ -f Business_Plan_v1.md ]          && mv Business_Plan_v1.md 01-project-overview/ && echo "   ✅ Business_Plan_v1.md"
[ -d business-plan ]                && mv business-plan 01-project-overview/business-plan && echo "   ✅ business-plan/"
[ -d strategy ]                     && mv strategy/strategic-memo-2026-04-29.md 01-project-overview/ 2>/dev/null && rmdir strategy 2>/dev/null; echo "   ✅ strategic-memo"

# ── 02 — Architecture ─────────────────────────────────────────────────────────
echo ""
echo "02 — Architecture"
if [ -d architecture ]; then
  mv architecture/architecture.md 02-architecture/ 2>/dev/null && echo "   ✅ architecture.md"
  mv architecture/design-system-manifest.md 02-architecture/ 2>/dev/null && echo "   ✅ design-system-manifest.md"
  mv architecture/enhancement-audit-2026-05-02.md 08-meeting-notes/sessions/ 2>/dev/null && echo "   ✅ enhancement-audit → sessions"
  mv architecture/session-2026-05-02-summary.md 08-meeting-notes/sessions/ 2>/dev/null && echo "   ✅ session-summary → sessions"
  rmdir architecture 2>/dev/null && echo "   ✅ architecture/ removed"
fi
if [ -d docs/decisions ]; then
  cp docs/decisions/*.md 02-architecture/decisions/ 2>/dev/null && echo "   ✅ ADRs copied → 02-architecture/decisions"
fi

# ── 03 — Roadmap ─────────────────────────────────────────────────────────────
echo ""
echo "03 — Roadmap"
[ -f mvp-readiness-checklist.md ]           && mv mvp-readiness-checklist.md 03-roadmap/ && echo "   ✅ mvp-readiness-checklist.md"
[ -f Production_Candidate_Criteria_v2.md ]  && mv Production_Candidate_Criteria_v2.md 03-roadmap/production-candidate-criteria-v2.md && echo "   ✅ PCC v2"
[ -f Validation_Data_Analysis_Plan_v1.md ]  && mv Validation_Data_Analysis_Plan_v1.md 03-roadmap/validation-data-analysis-plan-v1.md && echo "   ✅ Validation analysis plan"
[ -f Validation_Phase_Exit_Memo_TEMPLATE.md ] && mv Validation_Phase_Exit_Memo_TEMPLATE.md 03-roadmap/validation-phase-exit-memo-template.md && echo "   ✅ Validation exit memo template"

# ── 05 — Risk Management ──────────────────────────────────────────────────────
echo ""
echo "05 — Risk Management"
if [ -d docs/risk ]; then
  mv docs/risk/*.md 05-risk-management/ 2>/dev/null && echo "   ✅ docs/risk/* → 05-risk-management"
fi

# ── 07 — Workflows ────────────────────────────────────────────────────────────
echo ""
echo "07 — Workflows"
if [ -d docs/runbooks ]; then
  for f in docs/runbooks/*.md; do
    [ -f "$f" ] && mv "$f" 07-workflows/ && echo "   ✅ $(basename $f)"
  done
  rm -f docs/runbooks/*.bak 2>/dev/null
  rmdir docs/runbooks 2>/dev/null
fi
if [ -d docs/ops ]; then
  mv docs/ops/*.md 07-workflows/ 2>/dev/null && echo "   ✅ docs/ops/* → 07-workflows"
  rmdir docs/ops 2>/dev/null
fi
if [ -d incidents ]; then
  mv incidents/*.md 07-workflows/incidents/ 2>/dev/null && echo "   ✅ incidents/* → 07-workflows/incidents"
  rmdir incidents 2>/dev/null && echo "   ✅ incidents/ removed"
fi

# ── 08 — Meeting Notes ────────────────────────────────────────────────────────
echo ""
echo "08 — Meeting Notes"
# Decision log — canonical location
if [ -d 01-project-overview/business-plan/_decisions ]; then
  cp 01-project-overview/business-plan/_decisions/decision-log.md 08-meeting-notes/decision-log.md 2>/dev/null && echo "   ✅ decision-log.md → 08-meeting-notes (copy)"
fi
# Session files at root
for f in CODE_REVIEW_*.md CONFIG_AUDIT_*.md; do
  [ -f "$f" ] && mv "$f" 08-meeting-notes/sessions/ && echo "   ✅ $f → sessions"
done
# Architecture session files (already moved above)

# ── 09 — Research ─────────────────────────────────────────────────────────────
echo ""
echo "09 — Research"
if [ -d ml ]; then
  mv ml/regime_classifier_v3.py 09-research/ml/ 2>/dev/null
  mv ml/regime_label_dataset_v1.py 09-research/ml/ 2>/dev/null
  [ -d ml/models ] && mv ml/models 09-research/ml/models 2>/dev/null
  [ -d ml/data ] && mv ml/data 09-research/ml/data 2>/dev/null
  rmdir ml/__pycache__ 2>/dev/null
  rmdir ml 2>/dev/null && echo "   ✅ ml/ → 09-research/ml"
fi
if [ -d research ]; then
  mv research/*.md 09-research/market-research/ 2>/dev/null && echo "   ✅ research/* → 09-research/market-research"
  rmdir research 2>/dev/null && echo "   ✅ research/ removed"
fi
if [ -d docs/ml ]; then
  mv docs/ml/*.md 09-research/ml/ 2>/dev/null && echo "   ✅ docs/ml/* → 09-research/ml"
  rmdir docs/ml 2>/dev/null
fi

# ── 10 — Templates ────────────────────────────────────────────────────────────
echo ""
echo "10 — Templates"
if [ -d skills_src ]; then
  mv skills_src 10-templates/skills 2>/dev/null && echo "   ✅ skills_src → 10-templates/skills"
fi

# ── 11 — Legal ────────────────────────────────────────────────────────────────
echo ""
echo "11 — Legal"
if [ -d legal ]; then
  mv legal/*.md 11-legal/ 2>/dev/null && echo "   ✅ legal/* → 11-legal"
  rmdir legal 2>/dev/null && echo "   ✅ legal/ removed"
fi
[ -f Counsel_Brief_v2.md ] && mv Counsel_Brief_v2.md 11-legal/counsel-brief-v2.md && echo "   ✅ Counsel_Brief_v2.md → 11-legal"

# ── 14 — Admin ────────────────────────────────────────────────────────────────
echo ""
echo "14 — Admin"
if [ -d admin ]; then
  mv admin/*.pdf 14-admin/ 2>/dev/null && echo "   ✅ admin/*.pdf → 14-admin"
  rmdir admin 2>/dev/null && echo "   ✅ admin/ removed"
fi

# ── 99 — Archive ──────────────────────────────────────────────────────────────
echo ""
echo "99 — Archive"
[ -f OPS_Linear_Tickets_v1.md ]         && mv OPS_Linear_Tickets_v1.md 99-archive/ && echo "   ✅ OPS_Linear_Tickets_v1"
[ -f Vendor_Failure_Mode_Mapping_v1.md ] && mv Vendor_Failure_Mode_Mapping_v1.md 99-archive/ && echo "   ✅ Vendor_Failure_Mode_Mapping_v1"
[ -f "CLAUDE.md.bak.20260503-151747" ]  && mv "CLAUDE.md.bak.20260503-151747" 99-archive/ && echo "   ✅ CLAUDE.md.bak"
[ -d archive ]                          && mv archive/* 99-archive/ 2>/dev/null && rmdir archive 2>/dev/null && echo "   ✅ archive/ merged → 99-archive"

# ── Scripts ───────────────────────────────────────────────────────────────────
echo ""
echo "Scripts"
[ -f validation_analysis.py ]  && mv validation_analysis.py scripts/ && echo "   ✅ validation_analysis.py → scripts"
[ -f stripe_test_price_ids.json ] && mv stripe_test_price_ids.json 99-archive/ && echo "   ✅ stripe_test_price_ids → 99-archive"
[ -f billing_server.py ]       && mv billing_server.py 99-archive/ && echo "   ✅ billing_server.py → 99-archive"
[ -f prometheus.yml ]          && mv prometheus.yml 04-development/prometheus.yml 2>/dev/null || mv prometheus.yml 99-archive/ 2>/dev/null; echo "   ✅ prometheus.yml"

# ── Cleanup loose dirs ────────────────────────────────────────────────────────
echo ""
echo "Cleanup"
[ -f .write_test_2 ]           && rm .write_test_2 && echo "   ✅ deleted .write_test_2"
rmdir billing 2>/dev/null      && echo "   ✅ removed empty billing/" || true
rmdir dashboard 2>/dev/null    && echo "   ✅ removed empty dashboard/" || true
rmdir data 2>/dev/null         && echo "   ✅ removed empty data/" || true
rmdir testnet_trader 2>/dev/null && echo "   ✅ removed empty testnet_trader/" || true

# ── 04-development placeholder ───────────────────────────────────────────────
echo ""
echo "04 — Development symlinks/notes"
cat > 04-development/README.md << 'EOF'
# 04 — Development

Engine code lives in the Git repos, not here.

| Repo | Path | Purpose |
|---|---|---|
| v1 engine | `~/Projects/coinscope-ai` | Public, canonical engine |
| v2 private | `~/Projects/CoinScopeAI_v2` | Private framework |
| Dashboard | `~/Projects/coinscope-ai/coinscopeai-dashboard` | React frontend |

Key configs:
- `docker-compose.yml` — service orchestration
- `.env.example` — canonical env template (MAX_OPEN_POSITIONS=5, MAX_LEVERAGE=10)
- `scripts/` — operator scripts (drift_detector, risk_guardrail, daily_status, labels)
EOF
echo "   ✅ 04-development/README.md created"

# ── Final state ───────────────────────────────────────────────────────────────
echo ""
echo "================================================"
echo "✅ Restructure complete"
echo ""
echo "Final root structure:"
ls -la | grep -E "^d" | awk '{print $NF}' | grep -v "^\."
echo ""
echo "Loose files remaining at root:"
ls -la | grep "^-" | grep -v "^\." | awk '{print $NF}'
