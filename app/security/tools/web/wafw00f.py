"""
CloudShield Enterprise
WAFW00F Tool
"""

from app.security.tools.common.base import BaseTool


class WAFW00FTool(BaseTool):
    """
    WAFW00F Wrapper
    """

    name = "wafw00f"

    default_arguments = []

    timeout = 300


def get_tool():
    """
    Return WAFW00F tool instance.
    """
    return WAFW00FTool()
