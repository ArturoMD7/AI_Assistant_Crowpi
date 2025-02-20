#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/
from gpiozero import LED
import time

# Define LED pin
led = LED(26)

# Turn on LED
led.on()
# Wait half a second
time.sleep(0.2)
# Turn off LED
led.off()
# Wait half a second
time.sleep(0.2)

