"""
CloudShield Enterprise
Dalfox Tool
"""

from app.security.tools.common.base import BaseTool


class DalfoxTool(BaseTool):
    """
    Dalfox Wrapper
    """

    name = "dalfox"

    default_arguments = []

    timeout = 300


def get_tool():
    """
    Return Dalfox tool instance.
    """
    return DalfoxTool()