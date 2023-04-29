'''
This module catches dummy data and prints it.

The dummy data is received from localhost on port 5700.
This module should be used in conjunction with DIPPID-sender.py
'''
from typing import Dict
from DIPPID import SensorUDP

# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)


def handle_accelerometer(data: Dict[str, Dict[str, float]]):
    '''
    Prints x,y,z acceleration data if any is received
    '''
    print(data)


def handle_button_1(data: str):
    '''
    Prints buttonstate of button_1 if any changes occured
    '''
    print(data)


sensor.register_callback('accelerometer', handle_accelerometer)
sensor.register_callback('button_1', handle_button_1)
