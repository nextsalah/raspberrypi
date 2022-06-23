from email.policy import default
import os

from flask import Blueprint, flash, render_template, send_from_directory, redirect, url_for, send_from_directory
from src import app, db

from ..models import Settings, Language
from ..utils.forms import LanguageForm, SettingsForm
from ..utils.nextsalah_api import NextSalahAPI

main_routes = Blueprint( 'main' ,  __name__ )


# -------- Root --------
@main_routes.route( '/' )
def index():
    return render_template( 'index.html' , home = True)


# -------- Main Screen --------
@main_routes.route( '/screen', defaults={'path': ''} )
@main_routes.route( '/screen/<path:path>' )
def main_screen( path ):
    debug_path = '/home/ismail424/nextsalah/raspberrypi/venv/test'
    if path != "" and os.path.exists( debug_path + '/' + path ):
        return send_from_directory( debug_path , path )
    else:
        return send_from_directory(debug_path, 'index.html')



 # -------- Dashboard --------
@main_routes.route( '/theme' )
def theme():
    return render_template('dashboard/theme.html')

@main_routes.route( '/language' , methods = ['GET', 'POST']  )
def language():
    language =  Language.query.get_or_404(1)
    form = LanguageForm(obj=language)
    
    if form.validate_on_submit():
        form.populate_obj(language)
        db.session.commit()
        flash('Language updated successfully.', 'success')
        return redirect(url_for('main.index'))
    

    return render_template('dashboard/language.html', form = form)

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
    
    return render_template( 'dashboard/settings.html' , form = form)

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
        

    if Language.query.one_or_none() is None:
        print(' Inserted a new Language object into the database with id = 1.')
        db.session.add( Language( id = 1))
        
    db.session.commit()
    
    
@app.errorhandler( 404 )
def page_not_found( error):
    return render_template('generic/404.html'), 404
