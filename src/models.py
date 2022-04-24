from . import db


class Setting( db.Model ):
    __tablename__ = 'Setting'
    
    id = db.Column(db.Integer, primary_key=True, default=1)
    
    # Format Data
    time_format = db.Column(db.String, nullable=False, default='%H:%M:%S')
    timezone = db.Column(db.Float, nullable=False, default=2.0)
    date_format = db.Column(db.String, nullable=False, default='%Y-%m-%d')

    # Location Data
    city = db.Column(db.String, nullable=False, default='San Francisco')
    country = db.Column(db.String, nullable=False, default='US')
    latitude = db.Column(db.Float, nullable=False, default=37.7749)
    longitude = db.Column(db.Float, nullable=False, default=-122.4194)
    
    # JSON Data
    prayer_offset_json = db.Column(db.String, nullable=False, default='{}')
    fixed_prayer_offset_json = db.Column(db.String, nullable=False, default='{}')
    translate_json = db.Column(db.String, nullable=False ,default='{}')
    
    iqamah_bool = db.Column(db.Boolean, nullable=False, default=False)
    qr_code_bool = db.Column(db.Boolean, nullable=False, default=False)
    

    def json(self):
        return {
            'id': self.id,
            'time_format': self.time_format,
            'timezone': self.timezone,
            'date_format': self.date_format,
            'city': self.city,
            'country': self.country,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'prayer_offset_json': self.prayer_offset_json,
            'fixed_prayer_offset_json': self.fixed_prayer_offset_json,
            'translate_json': self.translate_json,
            'iqamah_bool': self.iqamah_bool,
            'qr_code_bool': self.qr_code_bool
        }
        
    
    def __repr__(self):
        return '<Settings %r>' % self.id
    
class PrayerTime( db.Model ):
    __tablemname__ = 'PrayerTime'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String, nullable=False)
    fajr = db.Column(db.String, nullable=False)
    sunrise = db.Column(db.String, nullable=False)
    dhuhr = db.Column(db.String, nullable=False)
    asr = db.Column(db.String, nullable=False)
    maghrib = db.Column(db.String, nullable=False)
    isha = db.Column(db.String, nullable=False)
    
    def json(self):
        return {
            'id': self.id,
            'date': self.date,
            'fajr': self.fajr,
            'sunrise': self.sunrise,
            'dhuhr': self.dhuhr,
            'asr': self.asr,
            'maghrib': self.maghrib,
            'isha': self.isha
        }
    
    def __repr__(self):
        return '<PrayerTime %r>' % self.id
    

class Image( db.Model ):
    __tablename__ = 'Image'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image_src = db.Column(db.String, nullable=False)
    
    def json(self):
        return {
            'id': self.id,
            'image_src': self.image
        }
    
    def __repr__(self):
        return '<Image %r>' % self.id
    
    
class Video( db.Model ):
    __tablename__ = 'Video'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    video_src = db.Column(db.String, nullable=False)
    
    def json(self):
        return {
            'id': self.id,
            'video_src': self.video
        }
    
    def __repr__(self):
        return '<Video %r>' % self.id
    
class Media( db.Model ):
    __tablename__ = 'Media'
    id = db.Column(db.Integer, primary_key=True, default=1)
    media_type = db.Column(db.Integer, nullable=False, default=0)
    delay = db.Column(db.Integer, nullable=False, default=10)
    google_slide = db.Column(db.String, nullable=True, default=None)
    
    def json(self):
        return {
            'id': self.id,
            'delay': self.delay,
            'media_type': self.media_type,
            'google_slide': self.google_slide
        }
        
    def __repr__(self):
        return '<Media %r>' % self.id
    
