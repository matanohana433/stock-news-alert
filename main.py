import requests
from twilio.rest import Client
import os

COMPANY_NAME = "Tesla Inc"
STOCK = "TSLA"

AV_API_KEY = os.environ.get("AV_API_KEY")


def get_closing_prices():
    av_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": AV_API_KEY,
    }
    av_url = f'https://www.alphavantage.co/query?'
    av_response = requests.get(url=av_url, params=av_params)
    av_response.raise_for_status()
    av_data = av_response.json()

    relevant_dates = list(av_data['Time Series (Daily)'].keys())[1:3]

    yesterday_closing_p = float(av_data['Time Series (Daily)'][relevant_dates[0]]["4. close"])
    before_yesterday_closing_p = float(av_data['Time Series (Daily)'][relevant_dates[1]]["4. close"])

    return yesterday_closing_p, before_yesterday_closing_p


def check_trend_percent(x, y):
    if x > y:
        result = x - y
        trend = "up"
    else:
        result = y - x
        trend = "down"
    perc = 100 * result / y
    return trend, perc


NEWS_API_KEY = os.environ.get("NEWS_API_KEY")


def get_news():
    news_params = {
        # "qInTitle": "Tesla",
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME[:COMPANY_NAME.find(" ")]
    }
    news_url = "https://newsapi.org/v2/top-headlines?"
    # news_url = "https://newsapi.org/v2/everything?"
    news_response = requests.get(news_url, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    tesla_articles_list = news_data["articles"]
    articles = []
    for i in range(3):
        articles.append((tesla_articles_list[i]["title"], tesla_articles_list[i]["description"]))

    return articles


TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")

TWILIO_PHONE = os.environ.get("TWILIO_PHONE")
MY_PHONE = os.environ.get("MY_PHONE")


def send_whats_app(trend, perc, articles):
    auth_token = TWILIO_AUTH_TOKEN
    account_sid = TWILIO_ACCOUNT_SID
    client = Client(account_sid, auth_token)
    if trend == "up":
        sym = "🔺"
    else:
        sym = "🔻"
    msg_body = f"{STOCK}: {sym}{perc:.2f}% \n"
    for i in range(len(articles)):
        for j in range(2):
            if j == 0:
                msg_body += f"Headline: {articles[i][j]}\n"
            else:
                msg_body += f"Brief: {articles[i][j]}\n"
    message = client.messages.create(
        from_=TWILIO_PHONE,
        body=msg_body,
        to=MY_PHONE
    )
    print(message.body)


yesterday_price, before_price = get_closing_prices()

price_trend, percent = check_trend_percent(yesterday_price, before_price)

if percent > 4.9:
    articles_list = get_news()
    send_whats_app(price_trend, percent, articles_list)
