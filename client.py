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

    # def get_url(self, message):
    #     """
    #     Client function to call the rpc for GetServerResponse
    #     """
    #     message = pb2.Message(message=message)
    #     print(f'{message}')
    #     return self.stub.GetServerResponse(message)

    def ping_server(self,id,message):
        """ Ping from traffic light node to traffic light server / controller """
        ping = pb2.Message(message= "{0} pinged : {1}".format(id,message))
        print(f'{ping}')
        #return server response in server.py
        return self.stub.GetServerResponse(ping)

    def ping_node(self,requestId,message,responseId):
        """ Ping from traffic light node to traffic light node """
        ping = pb2.Message(message= "{0} pinged : {1} to {2}".format(requestId,message,responseId))
        print(f'{ping}')


if __name__ == '__main__':
    client = trafficClient(id="testXXXXX")
    north = trafficClient(id="north")
    south = trafficClient(id="south")
    east = trafficClient(id="east")
    west = trafficClient(id="west")


    while True:
        #ping server
        # reply = client.ping_server(id=client.id,message="Server are you alive?")
        # print(f'{reply}')

        #Ping node - threaded
        ping_thread = threading.Thread(target=client.ping_node, args=(north.id,"THREADMESSAGE","south"))
        ping_thread.start()


        # time.sleep for fixed interval
        time.sleep(5)



    # result = client.get_url(message="Hello Server you there?")
    # x = threading.Thread(target=client.get_url, args=('thread',))
    # result = x.start()
    # print(f'{result}')