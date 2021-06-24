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

    def __init__(self,id):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.trafficLightStub(self.channel)
        #id to identify node
        self.id = id

    def ping_server(self,id,message):
        """ Ping from traffic light node to traffic light server / controller """
        ping = pb2.Message(message= "{0} pinged : {1}".format(id,message))
        print(f'{ping}')
        #return server response in server.py
        return self.stub.GetServerResponse(ping)

    def ping_node(self,requestId,message,responseId):
        """ Ping from traffic light node to traffic light node """
        ping = pb2.Message(message= "{0} pinged : {1} to {2}".format(requestId,message,responseId))

        #Getting a node reply if dead or alive
        print(client.node_reply(responseId))
        #print(f'{ping}')

    def node_reply(self,responseId):
        alive = True
        if alive:
            alive_message = ('Yes, {0} is alive'.format(responseId))
            return alive_message
        else:
            dead_message = ('No, {0} is dead'.format(responseId))
            return dead_message

if __name__ == '__main__':
    client = trafficClient(id="testXXXXX")
    north = trafficClient(id="north")
    south = trafficClient(id="south")
    east = trafficClient(id="east")
    west = trafficClient(id="west")
    node_array = [north,south,east,west]
    while True:
        #Ping node - threaded
        ping_thread = threading.Thread(target=client.ping_node, args=(north.id,"Are you alive?","south"))
        ping_thread.start()
        # time.sleep for fixed interval
        time.sleep(5)





        #ping server
        # reply = client.ping_server(id=client.id,message="Server are you alive?")
        # print(f'{reply}')