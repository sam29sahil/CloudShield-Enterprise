"""
CloudShield Enterprise
Security Tool Exceptions
"""


class ToolError(Exception):
    """
    Base Tool Exception
    """
    pass


class ToolNotInstalledError(ToolError):
    """
    Tool not installed.
    """
    pass


class ScanFailedError(ToolError):
    """
    Scan failed.
    """
    pass


class ScanTimeoutError(ToolError):
    """
    Scan timeout.
    """
    pass