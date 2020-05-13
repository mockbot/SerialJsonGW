#!/usr/bin/python3
"""
Serial JSON API
Author: Christian Mock
Date: 2020-05-10
Version: 2020-05-12 2100

Todo: 
send configuration commands and PWM to GPIO
connect roslibpy to websocket ros bridge and sent topics, test with RVIZ and PlotJuggler
connect paho to mosquitto server 
connect ros-mqtt-bridge
connect to donkeycar 

add more sensors: GPS,INA,HC04,RC channels,ADC
"""

import json
import random
import time
import serial
import io
import roslibpy
import paho


print("JSON serial receiver Test")
ser = serial.Serial('/dev/ttyACM0', timeout=1)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

#sio.write(unicode("\n"))
#sio.flush() # it is buffering. required to get the data out *now*

err=0
count=0

while True:
    json_string = sio.readline()
    try:
        data = json.loads(json_string)
        print(data["serial"],data["gyro"],data["accel"],data["magnetic"],data["temperature"],data["nmea"])
    except:
        print("ERROR:"+str(err)+" json decode error !!!")
        err=err+1




