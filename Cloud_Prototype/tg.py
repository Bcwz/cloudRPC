from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
from telegram.ext import Updater, InlineQueryHandler, CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from fpdf import FPDF 
import telebot
import requests
import grpc
import assignment_prototype_pb2
import assignment_prototype_pb2_grpc

# Please keep this safe as this is the bot token....
class tg():
    def __init__(self):
        self.bot_token = '1865636715:AAEmLEWQwrIIDTtWwVQVPxVwe5XFyvUulw0'
        self.bot_chatID = '347015062'

        self.logDir = ''
        self.clientName = ''
        
        self.port_range_start = 50051
        self.port_range_end = 50055

        self.port_range = [50051,50056,50061,50066]
        self.no_Of_client = 4

        self.functionType = 0

    def echo(self, update, context):
        keyboard = [[InlineKeyboardButton("Junction A", callback_data='0')], [InlineKeyboardButton("Junction B", callback_data='1')],[InlineKeyboardButton("Junction C", callback_data='2')], [InlineKeyboardButton("Junction C", callback_data='2')], [InlineKeyboardButton("Junction D", callback_data='3')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Please Select:', reply_markup=reply_markup)
        
        #update.message.reply_text(update.message.text)

    def getLog(self, update, context):
        #Let the user choose which Junction they would like to work on
        self.functionType = 0
        output_name = 'Consolidated_log.log'
        dataContent = ''

        for i in range(self.port_range_start, self.port_range_end):
            try:
                channel = grpc.insecure_channel('localhost:'+str(i))
                stub = assignment_prototype_pb2_grpc.communicatorStub(channel)
                response = stub.getLogs(assignment_prototype_pb2.RequestLog(types=3))
                dataContent = dataContent + '\n'+ response.Content 
            except grpc.RpcError as rpc_error:
                #print(rpc_error)
                if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
                    print('Port ' + str(i) +' is unavailable...')
            
        
        f = open(output_name, "w")
        f.write(dataContent)
        f.close()

        files = {'document': open(output_name)}
        send_file = 'https://api.telegram.org/bot' + self.bot_token + '/sendDocument?chat_id=' + self.bot_chatID + '&caption=Consolidated-Logs' 
        response = requests.post(send_file,  files=files)
        return response.json()

    def suspendJunction(self, update, context):
        self.functionType = 1
        keyboard = [[InlineKeyboardButton("Suspend Junction", callback_data='1')], [InlineKeyboardButton("Get Logs", callback_data='0')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Please Select:', reply_markup=reply_markup)



    def button(self,update, context):
        query = update.callback_query

        # CallbackQueries need to be answered, even if no notification to the user is needed
        # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
        query.answer()
        if (self.functionType == 0):
            self.functionType = 0.5
            keyboard = [[InlineKeyboardButton("Junction A", callback_data='0')], [InlineKeyboardButton("Junction B", callback_data='1')], [InlineKeyboardButton("Junction C", callback_data='2')], [InlineKeyboardButton("Junction D", callback_data='3')]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text('Please Select:', reply_markup=reply_markup)

            pass
        elif (self.functionType == 1):
            
            pass
        else:
            pass
        query.edit_message_text(text=f"Selected Junction: {query.data}")


    def telegram_start_server(self):
        updater = Updater(self.bot_token , use_context=True)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler('getLog',self.getLog))
        dp.add_handler(CommandHandler('echo',self.echo))
        dp.add_handler(CallbackQueryHandler(self.button))
        
        print("\nTelegram Board Initialized")
        updater.start_polling()
        updater.idle()

    def telegram_bot_sendtext(self, bot_message):
        send_text = 'https://api.telegram.org/bot' + self.bot_token + '/sendMessage?chat_id=' + self.bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        print('Text = ' + send_text)
        print(response)
        return response.json()

    def telegram_bot_sendFiles(self):
        files = {'document': open(logDir)}
        send_file = 'https://api.telegram.org/bot' + self.bot_token + '/sendDocument?chat_id=' + self.bot_chatID + '&caption=' + logDir
        response = requests.post(send_file,  files=files)
        print(logDir)
        print(response.json())
        return response.json()

