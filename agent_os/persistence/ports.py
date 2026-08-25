"""Metadata-only A1 ports; concrete adapters are outside this milestone."""

from __future__ import annotations

from typing import Protocol

from .contracts import (
    IngressBinding,
    IngressReceipt,
    ReceiptCommitResult,
    RedactedIngressReceipt,
)


class MetadataReceiptPort(Protocol):
    """Future tenant-scoped receipt coordination surface."""

    def lookup_receipt(self, binding: IngressBinding) -> IngressReceipt | None:
        """Return only a receipt bound to the trusted tenant and full identity."""
        ...

    def commit_receipt(self, receipt: IngressReceipt) -> ReceiptCommitResult:
        """Return a logical create/replay/conflict outcome without implementing it."""
        ...


class ReceiptRedactionPort(Protocol):
    """Future pure whitelist projection surface."""

    def redact_receipt(self, receipt: IngressReceipt) -> RedactedIngressReceipt:
        """Project an internal metadata receipt to its safe review shape."""
        ...
