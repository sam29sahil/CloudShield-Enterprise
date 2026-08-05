"""
CloudShield Enterprise
Masscan Tool
"""

from app.security.tools.common.base import BaseTool


class MasscanTool(BaseTool):
    """
    Masscan Wrapper
    """

    name = "masscan"

    default_arguments = ["-p1-1000"]

    timeout = 300


def get_tool():
    """
    Return Masscan tool instance.
    """
    return MasscanTool()
