import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

questions = requests.get("https://opentdb.com/api.php", params=parameters)
questions.raise_for_status()
data = questions.json()
question_data = data["results"]