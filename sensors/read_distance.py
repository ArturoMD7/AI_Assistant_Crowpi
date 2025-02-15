import sys
import time

if sys.platform.startswith("linux"):  # Solo ejecutar en Raspberry Pi
    import RPi.GPIO as GPIO

def measure_distance():
    if not sys.platform.startswith("linux"):  # Si no es Raspberry Pi
        print("Ejecutando en un entorno que no es Raspberry Pi, simulando medición de distancia.")
        return 25.0  # Simula una distancia de 25 cm

    try:
        GPIO.setmode(GPIO.BCM)

        TRIG = 16
        ECHO = 12

        print("Distance Measurement In Progress")

        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)

        GPIO.output(TRIG, False)
        print("Waiting For Sensor To Settle")
        time.sleep(2)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)

        print("Distance: %scm" % distance)

        return distance

    except Exception as e:
        print(f"Error al medir la distancia: {e}")
        return None

    finally:
        if sys.platform.startswith("linux"):  # Solo limpiar GPIO en Raspberry Pi
            GPIO.cleanup()