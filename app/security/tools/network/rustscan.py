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

<<<<<<< HEAD
    default_arguments = ["-a"]
=======
    default_arguments = [
        "-a"
    ]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    timeout = 300


def get_tool():
    """
    Return RustScan tool instance.
    """
<<<<<<< HEAD
    return RustScanTool()
=======
    return RustScanTool()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
