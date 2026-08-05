"""
CloudShield Enterprise
Security Utilities
"""

import ipaddress
import socket
import uuid
from datetime import datetime


def validate_target(target):
    """
    Validate hostname or IP address.
    """

    try:

        ipaddress.ip_address(target)

        return True

    except ValueError:

        try:

            socket.gethostbyname(target)

            return True

        except socket.error:

            return False


def resolve_ip(target):
    """
    Resolve hostname to IP.
    """

    try:

        return socket.gethostbyname(target)

    except Exception:

        return None


def timestamp():
    """
    Current UTC timestamp.
    """

    return datetime.utcnow()


def generate_scan_id():
    """
    Unique scan ID.
    """

    return str(uuid.uuid4())


def normalize_target(target):
    """
    Normalize user input.
    """

    target = target.strip()

<<<<<<< HEAD
    target = target.replace("https://", "")

    target = target.replace("http://", "")

    target = target.strip("/")

    return target
=======
    target = target.replace(
        "https://",
        ""
    )

    target = target.replace(
        "http://",
        ""
    )

    target = target.strip("/")

    return target
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
