import HD44780MCP
import time
import MCP230XX

# Initialize MCP
i2cAddr = 0x21  # MCP23008/17 i2c address
MCP = MCP230XX.MCP230XX('MCP23008', i2cAddr)

# Turn on backlight if using Adafruit i2c LCD backpack (uses MCP23008)
blPin = 7  # Backlight pin when using Adafruit LCD backpack
MCP.set_mode(blPin, 'output')
MCP.output(blPin, True)  # Turn backlight on

# Set 16 character x 2 row LCD screen without rw pin, 4-bit mode
LCD = HD44780MCP.HD44780(MCP, 1, -1, 2, [3, 4, 5, 6], rows=2, characters=16, mode=0, font=0)

# Display text on the LCD
LCD.display_string("Hola Humano")
time.sleep(1)
LCD.display(False)  # Turn display off
time.sleep(1)
LCD.display()  # Turn display on
LCD.set_cursor(2, 1)  # Move cursor to 2nd row, 1st position
LCD.display_string("Soy GAMA")
time.sleep(2)

# Blink cursor
LCD.blink()  # Blink cursor position
time.sleep(2)
LCD.blink(False)  # Turn blinking off
time.sleep(2)

# Toggle cursor
LCD.cursor(False)  # Turn cursor off
time.sleep(2)
LCD.cursor()  # Turn cursor on
time.sleep(2)


# Clear display
LCD.clear_display()

# Turn backlight off
MCP.output(blPin, False)