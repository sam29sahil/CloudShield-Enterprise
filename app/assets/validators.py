"""
CloudShield Enterprise
Asset Validators
"""

import ipaddress

import re

from urllib.parse import urlparse


def is_valid_ip(target):

    try:

        ipaddress.ip_address(target)

        return True

    except ValueError:

        return False


def is_valid_domain(domain):

    regex = re.compile(

        r"^([A-Za-z0-9-]+\.)+[A-Za-z]{2,}$"

    )

    return bool(

        regex.match(domain)

    )


def is_valid_url(url):

    try:

        parsed = urlparse(url)

        return all(

            [

                parsed.scheme,

                parsed.netloc

            ]

        )

    except Exception:

        return False
    