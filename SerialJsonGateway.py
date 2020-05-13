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
connect ros-mqtt-bridge and OpenHAB2
connect to donkeycar and simulator

add more sensors: GPS,INA,HC04,RC channels,ADC
add AHRS sensor fusion from raw imu values
add odometry sensors, wheel tick counter 

"""
enable_stdio=1  # enable loggin at console

enable_mqtt=0   # enable mqtt-connector, set ip address of the mqtt_broker when you enable this feature
mqtt_broker="m17" # address of the mqtt_broker

enable_ros=0                # enable ros-connector, set ip address of the rosbridge_server when you enable this feature
rosbridge_server="roscon"   # address of the rosbridge_server

import json
import random
import time
import serial
import io

if enable_ros == 1:
    import roslibpy

if enable_mqtt == 1:
   import paho.mqtt.publish as publish

# MQTT-Broker address
mqtt_broker="m17"


print("Serial JSON  Gateway")
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
        if enable_stdio == 1:
           print(data["serial"],data["gyro"],data["accel"],data["magnetic"],data["temperature"],data["nmea"])
    except:
        print("ERROR:"+str(err)+" json decode error !!!")
        err=err+1


    if enable_mqtt == 1:
        try:
            publish.single("/MM1/temperature", data["temperature"], hostname=mqtt_broker)
            publish.single("/MM1/gyro", data["gyro"], hostname=mqtt_broker)
            publish.single("/MM1/accel", data["accel"], hostname=mqtt_broker)
            publish.single("/MM1/magnetic", data["magnetic"], hostname=mqtt_broker)
        except:
            print("ERROR: mqtt publish error !!!")

