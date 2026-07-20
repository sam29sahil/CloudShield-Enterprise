"""
CloudShield Enterprise
Nmap Constants
"""

# -------------------------
# Scan Types
# -------------------------

PING_SCAN = [
    "-sn"
]

TCP_SCAN = [
    "-sT"
]

SYN_SCAN = [
    "-sS"
]

UDP_SCAN = [
    "-sU"
]

SERVICE_SCAN = [
    "-sV"
]

OS_SCAN = [
    "-O"
]

AGGRESSIVE_SCAN = [
    "-A"
]

VERSION_SCAN = [
    "-sV"
]

DEFAULT_SCAN = [

    "-sV",

    "-T4"

]

# -------------------------
# Timing
# -------------------------

T0 = "-T0"

T1 = "-T1"

T2 = "-T2"

T3 = "-T3"

T4 = "-T4"

T5 = "-T5"

# -------------------------
# Output
# -------------------------

XML_OUTPUT = "-oX"

NORMAL_OUTPUT = "-oN"

GREP_OUTPUT = "-oG"

# -------------------------
# NSE
# -------------------------

DEFAULT_SCRIPT = [
    "-sC"
]

VULN_SCRIPT = [
    "--script=vuln"
]

HTTP_SCRIPT = [
    "--script=http-*"
]

SMB_SCRIPT = [
    "--script=smb-*"
]

FTP_SCRIPT = [
    "--script=ftp-*"
]

SSH_SCRIPT = [
    "--script=ssh-*"
]