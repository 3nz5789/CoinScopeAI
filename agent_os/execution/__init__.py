"""Paper-only execution adapters for Phase 1."""

from .paper import PaperExecutor, PaperFill
from .ports import ExecutionPort

__all__ = ["ExecutionPort", "PaperExecutor", "PaperFill"]
