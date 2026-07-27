"""
CloudShield Enterprise
DNS Finding Rules
"""

DNS_RULES = {

    "A": {

        "title": "Missing A Record",

        "severity": "Critical",

        "cvss": 8.5,

        "description": (
            "No A record was found for the domain."
        ),

        "recommendation": (
            "Configure a valid A record."
        )

    },

    "AAAA": {

        "title": "IPv6 Record Missing",

        "severity": "Info",

        "cvss": 0.0,

        "description": (
            "No IPv6 AAAA record detected."
        ),

        "recommendation": (
            "Configure IPv6 if required."
        )

    },

    "MX": {

        "title": "Missing MX Record",

        "severity": "Medium",

        "cvss": 4.5,

        "description": (
            "Mail exchange record not configured."
        ),

        "recommendation": (
            "Configure a valid MX record."
        )

    },

    "TXT": {

        "title": "Missing TXT Record",

        "severity": "Low",

        "cvss": 3.2,

        "description": (
            "TXT record is missing."
        ),

        "recommendation": (
            "Review required TXT records."
        )

    },

    "SPF": {

        "title": "Missing SPF Record",

        "severity": "Medium",

        "cvss": 5.3,

        "description": (
            "SPF email protection is not configured."
        ),

        "recommendation": (
            "Publish an SPF TXT record."
        )

    },

    "DMARC": {

        "title": "Missing DMARC Policy",

        "severity": "Medium",

        "cvss": 5.6,

        "description": (
            "DMARC protection is missing."
        ),

        "recommendation": (
            "Create a DMARC DNS policy."
        )

    },

    "DKIM": {

        "title": "Missing DKIM Record",

        "severity": "Medium",

        "cvss": 5.4,

        "description": (
            "DKIM signing is not configured."
        ),

        "recommendation": (
            "Enable DKIM for outbound mail."
        )

    }

}