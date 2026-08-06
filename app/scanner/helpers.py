"""
CloudShield Enterprise
Scanner Helpers
"""

from app.scanner.constants import QUICK_TOOLS, DEEP_TOOLS


def get_tools(category, mode="quick"):

    if mode == "quick":

        tools = QUICK_TOOLS

    else:

        tools = DEEP_TOOLS

    return [

        (

            tool,

            tool.replace("_", " ").title()

        )

        for tool in tools.get(

            category,

            []

        )

    ]