"""
CloudShield Enterprise
Corsy Tool
"""

from app.security.tools.common.base import BaseTool


class CorsyTool(BaseTool):
    """
    Corsy Wrapper
    """

    name = "corsy"

    default_arguments = []

    timeout = 300


def get_tool():
    """
    Return Corsy tool instance.
    """
    return CorsyTool()
