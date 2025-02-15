#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import RPi.GPIO as GPIO
import time

# Definir pin de vibracion
VIBRATION_PIN = 27

# Configurar el modo de pines a BCM
GPIO.setmode(GPIO.BCM)

# Configurar el pin de vibracion como salida
GPIO.setup(VIBRATION_PIN, GPIO.OUT)

# Encender vibracion
GPIO.output(VIBRATION_PIN, GPIO.HIGH)
time.sleep(0.5)  # Esperar medio segundo

# Apagar vibracion
GPIO.output(VIBRATION_PIN, GPIO.LOW)

# Limpiar configuraciones de GPIO
GPIO.cleanup()
