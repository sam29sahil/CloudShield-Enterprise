"""
CloudShield Enterprise
Dalfox Tool
"""

from app.security.tools.common.base import BaseTool


class DalfoxTool(BaseTool):
    """
    Dalfox Wrapper
    """

    name = "dalfox"

    default_arguments = []

    timeout = 300


def get_tool():
    """
    Return Dalfox tool instance.
    """
<<<<<<< HEAD
    return DalfoxTool()
=======
    return DalfoxTool()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
