from ..models import PrayerTimes
from .. import db
from requests import get
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
            return []
        
    return wrapped

class NextSalahAPI():
    """
        Wrapper for the API
    """
    
    global API_URL, OPTIONS
    API_URL = "https://nextsalah.com/api/v1/prayertimes"
    OPTIONS = {
        "islamiska-forbundet" : {
            "url" : "/islamiska-forbundet"
        },
        "vaktijaba": {
            "url" : "/vaktijaba"
        },
        "vaktijaeu": {
            "url" : "/vaktijaeu"
        }
    }
    

    def get_options():
        """
        It gets all the avvaliable options for the API
        """
        output = {}
        for key, value in OPTIONS.items():
            try:
                url = API_URL + value['url'] + "/locations" 
                response = get( url )
                if response.status_code != 200:
                    raise RuntimeError( "Error: " + str(response.status_code) )
                output[key] = response.json()
            except Exception as exc:
                log.error('API Error: ' + str(exc) + " " + str(url))
                output[key] = []
                
        return output

            
                
    @catch_errors 
    def get_prayertimes(source, data):
        """
        Gets the prayertimes from the API
        
        :param source (str): The source of the API
        :param data (dict): The city name or the latitude and longitude of the city
        
        :return: A list of dictionaries with prayertimes
        """
        for key, value in OPTIONS.items():
            if key == source:
                print(" Getting prayertimes from " + key + "...")
                url = f'{API_URL}{value["url"]}?{value["argument"]}={data}'
                prayertimes = get( url )
                if prayertimes.status_code != 200:
                    raise Exception(f"API Error {prayertimes.status_code} - {url}")
                
                prayertimes_json = prayertimes.json()
                if prayertimes_json['success']:
                    print(" Done.")
                    return prayertimes_json['prayertimes']
                
                raise Exception(f"Server error 500 - {source} - {data}")

    @catch_errors
    def save_prayertimes( new_prayertimes: list ):
        if new_prayertimes != None and new_prayertimes != []:
            db.session.query(PrayerTimes).delete()
            [ db.session.add(PrayerTimes(**prayertimes)) for prayertimes in new_prayertimes ]
            db.session.commit()
