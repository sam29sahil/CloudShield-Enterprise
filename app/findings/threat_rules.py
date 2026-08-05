"""
CloudShield Enterprise
Threat Intelligence Rules
"""

THREAT_RULES = {
<<<<<<< HEAD
    "critical_cve": {
        "title": "Critical CVE Detected",
        "severity": "Critical",
        "category": "Threat Intelligence",
        "cvss": 9.8,
        "description": ("A critical vulnerability was detected."),
        "recommendation": ("Apply the vendor security patch immediately."),
    },
    "high_cve": {
        "title": "High Severity CVE",
        "severity": "High",
        "category": "Threat Intelligence",
        "cvss": 8.0,
        "description": ("A high severity vulnerability was detected."),
        "recommendation": ("Update affected software."),
    },
    "ioc_match": {
        "title": "IOC Match Detected",
        "severity": "Critical",
        "category": "Threat Intelligence",
        "cvss": 9.5,
        "description": ("Indicator of Compromise matched."),
        "recommendation": ("Investigate the affected asset immediately."),
    },
    "malicious_ip": {
        "title": "Malicious IP Address",
        "severity": "High",
        "category": "Threat Intelligence",
        "cvss": 8.5,
        "description": ("Communication with a known malicious IP."),
        "recommendation": ("Block the IP and investigate activity."),
    },
    "malicious_domain": {
        "title": "Malicious Domain",
        "severity": "High",
        "category": "Threat Intelligence",
        "cvss": 8.3,
        "description": ("Known malicious domain detected."),
        "recommendation": ("Block domain access immediately."),
    },
    "ransomware": {
        "title": "Possible Ransomware Activity",
        "severity": "Critical",
        "category": "Threat Intelligence",
        "cvss": 9.9,
        "description": ("Behavior matches known ransomware indicators."),
        "recommendation": ("Isolate the affected system immediately."),
    },
    "mitre_execution": {
        "title": "MITRE ATT&CK Execution Technique",
        "severity": "High",
        "category": "MITRE ATT&CK",
        "cvss": 8.5,
        "description": ("Execution technique observed."),
        "recommendation": ("Review endpoint logs and execution events."),
    },
    "mitre_persistence": {
        "title": "MITRE Persistence Technique",
        "severity": "High",
        "category": "MITRE ATT&CK",
        "cvss": 8.2,
        "description": ("Persistence technique detected."),
        "recommendation": ("Review startup services and scheduled tasks."),
    },
    "mitre_privilege": {
        "title": "Privilege Escalation Technique",
        "severity": "Critical",
        "category": "MITRE ATT&CK",
        "cvss": 9.2,
        "description": ("Privilege escalation behavior detected."),
        "recommendation": ("Investigate administrator activity immediately."),
    },
}
=======

    "critical_cve": {

        "title": "Critical CVE Detected",

        "severity": "Critical",

        "category": "Threat Intelligence",

        "cvss": 9.8,

        "description": (
            "A critical vulnerability was detected."
        ),

        "recommendation": (
            "Apply the vendor security patch immediately."
        )

    },

    "high_cve": {

        "title": "High Severity CVE",

        "severity": "High",

        "category": "Threat Intelligence",

        "cvss": 8.0,

        "description": (
            "A high severity vulnerability was detected."
        ),

        "recommendation": (
            "Update affected software."
        )

    },

    "ioc_match": {

        "title": "IOC Match Detected",

        "severity": "Critical",

        "category": "Threat Intelligence",

        "cvss": 9.5,

        "description": (
            "Indicator of Compromise matched."
        ),

        "recommendation": (
            "Investigate the affected asset immediately."
        )

    },

    "malicious_ip": {

        "title": "Malicious IP Address",

        "severity": "High",

        "category": "Threat Intelligence",

        "cvss": 8.5,

        "description": (
            "Communication with a known malicious IP."
        ),

        "recommendation": (
            "Block the IP and investigate activity."
        )

    },

    "malicious_domain": {

        "title": "Malicious Domain",

        "severity": "High",

        "category": "Threat Intelligence",

        "cvss": 8.3,

        "description": (
            "Known malicious domain detected."
        ),

        "recommendation": (
            "Block domain access immediately."
        )

    },

    "ransomware": {

        "title": "Possible Ransomware Activity",

        "severity": "Critical",

        "category": "Threat Intelligence",

        "cvss": 9.9,

        "description": (
            "Behavior matches known ransomware indicators."
        ),

        "recommendation": (
            "Isolate the affected system immediately."
        )

    },

    "mitre_execution": {

        "title": "MITRE ATT&CK Execution Technique",

        "severity": "High",

        "category": "MITRE ATT&CK",

        "cvss": 8.5,

        "description": (
            "Execution technique observed."
        ),

        "recommendation": (
            "Review endpoint logs and execution events."
        )

    },

    "mitre_persistence": {

        "title": "MITRE Persistence Technique",

        "severity": "High",

        "category": "MITRE ATT&CK",

        "cvss": 8.2,

        "description": (
            "Persistence technique detected."
        ),

        "recommendation": (
            "Review startup services and scheduled tasks."
        )

    },

    "mitre_privilege": {

        "title": "Privilege Escalation Technique",

        "severity": "Critical",

        "category": "MITRE ATT&CK",

        "cvss": 9.2,

        "description": (
            "Privilege escalation behavior detected."
        ),

        "recommendation": (
            "Investigate administrator activity immediately."
        )

    }

}
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
