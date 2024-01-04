import requests
import json
from twilio.rest import Client
import os

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_NEWS_KEY = os.environ.get("API_NEWS_KEY")
API_STOCK_KEY = os.environ.get("API_STOCK_KEY")

params_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": API_STOCK_KEY
}

params_news = {
    "apiKey": API_NEWS_KEY,
    "qInTitle": COMPANY_NAME,
    "sortBy": "relevancy"
}

response_stocks = requests.get(url=STOCK_ENDPOINT, params=params_stock)
response_stocks.raise_for_status()
data_stocks = response_stocks.json()["Time Series (Daily)"]

stocks_list = [value for (key, value) in data_stocks.items()]

day_before_yesterday_data = stocks_list[1]
day_before_yesterday_closing_price = float(stocks_list[1]["4. close"])

yesterday_data = stocks_list[0]
yesterday_closing_price = float(stocks_list[0]["4. close"])

difference = day_before_yesterday_closing_price - yesterday_closing_price
if difference >= 0:
    emoji_msg = "🔺"
else:
    emoji_msg = "🔻"
percentage = (abs(difference) * 100) / day_before_yesterday_closing_price

if percentage > 5:

    response_news = requests.get(url=NEWS_ENDPOINT, params=params_news)
    response_news.raise_for_status()
    news_data = response_news.json()["articles"][:3]

    articles_list = [
        f"{emoji_msg} {round(percentage, 2)}% \n Headline: {element['title']} \nBrief: {element['description']}" for
        element in news_data]

    for _ in articles_list:
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=_,
            from_="",
            to=""
        )
        print(message.status)
