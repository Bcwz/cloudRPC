
import grpc
import assignment_prototype_pb2
import assignment_prototype_pb2_grpc
class communicator(assignment_prototype_pb2_grpc.communicatorServicer):
    def makerequest(self, request, context):
        # A very simplified version of switch case...
        if(request.type == 0):#echo Request
            print('Request Received: ' + request.RequestMsg)
            return assignment_prototype_pb2.RequestResponse(ResponseMsg ='This is your request: %s!' % request.RequestMsg)
        elif (request.type == 1):
            #Other whatever request that the user requested....
            pass
        elif (request.type == 2):
            #Other whatever request that the user requested....
            pass
        else:
            return assignment_prototype_pb2.RequestResponse(ResponseMsg ='This is your request: Nonsense!')
