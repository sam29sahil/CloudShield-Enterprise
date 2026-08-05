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

<<<<<<< HEAD
    regex = re.compile(r"^([A-Za-z0-9-]+\.)+[A-Za-z]{2,}$")

    return bool(regex.match(domain))
=======
    regex = re.compile(

        r"^([A-Za-z0-9-]+\.)+[A-Za-z]{2,}$"

    )

    return bool(

        regex.match(domain)

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


def is_valid_url(url):

    try:

        parsed = urlparse(url)

<<<<<<< HEAD
        return all([parsed.scheme, parsed.netloc])
=======
        return all(

            [

                parsed.scheme,

                parsed.netloc

            ]

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    except Exception:

        return False
<<<<<<< HEAD
=======
    
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
