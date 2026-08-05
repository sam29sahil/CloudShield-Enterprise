"""
CloudShield Enterprise
Reports Forms
"""

from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired


class ReportForm(FlaskForm):
    """
    Report Generation Form
    """

    report_type = SelectField(
<<<<<<< HEAD
        "Report Format",
        choices=[("pdf", "PDF Report"), ("csv", "CSV Report"), ("json", "JSON Report")],
        validators=[DataRequired()],
    )

    submit = SubmitField("Generate Report")
=======

        "Report Format",

        choices=[

            ("pdf", "PDF Report"),

            ("csv", "CSV Report"),

            ("json", "JSON Report")

        ],

        validators=[DataRequired()]

    )

    submit = SubmitField(

        "Generate Report"

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
