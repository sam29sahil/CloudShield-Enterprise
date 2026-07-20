"""
CloudShield Enterprise
Scan Validator
"""

import ipaddress
import re
from urllib.parse import urlparse


class ScanValidator:
    """
    Validate scan requests.
    """

    @staticmethod
    def validate_target(target):

        if not target:

            return False

        target = target.strip()

        # URL

        if target.startswith("http://") or target.startswith("https://"):

            parsed = urlparse(target)

            return bool(parsed.netloc)

        # IP Address

        try:

            ipaddress.ip_address(target)

            return True

        except ValueError:

            pass

        # Domain Name

        pattern = r"^([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"

        return bool(

            re.match(

                pattern,

                target

            )

        )

    @staticmethod
    def validate_tool(tool, manager):

        return manager.installed(tool)

    @staticmethod
    def validate_arguments(arguments):

        if arguments is None:

            return True

        return isinstance(

            arguments,

            list

        )