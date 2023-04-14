from config import *
from flight_data import FlightData
import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"

class FlightSearch:

    def add_iataCode(self, city_name):
        headers = {
            "apikey": TEQUILA_API_KEY,
        }
        params_code = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=F"{TEQUILA_ENDPOINT}/locations/query", params=params_code, headers=headers)
        city = response.json()["locations"]
        city_code = city[0]["code"]
        return city_code
    
    def check_for_flights(self, origin_code, destination_code, from_date, to_date):
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        params_flights = {
            "fly_from": origin_code,
            "fly_to": destination_code,
            "date_from:": from_date.strftime("%d/%m/%Y"),
            "date_to": to_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 1,
            "curr": "BRL"
        }
        
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=params_flights)
        
        try: 
            data = response.json()["data"][0]    
        except IndexError:
            print(f"No flights found for {destination_code}.")
            return None
        
        fligh_data = FlightData(
            price=data["price"],
            origin=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            go_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        
        print(f"{fligh_data.destination}: R${fligh_data.price}")
        return fligh_data