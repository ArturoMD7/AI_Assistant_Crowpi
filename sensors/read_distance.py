from gpiozero import DistanceSensor
import time

distancesensor = DistanceSensor(echo=12, trigger=16, max_distance=5)
    
try:
    distance_cm = distancesensor.distance * 100 
    print('Distance:', distance_cm, "cm")
    time.sleep(1)
except KeyboardInterrupt:
    print("Medición detenida por el usuario.")
