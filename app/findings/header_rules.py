"""
CloudShield Enterprise
HTTP Security Header Rules
"""

HEADER_RULES = {

    "Content-Security-Policy": {

        "title": "Missing Content Security Policy",

        "severity": "High",

        "category": "HTTP Security",

        "cvss": 7.4,

        "description": (
            "The application does not define a "
            "Content Security Policy."
        ),

        "recommendation": (
            "Implement a strict Content-Security-Policy header."
        )

    },

    "Strict-Transport-Security": {

        "title": "Missing HSTS Header",

        "severity": "High",

        "category": "HTTP Security",

        "cvss": 7.2,

        "description": (
            "HTTP Strict Transport Security "
            "is not enabled."
        ),

        "recommendation": (
            "Enable Strict-Transport-Security."
        )

    },

    "X-Frame-Options": {

        "title": "Clickjacking Protection Missing",

        "severity": "Medium",

        "category": "HTTP Security",

        "cvss": 5.3,

        "description": (
            "The application is vulnerable "
            "to clickjacking attacks."
        ),

        "recommendation": (
            "Set X-Frame-Options: DENY or SAMEORIGIN."
        )

    },

    "X-Content-Type-Options": {

        "title": "MIME Sniffing Protection Missing",

        "severity": "Medium",

        "category": "HTTP Security",

        "cvss": 5.0,

        "description": (
            "The browser may MIME-sniff responses."
        ),

        "recommendation": (
            "Enable X-Content-Type-Options: nosniff."
        )

    },

    "Referrer-Policy": {

        "title": "Missing Referrer Policy",

        "severity": "Low",

        "category": "HTTP Security",

        "cvss": 3.5,

        "description": (
            "Referrer information may leak."
        ),

        "recommendation": (
            "Configure a Referrer-Policy header."
        )

    },

    "Permissions-Policy": {

        "title": "Missing Permissions Policy",

        "severity": "Low",

        "category": "HTTP Security",

        "cvss": 3.0,

        "description": (
            "Browser permissions are not restricted."
        ),

        "recommendation": (
            "Implement a Permissions-Policy header."
        )

    }

}