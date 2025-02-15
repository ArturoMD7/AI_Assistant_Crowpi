from subprocess import call
import sys
import time

# Verificar si estamos en un entorno de Raspberry Pi (Linux)
if sys.platform.startswith("linux"):
    import RPi.GPIO as GPIO
    from sensors.read_distance import measure_distance  # Importar la nueva función
else:
    print("Ejecutando en un entorno que no es Raspberry Pi, ignorando RPi.GPIO")

# Clase para ejecutar comandos en la Raspberry Pi con Raspbian
class PcCommand():
    def __init__(self):
        if sys.platform.startswith("linux"):  # Solo configurar GPIO en Raspberry Pi
            GPIO.setmode(GPIO.BCM)  # Usar numeración BCM para los pines GPIO

    def open_chrome(self, website):
        # Abrir Chrome en Raspbian
        website = "" if website is None else website
        call(f"chromium-browser {website}", shell=True)

    def open_epiphany(self, website):
        # Abrir Epiphany (navegador web ligero para Raspberry Pi)
        website = "" if website is None else website
        call(f"epiphany {website}", shell=True)

    def open_terminal(self):
        # Abrir una terminal en Raspbian
        call("lxterminal", shell=True)

    def read_distance(self):
        if not sys.platform.startswith("linux"):  # Si no es Raspberry Pi
            return "Simulando medición de distancia: 25 cm"  # Simular una distancia en Windows

        # Medir la distancia usando el sensor ultrasónico
        distance = measure_distance()
        if distance is not None:
            return f"La distancia medida es {distance} cm"
        else:
            return "No se pudo medir la distancia."