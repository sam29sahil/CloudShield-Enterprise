"""
CloudShield Enterprise
Technology Detection Rules
"""

TECHNOLOGY_RULES = {
    "Apache": {
        "title": "Apache Web Server Detected",
        "severity": "Info",
        "cvss": 0.0,
        "description": ("Apache HTTP Server detected."),
        "recommendation": ("Keep Apache updated with the latest security patches."),
    },
    "Nginx": {
        "title": "Nginx Web Server Detected",
        "severity": "Info",
        "cvss": 0.0,
        "description": ("Nginx Web Server detected."),
        "recommendation": ("Use the latest stable version of Nginx."),
    },
    "IIS": {
        "title": "Microsoft IIS Detected",
        "severity": "Info",
        "cvss": 0.0,
        "description": ("Microsoft IIS Web Server detected."),
        "recommendation": ("Keep Windows Server and IIS fully patched."),
    },
    "PHP": {
        "title": "PHP Detected",
        "severity": "Low",
        "cvss": 2.5,
        "description": ("PHP runtime detected."),
        "recommendation": ("Keep PHP updated and disable unused modules."),
    },
    "Python": {
        "title": "Python Application Detected",
        "severity": "Info",
        "cvss": 0.0,
        "description": ("Python-powered application detected."),
        "recommendation": ("Keep Python dependencies updated."),
    },
    "Flask": {
        "title": "Flask Framework Detected",
        "severity": "Info",
        "cvss": 0.0,
        "description": ("Flask framework detected."),
        "recommendation": ("Keep Flask and all extensions updated."),
    },
    "Django": {
        "title": "Django Framework Detected",
        "severity": "Info",
        "cvss": 0.0,
        "description": ("Django framework detected."),
        "recommendation": ("Apply Django security updates regularly."),
    },
    "Node.js": {
        "title": "Node.js Detected",
        "severity": "Low",
        "cvss": 2.8,
        "description": ("Node.js runtime detected."),
        "recommendation": ("Update Node.js and audit npm packages."),
    },
    "Express": {
        "title": "Express Framework Detected",
        "severity": "Low",
        "cvss": 2.8,
        "description": ("Express framework detected."),
        "recommendation": ("Update Express and middleware packages."),
    },
    "Tomcat": {
        "title": "Apache Tomcat Detected",
        "severity": "Medium",
        "cvss": 4.2,
        "description": ("Apache Tomcat detected."),
        "recommendation": ("Keep Tomcat updated and remove default applications."),
    },
    "WordPress": {
        "title": "WordPress CMS Detected",
        "severity": "Medium",
        "cvss": 5.0,
        "description": ("WordPress installation detected."),
        "recommendation": ("Keep WordPress core, themes and plugins updated."),
    },
    "Joomla": {
        "title": "Joomla CMS Detected",
        "severity": "Medium",
        "cvss": 5.0,
        "description": ("Joomla CMS detected."),
        "recommendation": ("Update Joomla and installed extensions."),
    },
    "Drupal": {
        "title": "Drupal CMS Detected",
        "severity": "Medium",
        "cvss": 5.0,
        "description": ("Drupal CMS detected."),
        "recommendation": ("Keep Drupal core and modules updated."),
    },
    "ASP.NET": {
        "title": "ASP.NET Application Detected",
        "severity": "Info",
        "cvss": 0.0,
        "description": ("ASP.NET application detected."),
        "recommendation": ("Apply Microsoft security updates regularly."),
    },
}
