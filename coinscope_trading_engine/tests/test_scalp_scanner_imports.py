"""
test_scalp_scanner_imports.py

Regression test for COI-55: verifies scalp_scanner.py imports from the
correct integration layer (app.integrations.<provider>) and NOT from
the stale app.engine.scanner path that no longer exports exchange helpers.

Run:
    pytest coinscope_trading_engine/tests/test_scalp_scanner_imports.py -v
"""

import ast
import pathlib
import pytest


SCALP_SCANNER_PATH = pathlib.Path(
    "coinscope_trading_engine/scanners/scalp_scanner.py"
)

# Imports that must NOT appear — these are the stale pre-restructure paths
BANNED_IMPORT_SOURCES = [
    "app.engine.scanner",
    "engine.scanner",
]

# Imports that MUST be present — canonical post-restructure paths
REQUIRED_IMPORT_SOURCES = [
    "app.integrations.binance",
]


def _get_imports(filepath: pathlib.Path) -> list[tuple[str, str]]:
    """Parse all import statements from a Python file.
    Returns list of (module, name) tuples.
    """
    source = filepath.read_text()
    tree = ast.parse(source)
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            for alias in node.names:
                imports.append((node.module, alias.name))
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports.append((alias.name, "*"))
    return imports


class TestScalpScannerImports:
    """COI-55 regression: scalp_scanner must use integrations layer."""

    def test_file_exists(self):
        """scalp_scanner.py must exist after COI-55 fix."""
        assert SCALP_SCANNER_PATH.exists(), (
            f"scalp_scanner.py not found at {SCALP_SCANNER_PATH}. "
            "COI-55 fix may not have been applied."
        )

    def test_no_banned_imports(self):
        """Must not import from stale app.engine.scanner path."""
        imports = _get_imports(SCALP_SCANNER_PATH)
        violations = [
            (mod, name)
            for mod, name in imports
            if any(banned in mod for banned in BANNED_IMPORT_SOURCES)
        ]
        assert not violations, (
            f"COI-55 regression: banned imports found in scalp_scanner.py:\n"
            + "\n".join(f"  from {mod} import {name}" for mod, name in violations)
            + "\n\nAll exchange helpers must come from app.integrations.<provider>"
        )

    def test_uses_integrations_layer(self):
        """Must import exchange helpers from app.integrations.binance."""
        imports = _get_imports(SCALP_SCANNER_PATH)
        modules_used = {mod for mod, _ in imports}
        missing = [
            src for src in REQUIRED_IMPORT_SOURCES
            if not any(src in mod for mod in modules_used)
        ]
        assert not missing, (
            f"scalp_scanner.py missing required integration imports: {missing}\n"
            "Exchange helpers must come from app.integrations.<provider>"
        )

    def test_okx_not_used_for_trading(self):
        """OKX integration is REST klines fallback only — verify scope comment."""
        source = SCALP_SCANNER_PATH.read_text()
        if "app.integrations.okx" in source:
            # OKX is allowed for klines fallback — but must have scope comment
            assert "data only" in source.lower() or "klines" in source.lower(), (
                "OKX import present but missing scope restriction comment. "
                "OKX is REST klines fallback only — not for trading. See COI-56."
            )

    def test_canonical_thresholds_not_overridden(self):
        """Canonical risk thresholds must not exceed PCC v2 §8 ceilings."""
        source = SCALP_SCANNER_PATH.read_text()
        tree = ast.parse(source)

        violations = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        if target.id == "MAX_LEVERAGE":
                            if isinstance(node.value, ast.Constant):
                                if node.value.value > 10:
                                    violations.append(
                                        f"MAX_LEVERAGE={node.value.value} exceeds ceiling of 10"
                                    )
                        if target.id == "MAX_OPEN_POSITIONS":
                            if isinstance(node.value, ast.Constant):
                                if node.value.value > 5:
                                    violations.append(
                                        f"MAX_OPEN_POSITIONS={node.value.value} exceeds ceiling of 5"
                                    )

        assert not violations, (
            f"Canonical threshold violations in scalp_scanner.py:\n"
            + "\n".join(f"  {v}" for v in violations)
        )
