"""
CloudShield Enterprise
Project Form
"""

from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    TextAreaField,
    SubmitField
)

from wtforms.validators import DataRequired


class ProjectForm(FlaskForm):

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