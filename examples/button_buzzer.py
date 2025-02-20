#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

from gpiozero import Button, Buzzer
import time

# Configure both button and buzzer pins
button = Button(26)
buzzer = Buzzer(18)

try:
    while True:
        if button.is_pressed:
            buzzer.on()  # Turn on the buzzer if the button is pressed
        else:
            buzzer.off()  # Turn off the buzzer if the button is not pressed
except KeyboardInterrupt:
    # CTRL+C detected, cleaning and quitting the script
    buzzer.off()