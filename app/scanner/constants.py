"""
CloudShield Enterprise
Scanner Tool Constants
"""

QUICK_TOOLS = {

    "web": [
        "whois",
        "dns",
        "headers",
        "ssl"
    ],

    "network": [
        "ping",
        "port_scan"
    ]

}

DEEP_TOOLS = {

    "web": [
        "whois",
        "dns",
        "headers",
        "ssl",
        "nmap",
        "nikto",
        "whatweb",
        "nuclei"
    ],

    "network": [
        "ping",
        "port_scan",
        "service_detection",
        "os_detection"
    ]

}