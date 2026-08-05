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
    return ZAPTool()
