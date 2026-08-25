import ast
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
PRODUCTION_PATHS = (
    ROOT / "agent_os" / "persistence" / "contracts.py",
    ROOT / "agent_os" / "persistence" / "ports.py",
    ROOT / "agent_os" / "persistence" / "ingress.py",
)
ALLOWED_IMPORT_ROOTS = {"__future__", "dataclasses", "enum", "re", "typing"}
FORBIDDEN_IMPORT_ROOTS = {
    "asyncio",
    "boto3",
    "botocore",
    "cryptography",
    "hashlib",
    "http",
    "httpx",
    "io",
    "json",
    "os",
    "pathlib",
    "requests",
    "socket",
    "sqlite3",
    "subprocess",
    "urllib",
}
FORBIDDEN_FIELD_NAMES = {
    "account",
    "artifact_bytes",
    "buffer",
    "byte",
    "bytearray",
    "bytes",
    "credentials",
    "descriptor",
    "external_order_id",
    "file",
    "filename",
    "filepath",
    "generic_payload",
    "key",
    "location",
    "locator",
    "material",
    "memoryview",
    "metadata",
    "order_id",
    "path",
    "payload",
    "pnl",
    "position",
    "provider_payload",
    "prompt",
    "raw_payload",
    "raw_rationale",
    "scanner_payload",
    "secret",
    "source_locator",
    "storage",
    "storage_handle",
    "storage_id",
    "storage_ref",
    "storage_reference",
    "storage_uri",
    "strategy_source",
    "stream",
    "token",
    "url",
    "uri",
}
FORBIDDEN_CALL_NAMES = {
    "canonicalize",
    "connect",
    "copy",
    "decrypt",
    "encrypt",
    "execute",
    "export",
    "hash",
    "load",
    "open",
    "read",
    "scan",
    "sha256",
    "submit",
    "write",
}
FORBIDDEN_CAPABILITY_NAMES = {
    "api",
    "capture",
    "connector",
    "database",
    "exchange",
    "filesystem",
    "kms",
    "network",
    "replay",
    "scanner_client",
    "storage",
    "subprocess",
    "wallet",
}


def parsed_sources() -> list[tuple[Path, ast.Module, str]]:
    return [(path, ast.parse(path.read_text()), path.read_text()) for path in PRODUCTION_PATHS]


def node_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


def test_only_approved_production_paths_exist() -> None:
    assert not (ROOT / "agent_os" / "persistence" / "__init__.py").exists()
    assert [path.relative_to(ROOT).as_posix() for path in PRODUCTION_PATHS] == [
        "agent_os/persistence/contracts.py",
        "agent_os/persistence/ports.py",
        "agent_os/persistence/ingress.py",
    ]


def test_production_imports_are_standard_library_or_relative_contract_imports() -> None:
    for path, tree, _ in parsed_sources():
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    root = alias.name.split(".", 1)[0]
                    assert root in ALLOWED_IMPORT_ROOTS, (path, alias.name)
                    assert root not in FORBIDDEN_IMPORT_ROOTS, (path, alias.name)
            elif isinstance(node, ast.ImportFrom) and node.level == 0:
                root = (node.module or "").split(".", 1)[0]
                assert root in ALLOWED_IMPORT_ROOTS, (path, node.module)
                assert root not in FORBIDDEN_IMPORT_ROOTS, (path, node.module)


def test_production_contracts_have_no_material_or_storage_fields() -> None:
    for path, tree, _ in parsed_sources():
        for node in ast.walk(tree):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                assert node.target.id.lower() not in FORBIDDEN_FIELD_NAMES, (path, node.target.id)
            if isinstance(node, ast.arg):
                assert node.arg.lower() not in FORBIDDEN_FIELD_NAMES, (path, node.arg)
            if isinstance(node, ast.Constant):
                assert not isinstance(node.value, (bytes, bytearray, memoryview)), path


def test_production_code_has_no_side_effecting_capability_calls() -> None:
    for path, tree, _ in parsed_sources():
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                name = node_name(node.func)
                assert name not in FORBIDDEN_CALL_NAMES, (path, name, node.lineno)
            if isinstance(node, ast.Attribute):
                assert node.attr.lower() not in FORBIDDEN_CAPABILITY_NAMES, (
                    path,
                    node.attr,
                    node.lineno,
                )


def test_ports_are_protocol_declarations_without_concrete_method_bodies() -> None:
    path = ROOT / "agent_os" / "persistence" / "ports.py"
    tree = ast.parse(path.read_text())
    classes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
    assert {node.name for node in classes} == {"MetadataReceiptPort", "ReceiptRedactionPort"}
    for class_node in classes:
        assert [node_name(base) for base in class_node.bases] == ["Protocol"]
        for method in class_node.body:
            if not isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            executable = [
                statement
                for statement in method.body
                if not (
                    isinstance(statement, ast.Expr)
                    and isinstance(statement.value, ast.Constant)
                    and isinstance(statement.value.value, str)
                )
            ]
            assert len(executable) == 1
            assert isinstance(executable[0], ast.Expr)
            assert isinstance(executable[0].value, ast.Constant)
            assert executable[0].value.value is Ellipsis


def test_security_scan_does_not_rely_on_ignored_or_generated_files() -> None:
    for path in PRODUCTION_PATHS:
        assert path.is_file()
        assert path.suffix == ".py"
        assert path.parent.name == "persistence"


@pytest.mark.parametrize(
    "forbidden",
    sorted(FORBIDDEN_FIELD_NAMES | FORBIDDEN_CAPABILITY_NAMES),
)
def test_forbidden_surface_names_are_not_declared_as_fields(forbidden: str) -> None:
    for path, tree, _ in parsed_sources():
        declared = {
            node.target.id.lower()
            for node in ast.walk(tree)
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name)
        }
        assert forbidden not in declared, (path, forbidden)
