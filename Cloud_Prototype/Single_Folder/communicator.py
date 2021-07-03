import grpc
import assignment_prototype_pb2
import assignment_prototype_pb2_grpc
#from tg import telegram_bot_sendtext, telegram_start_server
import tg
class communicator(assignment_prototype_pb2_grpc.communicatorServicer):

    def __init__(self,cName,bot,client_head_port):
        self.clientName = cName
        
        self.logDir = ''
        self.logOutDir = ''
 
        self.bot = bot
        self.junctions = ['JunctionA-Controller', 'JunctionB-Controller', 'JunctionC-Controller', 'JunctionD-Controller']
        self.traffic_lights = ['TL-A', 'TL-B','TL-C','TL-D']

        self.head_client_port = client_head_port
        self.no_Of_client = 4 

        self.client = None

        self.info = None


    def requestFunction(self,port):
       
        try:
            channel = grpc.insecure_channel('localhost:'+str(port))
            stub = assignment_prototype_pb2_grpc.communicatorStub(channel)
            
            response = stub.makerequest(assignment_prototype_pb2.RequestCall(type=0, RequestMsg= 'Ping From ' + self.clientName))
            print('Ping Port:' +str(port))
            return True

        except grpc.RpcError as rpc_error:
            #print(rpc_error)
            if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
                return False
                
    def makerequest(self, request, context):
        # A very simplified version of switch case...
        if(request.type == 0):
            print('Request Received: ' + request.RequestMsg)
            return assignment_prototype_pb2.RequestResponse(ResponseMsg ='This is your request: %s!' % request.RequestMsg)
        elif (request.type == 1):
            print('Request Received: ' + request.RequestMsg)
            self.bot.telegram_bot_sendtext('Request Received: ' + request.RequestMsg)
            return assignment_prototype_pb2.RequestResponse(ResponseMsg ='This is your request: %s!' % request.RequestMsg)
            #Other whatever request that the user requested....
        
        elif (request.type == 2):
            print('Request Received: ' + request.RequestMsg)
            self.bot.telegram_bot_sendtext('Request Received: ' + request.RequestMsg)
            return assignment_prototype_pb2.RequestResponse(ResponseMsg ='This is your request: %s!' % request.RequestMsg)
            

        elif (request.type == 3):
            print('Request Received: ' + request.RequestMsg)
            self.bot.telegram_bot_sendtext('Request Received: ' + request.RequestMsg)
            return assignment_prototype_pb2.RequestResponse(ResponseMsg ='This is your request: %s!' % request.RequestMsg)
            

        elif(request.type == 4): 
            # Only meant for tg to traffic controller
            response = self.clientName + ' : online\n'
            for i in range(0, self.no_Of_client):
                if(self.requestFunction(self.head_client_port + i)):
                    response = response + self.traffic_lights[i] + " : online\n"
                else:
                    response = response + self.traffic_lights[i] + " : offline\n"


            return assignment_prototype_pb2.RequestResponse(ResponseMsg = response)

        elif (request.type == 5):
            
            pass

        else:
            return assignment_prototype_pb2.RequestResponse(ResponseMsg ='This is your request: Nonsense!')

    def getLogs(self, request, context):
        dataContent = ''
        
        if(request.types == 0):
            
            for i in range(0, self.no_Of_client):
                try:
                    channel = grpc.insecure_channel('localhost:'+str(i + self.head_client_port))
                    stub = assignment_prototype_pb2_grpc.communicatorStub(channel)
                    response = stub.getLogs(assignment_prototype_pb2.RequestLog(types=1))
                    dataContent = dataContent + '\n'+ response.Content

                except grpc.RpcError as rpc_error:
                    #print(rpc_error)
                    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
                        print('Port ' + str(i + self.head_client_port ) +' is unavailable...')
            
            return assignment_prototype_pb2.logResponse(Content = dataContent,filename = self.logOutDir)
        elif (request.types == 1):
            print(self.logDir)
            with open(self.logDir, 'r') as file:
                dataContent = file.read()
        
            return assignment_prototype_pb2.logResponse(Content = dataContent,filename = self.logOutDir)

