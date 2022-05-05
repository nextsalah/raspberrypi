from .. import socketio
from ..utils.nextsalah_api import NextSalahAPI
from ..models import PrayerTimes
from .. import db

@socketio.on('connect', namespace='/dd')
def ws_conn():
    socketio.emit('msg', {'count': 1}, namespace='/dd')

@socketio.on('disconnect', namespace='/dd')
def ws_disconn():
    print('Disconnected')
    
@socketio.on('get_new_prayertimes')
def get_new_prayertimes(json):
    source, data = json['source'], json['data']
    new_prayertimes = NextSalahAPI.get_prayertimes(source, data)
    NextSalahAPI.save_prayertimes(new_prayertimes)

    if new_prayertimes != None and new_prayertimes != []:
        socketio.emit('alert', {'message': "New prayertimes successfully added."})
    else:
        socketio.emit('alert', {'message': "Failed to add new prayertimes."})