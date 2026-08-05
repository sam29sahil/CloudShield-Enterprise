"""
CloudShield Enterprise
Cloud Security Constants
"""

PROWLER_DEFAULT = ["aws"]

SCOUTSUITE_DEFAULT = ["aws"]

CLOUDSPLAINING_DEFAULT = ["scan"]

TRIVY_IMAGE_DEFAULT = ["image"]

TRIVY_FILESYSTEM_DEFAULT = ["fs"]

TRIVY_CONFIG_DEFAULT = ["config"]

TRIVY_KUBERNETES_DEFAULT = ["kubernetes"]

SUPPORTED_PROVIDERS = ["AWS", "Azure", "GCP", "Kubernetes", "Docker"]

DEFAULT_TIMEOUT = 900

SEVERITY_LEVELS = ["UNKNOWN", "LOW", "MEDIUM", "HIGH", "CRITICAL"]
