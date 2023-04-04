import requests


PRICE_ENDPOINT = "https://api.sheety.co/19a6fcd2eaf10061b52167d3ea0decf7/flightDeals/prices"
USER_ENDPOINT = "https://api.sheety.co/19a6fcd2eaf10061b52167d3ea0decf7/flightDeals/users"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}


    def get_destination_data(self):
        sheet_response = requests.get(PRICE_ENDPOINT)
        data = sheet_response.json()
        self.detination_data = data["prices"]
        return self.detination_data
    

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{PRICE_ENDPOINT}/{city['id']}",json=new_data)
            print(response.text)
    
    def get_customer_emails(self):
        response = requests.get(USER_ENDPOINT)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data