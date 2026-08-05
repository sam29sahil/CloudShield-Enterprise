"""
CloudShield Enterprise
WAFW00F Tool
"""

from app.security.tools.common.base import BaseTool


class WAFW00FTool(BaseTool):
    """
    WAFW00F Wrapper
    """

    name = "wafw00f"

    default_arguments = []

    timeout = 300


def get_tool():
    """
    Return WAFW00F tool instance.
    """
<<<<<<< HEAD
    return WAFW00FTool()
=======
    return WAFW00FTool()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
