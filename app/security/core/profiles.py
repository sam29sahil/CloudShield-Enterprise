"""
CloudShield Enterprise
Security Scan Profiles
"""

SCAN_PROFILES = {

    # =====================================================
    # Basic Website Scan
    # =====================================================

    "quick": {

        "name": "Quick Security Scan",

        "category": "basic",

        "description": "Fast website assessment.",

        "estimated_time": "30-60 sec",

        "tools": [

            "website",

            "headers",

            "ssl",

            "dns",

            "whois",

            "technology",

            "ports"

        ]

    },

    # =====================================================
    # Web Application Pentest
    # =====================================================

    "web": {

        "name": "Web Application Scan",

        "category": "web",

        "description": "Enterprise web security assessment.",

        "estimated_time": "3-10 min",

        "tools": [

            "whatweb",

            "nikto",

            "nuclei",

            "wafw00f",

            "headers",

            "ssl",

            "dnsrecon"

        ]

    },

    # =====================================================
    # Network Scan
    # =====================================================

    "network": {

        "name": "Network Assessment",

        "category": "network",

        "description": "Port discovery and service enumeration.",

        "estimated_time": "2-15 min",

        "tools": [

            "nmap",

            "rustscan",

            "masscan"

        ]

    },

    # =====================================================
    # Cloud Scan
    # =====================================================

    "cloud": {

        "name": "Cloud Security Audit",

        "category": "cloud",

        "description": "AWS / Azure / GCP security assessment.",

        "estimated_time": "5-20 min",

        "tools": [

            "prowler",

            "scoutsuite",

            "trivy"

        ]

    },

    # =====================================================
    # Wireless
    # =====================================================

    "wireless": {

        "name": "Wireless Assessment",

        "category": "wireless",

        "description": "Wireless network auditing.",

        "estimated_time": "Variable",

        "tools": [

            "aircrack",

            "wifite"

        ]

    },

    # =====================================================
    # Enterprise Full Scan
    # =====================================================

    "enterprise": {

        "name": "Enterprise Security Assessment",

        "category": "enterprise",

        "description": "Complete infrastructure assessment.",

        "estimated_time": "10-60 min",

        "tools": [

            "website",

            "headers",

            "ssl",

            "dns",

            "whois",

            "technology",

            "ports",

            "whatweb",

            "nikto",

            "nuclei",

            "wafw00f",

            "dnsrecon",

            "nmap",

            "rustscan",

            "masscan",

            "prowler",

            "scoutsuite",

            "trivy"

        ]

    }

}


def get_profile(profile):

    return SCAN_PROFILES.get(profile)


def profile_exists(profile):

    return profile in SCAN_PROFILES


def profile_tools(profile):

    data = SCAN_PROFILES.get(profile)

    if not data:

        return []

    return data["tools"]


def profiles():

    return list(SCAN_PROFILES.keys())