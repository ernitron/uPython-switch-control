# Micropython PIR Switch Control
# Erni Tron ernitron@gmail.com
# Copyright (c) 2016

import time
import gc

# Import the classes
from register import register
from relay import relay
from pir import pir
from ranges import ranges

class Control():
    def __init__(self, timeout=10):
        self.counter = 0
        self.presence = 0
        self.before = 0
        self.timeout = timeout

        # Let's start
        relay.set(0)
        print('Relay ready', self.timeout)

    def switch_on(self):
        self.counter = 0
        relay.set(1)
        return 'On!'

    def switch_off(self):
        self.counter = 0
        relay.set(0)
        return 'Off!'

    def status(self):
        if relay.get() == 1:
            return 'on'
        else:
            return 'off'

    def loop(self):
    	if not ranges.inrange() :
            relay.set(0)
            return

	#Get Sensor presence
        #print('Waiting PIR...')
        self.presence = pir.get()
        if self.presence :
          if not self.before :
            print('Switch on')
            relay.set(1)
            self.counter = 0
            register(relay.status())
        elif relay.get() == 1:
            self.counter += 1
            if self.counter > self.timeout:
                print('Timeout: switch off')
                relay.set(0)
                self.counter = 0
                register(relay.status())
            else:
                print(self.counter, end='..')
        # Save it for next loop
        self.before = self.presence

    def loop_time(self):
        if ranges.inrange():
            print('Timeout: switch on')
            relay.set(1)
        else:
            print('Timeout: switch off')
            relay.set(0)
        register(relay.status())

# The Control Class // initialized as NONE!
control = None

