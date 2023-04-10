import requests
from datetime import datetime

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

add_pixel_params = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": input("How many hours did you study Pixelas today? "),
}

new_pixel_params = {
    "quantity": "2"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

user_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{user_endpoint}/{USERNAME}/graphs"
add_pixel_endpoint = f"{user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
update_delete_pixel_endpoint = f"{user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{datetime.now().strftime('%Y%m%d')}"

#response = requests.post(url=user_endpoint, json=user_params)
#print(response.text)

#response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
#print(response.text)

response = requests.post(url=add_pixel_endpoint, json=add_pixel_params, headers=headers)
print(response.text)

#response = requests.put(url=update_pixel_endpoint, json=new_pixel_params, headers=headers)
#print(response.text)

#response = requests.delete(url=update_delete_pixel_endpoint, headers=headers)
#print(response.text)