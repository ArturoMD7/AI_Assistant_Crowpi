#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import RPi.GPIO as GPIO
import time

# Configuración de pines para el botón y el buzzer
button_pin = 26
buzzer_pin = 18

# Configurar el modo de la placa a BCM
GPIO.setmode(GPIO.BCM)

# Configurar el pin del botón como entrada con pull-up y el del buzzer como salida
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer_pin, GPIO.OUT)

try:
    while True:
        # Verificar si el botón está presionado
        if GPIO.input(button_pin) == GPIO.LOW:
            # Encender el buzzer
            GPIO.output(buzzer_pin, GPIO.HIGH)
        else:
            # Apagar el buzzer
            GPIO.output(buzzer_pin, GPIO.LOW)
        time.sleep(0.1)  # Pequeña pausa para evitar rebotes

except KeyboardInterrupt:
    # Limpiar la configuración de los pines GPIO al salir
    GPIO.cleanup()
