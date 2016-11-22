# Micropython PIR
# Erni Tron ernitron@gmail.com
# Copyright (c) 2016

import time
from machine import Pin
from config import config

class PirDevice():
    # D2	GPIO04	Pin(4)
    def __init__(self, p=4):
        self.pin = Pin(p, Pin.IN)
        self.sensor = config.get_config('pir')
        self.place = config.get_config('place')
        self.count = 0

    def get(self):
        self.count += 1
        return self.pin.value()

    def status(self):
        T = {}
        T['place'] = config.get_config('place')
        T['server'] = config.get_config('address')
        T['count'] = self.count
        T['sensor'] = self.sensor
        T['date'] = time.time()
        return T

