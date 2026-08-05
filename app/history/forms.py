"""
CloudShield Enterprise
History Forms
"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Optional


class HistorySearchForm(FlaskForm):

<<<<<<< HEAD
    search = StringField("Search", validators=[Optional()])
=======
    search = StringField(

        "Search",

        validators=[Optional()]

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
