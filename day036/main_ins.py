import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query?"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "PR0DSZT02C5R3Z91"
NEWS_API_KEY = "edfee498fd544e1e842f109d8111e875"
TWILIO_SID = "ACf772fa6713b8985ef23c5b838c8bdae3"
TWILIO_AUTH_TOKEN = "5f624f631e4b92a2bdca8894957f8e67"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)

if abs(diff_percent) > 1:
    news_params = {
        "q": COMPANY_NAME,
        "searchIn": "title",
        "apikey": NEWS_API_KEY
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)
    formatted_articles = [f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: " \
                          f"{article['description']}" for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+18142613653",
            to="+14805282664"
        )
