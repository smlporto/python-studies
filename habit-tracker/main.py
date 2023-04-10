import requests

USERNAME = "smlporto"
TOKEN = ""
GRAPH_ID = "t001"

user_params ={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

user_endpoint = "https://pixe.la/v1/users"

response = requests.post(url=user_endpoint, json=user_params)
print(response.text)

