# Micropython Http Server
# Erni Tron ernitron@gmail.com
# Copyright (c) 2016

#
from config import config

def application() :

    # Temperature sensor device
    from ds18b20 import sensor, TempSensor
    sensor = TempSensor()

    from register import register, Register
    rurl = config.get_config('register')
    auth = config.get_config('authorization')
    if rurl:
        register = Register(rurl, auth)

    # Pir device
    from pir import pir, PirDevice
    pir = PirDevice()

    # Relaye device
    from relay import relay, Relay
    pin = config.get_config('relay-pin')
    try: p = int(pin)
    except: p = 14
    relay = Relay(p)

    # The range application
    from ranges import ranges, Ranges
    ranges = Ranges()
    r = config.get_config('ranges')
    if r:
        ranges.set(r)

    # The control
    from control import control, Control
    timeout = config.get_config('timeout')
    if not timeout: timeout = 20
    control = Control(timeout)

    # Http Server
    from httpserver import Server
    server = Server()       # construct server object
    server.activate(8805)   # server activate with

    try:
        server.wait_connections(interface, 0) # activate and run for a while
        control.loop()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        sys.print_exception(e)
        print(e)



