from subprocess import call
import sys
import time
import os

# Importar la función measure_distance desde read_distance.py
from sensors.read_distance import measure_distance
from sensors.temperature import measure_temperature

# Clase para ejecutar comandos en la Raspberry Pi con Raspbian
class PcCommand():
    def __init__(self):
        if sys.platform.startswith("linux"):  # Solo ejecutar en Raspberry Pi
            from gpiozero import Buzzer  # Usar numeración BCM para los pines GPIO

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

        # Llamar a la función measure_distance para obtener la distancia
        distance_cm = measure_distance()
        if distance_cm is not None:
            return f"La distancia medida es {distance_cm:.2f} cm"  # Formatear a 2 decimales
        else:
            return "No se pudo medir la distancia."
        
    def read_temperature(self):
        if not sys.platform.startswith("linux"):  # Si no es Raspberry Pi
            return "Simulando mediciónn de temperatura: 16 grados"  # Simular una distancia en Windows

        # Llamar a la función measure_distance para obtener la distancia
        temperature = measure_temperature()
        if temperature is not None:
            return(f"la Temperatura es de: {temperature:.2f} grados Celcius")
        else:
            return("Fallo al medir la temperatura.")

    def use_buzzer(self):
        try:
            call("sudo python3 sensors/buzzer.py", shell=True)
        except Exception as e:
            print(f"Error al ejecutar el comando del buzzer: {e}")

    def use_matrix(self):
        try:
            call("sudo python3 sensors/matrix.py", shell=True)
        except Exception as e:
            print(f"Error al ejecutar el comando de la matrix: {e}")
            
    def use_lcd(self):
        try:
            call("sudo python3 sensors/lcd.py", shell=True)
        except Exception as e:
            print(f"Error al ejecutar el comando de lcd: {e}")
            
    def show_hour(self):
        try:
            call("sudo python3 sensors/hour.py", shell=True)
        except Exception as e:
            print(f"Error al ejecutar el comando de hora: {e}")
