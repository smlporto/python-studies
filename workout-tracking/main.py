import requests

APP_ID = ""
API_KEY = ""
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query": input("Tell me wich exercises you did: "),
    "gender":"male",
    "weight_kg":64,
    "height_cm":174.00,
    "age":22
}

response = requests.post(url=ENDPOINT, json=parameters, headers=headers)
response.raise_for_status()
print(response.json())
