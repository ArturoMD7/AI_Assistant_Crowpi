#!/usr/bin/python
# -*- coding: utf-8 -*-

from gpiozero import DistanceSensor
import time

# Initialize distance sensor
distance_sensor = DistanceSensor(echo=12, trigger=16, max_distance=5)

while True:
    print(f"Distance: {distance_sensor.distance * 100:.2f} cm")
    time.sleep(1)
