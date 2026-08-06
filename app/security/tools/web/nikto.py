"""
CloudShield Enterprise
Nikto Tool
"""

from app.security.tools.common.base import BaseTool


class NiktoTool(BaseTool):
    """
    Nikto Wrapper
    """

    name = "nikto"

    default_arguments = [

        "-h"

    ]

    timeout = 300


def get_tool():
    """
    Return Nikto tool instance.
    """
    return NiktoTool()