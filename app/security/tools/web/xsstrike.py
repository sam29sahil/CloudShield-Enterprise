"""
CloudShield Enterprise
XSStrike Tool
"""

from app.security.tools.common.base import BaseTool


class XSStrikeTool(BaseTool):
    """
    XSStrike Wrapper
    """

    name = "xsstrike"

    default_arguments = []

    timeout = 300


def get_tool():
    """
    Return XSStrike tool instance.
    """
<<<<<<< HEAD
    return XSStrikeTool()
=======
    return XSStrikeTool()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
