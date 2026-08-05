"""
CloudShield Enterprise
Finding Forms
"""

from flask_wtf import FlaskForm

<<<<<<< HEAD
from wtforms import SelectField, SubmitField, TextAreaField
=======
from wtforms import (
    SelectField,
    SubmitField,
    TextAreaField
)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


class FindingUpdateForm(FlaskForm):

    status = SelectField(
<<<<<<< HEAD
        "Status",
        choices=[
            ("Open", "Open"),
            ("In Progress", "In Progress"),
            ("Resolved", "Resolved"),
        ],
    )

    recommendation = TextAreaField("Recommendation")

    submit = SubmitField("Update Finding")
=======

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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
