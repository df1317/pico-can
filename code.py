# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""Example for Pico. Turns on the built-in LED."""
import board
import digitalio
from time import sleep
import busio
import adafruit_l3gd20
import adafruit_lis3dh

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

I2C = busio.I2C(board.SCL, board.SDA)
ACCEL = adafruit_lis3dh.LIS3DH_I2C(I2C)
GYRO = adafruit_l3gd20.L3GD20_I2C(I2C)

while True:
    led.value = not led.value
    print(led.value)
    print("Acceleration (m/s^2): X=%0.3f Y=%0.3f Z=%0.3f"%ACCEL.acceleration)
    print("Gyro (rad/s): X=%0.3f Y=%0.3f Z=%0.3f"%GYRO.gyro)
    sleep(0.5)