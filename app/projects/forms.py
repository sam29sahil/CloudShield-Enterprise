"""
CloudShield Enterprise
Project Form
"""

from flask_wtf import FlaskForm

<<<<<<< HEAD
from wtforms import StringField, TextAreaField, SubmitField
=======
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField
)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

from wtforms.validators import DataRequired


class ProjectForm(FlaskForm):

<<<<<<< HEAD
    name = StringField("Project Name", validators=[DataRequired()])

    description = TextAreaField("Description")

    owner = StringField("Owner")

    submit = SubmitField("Save Project")
=======
    name = StringField(

        "Project Name",

        validators=[DataRequired()]

    )

    description = TextAreaField(

        "Description"

    )

    owner = StringField(

        "Owner"

    )

    submit = SubmitField(

        "Save Project"

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
