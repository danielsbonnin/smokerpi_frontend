import sys
import time
import json
from datetime import datetime

while True:
    print(json.dumps({'x':datetime.now().isoformat(), 'y': temps[i]}))
    time.sleep(2)
    sys.stdout.flush()