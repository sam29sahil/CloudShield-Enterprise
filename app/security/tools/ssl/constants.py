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

<<<<<<< HEAD
SSLYZE_DEFAULT = ["--json_out=-", "--compression", "--reneg", "--resum", "--certinfo"]
=======
SSLYZE_DEFAULT = [

    "--json_out=-",

    "--compression",

    "--reneg",

    "--resum",

    "--certinfo"

]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# --------------------------------------------------
# TestSSL Default Arguments
# --------------------------------------------------

<<<<<<< HEAD
TESTSSL_DEFAULT = ["--warnings", "batch", "--color", "0"]
=======
TESTSSL_DEFAULT = [

    "--warnings",

    "batch",

    "--color",

    "0"

]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# --------------------------------------------------
# OpenSSL Default Arguments
# --------------------------------------------------

<<<<<<< HEAD
OPENSSL_DEFAULT = ["s_client"]
=======
OPENSSL_DEFAULT = [

    "s_client"

]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# --------------------------------------------------
# Supported TLS Versions
# --------------------------------------------------

<<<<<<< HEAD
TLS_VERSIONS = ["SSLv2", "SSLv3", "TLS1.0", "TLS1.1", "TLS1.2", "TLS1.3"]
=======
TLS_VERSIONS = [

    "SSLv2",

    "SSLv3",

    "TLS1.0",

    "TLS1.1",

    "TLS1.2",

    "TLS1.3"

]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# --------------------------------------------------
# Weak Ciphers
# --------------------------------------------------

<<<<<<< HEAD
WEAK_CIPHERS = ["RC2", "RC4", "DES", "3DES", "MD5", "NULL", "EXPORT"]
=======
WEAK_CIPHERS = [

    "RC2",

    "RC4",

    "DES",

    "3DES",

    "MD5",

    "NULL",

    "EXPORT"

]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# --------------------------------------------------
# Vulnerability Checks
# --------------------------------------------------

SSL_CHECKS = [
<<<<<<< HEAD
    "Heartbleed",
    "POODLE",
    "BEAST",
    "FREAK",
    "LOGJAM",
    "DROWN",
    "ROBOT",
    "CRIME",
    "BREACH",
=======

    "Heartbleed",

    "POODLE",

    "BEAST",

    "FREAK",

    "LOGJAM",

    "DROWN",

    "ROBOT",

    "CRIME",

    "BREACH"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
]

# --------------------------------------------------
# Certificate Checks
# --------------------------------------------------

CERTIFICATE_CHECKS = [
<<<<<<< HEAD
    "Expiration",
    "Issuer",
    "Chain",
    "Hostname",
    "Self Signed",
    "Revocation",
    "Key Size",
=======

    "Expiration",

    "Issuer",

    "Chain",

    "Hostname",

    "Self Signed",

    "Revocation",

    "Key Size"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
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

<<<<<<< HEAD
OUTPUT_TEXT = "text"
=======
OUTPUT_TEXT = "text"
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
