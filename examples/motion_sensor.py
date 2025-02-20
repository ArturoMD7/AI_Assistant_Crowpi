#!/usr/bin/python
# -*- coding: utf-8 -*-

from gpiozero import DigitalInputDevice as MOTION
import time

# Define motion pin
motion = MOTION(23)

while True:
    if motion.value == 0:
        print("Nothing moves ...")
    else:
        print("Motion detected!")
    time.sleep(0.1)
