"""
CloudShield Enterprise
Target Validator
"""

import ipaddress
import re
from urllib.parse import urlparse


class TargetValidator:
    """
    Validates scan targets.
    """

    @staticmethod
    def validate(target: str):

        if not target:
            return False, "Target cannot be empty."

        target = target.strip()

        # URL
        if target.startswith(("http://", "https://")):
            parsed = urlparse(target)

            if parsed.scheme and parsed.netloc:
                return True, "url"

            return False, "Invalid URL."

        # IP Address
        try:
            ipaddress.ip_address(target)
            return True, "ip"
        except ValueError:
            pass

        # CIDR
        try:
            ipaddress.ip_network(target, strict=False)
            return True, "network"
        except ValueError:
            pass

        # Domain
        domain_pattern = (
            r"^(?!-)[A-Za-z0-9-]{1,63}"
            r"(?<!-)"
            r"(\.[A-Za-z]{2,})+$"
        )

        if re.match(domain_pattern, target):
            return True, "domain"

        return False, "Unsupported target."