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

<<<<<<< HEAD
        return bool(re.match(pattern, target))
=======
        return bool(

            re.match(

                pattern,

                target

            )

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @staticmethod
    def validate_tool(tool, manager):

        return manager.installed(tool)

    @staticmethod
    def validate_arguments(arguments):

        if arguments is None:

            return True

<<<<<<< HEAD
        return isinstance(arguments, list)
=======
        return isinstance(

            arguments,

            list

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
