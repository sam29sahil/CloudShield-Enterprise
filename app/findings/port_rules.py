"""
CloudShield Enterprise
Network Port Rules
"""

PORT_RULES = {
    20: {
        "title": "FTP Data Port Exposed",
        "severity": "Medium",
        "cvss": 5.0,
        "recommendation": ("Restrict FTP access or disable if unused."),
    },
    21: {
        "title": "FTP Service Exposed",
        "severity": "Medium",
        "cvss": 5.5,
        "recommendation": ("Disable anonymous FTP and restrict access."),
    },
    22: {
        "title": "SSH Service Exposed",
        "severity": "Low",
        "cvss": 3.7,
        "recommendation": ("Restrict SSH to trusted IP addresses."),
    },
    23: {
        "title": "Telnet Service Enabled",
        "severity": "Critical",
        "cvss": 9.8,
        "recommendation": ("Disable Telnet immediately and use SSH."),
    },
    25: {
        "title": "SMTP Service Exposed",
        "severity": "Medium",
        "cvss": 5.2,
        "recommendation": ("Restrict SMTP relay and monitor usage."),
    },
    53: {
        "title": "DNS Service Exposed",
        "severity": "Low",
        "cvss": 2.9,
        "recommendation": ("Restrict recursive DNS queries."),
    },
    80: {
        "title": "HTTP Service Detected",
        "severity": "Info",
        "cvss": 0.0,
        "recommendation": ("Redirect HTTP traffic to HTTPS."),
    },
    110: {
        "title": "POP3 Service Exposed",
        "severity": "Medium",
        "cvss": 4.8,
        "recommendation": ("Use POP3S or disable POP3."),
    },
    143: {
        "title": "IMAP Service Exposed",
        "severity": "Medium",
        "cvss": 4.8,
        "recommendation": ("Use IMAPS and restrict access."),
    },
    443: {
        "title": "HTTPS Service Detected",
        "severity": "Info",
        "cvss": 0.0,
        "recommendation": ("Verify TLS configuration and certificate."),
    },
    3306: {
        "title": "MySQL Database Exposed",
        "severity": "High",
        "cvss": 8.2,
        "recommendation": ("Restrict MySQL to internal hosts only."),
    },
    3389: {
        "title": "Remote Desktop Exposed",
        "severity": "High",
        "cvss": 8.8,
        "recommendation": ("Protect RDP using VPN and MFA."),
    },
    5432: {
        "title": "PostgreSQL Database Exposed",
        "severity": "High",
        "cvss": 8.0,
        "recommendation": ("Restrict PostgreSQL network access."),
    },
    8080: {
        "title": "Alternate HTTP Service Exposed",
        "severity": "Low",
        "cvss": 3.5,
        "recommendation": ("Review alternate web service exposure."),
    },
}
