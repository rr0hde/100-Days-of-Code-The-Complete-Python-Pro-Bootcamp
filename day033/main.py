import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 33.263850
MY_LONG = -111.629780

MY_EMAIL = "randomemailaddress714@gmail.com"
PASSWORD = "NYny&%x1zaq1"


def in_range():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_time = int(time_now.strftime("%H"))
    if sunset <= current_time <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_night() and in_range():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="brent.lacorte@gmail.com",
                                msg=f"Subject:ISS IN RANGE\n\nTHE ISS IS IN RANGE"
                                )