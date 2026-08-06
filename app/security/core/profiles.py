"""
CloudShield Enterprise
Scan Profiles
"""

SCAN_PROFILES = {
    "quick": ["headers", "ssl", "whatweb"],
    "web": ["whatweb", "nikto", "nuclei", "wafw00f", "headers", "ssl", "dnsrecon"],
    "network": ["nmap", "rustscan", "masscan"],
    "cloud": ["prowler", "scoutsuite", "trivy"],
    "wireless": ["aircrack", "wifite"],
    "full_enterprise": [
        "whatweb",
        "nikto",
        "nuclei",
        "wafw00f",
        "headers",
        "ssl",
        "dnsrecon",
        "nmap",
        "rustscan",
        "masscan",
        "prowler",
        "scoutsuite",
        "trivy",
    ],
}
