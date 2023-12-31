import requests
import os
from twilio.rest import Client

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

API_KEY = os.environ.get("API_KEY")

LAT = 0
LONG = 0

ONW_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

params = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "units": "metric",
    "lang": "es"
}

response = requests.get(url=ONW_ENDPOINT, params=params)
response.raise_for_status()
weather_data = response.json()["list"][:4]
weather_hours = [key["weather"][0]["id"] for key in weather_data]

will_rain = False
for _ in weather_hours:
    if _ < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body='Hoy va a llover.',
        from_="",
        to=""
    )
    print(message.status)