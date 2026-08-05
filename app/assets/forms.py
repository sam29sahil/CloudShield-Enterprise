"""
CloudShield Enterprise
Asset Form
"""

from flask_wtf import FlaskForm

<<<<<<< HEAD
from wtforms import StringField, SubmitField, SelectField
=======
from wtforms import (
    StringField,
    SubmitField,
    SelectField
)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

from wtforms.validators import DataRequired


class AssetForm(FlaskForm):

<<<<<<< HEAD
    name = StringField("Asset Name", validators=[DataRequired()])

    target = StringField("Target", validators=[DataRequired()])
=======
    name = StringField(
        "Asset Name",
        validators=[DataRequired()]
    )

    target = StringField(
        "Target",
        validators=[DataRequired()]
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    asset_type = SelectField(
        "Asset Type",
        choices=[
            ("website", "Website"),
            ("server", "Server"),
            ("api", "API"),
            ("cloud", "Cloud Resource"),
<<<<<<< HEAD
            ("ip", "IP Address"),
        ],
        validators=[DataRequired()],
    )

    project_id = SelectField(
        "Project", coerce=int, validators=[DataRequired()], choices=[]
    )

    submit = SubmitField("Save Asset")
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
