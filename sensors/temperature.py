from time import sleep
from DFRobot_DHT20 import DFRobot_DHT20

# Configuracin del bus I2C y direcci del dispositivo
I2C_BUS = 0x01  # Usar I2C1
I2C_ADDRESS = 0x38  # Direccin I2C del sensor DHT20

# Inicializacin del sensor DHT20
dht20 = DFRobot_DHT20(I2C_BUS, I2C_ADDRESS)

def measure_temperature():
    # Verificar inicializacin del sensor
    if not dht20.begin():
        print("DHT20 sensor initialization failed")
        return None  # Devolver None si la inicializacin falla
    
    T_celcius, _, crc_error = dht20.get_temperature_and_humidity()

    if crc_error:
        print("CRC: Error\n")
        return None  # Devolver None si hay un error CRC
    else:
        return T_celcius  # Devolver la temperatura en grados Celsius

# Ejemplo de uso de la funcin
temperature = measure_temperature()
if temperature is not None:
    print(f"Temperature: {temperature:.2f} C")
else:
    print("Failed to measure temperature.")
