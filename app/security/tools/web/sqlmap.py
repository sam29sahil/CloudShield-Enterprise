"""
CloudShield Enterprise
SQLMap Tool
"""

from app.security.tools.common.base import BaseTool


class SQLMapTool(BaseTool):
    """
    SQLMap Wrapper
    """

    name = "sqlmap"

    default_arguments = ["--batch"]

    timeout = 300


def get_tool():
    """
    Return SQLMap tool instance.
    """
    return SQLMapTool()
