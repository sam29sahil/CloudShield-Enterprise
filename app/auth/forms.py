from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):

    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=3, max=20)],
        filters=[lambda value: value.strip() if value else value],
    )

    email = StringField(
        "Email",
        validators=[DataRequired(), Email()],
        filters=[lambda value: value.strip() if value else value],
    )

    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])

    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )

    submit = SubmitField("Register")


class LoginForm(FlaskForm):

    email = StringField(
        "Email",
        validators=[DataRequired(), Email()],
        filters=[lambda value: value.strip().lower() if value else value],
    )

    password = PasswordField("Password", validators=[DataRequired()])

    submit = SubmitField("Login")
