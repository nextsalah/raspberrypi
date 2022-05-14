from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField

class SettingsForm(FlaskForm):
    """
    Settings form.
    """
    name = StringField('Name')