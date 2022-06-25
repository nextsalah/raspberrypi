from src import create_app, socketio
import argparse

app = create_app()    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-dp', '--debug_port', help='Debug port', type=int, required=False, dest='debug_port')
    custom_port = parser.parse_args().debug_port if parser.parse_args().debug_port else 80

    # Run the socketio server
    socketio.run( app , host='0.0.0.0' , debug=True , port=custom_port)
