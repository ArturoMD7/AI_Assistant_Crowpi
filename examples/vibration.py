#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

from gpiozero import OutputDevice as Vibration
import time

# Define vibration pin
vibration_sensor = Vibration(27)

# Turn on vibration
vibration_sensor.on()
# Wait half a second
time.sleep(0.5)

# Turn off vibration
vibration_sensor.off()