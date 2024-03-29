import requests
from datetime import datetime
import os
from config import *

NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutri_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

nutri_parameters = {
    "query": input("Tell me wich exercises you did: "),
    "gender":"male",
    "weight_kg":64,
    "height_cm":174.00,
    "age":22
}

response_nutritionix = requests.post(url=NUTRI_ENDPOINT, json=nutri_parameters, headers=nutri_headers)
response_nutritionix.raise_for_status()
workout_info = response_nutritionix.json()

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

for exercise in workout_info["exercises"]:
    sheety_parameters = {
        "workout": {
            "date": datetime.now().strftime('%d/%m/%Y'),
            "time": datetime.now().strftime('%H:%M:%S'),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # response_sheety = requests.get(url=SHEETY_ENDPOINT)
    # response_sheety.raise_for_status()
    # print(response_sheety.json())

    response_sheety = requests.post(url=SHEETY_ENDPOINT, json=sheety_parameters, headers=sheety_headers)
    response_sheety.raise_for_status()
