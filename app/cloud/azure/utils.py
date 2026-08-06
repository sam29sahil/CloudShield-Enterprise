"""
CloudShield Enterprise
Azure Utilities
"""


def safe_value(value, default="-"):

    if value is None:

        return default

    return value


def safe_list(value):

    if value is None:

        return []

    return value
