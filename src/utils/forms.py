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
    

class LanguageForm(FlaskForm):
    """
    Language form.
    """
    monday = StringField('Monday', validators=[DataRequired(), Length(min=1, max=50)], default='Monday', render_kw={'placeholder': 'Monday'})
    tuesday = StringField('Tuesday', validators=[DataRequired(), Length(min=1, max=50)], default='Tuesday', render_kw={'placeholder': 'Tuesday'})
    wednesday = StringField('Wednesday', validators=[DataRequired(), Length(min=1, max=50)], default='Wednesday', render_kw={'placeholder': 'Wednesday'})
    thursday = StringField('Thursday', validators=[DataRequired(), Length(min=1, max=50)], default='Thursday', render_kw={'placeholder': 'Thursday'})
    friday = StringField('Friday', validators=[DataRequired(), Length(min=1, max=50)], default='Friday', render_kw={'placeholder': 'Friday'})
    saturday = StringField('Saturday', validators=[DataRequired(), Length(min=1, max=50)], default='Saturday', render_kw={'placeholder': 'Saturday'})
    sunday = StringField('Sunday', validators=[DataRequired(), Length(min=1, max=50)], default='Sunday', render_kw={'placeholder': 'Sunday'})

    january = StringField('January', validators=[DataRequired(), Length(min=1, max=50)], default='January', render_kw={'placeholder': 'January'})
    february = StringField('February', validators=[DataRequired(), Length(min=1, max=50)], default='February', render_kw={'placeholder': 'February'})
    march = StringField('March', validators=[DataRequired(), Length(min=1, max=50)], default='March', render_kw={'placeholder': 'March'})
    april = StringField('April', validators=[DataRequired(), Length(min=1, max=50)], default='April', render_kw={'placeholder': 'April'})
    may = StringField('May', validators=[DataRequired(), Length(min=1, max=50)], default='May', render_kw={'placeholder': 'May'})
    june = StringField('June', validators=[DataRequired(), Length(min=1, max=50)], default='June', render_kw={'placeholder': 'June'})
    july = StringField('July', validators=[DataRequired(), Length(min=1, max=50)], default='July', render_kw={'placeholder': 'July'})
    august = StringField('August', validators=[DataRequired(), Length(min=1, max=50)], default='August', render_kw={'placeholder': 'August'})
    september = StringField('September', validators=[DataRequired(), Length(min=1, max=50)], default='September', render_kw={'placeholder': 'September'})
    october = StringField('October', validators=[DataRequired(), Length(min=1, max=50)], default='October', render_kw={'placeholder': 'October'})
    november = StringField('November', validators=[DataRequired(), Length(min=1, max=50)], default='November', render_kw={'placeholder': 'November'})
    december = StringField('December', validators=[DataRequired(), Length(min=1, max=50)], default='December', render_kw={'placeholder': 'December'})
 
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