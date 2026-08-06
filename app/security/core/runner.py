"""Enterprise command runner for CloudShield's registered CLI security tools.

Execution flow
==============
``Runner.run(tool, arguments)`` accepts a tool name from :data:`TOOLS` and a
sequence of already-tokenized arguments.  It rejects unknown tools and invalid
arguments, resolves the configured binary with :func:`shutil.which`, then runs
the resolved executable with ``subprocess.run(shell=False)``.  Standard output,
standard error, the process return code, and elapsed time are captured for every
outcome.  No command string is evaluated by a shell, so arguments are data and
cannot introduce shell operators or expansions.

Return value
============
Every invocation returns this stable mapping, including validation, missing
binary, timeout, and unexpected-error paths::

    {
        "success": bool,
        "stdout": str,
        "stderr": str,
        "return_code": int | None,
        "execution_time": float,
        "command": str,
        "error": str,
    }

``success`` is true only when the command exits with return code zero.
``command`` is an escaped display representation of the argv passed to
``subprocess.run``; it is intended for logs and diagnostics, not execution.

Adding a tool
=============
First implement and register the scanner in one of the existing CloudShield
tool registries.  Only then add its registered name to :data:`TOOLS` with the
exact executable name and a bounded timeout.  Do not add aliases, arbitrary
commands, or tools that are not implemented and registered by the project.
In-process basic scanners (website, headers, SSL, DNS, WHOIS, ports, and
technology) intentionally do not belong here because they have no CLI binary.
"""

from __future__ import annotations

import logging
import shutil
import subprocess
from time import perf_counter
from typing import Any, Mapping, Sequence

from app.security.core.command import Command
from app.security.core.result import Result

logger = logging.getLogger(__name__)


# This allowlist is derived from the existing network, web, SSL, DNS, cloud,
# and wireless tool registries.  It deliberately excludes the in-process basic
# scanners, which are registered elsewhere but are not executable commands.
TOOLS: Mapping[str, Mapping[str, Any]] = {
    # Network
    "nmap": {"binary": "nmap", "timeout": 600},
    "rustscan": {"binary": "rustscan", "timeout": 300},
    "masscan": {"binary": "masscan", "timeout": 600},
    "netdiscover": {"binary": "netdiscover", "timeout": 300},
    # Web
    "whatweb": {"binary": "whatweb", "timeout": 300},
    "nikto": {"binary": "nikto", "timeout": 300},
    "nuclei": {"binary": "nuclei", "timeout": 300},
    "gobuster": {"binary": "gobuster", "timeout": 300},
    "ffuf": {"binary": "ffuf", "timeout": 300},
    "dirsearch": {"binary": "dirsearch", "timeout": 300},
    "sqlmap": {"binary": "sqlmap", "timeout": 300},
    "zap": {"binary": "zap", "timeout": 300},
    "dalfox": {"binary": "dalfox", "timeout": 300},
    "xsstrike": {"binary": "xsstrike", "timeout": 300},
    "wafw00f": {"binary": "wafw00f", "timeout": 300},
    "corsy": {"binary": "corsy", "timeout": 300},
    # SSL/TLS
    "sslyze": {"binary": "sslyze", "timeout": 300},
    "testssl": {"binary": "testssl", "timeout": 300},
    "openssl": {"binary": "openssl", "timeout": 300},
    # DNS
    "amass": {"binary": "amass", "timeout": 300},
    "subfinder": {"binary": "subfinder", "timeout": 300},
    "assetfinder": {"binary": "assetfinder", "timeout": 300},
    "dnsrecon": {"binary": "dnsrecon", "timeout": 300},
    "dnsenum": {"binary": "dnsenum", "timeout": 300},
    "fierce": {"binary": "fierce", "timeout": 300},
    # Cloud
    "prowler": {"binary": "prowler", "timeout": 300},
    "scoutsuite": {"binary": "scoutsuite", "timeout": 300},
    "cloudsplaining": {"binary": "cloudsplaining", "timeout": 300},
    "trivy": {"binary": "trivy", "timeout": 300},
    # Wireless
    "aircrack-ng": {"binary": "aircrack-ng", "timeout": 300},
    "airodump-ng": {"binary": "airodump-ng", "timeout": 300},
    "aireplay-ng": {"binary": "aireplay-ng", "timeout": 300},
    "wifite": {"binary": "wifite", "timeout": 300},
}


