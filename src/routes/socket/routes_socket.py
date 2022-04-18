from src import socketio

@socketio.on('test')
def test(json):
    return json

