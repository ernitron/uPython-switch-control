# Micropython Http Server
# Erni Tron ernitron@gmail.com
# Copyright (c) 2016
import time
import network
import machine
import gc
from ubinascii import hexlify
from config import config

def do_connect(ssid, pwd):
    sta_if = network.WLAN(network.STA_IF)

    # Stage zero if credential are null void connection
    if not pwd or not ssid :
        print('Disconnect from all known networks')
        sta_if.active(False)
        return None

    # Stage one check for default connection
    t = 10
    while t > 0:
        time.sleep_ms(200)
        if sta_if.isconnected():
            print('Connect to default: ', sta_if.ifconfig())
            return sta_if
        t -= 1

    # Stage two if not yet connected force active and connect with ssid/pwd
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(ssid, pwd)
        t = 10
        while t > 0:
            if sta_if.isconnected():
                print('Connect to: ', sta_if.ifconfig())
                return sta_if
            time.sleep_ms(500)
            t -= 1
    # No way we are not connected
    print('Cant Connect')
    return None

def do_accesspoint(ssid, pwd):
    ap_if = network.WLAN(network.AP_IF)
    if pwd == '' or ssid == '':
        ap_if.active(False)
        print('Disabling AP')
        return None
    ap_if.config(essid=ssid, password=pwd)
    ap_if.active(True)
    time.sleep_ms(200)
    print('AP config: ', ap_if.ifconfig())
    return ap_if

#----------------------------------------------------------------
# MAIN PROGRAM STARTS HERE
def main():

    # Enable automatic garbage collector
    gc.enable()

    config.read_config()

    # Get defaults
    ssid = config.get_config('ssid')
    pwd = config.get_config('pwd')

    # Connect to Network and save if
    sta_if = do_connect(ssid, pwd)

    chipid = hexlify(machine.unique_id())
    config.set_config('chipid', chipid)

    # Turn on Access Point only if AP PWD is present
    apssid = 'YoT-%s' % bytes.decode(chipid)
    appwd = config.get_config('appwd')
    do_accesspoint(apssid, appwd)

    # To have time to press ^c
    time.sleep(2)

    # Update config with new values
    # Get Network Parameters
    if sta_if != None:
        (address, mask, gateway, dns) = sta_if.ifconfig()
        config.set_config('address', address)
        config.set_config('mask', mask)
        config.set_config('gateway', gateway)
        config.set_config('dns', dns)
        config.set_config('mac', hexlify(sta_if.config('mac'), ':'))

    # Ok now we save configuration!
    config.set_time()
    config.save_config()

    # Free some memory
    ssid = pwd = None
    apssid = appwd = None
    address = mask = gateway = dns = None
    gc.collect()

    #
    from httpserver import Server
    server = Server(8805)    # construct server object
    server.activate(timeout=0.3) # activate

    # Initialize an external Control
    from control import control
    control.loop()
    server.wait_connections()

    try:
        while True:
           control.loop()
           server.wait_connections()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
        machine.reset()
        pass

