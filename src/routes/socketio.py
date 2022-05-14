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
    
