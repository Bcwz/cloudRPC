
from concurrent import futures
import logging

import grpc

import assignment_prototype_pb2
import assignment_prototype_pb2_grpc

fail_count = 0
my_name = 'TL_A'

class Greeter(assignment_prototype_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return assignment_prototype_pb2.HelloReply(message='Hello, %s!' % request.name)

    def SayHelloAgain(self, request, context):
        return assignment_prototype_pb2.HelloReply(message='Hello again, %s!' % request.name)

    def testAlive(self, request, context):
        if(request.clientname == "LOL"):
            return assignment_prototype_pb2.AliveReply(isAlive=True)
        else:
            return assignment_prototype_pb2.AliveReply(isAlive=False)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    assignment_prototype_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
