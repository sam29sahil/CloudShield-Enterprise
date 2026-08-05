"""
CloudShield Enterprise
Result Adapters
"""

from app.security.adapters.cli import CLIAdapter
from app.security.adapters.nmap import NmapAdapter

<<<<<<< HEAD
ADAPTERS = {
    "nmap": NmapAdapter(),
    "rustscan": CLIAdapter(),
    "masscan": CLIAdapter(),
    "netdiscover": CLIAdapter(),
    "whatweb": CLIAdapter(),
    "nikto": CLIAdapter(),
    "nuclei": CLIAdapter(),
    "gobuster": CLIAdapter(),
    "ffuf": CLIAdapter(),
    "dirsearch": CLIAdapter(),
    "sqlmap": CLIAdapter(),
    "zap": CLIAdapter(),
    "dalfox": CLIAdapter(),
    "xsstrike": CLIAdapter(),
    "wafw00f": CLIAdapter(),
    "corsy": CLIAdapter(),
    "sslyze": CLIAdapter(),
    "testssl": CLIAdapter(),
    "openssl": CLIAdapter(),
    "amass": CLIAdapter(),
    "subfinder": CLIAdapter(),
    "assetfinder": CLIAdapter(),
    "dnsrecon": CLIAdapter(),
    "dnsenum": CLIAdapter(),
    "fierce": CLIAdapter(),
    "trivy": CLIAdapter(),
    "prowler": CLIAdapter(),
    "scoutsuite": CLIAdapter(),
    "cloudsplaining": CLIAdapter(),
    "aircrack-ng": CLIAdapter(),
    "airodump-ng": CLIAdapter(),
    "aireplay-ng": CLIAdapter(),
    "wifite": CLIAdapter(),
=======

ADAPTERS = {

    "nmap": NmapAdapter(),

    "rustscan": CLIAdapter(),

    "masscan": CLIAdapter(),

    "netdiscover": CLIAdapter(),

    "whatweb": CLIAdapter(),

    "nikto": CLIAdapter(),

    "nuclei": CLIAdapter(),

    "gobuster": CLIAdapter(),

    "ffuf": CLIAdapter(),

    "dirsearch": CLIAdapter(),

    "sqlmap": CLIAdapter(),

    "zap": CLIAdapter(),

    "dalfox": CLIAdapter(),

    "xsstrike": CLIAdapter(),

    "wafw00f": CLIAdapter(),

    "corsy": CLIAdapter(),

    "sslyze": CLIAdapter(),

    "testssl": CLIAdapter(),

    "openssl": CLIAdapter(),

    "amass": CLIAdapter(),

    "subfinder": CLIAdapter(),

    "assetfinder": CLIAdapter(),

    "dnsrecon": CLIAdapter(),

    "dnsenum": CLIAdapter(),

    "fierce": CLIAdapter(),

    "trivy": CLIAdapter(),

    "prowler": CLIAdapter(),

    "scoutsuite": CLIAdapter(),

    "cloudsplaining": CLIAdapter(),

    "aircrack-ng": CLIAdapter(),

    "airodump-ng": CLIAdapter(),

    "aireplay-ng": CLIAdapter(),

    "wifite": CLIAdapter()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
}


def get_adapter(tool):

<<<<<<< HEAD
    return ADAPTERS.get(tool.lower())
=======
    return ADAPTERS.get(tool.lower())
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
