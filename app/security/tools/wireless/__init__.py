"""
CloudShield Enterprise
Wireless Security Tools
"""

from app.security.tools.wireless.aircrack import AircrackTool
from app.security.tools.wireless.airodump import AirodumpTool
from app.security.tools.wireless.aireplay import AireplayTool
from app.security.tools.wireless.wifite import WifiteTool


WIRELESS_TOOLS = {

    "aircrack-ng": AircrackTool(),

    "airodump-ng": AirodumpTool(),

    "aireplay-ng": AireplayTool(),

    "wifite": WifiteTool()

}


def get_tool(name):
    """
    Return a wireless tool.
    """

    return WIRELESS_TOOLS.get(name.lower())


def get_all_tools():
    """
    Return all wireless tools.
    """

    return WIRELESS_TOOLS


__all__ = [

    "AircrackTool",

    "AirodumpTool",

    "AireplayTool",

    "WifiteTool",

    "WIRELESS_TOOLS",

    "get_tool",

    "get_all_tools"

]