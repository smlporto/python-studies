import requests
from config import *

class DataManager:

    def __init__(self):
        self.destiny_info = {}
        
    def get_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destiny_info = data["prices"]
        return self.destiny_info
        
    def update_data(self):
        for city in self.destiny_info:
            new_info = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_info)
            print(response.json())