#!/usr/bin/python
# -*- coding: utf-8 -*-

from gpiozero import DigitalInputDevice as Touch
import time

touch_sensor = Touch(17)

while True:
    if touch_sensor.value:
        print('Touch Detected')
    time.sleep(0.1)
