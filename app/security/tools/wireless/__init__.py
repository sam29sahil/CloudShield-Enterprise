"""
CloudShield Enterprise
Wireless Security Tools
"""

from app.security.tools.wireless.aircrack import AircrackTool
from app.security.tools.wireless.airodump import AirodumpTool
from app.security.tools.wireless.aireplay import AireplayTool
from app.security.tools.wireless.wifite import WifiteTool

<<<<<<< HEAD
WIRELESS_TOOLS = {
    "aircrack-ng": AircrackTool(),
    "airodump-ng": AirodumpTool(),
    "aireplay-ng": AireplayTool(),
    "wifite": WifiteTool(),
=======

WIRELESS_TOOLS = {

    "aircrack-ng": AircrackTool(),

    "airodump-ng": AirodumpTool(),

    "aireplay-ng": AireplayTool(),

    "wifite": WifiteTool()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
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
<<<<<<< HEAD
    "AircrackTool",
    "AirodumpTool",
    "AireplayTool",
    "WifiteTool",
    "WIRELESS_TOOLS",
    "get_tool",
    "get_all_tools",
]
=======

    "AircrackTool",

    "AirodumpTool",

    "AireplayTool",

    "WifiteTool",

    "WIRELESS_TOOLS",

    "get_tool",

    "get_all_tools"

]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
