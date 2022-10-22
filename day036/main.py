import requests
from datetime import datetime as dt
from datetime import timedelta as td
from twilio.rest import Client

today = dt.date(dt.today())
yesterday = today - td(days=1)
day_before = yesterday - td(days=1)
week_back = today - td(days=7)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_endpoint = "https://www.alphavantage.co/query?"
stock_api = "PR0DSZT02C5R3Z91"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api
}

stock_response = requests.get(stock_endpoint, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()

yesterday_close = float(stock_data["Time Series (Daily)"][str(yesterday)]["4. close"])
day_before_close = float(stock_data["Time Series (Daily)"][str(day_before)]["4. close"])

difference = float(yesterday_close) - float(day_before_close)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_perc = round((difference / float(yesterday_close)) * 100)

if abs(diff_perc) >= 1:
    news_endpoint = "https://newsapi.org/v2/everything"
    news_api = "edfee498fd544e1e842f109d8111e875"

    news_params = {
        "q": COMPANY_NAME,
        "searchIn": "title",
        "apikey": news_api
    }

    news_response = requests.get(news_endpoint, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    news_data_slice = news_data["articles"][:3]

    news_dict = {}

    for day in news_data_slice:
        news_dict[day["title"]] = day["description"]

    for k, v in news_dict.items():
        stock_message = f"{STOCK}: {up_down}{diff_perc}%\nHeadline: {k}. \nBrief: {v}"

        account_sid = "ACf772fa6713b8985ef23c5b838c8bdae3"
        auth_token = "5f624f631e4b92a2bdca8894957f8e67"

        client = Client(account_sid,  auth_token)
        message = client.messages.create(
            body=stock_message,
            from_="+18142613653",
            to="+14805282664"
        )
