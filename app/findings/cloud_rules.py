"""
CloudShield Enterprise
Cloud Finding Rules
"""

CLOUD_RULES = {
<<<<<<< HEAD
    # ==========================================
    # AWS S3
    # ==========================================
    "public_s3": {
        "title": "Public S3 Bucket",
        "severity": "Critical",
        "category": "Cloud",
        "cvss": 9.8,
        "description": ("An Amazon S3 bucket is publicly accessible."),
        "recommendation": ("Disable public access and review bucket policies."),
    },
    # ==========================================
    # Security Groups
    # ==========================================
    "open_security_group": {
        "title": "Open Security Group",
        "severity": "High",
        "category": "Cloud",
        "cvss": 8.8,
        "description": ("Security Group allows unrestricted inbound access."),
        "recommendation": ("Restrict inbound rules to trusted IP addresses."),
    },
    # ==========================================
    # IAM
    # ==========================================
    "admin_policy": {
        "title": "Overly Permissive IAM Policy",
        "severity": "High",
        "category": "Cloud",
        "cvss": 8.5,
        "description": ("IAM policy grants excessive privileges."),
        "recommendation": ("Apply the principle of least privilege."),
    },
    "root_account_used": {
        "title": "Root Account Usage Detected",
        "severity": "Critical",
        "category": "Cloud",
        "cvss": 9.5,
        "description": ("AWS Root account has been used."),
        "recommendation": ("Avoid using the root account except for emergency tasks."),
    },
    # ==========================================
    # CloudTrail
    # ==========================================
    "cloudtrail_disabled": {
        "title": "CloudTrail Disabled",
        "severity": "Medium",
        "category": "Cloud",
        "cvss": 6.8,
        "description": ("CloudTrail logging is disabled."),
        "recommendation": ("Enable CloudTrail in all AWS regions."),
    },
    # ==========================================
    # GuardDuty
    # ==========================================
    "guardduty_disabled": {
        "title": "GuardDuty Disabled",
        "severity": "Medium",
        "category": "Cloud",
        "cvss": 6.5,
        "description": ("GuardDuty is not enabled."),
        "recommendation": ("Enable GuardDuty to detect threats."),
    },
    # ==========================================
    # Inspector
    # ==========================================
    "inspector_disabled": {
        "title": "Inspector Disabled",
        "severity": "Low",
        "category": "Cloud",
        "cvss": 3.8,
        "description": ("Amazon Inspector is disabled."),
        "recommendation": ("Enable Inspector for continuous vulnerability assessment."),
    },
    # ==========================================
    # EC2
    # ==========================================
    "public_ec2": {
        "title": "Public EC2 Instance",
        "severity": "Medium",
        "category": "Cloud",
        "cvss": 5.9,
        "description": ("EC2 instance has a public IP address."),
        "recommendation": ("Review whether public access is required."),
    },
}
=======

    # ==========================================
    # AWS S3
    # ==========================================

    "public_s3": {

        "title": "Public S3 Bucket",

        "severity": "Critical",

        "category": "Cloud",

        "cvss": 9.8,

        "description": (
            "An Amazon S3 bucket is publicly accessible."
        ),

        "recommendation": (
            "Disable public access and review bucket policies."
        )

    },

    # ==========================================
    # Security Groups
    # ==========================================

    "open_security_group": {

        "title": "Open Security Group",

        "severity": "High",

        "category": "Cloud",

        "cvss": 8.8,

        "description": (
            "Security Group allows unrestricted inbound access."
        ),

        "recommendation": (
            "Restrict inbound rules to trusted IP addresses."
        )

    },

    # ==========================================
    # IAM
    # ==========================================

    "admin_policy": {

        "title": "Overly Permissive IAM Policy",

        "severity": "High",

        "category": "Cloud",

        "cvss": 8.5,

        "description": (
            "IAM policy grants excessive privileges."
        ),

        "recommendation": (
            "Apply the principle of least privilege."
        )

    },

    "root_account_used": {

        "title": "Root Account Usage Detected",

        "severity": "Critical",

        "category": "Cloud",

        "cvss": 9.5,

        "description": (
            "AWS Root account has been used."
        ),

        "recommendation": (
            "Avoid using the root account except for emergency tasks."
        )

    },

    # ==========================================
    # CloudTrail
    # ==========================================

    "cloudtrail_disabled": {

        "title": "CloudTrail Disabled",

        "severity": "Medium",

        "category": "Cloud",

        "cvss": 6.8,

        "description": (
            "CloudTrail logging is disabled."
        ),

        "recommendation": (
            "Enable CloudTrail in all AWS regions."
        )

    },

    # ==========================================
    # GuardDuty
    # ==========================================

    "guardduty_disabled": {

        "title": "GuardDuty Disabled",

        "severity": "Medium",

        "category": "Cloud",

        "cvss": 6.5,

        "description": (
            "GuardDuty is not enabled."
        ),

        "recommendation": (
            "Enable GuardDuty to detect threats."
        )

    },

    # ==========================================
    # Inspector
    # ==========================================

    "inspector_disabled": {

        "title": "Inspector Disabled",

        "severity": "Low",

        "category": "Cloud",

        "cvss": 3.8,

        "description": (
            "Amazon Inspector is disabled."
        ),

        "recommendation": (
            "Enable Inspector for continuous vulnerability assessment."
        )

    },

    # ==========================================
    # EC2
    # ==========================================

    "public_ec2": {

        "title": "Public EC2 Instance",

        "severity": "Medium",

        "category": "Cloud",

        "cvss": 5.9,

        "description": (
            "EC2 instance has a public IP address."
        ),

        "recommendation": (
            "Review whether public access is required."
        )

    }

}
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
