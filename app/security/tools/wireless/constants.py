"""
CloudShield Enterprise
Wireless Security Constants
"""

# ------------------------------------------------
# Tool Names
# ------------------------------------------------

AIRCRACK = "aircrack-ng"

AIRODUMP = "airodump-ng"

AIREPLAY = "aireplay-ng"

WIFITE = "wifite"

# ------------------------------------------------
# Default Timeout
# ------------------------------------------------

DEFAULT_TIMEOUT = 600

# ------------------------------------------------
# Default Arguments
# ------------------------------------------------

AIRCRACK_DEFAULT = []

AIRODUMP_DEFAULT = []

AIREPLAY_DEFAULT = []

WIFITE_DEFAULT = []

# ------------------------------------------------
# Wireless Security
# ------------------------------------------------

SECURITY_TYPES = [

    "OPEN",

    "WEP",

    "WPA",

    "WPA2",

    "WPA3"

]

# ------------------------------------------------
# Attack Types
# ------------------------------------------------

ATTACK_TYPES = [

    "Handshake Capture",

    "PMKID Capture",

    "Deauthentication",

    "Fake Authentication",

    "Packet Injection"

]

# ------------------------------------------------
# Capture Files
# ------------------------------------------------

CAPTURE_EXTENSIONS = [

    ".cap",

    ".pcap",

    ".pcapng",

    ".ivs"

]

# ------------------------------------------------
# Risk Levels
# ------------------------------------------------

INFO = "Info"

LOW = "Low"

MEDIUM = "Medium"

HIGH = "High"

CRITICAL = "Critical"

# ------------------------------------------------
# Output Formats
# ------------------------------------------------

OUTPUT_TEXT = "text"

OUTPUT_JSON = "json"

OUTPUT_CSV = "csv"