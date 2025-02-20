from gpiozero import Button, LED
from time import sleep

# Define row and column pins for the keypad matrix
row_pins = [27, 22, 5, 6]
col_pins = [25, 26, 19, 13]

# Define the key map for the keypad matrix
key_map = [
    ['1', '2', '3', '4'],
    ['5', '6', '7', '8'],
    ['9', '10', '11', '12'],
    ['13', '14', '15', '16']
]

# Initialize row input and column output pins
rows = [Button(pin, pull_up=True) for pin in row_pins]
cols = [LED(pin) for pin in col_pins]

# Continuously scan the keypad
try:
    while True:
        for col in cols:
            col.off()
            for row in rows:
                if row.is_active:
                    # Key pressed detected
                    row.wait_for_release()
                    print("Key press:", key_map[rows.index(row)][cols.index(col)])
                    break
            col.on()
        sleep(0.1)

except KeyboardInterrupt:
    print("End")

finally:
    # Clean up GPIO state
    for row in rows:
        row.close()
    for col in cols:
        col.close()
