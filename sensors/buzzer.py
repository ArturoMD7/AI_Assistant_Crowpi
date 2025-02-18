import sys
import time
#import os
#os.environ['GPIOZERO_PIN_FACTORY'] = os.environ.get('GPIOZERO_PIN_FACTORY', 'mock')
from gpiozero import Buzzer


try:
        # Configuración del buzzer en el pin GPIO 18
    buzzer = Buzzer(18)

    print("Activando el buzzer durante 1 segundo...")
    buzzer.on()  # Activar el buzzer
    time.sleep(1)  # Mantener el buzzer encendido por 3 segundos
    buzzer.off()  # Desactivar el buzzer
    buzzer.close()
    print("Buzzer apagado.")

except Exception as e:
    print(f"Error al controlar el buzzer: {e}")
