from time import strftime, sleep
from DFRobot_DHT20 import DFRobot_DHT20

I2C_BUS = 0x01  # Default use I2C1 bus
I2C_ADDRESS = 0x38  # Default I2C device address

dht20 = DFRobot_DHT20(I2C_BUS, I2C_ADDRESS)

# Initialize sensor
if not dht20.begin():
    print("DHT20 sensor initialization failed")
else:
    while True:
        print(strftime("%Y-%m-%d %H:%M:%S %Z"))
        T_celcius, humidity, crc_error = dht20.get_temperature_and_humidity()
        
        if crc_error:
            print("CRC : Error\n")
        else:
            T_fahrenheit = T_celcius * 9 / 5 + 32
            print(f"Temperature : {T_celcius:.2f}°C / {T_fahrenheit:.2f}°F")
            print(f"Relative Humidity : {humidity:.2f} %")
            print("CRC : OK\n")
        
        sleep(5)
