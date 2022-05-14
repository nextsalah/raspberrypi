from functools import wraps
import logging

log = logging.getLogger(__name__)

def catch_errors(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
            return result
        except (Exception, RuntimeError) as exc:
            log.error('Error: ' + str(exc))
            return 
    return wrapped

