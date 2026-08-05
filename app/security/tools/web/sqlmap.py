"""
CloudShield Enterprise
SQLMap Tool
"""

from app.security.tools.common.base import BaseTool


class SQLMapTool(BaseTool):
    """
    SQLMap Wrapper
    """

    name = "sqlmap"

<<<<<<< HEAD
    default_arguments = ["--batch"]
=======
    default_arguments = [

        "--batch"

    ]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    timeout = 300


def get_tool():
    """
    Return SQLMap tool instance.
    """
<<<<<<< HEAD
    return SQLMapTool()
=======
    return SQLMapTool()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
