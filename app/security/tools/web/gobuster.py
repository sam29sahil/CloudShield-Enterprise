"""
CloudShield Enterprise
Gobuster Tool
"""

from app.security.tools.common.base import BaseTool


class GobusterTool(BaseTool):
    """
    Gobuster Wrapper
    """

    name = "gobuster"

    default_arguments = [

        "dir"

    ]

    timeout = 300


def get_tool():
    """
    Return Gobuster tool instance.
    """
    return GobusterTool()