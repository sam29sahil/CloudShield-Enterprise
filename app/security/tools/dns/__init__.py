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

DNS_TOOLS = {
    "amass": AmassTool(),
    "subfinder": SubfinderTool(),
    "assetfinder": AssetFinderTool(),
    "dnsrecon": DNSReconTool(),
    "dnsenum": DNSEnumTool(),
    "fierce": FierceTool(),
}


def get_tool(name):

    return DNS_TOOLS.get(name.lower())


def get_all_tools():

    return DNS_TOOLS


__all__ = [
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