class Runner:
    """Execute only CLI tools defined by the CloudShield tool allowlist."""

    tools = TOOLS

    def run(self, tool: str, arguments: Sequence[str] | None = None) -> dict[str, Any]:
        """Run one registered scanner command and return a normalized result."""
        started = perf_counter()
        normalized_tool = tool.lower().strip() if isinstance(tool, str) else ""
        config = self.tools.get(normalized_tool)
        if config is None:
            return self._failure(
                started,
                error="Tool is not registered for command execution.",
            )

        try:
            argv_arguments = self._arguments(arguments)
        except (TypeError, ValueError) as error:
            return self._failure(started, error=str(error))

        binary = config["binary"]
        executable = shutil.which(binary)
        if executable is None:
            logger.warning(
                "Registered security tool is not installed: %s", normalized_tool
            )
            return self._failure(
                started,
                command=binary,
                error=f"{binary} is not installed or is not on PATH.",
            )

        command = Command.build(executable, argv_arguments)
        timeout = config["timeout"]
        logger.info("Executing security tool %s", normalized_tool)

        try:
            completed = command.run(timeout=timeout)
        except subprocess.TimeoutExpired as error:
            logger.warning(
                "Security tool %s timed out after %s seconds", normalized_tool, timeout
            )
            return self._failure(
                started,
                command=display_command,
                stdout=self._text(error.stdout),
                stderr=self._text(error.stderr),
                error=f"{normalized_tool} timed out after {timeout} seconds.",
            )
        except OSError as error:
            logger.exception("Security tool %s could not be executed", normalized_tool)
            return self._failure(started, command=display_command, error=str(error))
        except Exception as error:  # Defensive boundary for scanner execution.
            logger.exception("Unexpected runner failure for %s", normalized_tool)
            return self._failure(started, command=display_command, error=str(error))

        elapsed = self._elapsed(started)
        success = completed.returncode == 0
        error = (
            ""
            if success
            else (
                completed.stderr.strip()
                or f"{normalized_tool} exited with code {completed.returncode}."
            )
        )
        logger.info(
            "Security tool %s completed with return code %s in %.3fs",
            normalized_tool,
            completed.returncode,
            elapsed,
        )
        return Result(
            success=success,
            tool=normalized_tool,
            target="",
            command=command.display,
            return_code=completed.returncode,
            stdout=completed.stdout,
            stderr=completed.stderr,
            data={"execution_time": elapsed},
            error=error,
        ).to_dict()

    @staticmethod
    def _arguments(arguments: Sequence[str] | None) -> list[str]:
        if arguments is None:
            return []
        if isinstance(arguments, (str, bytes)) or not isinstance(arguments, Sequence):
            raise TypeError("arguments must be a sequence of argument strings.")
        if any(
            not isinstance(argument, str) or "\x00" in argument
            for argument in arguments
        ):
            raise ValueError("arguments must contain only strings without NUL bytes.")
        return list(arguments)

    @staticmethod
    def _text(value: str | bytes | None) -> str:
        if isinstance(value, bytes):
            return value.decode(errors="replace")
        return value or ""

    @staticmethod
    def _elapsed(started: float) -> float:
        return round(perf_counter() - started, 3)

    def _failure(
        self,
        started: float,
        *,
        error: str,
        command: str = "",
        stdout: str = "",
        stderr: str = "",
    ) -> dict[str, Any]:
        return Result(
            success=False,
            tool=normalized_tool,
            target="",
            command=command.display if command else "",
            stdout=stdout,
            stderr=stderr,
            error=error,
        ).to_dict()


__all__ = ["Runner", "TOOLS"]
