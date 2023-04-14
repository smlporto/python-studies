import requests
from config import *

class NotificationManager:
    
    def telegram_bot_sendtext(self, bot_message):
        bot_token = BOT_TOKEN
        bot_chatID = CHAT_ID
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

        response = requests.get(send_text)

        return response.json()