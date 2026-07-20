"""
CloudShield Enterprise
SSL/TLS Finding Rules
"""

SSL_RULES = {

    "expired": {

        "title": "Expired SSL Certificate",

        "severity": "Critical",

        "cvss": 9.5,

        "description": (
            "The SSL certificate has expired."
        ),

        "recommendation": (
            "Renew and install a valid SSL certificate immediately."
        )

    },

    "expiring": {

        "title": "SSL Certificate Expiring Soon",

        "severity": "Medium",

        "cvss": 5.8,

        "description": (
            "The SSL certificate will expire soon."
        ),

        "recommendation": (
            "Renew the certificate before expiration."
        )

    },

    "invalid": {

        "title": "Invalid SSL Certificate",

        "severity": "High",

        "cvss": 8.4,

        "description": (
            "The SSL certificate validation failed."
        ),

        "recommendation": (
            "Install a trusted SSL certificate."
        )

    },

    "self_signed": {

        "title": "Self-Signed Certificate",

        "severity": "Medium",

        "cvss": 6.2,

        "description": (
            "The server is using a self-signed certificate."
        ),

        "recommendation": (
            "Replace with a certificate issued by a trusted CA."
        )

    },

    "weak_tls": {

        "title": "Weak TLS Version",

        "severity": "High",

        "cvss": 8.0,

        "description": (
            "The server supports outdated TLS protocols."
        ),

        "recommendation": (
            "Disable TLS 1.0 and TLS 1.1. Use TLS 1.2 or TLS 1.3."
        )

    },

    "weak_cipher": {

        "title": "Weak SSL Cipher",

        "severity": "Medium",

        "cvss": 6.5,

        "description": (
            "Weak encryption ciphers are supported."
        ),

        "recommendation": (
            "Disable weak ciphers and use strong encryption suites."
        )

    }

}