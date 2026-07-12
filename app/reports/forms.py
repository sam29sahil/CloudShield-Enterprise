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