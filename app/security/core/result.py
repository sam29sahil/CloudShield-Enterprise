"""Canonical result value returned by scanner implementations."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Result:
    success: bool
    tool: str
    target: str
    command: str = ""
    return_code: int | None = None
    stdout: str = ""
    stderr: str = ""
    data: dict[str, Any] = field(default_factory=dict)
    findings: list[dict[str, Any]] = field(default_factory=list)
    error: str = ""

    def to_dict(self) -> dict[str, Any]:
        payload = {"success": self.success, "tool": self.tool, "target": self.target,
                   "command": self.command, "return_code": self.return_code,
                   "stdout": self.stdout, "stderr": self.stderr, "findings": self.findings,
                   "error": self.error or self.stderr}
        payload.update(self.data)
        return payload
