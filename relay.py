# Micropython PIR Switch Control
# Erni Tron ernitron@gmail.com
# Copyright (c) 2016

import time
from machine import Pin

# The Relay Switch Class
class Relay():
    # D8	GPIO15	Pin(15)
    # D5	GPIO14	Pin(14)
    # D0	GPIO0 	Pin(0)
    def __init__(self, p=14, sensor='relay', place='nowhere', server=''):
        self.pin = Pin(p, Pin.OUT)
	self.pin.value(0)
        self.status = 0
        self.count = 0
        self.sensor = sensor
        self.place = place
        self.server = server

    def get(self):
        return self.status

    def set(self, position):
        if position != self.status:
            self.pin.value(position)
            self.status = position
            self.count += 1
        return (self.status, self.count)

    def toggle(self):
        self.set(1 - self.status)

    def status(self):
        T = {}
        T['place'] = self.place
        T['server'] = self.server
        T['switch'] = self.status
        T['temp'] = str(self.status)
        T['count'] = self.count
        T['sensor'] = self.sensor
        T['date'] = time.time()
        return T


# Initialize
relay = None
