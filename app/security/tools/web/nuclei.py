"""
CloudShield Enterprise
Nuclei Tool
"""

from app.security.tools.common.base import BaseTool


class NucleiTool(BaseTool):
    """
    Nuclei Wrapper
    """

    name = "nuclei"

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
    Return Nuclei tool instance.
    """
<<<<<<< HEAD
    return NucleiTool()
=======
    return NucleiTool()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
