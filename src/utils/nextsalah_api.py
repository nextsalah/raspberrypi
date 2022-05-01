from pickletools import optimize
from requests import get
from .. import socketio

class NextSalahAPI():
    global API_URL, OPTIONS
    API_URL = "https://nextsalah.com/api/v1/prayertimes"
    OPTIONS = {
        "islamiska-forbundet" : {
            "url" : "/islamiska-forbundet",
            "argument" : "city",
        },
        "vaktijaba": {
            "url" : "/vaktijaba",
            "argument" : "location_id",
        },
        "vaktijaeu": {
            "url" : "/vaktijaeu",
            "argument": "location_slug",
        }
    }
    
    def get_options():
        output = {}
        for key, value in OPTIONS.items():
            try:
                data = get( API_URL + value['url'] + "/locations" )
                if data.status_code != 200:                    
                    raise Exception("API Error")
                output[key] = data.json()
            except:
                output[key] = []
        return output    
            
                
            
    def get_prayertimes(source, data):
        for key, value in OPTIONS.items():
            if key == source:
                try:
                    prayertimes = get(f'{API_URL}{value["url"]}?{value["argument"]}={data}')
                    if prayertimes.status_code != 200:
                        raise Exception(f"API Error - {source} - {data}")
                    return prayertimes.json()
                except Exception as e:
                    print(e)
                    return []