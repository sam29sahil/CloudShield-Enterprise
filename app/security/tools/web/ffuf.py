"""
CloudShield Enterprise
FFUF Tool
"""

from app.security.tools.common.base import BaseTool


class FFUFTool(BaseTool):
    """
    FFUF Wrapper
    """

    name = "ffuf"

    default_arguments = [

        "-u"

    ]

    timeout = 300


def get_tool():
    """
    Return FFUF tool instance.
    """
    return FFUFTool()