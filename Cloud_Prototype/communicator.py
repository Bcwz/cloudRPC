import grpc
import assignment_prototype_pb2
import assignment_prototype_pb2_grpc
from tg import telegram_bot_sendtext, telegram_start_server
import tg
class communicator(assignment_prototype_pb2_grpc.communicatorServicer):
    clientName = ''
    logDir = ''
    logOutDir = ''
    def makerequest(self, request, context):
        # A very simplified version of switch case...
        if(request.type == 0):#echo Request
           # print('Request Received: ' + request.RequestMsg)
    
            return assignment_prototype_pb2.RequestResponse(ResponseMsg ='This is your request: %s!' % request.RequestMsg)
        elif (request.type == 1):
            #print('Request Received: ' + request.RequestMsg)
            telegram_bot_sendtext('Request Received: ' + request.RequestMsg)
            return assignment_prototype_pb2.RequestResponse(ResponseMsg ='This is your request: %s!' % request.RequestMsg)
            #Other whatever request that the user requested....
        
        elif (request.type == 2):
            #print('Request Received: ' + request.RequestMsg)
            telegram_bot_sendtext('Request Received: ' + request.RequestMsg)
            return assignment_prototype_pb2.RequestResponse(ResponseMsg ='This is your request: %s!' % request.RequestMsg)
            #Other whatever request that the user requested....
        elif (request.type == 3):
            #print('Request Received: ' + request.RequestMsg)
            telegram_bot_sendtext('Request Received: ' + request.RequestMsg)
            return assignment_prototype_pb2.RequestResponse(ResponseMsg ='This is your request: %s!' % request.RequestMsg)
            #Other whatever request that the user requested....    
        else:
            return assignment_prototype_pb2.RequestResponse(ResponseMsg ='This is your request: Nonsense!')

    def getLogs(self, request, context):
        data = ''
        print(logDir)
        with open(logDir, 'r') as file:
            data = file.read()
        return assignment_prototype_pb2.logResponse(Content = data,filename = logOutDir)

