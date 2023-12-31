import requests
import os

SHEET_ENDPOINT = f"https://api.sheety.co/{os.environ.get("SHEET_ENDPOINT")}"
bearer_headers = {"Authorization": f"Basic {os.environ.get("SHEET_API_KEY")}"}

class DataManager:
    def __init__(self):
        self.response = requests.get(url=SHEET_ENDPOINT, headers=bearer_headers)
        self.sheet_data = self.response.json()["prices"]
    def update_data(self):
        for city in self.sheet_data:
            new_data={
                "price": {
                    "iataCode":city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEET_ENDPOINT}/{city["id"]}",headers=bearer_headers,json=new_data)