from subprocess import call
import RPi.GPIO as GPIO
import time

# Clase para ejecutar comandos en la Raspberry Pi con Raspbian
class PcCommand():
    def __init__(self):
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

    def control_led(self, state):
        # Controlar un LED conectado al pin GPIO 18
        led_pin = 18
        GPIO.setup(led_pin, GPIO.OUT)
        if state == "on":
            GPIO.output(led_pin, GPIO.HIGH)
        elif state == "off":
            GPIO.output(led_pin, GPIO.LOW)
        else:
            print("Estado no válido. Usa 'on' o 'off'.")

    def read_temperature(self):
        # Leer la temperatura de un sensor DS18B20 (conexión 1-Wire)
        try:
            with open("/sys/bus/w1/devices/28-00000xxxxxxx/w1_slave", "r") as file:
                lines = file.readlines()
                if lines[0].strip()[-3:] == "YES":
                    temp_pos = lines[1].find("t=")
                    if temp_pos != -1:
                        temp = float(lines[1][temp_pos+2:]) / 1000.0
                        return f"La temperatura es {temp}°C"
        except Exception as e:
            return f"Error al leer la temperatura: {e}"
        return "No se pudo leer la temperatura."

    def cleanup_gpio(self):
        # Limpiar los pines GPIO al finalizar
        GPIO.cleanup()