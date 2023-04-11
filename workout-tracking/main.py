import requests
from datetime import datetime

APP_ID = ""
API_KEY = ""

NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = f"https://api.sheety.co/40f11ac21102be9c157ee3291cf7cf72/myWorkouts/workouts"

headers = {
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

response_nutritionix = requests.post(url=NUTRI_ENDPOINT, json=nutri_parameters, headers=headers)
response_nutritionix.raise_for_status()
workout_info = response_nutritionix.json()
print(workout_info)

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

    response_sheety = requests.post(url=SHEETY_ENDPOINT, json=sheety_parameters)
    response_sheety.raise_for_status()
    print(response_sheety.text)
