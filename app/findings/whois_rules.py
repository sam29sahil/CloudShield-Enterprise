"""
CloudShield Enterprise
WHOIS Finding Rules
"""

WHOIS_RULES = {
<<<<<<< HEAD
    "registrar": {
        "title": "Registrar Information Missing",
        "severity": "Low",
        "cvss": 2.0,
        "description": ("Registrar information could not be determined."),
        "recommendation": ("Verify WHOIS registration information."),
    },
    "expiry": {
        "title": "Domain Expiring Soon",
        "severity": "Medium",
        "cvss": 5.8,
        "description": ("The domain registration expires within 30 days."),
        "recommendation": ("Renew the domain registration."),
    },
    "privacy": {
        "title": "WHOIS Privacy Enabled",
        "severity": "Info",
        "cvss": 0.0,
        "description": ("WHOIS privacy protection is enabled."),
        "recommendation": ("No action required."),
    },
}
=======

    "registrar": {

        "title": "Registrar Information Missing",

        "severity": "Low",

        "cvss": 2.0,

        "description": (
            "Registrar information could not be determined."
        ),

        "recommendation": (
            "Verify WHOIS registration information."
        )

    },

    "expiry": {

        "title": "Domain Expiring Soon",

        "severity": "Medium",

        "cvss": 5.8,

        "description": (
            "The domain registration expires within 30 days."
        ),

        "recommendation": (
            "Renew the domain registration."
        )

    },

    "privacy": {

        "title": "WHOIS Privacy Enabled",

        "severity": "Info",

        "cvss": 0.0,

        "description": (
            "WHOIS privacy protection is enabled."
        ),

        "recommendation": (
            "No action required."
        )

    }

}
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
