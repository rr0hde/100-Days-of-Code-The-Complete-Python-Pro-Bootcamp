import datetime as dt
import random
import smtplib

MY_EMAIL = "randomemailaddress714@gmail.com"
PASSWORD = "NYny&%x1zaq1"
today = dt.datetime.now()
day_of_week = today.weekday()

if day_of_week == 1:
    with open(file="quotes.txt", mode="r") as quotes:
        quote_list = quotes.readlines()
        random_quote = random.choice(quote_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="brent.lacorte@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n{random_quote}"
                            )
