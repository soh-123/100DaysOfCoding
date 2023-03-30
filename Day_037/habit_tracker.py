import requests
from datetime import datetime

USERNAME = "sohier20"
TOKEN = "lkjh123lkj123"
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
value_endpoint = f"{graph_endpoint}/{GRAPHID}"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

graph_params = {
    "id":GRAPHID,
    "name":"Cycling graph",
    "unit":"Km",
    "type":"float",
    "color":"ichou"
}

today = datetime.now()
value_params = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"20"
}
put_endpoint = f"{value_endpoint}/{today}"
put_params = {
    "quantity":"18.4",
}

# response = requests.post(url=value_endpoint, json=value_params, headers=headers)
response = requests.put(url=put_endpoint, params=put_params, headers=headers)
print(response.text)