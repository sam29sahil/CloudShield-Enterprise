"""
CloudShield Enterprise
FFUF Tool
"""

from app.security.tools.common.base import BaseTool


class FFUFTool(BaseTool):
    """
    FFUF Wrapper
    """

    name = "ffuf"

<<<<<<< HEAD
    default_arguments = ["-u"]
=======
    default_arguments = [

        "-u"

    ]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    timeout = 300


def get_tool():
    """
    Return FFUF tool instance.
    """
<<<<<<< HEAD
    return FFUFTool()
=======
    return FFUFTool()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
