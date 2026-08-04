"""Normalized, validated scan targets."""

from __future__ import annotations

from dataclasses import dataclass
import ipaddress
import re
from urllib.parse import urlparse


_HOSTNAME = re.compile(
    r"^(?=.{1,253}$)(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+"
    r"[A-Za-z]{2,63}$"
)


@dataclass(frozen=True)
class Target:
    """A scanner target with a stable value and useful metadata."""

    value: str
    kind: str
    host: str
    port: int | None = None
    scheme: str | None = None

    @classmethod
    def parse(cls, value: str) -> "Target":
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Target cannot be empty.")
        value = value.strip()
        parsed = urlparse(value)
        if parsed.scheme:
            if parsed.scheme not in {"http", "https"}:
                raise ValueError("Only HTTP and HTTPS URLs are supported.")
            if not parsed.netloc or not parsed.hostname:
                raise ValueError("Invalid URL target.")
            cls._validate_host(parsed.hostname)
            try:
                port = parsed.port
            except ValueError as error:
                raise ValueError("Invalid URL port.") from error
            return cls(value, "url", parsed.hostname, port, parsed.scheme)
        try:
            address = ipaddress.ip_address(value)
        except ValueError:
            try:
                network = ipaddress.ip_network(value, strict=False)
            except ValueError:
                cls._validate_host(value)
                return cls(value, "domain", value)
            return cls(str(network), "network", str(network.network_address))
        return cls(str(address), "ip", str(address))

    @staticmethod
    def _validate_host(host: str) -> None:
        if host.lower() == "localhost":
            return
        try:
            ipaddress.ip_address(host)
            return
        except ValueError:
            pass
        if not _HOSTNAME.fullmatch(host.rstrip(".")):
            raise ValueError("Unsupported target.")

    @classmethod
    def validate(cls, value: str) -> tuple[bool, str]:
        try:
            target = cls.parse(value)
        except (TypeError, ValueError) as error:
            return False, str(error)
        return True, target.kind

    def __str__(self) -> str:
        return self.value
