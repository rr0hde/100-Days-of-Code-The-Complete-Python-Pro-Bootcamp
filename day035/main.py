import requests
from twilio.rest import Client

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = "8362a42710866117c52c023105379ab3"

account_sid = "ACf772fa6713b8985ef23c5b838c8bdae3"
auth_token = "5f624f631e4b92a2bdca8894957f8e67"

parameters = {
    "lat": 55.059750,
    "lon": 10.606870,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
#
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_='+18142613653',
        to='+14805282664'
    )
    print(message.status)