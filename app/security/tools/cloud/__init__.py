"""
CloudShield Enterprise
Cloud Security Tools
"""

from app.security.tools.cloud.prowler import ProwlerTool
from app.security.tools.cloud.scoutsuite import ScoutSuiteTool
from app.security.tools.cloud.cloudsplaining import CloudSplainingTool
from app.security.tools.cloud.trivy import TrivyTool


CLOUD_TOOLS = {

    "prowler": ProwlerTool(),

    "scoutsuite": ScoutSuiteTool(),

    "cloudsplaining": CloudSplainingTool(),

    "trivy": TrivyTool()

}


def get_tool(name):

    return CLOUD_TOOLS.get(name.lower())


def get_all_tools():

    return CLOUD_TOOLS


__all__ = [

    "ProwlerTool",

    "ScoutSuiteTool",

    "CloudSplainingTool",

    "TrivyTool",

    "CLOUD_TOOLS",

    "get_tool",

    "get_all_tools"

]