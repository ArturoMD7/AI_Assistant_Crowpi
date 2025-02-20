#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

from gpiozero import Servo
import time

servo = Servo(25)

def move_servo():
    """Mueve el servo entre sus posiciones mínima, media y máxima en bucle."""
    i = 0
    while (i<=2):
        servo.min()
        time.sleep(1)
        servo.mid()
        time.sleep(1)
        servo.max()
        time.sleep(1)
        i+=1
    
    servo.close()

if __name__ == "__main__":
    move_servo()
