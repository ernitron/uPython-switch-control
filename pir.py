# Micropython PIR
# Erni Tron ernitron@gmail.com
# Copyright (c) 2016

import time
from machine import Pin

class PirDevice():
    # D2	GPIO04	Pin(4)
    def __init__(self, p=4, sensor='Pir', place='noplace', server=''):
        self.pin = Pin(p, Pin.IN)
        self.sensor = sensor
        self.server = server
        self.place = place
        self.count = 0

    def get(self):
        self.count += 1
        return self.pin.value()

    def status(self):
        T = {}
        T['place'] = self.place
        T['server'] = self.server
        T['count'] = self.count
        T['sensor'] = self.sensor
        T['date'] = time.time()
        return T

# The Pir class initialized yo None
pir = None
