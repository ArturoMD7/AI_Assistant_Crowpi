from subprocess import call
import sys
import time

# Verificar si estamos en un entorno de Raspberry Pi (Linux)
if sys.platform.startswith("linux"):  # Solo ejecutar en Raspberry Pi
    from gpiozero import Buzzer

# Clase para ejecutar comandos en la Raspberry Pi con Raspbian
class PcCommand():
    def __init__(self):
        if sys.platform.startswith("linux"):  # Solo ejecutar en Raspberry Pi
            from gpiozero import Buzzer # Usar numeración BCM para los pines GPIO

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
        call("sudo python3 sensors/read_distance.py", shell=True)
    
    def use_buzzer(self):
        try:
            call("sudo python3 sensors/buzzer.py", shell=True)
        except Exception as e:
            print(f"Error al ejecutar el comando del buzzer: {e}")
