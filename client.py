from google.protobuf import message
import grpc
import trafficLight_pb2_grpc as pb2_grpc
import trafficLight_pb2 as pb2
import threading
import os
import time


class trafficClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self,id,status):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.trafficLightStub(self.channel)
        #id to identify node
        self.id = id
        #Status to identify if dead or alive
        self.status = status

    def ping_server(self,id,message):
        """ Ping from traffic light node to traffic light server / controller """
        ping = pb2.Message(message= "{0} pinged : {1}".format(id,message))
        print(f'{ping}')
        #return server response in server.py
        return self.stub.GetServerResponse(ping)

    def ping_node(self,requestId,message,responseId,responseStatus):
        """ Ping from traffic light node to traffic light node """
        ping = pb2.Message(message= "{0} pinged : {1} to {2}".format(requestId,message,responseId))
        #print(f'{ping}')

        #Getting a node reply if dead or alive
        replyStatus = client.node_reply(responseStatus)
        if replyStatus == "dead" : 
            print("pinged back dead")
        else:
            print("pinged back alive")
        

    def node_reply(self,responseStatus):
        alive = responseStatus
        if alive:
            return "alive"
        else:
            return "dead"

if __name__ == '__main__':
    # Status = 1 for alive, Status = 0 for dead
    client = trafficClient(id="testXXXXX",status=1)
    north = trafficClient(id="north",status=1)
    south = trafficClient(id="south",status=0)
    east = trafficClient(id="east",status=1)
    west = trafficClient(id="west",status=1)
    node_array = [north,south,east,west]
    while True:
        #Ping node - threaded
        ping_thread = threading.Thread(target=client.ping_node, args=(north.id,"Are you alive?",south.id,south.status))
        ping_thread.start()
        # time.sleep for fixed interval
        time.sleep(10)





        #ping server
        # reply = client.ping_server(id=client.id,message="Server are you alive?")
        # print(f'{reply}')