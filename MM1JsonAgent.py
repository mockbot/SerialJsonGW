"""
MM1 JSON API PoC
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
from adafruit_ina219 import INA219

from time import sleep

i2c = busio.I2C(board.SCL, board.SDA)

mpu = MPU6500(i2c, address=0x69)
ak = AK8963(i2c)
sensor_mpuak = MPU9250(mpu, ak)

ina219 = INA219(i2c,0x41)

serial=1
delay=0.1

capability = "serial,gyro,accel,magnetic,temperature,nmea,vbus,vshunt,current"

print("MM1 cpy JSON Agent (PoC)")

json_sot = "{"
json_eot = "}"

while True:
        # Fake data for json testing
        LON=random.uniform(1,180)
        LAT=random.uniform(1,180)

        gyro=sensor_mpuak.read_gyro()
        accel=sensor_mpuak.read_acceleration()
        magnetic=sensor_mpuak.read_magnetic()
        temperature = sensor_mpuak.read_temperature()
        vshunt = ina219.shunt_voltage
        vbus = ina219.bus_voltage
        current = ina219.current

	json_serial = "\"serial\":\""+str(serial)+"\","
	json_capability = "\"capability\":\""+capability+"\","
	json_gyro = "\"gyro\":\""+str(gyro)+"\","
	json_accel = "\"accel\":\""+str(accel)+"\","
	json_magnet = "\"magnetic\":\""+str(magnetic)+"\","
	json_temperature = "\"temperature\":\""+str(temperature)+"\","
	json_vshunt = "\"vshunt\":\""+str(vshunt)+"\","
	json_vbus = "\"vbus\":\""+str(vbus)+"\","
	json_current = "\"current\":\""+str(current)+"\","
	json_nmea = "\"nmea\":\"#GGA:W"+str(LON)+","+str(LAT)+"\""

	json_string=json_sot\
		+json_serial\
		+json_capability\
		+json_vshunt\
		+json_vbus\
		+json_current\
		+json_gyro\
		+json_accel\
		+json_magnet\
		+json_temperature\
		+json_nmea\
		+json_eot
	print(json_string)
	serial = serial+1
	time.sleep(delay)

