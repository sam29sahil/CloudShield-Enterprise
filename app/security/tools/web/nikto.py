"""
CloudShield Enterprise
Nikto Tool
"""

from app.security.tools.common.base import BaseTool


class NiktoTool(BaseTool):
    """
    Nikto Wrapper
    """

    name = "nikto"

<<<<<<< HEAD
    default_arguments = ["-h"]
=======
    default_arguments = [

        "-h"

    ]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    timeout = 300


def get_tool():
    """
    Return Nikto tool instance.
    """
<<<<<<< HEAD
    return NiktoTool()
=======
    return NiktoTool()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
