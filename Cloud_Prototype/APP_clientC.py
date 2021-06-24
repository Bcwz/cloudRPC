from __future__ import print_function
from concurrent import futures
from tg import telegram_bot_sendtext
import signal
import sys
import os
import logging
import threading
import time
import grpc
import assignment_prototype_pb2
import assignment_prototype_pb2_grpc

import communicator
import tg

max_fail = 3
fail_count = 0
name = 'TL-C'
host = 'localhost'
host_port = 50053
ping_port = 50054
ping_target = 'D'
time_gap = 30

channel = grpc.insecure_channel(host + ':'+str(ping_port))
stub = assignment_prototype_pb2_grpc.communicatorStub(channel)

suspicious_vehicle = {'SK123A','SC1235B','ST9021A'}
#Disabled the telegram (So called Send to LTA/Cloud)

    
def pingEcho():
    global fail_count
    try:
        response = stub.makerequest(assignment_prototype_pb2.RequestCall(type=0, RequestMsg='Ping From ' + name))
        #telegram_bot_sendtext(response.ResponseMsg)
        print(response.ResponseMsg)
        #If it's online, reset the fail count to 0
        fail_count = 0
        threading.Timer(time_gap, pingEcho).start()

    except grpc.RpcError as rpc_error:
        #print(rpc_error)
        if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
            fail_count = fail_count + 1
            if fail_count >= 3:
                #Call the Cloud Services when failed to ping Traffic Light B
                print('Failed to ping Traffic Light ' + ping_target)
                #telegram_bot_sendtext('Failed to ping Traffic Light ' + ping_target)
            threading.Timer(time_gap, pingEcho).start()
            #print('Client Not Available...Failure Count: ', fail_count)
            


def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    assignment_prototype_pb2_grpc.add_communicatorServicer_to_server(communicator.communicator(), server)
    server.add_insecure_port('[::]:'+str(host_port))
    server.start()
    server.wait_for_termination()



if __name__ == '__main__':
    logging.basicConfig()
    #Basically, the general idea is to run both client and server example to perform distributed communications...
    #Simply said, what's done here is to run the server and every 30s, it will ping alive another machine...    
    
    try:
        threading.Timer(time_gap, pingEcho).start()
        run_server()
    except KeyboardInterrupt:
        print('Process Killed')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

