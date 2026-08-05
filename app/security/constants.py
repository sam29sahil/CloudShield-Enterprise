"""
CloudShield Enterprise
Scanner Constants
"""

# ==========================================================
# QUICK SCAN TOOLS
# ==========================================================

QUICK_TOOLS = {
<<<<<<< HEAD
    "network": ["quick_scan"],
    "web": ["quick_scan"],
    "ssl": ["quick_scan"],
    "dns": ["quick_scan"],
    "cloud": [],
    "wireless": [],
=======

    "network": [
        "quick_scan"
    ],

    "web": [
        "quick_scan"
    ],

    "ssl": [
        "quick_scan"
    ],

    "dns": [
        "quick_scan"
    ],

    "cloud": [],

    "wireless": []

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
}

# ==========================================================
# DEEP SCAN TOOLS
# ==========================================================

DEEP_TOOLS = {
<<<<<<< HEAD
    "network": ["nmap", "rustscan", "masscan", "netdiscover"],
=======

    "network": [
        "nmap",
        "rustscan",
        "masscan",
        "netdiscover"
    ],

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    "web": [
        "whatweb",
        "nikto",
        "nuclei",
        "gobuster",
        "ffuf",
        "dirsearch",
        "sqlmap",
        "zap",
        "dalfox",
        "xsstrike",
        "wafw00f",
<<<<<<< HEAD
        "corsy",
    ],
    "ssl": ["sslyze", "testssl", "openssl"],
    "dns": ["amass", "subfinder", "assetfinder", "dnsrecon", "dnsenum", "fierce"],
    "cloud": ["prowler", "scoutsuite", "cloudsplaining", "trivy"],
    "wireless": ["aircrack-ng", "airodump-ng", "aireplay-ng", "wifite"],
=======
        "corsy"
    ],

    "ssl": [
        "sslyze",
        "testssl",
        "openssl"
    ],

    "dns": [
        "amass",
        "subfinder",
        "assetfinder",
        "dnsrecon",
        "dnsenum",
        "fierce"
    ],

    "cloud": [
        "prowler",
        "scoutsuite",
        "cloudsplaining",
        "trivy"
    ],

    "wireless": [
        "aircrack-ng",
        "airodump-ng",
        "aireplay-ng",
        "wifite"
    ]

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
}

# ==========================================================
# DNS
# ==========================================================

<<<<<<< HEAD
DNS_RECORDS = ["A", "AAAA", "CNAME", "MX", "NS", "TXT", "SOA"]
=======
DNS_RECORDS = [

    "A",
    "AAAA",
    "CNAME",
    "MX",
    "NS",
    "TXT",
    "SOA"

]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# ==========================================================
# WEBSITE
# ==========================================================

HTTP_TIMEOUT = 10

USER_AGENT = "CloudShield/1.0"

# ==========================================================
# SECURITY HEADERS
# ==========================================================

OWASP_REFERENCE = "https://owasp.org/www-project-secure-headers/"

SECURITY_HEADERS = {
<<<<<<< HEAD
    "Content-Security-Policy": {
        "severity": "High",
        "description": "Protects against XSS attacks.",
    },
    "Strict-Transport-Security": {"severity": "High", "description": "Forces HTTPS."},
    "X-Frame-Options": {"severity": "Medium", "description": "Prevents clickjacking."},
    "X-Content-Type-Options": {
        "severity": "Medium",
        "description": "Stops MIME sniffing.",
    },
    "Referrer-Policy": {"severity": "Low", "description": "Controls referrer leakage."},
    "Permissions-Policy": {
        "severity": "Low",
        "description": "Restricts browser features.",
    },
=======

    "Content-Security-Policy": {
        "severity": "High",
        "description": "Protects against XSS attacks."
    },

    "Strict-Transport-Security": {
        "severity": "High",
        "description": "Forces HTTPS."
    },

    "X-Frame-Options": {
        "severity": "Medium",
        "description": "Prevents clickjacking."
    },

    "X-Content-Type-Options": {
        "severity": "Medium",
        "description": "Stops MIME sniffing."
    },

    "Referrer-Policy": {
        "severity": "Low",
        "description": "Controls referrer leakage."
    },

    "Permissions-Policy": {
        "severity": "Low",
        "description": "Restricts browser features."
    }

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
}

# ==========================================
# Technology Detection
# ==========================================

SERVER_SIGNATURES = {
<<<<<<< HEAD
    "apache": "Apache",
    "nginx": "Nginx",
    "iis": "Microsoft IIS",
    "cloudflare": "Cloudflare",
    "openresty": "OpenResty",
    "caddy": "Caddy",
=======

    "apache": "Apache",

    "nginx": "Nginx",

    "iis": "Microsoft IIS",

    "cloudflare": "Cloudflare",

    "openresty": "OpenResty",

    "caddy": "Caddy"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
}


FRAMEWORK_SIGNATURES = {
<<<<<<< HEAD
    "php": "PHP",
    "express": "Express.js",
    "asp.net": "ASP.NET",
    "django": "Django",
    "flask": "Flask",
    "laravel": "Laravel",
    "wordpress": "WordPress",
=======

    "php": "PHP",

    "express": "Express.js",

    "asp.net": "ASP.NET",

    "django": "Django",

    "flask": "Flask",

    "laravel": "Laravel",

    "wordpress": "WordPress"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
}


HTML_SIGNATURES = {
<<<<<<< HEAD
    "wp-content": "WordPress",
    "drupal.settings": "Drupal",
    "__next": "Next.js",
    "react": "React",
    "vue": "Vue.js",
    "angular": "Angular",
    "bootstrap": "Bootstrap",
    "jquery": "jQuery",
}
=======

    "wp-content": "WordPress",

    "drupal.settings": "Drupal",

    "__next": "Next.js",

    "react": "React",

    "vue": "Vue.js",

    "angular": "Angular",

    "bootstrap": "Bootstrap",

    "jquery": "jQuery"

}
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
