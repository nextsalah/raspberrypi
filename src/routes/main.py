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

@app.errorhandler( 404 )
def page_not_found(e):
    return render_template('generic/404.html'), 404

@main_routes.route( '/' )
def index():
    return render_template( 'index.html' , home = True)

 # -------- Dashboard --------
@main_routes.route( '/media' )
def media():
    return render_template('dashboard/media.html')

@main_routes.route( '/language' )
def language():
    return render_template('dashboard/language.html')

@main_routes.route( '/prayertimes' )
def prayertimes():
    return render_template('dashboard/prayertimes.html')

@main_routes.route( '/advanced' )
def advanced():
    return render_template('dashboard/advanced.html')

# -------- Advanced --------
@main_routes.route( '/settings' )
def settings():
    settings = Setting.query.filter_by( id = 1 ).one_or_none()
    return render_template( 'advanced/settings.html' , settings = settings)