from __future__ import print_function
from concurrent import futures
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

JunctionName = str(sys.argv[1])
name = str(sys.argv[2])
ping_target = str(sys.argv[3]) 
host_port = int(sys.argv[4]) 
ping_port = int(sys.argv[5]) 

logDir = JunctionName+ '_'+name+'_log.log'
logOutDir = JunctionName+ '_'+ name + '_Output.log'


time_gap = 30
max_fail = 3
fail_count = 0
host = 'localhost'

controller_port = 50055

option_type = ['Ping','Report Accident', 'Report Suspicious Vehicle','Report Taffic Light Failure']
comm = communicator.communicator(name,None,None)

script_dir = os.path.dirname(__file__)
CA_path = "Cert/root-ca.pem"
root_CA = os.path.join(script_dir, CA_path)
key_path = "Cert/root-ca-key.pem"
root_KEY = os.path.join(script_dir, key_path)

#suspicious_vehicle = {'SK123A','SC1235B','ST9021A'}
#Disabled the telegram (So called Send to LTA/Cloud)

  
def requestFunction(port, requestType):
    global fail_count
    try:
        with open(root_CA, 'rb') as f:
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
                #Call the Cloud Services when failed to ping Traffic Light B
                    print('Failed to ping Traffic Light ' + ping_target)
                    requestFunction(controller_port, 3)
                    fail_count = 0
                threading.Timer(time_gap, requestFunction,[port,requestType]).start()

            else:
                print('Failed to ' + option_type[requestType])

            if port == controller_port:
                logging.info('Failed to communicate with Junction Controller')
                print('Failed to communicate with Junction Controller')
            #print('Client Not Available...Failure Count: ', fail_count)
            

def random_Event():
    #Randomized within 10 to 60s
    next_evt_trigger = random.randint(90,180)
    evt = random.randint(1,2)
    # Both Report Accident and Report Vehicle should be sent to the junction controller, so it should be controller port
    threading.Thread(target=requestFunction, args=(controller_port,evt,)).start()
    logging.info(option_type[evt] + ' sent to controller')
    threading.Timer( next_evt_trigger, random_Event).start()

def messageBox(messageHeader, message):
    root= tk.Tk()
    root.withdraw()

    MsgBox = tk.messagebox.askquestion (messageHeader,message,icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
    else:
        tk.messagebox.showinfo('Return','You will now return to the application screen')

def run_server():
    logging.info('Server '+JunctionName+  ' Started')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    with open(key_path, 'rb') as f:
        private_key = f.read()

    with open(CA_path, 'rb') as f:
        certificate_chain = f.read()
    
    server_credentials = grpc.ssl_server_credentials( ( (private_key, certificate_chain), ) )
    assignment_prototype_pb2_grpc.add_communicatorServicer_to_server(comm, server)
    server.add_secure_port('[::]:'+str(host_port), server_credentials)
    server.start()
    server.wait_for_termination()



if __name__ == '__main__':
    logging.basicConfig(filename=logDir, level=logging.INFO,format='%(message)s @ %(asctime)s')    

    #messageBox('Receive File','Are you sure to receive File?')

    #Basically, the general idea is to run both client and server example to perform distributed communications...
    #Simply said, what's done here is to run the server and every 30s, it will ping alive another machine...    
    
    try:
        comm.logDir = logDir
        comm.logOutDir = logOutDir
        comm.clientName = name
        print(comm.logDir)

        next_evt_trigger = random.randint(90,180)
        #threading.Thread(target=run_server, args=()).start()
        
        threading.Timer(next_evt_trigger, random_Event).start()
        threading.Timer(time_gap, requestFunction,[ping_port,0]).start()
        run_server()

    except KeyboardInterrupt:
        print('Process Killed')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)