"""
CloudShield Enterprise
Finding Rules
"""

RULES = [

    # ------------------------------------------
    # HTTP Security Headers
    # ------------------------------------------

    {

        "match": "content-security-policy",

        "title": "Missing Content Security Policy",

        "severity": "Medium",

        "category": "HTTP Security",

        "cvss": 6.4,

        "recommendation": "Configure the Content-Security-Policy header."

    },

    {

        "match": "x-frame-options",

        "title": "Missing X-Frame-Options Header",

        "severity": "Low",

        "category": "HTTP Security",

        "cvss": 3.5,

        "recommendation": "Enable X-Frame-Options."

    },

    {

        "match": "strict-transport-security",

        "title": "Missing HSTS Header",

        "severity": "Medium",

        "category": "HTTP Security",

        "cvss": 5.4,

        "recommendation": "Enable HSTS."

    },

    # ------------------------------------------
    # Open Ports
    # ------------------------------------------

    {

        "match": "22/tcp open",

        "title": "SSH Port Open",

        "severity": "Low",

        "category": "Network",

        "cvss": 3.9,

        "recommendation": "Restrict SSH access."

    },

    {

        "match": "21/tcp open",

        "title": "FTP Port Open",

        "severity": "Medium",

        "category": "Network",

        "cvss": 5.8,

        "recommendation": "Disable anonymous FTP."

    },

    {

        "match": "23/tcp open",

        "title": "Telnet Enabled",

        "severity": "Critical",

        "category": "Network",

        "cvss": 9.5,

        "recommendation": "Disable Telnet immediately."

    },

    {

        "match": "3389/tcp open",

        "title": "Remote Desktop Exposed",

        "severity": "High",

        "category": "Network",

        "cvss": 8.8,

        "recommendation": "Protect RDP behind VPN."

    },

    {

        "match": "445/tcp open",

        "title": "SMB Service Exposed",

        "severity": "High",

        "category": "Network",

        "cvss": 8.2,

        "recommendation": "Restrict SMB exposure."

    },

    # ------------------------------------------
    # SSL
    # ------------------------------------------

    {

        "match": "tlsv1",

        "title": "TLS 1.0 Enabled",

        "severity": "High",

        "category": "SSL",

        "cvss": 7.8,

        "recommendation": "Disable TLS 1.0."

    },

    {

        "match": "sslv3",

        "title": "SSLv3 Enabled",

        "severity": "Critical",

        "category": "SSL",

        "cvss": 9.0,

        "recommendation": "Disable SSLv3."

    },

    # ------------------------------------------
    # Web
    # ------------------------------------------

    {

        "match": "admin",

        "title": "Administrative Interface Detected",

        "severity": "Medium",

        "category": "Web",

        "cvss": 5.6,

        "recommendation": "Protect the administrative interface."

    }

]