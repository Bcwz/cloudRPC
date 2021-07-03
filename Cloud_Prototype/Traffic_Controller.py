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
name = 'JunctionA-Controller'
host = 'localhost'
host_port = 50055
#ping_port = 50055
time_gap = 30
num_of_TL = 4
suspend = False

bot = tg.tg()
def run_server():
    logging.info('Server Started')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    assignment_prototype_pb2_grpc.add_communicatorServicer_to_server(communicator.communicator(), server)
    server.add_insecure_port('[::]:'+str(host_port))
    server.start()
    server.wait_for_termination()

def forward_log(port):
   
    try:
        
        channel = grpc.insecure_channel(host + ':'+str(port))
        stub = assignment_prototype_pb2_grpc.communicatorStub(channel)
        response = stub.getLogs(assignment_prototype_pb2.RequestLog(types=3))
        
        f = open(response.filename, "w")
        f.write(response.Content)
        f.close()

        bot.logDir = response.filename
        bot.telegram_bot_sendFiles()   
    except grpc.RpcError as rpc_error:
        #print(rpc_error)
        if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
            print('Port ' + str(port) +' is unavailable...')



def transfer_All_Logs():
    
    try:
        for i in range(50051, 50055):
            forward_log(i)
            
    except KeyboardInterrupt:
        print('Process Killed')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

   


if __name__ == '__main__':
    logging.basicConfig(filename='Traffic_Controller.log', level=logging.INFO,format='%(message)s @ %(asctime)s')
      
    try:
        #transfer_All_Logs()
        #threading.Thread(target=run_server, args=()).start()
        #run_server()
        p = multiprocessing.Process(target=run_server)
        p.start()
        #threading.Thread(target=telegram_start_server, args=()).start()
        
        bot.telegram_start_server()

    except KeyboardInterrupt:
        print('Process Killed')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

