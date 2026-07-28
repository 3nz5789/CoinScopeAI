#!/usr/bin/env bash
# COI-5 / COI-6 / COI-7 — Terminal runbook (no Claude Code required)
# Run from: ~/Projects/CoinScopeAI_v2
# Date: 2026-05-10

set -euo pipefail

echo "=== Step 0: confirm we are in the right repo ==="
pwd   # must be ~/Projects/CoinScopeAI_v2
git remote -v   # must show 3nz5789/CoinScopeAI_v2

echo ""
echo "=== Step 1: create branch ==="
git checkout -b fix/coi-5-6-7-slo-save

echo ""
echo "=== Step 2: copy patch files from Cowork ==="
COWORK="/Users/mac/Documents/Claude/Projects/CoinScopeAI"

# utils/io.py — the shared atomic_write_json primitive (COI-5)
cp "$COWORK/coinscope_trading_engine/utils/io.py" utils/io.py

# test file covering all three issues
cp "$COWORK/tests/test_slo_save.py" tests/test_slo_save.py

echo "  copied utils/io.py"
echo "  copied tests/test_slo_save.py"

echo ""
echo "=== Step 3: wire save() in daily_session_state.py ==="
# Find the exact save() method and apply the patch.
# Preview first:
grep -n "def save" daily_session_state.py || grep -rn "def save" . --include="*.py" | head -10

echo ""
echo "--- Apply this change to daily_session_state.py manually or via sed ---"
echo "Add to top of file (after existing imports):"
echo "  from utils.io import atomic_write_json"
echo ""
echo "Replace save() body (two occurrences — DailySessionState and any subclass):"
echo "  BEFORE:"
echo "    def save(self) -> None:"
echo "        tmp = self._path.with_suffix('.tmp')"
echo "        tmp.write_text(json.dumps(self._to_dict(), indent=2))"
echo "        tmp.replace(self._path)"
echo ""
echo "  AFTER:"
echo "    def save(self) -> bool:"
echo "        \"\"\"Persist session state atomically. Returns True on success.\"\"\""
echo "        return atomic_write_json(self._path, self._to_dict())"

echo ""
echo "=== Step 4: wire save() in trade_monitor.py ==="
grep -n "def save\|def self_cancel\|STATE_ARCHIVED\|write_archive\|\.unlink" trade_monitor.py | head -20

echo ""
echo "--- Apply this change to trade_monitor.py ---"
echo "Add import: from utils.io import atomic_write_json"
echo ""
echo "Replace save() same as above."
echo ""
echo "Replace self_cancel() with:"
cat << 'PATCH'
    def self_cancel(self) -> bool:
        """Archive and remove monitor file. State set only after archive confirmed."""
        if not atomic_write_json(self._archive_path, self._to_dict()):
            logger.error("self_cancel: archive write failed, monitor left intact")
            return False
        try:
            self._path.unlink()
        except OSError as exc:
            logger.warning("self_cancel: unlink failed (archive safe): %s", exc)
        self.state = STATE_ARCHIVED
        return True
PATCH

echo ""
echo "=== Step 5: add trade_log to _to_dict() in daily_session_state.py ==="
echo "In _to_dict(), add:  'trade_log': list(self._trade_log)"
echo "In _from_dict() / load(), add:"
cat << 'PATCH'
        raw = data.get("trade_log", [])
        if isinstance(raw, list):
            obj._trade_log = collections.deque(
                raw[-MAX_LOG_SIZE:], maxlen=MAX_LOG_SIZE
            )
PATCH

echo ""
echo "=== Step 6: run tests ==="
echo "pytest tests/test_slo_save.py -v"
echo "pytest tests/ -x -q"

echo ""
echo "=== Step 7: commit ==="
echo "git add utils/io.py daily_session_state.py trade_monitor.py tests/test_slo_save.py"
echo "git commit -m 'fix(slo): atomic save + self_cancel atomicity + trade_log persistence'"
echo "  closes: COI-5, COI-6, COI-7"
echo "git push origin fix/coi-5-6-7-slo-save"
