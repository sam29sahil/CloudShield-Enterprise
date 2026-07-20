"""
CloudShield Enterprise
Finding Forms
"""

from flask_wtf import FlaskForm

from wtforms import (
    SelectField,
    SubmitField,
    TextAreaField
)


class FindingUpdateForm(FlaskForm):

    status = SelectField(

        "Status",

        choices=[

            ("Open", "Open"),

            ("In Progress", "In Progress"),

            ("Resolved", "Resolved")

        ]

    )

    recommendation = TextAreaField(

        "Recommendation"

    )

    submit = SubmitField(

        "Update Finding"

    )