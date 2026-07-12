"""
CloudShield Enterprise
Network Security Tools
"""

from app.security.tools.network.nmap import NmapTool
from app.security.tools.network.rustscan import RustScanTool
from app.security.tools.network.masscan import MasscanTool
from app.security.tools.network.netdiscover import NetdiscoverTool


def _safe_create(tool_class):
    """
    Safely create a tool instance.
    """

    try:

        return tool_class()

    except Exception:

        return None


NETWORK_TOOLS = {}

NETWORK_TOOLS["nmap"] = _safe_create(NmapTool)

NETWORK_TOOLS["rustscan"] = _safe_create(RustScanTool)

NETWORK_TOOLS["masscan"] = _safe_create(MasscanTool)

NETWORK_TOOLS["netdiscover"] = _safe_create(NetdiscoverTool)


def get_tool(name):
    """
    Return a tool instance.
    """

    tool = NETWORK_TOOLS.get(name.lower())

    return tool


def get_all_tools():
    """
    Return all registered tools.
    """

    return {

        name: tool

        for name, tool in NETWORK_TOOLS.items()

        if tool is not None

    }


__all__ = [

    "NmapTool",

    "RustScanTool",

    "MasscanTool",

    "NetdiscoverTool",

    "NETWORK_TOOLS",

    "get_tool",

    "get_all_tools"

]