"""
CloudShield Enterprise
RustScan Tool
"""

from app.security.tools.common.base import BaseTool


class RustScanTool(BaseTool):
    """
    RustScan Wrapper
    """

    name = "rustscan"

    default_arguments = [
        "-a"
    ]

    timeout = 300


def get_tool():
    """
    Return RustScan tool instance.
    """
    return RustScanTool()