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
from wtforms.validators import (
    DataRequired
)


class SecurityScanForm(FlaskForm):
    """
    Universal Security Scan Form
    """

    target = StringField(

        "Target",

        validators=[

            DataRequired()

        ]

    )

    tool = SelectField(

        "Security Tool",

        choices=[

            ("nmap", "Nmap"),

            ("whatweb", "WhatWeb"),

            ("nikto", "Nikto"),

            ("nuclei", "Nuclei"),

            ("gobuster", "Gobuster"),

            ("ffuf", "FFUF"),

            ("sqlmap", "SQLMap"),

            ("sslyze", "SSLyze"),

            ("testssl", "TestSSL"),

            ("amass", "Amass"),

            ("subfinder", "Subfinder")

        ],

        validators=[

            DataRequired()

        ]

    )

    submit = SubmitField(

        "Start Scan"

    )