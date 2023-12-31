import requests
from datetime import datetime, timedelta
from flight_data import FlightData
import os

today = datetime.now()
tomorrow =  today + timedelta(1)
tomorrow = tomorrow.strftime("%d/%m/%Y")
six_months =  today + timedelta(30*6)
six_months = six_months.strftime("%d/%m/%Y")


TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")

headers = {"apikey": TEQUILA_API_KEY}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass
    def search_IATA(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"

        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        IATA_code = results[0]["code"]
        return IATA_code
    def check_flights(self,fly_from,fly_to):
        query = {
            "fly_from":fly_from,
            "fly_to":fly_to,
            "date_from": tomorrow,
            "date_to":six_months,
            "one_for_city":1,
            "curr":"ARS"
        }
        response=requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers,params=query)

        try:
            search_data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {fly_to}.")
            return None

        flight_data=FlightData(
            price=search_data["price"],
            origin_city=search_data["cityFrom"],
            destination_city=search_data["cityTo"],
            out_date=search_data["route"][0]["local_departure"],
            return_date=search_data["route"][-1]["local_arrival"]

        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data