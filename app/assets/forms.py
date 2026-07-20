"""
CloudShield Enterprise
Asset Form
"""

from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    SubmitField,
    SelectField
)

from wtforms.validators import DataRequired


class AssetForm(FlaskForm):

    name = StringField(
        "Asset Name",
        validators=[DataRequired()]
    )

    target = StringField(
        "Target",
        validators=[DataRequired()]
    )

    asset_type = SelectField(
        "Asset Type",
        choices=[
            ("website", "Website"),
            ("server", "Server"),
            ("api", "API"),
            ("cloud", "Cloud Resource"),
            ("ip", "IP Address")
        ],
        validators=[DataRequired()]
    )

    project_id = SelectField(
        "Project",
        coerce=int,
        validators=[DataRequired()],
        choices=[]
    )

    submit = SubmitField(
        "Save Asset"
    )