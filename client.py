from google.protobuf import message
import grpc
import trafficLight_pb2_grpc as pb2_grpc
import trafficLight_pb2 as pb2
import threading
import os


class trafficClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.trafficLightStub(self.channel)

        self.id = ''

    # def get_url(self, message):
    #     """
    #     Client function to call the rpc for GetServerResponse
    #     """
    #     message = pb2.Message(message=message)
    #     print(f'{message}')
    #     return self.stub.GetServerResponse(message)

    def ping_nodes(self,id,message):
        """ Ping traffic light nodes within traffic light junction """
        ping = pb2.Message(message= "{0} pinged : {1}".format(id,message))
        print(f'{ping}')
        return self.stub.GetServerResponse(ping)

    def node_north():
        """ North traffic node"""
        id = "north"

    def node_south():
        """ South traffic node"""
        id = "south"
        
    def node_east():
        """ east traffic node"""
        id = "east"

    def node_west():
        """ West traffic node"""
        id = "west"

if __name__ == '__main__':
    client = trafficClient()
    # result = client.get_url(message="Hello Server you there?")
    # x = threading.Thread(target=client.get_url, args=('thread',))
    # result = x.start()
    # print(f'{result}')
    client.ping_nodes(id="north",message="Are you alive?")