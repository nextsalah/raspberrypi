from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length

class SettingsForm(FlaskForm):
    """
    Settings form.
    """
    time_format = StringField('Time format', validators=[DataRequired()], default='%H:%M:%S', render_kw={'placeholder': '%H:%M:%S'})
    date_format = StringField('Date Format', validators=[DataRequired()], default='DD/MM/YYYY', render_kw={'placeholder': 'DD/MM/YYYY'})
    iqamah_bool = BooleanField('Display Iqamah', default=True)
    qr_code_bool = BooleanField('Display QR-code', default=True)