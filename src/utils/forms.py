from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length
from .. import app
from src.models import Language

class SettingsForm(FlaskForm):
    """
    Settings form.
    """
    time_format = StringField('Time format', validators=[DataRequired(), Length(min=1, max=20)], default='%H:%M:%S', render_kw={'placeholder': '%H:%M:%S'})
    date_format = StringField('Date Format', validators=[DataRequired(), Length(min=1, max=20)], default='DD/MM/YYYY', render_kw={'placeholder': 'DD/MM/YYYY'})
    iqamah_bool = BooleanField('Display Iqamah', default=True)
    qr_code_bool = BooleanField('Display QR-code', default=True)

class LanguageForm(FlaskForm):
    """
    Language form.
    """  
    fajr = StringField('Fajr', validators=[DataRequired(), Length(min=1, max=50)], default='Fajr', render_kw={'placeholder': 'Fajr'})
    sunrise = StringField('Sunrise', validators=[DataRequired(), Length(min=1, max=50)], default='Sunrise', render_kw={'placeholder': 'Sunrise'})
    dhuhr = StringField('Dhuhr', validators=[DataRequired(), Length(min=1, max=50)], default='Dhuhr', render_kw={'placeholder': 'Dhuhr'})
    asr = StringField('Asr', validators=[DataRequired(), Length(min=1, max=50)], default='Asr', render_kw={'placeholder': 'Asr'})
    maghrib = StringField('Maghrib', validators=[DataRequired(), Length(min=1, max=50)], default='Maghrib', render_kw={'placeholder': 'Maghrib'})
    isha = StringField('Isha', validators=[DataRequired(), Length(min=1, max=50)], default='Isha', render_kw={'placeholder': 'Isha'})
    
    prayer = StringField('Prayer', validators=[DataRequired(), Length(min=1, max=50)], default='Prayer', render_kw={'placeholder': 'Prayer'})
    iqamah = StringField('Iqamah', validators=[DataRequired(), Length(min=1, max=50)], default='Iqamah', render_kw={'placeholder': 'Iqamah'})
    begins = StringField('Begins', validators=[DataRequired(), Length(min=1, max=50)], default='Begins', render_kw={'placeholder': 'Begins'})
    next = StringField('Next (text)', validators=[DataRequired(), Length(min=1, max=50)], default='Next...', render_kw={'placeholder': 'Next...'})
    turn_off_phone = StringField('Turn off phone (text)', validators=[DataRequired(), Length(min=1, max=50)], default='Please, turn off your phones', render_kw={'placeholder': 'Please, turn off your phones'})