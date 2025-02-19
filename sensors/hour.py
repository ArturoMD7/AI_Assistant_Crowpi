from adafruit_ht16k33.segments import Seg7x4
import board
import busio
import time
from datetime import datetime

# Inicializa el bus I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Inicializa el display
display = Seg7x4(i2c)
display.brightness = 0.5  # Ajusta el brillo (0.0 a 1.0)

def show_system_time(display, duration=5):
    start_time = time.time()
    while time.time() - start_time < duration:
        now = datetime.now()
        current_time = now.strftime("%H%M")  # Formato de 24 horas, minutos
        display.print(current_time)
        display.colon = True  # Enciende los dos puntos (si tu display los tiene)
        display.show()
        time.sleep(1)

# Ejemplo de uso
show_system_time(display, 5)

display.fill(0)  # Apaga el display
display.show()