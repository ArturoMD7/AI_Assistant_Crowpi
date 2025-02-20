#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

from gpiozero import Buzzer
import time

# Initialize the buzzer on GPIO pin 18
buzzer = Buzzer(18)

# Make buzzer sound
buzzer.on()
time.sleep(0.5)

# Stop buzzer sound
buzzer.off()