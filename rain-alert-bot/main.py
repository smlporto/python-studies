import requests

def telegram_bot_sendtext(bot_message):
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


url = "https://api.openweathermap.org/data/2.5/onecall"
api_key = ""

params = {
    "lat": '',
    "lon": '',
    "exclude": "current,minutely,daily",
    "appid": api_key
}

rain = False

response = requests.get(url, params=params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for data in weather_slice:
    weather_code = data["weather"][0]["id"]
    if int(weather_code) < 700:
        rain = True

if rain:
    telegram_bot_sendtext("It's going to rain today! ☔")