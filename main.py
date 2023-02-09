import requests
from datetime import datetime

############# CREATING A USER #############

pixela_endpoint = " https://pixe.la/v1/users"

TOKEN = "create a token for you"
USER_NAME = "chose a user name"
GRAPH_ID = "give a name for your graphs"
users_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

response = requests.post(url=pixela_endpoint,json=users_params)
print(response.text)

############# CREATING THE USER GRAPH #############

graphs_params = {
    "id": GRAPH_ID,
    "name": "Gym Graph",
    "unit": "calory",
    "type": "float",
    "color": "sora",

}

headers = {
    "X-USER-TOKEN": TOKEN
}


graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
response_graph = requests.post(url=graph_endpoint, json=graphs_params, headers=headers)
print(response_graph.text)

############# ADDING DAILY DATA #############

today = datetime.now()
post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many calories did you burn today")

}

post_p_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
response_pixel = requests.post(url=post_p_endpoint,json=post_params,headers=headers)
print(response_pixel.text)

############# CHANGING DATA #############

put_params = {

    "quantity": "15.5"

}

put_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response_put = requests.put(url=put_endpoint,json=put_params,headers=headers)
print(response_put.text)

############# DELETING DATA #############

delete_endpoint  = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response_delete = requests.delete(url=delete_endpoint,headers=headers)
print(response_delete.text)