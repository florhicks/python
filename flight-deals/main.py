from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.sheet_data

ORIGIN_CITY = "BUE"

if sheet_data[0]["iataCode"] == "":
    for city in sheet_data:
        city["iataCode"] = flight_search.search_IATA(city["city"])

    data_manager.sheet_data = sheet_data
    data_manager.update_data()

for city in sheet_data:
    flight = flight_search.check_flights(ORIGIN_CITY,city["iataCode"])