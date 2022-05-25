from . import db
from .utils.error_handling import catch_errors

class Base():
    def json(row):
        d = {}
        for column in row.__table__.columns:
            d[column.name] = str(getattr(row, column.name))
        return d
    
class Settings( Base, db.Model ):
    __tablename__ = 'Settings'
    
    id = db.Column(db.Integer, primary_key=True, default=1)

    # Format Data
    time_format = db.Column(db.String, nullable=False, default='%H:%M:%S', server_default='%H:%M:%S')
    timezone = db.Column(db.Float, nullable=False, default=2.0, server_default="2.0")
    date_format = db.Column(db.String, nullable=False, default='%Y-%m-%d', server_default='%Y-%m-%d')

    # Location Data
    city = db.Column(db.String, nullable=False, default='San Francisco', server_default='San Francisco')
    country = db.Column(db.String, nullable=False, default='US', server_default='US')
    latitude = db.Column(db.Float, nullable=False, default=37.7749, server_default="37.7749")
    longitude = db.Column(db.Float, nullable=False, default=-122.4194, server_default="-122.4194")
    
    # JSON Data
    prayer_offset_json = db.Column(db.String, nullable=False, default='{}', server_default='{}')
    fixed_prayer_offset_json = db.Column(db.String, nullable=False, default='{}', server_default='{}')

    iqamah_bool = db.Column(db.Boolean, nullable=False, default=False, server_default="False")
    qr_code_bool = db.Column(db.Boolean, nullable=False, default=False, server_default="False")

    def __repr__(self):
        return '<Settings %r>' % self.id
    
class PrayerTimes( Base , db.Model ):
    __tablename__ = 'PrayerTimes'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String, nullable=False)
    fajr = db.Column(db.String, nullable=False)
    sunrise = db.Column(db.String, nullable=False)
    dhuhr = db.Column(db.String, nullable=False)
    asr = db.Column(db.String, nullable=False)
    maghrib = db.Column(db.String, nullable=False)
    isha = db.Column(db.String, nullable=False)

    @catch_errors
    def save_prayertimes( new_prayertimes: list ):
        if new_prayertimes != None and new_prayertimes != []:
            try:
                db.session.query(PrayerTimes).delete()
                [ db.session.add(PrayerTimes(**prayertimes)) for prayertimes in new_prayertimes ]
                db.session.commit()
                return True
            except:
                pass
        return False
    
    
    def __repr__(self):
        return '<PrayerTime %r>' % self.id
    

class Images( Base , db.Model ):
    __tablename__ = 'Images'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image_src = db.Column(db.String, nullable=False)
    
    def json(self):
        return {
            'id': self.id,
            'image_src': self.image
        }
    
    def __repr__(self):
        return '<Image %r>' % self.id
    
    
class Videos( Base , db.Model ):
    __tablename__ = 'Videos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    video_src = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return '<Video %r>' % self.id
    
class Medias( db.Model ):
    __tablename__ = 'Medias'
    id = db.Column(db.Integer, primary_key=True, default=1)
    media_type = db.Column(db.Integer, nullable=False, default=0, server_default="0")
    delay = db.Column(db.Integer, nullable=False, default=10, server_default="10")
    google_slide = db.Column(db.String, nullable=True, default=None, server_default="None")

    def __repr__(self):
        return '<Media %r>' % self.id
    

class Language( Base , db.Model ):
    __tablename__ = 'Language'
    
    id = db.Column(db.Integer, primary_key=True, default=1)

    # Weekdays
    monday = db.Column(db.String, nullable=False, default='Monday', server_default='Monday')
    tuesday = db.Column(db.String, nullable=False, default='Tuesday', server_default='Tuesday')
    wednesday = db.Column(db.String, nullable=False, default='Wednesday', server_default='Wednesday')
    thursday = db.Column(db.String, nullable=False, default='Thursday', server_default='Thursday')
    friday = db.Column(db.String, nullable=False, default='Friday', server_default='Friday')
    saturday = db.Column(db.String, nullable=False, default='Saturday', server_default='Saturday')
    sunday = db.Column(db.String, nullable=False, default='Sunday', server_default='Sunday')

    # Months
    january = db.Column(db.String, nullable=False, default='January', server_default='January')
    february = db.Column(db.String, nullable=False, default='February', server_default='February')
    march = db.Column(db.String, nullable=False, default='March', server_default='March')
    april = db.Column(db.String, nullable=False, default='April', server_default='April')
    may = db.Column(db.String, nullable=False, default='May', server_default='May')
    june = db.Column(db.String, nullable=False, default='June', server_default='June')
    july = db.Column(db.String, nullable=False, default='July', server_default='July')
    august = db.Column(db.String, nullable=False, default='August', server_default='August')
    september = db.Column(db.String, nullable=False, default='September', server_default='September')
    october = db.Column(db.String, nullable=False, default='October', server_default='October')
    november = db.Column(db.String, nullable=False, default='November', server_default='November')
    december = db.Column(db.String, nullable=False, default='December', server_default='December')

    # Prayer Times
    fajr = db.Column(db.String, nullable=False, default='Fajr', server_default='Fajr')
    sunrise = db.Column(db.String, nullable=False, default='Sunrise', server_default='Sunrise')
    dhuhr = db.Column(db.String, nullable=False, default='Dhuhr', server_default='Dhuhr')
    asr = db.Column(db.String, nullable=False, default='Asr', server_default='Asr')
    maghrib = db.Column(db.String, nullable=False, default='Maghrib', server_default='Maghrib')
    isha = db.Column(db.String, nullable=False, default='Isha', server_default='Isha')
    
    prayer = db.Column(db.String, nullable=False, default='Prayer', server_default='Prayer')
    iqamah = db.Column(db.String, nullable=False, default='Iqamah', server_default='Iqamah')
    begins = db.Column(db.String, nullable=False, default='Begins', server_default='Begins')
    next = db.Column(db.String, nullable=False, default='Next...', server_default='Next...')
    turn_off_phone = db.Column(db.String, nullable=False, default='Please, turn off your phones', server_default='Please, turn off your phones')