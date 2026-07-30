"""
CloudShield Enterprise
Security Forms
"""

from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    StringField,
    SubmitField
)
from wtforms.validators import DataRequired

class SecurityScanForm(FlaskForm):
    """
    Universal Security Scan Form
    """

    target = StringField(
        "Target",
        validators=[DataRequired()]
    )

    profile = SelectField(
        "Scan Profile",
        choices=[
            ("quick", "⚡ Quick Scan"),
            ("web", "🌐 Web Security"),
            ("network", "🖥 Network Security"),
            ("cloud", "☁ Cloud Security"),
            ("wireless", "📡 Wireless Security"),
            ("full_enterprise", "🏢 Full Enterprise")
        ],
        validators=[DataRequired()]
    )

    arguments = StringField(
        "Tool Arguments (Optional)"
    )

    tool = SelectField(
        "Advanced Mode (Optional)",
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
            ("trivy", "Trivy")
        ]
    )

    submit = SubmitField("Start Scan")