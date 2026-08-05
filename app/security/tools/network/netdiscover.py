"""
CloudShield Enterprise
Netdiscover Tool
"""

from app.security.tools.common.base import BaseTool


class NetdiscoverTool(BaseTool):
    """
    Netdiscover Wrapper
    """

    name = "netdiscover"

    default_arguments = ["-r"]

    timeout = 300


def get_tool():
    """
    Return Netdiscover tool instance.
    """
    return NetdiscoverTool()
