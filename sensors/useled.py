from gpiozero import LED
from time import sleep

# Definir el pin GPIO 37 como salida para el LED
led = LED(37)  # GPIO 37

try:
    while True:
        # Encender el LED
        led.on()
        print("LED encendido")
        sleep(1)  # Esperar 1 segundo

        # Apagar el LED
        led.off()
        print("LED apagado")
        sleep(1)  # Esperar 1 segundo
        
except KeyboardInterrupt:
    led.off()
    print("\nPrograma terminado. LED apagado.")