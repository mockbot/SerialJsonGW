"""
MM1 JSON API
Author: Christian Mock
Date: 2020-05-11
Version: 2020-05-12 2100

"""
import json
import random
import time
import board
import busio
from robohat_mpu9250.mpu9250 import MPU9250
from robohat_mpu9250.mpu6500 import MPU6500
from robohat_mpu9250.ak8963 import AK8963

from time import sleep

i2c = busio.I2C(board.SCL, board.SDA)
mpu = MPU6500(i2c, address=0x69)
ak = AK8963(i2c)
sensor = MPU9250(mpu, ak)

serial=1
delay=0.1

print("MM1 cpy JSON Test")

json_sot = "{"
json_eot = "}"

while True:
        # Fake data for json testing
        LON=random.uniform(1,180)
        LAT=random.uniform(1,180)

        gyro=sensor.read_gyro()
        accel=sensor.read_acceleration()
        magnetic=sensor.read_magnetic()

	json_serial = "\"serial\":\""+str(serial)+"\","
	json_gyro = "\"gyro\":\""+str(gyro)+"\","
	json_accel = "\"accel\":\""+str(accel)+"\","
	json_magnet = "\"magnetic\":\""+str(magnetic)+"\","
	json_nmea = "\"nmea\":\"#GGA:W"+str(LON)+","+str(LAT)+"\""
	json_string=json_sot\
		+json_serial\
		+json_gyro\
		+json_accel\
		+json_magnet\
		+json_nmea\
		+json_eot
	print(json_string)
	serial = serial+1
	time.sleep(delay)

