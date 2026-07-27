"""
CloudShield Enterprise
Settings Forms
"""

from flask_wtf import FlaskForm

from wtforms import (

    StringField,

    PasswordField,

    BooleanField,

    SelectField,

    IntegerField,

    SubmitField

)

from wtforms.validators import (

    DataRequired,

    Email,

    EqualTo,

    Length,

    NumberRange,

    Optional

)


# ==========================================================
# Profile
# ==========================================================

class ProfileForm(FlaskForm):

    full_name = StringField(

        "Full Name",

        validators=[

            DataRequired(),

            Length(max=120)

        ]

    )

    username = StringField(

        "Username",

        validators=[

            DataRequired(),

            Length(max=80)

        ]

    )

    email = StringField(

        "Email",

        validators=[

            DataRequired(),

            Email()

        ]

    )

    submit = SubmitField(

        "Save Profile"

    )


# ==========================================================
# Password
# ==========================================================

class PasswordForm(FlaskForm):

    current_password = PasswordField(

        "Current Password",

        validators=[

            DataRequired()

        ]

    )

    new_password = PasswordField(

        "New Password",

        validators=[

            DataRequired(),

            Length(min=8)

        ]

    )

    confirm_password = PasswordField(

        "Confirm Password",

        validators=[

            DataRequired(),

            EqualTo("new_password")

        ]

    )

    submit = SubmitField(

        "Change Password"

    )


# ==========================================================
# Scanner Settings
# ==========================================================

class ScannerSettingsForm(FlaskForm):

    default_mode = SelectField(

        "Default Scan Mode",

        choices=[

            ("basic", "Basic"),

            ("deep", "Universal")

        ]

    )

    default_category = SelectField(

        "Default Category",

        choices=[

            ("network", "Network"),

            ("web", "Web"),

            ("cloud", "Cloud"),

            ("osint", "OSINT")

        ]

    )

    timeout = IntegerField(

        "Timeout (seconds)",

        validators=[

            Optional(),

            NumberRange(

                min=5,

                max=600

            )

        ]

    )

    save_history = BooleanField(

        "Save Scan History"

    )

    submit = SubmitField(

        "Save Scanner Settings"

    )


# ==========================================================
# Report Settings
# ==========================================================

class ReportSettingsForm(FlaskForm):

    company_name = StringField(

        "Company Name"

    )

    company_email = StringField(

        "Company Email",

        validators=[

            Optional(),

            Email()

        ]

    )

    company_website = StringField(

        "Company Website"

    )

    default_format = SelectField(

        "Default Export Format",

        choices=[

            ("pdf", "PDF"),

            ("csv", "CSV"),

            ("json", "JSON")

        ]

    )

    include_summary = BooleanField(

        "Include Executive Summary"

    )

    include_recommendations = BooleanField(

        "Include Recommendations"

    )

    include_raw = BooleanField(

        "Include Raw Output"

    )

    submit = SubmitField(

        "Save Report Settings"

    )


# ==========================================================
# Notification Settings
# ==========================================================

class NotificationSettingsForm(FlaskForm):

    enable_notifications = BooleanField(

        "Enable Notifications"

    )

    notify_scan_complete = BooleanField(

        "Notify When Scan Completes"

    )

    notify_scan_failed = BooleanField(

        "Notify When Scan Fails"

    )

    notify_critical = BooleanField(

        "Notify On Critical Findings"

    )

    notify_reports = BooleanField(

        "Notify When Report Is Generated"

    )

    submit = SubmitField(

        "Save Notification Settings"

    )