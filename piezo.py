# Micropython Switch Control
# Erni Tron ernitron@gmail.com
# Copyright (c) 2016

import time
from machine import Pin

#Temperature Sensor on D3 (which is GPIO0) // It is pull-up
#Relay Sensor       on D8 (which is GPIO15) // Starts LOW
#PIR Sensor         on D2 (which is GPIO4) //
#PiezoSound         on D1 (which is GPIO5)
#PiezoSound    also on D5 (which is GPIO14) // Put a 4.7kohm in Parallel

class PiezoSound():
    # Connect + to D1 of WeMos
    # D1    GPIO5	Pin(5)
    # this is because when it starts it is LOW
    def __init__(self, p=5, microsleep=50, macrosleep=200):
        self.pin = Pin(p, Pin.OUT)
        self.pin.value(0)
        self.microsleep = microsleep
        self.macrosleep = macrosleep
    def beep(self):
        self.pin.value(1)
        time.sleep_ms(self.microsleep)
        self.pin.value(0)
    def beepbeep(self):
        for i in range(10):
            self.pin.value(1)
            time.sleep_ms(self.microsleep)
            self.pin.value(0)
            time.sleep_ms(self.microsleep)
    def alarm(self):
        for i in range(10):
            self.beepbeep()
            time.sleep_ms(self.macrosleep)
    def alarm_forever(self):
        while True:
            self.beep()
            time.sleep_ms(self.macrosleep)

# The Piezo class initialized yo None
#piezo = PiezoSound(14, 50, 200)
piezo = None

