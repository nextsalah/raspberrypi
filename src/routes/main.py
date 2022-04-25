from flask import Blueprint, render_template, send_from_directory
from src import app, db
from src.models import Setting, Media
import os


main_routes = Blueprint( 'main' ,  __name__ )

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')

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
    return render_template( 'index.html' )
