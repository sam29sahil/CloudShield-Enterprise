"""
CloudShield Enterprise
Security Forms
"""

from flask_wtf import FlaskForm

from wtforms import (
    BooleanField,
    IntegerField,
    SelectField,
    StringField,
    SubmitField,
)

from wtforms.validators import (
    DataRequired,
    Length,
    NumberRange,
    Optional,
    ValidationError,
)

# ==========================================================
# Constants
# ==========================================================

SCAN_PROFILES = [
    ("quick", "⚡ Quick Scan"),
    ("web", "🌐 Web Security"),
    ("network", "🖥 Network Security"),
    ("cloud", "☁ Cloud Security"),
    ("wireless", "📡 Wireless Security"),
    ("full_enterprise", "🏢 Full Enterprise"),
]

OUTPUT_FORMATS = [
    ("html", "HTML"),
    ("pdf", "PDF"),
    ("json", "JSON"),
    ("csv", "CSV"),
]

SCAN_SPEEDS = [
    ("slow", "Slow"),
    ("normal", "Normal"),
    ("fast", "Fast"),
    ("aggressive", "Aggressive"),
]


# ==========================================================
# Shared Validators
# ==========================================================


def validate_target(form, field):
    """
    Validate scan target.
    Accepts domains and URLs.
    """

    target = field.data.strip()

    if not target:
        raise ValidationError("Target is required.")

    if len(target) > 255:
        raise ValidationError("Target is too long.")

    if (
        not target.startswith("http://")
        and not target.startswith("https://")
        and "." not in target
    ):
        raise ValidationError("Enter a valid domain or URL.")


# ==========================================================
# Universal Security Scan Form (Legacy / Generic)
# ==========================================================


class SecurityScanForm(FlaskForm):
    """
    Generic Security Scan Form.
    Kept for backward compatibility.
    """

    target = StringField(
        "Target",
        validators=[
            DataRequired(),
            Length(max=255),
            validate_target,
        ],
    )

    profile = SelectField(
        "Scan Profile",
        choices=SCAN_PROFILES,
        validators=[DataRequired()],
    )

    arguments = StringField(
        "Tool Arguments",
        validators=[
            Optional(),
            Length(max=500),
        ],
    )

    tool = SelectField(
        "Advanced Mode",
        choices=[
            ("", "-- Select Individual Tool --"),
            ("nmap", "Nmap"),
            ("rustscan", "RustScan"),
            ("masscan", "Masscan"),
            ("whatweb", "WhatWeb"),
            ("nikto", "Nikto"),
            ("nuclei", "Nuclei"),
            ("gobuster", "Gobuster"),
            ("ffuf", "FFUF"),
            ("sqlmap", "SQLMap"),
            ("wafw00f", "WAFW00F"),
            ("sslyze", "SSLyze"),
            ("testssl", "TestSSL"),
            ("amass", "Amass"),
            ("subfinder", "Subfinder"),
            ("dnsrecon", "DNSRecon"),
            ("prowler", "Prowler"),
            ("scoutsuite", "ScoutSuite"),
            ("trivy", "Trivy"),
        ],
    )

    submit = SubmitField("Start Scan")


# ==========================================================
# Basic Scanner Form
# ==========================================================


class BasicScannerForm(FlaskForm):
    """
    CloudShield Basic Scanner
    """

    target = StringField(
        "Target",
        validators=[
            DataRequired(),
            Length(max=255),
            validate_target,
        ],
    )

    profile = SelectField(
        "Scan Profile",
        choices=SCAN_PROFILES,
        default="quick",
    )

    website = BooleanField("Website Analysis", default=True)
    headers = BooleanField("HTTP Headers", default=True)
    ssl = BooleanField("SSL/TLS", default=True)
    dns = BooleanField("DNS Lookup", default=True)
    whois = BooleanField("WHOIS", default=True)
    technology = BooleanField("Technology Detection", default=True)
    services = BooleanField("Service Detection", default=True)
    ports = BooleanField("Port Scan", default=True)

    submit = SubmitField("Start Basic Scan")


# ==========================================================
# Universal Scanner Form
# ==========================================================


class UniversalScannerForm(FlaskForm):
    """
    CloudShield Universal Scanner
    """

    target = StringField(
        "Target",
        validators=[
            DataRequired(),
            Length(max=255),
            validate_target,
        ],
    )

    profile = SelectField(
        "Scan Profile",
        choices=SCAN_PROFILES,
        default="full_enterprise",
    )

    # -----------------------------
    # Network Tools
    # -----------------------------

    nmap = BooleanField("Nmap", default=True)
    rustscan = BooleanField("RustScan")
    masscan = BooleanField("Masscan")

    # -----------------------------
    # Web Tools
    # -----------------------------

    whatweb = BooleanField("WhatWeb", default=True)
    nikto = BooleanField("Nikto")
    nuclei = BooleanField("Nuclei")
    gobuster = BooleanField("Gobuster")
    ffuf = BooleanField("FFUF")
    sqlmap = BooleanField("SQLMap")

    # -----------------------------
    # SSL Tools
    # -----------------------------

    sslyze = BooleanField("SSLyze")
    testssl = BooleanField("TestSSL")

    # -----------------------------
    # Recon Tools
    # -----------------------------

    amass = BooleanField("Amass")
    subfinder = BooleanField("Subfinder")
    dnsrecon = BooleanField("DNSRecon")
    wafw00f = BooleanField("WAFW00F")

    # -----------------------------
    # Cloud Security
    # -----------------------------

    prowler = BooleanField("Prowler")
    scoutsuite = BooleanField("ScoutSuite")
    trivy = BooleanField("Trivy")

    # -----------------------------
    # Advanced Options
    # -----------------------------

    threads = IntegerField(
        "Threads",
        default=10,
        validators=[
            NumberRange(min=1, max=100),
        ],
    )

    timeout = IntegerField(
        "Timeout (seconds)",
        default=60,
        validators=[
            NumberRange(min=5, max=600),
        ],
    )

    speed = SelectField(
        "Scan Speed",
        choices=SCAN_SPEEDS,
        default="normal",
    )

    output = SelectField(
        "Output Format",
        choices=OUTPUT_FORMATS,
        default="html",
    )

    arguments = StringField(
        "Custom Arguments",
        validators=[
            Optional(),
            Length(max=500),
        ],
    )

    submit = SubmitField("Launch Enterprise Scan")
