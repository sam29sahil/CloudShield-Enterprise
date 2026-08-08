"""
CloudShield Enterprise
Scanner Constants
"""

# ==========================================================
# QUICK SCAN TOOLS
# ==========================================================

QUICK_TOOLS = {

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

}

# ==========================================================
# DEEP SCAN TOOLS
# ==========================================================

DEEP_TOOLS = {

    "network": [
        "nmap",
        "rustscan",
        "masscan",
        "netdiscover"
    ],

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

}

# ==========================================================
# DNS
# ==========================================================

DNS_RECORDS = [

    "A",
    "AAAA",
    "CNAME",
    "MX",
    "NS",
    "TXT",
    "SOA"

]

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

}

# ==========================================
# Technology Detection
# ==========================================

SERVER_SIGNATURES = {

    "apache": "Apache",

    "nginx": "Nginx",

    "iis": "Microsoft IIS",

    "cloudflare": "Cloudflare",

    "openresty": "OpenResty",

    "caddy": "Caddy"

}


FRAMEWORK_SIGNATURES = {

    "php": "PHP",

    "express": "Express.js",

    "asp.net": "ASP.NET",

    "django": "Django",

    "flask": "Flask",

    "laravel": "Laravel",

    "wordpress": "WordPress"

}


HTML_SIGNATURES = {

    "wp-content": "WordPress",

    "drupal.settings": "Drupal",

    "__next": "Next.js",

    "react": "React",

    "vue": "Vue.js",

    "angular": "Angular",

    "bootstrap": "Bootstrap",

    "jquery": "jQuery"

}