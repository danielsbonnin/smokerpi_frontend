import os
import time
import threading
DEVICE_NAME = '28-041692c6bfff'
class Thermometer:
    def __init__(self, d_name=DEVICE_NAME):
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')
        self.temp_sensor = '/sys/bus/w1/devices/' + d_name + '/w1_slave'
        self.time_last_read = 0
        self.f = -500
        self.c = -500
        self.read_temp()
    
    def temp_raw(self):
        f = open(self.temp_sensor, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp(self):
        lines = self.temp_raw()
        while lines[0].strip()[-3:]!='YES':
            time.sleep(0.5)
        lines = self.temp_raw()
        temp_output = lines[1].find('t=')

        if temp_output != -1:
            temp_string = lines[1].strip()[temp_output+2:]
            self.c = float(temp_string)/1000.0
            self.f = self.c * 9.0 / 5.0 + 32.0
            self.time_last_read = time.time()
        else:
            return (None, None)

    def get_f(self):
        if time.time() - self.time_last_read > 2:
            t = threading.Thread(target=self.read_temp)
            t.start()
        return self.f
    
    def get_c(self):
        if time.time() - self.time_last_read > 2:
            t = threading.Thread(target=self.read_temp)
            t.start()
        return self.c
    
    def read_continuous(self):
        while True:
            self.read_temp()
            print((self.c, self.f))
            time.sleep(1)
