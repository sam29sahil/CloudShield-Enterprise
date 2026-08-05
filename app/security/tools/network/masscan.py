"""
CloudShield Enterprise
Masscan Tool
"""

from app.security.tools.common.base import BaseTool


class MasscanTool(BaseTool):
    """
    Masscan Wrapper
    """

    name = "masscan"

<<<<<<< HEAD
    default_arguments = ["-p1-1000"]
=======
    default_arguments = [
        "-p1-1000"
    ]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    timeout = 300


def get_tool():
    """
    Return Masscan tool instance.
    """
<<<<<<< HEAD
    return MasscanTool()
=======
    return MasscanTool()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
