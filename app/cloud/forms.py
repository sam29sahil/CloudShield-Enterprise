"""
CloudShield Enterprise
Cloud Forms
"""

from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class CloudRegionForm(FlaskForm):

    region = SelectField(
        "AWS Region",
        choices=[
            ("ap-south-1", "Mumbai"),
            ("us-east-1", "N. Virginia"),
            ("us-west-2", "Oregon"),
            ("eu-west-1", "Ireland"),
        ],
        default="ap-south-1",
    )

    submit = SubmitField("Connect")
