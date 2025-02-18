from gpiozero import DigitalInputDevice as Sound
import time
i = 0

def detect_sound():
    sound_sensor = Sound(24)
    try:
        i = 0
        while True:
            # Check if sound is detected
            
            i = i+1
            if sound_sensor.value == 0:
                print('Sound Detected' + str(i))
                time.sleep(1)
    except KeyboardInterrupt:
        print("Medición detenida por el usuario.")
        return None
    
detect_sound()