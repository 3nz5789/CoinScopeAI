import ast
from pathlib import Path

ROOT = Path(__file__).parents[2]
PRODUCTION = {
    ROOT / "agent_os/persistence/authorization_contracts.py",
    ROOT / "agent_os/persistence/authorization_ports.py",
    ROOT / "agent_os/persistence/authorization_memory.py",
    ROOT / "agent_os/persistence/audit_contracts.py",
    ROOT / "agent_os/persistence/audit_redaction.py",
}
FORBIDDEN_IMPORT_ROOTS = {
    "boto3",
    "botocore",
    "cloudflare",
    "flask",
    "fastapi",
    "httpx",
    "psycopg",
    "requests",
    "socket",
    "sqlite3",
    "subprocess",
    "urllib",
    "websockets",
}
FORBIDDEN_CAPABILITIES = {
    "authorization_relational",
    "capture",
    "connector",
    "exchange",
    "live",
    "network",
    "recorder",
    "replay",
    "scanner",
    "sqlite",
    "storage",
    "testnet",
    "wallet",
}


def test_exact_a4_production_files_are_present():
    assert all(path.is_file() for path in PRODUCTION)


def test_a4_production_imports_are_safe():
    for path in PRODUCTION:
        tree = ast.parse(path.read_text(), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                roots = [alias.name.split(".")[0] for alias in node.names]
            elif isinstance(node, ast.ImportFrom):
                roots = [node.module.split(".")[0]] if node.module else []
            else:
                continue
            assert not set(roots) & FORBIDDEN_IMPORT_ROOTS, path


def test_a4_production_has_no_forbidden_capability_calls_or_names():
    for path in PRODUCTION:
        tree = ast.parse(path.read_text(), filename=str(path))
        executable_names = {
            node.id.lower() for node in ast.walk(tree) if isinstance(node, ast.Name)
        }
        executable_attributes = {
            node.attr.lower() for node in ast.walk(tree) if isinstance(node, ast.Attribute)
        }
        assert not (executable_names | executable_attributes) & FORBIDDEN_CAPABILITIES, path


def test_ports_are_protocol_only():
    tree = ast.parse((ROOT / "agent_os/persistence/authorization_ports.py").read_text())
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            assert any(isinstance(base, ast.Name) and base.id == "Protocol" for base in node.bases)
            for method in node.body:
                if isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    assert len(method.body) == 1
                    assert isinstance(method.body[0], ast.Expr)
                    assert isinstance(method.body[0].value, ast.Constant)
                    assert method.body[0].value.value is Ellipsis
