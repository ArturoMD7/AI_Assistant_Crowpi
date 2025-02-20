#!/usr/bin/python
# -*- coding: utf-8 -*-
from gpiozero import DigitalInputDevice as IR
from gpiozero import OutputDevice as Relay
import time

# Define infrared sensor pin
ir = IR(20)
# Define relay pin
relay = Relay(21)

def exec_cmd(key_val):
    if key_val == 0x45:
        print("Button CH-")
    elif key_val == 0x46:
        print("Button CH")
    elif key_val == 0x47:
        print("Button CH+")
    elif key_val == 0x44:
        print("Button PREV")
    elif key_val == 0x40:
        print("Button NEXT")
    elif key_val == 0x43:
        print("Button PLAY/PAUSE")
    elif key_val == 0x07:
        print("Button VOL-")
        # Open relay
        relay.on()
    elif key_val == 0x15:
        print("Button VOL+")
        # Close relay
        relay.off()
    elif key_val == 0x09:
        print("Button EQ")
    elif key_val == 0x16:
        print("Button 0")
    elif key_val == 0x19:
        print("Button 100+")
    elif key_val == 0x0D:
        print("Button 200+")
    elif key_val == 0x0C:
        print("Button 1")
    elif key_val == 0x18:
        print("Button 2")
    elif key_val == 0x5E:
        print("Button 3")
    elif key_val == 0x08:
        print("Button 4")
    elif key_val == 0x1C:
        print("Button 5")
    elif key_val == 0x5A:
        print("Button 6")
    elif key_val == 0x42:
        print("Button 7")
    elif key_val == 0x52:
        print("Button 8")
    elif key_val == 0x4A:
        print("Button 9")

while True:
    if ir.value == 0:
        count = 0
        while ir.value == 0 and count < 200:
            count += 1
            time.sleep(0.00006)
        count = 0
        while ir.value == 1 and count < 80:
            count += 1
            time.sleep(0.00006)
        idx = 0
        cnt = 0
        data = [0, 0, 0, 0]
        
        for i in range(0, 32):
            count = 0
            while ir.value == 0 and count < 15:
                count += 1
                time.sleep(0.00006)
            count = 0
            while ir.value == 1 and count < 40:
                count += 1
                time.sleep(0.00006)
            if count > 8:
                data[idx] |= 1 << cnt
            if cnt == 7:
                cnt = 0
                idx += 1
            else:
                cnt += 1
        if data[0] + data[1] == 0xFF and data[2] + data[3] == 0xFF:
            print("Retrieve key: 0x%02x" % data[2])
            exec_cmd(data[2])
