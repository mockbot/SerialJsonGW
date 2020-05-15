#!/usr/bin/python3

import time
import random

import roslibpy

client = roslibpy.Ros(host='192.166.253.117', port=9090)
client.run()

talker = roslibpy.Topic(client, '/mm1/temperature', 'std_msgs/String')

while client.is_connected:
    temperature = random.uniform(30,31)
    talker.publish(roslibpy.Message({'data': temperature}))
    print('Sending message...'+str(temperature))
    time.sleep(1)

talker.unadvertise()

client.terminate()

