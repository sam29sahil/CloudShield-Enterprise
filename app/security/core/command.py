"""Safe command construction and execution for CLI scanners."""

from __future__ import annotations

from dataclasses import dataclass, field
import shlex
import subprocess
from typing import Iterable


@dataclass(frozen=True)
class Command:
    """An argv-based command. Commands are never executed through a shell."""

    executable: str
    arguments: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        if not self.executable or not isinstance(self.executable, str):
            raise ValueError("A command executable is required.")

    @classmethod
    def build(cls, executable: str, *arguments: object) -> "Command":
        values: list[str] = []
        for argument in arguments:
            if argument is None:
                continue
            if isinstance(argument, str):
                values.append(argument)
            elif isinstance(argument, Iterable):
                values.extend(str(value) for value in argument if value is not None)
            else:
                values.append(str(argument))
        return cls(executable, tuple(values))

    @property
    def argv(self) -> list[str]:
        return [self.executable, *self.arguments]

    @property
    def display(self) -> str:
        return shlex.join(self.argv)

    def run(self, *, timeout: float | None = None) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            self.argv, capture_output=True, text=True, timeout=timeout, check=False
        )
