#!/usr/bin/python
# -*- coding: utf-8 -*-

import smbus
import time

class LightSensor:
    def __init__(self):
        # Define some constants from the datasheet
        self.DEVICE = 0x5C  # Default device I2C address
        
        self.POWER_DOWN = 0x00  # No active state
        self.POWER_ON = 0x01  # Power on
        self.RESET = 0x07  # Reset data register value

        # Measurement modes
        self.ONE_TIME_HIGH_RES_MODE_1 = 0x20

        self.bus = smbus.SMBus(1)
    
    def convert_to_number(self, data):
        """Convert 2 bytes of data into a decimal number."""
        return (data[1] + (256 * data[0])) / 1.2

    def read_light(self):
        """Read light level from sensor."""
        data = self.bus.read_i2c_block_data(self.DEVICE, self.ONE_TIME_HIGH_RES_MODE_1)
        return self.convert_to_number(data)

def main():
    sensor = LightSensor()
    try:
        while True:
            print(f"Light Level: {sensor.read_light():.2f} lx")
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
