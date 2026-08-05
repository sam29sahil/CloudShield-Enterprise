"""
CloudShield Enterprise
Cloud Security Tools
"""

from app.security.tools.cloud.prowler import ProwlerTool
from app.security.tools.cloud.scoutsuite import ScoutSuiteTool
from app.security.tools.cloud.cloudsplaining import CloudSplainingTool
from app.security.tools.cloud.trivy import TrivyTool

<<<<<<< HEAD
CLOUD_TOOLS = {
    "prowler": ProwlerTool(),
    "scoutsuite": ScoutSuiteTool(),
    "cloudsplaining": CloudSplainingTool(),
    "trivy": TrivyTool(),
=======

CLOUD_TOOLS = {

    "prowler": ProwlerTool(),

    "scoutsuite": ScoutSuiteTool(),

    "cloudsplaining": CloudSplainingTool(),

    "trivy": TrivyTool()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
}


def get_tool(name):

    return CLOUD_TOOLS.get(name.lower())


def get_all_tools():

    return CLOUD_TOOLS


__all__ = [
<<<<<<< HEAD
    "ProwlerTool",
    "ScoutSuiteTool",
    "CloudSplainingTool",
    "TrivyTool",
    "CLOUD_TOOLS",
    "get_tool",
    "get_all_tools",
]
=======

    "ProwlerTool",

    "ScoutSuiteTool",

    "CloudSplainingTool",

    "TrivyTool",

    "CLOUD_TOOLS",

    "get_tool",

    "get_all_tools"

]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
