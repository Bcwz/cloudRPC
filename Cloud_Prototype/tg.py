from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
from telegram.ext import Updater, InlineQueryHandler, CommandHandler

from fpdf import FPDF 
import telebot
import requests
import grpc
import assignment_prototype_pb2
import assignment_prototype_pb2_grpc

# Please keep this safe as this is the bot token....

bot_token = '1865636715:AAEmLEWQwrIIDTtWwVQVPxVwe5XFyvUulw0'
bot_chatID = '347015062'
logDir = ''
clientName = ''
port_range_start = 50051
port_range_end = 50055

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def getLog(update, context):
    output_name = 'Consolidated_log.log'
    dataContent = ''
    for i in range(port_range_start, port_range_end):
        try:
            channel = grpc.insecure_channel('localhost:'+str(i))
            stub = assignment_prototype_pb2_grpc.communicatorStub(channel)
            response = stub.getLogs(assignment_prototype_pb2.RequestLog(types=3))
            dataContent = dataContent + '\n'+ response.Content 
        except grpc.RpcError as rpc_error:
            if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
                print('Port ' + str(i) +' is unavailable...')
    
    f = open(output_name, "w")
    f.write(dataContent)
    f.close()

    files = {'document': open(output_name)}
    send_file = 'https://api.telegram.org/bot' + bot_token + '/sendDocument?chat_id=' + bot_chatID + '&caption=Consolidated-Logs' 
    response = requests.post(send_file,  files=files)
    return response.json()


def telegram_start_server():
    updater = Updater(bot_token , use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('getLog',getLog))
    dp.add_handler(CommandHandler('echo',echo))
    print("\nTelegram Board Initialized")
    updater.start_polling()
    updater.idle()

def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    print('Text = ' + send_text)
    print(response)
    return response.json()

def telegram_bot_sendFiles():
    files = {'document': open(logDir)}
    send_file = 'https://api.telegram.org/bot' + bot_token + '/sendDocument?chat_id=' + bot_chatID + '&caption=' + logDir
    response = requests.post(send_file,  files=files)
    print(logDir)
    print(response.json())
    return response.json()

