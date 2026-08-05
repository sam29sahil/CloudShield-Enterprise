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

<<<<<<< HEAD
    default_arguments = ["-r"]
=======
    default_arguments = [
        "-r"
    ]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    timeout = 300


def get_tool():
    """
    Return Netdiscover tool instance.
    """
<<<<<<< HEAD
    return NetdiscoverTool()
=======
    return NetdiscoverTool()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
