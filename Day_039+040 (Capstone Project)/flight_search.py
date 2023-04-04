import requests
from flight_data import FlightData
import os

KIWI_ENDPOINT = "https://api.tequila.kiwi.com"
KIWI_API_KEY = os.environ["KIWI_API_KEY"]

HEADERS = {"apikey":KIWI_API_KEY}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        location_endpoint = f"{KIWI_ENDPOINT}/locations/query"
        query = {
            "term": city_name, 
            "location_types": "city"
            }

        response = requests.get(url=location_endpoint, headers=HEADERS, params=query)
        result = response.json()["locations"]
        code = result[0]["code"]
        return code
    

    def find_flights(self, from_city, to_city, from_time,to_time):
        search_endpoint = f"{KIWI_ENDPOINT}/v2/search"
        query = {
            "fly_from":from_city,
            "fly_to":to_city,
            "date_from":from_time.strftime("%d/%m/%Y"),
            "date_to":to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from":7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "AED"
        }
        response = requests.get(url=search_endpoint, headers=HEADERS, params=query)

        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 1
            data = response.json()["data"][0]

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            return flight_data


    
    