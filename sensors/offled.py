from gpiozero import LED
import time

# Define LED pin
led = LED(26)

led.off()
# Wait half a second
time.sleep(0.2)