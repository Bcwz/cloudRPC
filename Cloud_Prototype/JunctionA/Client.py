class Client():
    def __init__(self, name,logDir):
        self.name = name
        self.logDir = logDir

        self.host_port = 50053
        self.ping_port = 50054


        self.port_range = [50051,50056,50061,50066]
        self.controller_ports = [50055,50060,50065,50070]

        self.no_Of_client = 4
        self.functionType = 0

        self.junctions = ['JunctionA-Controller', 'JunctionB-Controller', 'JunctionC-Controller', 'JunctionD-Controller']
        self.traffic_lights = ['TL-A', 'TL-B','TL-C','TL-D']
        self.functions = ['Get Logs', 'Suspend Junction', 'View Status']
        