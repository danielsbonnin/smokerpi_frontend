import sys
import time
import json
import thermometer
from datetime import datetime

t = thermometer.Thermometer()

while True:
    print(json.dumps({'x':datetime.now().isoformat(), 'y': t.get_f()}))
    time.sleep(2)
    sys.stdout.flush()
