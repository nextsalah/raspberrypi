from flask import Blueprint
from src import app, db
from src.models import Setting, Media
main_routes = Blueprint( 'main' ,  __name__ )

@app.before_first_request
def before_first_request():
    if Setting.query.one_or_none() is None:
        db.session.add( Setting(id = 1 ))
        print(' Inserted a new Setting object into the database with id = 1.')
        
    if Media.query.one_or_none() is None:
        print(' Inserted a new Media object into the database with id = 1.')
        db.session.add( Media( id = 1))
        
    db.session.commit()

@main_routes.route( '/' )
def index():
    return "Hello, World! Main Blueprint"
