import sys
import time
import json
import tempHistory
from datetime import datetime

while True:
    print(tempHistory.get_latest())
    sys.stdout.flush()