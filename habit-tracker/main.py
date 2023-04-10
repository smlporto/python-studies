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

graph_params = {
    "id": GRAPH_ID,
    "name": "LearningPixela",
    "unit": "Hours",
    "type": "float",
    "color": "ichou"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

user_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{user_endpoint}/{USERNAME}/graphs"

#response = requests.post(url=user_endpoint, json=user_params)
#print(response.text)

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)

