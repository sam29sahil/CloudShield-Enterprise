"""
CloudShield Enterprise
SSL Security Constants
"""

# --------------------------------------------------
# Tool Names
# --------------------------------------------------

SSLYZE = "sslyze"

TESTSSL = "testssl"

OPENSSL = "openssl"

# --------------------------------------------------
# Default Timeout
# --------------------------------------------------

DEFAULT_TIMEOUT = 300

# --------------------------------------------------
# SSLyze Default Arguments
# --------------------------------------------------

SSLYZE_DEFAULT = ["--json_out=-", "--compression", "--reneg", "--resum", "--certinfo"]

# --------------------------------------------------
# TestSSL Default Arguments
# --------------------------------------------------

TESTSSL_DEFAULT = ["--warnings", "batch", "--color", "0"]

# --------------------------------------------------
# OpenSSL Default Arguments
# --------------------------------------------------

OPENSSL_DEFAULT = ["s_client"]

# --------------------------------------------------
# Supported TLS Versions
# --------------------------------------------------

TLS_VERSIONS = ["SSLv2", "SSLv3", "TLS1.0", "TLS1.1", "TLS1.2", "TLS1.3"]

# --------------------------------------------------
# Weak Ciphers
# --------------------------------------------------

WEAK_CIPHERS = ["RC2", "RC4", "DES", "3DES", "MD5", "NULL", "EXPORT"]

# --------------------------------------------------
# Vulnerability Checks
# --------------------------------------------------

SSL_CHECKS = [
    "Heartbleed",
    "POODLE",
    "BEAST",
    "FREAK",
    "LOGJAM",
    "DROWN",
    "ROBOT",
    "CRIME",
    "BREACH",
]

# --------------------------------------------------
# Certificate Checks
# --------------------------------------------------

CERTIFICATE_CHECKS = [
    "Expiration",
    "Issuer",
    "Chain",
    "Hostname",
    "Self Signed",
    "Revocation",
    "Key Size",
]

# --------------------------------------------------
# Risk Levels
# --------------------------------------------------

INFO = "Info"

LOW = "Low"

MEDIUM = "Medium"

HIGH = "High"

CRITICAL = "Critical"

# --------------------------------------------------
# Output Formats
# --------------------------------------------------

OUTPUT_JSON = "json"

OUTPUT_XML = "xml"

OUTPUT_TEXT = "text"
