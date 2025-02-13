#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import RPi.GPIO as GPIO
import time

# Definir el pin del buzzer
buzzer_pin = 18

# Configurar el modo de los pines
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

try:
    # Hacer sonar el buzzer
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(0.5)
    
    # Detener el sonido del buzzer
    GPIO.output(buzzer_pin, GPIO.LOW)

finally:
    # Limpiar los recursos de GPIO
    GPIO.cleanup()