import json
import os
from datetime import datetime

import requests
import telegram

from variables.config import date_format, birthday_appender, telegram_update_api, bot_token_replacer, bot_token, \
    birthday_message


def send_birthday():
    # Check if birthday is there or not on the day
    today = datetime.today()
    formatted_birthday_check = today.strftime(date_format) + birthday_appender
    today_birthdays = os.getenv(formatted_birthday_check)
    if today_birthdays is not None:
        # get the latest message information
        payload = {}
        headers = {}
        update_api = os.getenv(telegram_update_api)
        update_api = update_api.replace(bot_token_replacer, os.getenv(bot_token))
        response = requests.request("GET", update_api, headers=headers, data=payload)

        # json format data
        json_data = json.loads(response.text)
        # get the latest chat id
        chat_id = json_data['result'][0]['message']['chat']['id']
        bot = telegram.Bot(token=os.getenv(bot_token))
        birthdays = today_birthdays.split(',')
        for people in birthdays:
            send_message = bot.sendMessage(chat_id=chat_id, text=birthday_message.replace('{{}}', people))
            chat_id = send_message.chat_id
        bot.close()


if __name__ == '__main__':
    send_birthday()
