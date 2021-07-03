@echo off
start python Traffic_Controller.py JunctionA-Controller JunctionB-Controller 50055 50060
start python Traffic_Light.py JunctionA TL-A TL-B 50051 50052
start python Traffic_Light.py JunctionA TL-B TL-C 50052 50053
start python Traffic_Light.py JunctionA TL-C TL-D 50053 50054
start python Traffic_Light.py JunctionA TL-D TL-A 50054 50051
pause