# Micropython PIR Switch Control
# Erni Tron ernitron@gmail.com
# Copyright (c) 2016

import time
from machine import Pin
from config import config

# The Relay Switch Class
class RelaySwitch():
    # D8	GPIO15	Pin(15)
    # D0	GPIO0 	Pin(0)
    def __init__(self, p=0):
        self.pin = Pin(p, Pin.OUT)
        self.switch_status = 0
        self.switch_count = 0
        self.sensor = config.get_config('chipid')
        self.place = config.get_config('place')

    def get(self):
        return self.switch_status

    def set(self, position):
        if position == 1:
            self.pin.value(1)
            self.switch_status = 1
        else :
            self.pin.value(0)
            self.switch_status = 0
        self.switch_count += 1
        return (self.switch_status, self.switch_count)

    def toggle(self):
        if self.switch_status == 0:
            self.set(1)
        else:
            self.set(0)
        self.switch_count += 1

    def status(self):
        T = {}
        T['place'] = config.get_config('place')
        T['server'] = config.get_config('address')
        T['switch'] = self.switch_status
        T['temp'] = str(self.switch_status)
        T['count'] = self.switch_count
        T['sensor'] = self.sensor
        T['date'] = time.time()
        return T

