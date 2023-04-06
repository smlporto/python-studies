import requests
import datetime

STOCK_KEY = ""
NEWS_KEY = ""
BOT_KEY = ""

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


def telegram_bot_sendtext(bot_message):
    bot_token = BOT_KEY
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


stock_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' + STOCK_NAME + '&apikey=' + STOCK_KEY
stock_reponse = requests.get(stock_url)
data = stock_reponse.json()

yesterday = str(datetime.date.today() - datetime.timedelta(days=1))
yesterday_closing = float(data["Time Series (Daily)"][yesterday]["4. close"])

day_before_yesterday = str(datetime.date.today() - datetime.timedelta(days=2))
day_before_yesterday_closing = float(data["Time Series (Daily)"][day_before_yesterday]["4. close"])

price_difference = yesterday_closing - day_before_yesterday_closing
if price_difference > 0:
    price_movement = "🟢"
else:
    price_movement = "🔴"

percentage_difference = (price_difference / ((yesterday_closing + day_before_yesterday_closing) / 2)) * 100 

if abs(percentage_difference) < 5:

    news_url = 'https://newsapi.org/v2/everything?q=' + COMPANY_NAME +'&language=en&pageSize=3&sortBy=publishedAt&apiKey=' + NEWS_KEY
    news_reponse = requests.get(news_url)
    articles = news_reponse.json()["articles"]


    formatted_articles = [f"{STOCK_NAME}: {price_movement} {round(percentage_difference, 2)}% \nHeadline: {article['title']} \nBrief: {article['description']}" for article in articles]

    for article in formatted_articles:
        telegram_bot_sendtext(article)


