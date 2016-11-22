# Temperature Sensor contents
from ds18b20 import sensor
from config import config
import json

def cb_temperature():
    T = sensor.status()
    place = config.get_config('place')
    starttime = config.get_config('starttime')
    content = '<h1><a href="/">%s: %s °C</a></h1>' \
              '<p>Sensor %s - Reading # %d @ %s' \
              '</p>Started on %s</div>' % (place, T['temp'], T['sensor'], T['count'], T['date'], starttime)
    return content

def cb_temperature_json():
    T = sensor.status()
    # Now add some configuration params
    T['mac'] = config.get_config('mac')
    T['server'] = config.get_config('address')
    T['place'] = config.get_config('place')
    T['chipid'] = config.get_config('chipid')
    return json.dumps(T)
