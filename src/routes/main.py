import os

from flask import Blueprint, flash, render_template, send_from_directory, redirect, url_for
from requests import request
from src import app, db

from ..models import Medias, Settings
from ..utils.forms import SettingsForm
from ..utils.nextsalah_api import NextSalahAPI

main_routes = Blueprint( 'main' ,  __name__ )


# -------- Root --------
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
    options = NextSalahAPI.get_options()
    return render_template('dashboard/prayertimes.html', options = options)

@main_routes.route( '/advanced' )
def advanced():
    return render_template('dashboard/advanced.html')




# -------- Advanced --------
@main_routes.route( '/settings' , methods = ['GET', 'POST'] )
def settings():
    settings = Settings.query.get_or_404(1)
    form = SettingsForm(obj = settings)
    
    if form.validate_on_submit():
        form.populate_obj(settings)
        db.session.commit()
        flash('Settings saved successfully!', 'success')
        return redirect(url_for('main.index')) 
    
    return render_template( 'advanced/settings.html' , form = form)

@main_routes.route( '/screen' , methods = [ 'GET' ] )
def screen():
    return "Screen"





# -------- Utils --------
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')
@app.before_first_request
def before_first_request():
    if Settings.query.one_or_none() is None:
        db.session.add( Settings(id = 1 ))
        print(' Inserted a new Setting object into the database with id = 1.')
        
    if Medias.query.one_or_none() is None:
        print(' Inserted a new Media object into the database with id = 1.')
        db.session.add( Medias( id = 1))
        
    db.session.commit()
@app.errorhandler( 404 )
def page_not_found( error):
    return render_template('generic/404.html'), 404
