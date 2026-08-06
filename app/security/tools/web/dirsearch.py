"""
CloudShield Enterprise
Dirsearch Tool
"""

from app.security.tools.common.base import BaseTool


class DirsearchTool(BaseTool):
    """
    Dirsearch Wrapper
    """

    name = "dirsearch"

    default_arguments = ["-u"]

    timeout = 300


def get_tool():
    """
    Return Dirsearch tool instance.
    """
    return DirsearchTool()
