import requests
import os

from datetime import datetime as dt

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

API_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = f"https://api.sheety.co/{os.environ.get("SHEET_ENDPOINT")}/workoutTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")

GENDER = "YOUR GENDER"
WEIGHT_KG = 0
HEIGHT_CM = 0
AGE = 0

params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

bearer_headers = {
    "Authorization": f"Bearer {os.environ.get("TOKEN")}"
}

today_date = dt.now().strftime("%d/%m/%Y")
now_time = dt.now().strftime("%X")

response = requests.post(API_END_POINT, json=params, headers=headers)
result = response.json()["exercises"]

for exercise in result:
    exercise_content = {"workout": {
        "date": today_date,
        "time": now_time,
        "exercise": exercise["user_input"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]}
    }

    sheet_response = requests.post(
            SHEET_ENDPOINT,
            json=exercise_content,
            headers=bearer_headers
        )
    print(sheet_response.text)