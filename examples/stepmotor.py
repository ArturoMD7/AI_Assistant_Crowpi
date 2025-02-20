#!/usr/bin/python
# -*- coding: utf-8 -*-
# Original Author: Ludwig Schuster
# Original GitHub: https://github.com/ludwigschuster/RasPi-GPIO-Stepmotor
# Adapted from: http://elecrow.com/

from gpiozero import OutputDevice
import time
import math

# Declarar pines como salida
pin_A = OutputDevice(5)
pin_B = OutputDevice(6)
pin_C = OutputDevice(13)
pin_D = OutputDevice(19)

class Stepmotor:
    def __init__(self):
        self.interval = 0.010

    def Step1(self):
        pin_D.on()
        time.sleep(self.interval)
        pin_D.off()

    def Step2(self):
        pin_D.on()
        pin_C.on()
        time.sleep(self.interval)
        pin_D.off()
        pin_C.off()

    def Step3(self):
        pin_C.on()
        time.sleep(self.interval)
        pin_C.off()

    def Step4(self):
        pin_B.on()
        pin_C.on()
        time.sleep(self.interval)
        pin_B.off()
        pin_C.off()

    def Step5(self):
        pin_B.on()
        time.sleep(self.interval)
        pin_B.off()

    def Step6(self):
        pin_A.on()
        pin_B.on()
        time.sleep(self.interval)
        pin_A.off()
        pin_B.off()

    def Step7(self):
        pin_A.on()
        time.sleep(self.interval)
        pin_A.off()

    def Step8(self):
        pin_A.on()
        pin_D.on()
        time.sleep(self.interval)
        pin_D.off()
        pin_A.off()

    def turn(self, count):
        for _ in range(int(count)):
            self.Step1()
            self.Step2()
            self.Step3()
            self.Step4()
            self.Step5()
            self.Step6()
            self.Step7()
            self.Step8()

    def close(self):
        """Liberar los pines GPIO"""
        pin_A.close()
        pin_B.close()
        pin_C.close()
        pin_D.close()

    def turnSteps(self, count):
        """Girar n pasos"""
        for _ in range(count):
            self.turn(1)

    def turnDegrees(self, degrees):
        """Girar n grados (pequeños valores pueden generar inexactitudes)"""
        self.turn(round(degrees * 512 / 360, 0))

    def turnDistance(self, dist, rad):
        """Girar basado en la distancia y el radio (puede haber inexactitudes)"""
        self.turn(round(512 * dist / (2 * math.pi * rad), 0))

def main():
    print("Movimiento iniciado")
    motor = Stepmotor()
    
    print("Un paso")
    motor.turnSteps(1)
    time.sleep(0.5)
    
    print("20 pasos")
    motor.turnSteps(20)
    time.sleep(0.5)
    
    print("Un cuarto de vuelta")
    motor.turnDegrees(90)
    
    print("Movimiento detenido")
    motor.close()

if __name__ == "__main__":
    main()
