import requests

SHEETY_ENDPOINT = "https://api.sheety.co/19a6fcd2eaf10061b52167d3ea0decf7/flightDeals/users"
BEARER_HEADER = {
    "Authorization": "Bearer CUNHell@2030"
}

    
print("Hello and welcome to Namlah's Flight Club.\nWe find the best flight deals and email them to you.")
first_name = input("Enter your first name.\n")
last_name = input("Enter your last name.\n")
emai_address_1 = input("Enter your email.\n")
emai_address_2 = input("Enter your email, again.\n")

if emai_address_1 == emai_address_2:
    print("You're in the club!")   

ret_response = requests.get(url=SHEETY_ENDPOINT, headers=BEARER_HEADER)
data_list = ret_response.json()["users"]
query = {
    "user":{
    "firstName":first_name,
    "lastName":last_name,
    "email": emai_address_2
    }
}
response = requests.post(url=SHEETY_ENDPOINT,headers=BEARER_HEADER,json=query)
data = response.json()
print(data)

