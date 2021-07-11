@echo off
start python Traffic_Controller.py JunctionA-Controller JunctionB-Controller DEFAULT 50055 50060 50051
start python Traffic_Light.py JunctionA TL-A TL-B 50051 50052 Green
start python Traffic_Light.py JunctionA TL-B TL-C 50052 50053 Red
start python Traffic_Light.py JunctionA TL-C TL-D 50053 50054 Green
start python Traffic_Light.py JunctionA TL-D TL-A 50054 50051 Red
start python Traffic_Controller.py JunctionB-Controller JunctionC-Controller NORMAL 50060 50065 50056
start python Traffic_Light.py JunctionB TL-A TL-B 50056 50057 Green
start python Traffic_Light.py JunctionB TL-B TL-C 50057 50058 Red
start python Traffic_Light.py JunctionB TL-C TL-D 50058 50059 Green
start python Traffic_Light.py JunctionB TL-D TL-A 50059 50056 Red
start python Traffic_Controller.py JunctionC-Controller JunctionD-Controller NORMAL 50065 50070 50061
start python Traffic_Light.py JunctionC TL-A TL-B 50061 50062 Green
start python Traffic_Light.py JunctionC TL-B TL-C 50062 50063 Red
start python Traffic_Light.py JunctionC TL-C TL-D 50063 50064 Green
start python Traffic_Light.py JunctionC TL-D TL-A 50064 50061 Red
start python Traffic_Controller.py JunctionD-Controller JunctionA-Controller NORMAL 50070 50055 50066
start python Traffic_Light.py JunctionD TL-A TL-B 50066 50067 Green
start python Traffic_Light.py JunctionD TL-B TL-C 50067 50068 Red
start python Traffic_Light.py JunctionD TL-C TL-D 50068 50069 Green
start python Traffic_Light.py JunctionD TL-D TL-A 50069 50066 Red
pause