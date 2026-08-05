"""
CloudShield Enterprise
Dirsearch Tool
"""

from app.security.tools.common.base import BaseTool


class DirsearchTool(BaseTool):
    """
    Dirsearch Wrapper
    """

    name = "dirsearch"

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
    Return Dirsearch tool instance.
    """
<<<<<<< HEAD
    return DirsearchTool()
=======
    return DirsearchTool()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
