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
    return XSStrikeTool()
