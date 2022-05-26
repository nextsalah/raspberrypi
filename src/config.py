class Config:
    SECRET_KEY = 'secret'
    UPLOAD_FOLDER = './static/upload'
    API_PREFIX = '/api'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_TRANSLATION_DIRECTORIES = './translations'
    WTF_CSRF_ENABLED = False
    SUPPORTED_LANGUAGES = [
        { 'language_name' : 'Bosnian' , 'language_code' : 'bs' },
        { 'language_name' : 'English' , 'language_code' : 'en' },
        { 'language_name' : 'Swedish' , 'language_code' : 'sv' }
    ]