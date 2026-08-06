"""
CloudShield Enterprise
Scanner Validators
"""

import ipaddress
import re
from urllib.parse import urlparse


def validate_target(target):
    """
    Validate scan target.
    Supports:
    - Domain
    - IPv4
    - IPv6
    - URL
    """

    if target is None:
        return False

    target = target.strip()

    if target == "":
        return False

    # -----------------------
    # URL
    # -----------------------

    if target.startswith(("http://", "https://")):

        parsed = urlparse(target)

        return bool(parsed.scheme and parsed.netloc)

    # -----------------------
    # IP Address
    # -----------------------

    try:

        ipaddress.ip_address(target)

        return True

    except ValueError:

        pass

    # -----------------------
    # Domain
    # -----------------------

    pattern = (
        r"^(?!-)"
        r"([A-Za-z0-9-]{1,63}\.)+"
        r"[A-Za-z]{2,63}$"
    )

    return bool(re.fullmatch(pattern, target))