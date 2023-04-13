from config import *
import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
class FlightSearch:

    def __init__(self):
        pass
    
    def add_iataCode(self, city_name):
        headers = {
            "apikey": TEQUILA_API_KEY,
        }
        params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=F"{TEQUILA_ENDPOINT}/locations/query", params=params, headers=headers)
        city = response.json()["locations"]
        city_code = city[0]["code"]
        code = city_code
        return code