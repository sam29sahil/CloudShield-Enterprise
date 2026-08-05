"""
CloudShield Enterprise
Corsy Tool
"""

from app.security.tools.common.base import BaseTool


class CorsyTool(BaseTool):
    """
    Corsy Wrapper
    """

    name = "corsy"

    default_arguments = []

    timeout = 300


def get_tool():
    """
    Return Corsy tool instance.
    """
<<<<<<< HEAD
    return CorsyTool()
=======
    return CorsyTool()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
