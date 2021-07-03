from __future__ import print_function
from concurrent import futures
<<<<<<< Updated upstream:Cloud_Prototype/APP_clientD.py
from tg import telegram_bot_sendtext
=======
from threading import Thread
#from tg import telegram_bot_sendtext, telegram_start_server

>>>>>>> Stashed changes:Cloud_Prototype/Single_Folder/Traffic_Controller.py
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
<<<<<<< Updated upstream:Cloud_Prototype/APP_clientD.py
=======
import multiprocessing
import _thread
>>>>>>> Stashed changes:Cloud_Prototype/Single_Folder/Traffic_Controller.py


max_fail = 3
fail_count = 0
<<<<<<< Updated upstream:Cloud_Prototype/APP_clientD.py
name = 'TL-D'
=======

name = str(sys.argv[1])
ping_target = str(sys.argv[2])
host_port = int(sys.argv[4])
ping_port = int(sys.argv[5])

>>>>>>> Stashed changes:Cloud_Prototype/Single_Folder/Traffic_Controller.py
host = 'localhost'


time_gap = 30
num_of_TL = 4
suspend = False

<<<<<<< Updated upstream:Cloud_Prototype/APP_clientD.py
channel = grpc.insecure_channel(host + ':'+str(ping_port))
stub = assignment_prototype_pb2_grpc.communicatorStub(channel)

suspicious_vehicle = {'SK123A','SC1235B','ST9021A'}
#Disabled the telegram (So called Send to LTA/Cloud)

    
def pingEcho():
=======
option_type = ['Ping','Report Accident', 'Report Suspicious Vehicle','Report Taffic Light Failure']

client_head_port = ping_port = int(sys.argv[6]) 
leader_controller = 50055


bot = tg.tg(name)
comm = communicator.communicator(name,bot,client_head_port)


def run_server():
    logging.info('Server '+name +' Started')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    assignment_prototype_pb2_grpc.add_communicatorServicer_to_server(comm, server)

    server.add_insecure_port('[::]:'+str(host_port))
    server.start()
    server.wait_for_termination()

def start_telegram():
    p = multiprocessing.Process(target=bot.telegram_start_server)
    p.start()    

def requestFunction(port, requestType):
    
>>>>>>> Stashed changes:Cloud_Prototype/Single_Folder/Traffic_Controller.py
    global fail_count
    try:
        response = stub.makerequest(assignment_prototype_pb2.RequestCall(type=0, RequestMsg='Ping From ' + name))
        #telegram_bot_sendtext(response.ResponseMsg)
        print(response.ResponseMsg)
<<<<<<< Updated upstream:Cloud_Prototype/APP_clientD.py
        #If it's online, reset the fail count to 0
        fail_count = 0
        threading.Timer(time_gap, pingEcho).start()
=======
        threading.Timer(time_gap, requestFunction,[port,requestType]).start()
        
        if requestType == 0:
            fail_count = 0
>>>>>>> Stashed changes:Cloud_Prototype/Single_Folder/Traffic_Controller.py

    except grpc.RpcError as rpc_error:
        #print(rpc_error)
        if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
<<<<<<< Updated upstream:Cloud_Prototype/APP_clientD.py
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
=======
            if requestType == 0:
                fail_count = fail_count + 1
                if fail_count >= max_fail:
                    print('Failed to ping ' + ping_target)
                    fail_count = 0
                    
                threading.Timer(time_gap, requestFunction,[port,requestType]).start()

            else:
                print('Failed to ' + option_type[requestType])


if __name__ == '__main__':
    logging.basicConfig(filename='Traffic_Controller.log', level=logging.INFO,format='%(message)s @ %(asctime)s')
      
    try:

        p = multiprocessing.Process(target=run_server)
        p.start()
        threading.Timer(time_gap, requestFunction,[ping_port,0]).start()
        if(str(sys.argv[3]) == 'DEFAULT'):
            start_telegram()

>>>>>>> Stashed changes:Cloud_Prototype/Single_Folder/Traffic_Controller.py
    except KeyboardInterrupt:
        print('Process Killed')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

