import sys
import time
import json
import thermometer
from datetime import datetime

t = thermometer.Thermometer()
temps = []
def get_latest():
    json.dumps(temps.pop())

def get_history():
    return json.dumps(temps)

while True:
    temps.append({'x':datetime.now().isoformat(), 'y': t.get_f()})
    time.sleep(2)
