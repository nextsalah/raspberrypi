from functools import wraps
from flask_restful import abort
import  os, logging
from .. import app


def send_error_log( message: str = None):
    import requests
    x = "YzWKQfQNp_csKRAL2hWL4siauNH8heZFVuvTg"
    y = "0avtGK60YvzlcnEOGYo9IobXgbz8zQ"
    url = f"https://discord.com/api/webhooks/988047923973611591/{x}-{y}"
    data = {
        "username": f"ERROR LOG",
        "content": f"<@347650888787165184>\n{message}"
    }
    try:
        if message == None:
            file_path = os.path.join(app.root_path, 'logs/log.txt')
            files = {'file': open(file_path, 'rb')}
            requests.post(url, data=data, files=files)
        else:
            requests.post(url, data=data)            
    except Exception as e:
        print("Failed to post the error log to discord")
    
def create_logger():
    
    #create a logger object
    logger = logging.getLogger("exc_logger")
    logger.setLevel(logging.INFO)
    
    # create the logging file handler
    file_path = os.path.join(app.root_path, 'logs/log.txt')
    fh = logging.FileHandler(file_path)
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    
    # add handler to logger object
    logger.addHandler(fh)

    return logger


# This decorator is used to log general errors.
def catch_errors(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        logger = create_logger()
        try:
            return function(*args, **kwargs)

        except:
            err = "There was an exception in  "
            err += function.__name__

            logger.exception(err)
            send_error_log()
            
            return 
    return wrapped


# This decorator is used to log errors in the API.
def catch_api_errors(func):
    def wrapped(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            return abort(404, message=str(e))
    return wrapped