"""
CloudShield Enterprise
History Forms
"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Optional


class HistorySearchForm(FlaskForm):

    search = StringField("Search", validators=[Optional()])
