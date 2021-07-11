from __future__ import print_function
from concurrent import futures
from threading import Thread
#from tg import telegram_bot_sendtext, telegram_start_server

import signal
import sys
import os
import logging
import threading
import time
import grpc
import assignment_prototype_pb2
import assignment_prototype_pb2_grpc
import random
import communicator
import tg
import multiprocessing
import _thread


max_fail = 3
fail_count = 0

name = str(sys.argv[1])
ping_target = str(sys.argv[2])
host_port = int(sys.argv[4])
ping_port = int(sys.argv[5])
client_head_port = int(sys.argv[6])

host = 'localhost'

time_gap = 30
num_of_TL = 4
suspend = False
option_type = ['Ping','Report Accident', 'Report Suspicious Vehicle','Report Taffic Light Failure']
leader_controller = 50055

bot = tg.tg(name)
comm = communicator.communicator(name,bot,client_head_port,None)

script_dir = os.path.dirname(__file__)
CA_path = "Cert/root-ca.pem"
root_CA = os.path.join(script_dir, CA_path)
key_path = "Cert/root-ca-key.pem"
root_Key = os.path.join(script_dir, key_path)

def run_server():
    logging.info('Server '+name +' Started')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    with open(root_Key, 'rb') as f:
        private_key = f.read()
    with open(CA_path , 'rb') as f:
        certificate_chain = f.read()

    server_credentials = grpc.ssl_server_credentials( ( (private_key, certificate_chain), ) )
    assignment_prototype_pb2_grpc.add_communicatorServicer_to_server(comm, server)
    server.add_secure_port('[::]:'+str(host_port), server_credentials)
    
    server.start()
    server.wait_for_termination()

def start_telegram():
    lta = multiprocessing.Process(target=bot.telegram_start_lta_server)
    lta.start()    

    driver = multiprocessing.Process(target=bot.telegram_start_driver_server)
    driver.start()    

def requestFunction(port, requestType):
    
    global fail_count
    try:
        with open(CA_path, 'rb') as f:
            creds = grpc.ssl_channel_credentials(f.read())

        channel = grpc.secure_channel(host + ':'+str(port), creds)
        stub = assignment_prototype_pb2_grpc.communicatorStub(channel)
        response = stub.makerequest(assignment_prototype_pb2.RequestCall(type=requestType, RequestMsg= option_type[requestType] + ' From ' + name))
        print(response.ResponseMsg)
        threading.Timer(time_gap, requestFunction,[port,requestType]).start()
        
        if requestType == 0:
            fail_count = 0

    except grpc.RpcError as rpc_error:
        #print(rpc_error)
        if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
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

    except KeyboardInterrupt:
        print('Process Killed')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

