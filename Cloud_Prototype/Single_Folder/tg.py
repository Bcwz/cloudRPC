from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
from telegram.ext import Updater, InlineQueryHandler, CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import json 
from fpdf import FPDF 
import telebot
import requests
import communicator
import grpc
import assignment_prototype_pb2
import assignment_prototype_pb2_grpc

# Please keep this safe as this is the bot token....
class tg():
    def __init__(self, cName):
        self.bot_token = '1865636715:AAEmLEWQwrIIDTtWwVQVPxVwe5XFyvUulw0'
        self.bot_chatID = '347015062'

        self.logDir = ''

        self.port_range = [50051,50056,50061,50066]
        self.controller_ports = [50055,50060,50065,50070]

        self.no_Of_client = 4
        self.functionType = 0

        self.junctions = ['JunctionA-Controller', 'JunctionB-Controller', 'JunctionC-Controller', 'JunctionD-Controller']
        self.traffic_lights = ['TL-A', 'TL-B','TL-C','TL-D']
        self.functions = ['Get Logs', 'Suspend Junction', 'View Status']
        

    def menu(self, update, context):
        keyboard = [[InlineKeyboardButton("Get Logs", callback_data='{"Function": 0}'),InlineKeyboardButton("Suspend Junction", callback_data='{"Function": 1}')], [InlineKeyboardButton("View Junction Status", callback_data='{"Function": 2}')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Please Select:', reply_markup=reply_markup)
        
        #update.message.reply_text(update.message.text)
    
    def getLog(self,junctionIndex):
        #Let the user choose which Junction they would like to work on
        self.functionType = 0
        output_name = self.junctions[junctionIndex]+'_Consolidated_log.log'
        dataContent = ''

        try:
            channel = grpc.insecure_channel('localhost:'+str(self.controller_ports[junctionIndex]))
            stub = assignment_prototype_pb2_grpc.communicatorStub(channel)
            response = stub.getLogs(assignment_prototype_pb2.RequestLog(types=0))
            dataContent = dataContent + '\n'+ response.Content

        except grpc.RpcError as rpc_error:
                    #print(rpc_error)
            if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
                print('Port ' + str(self.controller_ports[junctionIndex]) +' is unavailable...')
            
        
        f = open(output_name, "w")
        f.write(dataContent)
        f.close()

        files = {'document': open(output_name)}
        send_file = 'https://api.telegram.org/bot' + self.bot_token + '/sendDocument?chat_id=' + self.bot_chatID + '&caption=Consolidated-Logs' 
        response = requests.post(send_file,  files=files)
        return response.json()

    def suspendJunction(self,junctionIndex):
        
        try:
            channel = grpc.insecure_channel('localhost:'+str(self.controller_ports[junctionIndex]))
            stub = assignment_prototype_pb2_grpc.communicatorStub(channel)

            response = stub.makerequest(assignment_prototype_pb2.RequestCall(type=0, RequestMsg='Suspend Junction'))
            

        except grpc.RpcError as rpc_error:
                    #print(rpc_error)
            if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
                print('Port ' + str(self.controller_ports[junctionIndex]) +' is unavailable...')
        
        pass
    
    
    def viewStatus(self,junctionIndex):
        try:
            
            channel = grpc.insecure_channel('localhost:'+str(self.controller_ports[junctionIndex]))
            stub = assignment_prototype_pb2_grpc.communicatorStub(channel)
            
            response = stub.makerequest(assignment_prototype_pb2.RequestCall(type=4, RequestMsg='Request to get Traffic Light Status'))
            return response.ResponseMsg
            #return content

        except grpc.RpcError as rpc_error:
                #print(rpc_error)
            if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
                return self.junctions[junctionIndex] + ' is currently offline'

    def getJunction(self,query):
        keyboard = [[InlineKeyboardButton("Junction A", callback_data='{"Junction": 0}'),InlineKeyboardButton("Junction B", callback_data='{"Junction": 1}')],  [InlineKeyboardButton("Junction C", callback_data='{"Junction": 2}'),InlineKeyboardButton("Junction D", callback_data='{"Junction": 3}')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_text('Please Select:', reply_markup=reply_markup)


    def handleUser(self,update, context):
        query = update.callback_query

        # CallbackQueries need to be answered, even if no notification to the user is needed
        # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
        query.answer()
        ans = json.loads(query.data)
        if 'Function' in ans:
            query.edit_message_text(text=f"Selected Function: {self.functions[ans['Function']]}")
            self.functionType = ans['Function']
            if self.functionType != 2:
                self.getJunction(query)
            else:
                
                AllStatus = ''
                for i in range(0, self.no_Of_client):
                    AllStatus = AllStatus+ self.viewStatus(i) + '\n'
                query.message.reply_text(AllStatus)
                #Execute Function 2, to view Status of all Junctions
                pass
        elif 'Junction' in ans:
            query.edit_message_text(text=f"Selected Junction: {self.junctions[ans['Junction']]}")
            
            if self.functionType == 0:
                #Run function 0,to get logs of one Junction 
                self.getLog(ans['Junction'])
                #query.message.reply_text('Running Get Log Function for '+self.junctions[ans['Junction']])
                pass
            elif self.functionType == 1:

                query.message.reply_text('Running Suspend Function for '+self.junctions[ans['Junction']])
                #Run function 1,  to suspend one junction
                pass


    def telegram_start_server(self):
        updater = Updater(self.bot_token , use_context=True)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler('getLog',self.getLog))
        dp.add_handler(CommandHandler('menu',self.menu))
        dp.add_handler(CallbackQueryHandler(self.handleUser))
        
        print("\nTelegram Board Initialized")
        updater.start_polling()
        updater.idle()

    def telegram_bot_sendtext(self, bot_message):
        send_text = 'https://api.telegram.org/bot' + self.bot_token + '/sendMessage?chat_id=' + self.bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        print('Text = ' + send_text)
        print(response)
        return response.json()

    # def telegram_bot_sendFiles(self):
    #     files = {'document': open(logDir)}
    #     send_file = 'https://api.telegram.org/bot' + self.bot_token + '/sendDocument?chat_id=' + self.bot_chatID + '&caption=' + logDir
    #     response = requests.post(send_file,  files=files)
    #     print(logDir)
    #     print(response.json())
    #     return response.json()

