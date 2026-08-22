"""Typed Skill registry for the Phase-1 runtime."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

SkillHandler = Callable[..., Any]


@dataclass(frozen=True)
class Skill:
    """A named runtime capability with no implicit provider permissions."""

    name: str
    description: str
    handler: SkillHandler | None = None
    read_only: bool = True


class SkillRegistry:
    """Explicit registry; unknown Skills fail rather than being guessed."""

    def __init__(self) -> None:
        self._skills: dict[str, Skill] = {}

    def register(self, skill: Skill) -> None:
        if not skill.name.strip():
            raise ValueError("Skill name must not be empty")
        if skill.name in self._skills:
            raise ValueError(f"Skill already registered: {skill.name}")
        self._skills[skill.name] = skill

    def get(self, name: str) -> Skill:
        try:
            return self._skills[name]
        except KeyError as exc:
            raise KeyError(f"Unknown Skill: {name}") from exc

    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._skills))
