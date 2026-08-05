"""
CloudShield Enterprise
Gobuster Tool
"""

from app.security.tools.common.base import BaseTool


class GobusterTool(BaseTool):
    """
    Gobuster Wrapper
    """

    name = "gobuster"

<<<<<<< HEAD
    default_arguments = ["dir"]
=======
    default_arguments = [

        "dir"

    ]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    timeout = 300


def get_tool():
    """
    Return Gobuster tool instance.
    """
<<<<<<< HEAD
    return GobusterTool()
=======
    return GobusterTool()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
