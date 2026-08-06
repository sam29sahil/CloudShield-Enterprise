"""Parser for turning scanner results into the platform's stable response shape."""

from __future__ import annotations

import json
from typing import Any, Mapping

from app.security.core.result import Result


class Parser:
    """Normalize old mapping-based tools and new :class:`Result` values."""

    def parse(
        self,
        tool: str,
        target: str,
        result: Result | Mapping[str, Any] | None,
        execution_time: float = 0,
    ) -> dict[str, Any]:
        raw = result.to_dict() if isinstance(result, Result) else dict(result or {})
        success = bool(raw.get("success", False))
        error = raw.get("stderr") or raw.get("error", "")
        return {
            "success": success,
            "tool": tool,
            "target": target,
            "summary": self.summary(raw, execution_time),
            "website": raw.get("website", {}),
            "headers": raw.get("headers", []),
            "ssl": raw.get("ssl", {}),
            "dns": raw.get("dns", {}),
            "whois": raw.get("whois", {}),
            "technology": raw.get("technology", []),
            "ports": raw.get("ports", []),
            "findings": self.findings(raw),
            "raw_output": raw,
            "command": raw.get("command", ""),
            "return_code": raw.get("return_code", 0),
            "execution_time": execution_time,
            "error": error,
        }

    @staticmethod
    def lines(output: object) -> list[str]:
        return [line.strip() for line in str(output or "").splitlines() if line.strip()]

    def summary(
        self, result: Mapping[str, Any], execution_time: float
    ) -> dict[str, Any]:
        success = bool(result.get("success", False))
        return {
            "status": "Completed" if success else "Failed",
            "message": (
                "Scan completed successfully."
                if success
                else (result.get("error") or result.get("stderr") or "Unknown error")
            ),
            "score": result.get("score", 0),
            "risk": result.get("risk", "Unknown"),
            "execution_time": execution_time,
            "return_code": result.get("return_code", 0),
        }

    def findings(self, result: Mapping[str, Any]) -> list[Any]:
        findings = result.get("findings")
        if isinstance(findings, list):
            return findings
        return self.lines(result.get("stdout", ""))

    @staticmethod
    def json(value: str, default: Any = None) -> Any:
        try:
            return json.loads(value)
        except (TypeError, ValueError):
            return {} if default is None else default
