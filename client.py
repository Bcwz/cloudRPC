from google.protobuf import message
import grpc
import trafficLight_pb2_grpc as pb2_grpc
import trafficLight_pb2 as pb2
import threading


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

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.Message(message=message)
        print(f'{message}')
        return self.stub.GetServerResponse(message)


if __name__ == '__main__':
    client = trafficClient()
    # result = client.get_url(message="Hello Server you there?")
    x = threading.Thread(target=client.get_url, args=('thread',))
    result = x.start()
    # print(f'{result}')