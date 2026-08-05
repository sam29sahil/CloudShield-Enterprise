"""
CloudShield Enterprise
OWASP ZAP Tool
"""

from app.security.tools.common.base import BaseTool


class ZAPTool(BaseTool):
    """
    OWASP ZAP Wrapper
    """

    name = "zap"

    default_arguments = []

    timeout = 300


def get_tool():
    """
    Return ZAP tool instance.
    """
<<<<<<< HEAD
    return ZAPTool()
=======
    return ZAPTool()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
