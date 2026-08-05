"""
CloudShield Enterprise
Analytics Forms
"""

from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class AnalyticsForm(FlaskForm):
    """
    Analytics Filter Form
    """

    period = SelectField(
<<<<<<< HEAD
        "Time Period",
        choices=[
            ("7", "Last 7 Days"),
            ("30", "Last 30 Days"),
            ("90", "Last 90 Days"),
            ("365", "Last Year"),
        ],
    )

    submit = SubmitField("Apply Filter")
=======

        "Time Period",

        choices=[

            ("7", "Last 7 Days"),

            ("30", "Last 30 Days"),

            ("90", "Last 90 Days"),

            ("365", "Last Year")

        ]

    )

    submit = SubmitField(

        "Apply Filter"

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
