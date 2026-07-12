"""
CloudShield Enterprise
Universal Scanner Form
"""

from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired


class ScanForm(FlaskForm):

    mode = SelectField(

        "Scanner Mode",

        choices=[

            ("basic", "Basic Scanner"),

            ("universal", "Universal Scanner")

        ],

        default="basic",

        validators=[DataRequired()]

    )

    category = SelectField(

        "Category",

        validators=[DataRequired()],

        choices=[

            ("network", "Network"),

            ("web", "Web"),

            ("ssl", "SSL"),

            ("dns", "DNS"),

            ("cloud", "Cloud"),

            ("wireless", "Wireless")

        ]

    )

    tool = SelectField(

        "Tool",

        choices=[]

    )

    target = StringField(

        "Target",

        validators=[DataRequired()]

    )

    arguments = StringField(

        "Arguments"

    )

    submit = SubmitField(

        "Run Scan"

    )