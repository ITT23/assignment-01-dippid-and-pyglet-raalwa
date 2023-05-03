'''
This module generates dummy data

Simulated acceleration data on the x/y/z axes and button presses
are sent every second to the local machine on port 5700.
'''
import socket
import time
import math
import random

IP = '127.0.0.1'
PORT = 5700

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# randomizes starting point to create different values each run
counter = random.randint(0, 100)
pressed = 0


def generate_dummy_acceleration(radian: int):
    '''
    Generates dummy acceleration values for x,y,z axes following sine functions

    Args:
        radian (int): Value to calculate sine with

    Returns:
        dict: x,y,z as [Key]s and sin(x,y,z) as [Value]s
    '''
    return {"x": str(math.sin(radian/10)),
            "y": str(math.sin(radian)),
            "z": str(math.sin(radian/5))
            }


def translate_button_state(btn_state: int):
    '''
    Helper function to translate int of button state to String

    Args:
        btn_state (int): current button state

    Returns:
        str: "pressed" for btn_state = 1 and "released" for btn_state = 0
    '''
    return "pressed" if btn_state else "released"


while True:
    accelerometer = '{"accelerometer" : "' + \
        str(generate_dummy_acceleration(radian=counter)) + '"}'

    # round a random float => 50% chance of button switch to occur
    # button_1 data is only sent to socket if button state changes
    if pressed != round(random.random()):
        # switch button state
        pressed = abs(pressed - 1)
        button_1 = '{"button_1" : "' + \
            str(translate_button_state(pressed)) + '"}'
        sock.sendto(str(button_1).encode(), (IP, PORT))

    print(accelerometer)
    sock.sendto(str(accelerometer).encode(), (IP, PORT))

    counter += 1
    time.sleep(1)
