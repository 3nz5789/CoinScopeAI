"""Inspectable strategy graph primitives."""

from __future__ import annotations

from dataclasses import dataclass

from agent_os.contracts import NodeKind, StrategyDocument, StrategyNode

REQUIRED_NODE_KINDS = (
    NodeKind.SCHEDULE,
    NodeKind.MARKET,
    NodeKind.CONDITION,
    NodeKind.ENTRY,
    NodeKind.RISK,
    NodeKind.EXIT,
)


@dataclass(frozen=True)
class GraphValidation:
    """Validation result used by API and UI surfaces."""

    valid: bool
    missing_kinds: tuple[str, ...] = ()
    missing_fields: tuple[str, ...] = ()
    errors: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, object]:
        return {
            "valid": self.valid,
            "missing_kinds": list(self.missing_kinds),
            "missing_fields": list(self.missing_fields),
            "errors": list(self.errors),
        }


class AgentGraph:
    """A thin graph view over the portable strategy document."""

    def __init__(self, document: StrategyDocument) -> None:
        self.document = document
        self.nodes = tuple(document.nodes)

    def validate(self) -> GraphValidation:
        present = {node.kind for node in self.nodes}
        missing = tuple(kind.value for kind in REQUIRED_NODE_KINDS if kind not in present)
        errors: list[str] = []
        missing_fields = tuple(self.document.missing_fields)
        if missing_fields:
            errors.append("Required draft fields missing: " + ", ".join(missing_fields))
        if self.document.mode != "paper":
            errors.append("Phase 1 only permits paper mode")
        return GraphValidation(
            valid=not missing and not missing_fields and not errors,
            missing_kinds=missing,
            missing_fields=missing_fields,
            errors=tuple(errors),
        )

    def summary(self) -> list[dict[str, str]]:
        return [
            {
                "id": node.id,
                "kind": node.kind.value,
                "title": node.title,
                "detail": node.detail,
            }
            for node in self.nodes
        ]


def node(kind: NodeKind, title: str, detail: str, index: int, tone: str = "blue") -> StrategyNode:
    """Create stable IDs for deterministic graph previews."""
    return StrategyNode(
        id=f"{kind.value}-{index}", kind=kind, title=title, detail=detail, tone=tone
    )
