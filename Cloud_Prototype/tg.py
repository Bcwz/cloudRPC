from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import telebot
import requests
# Please keep this safe as this is the bot token....
bot_token = '1865636715:AAEmLEWQwrIIDTtWwVQVPxVwe5XFyvUulw0'
bot_chatID = '347015062'


def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    print('Text = ' + send_text)
    print(response)
    return response.json()