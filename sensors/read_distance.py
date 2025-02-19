import sys
import time

if sys.platform.startswith("linux"):  # Si es Raspberry Pi
            from gpiozero import DistanceSensor

def measure_distance():
    distancesensor = DistanceSensor(echo=12, trigger=16, max_distance=5)
    try:
        distance_cm = distancesensor.distance * 100  # Convertir a centímetros
        print('Distance:', distance_cm, "cm")
        return distance_cm  # Devolver la distancia medida
    except KeyboardInterrupt:
        print("Medición detenida por el usuario.")
        return None  # Devolver None si se interrumpe la medición