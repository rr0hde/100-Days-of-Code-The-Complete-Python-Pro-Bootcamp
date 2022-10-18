import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "randomemailaddress714@gmail.com"
PASSWORD = "NYny&%x1zaq1"
today = dt.datetime.now()
day = today.day
month = today.month

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

for k in data_dict:
    if day == k["day"] and month == k["month"]:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r") as letter:
            letter_data = letter.read()

        letter_data = letter_data.replace("[NAME]", k["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=k["email"],
                                msg=f"Subject:Happy Birthday!\n\n{letter_data}"
                                )
