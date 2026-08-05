"""
CloudShield Enterprise
DNS Security Tools
"""

from app.security.tools.dns.amass import AmassTool
from app.security.tools.dns.subfinder import SubfinderTool
from app.security.tools.dns.assetfinder import AssetFinderTool
from app.security.tools.dns.dnsrecon import DNSReconTool
from app.security.tools.dns.dnsenum import DNSEnumTool
from app.security.tools.dns.fierce import FierceTool

<<<<<<< HEAD
DNS_TOOLS = {
    "amass": AmassTool(),
    "subfinder": SubfinderTool(),
    "assetfinder": AssetFinderTool(),
    "dnsrecon": DNSReconTool(),
    "dnsenum": DNSEnumTool(),
    "fierce": FierceTool(),
=======

DNS_TOOLS = {

    "amass": AmassTool(),

    "subfinder": SubfinderTool(),

    "assetfinder": AssetFinderTool(),

    "dnsrecon": DNSReconTool(),

    "dnsenum": DNSEnumTool(),

    "fierce": FierceTool()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
}


def get_tool(name):

    return DNS_TOOLS.get(name.lower())


def get_all_tools():

    return DNS_TOOLS


__all__ = [
<<<<<<< HEAD
    "AmassTool",
    "SubfinderTool",
    "AssetFinderTool",
    "DNSReconTool",
    "DNSEnumTool",
    "FierceTool",
    "DNS_TOOLS",
    "get_tool",
    "get_all_tools",
]
=======

    "AmassTool",

    "SubfinderTool",

    "AssetFinderTool",

    "DNSReconTool",

    "DNSEnumTool",

    "FierceTool",

    "DNS_TOOLS",

    "get_tool",

    "get_all_tools"

]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
