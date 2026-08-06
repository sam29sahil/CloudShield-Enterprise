"""
CloudShield Enterprise
Nuclei Tool
"""

from app.security.tools.common.base import BaseTool


class NucleiTool(BaseTool):
    """
    Nuclei Wrapper
    """

    name = "nuclei"

    default_arguments = ["-u"]

    timeout = 300


def get_tool():
    """
    Return Nuclei tool instance.
    """
    return NucleiTool()
