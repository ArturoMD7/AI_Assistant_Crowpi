#!/usr/bin/python
# -*- coding: utf-8 -*-

from gpiozero import DigitalInputDevice as Tilt
import time

tilt_sensor = Tilt(22)

while True:
    if tilt_sensor.value:
        print("[-] Left Tilt")
    else:
        print("[-] Right Tilt")
    time.sleep(1)
