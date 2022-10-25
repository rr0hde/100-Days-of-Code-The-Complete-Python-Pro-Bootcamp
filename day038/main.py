import requests
from datetime import datetime as dt
import os

print(os.environ)

NUTRI_API = "183ab58730d198ecc9c6879c6f5ccb19"
NUTRI_ID = os.environ.get("NT_APP_ID")  # f89ff06b

NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/b7f7ca708e53f4cf04563bfa8da1d0c8/workoutTracking/workouts"

today = dt.now().strftime("%d/%m/%Y")
time = dt.now().strftime("%X")


params = {
    "query": input("Tell me which exercises you did: "),
    "gender": "male",
    "weight_kg": 102.06,
    "height_cm": 190.5,
    "age": 37,
}

header = {
    "x-app-id": NUTRI_ID,
    "x-app-key": NUTRI_API
}

nutri_response = requests.post(url=NUTRI_ENDPOINT, json=params, headers=header)
nutri_result = nutri_response.json()

for exercise in nutri_result["exercises"]:
    sheety_param = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

header = {
    "Authorization": "Basic IHJyb2hkZTpOWW55JiV4MXphcTE="
}

sheety_get = requests.get(url=SHEETY_ENDPOINT)

sheety_post = requests.post(url=SHEETY_ENDPOINT, json=sheety_param, headers=header)
