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

<<<<<<< HEAD
    return value
=======
    return value
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
