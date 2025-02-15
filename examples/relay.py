#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import RPi.GPIO as GPIO
import time

# Definir pin del relay
RELAY_PIN = 21

# Configurar el modo de pines a BCM
GPIO.setmode(GPIO.BCM)

# Configurar el pin del relay como salida
GPIO.setup(RELAY_PIN, GPIO.OUT)

# Activar el relay
GPIO.output(RELAY_PIN, GPIO.LOW)
time.sleep(0.5)  # Esperar medio segundo

# Desactivar el relay
GPIO.output(RELAY_PIN, GPIO.HIGH)
time.sleep(0.5)  # Esperar medio segundo

# Apagar el relay
GPIO.output(RELAY_PIN, GPIO.LOW)

# Limpiar configuraciones de GPIO
GPIO.cleanup()
