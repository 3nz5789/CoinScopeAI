# Common operator commands. Run from the repository root.
# Phase-1 defaults are local, paper-only, and do not require exchange credentials.

PYTHON ?= python3
AGENT_OS_PORT ?= 8010
DATA_DIR ?= ./data/recordings
SPEED ?= 1.0
START ?=
END ?=

.PHONY: help install dev dev-all worker test smoke lint format typecheck guardrail sync status replay agent-demo clean

help:
	@echo ""
	@echo "CoinScopeAI — available targets"
	@echo "────────────────────────────────────────────────────────"
	@echo "  make install     Install Python dependencies"
	@echo "  make dev         Alias for the Phase-1 Agent OS API"
	@echo "  make dev-all     Start the Phase-1 Agent OS API locally"
	@echo "  make worker      Run one deterministic paper worker cycle"
	@echo "  make agent-demo  Alias for worker"
	@echo "  make test        Run repository and Agent OS tests"
	@echo "  make replay      Replay recorded data through the existing stream CLI"
	@echo "  make smoke       Run fast CI smoke tests"
	@echo "  make lint        Run ruff + black checks (no auto-fix)"
	@echo "  make format      Auto-fix with ruff + black"
	@echo "  make typecheck   Run mypy type checks on Phase-1 packages"
	@echo "  make guardrail   Run risk threshold guardrail"
	@echo "  make sync        Run session-end sync verifier"
	@echo "  make status      Run the daily engine status script"
	@echo "  make clean       Remove build/cache artefacts"
	@echo "────────────────────────────────────────────────────────"
	@echo ""

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt
	$(PYTHON) -m pip install ruff black mypy pytest pytest-asyncio pytest-cov

dev: dev-all

dev-all:
	@echo "Starting CoinScopeAI Agent OS API in PAPER mode on port $(AGENT_OS_PORT)..."
	@echo "Live order placement: disabled. Mainnet wallets: disabled."
	$(PYTHON) -m uvicorn agent_os.api.app:app --reload --port $(AGENT_OS_PORT)

worker:
	@echo "Running one deterministic CoinScopeAI Agent OS paper cycle..." >&2
	@$(PYTHON) -m services.agent_worker.main

agent-demo: worker

test:
	$(PYTHON) -m pytest -x -q tests/

smoke:
	$(PYTHON) -m pytest -x -q tests/test_ci_smoke.py -W ignore::pytest.PytestConfigWarning

lint:
	ruff check agent_os services/agent_worker tests/agent_os
	black --check agent_os services/agent_worker tests/agent_os

format:
	ruff check --fix agent_os services/agent_worker tests/agent_os
	black agent_os services/agent_worker tests/agent_os

typecheck:
	mypy agent_os services/agent_worker --ignore-missing-imports --no-error-summary

guardrail:
	@echo "Running risk threshold guardrail..."
	$(PYTHON) scripts/risk_threshold_guardrail.py

sync:
	$(PYTHON) scripts/sync_verify.py

status:
	./scripts/run_daily_status.sh

replay:
	@test -n "$(DATA_DIR)" || (echo "DATA_DIR is required" && exit 2)
	$(PYTHON) -m services.market_data.streams.cli replay \
		--data-dir "$(DATA_DIR)" \
		--speed "$(SPEED)" \
		$(if $(START),--start "$(START)",) \
		$(if $(END),--end "$(END)",) \
		--verbose

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	find . -name ".coverage" -delete 2>/dev/null || true
	find . -name "coverage.xml" -delete 2>/dev/null || true
	@echo "Clean ✓"
